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
module: azure_rm_scheduledqueryrule
version_added: '2.9'
short_description: Manage Azure ScheduledQueryRule instance.
description:
  - 'Create, update and delete instance of Azure ScheduledQueryRule.'
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
      - The description of the Log Search rule.
    type: str
  enabled:
    description:
      - >-
        The flag which indicates whether the Log Search rule is enabled. Value
        should be true or false
    type: str
    choices:
      - 'true'
      - 'false'
  source:
    description:
      - Data Source against which rule will Query Data
    type: dict
    suboptions:
      query:
        description:
          - Log search query. Required for action type - AlertingAction
        type: str
      authorized_resources:
        description:
          - List of  Resource referred into query
        type: list
      data_source_id:
        description:
          - The resource uri over which log search query is to be run.
        required: true
        type: str
      query_type:
        description:
          - Set value to 'ResultCount' .
        type: str
        choices:
          - ResultCount
  schedule:
    description:
      - >-
        Schedule (Frequency, Time Window) for rule. Required for action type -
        AlertingAction
    type: dict
    suboptions:
      frequency_in_minutes:
        description:
          - frequency (in minutes) at which rule condition should be evaluated.
        required: true
        type: integer
      time_window_in_minutes:
        description:
          - >-
            Time window for which data needs to be fetched for query (should be
            greater than or equal to frequencyInMinutes).
        required: true
        type: integer
  action:
    description:
      - Action needs to be taken on rule execution.
    type: dict
    suboptions:
      odata_type:
        description:
          - >-
            Specifies the action. Supported values - AlertingAction,
            LogToMetricAction
        required: true
        type: str
  state:
    description:
      - Assert the state of the ScheduledQueryRule.
      - >-
        Use C(present) to create or update an ScheduledQueryRule and C(absent)
        to delete it.
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
    - name: Create or Update rule - AlertingAction
      azure_rm_scheduledqueryrule: 
        resource_group_name: Rac46PostSwapRG
        rule_name: logalertfoo
        location: eastus
        properties:
          description: log alert description
          action:
            azns_action:
              action_group: []
              custom_webhook_payload: '{}'
              email_subject: Email Header
            odata.type: >-
              Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction
            severity: '1'
            trigger:
              metric_trigger:
                metric_column: Computer
                metric_trigger_type: Consecutive
                threshold: 5
                threshold_operator: GreaterThan
              threshold: 3
              threshold_operator: GreaterThan
          enabled: 'true'
          last_updated_time: '2017-06-23T21:23:52.0221265Z'
          provisioning_state: Succeeded
          schedule:
            frequency_in_minutes: 15
            time_window_in_minutes: 15
          source:
            data_source_id: >-
              /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/Microsoft.OperationalInsights/workspaces/sampleWorkspace
            query: 'Heartbeat | summarize AggregatedValue = count() by bin(TimeGenerated, 5m)'
            query_type: ResultCount
        tags: {}
        

    - name: Create or Update rule - AlertingAction with Cross-Resource
      azure_rm_scheduledqueryrule: 
        resource_group_name: Rac46PostSwapRG
        rule_name: SampleCrossResourceAlert
        location: eastus
        properties:
          description: Sample Cross Resource alert
          action:
            azns_action:
              action_group:
                - >-
                  /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/microsoft.insights/actiongroups/test-ag
              email_subject: Cross Resource Mail!!
            odata.type: >-
              Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction
            severity: '3'
            trigger:
              threshold: 5000
              threshold_operator: GreaterThan
          enabled: 'true'
          schedule:
            frequency_in_minutes: 60
            time_window_in_minutes: 60
          source:
            authorized_resources:
              - >-
                /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/Microsoft.OperationalInsights/workspaces/sampleWorkspace
              - >-
                /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/microsoft.insights/components/sampleAI
            data_source_id: >-
              /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/microsoft.insights/components/sampleAI
            query: 'union requests, workspace("sampleWorkspace").Update'
            query_type: ResultCount
        tags: {}
        

    - name: Create or Update rule - LogToMetricAction
      azure_rm_scheduledqueryrule: 
        resource_group_name: alertsweu
        rule_name: logtometricfoo
        location: West Europe
        properties:
          description: log to metric description
          action:
            criteria:
              - dimensions: []
                metric_name: Average_% Idle Time
            odata.type: >-
              Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction
          enabled: 'true'
          source:
            data_source_id: >-
              /subscriptions/af52d502-a447-4bc6-8cb7-4780fbb00490/resourceGroups/alertsweu/providers/Microsoft.OperationalInsights/workspaces/alertsweu
        tags: {}
        

    - name: Patch Log Search Rule
      azure_rm_scheduledqueryrule: 
        resource_group_name: my-resource-group
        rule_name: logalertfoo
        properties:
          enabled: 'true'
        

    - name: Delete rule
      azure_rm_scheduledqueryrule: 
        resource_group_name: Rac46PostSwapRG
        rule_name: logalertfoo
        

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
    - The description of the Log Search rule.
  returned: always
  type: str
  sample: null
