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
module: azure_rm_restorepoint
version_added: '2.9'
short_description: Manage Azure RestorePoint instance.
description:
  - 'Create, update and delete instance of Azure RestorePoint.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - The name of the database.
    required: true
    type: str
  restore_point_label:
    description:
      - The restore point label to apply
    type: str
  restore_point_name:
    description:
      - The name of the restore point.
    type: str
  state:
    description:
      - Assert the state of the RestorePoint.
      - >-
        Use C(present) to create or update an RestorePoint and C(absent) to
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
    - name: Creates datawarehouse database restore point.
      azure_rm_restorepoint: 
        database_name: testDatabase
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testserver
        restore_point_label: mylabel
        

    - name: Deletes a restore point.
      azure_rm_restorepoint: 
        database_name: testDatabase
        resource_group_name: Default-SQL-SouthEastAsia
        restore_point_name: '131546477590000000'
        server_name: testserver
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
restore_point_type:
  description:
    - The type of restore point
  returned: always
  type: sealed-choice
  sample: null
earliest_restore_date:
  description:
    - The earliest time to which this database can be restored
  returned: always
  type: str
  sample: null
restore_point_creation_date:
  description:
    - The time the backup was taken
  returned: always
  type: str
  sample: null
restore_point_label:
  description:
    - The label of restore point for backup request by user
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRestorePoint(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            restore_point_label=dict(
                type='str',
                disposition='/restore_point_label'
            ),
            restore_point_name=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.restore_point_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRestorePoint, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.restore_points.create(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  database_name=self.database_name,
                                                                  parameters=self.body)
            else:
                response = self.mgmt_client.restore_points.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RestorePoint instance.')
            self.fail('Error creating the RestorePoint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.restore_points.delete(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              database_name=self.database_name,
                                                              restore_point_name=self.restore_point_name)
        except CloudError as e:
            self.log('Error attempting to delete the RestorePoint instance.')
            self.fail('Error deleting the RestorePoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.restore_points.get(resource_group_name=self.resource_group_name,
                                                           server_name=self.server_name,
                                                           database_name=self.database_name,
                                                           restore_point_name=self.restore_point_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRestorePoint()


if __name__ == '__main__':
    main()
