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
module: azure_rm_metricdefinition_info
version_added: '2.9'
short_description: Get MetricDefinition info.
description:
  - Get info of MetricDefinition.
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
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
    - name: Get Metric Definitions without filter
      azure_rm_metricdefinition_info: 
        metricnamespace: Microsoft.Web/sites
        resource_uri: >-
          subscriptions/07c0b09d-9f69-4e6e-8d05-f59f67299cb2/resourceGroups/Rac46PostSwapRG/providers/Microsoft.Web/sites/alertruleTest/providers/microsoft.insights/metricDefinitions
        

'''

RETURN = '''
metric_definitions:
  description: >-
    A list of dict results where the key is the name of the MetricDefinition and
    the values are the facts for that MetricDefinition.
  returned: always
  type: complex
  contains:
    value:
      description:
        - the values for the metric definitions.
      returned: always
      type: list
      sample: null
      contains:
        is_dimension_required:
          description:
            - Flag to indicate whether the dimension is required.
          returned: always
          type: bool
          sample: null
        resource_id:
          description:
            - the resource identifier of the resource that emitted the metric.
          returned: always
          type: str
          sample: null
        namespace:
          description:
            - the namespace the metric belongs to.
          returned: always
          type: str
          sample: null
        name:
          description:
            - >-
              the name and the display name of the metric, i.e. it is a
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
        primary_aggregation_type:
          description:
            - >-
              the primary aggregation type value defining how to use the values
              for display.
          returned: always
          type: sealed-choice
          sample: null
        supported_aggregation_types:
          description:
            - the collection of what aggregation types are supported.
          returned: always
          type: list
          sample: null
        metric_availabilities:
          description:
            - >-
              the collection of what aggregation intervals are available to be
              queried.
          returned: always
          type: list
          sample: null
          contains:
            time_grain:
              description:
                - >-
                  the time grain specifies the aggregation interval for the
                  metric. Expressed as a duration 'PT1M', 'P1D', etc.
              returned: always
              type: duration
              sample: null
            retention:
              description:
                - >-
                  the retention period for the metric at the specified
                  timegrain.  Expressed as a duration 'PT1M', 'P1D', etc.
              returned: always
              type: duration
              sample: null
        id:
          description:
            - the resource identifier of the metric definition.
          returned: always
          type: str
          sample: null
        dimensions:
          description:
            - >-
              the name and the display name of the dimension, i.e. it is a
              localizable string.
          returned: always
          type: list
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


class AzureRMMetricDefinitionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            metricnamespace=dict(
                type='str',
                required=True
            )
        )

        self.resource_uri = None
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
        super(AzureRMMetricDefinitionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01')

        if (self.resource_uri is not None):
            self.results['metric_definitions'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.metric_definitions.list(resource_uri=self.resource_uri,
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
    AzureRMMetricDefinitionInfo()


if __name__ == '__main__':
    main()
