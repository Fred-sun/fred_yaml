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
module: azure_rm_redi_info
version_added: '2.9'
short_description: Get Redi info.
description:
  - Get info of Redi.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  name:
    description:
      - The name of the Redis cache.
    type: str
  history:
    description:
      - how many minutes in past to look for upgrade notifications
    type: number
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RedisCacheGet
      azure_rm_redi_info: 
        name: cache1
        history: '5000'
        resource_group_name: rg1
        

    - name: RedisCacheListByResourceGroup
      azure_rm_redi_info: 
        resource_group_name: rg1
        

    - name: RedisCacheList
      azure_rm_redi_info: 
        {}
        

'''

RETURN = '''
redis:
  description: >-
    A list of dict results where the key is the name of the Redi and the values
    are the facts for that Redi.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          List of all notifications.
          List of Redis cache instances.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of upgrade notification.
          returned: always
          type: str
          sample: null
        timestamp:
          description:
            - Timestamp when upgrade notification occurred.
          returned: always
          type: str
          sample: null
        upsell_notification:
          description:
            - Details about this upgrade notification
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - |-
          Link for next set of notifications.
          Link for next page of results.
      returned: always
      type: str
      sample: null
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
          Optional: requires clients to use a specified TLS version (or higher)
          to connect (e,g, '1.0', '1.1', '1.2')
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
              The SKU family to use. Valid values: (C, P). (C = Basic/Standard,
              P = Premium).
          returned: always
          type: str
          sample: null
        capacity:
          description:
            - >-
              The size of the Redis cache to deploy. Valid values: for C
              (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium)
              family (1, 2, 3, 4, 5).
          returned: always
          type: integer
          sample: null
    subnet_id:
      description:
        - >-
          The full resource ID of a subnet in a virtual network to deploy the
          Redis cache in. Example format:
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
          The keys of the Redis cache - not set if this object is not the
          response to Create or Update redis cache
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
              The current secondary key that clients can use to authenticate
              with Redis cache.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.redis import RedisManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRediInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            history=dict(
                type='number'
            )
        )

        self.resource_group_name = None
        self.name = None
        self.history = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRediInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RedisManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01')

        if (self.resource_group_name is not None and
            self.name is not None and
            self.history is not None):
            self.results['redis'] = self.format_item(self.listupgradenotification())
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['redis'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['redis'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['redis'] = self.format_item(self.list())
        return self.results

    def listupgradenotification(self):
        response = None

        try:
            response = self.mgmt_client.redis.list_upgrade_notification(resource_group_name=self.resource_group_name,
                                                                        name=self.name,
                                                                        history=self.history)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.redis.get(resource_group_name=self.resource_group_name,
                                                  name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.redis.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.redis.list()
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
    AzureRMRediInfo()


if __name__ == '__main__':
    main()
