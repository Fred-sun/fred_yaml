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
module: azure_rm_backuppolicy
version_added: '2.9'
short_description: Manage Azure BackupPolicy instance.
description:
  - 'Create, update and delete instance of Azure BackupPolicy.'
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  backup_policy_name:
    description:
      - The name of backup policy to be fetched.
      - The name of the backup policy to be created/updated.
      - The name of the backup policy.
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
  volume_ids:
    description:
      - The path IDs of the volumes which are part of the backup policy.
    type: list
  state:
    description:
      - Assert the state of the BackupPolicy.
      - >-
        Use C(present) to create or update an BackupPolicy and C(absent) to
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
    - name: BackupPoliciesCreateOrUpdate
      azure_rm_backuppolicy: 
        backup_policy_name: BkUpPolicy01ForSDKTest
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        kind: Series8000
        properties:
          volume_ids:
            - >-
              /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/ResourceGroupForSDKTest/providers/Microsoft.StorSimple/managers/ManagerForSDKTest1/devices/Device05ForSDKTest/volumeContainers/volumeContainerForSDKTest/volumes/Clonedvolume1
            - >-
              /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/ResourceGroupForSDKTest/providers/Microsoft.StorSimple/managers/ManagerForSDKTest1/devices/Device05ForSDKTest/volumeContainers/volumeContainerForSDKTest/volumes/volume1
        

    - name: BackupPoliciesDelete
      azure_rm_backuppolicy: 
        backup_policy_name: BkUpPolicy01ForSDKTest
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
      Indicates whether at least one of the schedules in the backup policy is
      active or not.
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
      If the backup policy was created by StorSimple Snapshot Manager, then this
      field indicates the hostname of the StorSimple Snapshot Manager.
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


class AzureRMBackupPolicy(AzureRMModuleBaseExt):
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
            volume_ids=dict(
                type='list',
                disposition='/volume_ids',
                elements='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.backup_policy_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBackupPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.backup_policies.create_or_update(device_name=self.device_name,
                                                                         backup_policy_name=self.backup_policy_name,
                                                                         resource_group_name=self.resource_group_name,
                                                                         manager_name=self.manager_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BackupPolicy instance.')
            self.fail('Error creating the BackupPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.backup_policies.delete(device_name=self.device_name,
                                                               backup_policy_name=self.backup_policy_name,
                                                               resource_group_name=self.resource_group_name,
                                                               manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the BackupPolicy instance.')
            self.fail('Error deleting the BackupPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.backup_policies.get(device_name=self.device_name,
                                                            backup_policy_name=self.backup_policy_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBackupPolicy()


if __name__ == '__main__':
    main()
