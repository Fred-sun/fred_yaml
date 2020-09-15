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
module: azure_rm_backupschedulegroup
version_added: '2.9'
short_description: Manage Azure BackupScheduleGroup instance.
description:
  - 'Create, update and delete instance of Azure BackupScheduleGroup.'
options:
  device_name:
    description:
      - The name of the device.
    required: true
    type: str
  schedule_group_name:
    description:
      - The name of the schedule group.
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
  start_time:
    description:
      - >-
        The start time. When this field is specified we will generate Default
        GrandFather Father Son Backup Schedules.
    type: dict
    suboptions:
      hour:
        description:
          - The hour.
        required: true
        type: integer
      minute:
        description:
          - The minute.
        required: true
        type: integer
  state:
    description:
      - Assert the state of the BackupScheduleGroup.
      - >-
        Use C(present) to create or update an BackupScheduleGroup and C(absent)
        to delete it.
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
    - name: BackupScheduleGroupsCreateOrUpdate
      azure_rm_backupschedulegroup: 
        device_name: HSDK-4XY4FI2IVG
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        schedule_group_name: BackupSchGroupForSDKTest
        

    - name: BackupScheduleGroupsDelete
      azure_rm_backupschedulegroup: 
        device_name: HSDK-DMNJB2PET0
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        schedule_group_name: BackupSchGroupForSDKTest
        

'''

RETURN = '''
id:
  description:
    - The identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type.
  returned: always
  type: str
  sample: null
start_time:
  description:
    - >-
      The start time. When this field is specified we will generate Default
      GrandFather Father Son Backup Schedules.
  returned: always
  type: dict
  sample: null
  contains:
    hour:
      description:
        - The hour.
      returned: always
      type: integer
      sample: null
    minute:
      description:
        - The minute.
      returned: always
      type: integer
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBackupScheduleGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            schedule_group_name=dict(
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
            start_time=dict(
                type='dict',
                disposition='/start_time',
                options=dict(
                    hour=dict(
                        type='integer',
                        disposition='hour',
                        required=True
                    ),
                    minute=dict(
                        type='integer',
                        disposition='minute',
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

        self.device_name = None
        self.schedule_group_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBackupScheduleGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

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
            response = self.mgmt_client.backup_schedule_groups.create_or_update(device_name=self.device_name,
                                                                                schedule_group_name=self.schedule_group_name,
                                                                                resource_group_name=self.resource_group_name,
                                                                                manager_name=self.manager_name,
                                                                                schedule_group=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BackupScheduleGroup instance.')
            self.fail('Error creating the BackupScheduleGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.backup_schedule_groups.delete(device_name=self.device_name,
                                                                      schedule_group_name=self.schedule_group_name,
                                                                      resource_group_name=self.resource_group_name,
                                                                      manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the BackupScheduleGroup instance.')
            self.fail('Error deleting the BackupScheduleGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.backup_schedule_groups.get(device_name=self.device_name,
                                                                   schedule_group_name=self.schedule_group_name,
                                                                   resource_group_name=self.resource_group_name,
                                                                   manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBackupScheduleGroup()


if __name__ == '__main__':
    main()
