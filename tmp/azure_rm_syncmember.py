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
module: azure_rm_syncmember
version_added: '2.9'
short_description: Manage Azure SyncMember instance.
description:
  - 'Create, update and delete instance of Azure SyncMember.'
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
      - The name of the database on which the sync group is hosted.
    required: true
    type: str
  sync_group_name:
    description:
      - The name of the sync group on which the sync member is hosted.
    required: true
    type: str
  sync_member_name:
    description:
      - The name of the sync member.
    required: true
    type: str
  database_type:
    description:
      - Database type of the sync member.
    type: str
    choices:
      - AzureSqlDatabase
      - SqlServerDatabase
  sync_agent_id:
    description:
      - ARM resource id of the sync agent in the sync member.
    type: str
  sqlserver_database_id:
    description:
      - SQL Server database id of the sync member.
    type: uuid
  sync_member_azure_database_resource_id:
    description:
      - >-
        ARM resource id of the sync member logical database, for sync members in
        Azure.
    type: str
  use_private_link_connection:
    description:
      - Whether to use private link connection.
    type: bool
  sync_member_properties_server_name:
    description:
      - Server name of the member database in the sync member
    type: str
  sync_member_properties_database_name:
    description:
      - Database name of the member database in the sync member.
    type: str
  user_name:
    description:
      - User name of the member database in the sync member.
    type: str
  password:
    description:
      - Password of the member database in the sync member.
    type: str
  sync_direction:
    description:
      - Sync direction of the sync member.
    type: str
    choices:
      - Bidirectional
      - OneWayMemberToHub
      - OneWayHubToMember
  state:
    description:
      - Assert the state of the SyncMember.
      - >-
        Use C(present) to create or update an SyncMember and C(absent) to delete
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
    - name: Create a new sync member
      azure_rm_syncmember: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        sync_member_name: syncgroupcrud-4879
        properties:
          database_name: syncgroupcrud-7421
          database_type: AzureSqlDatabase
          server_name: syncgroupcrud-3379.database.windows.net
          sync_direction: Bidirectional
          sync_member_azure_database_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/syncgroupcrud-65440/providers/Microsoft.Sql/servers/syncgroupcrud-8475/databases/syncgroupcrud-4328
          use_private_link_connection: true
          user_name: myUser
        

    - name: Update a sync member
      azure_rm_syncmember: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        sync_member_name: syncgroupcrud-4879
        properties:
          database_name: syncgroupcrud-7421
          database_type: AzureSqlDatabase
          server_name: syncgroupcrud-3379.database.windows.net
          sync_direction: Bidirectional
          sync_member_azure_database_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/syncgroupcrud-65440/providers/Microsoft.Sql/servers/syncgroupcrud-8475/databases/syncgroupcrud-4328
          use_private_link_connection: true
          user_name: myUser
        

    - name: Delete a sync member
      azure_rm_syncmember: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        sync_member_name: syncgroupcrud-4879
        

    - name: Update an existing sync member
      azure_rm_syncmember: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        sync_member_name: syncgroupcrud-4879
        properties:
          database_name: syncgroupcrud-7421
          database_type: AzureSqlDatabase
          server_name: syncgroupcrud-3379.database.windows.net
          sync_direction: Bidirectional
          sync_member_azure_database_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/syncgroupcrud-65440/providers/Microsoft.Sql/servers/syncgroupcrud-8475/databases/syncgroupcrud-4328
          use_private_link_connection: true
          user_name: myUser
        

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
database_type:
  description:
    - Database type of the sync member.
  returned: always
  type: str
  sample: null
sync_agent_id:
  description:
    - ARM resource id of the sync agent in the sync member.
  returned: always
  type: str
  sample: null
sqlserver_database_id:
  description:
    - SQL Server database id of the sync member.
  returned: always
  type: uuid
  sample: null
sync_member_azure_database_resource_id:
  description:
    - >-
      ARM resource id of the sync member logical database, for sync members in
      Azure.
  returned: always
  type: str
  sample: null
use_private_link_connection:
  description:
    - Whether to use private link connection.
  returned: always
  type: bool
  sample: null
server_name:
  description:
    - Server name of the member database in the sync member
  returned: always
  type: str
  sample: null
database_name:
  description:
    - Database name of the member database in the sync member.
  returned: always
  type: str
  sample: null
user_name:
  description:
    - User name of the member database in the sync member.
  returned: always
  type: str
  sample: null
password:
  description:
    - Password of the member database in the sync member.
  returned: always
  type: str
  sample: null
sync_direction:
  description:
    - Sync direction of the sync member.
  returned: always
  type: str
  sample: null
sync_state:
  description:
    - Sync state of the sync member.
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


class AzureRMSyncMember(AzureRMModuleBaseExt):
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
            sync_group_name=dict(
                type='str',
                required=True
            ),
            sync_member_name=dict(
                type='str',
                required=True
            ),
            database_type=dict(
                type='str',
                disposition='/database_type',
                choices=['AzureSqlDatabase',
                         'SqlServerDatabase']
            ),
            sync_agent_id=dict(
                type='str',
                disposition='/sync_agent_id'
            ),
            sqlserver_database_id=dict(
                type='uuid',
                disposition='/sqlserver_database_id'
            ),
            sync_member_azure_database_resource_id=dict(
                type='str',
                disposition='/sync_member_azure_database_resource_id'
            ),
            use_private_link_connection=dict(
                type='bool',
                disposition='/use_private_link_connection'
            ),
            sync_member_properties_server_name=dict(
                type='str',
                disposition='/sync_member_properties_server_name'
            ),
            sync_member_properties_database_name=dict(
                type='str',
                disposition='/sync_member_properties_database_name'
            ),
            user_name=dict(
                type='str',
                disposition='/user_name'
            ),
            password=dict(
                type='str',
                disposition='/password'
            ),
            sync_direction=dict(
                type='str',
                disposition='/sync_direction',
                choices=['Bidirectional',
                         'OneWayMemberToHub',
                         'OneWayHubToMember']
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
        self.sync_group_name = None
        self.sync_member_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSyncMember, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-06-01-preview')

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
            response = self.mgmt_client.sync_members.create_or_update(resource_group_name=self.resource_group_name,
                                                                      server_name=self.server_name,
                                                                      database_name=self.database_name,
                                                                      sync_group_name=self.sync_group_name,
                                                                      sync_member_name=self.sync_member_name,
                                                                      parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SyncMember instance.')
            self.fail('Error creating the SyncMember instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sync_members.delete(resource_group_name=self.resource_group_name,
                                                            server_name=self.server_name,
                                                            database_name=self.database_name,
                                                            sync_group_name=self.sync_group_name,
                                                            sync_member_name=self.sync_member_name)
        except CloudError as e:
            self.log('Error attempting to delete the SyncMember instance.')
            self.fail('Error deleting the SyncMember instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sync_members.get(resource_group_name=self.resource_group_name,
                                                         server_name=self.server_name,
                                                         database_name=self.database_name,
                                                         sync_group_name=self.sync_group_name,
                                                         sync_member_name=self.sync_member_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSyncMember()


if __name__ == '__main__':
    main()
