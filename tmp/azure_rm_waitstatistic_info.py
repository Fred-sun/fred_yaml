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
module: azure_rm_waitstatistic_info
version_added: '2.9'
short_description: Get WaitStatistic info.
description:
  - Get info of WaitStatistic.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  wait_statistics_id:
    description:
      - The Wait Statistic identifier.
    type: str
  observation_start_time:
    description:
      - Observation start time.
    type: str
  observation_end_time:
    description:
      - Observation end time.
    type: str
  aggregation_window:
    description:
      - Aggregation interval type in ISO 8601 format.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: WaitStatisticsGet
      azure_rm_waitstatistic_info: 
        resource_group_name: testResourceGroupName
        server_name: testServerName
        wait_statistics_id: >-
          636927606000000000-636927615000000000-send-wait/io/socket/sql/client_connection-2--0
        

    - name: WaitStatisticsListByServer
      azure_rm_waitstatistic_info: 
        resource_group_name: testResourceGroupName
        server_name: testServerName
        properties:
          aggregation_window: PT15M
          observation_end_time: '2019-05-07T20:00:00.000Z'
          observation_start_time: '2019-05-01T20:00:00.000Z'
        

'''

RETURN = '''
wait_statistics:
  description: >-
    A list of dict results where the key is the name of the WaitStatistic and
    the values are the facts for that WaitStatistic.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - Observation start time.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - Observation end time.
      returned: always
      type: str
      sample: null
    event_name:
      description:
        - Wait event name.
      returned: always
      type: str
      sample: null
    event_type_name:
      description:
        - Wait event type name.
      returned: always
      type: str
      sample: null
    query_id:
      description:
        - Database query identifier.
      returned: always
      type: integer
      sample: null
    database_name:
      description:
        - Database Name.
      returned: always
      type: str
      sample: null
    user_id:
      description:
        - Database user identifier.
      returned: always
      type: integer
      sample: null
    count:
      description:
        - Wait event count observed in this time interval.
      returned: always
      type: integer
      sample: null
    total_time_in_ms:
      description:
        - Total time of wait in milliseconds in this time interval.
      returned: always
      type: number
      sample: null
    value:
      description:
        - The list of wait statistics.
      returned: always
      type: list
      sample: null
      contains:
        start_time:
          description:
            - Observation start time.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - Observation end time.
          returned: always
          type: str
          sample: null
        event_name:
          description:
            - Wait event name.
          returned: always
          type: str
          sample: null
        event_type_name:
          description:
            - Wait event type name.
          returned: always
          type: str
          sample: null
        query_id:
          description:
            - Database query identifier.
          returned: always
          type: integer
          sample: null
        database_name:
          description:
            - Database Name.
          returned: always
          type: str
          sample: null
        user_id:
          description:
            - Database user identifier.
          returned: always
          type: integer
          sample: null
        count:
          description:
            - Wait event count observed in this time interval.
          returned: always
          type: integer
          sample: null
        total_time_in_ms:
          description:
            - Total time of wait in milliseconds in this time interval.
          returned: always
          type: number
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.my import MySQLManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWaitStatisticInfo(AzureRMModuleBase):
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
            wait_statistics_id=dict(
                type='str'
            ),
            observation_start_time=dict(
                type='str'
            ),
            observation_end_time=dict(
                type='str'
            ),
            aggregation_window=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.wait_statistics_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWaitStatisticInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.observation_start_time is not None and
            self.observation_end_time is not None and
            self.aggregation_window is not None):
            self.results['wait_statistics'] = self.format_item(self.listbyserver())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.wait_statistics_id is not None):
            self.results['wait_statistics'] = self.format_item(self.get())
        return self.results

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.wait_statistics.list_by_server(resource_group_name=self.resource_group_name,
                                                                       server_name=self.server_name,
                                                                       parameters=self.body)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.wait_statistics.get(resource_group_name=self.resource_group_name,
                                                            server_name=self.server_name,
                                                            wait_statistics_id=self.wait_statistics_id)
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
    AzureRMWaitStatisticInfo()


if __name__ == '__main__':
    main()
