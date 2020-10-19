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
module: azure_rm_jobstep
version_added: '2.9'
short_description: Manage Azure JobStep instance.
description:
  - 'Create, update and delete instance of Azure JobStep.'
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
  job_name:
    description:
      - The name of the job.
    required: true
    type: str
  step_name:
    description:
      - The name of the job step.
      - The name of the job step to delete.
    required: true
    type: str
  step_id:
    description:
      - >-
        The job step's index within the job. If not specified when creating the
        job step, it will be created as the last step. If not specified when
        updating the job step, the step id is not modified.
    type: integer
  target_group:
    description:
      - >-
        The resource ID of the target group that the job step will be executed
        on.
    type: str
  credential:
    description:
      - >-
        The resource ID of the job credential that will be used to connect to
        the targets.
    type: str
  action:
    description:
      - The action payload of the job step.
    type: dict
    suboptions:
      type:
        description:
          - Type of action being executed by the job step.
        type: str
        choices:
          - TSql
      source:
        description:
          - The source of the action to execute.
        type: str
        choices:
          - Inline
      value:
        description:
          - >-
            The action value, for example the text of the T-SQL script to
            execute.
        required: true
        type: str
  output:
    description:
      - Output destination properties of the job step.
    type: dict
    suboptions:
      type:
        description:
          - The output destination type.
        type: str
        choices:
          - SqlDatabase
      subscription_id:
        description:
          - The output destination subscription id.
        type: uuid
      resource_group_name:
        description:
          - The output destination resource group.
        type: str
      server_name:
        description:
          - The output destination server name.
        required: true
        type: str
      database_name:
        description:
          - The output destination database.
        required: true
        type: str
      schema_name:
        description:
          - The output destination schema.
        type: str
      table_name:
        description:
          - The output destination table.
        required: true
        type: str
      credential:
        description:
          - >-
            The resource ID of the credential to use to connect to the output
            destination.
        required: true
        type: str
  execution_options:
    description:
      - Execution options for the job step.
    type: dict
    suboptions:
      timeout_seconds:
        description:
          - Execution timeout for the job step.
        type: integer
      retry_attempts:
        description:
          - >-
            Maximum number of times the job step will be reattempted if the
            first attempt fails.
        type: integer
      initial_retry_interval_seconds:
        description:
          - Initial delay between retries for job step execution.
        type: integer
      maximum_retry_interval_seconds:
        description:
          - >-
            The maximum amount of time to wait between retries for job step
            execution.
        type: integer
      retry_interval_backoff_multiplier:
        description:
          - The backoff multiplier for the time between retries.
        type: number
  state:
    description:
      - Assert the state of the JobStep.
      - >-
        Use C(present) to create or update an JobStep and C(absent) to delete
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
    - name: Create or update a job step with all properties specified.
      azure_rm_jobstep: 
        job_agent_name: agent1
        job_name: job1
        resource_group_name: group1
        server_name: server1
        step_name: step1
        properties:
          action:
            type: TSql
            source: Inline
            value: select 2
          credential: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/credentials/cred1
          execution_options:
            initial_retry_interval_seconds: 11
            maximum_retry_interval_seconds: 222
            retry_attempts: 42
            retry_interval_backoff_multiplier: 3
            timeout_seconds: 1234
          output:
            type: SqlDatabase
            credential: >-
              /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/credentials/cred0
            database_name: database3
            resource_group_name: group3
            schema_name: myschema1234
            server_name: server3
            subscription_id: 3501b905-a848-4b5d-96e8-b253f62d735a
            table_name: mytable5678
          step_id: 1
          target_group: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/targetGroups/targetGroup1
        

    - name: Create or update a job step with minimal properties specified.
      azure_rm_jobstep: 
        job_agent_name: agent1
        job_name: job1
        resource_group_name: group1
        server_name: server1
        step_name: step1
        properties:
          action:
            value: select 1
          credential: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/credentials/cred0
          target_group: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/group1/providers/Microsoft.Sql/servers/server1/jobAgents/agent1/targetGroups/targetGroup0
        

    - name: Delete a job step.
      azure_rm_jobstep: 
        job_agent_name: agent1
        job_name: job1
        resource_group_name: group1
        server_name: server1
        step_name: step1
        

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
step_id:
  description:
    - >-
      The job step's index within the job. If not specified when creating the
      job step, it will be created as the last step. If not specified when
      updating the job step, the step id is not modified.
  returned: always
  type: integer
  sample: null
target_group:
  description:
    - The resource ID of the target group that the job step will be executed on.
  returned: always
  type: str
  sample: null
credential:
  description:
    - >-
      The resource ID of the job credential that will be used to connect to the
      targets.
  returned: always
  type: str
  sample: null
action:
  description:
    - The action payload of the job step.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - Type of action being executed by the job step.
      returned: always
      type: str
      sample: null
    source:
      description:
        - The source of the action to execute.
      returned: always
      type: str
      sample: null
    value:
      description:
        - 'The action value, for example the text of the T-SQL script to execute.'
      returned: always
      type: str
      sample: null
