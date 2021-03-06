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
module: azure_rm_longtermretentionmanagedinstancebackup
version_added: '2.9'
short_description: Manage Azure LongTermRetentionManagedInstanceBackup instance.
description:
  - >-
    Create, update and delete instance of Azure
    LongTermRetentionManagedInstanceBackup.
options:
  location_name:
    description:
      - The location of the database.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  database_name:
    description:
      - The name of the managed database.
    required: true
    type: str
  backup_name:
    description:
      - The backup name.
    required: true
    type: str
  state:
    description:
      - Assert the state of the LongTermRetentionManagedInstanceBackup.
      - >-
        Use C(present) to create or update an
        LongTermRetentionManagedInstanceBackup and C(absent) to delete it.
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
    - name: Delete the long term retention backup.
      azure_rm_longtermretentionmanagedinstancebackup: 
        backup_name: 55555555-6666-7777-8888-999999999999;131637960820000000
        database_name: testDatabase
        location_name: japaneast
        managed_instance_name: testInstance
        

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
managed_instance_name:
  description:
    - The managed instance that the backup database belongs to.
  returned: always
  type: str
  sample: null
managed_instance_create_time:
  description:
    - The create time of the instance.
  returned: always
  type: str
  sample: null
database_name:
  description:
    - The name of the database the backup belong to
  returned: always
  type: str
  sample: null
database_deletion_time:
  description:
    - The delete time of the database
  returned: always
  type: str
  sample: null
backup_time:
  description:
    - The time the backup was taken
  returned: always
  type: str
  sample: null
backup_expiration_time:
  description:
    - The time the long term retention backup will expire.
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


class AzureRMLongTermRetentionManagedInstanceBackup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            backup_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location_name = None
        self.managed_instance_name = None
        self.database_name = None
        self.backup_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLongTermRetentionManagedInstanceBackup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2018-06-01-preview')

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
                response = self.mgmt_client.long_term_retention_managed_instance_backups.create()
            else:
                response = self.mgmt_client.long_term_retention_managed_instance_backups.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LongTermRetentionManagedInstanceBackup instance.')
            self.fail('Error creating the LongTermRetentionManagedInstanceBackup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.delete(location_name=self.location_name,
                                                                                            managed_instance_name=self.managed_instance_name,
                                                                                            database_name=self.database_name,
                                                                                            backup_name=self.backup_name)
        except CloudError as e:
            self.log('Error attempting to delete the LongTermRetentionManagedInstanceBackup instance.')
            self.fail('Error deleting the LongTermRetentionManagedInstanceBackup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.get(location_name=self.location_name,
                                                                                         managed_instance_name=self.managed_instance_name,
                                                                                         database_name=self.database_name,
                                                                                         backup_name=self.backup_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLongTermRetentionManagedInstanceBackup()


if __name__ == '__main__':
    main()
