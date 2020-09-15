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
module: azure_rm_cache_info
version_added: '2.9'
short_description: Get Cache info.
description:
  - Get info of Cache.
options:
  resource_group_name:
    description:
      - Target resource group.
    type: str
  cache_name:
    description:
      - >-
        Name of Cache. Length of name must be not greater than 80 and chars must
        be in list of [-0-9a-zA-Z_] char class.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Caches_List
      azure_rm_cache_info: 
        {}
        

    - name: Caches_ListByResourceGroup
      azure_rm_cache_info: 
        resource_group_name: scgroup
        

    - name: Caches_Get
      azure_rm_cache_info: 
        cache_name: sc1
        resource_group_name: scgroup
        

'''

RETURN = '''
caches:
  description: >-
    A list of dict results where the key is the name of the Cache and the values
    are the facts for that Cache.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - 'URL to get the next set of Cache list results, if there are any.'
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of Caches.
      returned: always
      type: list
      sample: null
      contains:
        tags:
          description:
            - ARM tags as name/value pairs.
          returned: always
          type: any
          sample: null
        id:
          description:
            - Resource ID of the Cache.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Region name string.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Name of Cache.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Type of the Cache; Microsoft.StorageCache/Cache
          returned: always
          type: str
          sample: null
        name_sku_name:
          description:
            - SKU name for this Cache.
          returned: always
          type: str
          sample: null
        cache_size_gb:
          description:
            - 'The size of this Cache, in GB.'
          returned: always
          type: integer
          sample: null
        health:
          description:
            - Health of the Cache.
          returned: always
          type: dict
          sample: null
          contains:
            state:
              description:
                - List of Cache health states.
              returned: always
              type: str
              sample: null
            status_description:
              description:
                - Describes explanation of state.
              returned: always
              type: str
              sample: null
        mount_addresses:
          description:
            - >-
              Array of IP addresses that can be used by clients mounting this
              Cache.
          returned: always
          type: list
          sample: null
        provisioning_state:
          description:
            - >-
              ARM provisioning state, see
              https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
          returned: always
          type: str
          sample: null
        subnet:
          description:
            - Subnet used for the Cache.
          returned: always
          type: str
          sample: null
        upgrade_status:
          description:
            - Upgrade status of the Cache.
          returned: always
          type: dict
          sample: null
          contains:
            current_firmware_version:
              description:
                - >-
                  Version string of the firmware currently installed on this
                  Cache.
              returned: always
              type: str
              sample: null
            firmware_update_status:
              description:
                - >-
                  True if there is a firmware update ready to install on this
                  Cache. The firmware will automatically be installed after
                  firmwareUpdateDeadline if not triggered earlier via the
                  upgrade operation.
              returned: always
              type: str
              sample: null
            firmware_update_deadline:
              description:
                - >-
                  Time at which the pending firmware update will automatically
                  be installed on the Cache.
              returned: always
              type: str
              sample: null
            last_firmware_update:
              description:
                - Time of the last successful firmware update.
              returned: always
              type: str
              sample: null
            pending_firmware_version:
              description:
                - >-
                  When firmwareUpdateAvailable is true, this field holds the
                  version string for the update.
              returned: always
              type: str
              sample: null
        network_settings:
          description:
            - Specifies network settings of the cache.
          returned: always
          type: dict
          sample: null
          contains:
            mtu:
              description:
                - The IPv4 maximum transmission unit configured for the subnet.
              returned: always
              type: integer
              sample: null
            utility_addresses:
              description:
                - Array of additional IP addresses used by this Cache.
              returned: always
              type: list
              sample: null
        encryption_settings:
          description:
            - Specifies encryption settings of the cache.
          returned: always
          type: dict
          sample: null
          contains:
            key_encryption_key:
              description:
                - Specifies the location of the key encryption key in Key Vault.
              returned: always
              type: dict
              sample: null
              contains:
                key_url:
                  description:
                    - The URL referencing a key encryption key in Key Vault.
                  returned: always
                  type: str
                  sample: null
                source_vault:
                  description:
                    - Describes a resource Id to source Key Vault.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    id:
                      description:
                        - Resource Id.
                      returned: always
                      type: str
                      sample: null
        security_settings:
          description:
            - Specifies security settings of the cache.
          returned: always
          type: dict
          sample: null
          contains:
            root_squash:
              description:
                - root squash of cache property.
              returned: always
              type: bool
              sample: null
        principal_id:
          description:
            - The principal id of the cache.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The tenant id associated with the cache.
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - The type of identity used for the cache
          returned: always
          type: sealed-choice
          sample: null
    tags:
      description:
        - ARM tags as name/value pairs.
      returned: always
      type: any
      sample: null
    id:
      description:
        - Resource ID of the Cache.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Region name string.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of Cache.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the Cache; Microsoft.StorageCache/Cache
      returned: always
      type: str
      sample: null
    name_sku_name:
      description:
        - SKU name for this Cache.
      returned: always
      type: str
      sample: null
    cache_size_gb:
      description:
        - 'The size of this Cache, in GB.'
      returned: always
      type: integer
      sample: null
    health:
      description:
        - Health of the Cache.
      returned: always
      type: dict
      sample: null
      contains:
        state:
          description:
            - List of Cache health states.
          returned: always
          type: str
          sample: null
        status_description:
          description:
            - Describes explanation of state.
          returned: always
          type: str
          sample: null
    mount_addresses:
      description:
        - Array of IP addresses that can be used by clients mounting this Cache.
      returned: always
      type: list
      sample: null
    provisioning_state:
      description:
        - >-
          ARM provisioning state, see
          https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
      returned: always
      type: str
      sample: null
    subnet:
      description:
        - Subnet used for the Cache.
      returned: always
      type: str
      sample: null
    upgrade_status:
      description:
        - Upgrade status of the Cache.
      returned: always
      type: dict
      sample: null
      contains:
        current_firmware_version:
          description:
            - Version string of the firmware currently installed on this Cache.
          returned: always
          type: str
          sample: null
        firmware_update_status:
          description:
            - >-
              True if there is a firmware update ready to install on this Cache.
              The firmware will automatically be installed after
              firmwareUpdateDeadline if not triggered earlier via the upgrade
              operation.
          returned: always
          type: str
          sample: null
        firmware_update_deadline:
          description:
            - >-
              Time at which the pending firmware update will automatically be
              installed on the Cache.
          returned: always
          type: str
          sample: null
        last_firmware_update:
          description:
            - Time of the last successful firmware update.
          returned: always
          type: str
          sample: null
        pending_firmware_version:
          description:
            - >-
              When firmwareUpdateAvailable is true, this field holds the version
              string for the update.
          returned: always
          type: str
          sample: null
    network_settings:
      description:
        - Specifies network settings of the cache.
      returned: always
      type: dict
      sample: null
      contains:
        mtu:
          description:
            - The IPv4 maximum transmission unit configured for the subnet.
          returned: always
          type: integer
          sample: null
        utility_addresses:
          description:
            - Array of additional IP addresses used by this Cache.
          returned: always
          type: list
          sample: null
    encryption_settings:
      description:
        - Specifies encryption settings of the cache.
      returned: always
      type: dict
      sample: null
      contains:
        key_encryption_key:
          description:
            - Specifies the location of the key encryption key in Key Vault.
          returned: always
          type: dict
          sample: null
          contains:
            key_url:
              description:
                - The URL referencing a key encryption key in Key Vault.
              returned: always
              type: str
              sample: null
            source_vault:
              description:
                - Describes a resource Id to source Key Vault.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource Id.
                  returned: always
                  type: str
                  sample: null
    security_settings:
      description:
        - Specifies security settings of the cache.
      returned: always
      type: dict
      sample: null
      contains:
        root_squash:
          description:
            - root squash of cache property.
          returned: always
          type: bool
          sample: null
    principal_id:
      description:
        - The principal id of the cache.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The tenant id associated with the cache.
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - The type of identity used for the cache
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageCacheManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCacheInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            cache_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cache_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCacheInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageCacheManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.cache_name is not None):
            self.results['caches'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['caches'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['caches'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.caches.get(resource_group_name=self.resource_group_name,
                                                   cache_name=self.cache_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.caches.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.caches.list()
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
    AzureRMCacheInfo()


if __name__ == '__main__':
    main()
