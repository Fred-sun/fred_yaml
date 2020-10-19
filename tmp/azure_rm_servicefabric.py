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
module: azure_rm_servicefabric
version_added: '2.9'
short_description: Manage Azure ServiceFabric instance.
description:
  - 'Create, update and delete instance of Azure ServiceFabric.'
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
  user_name:
    description:
      - The name of the user profile.
    required: true
    type: str
  name:
    description:
      - The name of the service fabric.
    required: true
    type: str
  expand:
    description:
      - >-
        Specify the $expand query. Example:
        'properties($expand=applicableSchedule)'
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  external_service_fabric_id:
    description:
      - The backing service fabric resource's id
    type: str
  environment_id:
    description:
      - >-
        The resource id of the environment under which the service fabric
        resource is present
    type: str
  state:
    description:
      - Assert the state of the ServiceFabric.
      - >-
        Use C(present) to create or update an ServiceFabric and C(absent) to
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
external_service_fabric_id:
  description:
    - The backing service fabric resource's id
  returned: always
  type: str
  sample: null
environment_id:
  description:
    - >-
      The resource id of the environment under which the service fabric resource
      is present
  returned: always
  type: str
  sample: null
applicable_schedule:
  description:
    - The applicable schedule for the virtual machine.
  returned: always
  type: dict
  sample: null
  contains:
    lab_vms_shutdown:
      description:
        - >-
          The auto-shutdown schedule, if one has been set at the lab or lab
          resource level.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - 'The status of the schedule (i.e. Enabled, Disabled)'
          returned: always
          type: str
          sample: null
        task_type:
          description:
            - >-
              The task type of the schedule (e.g. LabVmsShutdownTask,
              LabVmAutoStart).
          returned: always
          type: str
          sample: null
        weekly_recurrence:
          description:
            - >-
              If the schedule will occur only some days of the week, specify the
              weekly recurrence.
          returned: always
          type: dict
          sample: null
          contains:
            weekdays:
              description:
                - >-
                  The days of the week for which the schedule is set (e.g.
                  Sunday, Monday, Tuesday, etc.).
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
                - >-
                  Time in minutes before event at which notification will be
                  sent.
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
    lab_vms_startup:
      description:
        - >-
          The auto-startup schedule, if one has been set at the lab or lab
          resource level.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - 'The status of the schedule (i.e. Enabled, Disabled)'
          returned: always
          type: str
          sample: null
        task_type:
          description:
            - >-
              The task type of the schedule (e.g. LabVmsShutdownTask,
              LabVmAutoStart).
          returned: always
          type: str
          sample: null
        weekly_recurrence:
          description:
            - >-
              If the schedule will occur only some days of the week, specify the
              weekly recurrence.
          returned: always
          type: dict
          sample: null
          contains:
            weekdays:
              description:
                - >-
                  The days of the week for which the schedule is set (e.g.
                  Sunday, Monday, Tuesday, etc.).
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
                - >-
                  Time in minutes before event at which notification will be
                  sent.
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


class AzureRMServiceFabric(AzureRMModuleBaseExt):
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
            user_name=dict(
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
            external_service_fabric_id=dict(
                type='str',
                disposition='/external_service_fabric_id'
            ),
            environment_id=dict(
                type='str',
                disposition='/environment_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.user_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServiceFabric, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.service_fabrics.create_or_update(resource_group_name=self.resource_group_name,
                                                                         lab_name=self.lab_name,
                                                                         user_name=self.user_name,
                                                                         name=self.name,
                                                                         service_fabric=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ServiceFabric instance.')
            self.fail('Error creating the ServiceFabric instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.service_fabrics.delete(resource_group_name=self.resource_group_name,
                                                               lab_name=self.lab_name,
                                                               user_name=self.user_name,
                                                               name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ServiceFabric instance.')
            self.fail('Error deleting the ServiceFabric instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.service_fabrics.get(resource_group_name=self.resource_group_name,
                                                            lab_name=self.lab_name,
                                                            user_name=self.user_name,
                                                            name=self.name,
                                                            expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServiceFabric()


if __name__ == '__main__':
    main()
