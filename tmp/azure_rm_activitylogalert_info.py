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
module: azure_rm_activitylogalert_info
version_added: '2.9'
short_description: Get ActivityLogAlert info.
description:
  - Get info of ActivityLogAlert.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  activity_log_alert_name:
    description:
      - The name of the activity log alert.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an activity log alert
      azure_rm_activitylogalert_info: 
        activity_log_alert_name: SampleActivityLogAlert
        resource_group_name: Default-ActivityLogAlerts
        

    - name: List activity log alerts
      azure_rm_activitylogalert_info: 
        {}
        

'''

RETURN = '''
activity_log_alerts:
  description: >-
    A list of dict results where the key is the name of the ActivityLogAlert and
    the values are the facts for that ActivityLogAlert.
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
    scopes:
      description:
        - >-
          A list of resourceIds that will be used as prefixes. The alert will
          only apply to activityLogs with resourceIds that fall under one of
          these prefixes. This list must include at least one item.
      returned: always
      type: list
      sample: null
    enabled:
      description:
        - >-
          Indicates whether this activity log alert is enabled. If an activity
          log alert is not enabled, then none of its actions will be activated.
      returned: always
      type: bool
      sample: null
    condition:
      description:
        - The condition that will cause this alert to activate.
      returned: always
      type: dict
      sample: null
      contains:
        all_of:
          description:
            - The list of activity log alert conditions.
          returned: always
          type: list
          sample: null
          contains:
            field:
              description:
                - >-
                  The name of the field that this condition will examine. The
                  possible values for this field are (case-insensitive):
                  'resourceId', 'category', 'caller', 'level', 'operationName',
                  'resourceGroup', 'resourceProvider', 'status', 'subStatus',
                  'resourceType', or anything beginning with 'properties.'.
              returned: always
              type: str
              sample: null
            equals:
              description:
                - >-
                  The field value will be compared to this value
                  (case-insensitive) to determine if the condition is met.
              returned: always
              type: str
              sample: null
    actions:
      description:
        - The actions that will activate when the condition is met.
      returned: always
      type: dict
      sample: null
      contains:
        action_groups:
          description:
            - The list of activity log alerts.
          returned: always
          type: list
          sample: null
          contains:
            action_group_id:
              description:
                - >-
                  The resourceId of the action group. This cannot be null or
                  empty.
              returned: always
              type: str
              sample: null
            webhook_properties:
              description:
                - >-
                  the dictionary of custom properties to include with the post
                  operation. These data are appended to the webhook payload.
              returned: always
              type: dictionary
              sample: null
    description:
      description:
        - A description of this activity log alert.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of activity log alerts.
      returned: always
      type: list
      sample: null
      contains:
        scopes:
          description:
            - >-
              A list of resourceIds that will be used as prefixes. The alert
              will only apply to activityLogs with resourceIds that fall under
              one of these prefixes. This list must include at least one item.
          returned: always
          type: list
          sample: null
        enabled:
          description:
            - >-
              Indicates whether this activity log alert is enabled. If an
              activity log alert is not enabled, then none of its actions will
              be activated.
          returned: always
          type: bool
          sample: null
        condition:
          description:
            - The condition that will cause this alert to activate.
          returned: always
          type: dict
          sample: null
          contains:
            all_of:
              description:
                - The list of activity log alert conditions.
              returned: always
              type: list
              sample: null
              contains:
                field:
                  description:
                    - >-
                      The name of the field that this condition will examine.
                      The possible values for this field are (case-insensitive):
                      'resourceId', 'category', 'caller', 'level',
                      'operationName', 'resourceGroup', 'resourceProvider',
                      'status', 'subStatus', 'resourceType', or anything
                      beginning with 'properties.'.
                  returned: always
                  type: str
                  sample: null
                equals:
                  description:
                    - >-
                      The field value will be compared to this value
                      (case-insensitive) to determine if the condition is met.
                  returned: always
                  type: str
                  sample: null
        actions:
          description:
            - The actions that will activate when the condition is met.
          returned: always
          type: dict
          sample: null
          contains:
            action_groups:
              description:
                - The list of activity log alerts.
              returned: always
              type: list
              sample: null
              contains:
                action_group_id:
                  description:
                    - >-
                      The resourceId of the action group. This cannot be null or
                      empty.
                  returned: always
                  type: str
                  sample: null
                webhook_properties:
                  description:
                    - >-
                      the dictionary of custom properties to include with the
                      post operation. These data are appended to the webhook
                      payload.
                  returned: always
                  type: dictionary
                  sample: null
        description:
          description:
            - A description of this activity log alert.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Provides the link to retrieve the next set of elements.
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


class AzureRMActivityLogAlertInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            activity_log_alert_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.activity_log_alert_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMActivityLogAlertInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.activity_log_alert_name is not None):
            self.results['activity_log_alerts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['activity_log_alerts'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['activity_log_alerts'] = self.format_item(self.listbysubscriptionid())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.activity_log_alerts.get(resource_group_name=self.resource_group_name,
                                                                activity_log_alert_name=self.activity_log_alert_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.activity_log_alerts.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscriptionid(self):
        response = None

        try:
            response = self.mgmt_client.activity_log_alerts.list_by_subscription_id()
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
    AzureRMActivityLogAlertInfo()


if __name__ == '__main__':
    main()
