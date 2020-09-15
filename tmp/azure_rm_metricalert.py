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
module: azure_rm_metricalert
version_added: '2.9'
short_description: Manage Azure MetricAlert instance.
description:
  - 'Create, update and delete instance of Azure MetricAlert.'
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
  location:
    description:
      - Resource location
    type: str
  description:
    description:
      - >-
        the description of the metric alert that will be included in the alert
        email.
    type: str
  severity:
    description:
      - 'Alert severity {0, 1, 2, 3, 4}'
    type: integer
  enabled:
    description:
      - the flag that indicates whether the metric alert is enabled.
    type: bool
  scopes:
    description:
      - the list of resource id's that this metric alert is scoped to.
    type: list
  evaluation_frequency:
    description:
      - >-
        how often the metric alert is evaluated represented in ISO 8601 duration
        format.
    type: duration
  window_size:
    description:
      - >-
        the period of time (in ISO 8601 duration format) that is used to monitor
        alert activity based on the threshold.
    type: duration
  target_resource_type:
    description:
      - >-
        the resource type of the target resource(s) on which the alert is
        created/updated. Mandatory for MultipleResourceMultipleMetricCriteria.
    type: str
  target_resource_region:
    description:
      - >-
        the region of the target resource(s) on which the alert is
        created/updated. Mandatory for MultipleResourceMultipleMetricCriteria.
    type: str
  criteria:
    description:
      - defines the specific alert criteria information.
    type: dict
    suboptions:
      odata_type:
        description:
          - specifies the type of the alert criteria.
        required: true
        type: str
        choices:
          - Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria
          - Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria
          - Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria
  auto_mitigate:
    description:
      - >-
        the flag that indicates whether the alert should be auto resolved or
        not. The default is true.
    type: bool
  actions:
    description:
      - >-
        the array of actions that are performed when the alert rule becomes
        active, and when an alert condition is resolved.
    type: list
    suboptions:
      action_group_id:
        description:
          - the id of the action group to use.
        type: str
      web_hook_properties:
        description:
          - The properties of a webhook object.
        type: dictionary
  state:
    description:
      - Assert the state of the MetricAlert.
      - >-
        Use C(present) to create or update an MetricAlert and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create or update a dynamic alert rule for Multiple Resources
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: MetricAlertOnMultipleResources
        location: global
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                alert_sensitivity: Medium
                criterion_type: DynamicThresholdCriterion
                dimensions: []
                failing_periods:
                  min_failing_periods_to_alert: 4
                  number_of_evaluation_periods: 4
                metric_name: Percentage CPU
                metric_namespace: microsoft.compute/virtualmachines
                operator: GreaterOrLessThan
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: PT1M
          scopes:
            - >-
              /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme1
            - >-
              /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme2
          severity: 3
          target_resource_region: southcentralus
          target_resource_type: Microsoft.Compute/virtualMachines
          window_size: PT15M
        tags: {}
        

    - name: Create or update a dynamic alert rule for Single Resource
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: chiricutin
        location: global
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                alert_sensitivity: Medium
                criterion_type: DynamicThresholdCriterion
                dimensions: []
                failing_periods:
                  min_failing_periods_to_alert: 4
                  number_of_evaluation_periods: 4
                ignore_data_before: '2019-04-04T21:00:00.000Z'
                metric_name: Percentage CPU
                metric_namespace: microsoft.compute/virtualmachines
                operator: GreaterOrLessThan
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: PT1M
          scopes:
            - >-
              /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme
          severity: 3
          target_resource_region: southcentralus
          target_resource_type: Microsoft.Compute/virtualMachines
          window_size: PT15M
        tags: {}
        

    - name: Create or update a web test alert rule
      azure_rm_metricalert: 
        resource_group_name: rg-example
        rule_name: webtest-name-example
        location: global
        properties:
          description: Automatically created alert rule for availability test "component-example" a
          actions: []
          criteria:
            component_id: >-
              /subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/components/webtest-name-example
            failed_location_count: 2
            odata.type: Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria
            web_test_id: >-
              /subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/webtests/component-example
          enabled: true
          evaluation_frequency: PT1M
          scopes:
            - >-
              /subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/webtests/component-example
            - >-
              /subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/components/webtest-name-example
          severity: 4
          window_size: PT15M
        tags:
          'hidden-link:/subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/components/webtest-name-example': Resource
          'hidden-link:/subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/webtests/component-example': Resource
        

    - name: Create or update an alert rule for Multiple Resource
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: MetricAlertOnMultipleResources
        location: global
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                criterion_type: StaticThresholdCriterion
                dimensions: []
                metric_name: Percentage CPU
                metric_namespace: microsoft.compute/virtualmachines
                operator: GreaterThan
                threshold: 80.5
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: PT1M
          scopes:
            - >-
              /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme1
            - >-
              /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme2
          severity: 3
          target_resource_region: southcentralus
          target_resource_type: Microsoft.Compute/virtualMachines
          window_size: PT15M
        tags: {}
        

    - name: Create or update an alert rule for Single Resource
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: chiricutin
        location: global
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                criterion_type: StaticThresholdCriterion
                dimensions: []
                metric_name: \Processor(_Total)\% Processor Time
                operator: GreaterThan
                threshold: 80.5
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: Pt1m
          scopes:
            - >-
              /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme
          severity: 3
          window_size: Pt15m
        tags: {}
        

    - name: Create or update an alert rule on Resource group(s)
      azure_rm_metricalert: 
        resource_group_name: gigtest1
        rule_name: MetricAlertAtResourceGroupLevel
        location: global
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                criterion_type: StaticThresholdCriterion
                dimensions: []
                metric_name: Percentage CPU
                metric_namespace: microsoft.compute/virtualmachines
                operator: GreaterThan
                threshold: 80.5
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: PT1M
          scopes:
            - >-
              /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest1
            - >-
              /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest2
          severity: 3
          target_resource_region: southcentralus
          target_resource_type: Microsoft.Compute/virtualMachines
          window_size: PT15M
        tags: {}
        

    - name: Create or update an alert rule on Subscription 
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: MetricAlertAtSubscriptionLevel
        location: global
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                criterion_type: StaticThresholdCriterion
                dimensions: []
                metric_name: Percentage CPU
                metric_namespace: microsoft.compute/virtualmachines
                operator: GreaterThan
                threshold: 80.5
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: PT1M
          scopes:
            - /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7
          severity: 3
          target_resource_region: southcentralus
          target_resource_type: Microsoft.Compute/virtualMachines
          window_size: PT15M
        tags: {}
        

    - name: Create or update an alert rule
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: chiricutin
        properties:
          description: This is the description of the rule1
          actions:
            - action_group_id: >-
                /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourcegroups/gigtest/providers/microsoft.insights/notificationgroups/group2
              web_hook_properties:
                key11: value11
                key12: value12
          auto_mitigate: false
          criteria:
            all_of:
              - name: High_CPU_80
                criterion_type: StaticThresholdCriterion
                dimensions: []
                metric_name: \Processor(_Total)\% Processor Time
                operator: GreaterThan
                threshold: 80.5
                time_aggregation: Average
            odata.type: Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria
          enabled: true
          evaluation_frequency: Pt1m
          scopes:
            - >-
              /subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme
          severity: 3
          window_size: Pt15m
        tags: {}
        

    - name: Delete an alert rule
      azure_rm_metricalert: 
        resource_group_name: gigtest
        rule_name: chiricutin
        

