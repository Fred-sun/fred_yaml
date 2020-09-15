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
module: azure_rm_backupschedule
version_added: '2.9'
short_description: Manage Azure BackupSchedule instance.
description:
  - 'Create, update and delete instance of Azure BackupSchedule.'
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  backup_policy_name:
    description:
      - The backup policy name.
    required: true
    type: str
  backup_schedule_name:
    description:
      - The name of the backup schedule to be fetched
      - The backup schedule name.
      - The name the backup schedule.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  kind:
    description:
      - The Kind of the object. Currently only Series8000 is supported
    type: constant
  schedule_recurrence:
    description:
      - The schedule recurrence.
    type: dict
    suboptions:
      recurrence_type:
        description:
          - The recurrence type.
        required: true
        type: sealed-choice
      recurrence_value:
        description:
          - The recurrence value.
        required: true
        type: integer
      weekly_days_list:
        description:
          - >-
            The week days list. Applicable only for schedules of recurrence type
            'weekly'.
        type: list
  backup_type:
    description:
      - The type of backup which needs to be taken.
    type: sealed-choice
  retention_count:
    description:
      - The number of backups to be retained.
    type: integer
  start_time:
    description:
      - The start time of the schedule.
    type: str
  schedule_status:
    description:
      - The schedule status.
    type: sealed-choice
  state:
    description:
      - Assert the state of the BackupSchedule.
      - >-
        Use C(present) to create or update an BackupSchedule and C(absent) to
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
    - name: BackupSchedulesCreateOrUpdate
      azure_rm_backupschedule: 
        backup_policy_name: BkUpPolicy01ForSDKTest
        backup_schedule_name: schedule2
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        kind: Series8000
        properties:
          backup_type: CloudSnapshot
          retention_count: 1
          schedule_recurrence:
            recurrence_type: Weekly
            recurrence_value: 1
            weekly_days_list:
              - Friday
              - Thursday
              - Monday
          schedule_status: Enabled
          start_time: '2017-06-24T01:00:00Z'
        

    - name: BackupSchedulesDelete
      azure_rm_backupschedule: 
        backup_policy_name: BkUpPolicy01ForSDKTest
        backup_schedule_name: schedule1
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the object.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
kind:
  description:
    - The Kind of the object. Currently only Series8000 is supported
  returned: always
  type: constant
  sample: null
schedule_recurrence:
  description:
    - The schedule recurrence.
  returned: always
  type: dict
  sample: null
  contains:
    recurrence_type:
      description:
        - The recurrence type.
      returned: always
      type: sealed-choice
      sample: null
    recurrence_value:
      description:
        - The recurrence value.
      returned: always
      type: integer
      sample: null
    weekly_days_list:
      description:
        - >-
          The week days list. Applicable only for schedules of recurrence type
          'weekly'.
      returned: always
      type: list
      sample: null
backup_type:
  description:
    - The type of backup which needs to be taken.
  returned: always
  type: sealed-choice
  sample: null
retention_count:
  description:
    - The number of backups to be retained.
  returned: always
  type: integer
  sample: null
start_time:
  description:
    - The start time of the schedule.
  returned: always
  type: str
  sample: null
schedule_status:
  description:
    - The schedule status.
  returned: always
  type: sealed-choice
  sample: null
last_successful_run:
  description:
    - The last successful backup run which was triggered for the schedule.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBackupSchedule(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            backup_policy_name=dict(
                type='str',
                required=True
            ),
            backup_schedule_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='constant',
                disposition='/kind'
            ),
            schedule_recurrence=dict(
                type='dict',
                disposition='/schedule_recurrence',
                options=dict(
                    recurrence_type=dict(
                        type='sealed-choice',
                        disposition='recurrence_type',
                        required=True
                    ),
                    recurrence_value=dict(
                        type='integer',
                        disposition='recurrence_value',
                        required=True
                    ),
                    weekly_days_list=dict(
                        type='list',
                        disposition='weekly_days_list',
                        elements='sealed-choice'
                    )
                )
            ),
            backup_type=dict(
                type='sealed-choice',
                disposition='/backup_type'
            ),
            retention_count=dict(
                type='integer',
                disposition='/retention_count'
            ),
            start_time=dict(
                type='str',
                disposition='/start_time'
            ),
            schedule_status=dict(
                type='sealed-choice',
                disposition='/schedule_status'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.backup_policy_name = None
        self.backup_schedule_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBackupSchedule, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
            response = self.mgmt_client.backup_schedules.create_or_update(device_name=self.device_name,
                                                                          backup_policy_name=self.backup_policy_name,
                                                                          backup_schedule_name=self.backup_schedule_name,
                                                                          resource_group_name=self.resource_group_name,
                                                                          manager_name=self.manager_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BackupSchedule instance.')
            self.fail('Error creating the BackupSchedule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.backup_schedules.delete(device_name=self.device_name,
                                                                backup_policy_name=self.backup_policy_name,
                                                                backup_schedule_name=self.backup_schedule_name,
                                                                resource_group_name=self.resource_group_name,
                                                                manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the BackupSchedule instance.')
            self.fail('Error deleting the BackupSchedule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.backup_schedules.get(device_name=self.device_name,
                                                             backup_policy_name=self.backup_policy_name,
                                                             backup_schedule_name=self.backup_schedule_name,
                                                             resource_group_name=self.resource_group_name,
                                                             manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBackupSchedule()


if __name__ == '__main__':
    main()
