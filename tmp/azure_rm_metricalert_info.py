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
module: azure_rm_metricalert_info
version_added: '2.9'
short_description: Get MetricAlert info.
description:
  - Get info of MetricAlert.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  rule_name:
    description:
      - The name of the rule.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List metric alert rules
      azure_rm_metricalert_info: 
        {}
        

    - name: Get a dynamic alert rule for multiple resources
      azure_rm_metricalert_info: 
        resource_group_name: gigtest
        rule_name: MetricAlertOnMultipleResources
        

    - name: Get a dynamic alert rule for single resource
      azure_rm_metricalert_info: 
        resource_group_name: gigtest
        rule_name: chiricutin
        

    - name: Get a web test alert rule
      azure_rm_metricalert_info: 
        resource_group_name: rg-example
        rule_name: webtest-name-example
        

    - name: Get an alert rule for multiple resources
      azure_rm_metricalert_info: 
        resource_group_name: gigtest
        rule_name: MetricAlertOnMultipleResources
        

    - name: Get an alert rule for single resource
      azure_rm_metricalert_info: 
        resource_group_name: gigtest
        rule_name: chiricutin
        

    - name: Get an alert rule on resource group(s)
      azure_rm_metricalert_info: 
        resource_group_name: gigtest1
        rule_name: MetricAlertAtResourceGroupLevel
        

    - name: Get an alert rule on subscription
      azure_rm_metricalert_info: 
        resource_group_name: gigtest
        rule_name: MetricAlertAtSubscriptionLevel
        

'''

RETURN = '''
metric_alerts:
  description: >-
    A list of dict results where the key is the name of the MetricAlert and the
    values are the facts for that MetricAlert.
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
        description:
          description:
            - >-
              the description of the metric alert that will be included in the
              alert email.
          returned: always
          type: str
          sample: null
        severity:
          description:
            - 'Alert severity {0, 1, 2, 3, 4}'
          returned: always
          type: integer
          sample: null
        enabled:
          description:
            - the flag that indicates whether the metric alert is enabled.
          returned: always
          type: bool
          sample: null
        scopes:
          description:
            - the list of resource id's that this metric alert is scoped to.
          returned: always
          type: list
          sample: null
        evaluation_frequency:
          description:
            - >-
              how often the metric alert is evaluated represented in ISO 8601
              duration format.
          returned: always
          type: duration
          sample: null
        window_size:
          description:
            - >-
              the period of time (in ISO 8601 duration format) that is used to
              monitor alert activity based on the threshold.
          returned: always
          type: duration
          sample: null
        target_resource_type:
          description:
            - >-
              the resource type of the target resource(s) on which the alert is
              created/updated. Mandatory for
              MultipleResourceMultipleMetricCriteria.
          returned: always
          type: str
          sample: null
        target_resource_region:
          description:
            - >-
              the region of the target resource(s) on which the alert is
              created/updated. Mandatory for
              MultipleResourceMultipleMetricCriteria.
          returned: always
          type: str
          sample: null
        criteria:
          description:
            - defines the specific alert criteria information.
          returned: always
          type: dict
          sample: null
          contains:
            odata_type:
              description:
                - specifies the type of the alert criteria.
              returned: always
              type: str
              sample: null
        auto_mitigate:
          description:
            - >-
              the flag that indicates whether the alert should be auto resolved
              or not. The default is true.
          returned: always
          type: bool
          sample: null
        actions:
          description:
            - >-
              the array of actions that are performed when the alert rule
              becomes active, and when an alert condition is resolved.
          returned: always
          type: list
          sample: null
          contains:
            action_group_id:
              description:
                - the id of the action group to use.
              returned: always
              type: str
              sample: null
            web_hook_properties:
              description:
                - The properties of a webhook object.
              returned: always
              type: dictionary
              sample: null
        last_updated_time:
          description:
            - Last time the rule was updated in ISO8601 format.
          returned: always
          type: str
          sample: null
    id:
      description:
        - Azure resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Azure resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Azure resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    description:
      description:
        - >-
          the description of the metric alert that will be included in the alert
          email.
      returned: always
      type: str
      sample: null
    severity:
      description:
        - 'Alert severity {0, 1, 2, 3, 4}'
      returned: always
      type: integer
      sample: null
    enabled:
      description:
        - the flag that indicates whether the metric alert is enabled.
      returned: always
      type: bool
      sample: null
    scopes:
      description:
        - the list of resource id's that this metric alert is scoped to.
      returned: always
      type: list
      sample: null
    evaluation_frequency:
      description:
        - >-
          how often the metric alert is evaluated represented in ISO 8601
          duration format.
      returned: always
      type: duration
      sample: null
    window_size:
      description:
        - >-
          the period of time (in ISO 8601 duration format) that is used to
          monitor alert activity based on the threshold.
      returned: always
      type: duration
      sample: null
    target_resource_type:
      description:
        - >-
          the resource type of the target resource(s) on which the alert is
          created/updated. Mandatory for MultipleResourceMultipleMetricCriteria.
      returned: always
      type: str
      sample: null
    target_resource_region:
      description:
        - >-
          the region of the target resource(s) on which the alert is
          created/updated. Mandatory for MultipleResourceMultipleMetricCriteria.
      returned: always
      type: str
      sample: null
    criteria:
      description:
        - defines the specific alert criteria information.
      returned: always
      type: dict
      sample: null
      contains:
        odata_type:
          description:
            - specifies the type of the alert criteria.
          returned: always
          type: str
          sample: null
    auto_mitigate:
      description:
        - >-
          the flag that indicates whether the alert should be auto resolved or
          not. The default is true.
      returned: always
      type: bool
      sample: null
    actions:
      description:
        - >-
          the array of actions that are performed when the alert rule becomes
          active, and when an alert condition is resolved.
      returned: always
      type: list
      sample: null
      contains:
        action_group_id:
          description:
            - the id of the action group to use.
          returned: always
          type: str
          sample: null
        web_hook_properties:
          description:
            - The properties of a webhook object.
          returned: always
          type: dictionary
          sample: null
    last_updated_time:
      description:
        - Last time the rule was updated in ISO8601 format.
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


class AzureRMMetricAlertInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.rule_name = None

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
        super(AzureRMMetricAlertInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-03-01')

        if (self.resource_group_name is not None and
            self.rule_name is not None):
            self.results['metric_alerts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['metric_alerts'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['metric_alerts'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.metric_alerts.get(resource_group_name=self.resource_group_name,
                                                          rule_name=self.rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.metric_alerts.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.metric_alerts.list_by_subscription()
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
    AzureRMMetricAlertInfo()


if __name__ == '__main__':
    main()
