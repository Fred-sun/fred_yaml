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
module: azure_rm_baseline_info
version_added: '2.9'
short_description: Get Baseline info.
description:
  - Get info of Baseline.
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
  metricnames:
    description:
      - The names of the metrics (comma separated) to retrieve.
    required: true
    type: str
  metricnamespace:
    description:
      - Metric namespace to query metric definitions for.
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
  aggregation:
    description:
      - The list of aggregation types (comma separated) to retrieve.
    required: true
    type: str
  sensitivities:
    description:
      - The list of sensitivities (comma separated) to retrieve.
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
        Allows retrieving only metadata of the baseline. On data request all
        information is retrieved.
    required: true
    type: sealed-choice
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get metric baselines
      azure_rm_baseline_info: 
        aggregation: average
        interval: PT1H
        resource_uri: >-
          subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
        sensitivities: 'Low,Medium'
        timespan: '2019-03-12T11:00:00.000Z/2019-03-12T12:00:00.000Z'
        

'''

RETURN = '''
baselines:
  description: >-
    A list of dict results where the key is the name of the Baseline and the
    values are the facts for that Baseline.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of metric baselines.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The metric baseline Id.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The resource type of the metric baseline resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the metric for which the baselines were retrieved.
          returned: always
          type: str
          sample: null
        timespan:
          description:
            - >-
              The timespan for which the data was retrieved. Its value consists
              of two datetimes concatenated, separated by '/'.  This may be
              adjusted in the future and returned back from what was originally
              requested.
          returned: always
          type: str
          sample: null
        interval:
          description:
            - >-
              The interval (window size) for which the metric data was returned
              in.  This may be adjusted in the future and returned back from
              what was originally requested.  This is not present if a metadata
              request was made.
          returned: always
          type: duration
          sample: null
        namespace:
          description:
            - The namespace of the metrics been queried.
          returned: always
          type: str
          sample: null
        baselines:
          description:
            - The baseline for each time series that was queried.
          returned: always
          type: list
          sample: null
          contains:
            aggregation:
              description:
                - The aggregation type of the metric.
              returned: always
              type: str
              sample: null
            dimensions:
              description:
                - The dimensions of this time series.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Name of the dimension.
                  returned: always
                  type: str
                  sample: null
                value:
                  description:
                    - Value of the dimension.
                  returned: always
                  type: str
                  sample: null
            timestamps:
              description:
                - The list of timestamps of the baselines.
              returned: always
              type: list
              sample: null
            data:
              description:
                - The baseline values for each sensitivity.
              returned: always
              type: list
              sample: null
              contains:
                sensitivity:
                  description:
                    - the sensitivity of the baseline.
                  returned: always
                  type: str
                  sample: null
                low_thresholds:
                  description:
                    - The low thresholds of the baseline.
                  returned: always
                  type: list
                  sample: null
                high_thresholds:
                  description:
                    - The high thresholds of the baseline.
                  returned: always
                  type: list
                  sample: null
            metadata:
              description:
                - The baseline metadata values.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Name of the baseline metadata.
                  returned: always
                  type: str
                  sample: null
                value:
                  description:
                    - Value of the baseline metadata.
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
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBaselineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            metricnames=dict(
                type='str',
                required=True
            ),
            metricnamespace=dict(
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
            aggregation=dict(
                type='str',
                required=True
            ),
            sensitivities=dict(
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
            )
        )

        self.resource_uri = None
        self.metricnames = None
        self.metricnamespace = None
        self.timespan = None
        self.interval = None
        self.aggregation = None
        self.sensitivities = None
        self.filter = None
        self.result_type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMBaselineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-03-01')

        if (self.resource_uri is not None):
            self.results['baselines'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.baselines.list(resource_uri=self.resource_uri,
                                                       metricnames=self.metricnames,
                                                       metricnamespace=self.metricnamespace,
                                                       timespan=self.timespan,
                                                       interval=self.interval,
                                                       aggregation=self.aggregation,
                                                       sensitivities=self.sensitivities,
                                                       filter=self.filter,
                                                       result_type=self.result_type)
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
    AzureRMBaselineInfo()


if __name__ == '__main__':
    main()
