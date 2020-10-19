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
module: azure_rm_jobtargetgroup
version_added: '2.9'
short_description: Manage Azure JobTargetGroup instance.
description:
  - 'Create, update and delete instance of Azure JobTargetGroup.'
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
  job_agent_name:
    description:
      - The name of the job agent.
    required: true
    type: str
  target_group_name:
    description:
      - The name of the target group.
    required: true
    type: str
  members:
    description:
      - Members of the target group.
    type: list
    suboptions:
      membership_type:
        description:
          - Whether the target is included or excluded from the group.
        type: sealed-choice
      type:
        description:
          - The target type.
        required: true
        type: str
        choices:
          - TargetGroup
          - SqlDatabase
          - SqlElasticPool
          - SqlShardMap
          - SqlServer
      server_name:
        description:
          - The target server name.
        type: str
      database_name:
        description:
          - The target database name.
        type: str
      elastic_pool_name:
        description:
          - The target elastic pool name.
        type: str
      shard_map_name:
        description:
          - The target shard map.
        type: str
      refresh_credential:
        description:
          - >-
            The resource ID of the credential that is used during job execution
            to connect to the target and determine the list of databases inside
            the target.
        type: str
  state:
    description:
      - Assert the state of the JobTargetGroup.
      - >-
        Use C(present) to create or update an JobTargetGroup and C(absent) to
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
    - name: Create or update a target group with all properties.
      azure_rm_jobtargetgroup: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        target_group_name: targetGroup1
        properties:
          members:
            - type: SqlDatabase
              database_name: database1
              membership_type: Exclude
              server_name: server1
            - type: SqlServer
              membership_type: Include
              refresh_credential: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/credentials/testCredential
              server_name: server1
            - type: SqlElasticPool
              elastic_pool_name: pool1
              membership_type: Include
              refresh_credential: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/credentials/testCredential
              server_name: server2
            - type: SqlShardMap
              database_name: database1
              membership_type: Include
              refresh_credential: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/credentials/testCredential
              server_name: server3
              shard_map_name: shardMap1
        

    - name: Create or update a target group with minimal properties.
      azure_rm_jobtargetgroup: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        target_group_name: targetGroup1
        properties:
          members: []
        

    - name: Delete a target group.
      azure_rm_jobtargetgroup: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        target_group_name: targetGroup1
        

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
members:
  description:
    - Members of the target group.
  returned: always
  type: list
  sample: null
  contains:
    membership_type:
      description:
        - Whether the target is included or excluded from the group.
      returned: always
      type: sealed-choice
      sample: null
    type:
      description:
        - The target type.
      returned: always
      type: str
      sample: null
    server_name:
      description:
        - The target server name.
      returned: always
      type: str
      sample: null
    database_name:
      description:
        - The target database name.
      returned: always
      type: str
      sample: null
    elastic_pool_name:
      description:
        - The target elastic pool name.
      returned: always
      type: str
      sample: null
    shard_map_name:
      description:
        - The target shard map.
      returned: always
      type: str
      sample: null
    refresh_credential:
      description:
        - >-
          The resource ID of the credential that is used during job execution to
          connect to the target and determine the list of databases inside the
          target.
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


class AzureRMJobTargetGroup(AzureRMModuleBaseExt):
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
            job_agent_name=dict(
                type='str',
                required=True
            ),
            target_group_name=dict(
                type='str',
                required=True
            ),
            members=dict(
                type='list',
                disposition='/members',
                elements='dict',
                options=dict(
                    membership_type=dict(
                        type='sealed-choice',
                        disposition='membership_type'
                    ),
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['TargetGroup',
                                 'SqlDatabase',
                                 'SqlElasticPool',
                                 'SqlShardMap',
                                 'SqlServer'],
                        required=True
                    ),
                    server_name=dict(
                        type='str',
                        disposition='server_name'
                    ),
                    database_name=dict(
                        type='str',
                        disposition='database_name'
                    ),
                    elastic_pool_name=dict(
                        type='str',
                        disposition='elastic_pool_name'
                    ),
                    shard_map_name=dict(
                        type='str',
                        disposition='shard_map_name'
                    ),
                    refresh_credential=dict(
                        type='str',
                        disposition='refresh_credential'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.job_agent_name = None
        self.target_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobTargetGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.job_target_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                           server_name=self.server_name,
                                                                           job_agent_name=self.job_agent_name,
                                                                           target_group_name=self.target_group_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobTargetGroup instance.')
            self.fail('Error creating the JobTargetGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.job_target_groups.delete(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 job_agent_name=self.job_agent_name,
                                                                 target_group_name=self.target_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the JobTargetGroup instance.')
            self.fail('Error deleting the JobTargetGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.job_target_groups.get(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              job_agent_name=self.job_agent_name,
                                                              target_group_name=self.target_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobTargetGroup()


if __name__ == '__main__':
    main()
