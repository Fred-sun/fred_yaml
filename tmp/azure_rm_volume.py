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
module: azure_rm_volume
version_added: '2.9'
short_description: Manage Azure Volume instance.
description:
  - 'Create, update and delete instance of Azure Volume.'
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  volume_container_name:
    description:
      - The volume container name.
    required: true
    type: str
  volume_name:
    description:
      - The volume name.
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
  size_in_bytes:
    description:
      - The size of the volume in bytes.
    type: integer
  volume_type:
    description:
      - The type of the volume.
    type: sealed-choice
  access_control_record_ids:
    description:
      - 'The IDs of the access control records, associated with the volume.'
    type: list
  volume_status:
    description:
      - The volume status.
    type: sealed-choice
  monitoring_status:
    description:
      - The monitoring status of the volume.
    type: sealed-choice
  state:
    description:
      - Assert the state of the Volume.
      - Use C(present) to create or update an Volume and C(absent) to delete it.
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
    - name: VolumesCreateOrUpdate
      azure_rm_volume: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: VolumeContainerForSDKTest
        volume_name: Volume1ForSDKTest
        properties:
          access_control_record_ids:
            - >-
              /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/ResourceGroupForSDKTest/providers/Microsoft.StorSimple/managers/ManagerForSDKTest1/accessControlRecords/ACR2
          monitoring_status: Enabled
          size_in_bytes: 5368709120
          volume_status: Offline
          volume_type: Tiered
        

    - name: VolumesDelete
      azure_rm_volume: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: VolumeContainerForSDKTest
        volume_name: Volume1ForSDKTest
        

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
size_in_bytes:
  description:
    - The size of the volume in bytes.
  returned: always
  type: integer
  sample: null
volume_type:
  description:
    - The type of the volume.
  returned: always
  type: sealed-choice
  sample: null
volume_container_id:
  description:
    - 'The ID of the volume container, in which this volume is created.'
  returned: always
  type: str
  sample: null
access_control_record_ids:
  description:
    - 'The IDs of the access control records, associated with the volume.'
  returned: always
  type: list
  sample: null
volume_status:
  description:
    - The volume status.
  returned: always
  type: sealed-choice
  sample: null
operation_status:
  description:
    - The operation status on the volume.
  returned: always
  type: sealed-choice
  sample: null
backup_status:
  description:
    - The backup status of the volume.
  returned: always
  type: sealed-choice
  sample: null
monitoring_status:
  description:
    - The monitoring status of the volume.
  returned: always
  type: sealed-choice
  sample: null
backup_policy_ids:
  description:
    - 'The IDs of the backup policies, in which this volume is part of.'
  returned: always
  type: list
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


class AzureRMVolume(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            volume_container_name=dict(
                type='str',
                required=True
            ),
            volume_name=dict(
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
            size_in_bytes=dict(
                type='integer',
                disposition='/size_in_bytes'
            ),
            volume_type=dict(
                type='sealed-choice',
                disposition='/volume_type'
            ),
            access_control_record_ids=dict(
                type='list',
                disposition='/access_control_record_ids',
                elements='str'
            ),
            volume_status=dict(
                type='sealed-choice',
                disposition='/volume_status'
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
        self.volume_container_name = None
        self.volume_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVolume, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.volumes.create_or_update(device_name=self.device_name,
                                                                 volume_container_name=self.volume_container_name,
                                                                 volume_name=self.volume_name,
                                                                 resource_group_name=self.resource_group_name,
                                                                 manager_name=self.manager_name,
                                                                 parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Volume instance.')
            self.fail('Error creating the Volume instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.volumes.delete(device_name=self.device_name,
                                                       volume_container_name=self.volume_container_name,
                                                       volume_name=self.volume_name,
                                                       resource_group_name=self.resource_group_name,
                                                       manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the Volume instance.')
            self.fail('Error deleting the Volume instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.volumes.get(device_name=self.device_name,
                                                    volume_container_name=self.volume_container_name,
                                                    volume_name=self.volume_name,
                                                    resource_group_name=self.resource_group_name,
                                                    manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVolume()


if __name__ == '__main__':
    main()