output:
  description:
    - Output destination properties of the job step.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - The output destination type.
      returned: always
      type: str
      sample: null
    subscription_id:
      description:
        - The output destination subscription id.
      returned: always
      type: uuid
      sample: null
    resource_group_name:
      description:
        - The output destination resource group.
      returned: always
      type: str
      sample: null
    server_name:
      description:
        - The output destination server name.
      returned: always
      type: str
      sample: null
    database_name:
      description:
        - The output destination database.
      returned: always
      type: str
      sample: null
    schema_name:
      description:
        - The output destination schema.
      returned: always
      type: str
      sample: null
    table_name:
      description:
        - The output destination table.
      returned: always
      type: str
      sample: null
    credential:
      description:
        - >-
          The resource ID of the credential to use to connect to the output
          destination.
      returned: always
      type: str
      sample: null
execution_options:
  description:
    - Execution options for the job step.
  returned: always
  type: dict
  sample: null
  contains:
    timeout_seconds:
      description:
        - Execution timeout for the job step.
      returned: always
      type: integer
      sample: null
    retry_attempts:
      description:
        - >-
          Maximum number of times the job step will be reattempted if the first
          attempt fails.
      returned: always
      type: integer
      sample: null
    initial_retry_interval_seconds:
      description:
        - Initial delay between retries for job step execution.
      returned: always
      type: integer
      sample: null
    maximum_retry_interval_seconds:
      description:
        - >-
          The maximum amount of time to wait between retries for job step
          execution.
      returned: always
      type: integer
      sample: null
    retry_interval_backoff_multiplier:
      description:
        - The backoff multiplier for the time between retries.
      returned: always
      type: number
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


class AzureRMJobStep(AzureRMModuleBaseExt):
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
            job_name=dict(
                type='str',
                required=True
            ),
            step_name=dict(
                type='str',
                required=True
            ),
            step_id=dict(
                type='integer',
                disposition='/step_id'
            ),
            target_group=dict(
                type='str',
                disposition='/target_group'
            ),
            credential=dict(
                type='str',
                disposition='/credential'
            ),
            action=dict(
                type='dict',
                disposition='/action',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['TSql']
                    ),
                    source=dict(
                        type='str',
                        disposition='source',
                        choices=['Inline']
                    ),
                    value=dict(
                        type='str',
                        disposition='value',
                        required=True
                    )
                )
            ),
            output=dict(
                type='dict',
                disposition='/output',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['SqlDatabase']
                    ),
                    subscription_id=dict(
                        type='uuid',
                        disposition='subscription_id'
                    ),
                    resource_group_name=dict(
                        type='str',
                        disposition='resource_group_name'
                    ),
                    server_name=dict(
                        type='str',
                        disposition='server_name',
                        required=True
                    ),
                    database_name=dict(
                        type='str',
                        disposition='database_name',
                        required=True
                    ),
                    schema_name=dict(
                        type='str',
                        disposition='schema_name'
                    ),
                    table_name=dict(
                        type='str',
                        disposition='table_name',
                        required=True
                    ),
                    credential=dict(
                        type='str',
                        disposition='credential',
                        required=True
                    )
                )
            ),
            execution_options=dict(
                type='dict',
                disposition='/execution_options',
                options=dict(
                    timeout_seconds=dict(
                        type='integer',
                        disposition='timeout_seconds'
                    ),
                    retry_attempts=dict(
                        type='integer',
                        disposition='retry_attempts'
                    ),
                    initial_retry_interval_seconds=dict(
                        type='integer',
                        disposition='initial_retry_interval_seconds'
                    ),
                    maximum_retry_interval_seconds=dict(
                        type='integer',
                        disposition='maximum_retry_interval_seconds'
                    ),
                    retry_interval_backoff_multiplier=dict(
                        type='number',
                        disposition='retry_interval_backoff_multiplier'
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
        self.job_name = None
        self.step_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobStep, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.job_steps.create_or_update(resource_group_name=self.resource_group_name,
                                                                   server_name=self.server_name,
                                                                   job_agent_name=self.job_agent_name,
                                                                   job_name=self.job_name,
                                                                   step_name=self.step_name,
                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobStep instance.')
            self.fail('Error creating the JobStep instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.job_steps.delete(resource_group_name=self.resource_group_name,
                                                         server_name=self.server_name,
                                                         job_agent_name=self.job_agent_name,
                                                         job_name=self.job_name,
                                                         step_name=self.step_name)
        except CloudError as e:
            self.log('Error attempting to delete the JobStep instance.')
            self.fail('Error deleting the JobStep instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.job_steps.get(resource_group_name=self.resource_group_name,
                                                      server_name=self.server_name,
                                                      job_agent_name=self.job_agent_name,
                                                      job_name=self.job_name,
                                                      step_name=self.step_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobStep()


if __name__ == '__main__':
    main()