enabled:
  description:
    - >-
      The flag which indicates whether the Log Search rule is enabled. Value
      should be true or false
  returned: always
  type: str
  sample: null
last_updated_time:
  description:
    - Last time the rule was updated in IS08601 format.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state of the scheduled query rule
  returned: always
  type: str
  sample: null
source:
  description:
    - Data Source against which rule will Query Data
  returned: always
  type: dict
  sample: null
  contains:
    query:
      description:
        - Log search query. Required for action type - AlertingAction
      returned: always
      type: str
      sample: null
    authorized_resources:
      description:
        - List of  Resource referred into query
      returned: always
      type: list
      sample: null
    data_source_id:
      description:
        - The resource uri over which log search query is to be run.
      returned: always
      type: str
      sample: null
    query_type:
      description:
        - Set value to 'ResultCount' .
      returned: always
      type: str
      sample: null
schedule:
  description:
    - >-
      Schedule (Frequency, Time Window) for rule. Required for action type -
      AlertingAction
  returned: always
  type: dict
  sample: null
  contains:
    frequency_in_minutes:
      description:
        - frequency (in minutes) at which rule condition should be evaluated.
      returned: always
      type: integer
      sample: null
    time_window_in_minutes:
      description:
        - >-
          Time window for which data needs to be fetched for query (should be
          greater than or equal to frequencyInMinutes).
      returned: always
      type: integer
      sample: null
action:
  description:
    - Action needs to be taken on rule execution.
  returned: always
  type: dict
  sample: null
  contains:
    odata_type:
      description:
        - >-
          Specifies the action. Supported values - AlertingAction,
          LogToMetricAction
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


class AzureRMScheduledQueryRule(AzureRMModuleBaseExt):
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
            enabled=dict(
                type='str',
                disposition='/enabled',
                choices=['true',
                         'false']
            ),
            source=dict(
                type='dict',
                disposition='/source',
                options=dict(
                    query=dict(
                        type='str',
                        disposition='query'
                    ),
                    authorized_resources=dict(
                        type='list',
                        disposition='authorized_resources',
                        elements='str'
                    ),
                    data_source_id=dict(
                        type='str',
                        disposition='data_source_id',
                        required=True
                    ),
                    query_type=dict(
                        type='str',
                        disposition='query_type',
                        choices=['ResultCount']
                    )
                )
            ),
            schedule=dict(
                type='dict',
                disposition='/schedule',
                options=dict(
                    frequency_in_minutes=dict(
                        type='integer',
                        disposition='frequency_in_minutes',
                        required=True
                    ),
                    time_window_in_minutes=dict(
                        type='integer',
                        disposition='time_window_in_minutes',
                        required=True
                    )
                )
            ),
            action=dict(
                type='dict',
                disposition='/action',
                options=dict(
                    odata_type=dict(
                        type='str',
                        disposition='odata_type',
                        required=True
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

        super(AzureRMScheduledQueryRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2018-04-16')

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
            response = self.mgmt_client.scheduled_query_rules.create_or_update(resource_group_name=self.resource_group_name,
                                                                               rule_name=self.rule_name,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ScheduledQueryRule instance.')
            self.fail('Error creating the ScheduledQueryRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.scheduled_query_rules.delete(resource_group_name=self.resource_group_name,
                                                                     rule_name=self.rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the ScheduledQueryRule instance.')
            self.fail('Error deleting the ScheduledQueryRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.scheduled_query_rules.get(resource_group_name=self.resource_group_name,
                                                                  rule_name=self.rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMScheduledQueryRule()


if __name__ == '__main__':
    main()
