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
module: azure_rm_syncmember_info
version_added: '2.9'
short_description: Get SyncMember info.
description:
  - Get info of SyncMember.
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
      - The name of the sync group.
    required: true
    type: str
  sync_member_name:
    description:
      - The name of the sync member.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a sync member
      azure_rm_syncmember_info: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        sync_member_name: syncgroupcrud-4879
        

    - name: List sync members under a sync group
      azure_rm_syncmember_info: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        

    - name: Get a sync member schema
      azure_rm_syncmember_info: 
        database_name: syncgroupcrud-4328
        resource_group_name: syncgroupcrud-65440
        server_name: syncgroupcrud-8475
        sync_group_name: syncgroupcrud-3187
        sync_member_name: syncgroupcrud-4879
        

'''

RETURN = '''
sync_members:
  description: >-
    A list of dict results where the key is the name of the SyncMember and the
    values are the facts for that SyncMember.
  returned: always
  type: complex
  contains:
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
          ARM resource id of the sync member logical database, for sync members
          in Azure.
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
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
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
              ARM resource id of the sync member logical database, for sync
              members in Azure.
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
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSyncMemberInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.sync_group_name = None
        self.sync_member_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSyncMemberInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.sync_group_name is not None and
            self.sync_member_name is not None):
            self.results['sync_members'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.sync_group_name is not None and
              self.sync_member_name is not None):
            self.results['sync_members'] = self.format_item(self.listmemberschema())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.sync_group_name is not None):
            self.results['sync_members'] = self.format_item(self.listbysyncgroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sync_members.get(resource_group_name=self.resource_group_name,
                                                         server_name=self.server_name,
                                                         database_name=self.database_name,
                                                         sync_group_name=self.sync_group_name,
                                                         sync_member_name=self.sync_member_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmemberschema(self):
        response = None

        try:
            response = self.mgmt_client.sync_members.list_member_schema(resource_group_name=self.resource_group_name,
                                                                        server_name=self.server_name,
                                                                        database_name=self.database_name,
                                                                        sync_group_name=self.sync_group_name,
                                                                        sync_member_name=self.sync_member_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysyncgroup(self):
        response = None

        try:
            response = self.mgmt_client.sync_members.list_by_sync_group(resource_group_name=self.resource_group_name,
                                                                        server_name=self.server_name,
                                                                        database_name=self.database_name,
                                                                        sync_group_name=self.sync_group_name)
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
    AzureRMSyncMemberInfo()


if __name__ == '__main__':
    main()
