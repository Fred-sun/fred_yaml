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
module: azure_rm_jobagent
version_added: '2.9'
short_description: Manage Azure JobAgent instance.
description:
  - 'Create, update and delete instance of Azure JobAgent.'
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
      - The name of the job agent to be retrieved.
      - The name of the job agent to be created or updated.
      - The name of the job agent to be deleted.
      - The name of the job agent to be updated.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  sku:
    description:
      - The name and tier of the SKU.
    type: dict
    suboptions:
      name:
        description:
          - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
        required: true
        type: str
      tier:
        description:
          - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
        type: str
      size:
        description:
          - Size of the particular SKU
        type: str
      family:
        description:
          - >-
            If the service has different generations of hardware, for the same
            SKU, then that can be captured here.
        type: str
      capacity:
        description:
          - Capacity of the particular SKU.
        type: integer
  database_id:
    description:
      - Resource ID of the database to store job metadata in.
    type: str
  state:
    description:
      - Assert the state of the JobAgent.
      - >-
        Use C(present) to create or update an JobAgent and C(absent) to delete
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
    - name: Create or update a job agent with all properties
      azure_rm_jobagent: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        location: southeastasia
        properties:
          database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/databases/db1
        sku:
          name: Agent
          capacity: 100
        tags:
          octopus: agent
        

    - name: Create or update a job agent with minimum properties
      azure_rm_jobagent: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        location: southeastasia
        properties:
          database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/databases/db1
        

    - name: Delete a job agent
      azure_rm_jobagent: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        

    - name: Update a job agent's tags.
      azure_rm_jobagent: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        tags:
          mytag1: myvalue1
        

'''

RETURN = '''
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
sku:
  description:
    - The name and tier of the SKU.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
      returned: always
      type: str
      sample: null
    tier:
      description:
        - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
      returned: always
      type: str
      sample: null
    size:
      description:
        - Size of the particular SKU
      returned: always
      type: str
      sample: null
    family:
      description:
        - >-
          If the service has different generations of hardware, for the same
          SKU, then that can be captured here.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - Capacity of the particular SKU.
      returned: always
      type: integer
      sample: null
database_id:
  description:
    - Resource ID of the database to store job metadata in.
  returned: always
  type: str
  sample: null
state:
  description:
    - The state of the job agent.
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


class AzureRMJobAgent(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    size=dict(
                        type='str',
                        disposition='size'
                    ),
                    family=dict(
                        type='str',
                        disposition='family'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            database_id=dict(
                type='str',
                disposition='/database_id'
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobAgent, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.job_agents.create_or_update(resource_group_name=self.resource_group_name,
                                                                    server_name=self.server_name,
                                                                    job_agent_name=self.job_agent_name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobAgent instance.')
            self.fail('Error creating the JobAgent instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.job_agents.delete(resource_group_name=self.resource_group_name,
                                                          server_name=self.server_name,
                                                          job_agent_name=self.job_agent_name)
        except CloudError as e:
            self.log('Error attempting to delete the JobAgent instance.')
            self.fail('Error deleting the JobAgent instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.job_agents.get(resource_group_name=self.resource_group_name,
                                                       server_name=self.server_name,
                                                       job_agent_name=self.job_agent_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobAgent()


if __name__ == '__main__':
    main()
