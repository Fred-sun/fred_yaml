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
module: azure_rm_alertruleincident_info
version_added: '2.9'
short_description: Get AlertRuleIncident info.
description:
  - Get info of AlertRuleIncident.
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
  incident_name:
    description:
      - The name of the incident to retrieve.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a single alert rule incident
      azure_rm_alertruleincident_info: 
        incident_name: Website_started
        resource_group_name: Rac46PostSwapRG
        rule_name: myRuleName
        

    - name: List alert rule incidents
      azure_rm_alertruleincident_info: 
        resource_group_name: Rac46PostSwapRG
        rule_name: myRuleName
        

'''

RETURN = '''
alert_rule_incidents:
  description: >-
    A list of dict results where the key is the name of the AlertRuleIncident
    and the values are the facts for that AlertRuleIncident.
  returned: always
  type: complex
  contains:
    name:
      description:
        - Incident name.
      returned: always
      type: str
      sample: null
    rule_name:
      description:
        - Rule name that is associated with the incident.
      returned: always
      type: str
      sample: null
    is_active:
      description:
        - A boolean to indicate whether the incident is active or resolved.
      returned: always
      type: bool
      sample: null
    activated_time:
      description:
        - The time at which the incident was activated in ISO8601 format.
      returned: always
      type: str
      sample: null
    resolved_time:
      description:
        - >-
          The time at which the incident was resolved in ISO8601 format. If
          null, it means the incident is still active.
      returned: always
      type: str
      sample: null
    value:
      description:
        - the incident collection.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Incident name.
          returned: always
          type: str
          sample: null
        rule_name:
          description:
            - Rule name that is associated with the incident.
          returned: always
          type: str
          sample: null
        is_active:
          description:
            - A boolean to indicate whether the incident is active or resolved.
          returned: always
          type: bool
          sample: null
        activated_time:
          description:
            - The time at which the incident was activated in ISO8601 format.
          returned: always
          type: str
          sample: null
        resolved_time:
          description:
            - >-
              The time at which the incident was resolved in ISO8601 format. If
              null, it means the incident is still active.
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


class AzureRMAlertRuleIncidentInfo(AzureRMModuleBase):
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
            incident_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.rule_name = None
        self.incident_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAlertRuleIncidentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-01')

        if (self.resource_group_name is not None and
            self.rule_name is not None and
            self.incident_name is not None):
            self.results['alert_rule_incidents'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.rule_name is not None):
            self.results['alert_rule_incidents'] = self.format_item(self.listbyalertrule())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.alert_rule_incidents.get(resource_group_name=self.resource_group_name,
                                                                 rule_name=self.rule_name,
                                                                 incident_name=self.incident_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyalertrule(self):
        response = None

        try:
            response = self.mgmt_client.alert_rule_incidents.list_by_alert_rule(resource_group_name=self.resource_group_name,
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
    AzureRMAlertRuleIncidentInfo()


if __name__ == '__main__':
    main()
