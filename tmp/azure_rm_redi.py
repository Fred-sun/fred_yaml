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
module: azure_rm_redi
version_added: '2.9'
short_description: Manage Azure Redi instance.
description:
  - 'Create, update and delete instance of Azure Redi.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The name of the Redis cache.
    required: true
    type: str
  zones:
    description:
      - >-
        A list of availability zones denoting where the resource needs to come
        from.
    type: list
  location:
    description:
      - The geo-location where the resource lives
    type: str
  redis_configuration:
    description:
      - >-
        All Redis Settings. Few possible keys:
        rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value
        etc.
    type: dictionary
  enable_non_sslport:
    description:
      - Specifies whether the non-ssl Redis server port (6379) is enabled.
    type: bool
  replicas_per_master:
    description:
      - The number of replicas to be created per master.
    type: integer
  tenant_settings:
    description:
      - A dictionary of tenant settings
    type: dictionary
  shard_count:
    description:
      - The number of shards to be created on a Premium Cluster Cache.
    type: integer
  minimum_tls_version:
    description:
      - >-
        Optional: requires clients to use a specified TLS version (or higher) to
        connect (e,g, '1.0', '1.1', '1.2')
    type: str
    choices:
      - '1.0'
      - '1.1'
      - '1.2'
  sku:
    description:
      - The SKU of the Redis cache to deploy.
    type: dict
    suboptions:
      name:
        description:
          - >-
            The type of Redis cache to deploy. Valid values: (Basic, Standard,
            Premium)
        required: true
        type: str
        choices:
          - Basic
          - Standard
          - Premium
      family:
        description:
          - >-
            The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P
            = Premium).
        required: true
        type: str
        choices:
          - C
          - P
      capacity:
        description:
          - >-
            The size of the Redis cache to deploy. Valid values: for C
            (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium)
            family (1, 2, 3, 4, 5).
        required: true
        type: integer
  subnet_id:
    description:
      - >-
        The full resource ID of a subnet in a virtual network to deploy the
        Redis cache in. Example format:
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1
    type: str
  static_ip:
    description:
      - >-
        Static IP address. Required when deploying a Redis cache inside an
        existing Azure Virtual Network.
    type: str
  state:
    description:
      - Assert the state of the Redi.
      - Use C(present) to create or update an Redi and C(absent) to delete it.
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
    - name: RedisCacheCreate
      azure_rm_redi: 
        name: cache1
        resource_group_name: rg1
        location: West US
        properties:
          enable_non_ssl_port: true
          minimum_tls_version: '1.2'
          redis_configuration:
            maxmemory-policy: allkeys-lru
          replicas_per_master: 2
          shard_count: 2
          sku:
            name: Premium
            capacity: 1
            family: P
          static_ip: 192.168.0.5
          subnet_id: >-
            /subscriptions/subid/resourceGroups/rg2/providers/Microsoft.Network/virtualNetworks/network1/subnets/subnet1
        zones:
          - '1'
        

    - name: RedisCacheUpdate
      azure_rm_redi: 
        name: cache1
        resource_group_name: rg1
        properties:
          enable_non_ssl_port: true
        

    - name: RedisCacheDelete
      azure_rm_redi: 
        name: cache1
        resource_group_name: rg1
        

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
zones:
  description:
    - >-
      A list of availability zones denoting where the resource needs to come
      from.
  returned: always
  type: list
  sample: null
redis_configuration:
  description:
    - >-
      All Redis Settings. Few possible keys:
      rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value
      etc.
  returned: always
  type: dictionary
  sample: null
enable_non_sslport:
  description:
    - Specifies whether the non-ssl Redis server port (6379) is enabled.
  returned: always
  type: bool
  sample: null
replicas_per_master:
  description:
    - The number of replicas to be created per master.
  returned: always
  type: integer
  sample: null
tenant_settings:
  description:
    - A dictionary of tenant settings
  returned: always
  type: dictionary
  sample: null
shard_count:
  description:
    - The number of shards to be created on a Premium Cluster Cache.
  returned: always
  type: integer
  sample: null
minimum_tls_version:
  description:
    - >-
      Optional: requires clients to use a specified TLS version (or higher) to
      connect (e,g, '1.0', '1.1', '1.2')
  returned: always
  type: str
  sample: null
