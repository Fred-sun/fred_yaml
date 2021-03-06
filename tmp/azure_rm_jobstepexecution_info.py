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
module: azure_rm_jobstepexecution_info
version_added: '2.9'
short_description: Get JobStepExecution info.
description:
  - Get info of JobStepExecution.
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
      - The name of the job to get.
    required: true
    type: str
  job_execution_id:
    description:
      - The id of the job execution
      - The unique id of the job execution
    required: true
    type: uuid
  create_time_min:
    description:
      - >-
        If specified, only job executions created at or after the specified time
        are included.
    type: str
  create_time_max:
    description:
      - >-
        If specified, only job executions created before the specified time are
        included.
    type: str
  end_time_min:
    description:
      - >-
        If specified, only job executions completed at or after the specified
        time are included.
    type: str
  end_time_max:
    description:
      - >-
        If specified, only job executions completed before the specified time
        are included.
    type: str
  is_active:
    description:
      - 'If specified, only active or only completed job executions are included.'
    type: bool
  skip:
    description:
      - The number of elements in the collection to skip.
    type: integer
  top:
    description:
      - The number of elements to return from the collection.
    type: integer
  step_name:
    description:
      - The name of the step.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List job step executions
      azure_rm_jobstepexecution_info: 
        job_agent_name: agent1
        job_execution_id: 5555-6666-7777-8888-999999999999
        job_name: job1
        resource_group_name: group1
        server_name: server1
        

    - name: Get a job step execution
      azure_rm_jobstepexecution_info: 
        job_agent_name: agent1
        job_execution_id: 5555-6666-7777-8888-999999999999
        job_name: job1
        resource_group_name: group1
        server_name: server1
        step_name: step1
        

'''

RETURN = '''
job_step_executions:
  description: >-
    A list of dict results where the key is the name of the JobStepExecution and
    the values are the facts for that JobStepExecution.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        job_version:
          description:
            - The job version number.
          returned: always
          type: integer
          sample: null
        step_name:
          description:
            - The job step name.
          returned: always
          type: str
          sample: null
        step_id:
          description:
            - The job step id.
          returned: always
          type: integer
          sample: null
        job_execution_id:
          description:
            - The unique identifier of the job execution.
          returned: always
          type: uuid
          sample: null
        lifecycle:
          description:
            - The detailed state of the job execution.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The ARM provisioning state of the job execution.
          returned: always
          type: str
          sample: null
        create_time:
          description:
            - The time that the job execution was created.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - The time that the job execution started.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The time that the job execution completed.
          returned: always
          type: str
          sample: null
        current_attempts:
          description:
            - Number of times the job execution has been attempted.
          returned: always
          type: integer
          sample: null
        current_attempt_start_time:
          description:
            - Start time of the current attempt.
          returned: always
          type: str
          sample: null
        last_message:
          description:
            - The last status or error message.
          returned: always
          type: str
          sample: null
        target:
          description:
            - The target that this execution is executed on.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of the target.
              returned: always
              type: str
              sample: null
            server_name:
              description:
                - The server name.
              returned: always
              type: str
              sample: null
            database_name:
              description:
                - The database name.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
    job_version:
      description:
        - The job version number.
      returned: always
      type: integer
      sample: null
    step_name:
      description:
        - The job step name.
      returned: always
      type: str
      sample: null
    step_id:
      description:
        - The job step id.
      returned: always
      type: integer
      sample: null
    job_execution_id:
      description:
        - The unique identifier of the job execution.
      returned: always
      type: uuid
      sample: null
    lifecycle:
      description:
        - The detailed state of the job execution.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The ARM provisioning state of the job execution.
      returned: always
      type: str
      sample: null
    create_time:
      description:
        - The time that the job execution was created.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - The time that the job execution started.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - The time that the job execution completed.
      returned: always
      type: str
      sample: null
    current_attempts:
      description:
        - Number of times the job execution has been attempted.
      returned: always
      type: integer
      sample: null
    current_attempt_start_time:
      description:
        - Start time of the current attempt.
      returned: always
      type: str
      sample: null
    last_message:
      description:
        - The last status or error message.
      returned: always
      type: str
      sample: null
    target:
      description:
        - The target that this execution is executed on.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - The type of the target.
          returned: always
          type: str
          sample: null
        server_name:
          description:
            - The server name.
          returned: always
          type: str
          sample: null
        database_name:
          description:
            - The database name.
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


class AzureRMJobStepExecutionInfo(AzureRMModuleBase):
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
            job_execution_id=dict(
                type='uuid',
                required=True
            ),
            create_time_min=dict(
                type='str'
            ),
            create_time_max=dict(
                type='str'
            ),
            end_time_min=dict(
                type='str'
            ),
            end_time_max=dict(
                type='str'
            ),
            is_active=dict(
                type='bool'
            ),
            skip=dict(
                type='integer'
            ),
            top=dict(
                type='integer'
            ),
            step_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.job_agent_name = None
        self.job_name = None
        self.job_execution_id = None
        self.create_time_min = None
        self.create_time_max = None
        self.end_time_min = None
        self.end_time_max = None
        self.is_active = None
        self.skip = None
        self.top = None
        self.step_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMJobStepExecutionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.job_agent_name is not None and
            self.job_name is not None and
            self.job_execution_id is not None and
            self.step_name is not None):
            self.results['job_step_executions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.job_agent_name is not None and
              self.job_name is not None and
              self.job_execution_id is not None):
            self.results['job_step_executions'] = self.format_item(self.listbyjobexecution())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_step_executions.get(resource_group_name=self.resource_group_name,
                                                                server_name=self.server_name,
                                                                job_agent_name=self.job_agent_name,
                                                                job_name=self.job_name,
                                                                job_execution_id=self.job_execution_id,
                                                                step_name=self.step_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyjobexecution(self):
        response = None

        try:
            response = self.mgmt_client.job_step_executions.list_by_job_execution(resource_group_name=self.resource_group_name,
                                                                                  server_name=self.server_name,
                                                                                  job_agent_name=self.job_agent_name,
                                                                                  job_name=self.job_name,
                                                                                  job_execution_id=self.job_execution_id,
                                                                                  create_time_min=self.create_time_min,
                                                                                  create_time_max=self.create_time_max,
                                                                                  end_time_min=self.end_time_min,
                                                                                  end_time_max=self.end_time_max,
                                                                                  is_active=self.is_active,
                                                                                  skip=self.skip,
                                                                                  top=self.top)
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
    AzureRMJobStepExecutionInfo()


if __name__ == '__main__':
    main()
