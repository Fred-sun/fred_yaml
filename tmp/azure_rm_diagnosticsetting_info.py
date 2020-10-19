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
module: azure_rm_diagnosticsetting_info
version_added: '2.9'
short_description: Get DiagnosticSetting info.
description:
  - Get info of DiagnosticSetting.
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
  name:
    description:
      - The name of the diagnostic setting.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets the diagnostic setting
      azure_rm_diagnosticsetting_info: 
        name: mysetting
        resource_uri: >-
          subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourcegroups/viruela1/providers/microsoft.logic/workflows/viruela6
        

'''

RETURN = '''
diagnostic_settings:
  description: >-
    A list of dict results where the key is the name of the DiagnosticSetting
    and the values are the facts for that DiagnosticSetting.
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
              Name of a Diagnostic Metric category for a resource type this
              setting is applied to. To obtain the list of Diagnostic metric
              categories for a resource, first perform a GET diagnostic settings
              operation.
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
              the number of days for the retention in days. A value of 0 will
              retain the events indefinitely.
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
              Name of a Diagnostic Log category for a resource type this setting
              is applied to. To obtain the list of Diagnostic Log categories for
              a resource, first perform a GET diagnostic settings operation.
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
              the number of days for the retention in days. A value of 0 will
              retain the events indefinitely.
          returned: always
          type: integer
          sample: null
    workspace_id:
      description:
        - >-
          The full ARM resource ID of the Log Analytics workspace to which you
          would like to send Diagnostic Logs. Example:
          /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
      returned: always
      type: str
      sample: null
    log_analytics_destination_type:
      description:
        - >-
          A string indicating whether the export to Log Analytics should use the
          default destination type, i.e. AzureDiagnostics, or use a destination
          type constructed as follows: <normalized service identity>_<normalized
          category name>. Possible values are: Dedicated and null (null is
          default.)
      returned: always
      type: str
      sample: null
    value:
      description:
        - The collection of diagnostic settings resources;.
      returned: always
      type: list
      sample: null
      contains:
        storage_account_id:
          description:
            - >-
              The resource ID of the storage account to which you would like to
              send Diagnostic Logs.
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
              The name of the event hub. If none is specified, the default event
              hub will be selected.
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
                  Name of a Diagnostic Metric category for a resource type this
                  setting is applied to. To obtain the list of Diagnostic metric
                  categories for a resource, first perform a GET diagnostic
                  settings operation.
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
                  the number of days for the retention in days. A value of 0
                  will retain the events indefinitely.
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
                  Name of a Diagnostic Log category for a resource type this
                  setting is applied to. To obtain the list of Diagnostic Log
                  categories for a resource, first perform a GET diagnostic
                  settings operation.
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
                  the number of days for the retention in days. A value of 0
                  will retain the events indefinitely.
              returned: always
              type: integer
              sample: null
        workspace_id:
          description:
            - >-
              The full ARM resource ID of the Log Analytics workspace to which
              you would like to send Diagnostic Logs. Example:
              /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
          returned: always
          type: str
          sample: null
        log_analytics_destination_type:
          description:
            - >-
              A string indicating whether the export to Log Analytics should use
              the default destination type, i.e. AzureDiagnostics, or use a
              destination type constructed as follows: <normalized service
              identity>_<normalized category name>. Possible values are:
              Dedicated and null (null is default.)
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


class AzureRMDiagnosticSettingInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_uri = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDiagnosticSettingInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-05-01-preview')

        if (self.resource_uri is not None and
            self.name is not None):
            self.results['diagnostic_settings'] = self.format_item(self.get())
        elif (self.resource_uri is not None):
            self.results['diagnostic_settings'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.diagnostic_settings.get(resource_uri=self.resource_uri,
                                                                name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.diagnostic_settings.list(resource_uri=self.resource_uri)
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
    AzureRMDiagnosticSettingInfo()


if __name__ == '__main__':
    main()
