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
module: azure_rm_syncagent_info
version_added: '2.9'
short_description: Get SyncAgent info.
description:
  - Get info of SyncAgent.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a sync agent
      azure_rm_syncagent_info: 
        resource_group_name: syncagentcrud-65440
        server_name: syncagentcrud-8475
        sync_agent_name: syncagentcrud-3187
        

    - name: Get sync agents under a server
      azure_rm_syncagent_info: 
        resource_group_name: syncagentcrud-65440
        server_name: syncagentcrud-8475
        

    - name: Get sync agent linked databases
      azure_rm_syncagent_info: 
        resource_group_name: syncagentcrud-65440
        server_name: syncagentcrud-8475
        sync_agent_name: syncagentcrud-3187
        

'''

RETURN = '''
sync_agents:
  description: >-
    A list of dict results where the key is the name of the SyncAgent and the
    values are the facts for that SyncAgent.
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
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
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


class AzureRMSyncAgentInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.sync_agent_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSyncAgentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.sync_agent_name is not None):
            self.results['sync_agents'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.sync_agent_name is not None):
            self.results['sync_agents'] = self.format_item(self.listlinkeddatabase())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['sync_agents'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sync_agents.get(resource_group_name=self.resource_group_name,
                                                        server_name=self.server_name,
                                                        sync_agent_name=self.sync_agent_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listlinkeddatabase(self):
        response = None

        try:
            response = self.mgmt_client.sync_agents.list_linked_database(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         sync_agent_name=self.sync_agent_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.sync_agents.list_by_server(resource_group_name=self.resource_group_name,
                                                                   server_name=self.server_name)
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
    AzureRMSyncAgentInfo()


if __name__ == '__main__':
    main()