'''

RETURN = '''
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
      how often the metric alert is evaluated represented in ISO 8601 duration
      format.
  returned: always
  type: duration
  sample: null
window_size:
  description:
    - >-
      the period of time (in ISO 8601 duration format) that is used to monitor
      alert activity based on the threshold.
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
      the flag that indicates whether the alert should be auto resolved or not.
      The default is true.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMetricAlert(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            severity=dict(
                type='integer',
                disposition='/severity'
            ),
            enabled=dict(
                type='bool',
                disposition='/enabled'
            ),
            scopes=dict(
                type='list',
                disposition='/scopes',
                elements='str'
            ),
            evaluation_frequency=dict(
                type='duration',
                disposition='/evaluation_frequency'
            ),
            window_size=dict(
                type='duration',
                disposition='/window_size'
            ),
            target_resource_type=dict(
                type='str',
                disposition='/target_resource_type'
            ),
            target_resource_region=dict(
                type='str',
                disposition='/target_resource_region'
            ),
            criteria=dict(
                type='dict',
                disposition='/criteria',
                options=dict(
                    odata_type=dict(
                        type='str',
                        disposition='odata_type',
                        choices=['Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria',
                                 'Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria',
                                 'Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria'],
                        required=True
                    )
                )
            ),
            auto_mitigate=dict(
                type='bool',
                disposition='/auto_mitigate'
            ),
            actions=dict(
                type='list',
                disposition='/actions',
                elements='dict',
                options=dict(
                    action_group_id=dict(
                        type='str',
                        disposition='action_group_id'
                    ),
                    web_hook_properties=dict(
                        type='dictionary',
                        disposition='web_hook_properties'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMetricAlert, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                 supports_check_mode=True,
                                                 supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-03-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.metric_alerts.create_or_update(resource_group_name=self.resource_group_name,
                                                                       rule_name=self.rule_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MetricAlert instance.')
            self.fail('Error creating the MetricAlert instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.metric_alerts.delete(resource_group_name=self.resource_group_name,
                                                             rule_name=self.rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the MetricAlert instance.')
            self.fail('Error deleting the MetricAlert instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.metric_alerts.get(resource_group_name=self.resource_group_name,
                                                          rule_name=self.rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMetricAlert()


if __name__ == '__main__':
    main()
