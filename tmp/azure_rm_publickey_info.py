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
module: azure_rm_publickey_info
version_added: '2.9'
short_description: Get PublicKey info.
description:
  - Get info of PublicKey.
options:
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
  public_key_name:
    description:
      - Name of the public key.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: PublicKeys_ListByDataManagerGET211
      azure_rm_publickey_info: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: PublicKeys_GetGET222
      azure_rm_publickey_info: 
        data_manager_name: TestAzureSDKOperations
        public_key_name: default
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
public_keys:
  description: >-
    A list of dict results where the key is the name of the PublicKey and the
    values are the facts for that PublicKey.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of public keys.
      returned: always
      type: list
      sample: null
      contains:
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
                  The maximum byte size that can be encrypted by the key. For a
                  key size larger than the size, break into chunks and encrypt
                  each chunk, append each encrypted chunk with : to mark the end
                  of the chunk.
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
                  The maximum byte size that can be encrypted by the key. For a
                  key size larger than the size, break into chunks and encrypt
                  each chunk, append each encrypted chunk with : to mark the end
                  of the chunk.
              returned: always
              type: integer
              sample: null
    next_link:
      description:
        - Link for the next set of public keys.
      returned: always
      type: str
      sample: null
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
              The maximum byte size that can be encrypted by the key. For a key
              size larger than the size, break into chunks and encrypt each
              chunk, append each encrypted chunk with : to mark the end of the
              chunk.
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
              The maximum byte size that can be encrypted by the key. For a key
              size larger than the size, break into chunks and encrypt each
              chunk, append each encrypted chunk with : to mark the end of the
              chunk.
          returned: always
          type: integer
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPublicKeyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            public_key_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.data_manager_name = None
        self.public_key_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPublicKeyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.public_key_name is not None and
            self.resource_group_name is not None and
            self.data_manager_name is not None):
            self.results['public_keys'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.data_manager_name is not None):
            self.results['public_keys'] = self.format_item(self.listbydatamanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.public_keys.get(public_key_name=self.public_key_name,
                                                        resource_group_name=self.resource_group_name,
                                                        data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatamanager(self):
        response = None

        try:
            response = self.mgmt_client.public_keys.list_by_data_manager(resource_group_name=self.resource_group_name,
                                                                         data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
               result.append(tmp.as_dict())
            return result


def main():
    AzureRMPublicKeyInfo()


if __name__ == '__main__':
    main()
