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
module: azure_rm_accesscontrolrecord
version_added: '2.9'
short_description: Manage Azure AccessControlRecord instance.
description:
  - 'Create, update and delete instance of Azure AccessControlRecord.'
options:
  access_control_record_name:
    description:
      - Name of access control record to be fetched.
      - The name of the access control record.
      - The name of the access control record to delete.
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
  initiator_name:
    description:
      - The iSCSI initiator name (IQN).
    type: str
  state:
    description:
      - Assert the state of the AccessControlRecord.
      - >-
        Use C(present) to create or update an AccessControlRecord and C(absent)
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
    - name: AccessControlRecordsCreateOrUpdate
      azure_rm_accesscontrolrecord: 
        access_control_record_name: ACRForTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        properties:
          initiator_name: 'iqn.2017-06.com.contoso:ForTest'
        

    - name: AccessControlRecordsDelete
      azure_rm_accesscontrolrecord: 
        access_control_record_name: ACRForTest
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
initiator_name:
  description:
    - The iSCSI initiator name (IQN).
  returned: always
  type: str
  sample: null
volume_count:
  description:
    - The number of volumes using the access control record.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAccessControlRecord(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            access_control_record_name=dict(
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
            initiator_name=dict(
                type='str',
                disposition='/initiator_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.access_control_record_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAccessControlRecord, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.access_control_records.create_or_update(access_control_record_name=self.access_control_record_name,
                                                                                resource_group_name=self.resource_group_name,
                                                                                manager_name=self.manager_name,
                                                                                parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AccessControlRecord instance.')
            self.fail('Error creating the AccessControlRecord instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.access_control_records.delete(access_control_record_name=self.access_control_record_name,
                                                                      resource_group_name=self.resource_group_name,
                                                                      manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the AccessControlRecord instance.')
            self.fail('Error deleting the AccessControlRecord instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.access_control_records.get(access_control_record_name=self.access_control_record_name,
                                                                   resource_group_name=self.resource_group_name,
                                                                   manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAccessControlRecord()


if __name__ == '__main__':
    main()
