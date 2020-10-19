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
module: azure_rm_encryptionprotector_info
version_added: '2.9'
short_description: Get EncryptionProtector info.
description:
  - Get info of EncryptionProtector.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  encryption_protector_name:
    description:
      - The name of the encryption protector to be retrieved.
    type: str
    choices:
      - current
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List encryption protectors by server
      azure_rm_encryptionprotector_info: 
        resource_group_name: sqlcrudtest-7398
        server_name: sqlcrudtest-4645
        

    - name: Get the encryption protector
      azure_rm_encryptionprotector_info: 
        encryption_protector_name: current
        resource_group_name: sqlcrudtest-7398
        server_name: sqlcrudtest-4645
        

'''

RETURN = '''
encryption_protectors:
  description: >-
    A list of dict results where the key is the name of the EncryptionProtector
    and the values are the facts for that EncryptionProtector.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - >-
              Kind of encryption protector. This is metadata used for the Azure
              portal experience.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        subregion:
          description:
            - Subregion of the encryption protector.
          returned: always
          type: str
          sample: null
        server_key_name:
          description:
            - The name of the server key.
          returned: always
          type: str
          sample: null
        server_key_type:
          description:
            - >-
              The encryption protector type like 'ServiceManaged',
              'AzureKeyVault'.
          returned: always
          type: str
          sample: null
        uri:
          description:
            - The URI of the server key.
          returned: always
          type: str
          sample: null
        thumbprint:
          description:
            - Thumbprint of the server key.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
          Kind of encryption protector. This is metadata used for the Azure
          portal experience.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    subregion:
      description:
        - Subregion of the encryption protector.
      returned: always
      type: str
      sample: null
    server_key_name:
      description:
        - The name of the server key.
      returned: always
      type: str
      sample: null
    server_key_type:
      description:
        - 'The encryption protector type like ''ServiceManaged'', ''AzureKeyVault''.'
      returned: always
      type: str
      sample: null
    uri:
      description:
        - The URI of the server key.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - Thumbprint of the server key.
      returned: always
      type: str
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEncryptionProtectorInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            encryption_protector_name=dict(
                type='str',
                choices=['current']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.encryption_protector_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEncryptionProtectorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.encryption_protector_name is not None):
            self.results['encryption_protectors'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['encryption_protectors'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.encryption_protectors.get(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  encryption_protector_name=self.encryption_protector_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.encryption_protectors.list_by_server(resource_group_name=self.resource_group_name,
                                                                             server_name=self.server_name)
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
    AzureRMEncryptionProtectorInfo()


if __name__ == '__main__':
    main()
