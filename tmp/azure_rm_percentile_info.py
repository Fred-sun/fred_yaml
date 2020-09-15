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
module: azure_rm_percentile_info
version_added: '2.9'
short_description: Get Percentile info.
description:
  - Get info of Percentile.
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
      azure_rm_percentile_info: 
        account_name: ddb1
        resource_group_name: rg1
        

'''

RETURN = '''
percentile:
  description: >-
    A list of dict results where the key is the name of the Percentile and the
    values are the facts for that Percentile.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of percentile metrics for the account.
      returned: always
      type: list
      sample: null
      contains:
        start_time:
          description:
            - The start time for the metric (ISO-8601 format).
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The end time for the metric (ISO-8601 format).
          returned: always
          type: str
          sample: null
        time_grain:
          description:
            - The time grain to be used to summarize the metric values.
          returned: always
          type: str
          sample: null
        unit:
          description:
            - The unit of the metric.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name information for the metric.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - The name of the metric.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - The friendly name of the metric.
              returned: always
              type: str
              sample: null
        metric_values:
          description:
            - >-
              The percentile metric values for the specified time window and
              timestep.
          returned: always
          type: list
          sample: null
          contains:
            p10:
              description:
                - The 10th percentile value for the metric.
              returned: always
              type: number
              sample: null
            p25:
              description:
                - The 25th percentile value for the metric.
              returned: always
              type: number
              sample: null
            p50:
              description:
                - The 50th percentile value for the metric.
              returned: always
              type: number
              sample: null
            p75:
              description:
                - The 75th percentile value for the metric.
              returned: always
              type: number
              sample: null
            p90:
              description:
                - The 90th percentile value for the metric.
              returned: always
              type: number
              sample: null
            p95:
              description:
                - The 95th percentile value for the metric.
              returned: always
              type: number
              sample: null
            p99:
              description:
                - The 99th percentile value for the metric.
              returned: always
              type: number
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


class AzureRMPercentileInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.account_name = None
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
        super(AzureRMPercentileInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.filter is not None):
            self.results['percentile'] = self.format_item(self.listmetric())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.percentile.list_metric(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
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
    AzureRMPercentileInfo()


if __name__ == '__main__':
    main()
