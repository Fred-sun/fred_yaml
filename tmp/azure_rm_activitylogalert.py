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
module: azure_rm_activitylogalert
version_added: '2.9'
short_description: Manage Azure ActivityLogAlert instance.
description:
  - 'Create, update and delete instance of Azure ActivityLogAlert.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  activity_log_alert_name:
    description:
      - The name of the activity log alert.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  scopes:
    description:
      - >-
        A list of resourceIds that will be used as prefixes. The alert will only
        apply to activityLogs with resourceIds that fall under one of these
        prefixes. This list must include at least one item.
    type: list
  enabled:
    description:
      - >-
        Indicates whether this activity log alert is enabled. If an activity log
        alert is not enabled, then none of its actions will be activated.
    type: bool
  condition:
    description:
      - The condition that will cause this alert to activate.
    type: dict
    suboptions:
      all_of:
        description:
          - The list of activity log alert conditions.
        required: true
        type: list
        suboptions:
          field:
            description:
              - >-
                The name of the field that this condition will examine. The
                possible values for this field are (case-insensitive):
                'resourceId', 'category', 'caller', 'level', 'operationName',
                'resourceGroup', 'resourceProvider', 'status', 'subStatus',
                'resourceType', or anything beginning with 'properties.'.
            required: true
            type: str
          equals:
            description:
              - >-
                The field value will be compared to this value
                (case-insensitive) to determine if the condition is met.
            required: true
            type: str
  actions:
    description:
      - The actions that will activate when the condition is met.
    type: dict
    suboptions:
      action_groups:
        description:
          - The list of activity log alerts.
        type: list
        suboptions:
          action_group_id:
            description:
              - >-
                The resourceId of the action group. This cannot be null or
                empty.
            required: true
            type: str
          webhook_properties:
            description:
              - >-
                the dictionary of custom properties to include with the post
                operation. These data are appended to the webhook payload.
            type: dictionary
  description:
    description:
      - A description of this activity log alert.
    type: str
  state:
    description:
      - Assert the state of the ActivityLogAlert.
      - >-
        Use C(present) to create or update an ActivityLogAlert and C(absent) to
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
    - name: Create or update an activity log alert
      azure_rm_activitylogalert: 
        activity_log_alert_name: SampleActivityLogAlert
        resource_group_name: Default-ActivityLogAlerts
        

    - name: Delete an activity log alert
      azure_rm_activitylogalert: 
        activity_log_alert_name: SampleActivityLogAlert
        resource_group_name: Default-ActivityLogAlerts
        

    - name: Patch an activity log alert
      azure_rm_activitylogalert: 
        activity_log_alert_name: SampleActivityLogAlert
        resource_group_name: Default-ActivityLogAlerts
        

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
scopes:
  description:
    - >-
      A list of resourceIds that will be used as prefixes. The alert will only
      apply to activityLogs with resourceIds that fall under one of these
      prefixes. This list must include at least one item.
  returned: always
  type: list
  sample: null
enabled:
  description:
    - >-
      Indicates whether this activity log alert is enabled. If an activity log
      alert is not enabled, then none of its actions will be activated.
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
              The field value will be compared to this value (case-insensitive)
              to determine if the condition is met.
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
            - The resourceId of the action group. This cannot be null or empty.
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


class AzureRMActivityLogAlert(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            activity_log_alert_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            scopes=dict(
                type='list',
                disposition='/scopes',
                elements='str'
            ),
            enabled=dict(
                type='bool',
                disposition='/enabled'
            ),
            condition=dict(
                type='dict',
                disposition='/condition',
                options=dict(
                    all_of=dict(
                        type='list',
                        disposition='all_of',
                        required=True,
                        elements='dict',
                        options=dict(
                            field=dict(
                                type='str',
                                disposition='field',
                                required=True
                            ),
                            equals=dict(
                                type='str',
                                disposition='equals',
                                required=True
                            )
                        )
                    )
                )
            ),
            actions=dict(
                type='dict',
                disposition='/actions',
                options=dict(
                    action_groups=dict(
                        type='list',
                        disposition='action_groups',
                        elements='dict',
                        options=dict(
                            action_group_id=dict(
                                type='str',
                                disposition='action_group_id',
                                required=True
                            ),
                            webhook_properties=dict(
                                type='dictionary',
                                disposition='webhook_properties'
                            )
                        )
                    )
                )
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.activity_log_alert_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMActivityLogAlert, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-04-01')

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
            response = self.mgmt_client.activity_log_alerts.create_or_update(resource_group_name=self.resource_group_name,
                                                                             activity_log_alert_name=self.activity_log_alert_name,
                                                                             activity_log_alert=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ActivityLogAlert instance.')
            self.fail('Error creating the ActivityLogAlert instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.activity_log_alerts.delete(resource_group_name=self.resource_group_name,
                                                                   activity_log_alert_name=self.activity_log_alert_name)
        except CloudError as e:
            self.log('Error attempting to delete the ActivityLogAlert instance.')
            self.fail('Error deleting the ActivityLogAlert instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.activity_log_alerts.get(resource_group_name=self.resource_group_name,
                                                                activity_log_alert_name=self.activity_log_alert_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMActivityLogAlert()


if __name__ == '__main__':
    main()