sku:
  description:
    - The SKU of the Redis cache to deploy.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - >-
          The type of Redis cache to deploy. Valid values: (Basic, Standard,
          Premium)
      returned: always
      type: str
      sample: null
    family:
      description:
        - >-
          The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P =
          Premium).
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - >-
          The size of the Redis cache to deploy. Valid values: for C
          (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family
          (1, 2, 3, 4, 5).
      returned: always
      type: integer
      sample: null
subnet_id:
  description:
    - >-
      The full resource ID of a subnet in a virtual network to deploy the Redis
      cache in. Example format:
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1
  returned: always
  type: str
  sample: null
static_ip:
  description:
    - >-
      Static IP address. Required when deploying a Redis cache inside an
      existing Azure Virtual Network.
  returned: always
  type: str
  sample: null
redis_version:
  description:
    - Redis version.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Redis instance provisioning status.
  returned: always
  type: str
  sample: null
host_name:
  description:
    - Redis host name.
  returned: always
  type: str
  sample: null
port:
  description:
    - Redis non-SSL port.
  returned: always
  type: integer
  sample: null
sslport:
  description:
    - Redis SSL port.
  returned: always
  type: integer
  sample: null
access_keys:
  description:
    - >-
      The keys of the Redis cache - not set if this object is not the response
      to Create or Update redis cache
  returned: always
  type: dict
  sample: null
  contains:
    primary_key:
      description:
        - >-
          The current primary key that clients can use to authenticate with
          Redis cache.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - >-
          The current secondary key that clients can use to authenticate with
          Redis cache.
      returned: always
      type: str
      sample: null
linked_servers:
  description:
    - List of the linked servers associated with the cache
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - Linked server Id.
      returned: always
      type: str
      sample: null
instances:
  description:
    - List of the Redis instances associated with the cache
  returned: always
  type: list
  sample: null
  contains:
    sslport:
      description:
        - Redis instance SSL port.
      returned: always
      type: integer
      sample: null
    non_sslport:
      description:
        - 'If enableNonSslPort is true, provides Redis instance Non-SSL port.'
      returned: always
      type: integer
      sample: null
    zone:
      description:
        - >-
          If the Cache uses availability zones, specifies availability zone
          where this instance is located.
      returned: always
      type: str
      sample: null
    shard_id:
      description:
        - 'If clustering is enabled, the Shard ID of Redis Instance'
      returned: always
      type: integer
      sample: null
    is_master:
      description:
        - Specifies whether the instance is a master node.
      returned: always
      type: bool
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.redis import RedisManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRedi(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            redis_configuration=dict(
                type='dictionary',
                disposition='/redis_configuration'
            ),
            enable_non_sslport=dict(
                type='bool',
                disposition='/enable_non_sslport'
            ),
            replicas_per_master=dict(
                type='integer',
                disposition='/replicas_per_master'
            ),
            tenant_settings=dict(
                type='dictionary',
                disposition='/tenant_settings'
            ),
            shard_count=dict(
                type='integer',
                disposition='/shard_count'
            ),
            minimum_tls_version=dict(
                type='str',
                disposition='/minimum_tls_version',
                choices=['1.0',
                         '1.1',
                         '1.2']
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['Basic',
                                 'Standard',
                                 'Premium'],
                        required=True
                    ),
                    family=dict(
                        type='str',
                        disposition='family',
                        choices=['C',
                                 'P'],
                        required=True
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity',
                        required=True
                    )
                )
            ),
            subnet_id=dict(
                type='str',
                disposition='/subnet_id'
            ),
            static_ip=dict(
                type='str',
                disposition='/static_ip'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRedi, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(RedisManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01')

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
                response = self.mgmt_client.redis.create(resource_group_name=self.resource_group_name,
                                                         name=self.name,
                                                         parameters=self.body)
            else:
                response = self.mgmt_client.redis.update(resource_group_name=self.resource_group_name,
                                                         name=self.name,
                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Redi instance.')
            self.fail('Error creating the Redi instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.redis.delete(resource_group_name=self.resource_group_name,
                                                     name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Redi instance.')
            self.fail('Error deleting the Redi instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.redis.get(resource_group_name=self.resource_group_name,
                                                  name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRedi()


if __name__ == '__main__':
    main()
