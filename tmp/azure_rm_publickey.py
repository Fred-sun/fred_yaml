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
module: azure_rm_publickey
version_added: '2.9'
short_description: Manage Azure PublicKey instance.
description:
  - 'Create, update and delete instance of Azure PublicKey.'
options:
  public_key_name:
    description:
      - Name of the public key.
    required: true
    type: str
  resource_group_name:
    description:
      - The Resource Group Name
    required: true
    type: str
  data_manager_name:
    description:
      - >-
        The name of the DataManager Resource within the specified resource
        group. DataManager names must be between 3 and 24 characters in length
        and use any alphanumeric and underscore only
    required: true
    type: str
  state:
    description:
      - Assert the state of the PublicKey.
      - >-
        Use C(present) to create or update an PublicKey and C(absent) to delete
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
'''

RETURN = '''
name:
  description:
    - Name of the object.
  returned: always
  type: str
  sample: null
id:
  description:
    - Id of the object.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of the object.
  returned: always
  type: str
  sample: null
data_service_level1key:
  description:
    - Level one public key for encryption
  returned: always
  type: dict
  sample: null
  contains:
    key_modulus:
      description:
        - Modulus of the encryption key.
      returned: always
      type: str
      sample: null
    key_exponent:
      description:
        - Exponent of the encryption key.
      returned: always
      type: str
      sample: null
    encryption_chunk_size_in_bytes:
      description:
        - >-
          The maximum byte size that can be encrypted by the key. For a key size
          larger than the size, break into chunks and encrypt each chunk, append
          each encrypted chunk with : to mark the end of the chunk.
      returned: always
      type: integer
      sample: null
data_service_level2key:
  description:
    - Level two public key for encryption
  returned: always
  type: dict
  sample: null
  contains:
    key_modulus:
      description:
        - Modulus of the encryption key.
      returned: always
      type: str
      sample: null
    key_exponent:
      description:
        - Exponent of the encryption key.
      returned: always
      type: str
      sample: null
    encryption_chunk_size_in_bytes:
      description:
        - >-
          The maximum byte size that can be encrypted by the key. For a key size
          larger than the size, break into chunks and encrypt each chunk, append
          each encrypted chunk with : to mark the end of the chunk.
      returned: always
      type: integer
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPublicKey(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            public_key_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.public_key_name = None
        self.resource_group_name = None
        self.data_manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPublicKey, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

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
                response = self.mgmt_client.public_keys.create()
            else:
                response = self.mgmt_client.public_keys.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PublicKey instance.')
            self.fail('Error creating the PublicKey instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.public_keys.delete()
        except CloudError as e:
            self.log('Error attempting to delete the PublicKey instance.')
            self.fail('Error deleting the PublicKey instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.public_keys.get(public_key_name=self.public_key_name,
                                                        resource_group_name=self.resource_group_name,
                                                        data_manager_name=self.data_manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPublicKey()


if __name__ == '__main__':
    main()
