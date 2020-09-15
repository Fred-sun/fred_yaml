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
module: azure_rm_diagnosticsetting
version_added: '2.9'
short_description: Manage Azure DiagnosticSetting instance.
description:
  - 'Create, update and delete instance of Azure DiagnosticSetting.'
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
  name:
    description:
      - The name of the diagnostic setting.
    required: true
    type: str
  storage_account_id:
    description:
      - >-
        The resource ID of the storage account to which you would like to send
        Diagnostic Logs.
    type: str
  service_bus_rule_id:
    description:
      - >-
        The service bus rule Id of the diagnostic setting. This is here to
        maintain backwards compatibility.
    type: str
  event_hub_authorization_rule_id:
    description:
      - The resource Id for the event hub authorization rule.
    type: str
  event_hub_name:
    description:
      - >-
        The name of the event hub. If none is specified, the default event hub
        will be selected.
    type: str
  metrics:
    description:
      - The list of metric settings.
    type: list
    suboptions:
      time_grain:
        description:
          - the timegrain of the metric in ISO8601 format.
        type: duration
      category:
        description:
          - >-
            Name of a Diagnostic Metric category for a resource type this
            setting is applied to. To obtain the list of Diagnostic metric
            categories for a resource, first perform a GET diagnostic settings
            operation.
        type: str
      enabled:
        description:
          - a value indicating whether this category is enabled.
        required: true
        type: bool
      enabled_retention_policy_enabled:
        description:
          - a value indicating whether the retention policy is enabled.
        type: bool
      days:
        description:
          - >-
            the number of days for the retention in days. A value of 0 will
            retain the events indefinitely.
        type: integer
  logs:
    description:
      - The list of logs settings.
    type: list
    suboptions:
      category:
        description:
          - >-
            Name of a Diagnostic Log category for a resource type this setting
            is applied to. To obtain the list of Diagnostic Log categories for a
            resource, first perform a GET diagnostic settings operation.
        type: str
      enabled:
        description:
          - a value indicating whether this log is enabled.
        required: true
        type: bool
      enabled_retention_policy_enabled:
        description:
          - a value indicating whether the retention policy is enabled.
        type: bool
      days:
        description:
          - >-
            the number of days for the retention in days. A value of 0 will
            retain the events indefinitely.
        type: integer
  workspace_id:
    description:
      - >-
        The full ARM resource ID of the Log Analytics workspace to which you
        would like to send Diagnostic Logs. Example:
        /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
    type: str
  log_analytics_destination_type:
    description:
      - >-
        A string indicating whether the export to Log Analytics should use the
        default destination type, i.e. AzureDiagnostics, or use a destination
        type constructed as follows: <normalized service identity>_<normalized
        category name>. Possible values are: Dedicated and null (null is
        default.)
    type: str
  state:
    description:
      - Assert the state of the DiagnosticSetting.
      - >-
        Use C(present) to create or update an DiagnosticSetting and C(absent) to
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
    - name: Creates or Updates the diagnostic setting
      azure_rm_diagnosticsetting: 
        name: mysetting
        resource_uri: >-
          subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourcegroups/viruela1/providers/microsoft.logic/workflows/viruela6
        properties:
          event_hub_authorization_rule_id: >-
            /subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourceGroups/montest/providers/microsoft.eventhub/namespaces/mynamespace/eventhubs/myeventhub/authorizationrules/myrule
          event_hub_name: myeventhub
          log_analytics_destination_type: Dedicated
          logs:
            - category: WorkflowRuntime
              enabled: true
              retention_policy:
                days: 0
                enabled: false
          metrics:
            - category: WorkflowMetrics
              enabled: true
              retention_policy:
                days: 0
                enabled: false
          storage_account_id: >-
            /subscriptions/df602c9c-7aa0-407d-a6fb-eb20c8bd1192/resourceGroups/apptest/providers/Microsoft.Storage/storageAccounts/appteststorage1
          workspace_id: ''
        

    - name: Deletes the diagnostic setting
      azure_rm_diagnosticsetting: 
        name: mysetting
        resource_uri: >-
          subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourcegroups/viruela1/providers/microsoft.logic/workflows/viruela6
        

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
storage_account_id:
  description:
    - >-
      The resource ID of the storage account to which you would like to send
      Diagnostic Logs.
  returned: always
  type: str
  sample: null
service_bus_rule_id:
  description:
    - >-
      The service bus rule Id of the diagnostic setting. This is here to
      maintain backwards compatibility.
  returned: always
  type: str
  sample: null
event_hub_authorization_rule_id:
  description:
    - The resource Id for the event hub authorization rule.
  returned: always
  type: str
  sample: null
