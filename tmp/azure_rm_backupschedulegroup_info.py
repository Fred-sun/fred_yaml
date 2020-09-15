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
module: azure_rm_backupschedulegroup_info
version_added: '2.9'
short_description: Get BackupScheduleGroup info.
description:
  - Get info of BackupScheduleGroup.
options:
  device_name:
    description:
      - The name of the device.
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
  schedule_group_name:
    description:
      - The name of the schedule group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: BackupScheduleGroupsListByDevice
      azure_rm_backupschedulegroup_info: 
        device_name: HSDK-0NZI14MDTF
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: BackupScheduleGroupsGet
      azure_rm_backupschedulegroup_info: 
        device_name: HSDK-4XY4FI2IVG
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        schedule_group_name: BackupSchGroupForSDKTest
        

'''

RETURN = '''
backup_schedule_groups:
  description: >-
    A list of dict results where the key is the name of the BackupScheduleGroup
    and the values are the facts for that BackupScheduleGroup.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        start_time:
          description:
            - >-
              The start time. When this field is specified we will generate
              Default GrandFather Father Son Backup Schedules.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBackupScheduleGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
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
            schedule_group_name=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.schedule_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-10-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMBackupScheduleGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

        if (self.device_name is not None and
            self.schedule_group_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['backup_schedule_groups'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['backup_schedule_groups'] = self.format_item(self.listbydevice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.backup_schedule_groups.get(device_name=self.device_name,
                                                                   schedule_group_name=self.schedule_group_name,
                                                                   resource_group_name=self.resource_group_name,
                                                                   manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.backup_schedule_groups.list_by_device(device_name=self.device_name,
                                                                              resource_group_name=self.resource_group_name,
                                                                              manager_name=self.manager_name)
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
    AzureRMBackupScheduleGroupInfo()


if __name__ == '__main__':
    main()
