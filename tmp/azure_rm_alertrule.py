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
module: azure_rm_alertrule
version_added: '2.9'
short_description: Manage Azure AlertRule instance.
description:
  - 'Create, update and delete instance of Azure AlertRule.'
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
    required: true
    type: str
  alert_rule:
    description:
      - The alert rule
    type: dict
    suboptions:
      kind:
        description:
          - The alert rule kind
        required: true
        type: str
        choices:
          - Scheduled
          - MicrosoftSecurityIncidentCreation
          - Fusion
  state:
    description:
      - Assert the state of the AlertRule.
      - >-
        Use C(present) to create or update an AlertRule and C(absent) to delete
        it.
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
    - name: Creates or updates a Fusion alert rule.
      azure_rm_alertrule: 
        alert_rule:
          etag: 3d00c3ca-0000-0100-0000-5d42d5010000
          kind: Fusion
          properties:
            alert_rule_template_name: f71aba3d-28fb-450b-b192-4e76a83015c8
            enabled: true
        resource_group_name: myRg
        rule_id: myFirstFusionRule
        workspace_name: myWorkspace
        

    - name: Creates or updates a MicrosoftSecurityIncidentCreation rule.
      azure_rm_alertrule: 
        alert_rule:
          etag: '"260097e0-0000-0d00-0000-5d6fa88f0000"'
          kind: MicrosoftSecurityIncidentCreation
          properties:
            display_name: testing displayname
            enabled: true
            product_filter: Microsoft Cloud App Security
        resource_group_name: myRg
        rule_id: microsoftSecurityIncidentCreationRuleExample
        workspace_name: myWorkspace
        

    - name: Creates or updates a Scheduled alert rule.
      azure_rm_alertrule: 
        alert_rule:
          etag: '"0300bf09-0000-0000-0000-5c37296e0000"'
          kind: Scheduled
          properties:
            description: ''
            display_name: Rule2
            enabled: true
            query: >-
              ProtectionStatus | extend HostCustomEntity = Computer | extend
              IPCustomEntity = ComputerIP_Hidden
            query_frequency: PT1H
            query_period: P2DT1H30M
            severity: High
            suppression_duration: PT1H
            suppression_enabled: false
            tactics:
              - Persistence
              - LateralMovement
            trigger_operator: GreaterThan
            trigger_threshold: 0
        resource_group_name: myRg
        rule_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        workspace_name: myWorkspace
        

    - name: Delete an alert rule.
      azure_rm_alertrule: 
        resource_group_name: myRg
        rule_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        workspace_name: myWorkspace
        

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
etag:
  description:
    - Etag of the azure resource
  returned: always
  type: str
  sample: null
kind:
  description:
    - The alert rule kind
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
    from azure.mgmt.security import Security Insights
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAlertRule(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            alert_rule=dict(
                type='dict',
                disposition='/alert_rule',
                options=dict(
                    kind=dict(
                        type='str',
                        disposition='kind',
                        choices=['Scheduled',
                                 'MicrosoftSecurityIncidentCreation',
                                 'Fusion'],
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
        self.workspace_name = None
        self.rule_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAlertRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

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
            response = self.mgmt_client.alert_rules.create_or_update(resource_group_name=self.resource_group_name,
                                                                     workspace_name=self.workspace_name,
                                                                     rule_id=self.rule_id,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AlertRule instance.')
            self.fail('Error creating the AlertRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.alert_rules.delete(resource_group_name=self.resource_group_name,
                                                           workspace_name=self.workspace_name,
                                                           rule_id=self.rule_id)
        except CloudError as e:
            self.log('Error attempting to delete the AlertRule instance.')
            self.fail('Error deleting the AlertRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.alert_rules.get(resource_group_name=self.resource_group_name,
                                                        workspace_name=self.workspace_name,
                                                        rule_id=self.rule_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAlertRule()


if __name__ == '__main__':
    main()