event_hub_name:
  description:
    - >-
      The name of the event hub. If none is specified, the default event hub
      will be selected.
  returned: always
  type: str
  sample: null
metrics:
  description:
    - The list of metric settings.
  returned: always
  type: list
  sample: null
  contains:
    time_grain:
      description:
        - the timegrain of the metric in ISO8601 format.
      returned: always
      type: duration
      sample: null
    category:
      description:
        - >-
          Name of a Diagnostic Metric category for a resource type this setting
          is applied to. To obtain the list of Diagnostic metric categories for
          a resource, first perform a GET diagnostic settings operation.
      returned: always
      type: str
      sample: null
    enabled:
      description:
        - a value indicating whether this category is enabled.
      returned: always
      type: bool
      sample: null
    enabled_retention_policy_enabled:
      description:
        - a value indicating whether the retention policy is enabled.
      returned: always
      type: bool
      sample: null
    days:
      description:
        - >-
          the number of days for the retention in days. A value of 0 will retain
          the events indefinitely.
      returned: always
      type: integer
      sample: null
logs:
  description:
    - The list of logs settings.
  returned: always
  type: list
  sample: null
  contains:
    category:
      description:
        - >-
          Name of a Diagnostic Log category for a resource type this setting is
          applied to. To obtain the list of Diagnostic Log categories for a
          resource, first perform a GET diagnostic settings operation.
      returned: always
      type: str
      sample: null
    enabled:
      description:
        - a value indicating whether this log is enabled.
      returned: always
      type: bool
      sample: null
    enabled_retention_policy_enabled:
      description:
        - a value indicating whether the retention policy is enabled.
      returned: always
      type: bool
      sample: null
    days:
      description:
        - >-
          the number of days for the retention in days. A value of 0 will retain
          the events indefinitely.
      returned: always
      type: integer
      sample: null
workspace_id:
  description:
    - >-
      The full ARM resource ID of the Log Analytics workspace to which you would
      like to send Diagnostic Logs. Example:
      /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
  returned: always
  type: str
  sample: null
log_analytics_destination_type:
  description:
    - >-
      A string indicating whether the export to Log Analytics should use the
      default destination type, i.e. AzureDiagnostics, or use a destination type
      constructed as follows: <normalized service identity>_<normalized category
      name>. Possible values are: Dedicated and null (null is default.)
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


class AzureRMDiagnosticSetting(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            storage_account_id=dict(
                type='str',
                disposition='/storage_account_id'
            ),
            service_bus_rule_id=dict(
                type='str',
                disposition='/service_bus_rule_id'
            ),
            event_hub_authorization_rule_id=dict(
                type='str',
                disposition='/event_hub_authorization_rule_id'
            ),
            event_hub_name=dict(
                type='str',
                disposition='/event_hub_name'
            ),
            metrics=dict(
                type='list',
                disposition='/metrics',
                elements='dict',
                options=dict(
                    time_grain=dict(
                        type='duration',
                        disposition='time_grain'
                    ),
                    category=dict(
                        type='str',
                        disposition='category'
                    ),
                    enabled=dict(
                        type='bool',
                        disposition='enabled',
                        required=True
                    ),
                    enabled_retention_policy_enabled=dict(
                        type='bool',
                        disposition='enabled_retention_policy_enabled'
                    ),
                    days=dict(
                        type='integer',
                        disposition='days'
                    )
                )
            ),
            logs=dict(
                type='list',
                disposition='/logs',
                elements='dict',
                options=dict(
                    category=dict(
                        type='str',
                        disposition='category'
                    ),
                    enabled=dict(
                        type='bool',
                        disposition='enabled',
                        required=True
                    ),
                    enabled_retention_policy_enabled=dict(
                        type='bool',
                        disposition='enabled_retention_policy_enabled'
                    ),
                    days=dict(
                        type='integer',
                        disposition='days'
                    )
                )
            ),
            workspace_id=dict(
                type='str',
                disposition='/workspace_id'
            ),
            log_analytics_destination_type=dict(
                type='str',
                disposition='/log_analytics_destination_type'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_uri = None
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDiagnosticSetting, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-05-01-preview')

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
            response = self.mgmt_client.diagnostic_settings.create_or_update(resource_uri=self.resource_uri,
                                                                             name=self.name,
                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DiagnosticSetting instance.')
            self.fail('Error creating the DiagnosticSetting instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.diagnostic_settings.delete(resource_uri=self.resource_uri,
                                                                   name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the DiagnosticSetting instance.')
            self.fail('Error deleting the DiagnosticSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.diagnostic_settings.get(resource_uri=self.resource_uri,
                                                                name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDiagnosticSetting()


if __name__ == '__main__':
    main()
