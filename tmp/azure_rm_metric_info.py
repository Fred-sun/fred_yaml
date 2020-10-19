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
module: azure_rm_metric_info
version_added: '2.9'
short_description: Get Metric info.
description:
  - Get info of Metric.
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
  timespan:
    description:
      - >-
        The timespan of the query. It is a string with the following format
        'startDateTime_ISO/endDateTime_ISO'.
    required: true
    type: str
  interval:
    description:
      - The interval (i.e. timegrain) of the query.
    required: true
    type: duration
  metricnames:
    description:
      - The names of the metrics (comma separated) to retrieve.
    required: true
    type: str
  aggregation:
    description:
      - The list of aggregation types (comma separated) to retrieve.
    required: true
    type: str
  top:
    description:
      - The maximum number of records to retrieve.
      - Valid only if $filter is specified.
      - Defaults to 10.
    required: true
    type: integer
  orderby:
    description:
      - >-
        The aggregation to use for sorting results and the direction of the
        sort.
      - Only one order can be specified.
      - 'Examples: sum asc.'
    required: true
    type: str
  filter:
    description:
      - >-
        The **$filter** is used to reduce the set of metric data
        returned.<br>Example:<br>Metric contains metadata A, B and C.<br>-
        Return all time series of C where A = a1 and B = b1 or b2<br>**$filter=A
        eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**<br>- Invalid
        variant:<br>**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B =
        ‘b2’**<br>This is invalid because the logical or operator cannot
        separate two different metadata names.<br>- Return all time series where
        A = a1, B = b1 and C = c1:<br>**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq
        ‘c1’**<br>- Return all time series where A = a1<br>**$filter=A eq ‘a1’
        and B eq ‘*’ and C eq ‘*’**.
    required: true
    type: str
  result_type:
    description:
      - >-
        Reduces the set of data collected. The syntax allowed depends on the
        operation. See the operation's description for details.
    required: true
    type: sealed-choice
  metricnamespace:
    description:
      - Metric namespace to query metric definitions for.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Metric for data
      azure_rm_metric_info: 
        aggregation: 'Average,count'
        interval: PT1M
        metricnamespace: Microsoft.Storage/storageAccounts/blobServices
        orderby: Average asc
        resource_uri: >-
          subscriptions/b324c52b-4073-4807-93af-e07d289c093e/resourceGroups/test/providers/Microsoft.Storage/storageAccounts/larryshoebox/blobServices/default
        timespan: '2017-04-14T02:20:00Z/2017-04-14T04:20:00Z'
        top: 3
        

    - name: Get Metric for metadata
      azure_rm_metric_info: 
        aggregation: 'Average,count'
        interval: PT1M
        metricnamespace: Microsoft.Storage/storageAccounts/blobServices
        orderby: Average asc
        resource_uri: >-
          subscriptions/b324c52b-4073-4807-93af-e07d289c093e/resourceGroups/test/providers/Microsoft.Storage/storageAccounts/larryshoebox/blobServices/default
        timespan: '2017-04-14T02:20:00Z/2017-04-14T04:20:00Z'
        top: 3
        

'''

RETURN = '''
metrics:
  description: >-
    A list of dict results where the key is the name of the Metric and the
    values are the facts for that Metric.
  returned: always
  type: complex
  contains:
    cost:
      description:
        - 'The integer value representing the cost of the query, for data case.'
      returned: always
      type: integer
      sample: null
    timespan:
      description:
        - >-
          The timespan for which the data was retrieved. Its value consists of
          two datetimes concatenated, separated by '/'.  This may be adjusted in
          the future and returned back from what was originally requested.
      returned: always
      type: str
      sample: null
    interval:
      description:
        - >-
          The interval (window size) for which the metric data was returned in. 
          This may be adjusted in the future and returned back from what was
          originally requested.  This is not present if a metadata request was
          made.
      returned: always
      type: duration
      sample: null
    namespace:
      description:
        - The namespace of the metrics been queried
      returned: always
      type: str
      sample: null
    resourceregion:
      description:
        - The region of the resource been queried for metrics.
      returned: always
      type: str
      sample: null
    value:
      description:
        - the value of the collection.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - the metric Id.
          returned: always
          type: str
          sample: null
        type:
          description:
            - the resource type of the metric resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - >-
              the name and the display name of the metric, i.e. it is
              localizable string.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        unit:
          description:
            - the unit of the metric.
          returned: always
          type: sealed-choice
          sample: null
        timeseries:
          description:
            - the time series returned when a data query is performed.
          returned: always
          type: list
          sample: null
          contains:
            metadatavalues:
              description:
                - >-
                  the metadata values returned if $filter was specified in the
                  call.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - the name of the metadata.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    value:
                      description:
                        - the invariant value.
                      returned: always
                      type: str
                      sample: null
                    localized_value:
                      description:
                        - the locale specific value.
                      returned: always
                      type: str
                      sample: null
                value:
                  description:
                    - the value of the metadata.
                  returned: always
                  type: str
                  sample: null
            data:
              description:
                - >-
                  An array of data points representing the metric values.  This
                  is only returned if a result type of data is specified.
              returned: always
              type: list
              sample: null
              contains:
                time_stamp:
                  description:
                    - the timestamp for the metric value in ISO 8601 format.
                  returned: always
                  type: str
                  sample: null
                average:
                  description:
                    - the average value in the time range.
                  returned: always
                  type: number
                  sample: null
                minimum:
                  description:
                    - the least value in the time range.
                  returned: always
                  type: number
                  sample: null
                maximum:
                  description:
                    - the greatest value in the time range.
                  returned: always
                  type: number
                  sample: null
                total:
                  description:
                    - the sum of all of the values in the time range.
                  returned: always
                  type: number
                  sample: null
                count:
                  description:
                    - >-
                      the number of samples in the time range. Can be used to
                      determine the number of values that contributed to the
                      average value.
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
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMetricInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            timespan=dict(
                type='str',
                required=True
            ),
            interval=dict(
                type='duration',
                required=True
            ),
            metricnames=dict(
                type='str',
                required=True
            ),
            aggregation=dict(
                type='str',
                required=True
            ),
            top=dict(
                type='integer',
                required=True
            ),
            orderby=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str',
                required=True
            ),
            result_type=dict(
                type='sealed-choice',
                required=True
            ),
            metricnamespace=dict(
                type='str',
                required=True
            )
        )

        self.resource_uri = None
        self.timespan = None
        self.interval = None
        self.metricnames = None
        self.aggregation = None
        self.top = None
        self.orderby = None
        self.filter = None
        self.result_type = None
        self.metricnamespace = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMetricInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01')

        if (self.resource_uri is not None):
            self.results['metrics'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.metrics.list(resource_uri=self.resource_uri,
                                                     timespan=self.timespan,
                                                     interval=self.interval,
                                                     metricnames=self.metricnames,
                                                     aggregation=self.aggregation,
                                                     top=self.top,
                                                     orderby=self.orderby,
                                                     filter=self.filter,
                                                     result_type=self.result_type,
                                                     metricnamespace=self.metricnamespace)
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
    AzureRMMetricInfo()


if __name__ == '__main__':
    main()
