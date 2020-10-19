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
module: azure_rm_cache
version_added: '2.9'
short_description: Manage Azure Cache instance.
description:
  - 'Create, update and delete instance of Azure Cache.'
options:
  resource_group_name:
    description:
      - Target resource group.
    required: true
    type: str
  cache_name:
    description:
      - >-
        Name of Cache. Length of name must be not greater than 80 and chars must
        be in list of [-0-9a-zA-Z_] char class.
    required: true
    type: str
  location:
    description:
      - Region name string.
    type: str
  name:
    description:
      - SKU name for this Cache.
    type: str
  cache_size_gb:
    description:
      - 'The size of this Cache, in GB.'
    type: integer
  provisioning_state:
    description:
      - >-
        ARM provisioning state, see
        https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
    type: str
    choices:
      - Succeeded
      - Failed
      - Cancelled
      - Creating
      - Deleting
      - Updating
  subnet:
    description:
      - Subnet used for the Cache.
    type: str
  network_settings:
    description:
      - Specifies network settings of the cache.
    type: dict
    suboptions:
      mtu:
        description:
          - The IPv4 maximum transmission unit configured for the subnet.
        type: integer
      utility_addresses:
        description:
          - Array of additional IP addresses used by this Cache.
        type: list
  encryption_settings:
    description:
      - Specifies encryption settings of the cache.
    type: dict
    suboptions:
      key_encryption_key:
        description:
          - Specifies the location of the key encryption key in Key Vault.
        type: dict
        suboptions:
          key_url:
            description:
              - The URL referencing a key encryption key in Key Vault.
            required: true
            type: str
          source_vault:
            description:
              - Describes a resource Id to source Key Vault.
            required: true
            type: dict
            suboptions:
              id:
                description:
                  - Resource Id.
                type: str
  security_settings:
    description:
      - Specifies security settings of the cache.
    type: dict
    suboptions:
      root_squash:
        description:
          - root squash of cache property.
        type: bool
  type:
    description:
      - The type of identity used for the cache
    type: sealed-choice
  state:
    description:
      - Assert the state of the Cache.
      - Use C(present) to create or update an Cache and C(absent) to delete it.
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
    - name: Caches_Delete
      azure_rm_cache: 
        cache_name: sc
        resource_group_name: scgroup
        

    - name: Caches_CreateOrUpdate
      azure_rm_cache: 
        cache_name: sc1
        resource_group_name: scgroup
        location: westus
        properties:
          cache_size_gb: 3072
          subnet: >-
            /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1
        sku:
          name: Standard_2G
        tags:
          dept: ContosoAds
        

    - name: Caches_Update
      azure_rm_cache: 
        cache_name: sc1
        resource_group_name: scgroup
        location: westus
        properties:
          cache_size_gb: 3072
          subnet: >-
            /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1
        sku:
          name: Standard_2G
        tags:
          dept: ContosoAds
        

'''

RETURN = '''
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
          True if there is a firmware update ready to install on this Cache. The
          firmware will automatically be installed after firmwareUpdateDeadline
          if not triggered earlier via the upgrade operation.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageCacheManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCache(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cache_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            cache_size_gb=dict(
                type='integer',
                disposition='/cache_size_gb'
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state',
                choices=['Succeeded',
                         'Failed',
                         'Cancelled',
                         'Creating',
                         'Deleting',
                         'Updating']
            ),
            subnet=dict(
                type='str',
                disposition='/subnet'
            ),
            network_settings=dict(
                type='dict',
                disposition='/network_settings',
                options=dict(
                    mtu=dict(
                        type='integer',
                        disposition='mtu'
                    ),
                    utility_addresses=dict(
                        type='list',
                        updatable=False,
                        disposition='utility_addresses',
                        elements='str'
                    )
                )
            ),
            encryption_settings=dict(
                type='dict',
                disposition='/encryption_settings',
                options=dict(
                    key_encryption_key=dict(
                        type='dict',
                        disposition='key_encryption_key',
                        options=dict(
                            key_url=dict(
                                type='str',
                                disposition='key_url',
                                required=True
                            ),
                            source_vault=dict(
                                type='dict',
                                disposition='source_vault',
                                required=True,
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            security_settings=dict(
                type='dict',
                disposition='/security_settings',
                options=dict(
                    root_squash=dict(
                        type='bool',
                        disposition='root_squash'
                    )
                )
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.cache_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCache, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorageCacheManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

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
            response = self.mgmt_client.caches.create_or_update(resource_group_name=self.resource_group_name,
                                                                cache_name=self.cache_name,
                                                                cache=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Cache instance.')
            self.fail('Error creating the Cache instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.caches.delete(resource_group_name=self.resource_group_name,
                                                      cache_name=self.cache_name)
        except CloudError as e:
            self.log('Error attempting to delete the Cache instance.')
            self.fail('Error deleting the Cache instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.caches.get(resource_group_name=self.resource_group_name,
                                                   cache_name=self.cache_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCache()


if __name__ == '__main__':
    main()
