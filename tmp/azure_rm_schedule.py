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
module: azure_rm_schedule
version_added: '2.9'
short_description: Manage Azure Schedule instance.
description:
  - 'Create, update and delete instance of Azure Schedule.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  name:
    description:
      - The name of the schedule.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=status)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  status:
    description:
      - 'The status of the schedule (i.e. Enabled, Disabled)'
    type: str
    choices:
      - Enabled
      - Disabled
  task_type:
    description:
      - 'The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).'
    type: str
  weekly_recurrence:
    description:
      - >-
        If the schedule will occur only some days of the week, specify the
        weekly recurrence.
    type: dict
    suboptions:
      weekdays:
        description:
          - >-
            The days of the week for which the schedule is set (e.g. Sunday,
            Monday, Tuesday, etc.).
        type: list
      time:
        description:
          - The time of the day the schedule will occur.
        type: str
  time_zone_id:
    description:
      - The time zone ID (e.g. Pacific Standard time).
    type: str
  notification_settings:
    description:
      - Notification settings.
    type: dict
    suboptions:
      status:
        description:
          - >-
            If notifications are enabled for this schedule (i.e. Enabled,
            Disabled).
        type: str
        choices:
          - Enabled
          - Disabled
      time_in_minutes:
        description:
          - Time in minutes before event at which notification will be sent.
        type: integer
      webhook_url:
        description:
          - The webhook URL to which the notification will be sent.
        type: str
      email_recipient:
        description:
          - >-
            The email recipient to send notifications to (can be a list of
            semi-colon separated email addresses).
        type: str
      notification_locale:
        description:
          - >-
            The locale to use when sending a notification (fallback for
            unsupported languages is EN).
        type: str
  target_resource_id:
    description:
      - The resource ID to which the schedule belongs
    type: str
  minute:
    description:
      - Minutes of the hour the schedule will run.
    type: integer
  time:
    description:
      - The time of day the schedule will occur.
    type: str
  state:
    description:
      - Assert the state of the Schedule.
      - >-
        Use C(present) to create or update an Schedule and C(absent) to delete
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
'''

RETURN = '''
id:
  description:
    - The identifier of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
status:
  description:
    - 'The status of the schedule (i.e. Enabled, Disabled)'
  returned: always
  type: str
  sample: null
task_type:
  description:
    - 'The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).'
  returned: always
  type: str
  sample: null
weekly_recurrence:
  description:
    - >-
      If the schedule will occur only some days of the week, specify the weekly
      recurrence.
  returned: always
  type: dict
  sample: null
  contains:
    weekdays:
      description:
        - >-
          The days of the week for which the schedule is set (e.g. Sunday,
          Monday, Tuesday, etc.).
      returned: always
      type: list
      sample: null
    time:
      description:
        - The time of the day the schedule will occur.
      returned: always
      type: str
      sample: null
time_zone_id:
  description:
    - The time zone ID (e.g. Pacific Standard time).
  returned: always
  type: str
  sample: null
notification_settings:
  description:
    - Notification settings.
  returned: always
  type: dict
  sample: null
  contains:
    status:
      description:
        - >-
          If notifications are enabled for this schedule (i.e. Enabled,
          Disabled).
      returned: always
      type: str
      sample: null
    time_in_minutes:
      description:
        - Time in minutes before event at which notification will be sent.
      returned: always
      type: integer
      sample: null
    webhook_url:
      description:
        - The webhook URL to which the notification will be sent.
      returned: always
      type: str
      sample: null
    email_recipient:
      description:
        - >-
          The email recipient to send notifications to (can be a list of
          semi-colon separated email addresses).
      returned: always
      type: str
      sample: null
    notification_locale:
      description:
        - >-
          The locale to use when sending a notification (fallback for
          unsupported languages is EN).
      returned: always
      type: str
      sample: null
created_date:
  description:
    - The creation date of the schedule.
  returned: always
  type: str
  sample: null
target_resource_id:
  description:
    - The resource ID to which the schedule belongs
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning status of the resource.
  returned: always
  type: str
  sample: null
unique_identifier:
  description:
    - The unique immutable identifier of a resource (Guid).
  returned: always
  type: str
  sample: null
minute:
  description:
    - Minutes of the hour the schedule will run.
  returned: always
  type: integer
  sample: null
time:
  description:
    - The time of day the schedule will occur.
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSchedule(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['Enabled',
                         'Disabled']
            ),
            task_type=dict(
                type='str',
                disposition='/task_type'
            ),
            weekly_recurrence=dict(
                type='dict',
                disposition='/weekly_recurrence',
                options=dict(
                    weekdays=dict(
                        type='list',
                        disposition='weekdays',
                        elements='str'
                    ),
                    time=dict(
                        type='str',
                        disposition='time'
                    )
                )
            ),
            time_zone_id=dict(
                type='str',
                disposition='/time_zone_id'
            ),
            notification_settings=dict(
                type='dict',
                disposition='/notification_settings',
                options=dict(
                    status=dict(
                        type='str',
                        disposition='status',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    time_in_minutes=dict(
                        type='integer',
                        disposition='time_in_minutes'
                    ),
                    webhook_url=dict(
                        type='str',
                        disposition='webhook_url'
                    ),
                    email_recipient=dict(
                        type='str',
                        disposition='email_recipient'
                    ),
                    notification_locale=dict(
                        type='str',
                        disposition='notification_locale'
                    )
                )
            ),
            target_resource_id=dict(
                type='str',
                disposition='/target_resource_id'
            ),
            minute=dict(
                type='integer',
                disposition='/minute'
            ),
            time=dict(
                type='str',
                disposition='/time'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSchedule, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.schedules.create_or_update(resource_group_name=self.resource_group_name,
                                                                   lab_name=self.lab_name,
                                                                   name=self.name,
                                                                   schedule=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Schedule instance.')
            self.fail('Error creating the Schedule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.schedules.delete(resource_group_name=self.resource_group_name,
                                                         lab_name=self.lab_name,
                                                         name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Schedule instance.')
            self.fail('Error deleting the Schedule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.schedules.get(resource_group_name=self.resource_group_name,
                                                      lab_name=self.lab_name,
                                                      name=self.name,
                                                      expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSchedule()


if __name__ == '__main__':
    main()
