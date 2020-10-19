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
module: azure_rm_report_info
version_added: '2.9'
short_description: Get Report info.
description:
  - Get info of Report.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  profile_name:
    description:
      - The Profile identifier associated with the Tenant and Partner
    required: true
    type: str
  experiment_name:
    description:
      - The Experiment identifier associated with the Experiment
    required: true
    type: str
  end_date_time_utc:
    description:
      - The end DateTime of the Latency Scorecard in UTC
      - The end DateTime of the Timeseries in UTC
    required: true
    type: str
  country:
    description:
      - >-
        The country associated with the Latency Scorecard. Values are country
        ISO codes as specified here-
        https://www.iso.org/iso-3166-country-codes.html
      - >-
        The country associated with the Timeseries. Values are country ISO codes
        as specified here- https://www.iso.org/iso-3166-country-codes.html
    required: true
    type: str
  aggregation_interval:
    description:
      - The aggregation interval of the Latency Scorecard
      - The aggregation interval of the Timeseries
    required: true
    type: str
    choices:
      - Daily
      - Weekly
      - Monthly
  start_date_time_utc:
    description:
      - The start DateTime of the Timeseries in UTC
    type: str
  timeseries_type:
    description:
      - The type of Timeseries
    type: str
    choices:
      - MeasurementCounts
      - LatencyP50
      - LatencyP75
      - LatencyP95
  endpoint:
    description:
      - The specific endpoint
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a Latency Scorecard for a given Experiment
      azure_rm_report_info: 
        aggregation_interval: Daily
        experiment_name: MyExperiment
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        

    - name: Gets a Timeseries for a given Experiment
      azure_rm_report_info: 
        aggregation_interval: Hourly
        end_date_time_utc: '2019-09-21T17:32:28Z'
        experiment_name: MyExperiment
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        start_date_time_utc: '2019-07-21T17:32:28Z'
        timeseries_type: MeasurementCounts
        

'''

RETURN = '''
reports:
  description: >-
    A list of dict results where the key is the name of the Report and the
    values are the facts for that Report.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    id_properties_id:
      description:
        - The unique identifier of the Latency Scorecard
      returned: always
      type: str
      sample: null
    name_properties_name:
      description:
        - The name of the Latency Scorecard
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the Latency Scorecard
      returned: always
      type: str
      sample: null
    endpoint_a:
      description:
        - The A endpoint in the scorecard
      returned: always
      type: str
      sample: null
    endpoint_b:
      description:
        - The B endpoint in the scorecard
      returned: always
      type: str
      sample: null
    start_date_time_utc:
      description:
        - |-
          The start time of the Latency Scorecard in UTC
          The start DateTime of the Timeseries in UTC
      returned: always
      type: str
      sample: null
    end_date_time_utc:
      description:
        - |-
          The end time of the Latency Scorecard in UTC
          The end DateTime of the Timeseries in UTC
      returned: always
      type: str
      sample: null
    country:
      description:
        - >-
          The country associated with the Latency Scorecard. Values are country
          ISO codes as specified here-
          https://www.iso.org/iso-3166-country-codes.html

          The country associated with the Timeseries. Values are country ISO
          codes as specified here-
          https://www.iso.org/iso-3166-country-codes.html
      returned: always
      type: str
      sample: null
    latency_metrics:
      description:
        - The latency metrics of the Latency Scorecard
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the Latency Metric
          returned: always
          type: str
          sample: null
        end_date_time_utc:
          description:
            - The end time of the Latency Scorecard in UTC
          returned: always
          type: str
          sample: null
        a_value:
          description:
            - The metric value of the A endpoint
          returned: always
          type: number
          sample: null
        b_value:
          description:
            - The metric value of the B endpoint
          returned: always
          type: number
          sample: null
        delta:
          description:
            - The difference in value between endpoint A and B
          returned: always
          type: number
          sample: null
        delta_percent:
          description:
            - The percent difference between endpoint A and B
          returned: always
          type: number
          sample: null
        a_clower95ci:
          description:
            - The lower end of the 95% confidence interval for endpoint A
          returned: always
          type: number
          sample: null
        a_hupper95ci:
          description:
            - The upper end of the 95% confidence interval for endpoint A
          returned: always
          type: number
          sample: null
        b_clower95ci:
          description:
            - The lower end of the 95% confidence interval for endpoint B
          returned: always
          type: number
          sample: null
        b_upper95ci:
          description:
            - The upper end of the 95% confidence interval for endpoint B
          returned: always
          type: number
          sample: null
    endpoint:
      description:
        - The endpoint associated with the Timeseries data point
      returned: always
      type: str
      sample: null
    aggregation_interval:
      description:
        - The aggregation interval of the Timeseries
      returned: always
      type: str
      sample: null
    timeseries_type:
      description:
        - The type of Timeseries
      returned: always
      type: str
      sample: null
    timeseries_data:
      description:
        - The set of data points for the timeseries
      returned: always
      type: list
      sample: null
      contains:
        date_time_utc:
          description:
            - The DateTime of the Timeseries data point in UTC
          returned: always
          type: str
          sample: null
        value:
          description:
            - The Value of the Timeseries data point
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReportInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            profile_name=dict(
                type='str',
                required=True
            ),
            experiment_name=dict(
                type='str',
                required=True
            ),
            end_date_time_utc=dict(
                type='str',
                required=True
            ),
            country=dict(
                type='str',
                required=True
            ),
            aggregation_interval=dict(
                type='str',
                choices=['Daily',
                         'Weekly',
                         'Monthly'],
                required=True
            ),
            start_date_time_utc=dict(
                type='str'
            ),
            timeseries_type=dict(
                type='str',
                choices=['MeasurementCounts',
                         'LatencyP50',
                         'LatencyP75',
                         'LatencyP95']
            ),
            endpoint=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.profile_name = None
        self.experiment_name = None
        self.end_date_time_utc = None
        self.country = None
        self.aggregation_interval = None
        self.start_date_time_utc = None
        self.timeseries_type = None
        self.endpoint = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReportInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01')

        if (self.resource_group_name is not None and
            self.profile_name is not None and
            self.experiment_name is not None and
            self.start_date_time_utc is not None and
            self.end_date_time_utc is not None and
            self.aggregation_interval is not None and
            self.timeseries_type is not None):
            self.results['reports'] = self.format_item(self.gettimesery())
        elif (self.resource_group_name is not None and
              self.profile_name is not None and
              self.experiment_name is not None and
              self.aggregation_interval is not None):
            self.results['reports'] = self.format_item(self.getlatencyscorecard())
        return self.results

    def gettimesery(self):
        response = None

        try:
            response = self.mgmt_client.reports.get_timesery(resource_group_name=self.resource_group_name,
                                                             profile_name=self.profile_name,
                                                             experiment_name=self.experiment_name,
                                                             start_date_time_utc=self.start_date_time_utc,
                                                             end_date_time_utc=self.end_date_time_utc,
                                                             aggregation_interval=self.aggregation_interval,
                                                             timeseries_type=self.timeseries_type,
                                                             endpoint=self.endpoint,
                                                             country=self.country)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getlatencyscorecard(self):
        response = None

        try:
            response = self.mgmt_client.reports.get_latency_scorecard(resource_group_name=self.resource_group_name,
                                                                      profile_name=self.profile_name,
                                                                      experiment_name=self.experiment_name,
                                                                      end_date_time_utc=self.end_date_time_utc,
                                                                      country=self.country,
                                                                      aggregation_interval=self.aggregation_interval)
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
    AzureRMReportInfo()


if __name__ == '__main__':
    main()
