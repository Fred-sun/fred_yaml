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
module: azure_rm_metricalertsstatu_info
version_added: '2.9'
short_description: Get MetricAlertsStatu info.
description:
  - Get info of MetricAlertsStatu.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  rule_name:
    description:
      - The name of the rule.
    required: true
    type: str
  status_name:
    description:
      - The name of the status.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an alert rule status
      azure_rm_metricalertsstatu_info: 
        resource_group_name: gigtest
        rule_name: chiricutin
        

'''

RETURN = '''
metric_alerts_status:
  description: >-
    A list of dict results where the key is the name of the MetricAlertsStatu
    and the values are the facts for that MetricAlertsStatu.
  returned: always
  type: complex
  contains:
    value:
      description:
        - the values for the alert rule resources.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The status name.
          returned: always
          type: str
          sample: null
        id:
          description:
            - The alert rule arm id.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The extended resource type name.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The alert status properties of the metric alert status.
          returned: always
          type: dict
          sample: null
          contains:
            dimensions:
              description:
                - An object describing the type of the dimensions.
              returned: always
              type: dictionary
              sample: null
            status:
              description:
                - status value
              returned: always
              type: str
              sample: null
            timestamp:
              description:
                - UTC time when the status was checked.
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


class AzureRMMetricAlertsStatuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            rule_name=dict(
                type='str',
                required=True
            ),
            status_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.rule_name = None
        self.status_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMetricAlertsStatuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-03-01')

        if (self.resource_group_name is not None and
            self.rule_name is not None and
            self.status_name is not None):
            self.results['metric_alerts_status'] = self.format_item(self.listbyname())
        elif (self.resource_group_name is not None and
              self.rule_name is not None):
            self.results['metric_alerts_status'] = self.format_item(self.list())
        return self.results

    def listbyname(self):
        response = None

        try:
            response = self.mgmt_client.metric_alerts_status.list_by_name(resource_group_name=self.resource_group_name,
                                                                          rule_name=self.rule_name,
                                                                          status_name=self.status_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.metric_alerts_status.list(resource_group_name=self.resource_group_name,
                                                                  rule_name=self.rule_name)
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
    AzureRMMetricAlertsStatuInfo()


if __name__ == '__main__':
    main()
