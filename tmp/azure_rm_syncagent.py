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
module: azure_rm_syncagent
version_added: '2.9'
short_description: Manage Azure SyncAgent instance.
description:
  - 'Create, update and delete instance of Azure SyncAgent.'
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
      - The name of the server on which the sync agent is hosted.
    required: true
    type: str
  sync_agent_name:
    description:
      - The name of the sync agent.
    required: true
    type: str
  sync_database_id:
    description:
      - ARM resource id of the sync database in the sync agent.
    type: str
  state:
    description:
      - Assert the state of the SyncAgent.
      - >-
        Use C(present) to create or update an SyncAgent and C(absent) to delete
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
    - name: Create a new sync agent
      azure_rm_syncagent: 
        resource_group_name: syncagentcrud-65440
        server_name: syncagentcrud-8475
        sync_agent_name: syncagentcrud-3187
        properties:
          sync_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-Onebox/providers/Microsoft.Sql/servers/syncagentcrud-8475/databases/sync
        

    - name: Update a sync agent
      azure_rm_syncagent: 
        resource_group_name: syncagentcrud-65440
        server_name: syncagentcrud-8475
        sync_agent_name: syncagentcrud-3187
        properties:
          sync_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-Onebox/providers/Microsoft.Sql/servers/syncagentcrud-8475/databases/sync
        

    - name: Delete a sync agent
      azure_rm_syncagent: 
        resource_group_name: syncagentcrud-65440
        server_name: syncagentcrud-8475
        sync_agent_name: syncagentcrud-3187
        

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
name_properties_name:
  description:
    - Name of the sync agent.
  returned: always
  type: str
  sample: null
sync_database_id:
  description:
    - ARM resource id of the sync database in the sync agent.
  returned: always
  type: str
  sample: null
last_alive_time:
  description:
    - Last alive time of the sync agent.
  returned: always
  type: str
  sample: null
state:
  description:
    - State of the sync agent.
  returned: always
  type: str
  sample: null
is_up_to_date:
  description:
    - If the sync agent version is up to date.
  returned: always
  type: bool
  sample: null
expiry_time:
  description:
    - Expiration time of the sync agent version.
  returned: always
  type: str
  sample: null
version:
  description:
    - Version of the sync agent.
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


class AzureRMSyncAgent(AzureRMModuleBaseExt):
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
            sync_agent_name=dict(
                type='str',
                required=True
            ),
            sync_database_id=dict(
                type='str',
                disposition='/sync_database_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.sync_agent_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSyncAgent, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2015-05-01-preview')

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
            response = self.mgmt_client.sync_agents.create_or_update(resource_group_name=self.resource_group_name,
                                                                     server_name=self.server_name,
                                                                     sync_agent_name=self.sync_agent_name,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SyncAgent instance.')
            self.fail('Error creating the SyncAgent instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sync_agents.delete(resource_group_name=self.resource_group_name,
                                                           server_name=self.server_name,
                                                           sync_agent_name=self.sync_agent_name)
        except CloudError as e:
            self.log('Error attempting to delete the SyncAgent instance.')
            self.fail('Error deleting the SyncAgent instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sync_agents.get(resource_group_name=self.resource_group_name,
                                                        server_name=self.server_name,
                                                        sync_agent_name=self.sync_agent_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSyncAgent()


if __name__ == '__main__':
    main()
