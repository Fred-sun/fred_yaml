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
module: azure_rm_metricbaseline_info
version_added: '2.9'
short_description: Get MetricBaseline info.
description:
  - Get info of MetricBaseline.
options:
  resource_uri:
    description:
      - >-
        The identifier of the resource. It has the following structure:
        subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}.
        For example:
        subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
    required: true
    type: str
  metric_name:
    description:
      - The name of the metric to retrieve the baseline for.
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
      - The aggregation type of the metric to retrieve the baseline for.
    required: true
    type: str
  sensitivities:
    description:
      - The list of sensitivities (comma separated) to retrieve.
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
    - name: Get Metric for data
      azure_rm_metricbaseline_info: 
        aggregation: Average
        interval: PT1H
        metric_name: PercentageCpu
        resource_uri: >-
          subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
        sensitivities: 'Low,Medium'
        timespan: '2017-04-14T02:20:00Z/2017-04-14T04:20:00Z'
        

    - name: Get Metric for metadata
      azure_rm_metricbaseline_info: 
        aggregation: Average
        interval: PT1H
        metric_name: PercentageCpu
        resource_uri: >-
          subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
        timespan: '2017-04-14T02:20:00Z/2017-04-14T04:20:00Z'
        

'''

RETURN = '''
metric_baseline:
  description: >-
    A list of dict results where the key is the name of the MetricBaseline and
    the values are the facts for that MetricBaseline.
  returned: always
  type: complex
  contains:
    id:
      description:
        - the metric baseline Id.
      returned: always
      type: str
      sample: null
    type:
      description:
        - the resource type of the baseline resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          the name and the display name of the metric, i.e. it is localizable
          string.
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
    aggregation:
      description:
        - The aggregation type of the metric.
      returned: always
      type: str
      sample: null
    timestamps:
      description:
        - the array of timestamps of the baselines.
      returned: always
      type: list
      sample: null
    baseline:
      description:
        - the baseline values for each sensitivity.
      returned: always
      type: list
      sample: null
      contains:
        sensitivity:
          description:
            - the sensitivity of the baseline.
          returned: always
          type: sealed-choice
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
        - the baseline metadata values.
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


class AzureRMMetricBaselineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            metric_name=dict(
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
            result_type=dict(
                type='sealed-choice',
                required=True
            )
        )

        self.resource_uri = None
        self.metric_name = None
        self.timespan = None
        self.interval = None
        self.aggregation = None
        self.sensitivities = None
        self.result_type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-11-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMetricBaselineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-11-01-preview')

        if (self.resource_uri is not None and
            self.metric_name is not None):
            self.results['metric_baseline'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.metric_baseline.get(resource_uri=self.resource_uri,
                                                            metric_name=self.metric_name,
                                                            timespan=self.timespan,
                                                            interval=self.interval,
                                                            aggregation=self.aggregation,
                                                            sensitivities=self.sensitivities,
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
    AzureRMMetricBaselineInfo()


if __name__ == '__main__':
    main()
