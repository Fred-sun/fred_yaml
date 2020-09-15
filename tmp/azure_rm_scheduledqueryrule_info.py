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
module: azure_rm_scheduledqueryrule_info
version_added: '2.9'
short_description: Get ScheduledQueryRule info.
description:
  - Get info of ScheduledQueryRule.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  rule_name:
    description:
      - The name of the rule.
    type: str
  filter:
    description:
      - >-
        The filter to apply on the operation. For more information please see
        https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get rule
      azure_rm_scheduledqueryrule_info: 
        resource_group_name: Rac46PostSwapRG
        rule_name: logalertfoo
        

    - name: List rules
      azure_rm_scheduledqueryrule_info: 
        {}
        

'''

RETURN = '''
scheduled_query_rules:
  description: >-
    A list of dict results where the key is the name of the ScheduledQueryRule
    and the values are the facts for that ScheduledQueryRule.
  returned: always
  type: complex
  contains:
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
            - >-
              frequency (in minutes) at which rule condition should be
              evaluated.
          returned: always
          type: integer
          sample: null
        time_window_in_minutes:
          description:
            - >-
              Time window for which data needs to be fetched for query (should
              be greater than or equal to frequencyInMinutes).
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
    value:
      description:
        - The values for the Log Search Rule resources.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The description of the Log Search rule.
          returned: always
          type: str
          sample: null
        enabled:
          description:
            - >-
              The flag which indicates whether the Log Search rule is enabled.
              Value should be true or false
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
              Schedule (Frequency, Time Window) for rule. Required for action
              type - AlertingAction
          returned: always
          type: dict
          sample: null
          contains:
            frequency_in_minutes:
              description:
                - >-
                  frequency (in minutes) at which rule condition should be
                  evaluated.
              returned: always
              type: integer
              sample: null
            time_window_in_minutes:
              description:
                - >-
                  Time window for which data needs to be fetched for query
                  (should be greater than or equal to frequencyInMinutes).
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


class AzureRMScheduledQueryRuleInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            rule_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.rule_name = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-04-16'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMScheduledQueryRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-04-16')

        if (self.resource_group_name is not None and
            self.rule_name is not None):
            self.results['scheduled_query_rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['scheduled_query_rules'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['scheduled_query_rules'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.scheduled_query_rules.get(resource_group_name=self.resource_group_name,
                                                                  rule_name=self.rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.scheduled_query_rules.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                     filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.scheduled_query_rules.list_by_subscription(filter=self.filter)
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
    AzureRMScheduledQueryRuleInfo()


if __name__ == '__main__':
    main()
