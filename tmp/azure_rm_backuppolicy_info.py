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
module: azure_rm_backuppolicy_info
version_added: '2.9'
short_description: Get BackupPolicy info.
description:
  - Get info of BackupPolicy.
options:
  device_name:
    description:
      - The device name
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
  backup_policy_name:
    description:
      - The name of backup policy to be fetched.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: BackupPoliciesListByDevice
      azure_rm_backuppolicy_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: BackupPoliciesGet
      azure_rm_backuppolicy_info: 
        backup_policy_name: BkUpPolicy01ForSDKTest
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
backup_policies:
  description: >-
    A list of dict results where the key is the name of the BackupPolicy and the
    values are the facts for that BackupPolicy.
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
        volume_ids:
          description:
            - The path IDs of the volumes which are part of the backup policy.
          returned: always
          type: list
          sample: null
        next_backup_time:
          description:
            - The time of the next backup for the backup policy.
          returned: always
          type: str
          sample: null
        last_backup_time:
          description:
            - The time of the last backup for the backup policy.
          returned: always
          type: str
          sample: null
        schedules_count:
          description:
            - The count of schedules the backup policy contains.
          returned: always
          type: integer
          sample: null
        scheduled_backup_status:
          description:
            - >-
              Indicates whether at least one of the schedules in the backup
              policy is active or not.
          returned: always
          type: sealed-choice
          sample: null
        backup_policy_creation_type:
          description:
            - >-
              The backup policy creation type. Indicates whether this was
              created through SaaS or through StorSimple Snapshot Manager.
          returned: always
          type: sealed-choice
          sample: null
        ssm_host_name:
          description:
            - >-
              If the backup policy was created by StorSimple Snapshot Manager,
              then this field indicates the hostname of the StorSimple Snapshot
              Manager.
          returned: always
          type: str
          sample: null
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
    volume_ids:
      description:
        - The path IDs of the volumes which are part of the backup policy.
      returned: always
      type: list
      sample: null
    next_backup_time:
      description:
        - The time of the next backup for the backup policy.
      returned: always
      type: str
      sample: null
    last_backup_time:
      description:
        - The time of the last backup for the backup policy.
      returned: always
      type: str
      sample: null
    schedules_count:
      description:
        - The count of schedules the backup policy contains.
      returned: always
      type: integer
      sample: null
    scheduled_backup_status:
      description:
        - >-
          Indicates whether at least one of the schedules in the backup policy
          is active or not.
      returned: always
      type: sealed-choice
      sample: null
    backup_policy_creation_type:
      description:
        - >-
          The backup policy creation type. Indicates whether this was created
          through SaaS or through StorSimple Snapshot Manager.
      returned: always
      type: sealed-choice
      sample: null
    ssm_host_name:
      description:
        - >-
          If the backup policy was created by StorSimple Snapshot Manager, then
          this field indicates the hostname of the StorSimple Snapshot Manager.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBackupPolicyInfo(AzureRMModuleBase):
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
            backup_policy_name=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.backup_policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMBackupPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.backup_policy_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['backup_policies'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['backup_policies'] = self.format_item(self.listbydevice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.backup_policies.get(device_name=self.device_name,
                                                            backup_policy_name=self.backup_policy_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.backup_policies.list_by_device(device_name=self.device_name,
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
    AzureRMBackupPolicyInfo()


if __name__ == '__main__':
    main()
