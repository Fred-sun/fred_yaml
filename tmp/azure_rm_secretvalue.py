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
module: azure_rm_secretvalue
version_added: '2.9'
short_description: Manage Azure SecretValue instance.
description:
  - 'Create, update and delete instance of Azure SecretValue.'
options:
  resource_group_name:
    description:
      - Azure resource group name
    required: true
    type: str
  secret_resource_name:
    description:
      - The name of the secret resource.
    required: true
    type: str
  secret_value_resource_name:
    description:
      - >-
        The name of the secret resource value which is typically the version
        identifier for the value.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  value:
    description:
      - The actual value of the secret.
    type: str
  state:
    description:
      - Assert the state of the SecretValue.
      - >-
        Use C(present) to create or update an SecretValue and C(absent) to
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
    - name: CreateSecretValue
      azure_rm_secretvalue: 
        resource_group_name: sbz_demo
        secret_resource_name: dbConnectionString
        secret_value_resource_name: v1
        

    - name: DeleteSecretValue
      azure_rm_secretvalue: 
        resource_group_name: sbz_demo
        secret_resource_name: dbConnectionString
        secret_value_resource_name: v1
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - State of the resource.
  returned: always
  type: str
  sample: null
value:
  description:
    - The actual value of the secret.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSecretValue(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            secret_resource_name=dict(
                type='str',
                required=True
            ),
            secret_value_resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            value=dict(
                type='str',
                disposition='/value'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.secret_resource_name = None
        self.secret_value_resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSecretValue, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.secret_value.create(resource_group_name=self.resource_group_name,
                                                                secret_resource_name=self.secret_resource_name,
                                                                secret_value_resource_name=self.secret_value_resource_name,
                                                                secret_value_resource_description=self.body)
            else:
                response = self.mgmt_client.secret_value.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SecretValue instance.')
            self.fail('Error creating the SecretValue instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.secret_value.delete(resource_group_name=self.resource_group_name,
                                                            secret_resource_name=self.secret_resource_name,
                                                            secret_value_resource_name=self.secret_value_resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the SecretValue instance.')
            self.fail('Error deleting the SecretValue instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.secret_value.get(resource_group_name=self.resource_group_name,
                                                         secret_resource_name=self.secret_resource_name,
                                                         secret_value_resource_name=self.secret_value_resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSecretValue()


if __name__ == '__main__':
    main()
