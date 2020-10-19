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
module: azure_rm_alertrule_info
version_added: '2.9'
short_description: Get AlertRule info.
description:
  - Get info of AlertRule.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  workspace_name:
    description:
      - The name of the workspace.
    required: true
    type: str
  rule_id:
    description:
      - Alert rule ID
    type: str
  action_id:
    description:
      - Action ID
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all alert rules.
      azure_rm_alertrule_info: 
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get a Fusion alert rule.
      azure_rm_alertrule_info: 
        resource_group_name: myRg
        rule_id: myFirstFusionRule
        workspace_name: myWorkspace
        

    - name: Get a MicrosoftSecurityIncidentCreation rule.
      azure_rm_alertrule_info: 
        resource_group_name: myRg
        rule_id: microsoftSecurityIncidentCreationRuleExample
        workspace_name: myWorkspace
        

    - name: Get a Scheduled alert rule.
      azure_rm_alertrule_info: 
        resource_group_name: myRg
        rule_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        workspace_name: myWorkspace
        

    - name: Get an action of alert rule.
      azure_rm_alertrule_info: 
        action_id: 912bec42-cb66-4c03-ac63-1761b6898c3e
        resource_group_name: myRg
        rule_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        workspace_name: myWorkspace
        

'''

RETURN = '''
alert_rules:
  description: >-
    A list of dict results where the key is the name of the AlertRule and the
    values are the facts for that AlertRule.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URL to fetch the next set of alert rules.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of alert rules.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - The alert rule kind
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
    etag:
      description:
        - |-
          Etag of the azure resource
          Etag of the action.
      returned: always
      type: str
      sample: null
    kind:
      description:
        - The alert rule kind
      returned: always
      type: str
      sample: null
    logic_app_resource_id:
      description:
        - >-
          Logic App Resource Id,
          /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.
      returned: always
      type: str
      sample: null
    workflow_id:
      description:
        - The name of the logic app's workflow.
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
    from azure.mgmt.security import Security Insights
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAlertRuleInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            ),
            rule_id=dict(
                type='str'
            ),
            action_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.rule_id = None
        self.action_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAlertRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.rule_id is not None and
            self.action_id is not None):
            self.results['alert_rules'] = self.format_item(self.getaction())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None and
              self.rule_id is not None):
            self.results['alert_rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['alert_rules'] = self.format_item(self.list())
        return self.results

    def getaction(self):
        response = None

        try:
            response = self.mgmt_client.alert_rules.get_action(resource_group_name=self.resource_group_name,
                                                               workspace_name=self.workspace_name,
                                                               rule_id=self.rule_id,
                                                               action_id=self.action_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.alert_rules.get(resource_group_name=self.resource_group_name,
                                                        workspace_name=self.workspace_name,
                                                        rule_id=self.rule_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.alert_rules.list(resource_group_name=self.resource_group_name,
                                                         workspace_name=self.workspace_name)
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
    AzureRMAlertRuleInfo()


if __name__ == '__main__':
    main()
