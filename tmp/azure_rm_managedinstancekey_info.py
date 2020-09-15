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
module: azure_rm_managedinstancekey_info
version_added: '2.9'
short_description: Get ManagedInstanceKey info.
description:
  - Get info of ManagedInstanceKey.
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
  filter:
    description:
      - An OData filter expression that filters elements in the collection.
    type: str
  key_name:
    description:
      - The name of the managed instance key to be retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List the keys for a managed instance.
      azure_rm_managedinstancekey_info: 
        managed_instance_name: sqlcrudtest-4645
        resource_group_name: sqlcrudtest-7398
        

    - name: Get the managed instance key
      azure_rm_managedinstancekey_info: 
        key_name: someVault_someKey_01234567890123456789012345678901
        managed_instance_name: sqlcrudtest-4645
        resource_group_name: sqlcrudtest-7398
        

'''

RETURN = '''
managed_instance_keys:
  description: >-
    A list of dict results where the key is the name of the ManagedInstanceKey
    and the values are the facts for that ManagedInstanceKey.
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
        server_key_type:
          description:
            - 'The key type like ''ServiceManaged'', ''AzureKeyVault''.'
          returned: always
          type: str
          sample: null
        uri:
          description:
            - >-
              The URI of the key. If the ServerKeyType is AzureKeyVault, then
              the URI is required.
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
    server_key_type:
      description:
        - 'The key type like ''ServiceManaged'', ''AzureKeyVault''.'
      returned: always
      type: str
      sample: null
    uri:
      description:
        - >-
          The URI of the key. If the ServerKeyType is AzureKeyVault, then the
          URI is required.
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


class AzureRMManagedInstanceKeyInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            key_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.filter = None
        self.key_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-10-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedInstanceKeyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.key_name is not None):
            self.results['managed_instance_keys'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['managed_instance_keys'] = self.format_item(self.listbyinstance())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_keys.get(resource_group_name=self.resource_group_name,
                                                                  managed_instance_name=self.managed_instance_name,
                                                                  key_name=self.key_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstance(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_keys.list_by_instance(resource_group_name=self.resource_group_name,
                                                                               managed_instance_name=self.managed_instance_name,
                                                                               filter=self.filter)
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
    AzureRMManagedInstanceKeyInfo()


if __name__ == '__main__':
    main()
