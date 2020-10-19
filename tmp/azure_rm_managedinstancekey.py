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
module: azure_rm_managedinstancekey
version_added: '2.9'
short_description: Manage Azure ManagedInstanceKey instance.
description:
  - 'Create, update and delete instance of Azure ManagedInstanceKey.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  key_name:
    description:
      - The name of the managed instance key to be retrieved.
      - >-
        The name of the managed instance key to be operated on (updated or
        created).
      - The name of the managed instance key to be deleted.
    required: true
    type: str
  server_key_type:
    description:
      - 'The key type like ''ServiceManaged'', ''AzureKeyVault''.'
    type: str
    choices:
      - ServiceManaged
      - AzureKeyVault
  uri:
    description:
      - >-
        The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI
        is required.
    type: str
  state:
    description:
      - Assert the state of the ManagedInstanceKey.
      - >-
        Use C(present) to create or update an ManagedInstanceKey and C(absent)
        to delete it.
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
    - name: Creates or updates a managed instance key
      azure_rm_managedinstancekey: 
        key_name: someVault_someKey_01234567890123456789012345678901
        managed_instance_name: sqlcrudtest-4645
        resource_group_name: sqlcrudtest-7398
        properties:
          server_key_type: AzureKeyVault
          uri: >-
            https://someVault.vault.azure.net/keys/someKey/01234567890123456789012345678901
        

    - name: Delete the managed instance key
      azure_rm_managedinstancekey: 
        key_name: someVault_someKey_01234567890123456789012345678901
        managed_instance_name: sqlcrudtest-4645
        resource_group_name: sqlcrudtest-7398
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
kind:
  description:
    - >-
      Kind of encryption protector. This is metadata used for the Azure portal
      experience.
  returned: always
  type: str
  sample: null
server_key_type:
  description:
    - 'The key type like ''ServiceManaged'', ''AzureKeyVault''.'
  returned: always
  type: str
  sample: null
uri:
  description:
    - >-
      The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is
      required.
  returned: always
  type: str
  sample: null
thumbprint:
  description:
    - Thumbprint of the key.
  returned: always
  type: str
  sample: null
creation_date:
  description:
    - The key creation date.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagedInstanceKey(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            key_name=dict(
                type='str',
                required=True
            ),
            server_key_type=dict(
                type='str',
                disposition='/server_key_type',
                choices=['ServiceManaged',
                         'AzureKeyVault']
            ),
            uri=dict(
                type='str',
                disposition='/uri'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.key_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedInstanceKey, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01-preview')

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
            response = self.mgmt_client.managed_instance_keys.create_or_update(resource_group_name=self.resource_group_name,
                                                                               managed_instance_name=self.managed_instance_name,
                                                                               key_name=self.key_name,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedInstanceKey instance.')
            self.fail('Error creating the ManagedInstanceKey instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_instance_keys.delete(resource_group_name=self.resource_group_name,
                                                                     managed_instance_name=self.managed_instance_name,
                                                                     key_name=self.key_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagedInstanceKey instance.')
            self.fail('Error deleting the ManagedInstanceKey instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_instance_keys.get(resource_group_name=self.resource_group_name,
                                                                  managed_instance_name=self.managed_instance_name,
                                                                  key_name=self.key_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedInstanceKey()


if __name__ == '__main__':
    main()
