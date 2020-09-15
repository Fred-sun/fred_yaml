#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_customresourceprovider
version_added: '2.9'
short_description: Manage Azure CustomResourceProvider instance.
description:
  - 'Create, update and delete instance of Azure CustomResourceProvider.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  resource_provider_name:
    description:
      - The name of the resource provider.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  actions:
    description:
      - A list of actions that the custom resource provider implements.
    type: list
    suboptions:
      routing_type:
        description:
          - The routing types that are supported for action requests.
        type: str
        choices:
          - Proxy
  resource_types:
    description:
      - A list of resource types that the custom resource provider implements.
    type: list
    suboptions:
      routing_type:
        description:
          - The routing types that are supported for resource requests.
        type: str
        choices:
          - Proxy
          - 'Proxy,Cache'
  validations:
    description:
      - A list of validations to run on the custom resource provider's requests.
    type: list
    suboptions:
      validation_type:
        description:
          - The type of validation to run against a matching request.
        type: str
        choices:
          - Swagger
      specification:
        description:
          - >-
            A link to the validation specification. The specification must be
            hosted on raw.githubusercontent.com.
        required: true
        type: str
  state:
    description:
      - Assert the state of the CustomResourceProvider.
      - >-
        Use C(present) to create or update an CustomResourceProvider and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create or update the custom resource provider
      azure_rm_customresourceprovider: 
        resource_group_name: testRG
        resource_provider_name: newrp
        

    - name: Delete a custom resource provider
      azure_rm_customresourceprovider: 
        resource_group_name: testRG
        resource_provider_name: newrp
        

    - name: Update a custom resource provider
      azure_rm_customresourceprovider: 
        resource_group_name: testRG
        resource_provider_name: newrp
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
actions:
  description:
    - A list of actions that the custom resource provider implements.
  returned: always
  type: list
  sample: null
  contains:
    routing_type:
      description:
        - The routing types that are supported for action requests.
      returned: always
      type: str
      sample: null
resource_types:
  description:
    - A list of resource types that the custom resource provider implements.
  returned: always
  type: list
  sample: null
  contains:
    routing_type:
      description:
        - The routing types that are supported for resource requests.
      returned: always
      type: str
      sample: null
validations:
  description:
    - A list of validations to run on the custom resource provider's requests.
  returned: always
  type: list
  sample: null
  contains:
    validation_type:
      description:
        - The type of validation to run against a matching request.
      returned: always
      type: str
      sample: null
    specification:
      description:
        - >-
          A link to the validation specification. The specification must be
          hosted on raw.githubusercontent.com.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - The provisioning state of the resource provider.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.customproviders import customproviders
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCustomResourceProvider(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_provider_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            actions=dict(
                type='list',
                disposition='/actions',
                elements='dict',
                options=dict(
                    routing_type=dict(
                        type='str',
                        disposition='routing_type',
                        choices=['Proxy']
                    )
                )
            ),
            resource_types=dict(
                type='list',
                disposition='/resource_types',
                elements='dict',
                options=dict(
                    routing_type=dict(
                        type='str',
                        disposition='routing_type',
                        choices=['Proxy',
                                 'Proxy,Cache']
                    )
                )
            ),
            validations=dict(
                type='list',
                disposition='/validations',
                elements='dict',
                options=dict(
                    validation_type=dict(
                        type='str',
                        disposition='validation_type',
                        choices=['Swagger']
                    ),
                    specification=dict(
                        type='str',
                        disposition='specification',
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_provider_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCustomResourceProvider, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                            supports_check_mode=True,
                                                            supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(customproviders,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.custom_resource_provider.create_or_update(resource_group_name=self.resource_group_name,
                                                                                  resource_provider_name=self.resource_provider_name,
                                                                                  resource_provider=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the CustomResourceProvider instance.')
            self.fail('Error creating the CustomResourceProvider instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.custom_resource_provider.delete(resource_group_name=self.resource_group_name,
                                                                        resource_provider_name=self.resource_provider_name)
        except CloudError as e:
            self.log('Error attempting to delete the CustomResourceProvider instance.')
            self.fail('Error deleting the CustomResourceProvider instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.custom_resource_provider.get(resource_group_name=self.resource_group_name,
                                                                     resource_provider_name=self.resource_provider_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCustomResourceProvider()


if __name__ == '__main__':
    main()
