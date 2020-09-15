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
module: azure_rm_iscsidisk
version_added: '2.9'
short_description: Manage Azure IscsiDisk instance.
description:
  - 'Create, update and delete instance of Azure IscsiDisk.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  iscsi_server_name:
    description:
      - The iSCSI server name.
    required: true
    type: str
  disk_name:
    description:
      - The disk name.
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
  description:
    description:
      - The description.
    type: str
  disk_status:
    description:
      - The disk status.
    type: sealed-choice
  access_control_records:
    description:
      - The access control records.
    type: list
  data_policy:
    description:
      - The data policy.
    type: sealed-choice
  provisioned_capacity_in_bytes:
    description:
      - The provisioned capacity in bytes.
    type: integer
  monitoring_status:
    description:
      - The monitoring.
    type: sealed-choice
  state:
    description:
      - Assert the state of the IscsiDisk.
      - >-
        Use C(present) to create or update an IscsiDisk and C(absent) to delete
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
    - name: IscsiDisksCreateOrUpdate
      azure_rm_iscsidisk: 
        device_name: HSDK-0NZI14MDTF
        disk_name: Auto-TestIscsiDisk1
        iscsi_server_name: HSDK-0NZI14MDTF
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiDisksDelete
      azure_rm_iscsidisk: 
        device_name: HSDK-UGU4PITWNI
        disk_name: ClonedTieredIscsiDiskForSDKTest
        iscsi_server_name: HSDK-UGU4PITWNI
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

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
description:
  description:
    - The description.
  returned: always
  type: str
  sample: null
disk_status:
  description:
    - The disk status.
  returned: always
  type: sealed-choice
  sample: null
access_control_records:
  description:
    - The access control records.
  returned: always
  type: list
  sample: null
data_policy:
  description:
    - The data policy.
  returned: always
  type: sealed-choice
  sample: null
provisioned_capacity_in_bytes:
  description:
    - The provisioned capacity in bytes.
  returned: always
  type: integer
  sample: null
used_capacity_in_bytes:
  description:
    - The used capacity in bytes.
  returned: always
  type: integer
  sample: null
local_used_capacity_in_bytes:
  description:
    - The local used capacity in bytes.
  returned: always
  type: integer
  sample: null
monitoring_status:
  description:
    - The monitoring.
  returned: always
  type: sealed-choice
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


class AzureRMIscsiDisk(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            iscsi_server_name=dict(
                type='str',
                required=True
            ),
            disk_name=dict(
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
            description=dict(
                type='str',
                disposition='/description'
            ),
            disk_status=dict(
                type='sealed-choice',
                disposition='/disk_status'
            ),
            access_control_records=dict(
                type='list',
                disposition='/access_control_records',
                elements='str'
            ),
            data_policy=dict(
                type='sealed-choice',
                disposition='/data_policy'
            ),
            provisioned_capacity_in_bytes=dict(
                type='integer',
                disposition='/provisioned_capacity_in_bytes'
            ),
            monitoring_status=dict(
                type='sealed-choice',
                disposition='/monitoring_status'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.iscsi_server_name = None
        self.disk_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIscsiDisk, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.iscsi_disks.create_or_update(device_name=self.device_name,
                                                                     iscsi_server_name=self.iscsi_server_name,
                                                                     disk_name=self.disk_name,
                                                                     resource_group_name=self.resource_group_name,
                                                                     manager_name=self.manager_name,
                                                                     iscsi_disk=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IscsiDisk instance.')
            self.fail('Error creating the IscsiDisk instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.iscsi_disks.delete(device_name=self.device_name,
                                                           iscsi_server_name=self.iscsi_server_name,
                                                           disk_name=self.disk_name,
                                                           resource_group_name=self.resource_group_name,
                                                           manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the IscsiDisk instance.')
            self.fail('Error deleting the IscsiDisk instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.iscsi_disks.get(device_name=self.device_name,
                                                        iscsi_server_name=self.iscsi_server_name,
                                                        disk_name=self.disk_name,
                                                        resource_group_name=self.resource_group_name,
                                                        manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIscsiDisk()


if __name__ == '__main__':
    main()
