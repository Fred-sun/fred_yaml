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
module: azure_rm_servicerunner
version_added: '2.9'
short_description: Manage Azure ServiceRunner instance.
description:
  - 'Create, update and delete instance of Azure ServiceRunner.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  name:
    description:
      - The name of the service runner.
    required: true
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  identity:
    description:
      - The identity of the resource.
    type: dict
    suboptions:
      type:
        description:
          - Managed identity.
        type: str
      principal_id:
        description:
          - The principal id of resource identity.
        type: str
      tenant_id:
        description:
          - The tenant identifier of resource.
        type: str
      client_secret_url:
        description:
          - The client secret URL of the identity.
        type: str
  state:
    description:
      - Assert the state of the ServiceRunner.
      - >-
        Use C(present) to create or update an ServiceRunner and C(absent) to
        delete it.
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
'''

RETURN = '''
id:
  description:
    - The identifier of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
identity:
  description:
    - The identity of the resource.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - Managed identity.
      returned: always
      type: str
      sample: null
    principal_id:
      description:
        - The principal id of resource identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The tenant identifier of resource.
      returned: always
      type: str
      sample: null
    client_secret_url:
      description:
        - The client secret URL of the identity.
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMServiceRunner(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type'
                    ),
                    principal_id=dict(
                        type='str',
                        disposition='principal_id'
                    ),
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id'
                    ),
                    client_secret_url=dict(
                        type='str',
                        disposition='client_secret_url'
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
        self.lab_name = None
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServiceRunner, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.service_runners.create_or_update(resource_group_name=self.resource_group_name,
                                                                         lab_name=self.lab_name,
                                                                         name=self.name,
                                                                         service_runner=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ServiceRunner instance.')
            self.fail('Error creating the ServiceRunner instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.service_runners.delete(resource_group_name=self.resource_group_name,
                                                               lab_name=self.lab_name,
                                                               name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ServiceRunner instance.')
            self.fail('Error deleting the ServiceRunner instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.service_runners.get(resource_group_name=self.resource_group_name,
                                                            lab_name=self.lab_name,
                                                            name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServiceRunner()


if __name__ == '__main__':
    main()
