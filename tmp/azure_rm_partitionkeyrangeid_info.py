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
module: azure_rm_partitionkeyrangeid_info
version_added: '2.9'
short_description: Get PartitionKeyRangeId info.
description:
  - Get info of PartitionKeyRangeId.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    required: true
    type: str
  database_rid:
    description:
      - Cosmos DB database rid.
    required: true
    type: str
  collection_rid:
    description:
      - Cosmos DB collection rid.
    required: true
    type: str
  partition_key_range_id:
    description:
      - Partition Key Range Id for which to get data.
    required: true
    type: str
  filter:
    description:
      - >-
        An OData filter expression that describes a subset of metrics to return.
        The parameters that can be filtered are name.value (name of the metric,
        can have an or of multiple names), startTime, endTime, and timeGrain.
        The supported operator is eq.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CosmosDBDatabaseAccountRegionGetMetrics
      azure_rm_partitionkeyrangeid_info: 
        account_name: ddb1
        collection_rid: collectionRid
        database_rid: databaseRid
        partition_key_range_id: '0'
        resource_group_name: rg1
        

'''

RETURN = '''
partition_key_range_id:
  description: >-
    A list of dict results where the key is the name of the PartitionKeyRangeId
    and the values are the facts for that PartitionKeyRangeId.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of partition-level metrics for the account.
      returned: always
      type: list
      sample: null
      contains:
        partition_id:
          description:
            - The partition id (GUID identifier) of the metric values.
          returned: always
          type: str
          sample: null
        partition_key_range_id:
          description:
            - >-
              The partition key range id (integer identifier) of the metric
              values.
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
    from azure.mgmt.cosmos import CosmosDBManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPartitionKeyRangeIdInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            database_rid=dict(
                type='str',
                required=True
            ),
            collection_rid=dict(
                type='str',
                required=True
            ),
            partition_key_range_id=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.database_rid = None
        self.collection_rid = None
        self.partition_key_range_id = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPartitionKeyRangeIdInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.database_rid is not None and
            self.collection_rid is not None and
            self.partition_key_range_id is not None and
            self.filter is not None):
            self.results['partition_key_range_id'] = self.format_item(self.listmetric())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.partition_key_range_id.list_metric(resource_group_name=self.resource_group_name,
                                                                           account_name=self.account_name,
                                                                           database_rid=self.database_rid,
                                                                           collection_rid=self.collection_rid,
                                                                           partition_key_range_id=self.partition_key_range_id,
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
    AzureRMPartitionKeyRangeIdInfo()


if __name__ == '__main__':
    main()
