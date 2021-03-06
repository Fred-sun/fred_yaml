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
module: azure_rm_extension
version_added: '2.9'
short_description: Manage Azure Extension instance.
description:
  - 'Create, update and delete instance of Azure Extension.'
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    required: true
    type: str
  account_resource_name:
    description:
      - The name of the Visual Studio Team Services account resource.
    required: true
    type: str
  extension_resource_name:
    description:
      - The name of the extension.
    required: true
    type: str
  location:
    description:
      - >-
        The Azure region of the Visual Studio account associated with this
        request (i.e 'southcentralus'.)
    type: str
  plan:
    description:
      - >-
        Extended information about the plan being purchased for this extension
        resource.
    type: dict
    suboptions:
      name:
        description:
          - Name of the plan.
        type: str
      product:
        description:
          - Product name.
        type: str
      promotion_code:
        description:
          - 'Optional: the promotion code associated with the plan.'
        type: str
      publisher:
        description:
          - Name of the extension publisher.
        type: str
      version:
        description:
          - A string that uniquely identifies the plan version.
        type: str
  properties:
    description:
      - A dictionary of extended properties. This property is currently unused.
    type: dictionary
  state:
    description:
      - Assert the state of the Extension.
      - >-
        Use C(present) to create or update an Extension and C(absent) to delete
        it.
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
    - name: Create an extension resource
      azure_rm_extension: 
        account_resource_name: ExampleAccount
        extension_resource_name: ms.example
        resource_group_name: VS-Example-Group
        location: Central US
        plan:
          name: ExamplePlan
          product: ExampleExtensionName
          promotion_code: ''
          publisher: ExampleExtensionPublisher
          version: '1.0'
        properties: {}
        tags: {}
        

    - name: Delete an extension resource
      azure_rm_extension: 
        account_resource_name: Example
        extension_resource_name: ms.example
        resource_group_name: VS-Example-Group
        

    - name: Update an extension resource
      azure_rm_extension: 
        account_resource_name: ExampleAccount
        extension_resource_name: Example
        resource_group_name: VS-Example-Group
        location: Central US
        plan:
          name: ExamplePlan
          product: ExampleExtensionName
          promotion_code: ''
          publisher: ExampleExtensionPublisher
          version: '1.0'
        properties: {}
        tags: {}
        

'''

RETURN = '''
id:
  description:
    - Unique identifier of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
plan:
  description:
    - The extension plan that was purchased.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of the plan.
      returned: always
      type: str
      sample: null
    product:
      description:
        - Product name.
      returned: always
      type: str
      sample: null
    promotion_code:
      description:
        - 'Optional: the promotion code associated with the plan.'
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - Name of the extension publisher.
      returned: always
      type: str
      sample: null
    version:
      description:
        - A string that uniquely identifies the plan version.
      returned: always
      type: str
      sample: null
properties:
  description:
    - Resource properties.
  returned: always
  type: dictionary
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.visual import Visual Studio Resource Provider Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMExtension(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_resource_name=dict(
                type='str',
                required=True
            ),
            extension_resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            plan=dict(
                type='dict',
                disposition='/plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    product=dict(
                        type='str',
                        disposition='product'
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='promotion_code'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    version=dict(
                        type='str',
                        disposition='version'
                    )
                )
            ),
            properties=dict(
                type='dictionary',
                disposition='/properties'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_resource_name = None
        self.extension_resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExtension, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Visual Studio Resource Provider Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.extensions.create(resource_group_name=self.resource_group_name,
                                                              account_resource_name=self.account_resource_name,
                                                              extension_resource_name=self.extension_resource_name,
                                                              body=self.body)
            else:
                response = self.mgmt_client.extensions.update(resource_group_name=self.resource_group_name,
                                                              account_resource_name=self.account_resource_name,
                                                              extension_resource_name=self.extension_resource_name,
                                                              body=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Extension instance.')
            self.fail('Error creating the Extension instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.extensions.delete(resource_group_name=self.resource_group_name,
                                                          account_resource_name=self.account_resource_name,
                                                          extension_resource_name=self.extension_resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Extension instance.')
            self.fail('Error deleting the Extension instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.extensions.get(resource_group_name=self.resource_group_name,
                                                       account_resource_name=self.account_resource_name,
                                                       extension_resource_name=self.extension_resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMExtension()


if __name__ == '__main__':
    main()
