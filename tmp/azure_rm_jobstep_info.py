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
module: azure_rm_jobstep_info
version_added: '2.9'
short_description: Get JobStep info.
description:
  - Get info of JobStep.
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
      - The name of the job.
    required: true
    type: str
  job_version:
    description:
      - The version of the job to get.
    type: integer
  step_name:
    description:
      - The name of the job step.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List job steps for the specified version of a job.
      azure_rm_jobstep_info: 
        job_agent_name: agent1
        job_name: job1
        job_version: '1'
        resource_group_name: group1
        server_name: server1
        

    - name: Get the specified version of a job step.
      azure_rm_jobstep_info: 
        job_agent_name: agent1
        job_name: job1
        job_version: '1'
        resource_group_name: group1
        server_name: server1
        step_name: step1
        

    - name: List job steps for the latest version of a job.
      azure_rm_jobstep_info: 
        job_agent_name: agent1
        job_name: job1
        resource_group_name: group1
        server_name: server1
        

    - name: Get the latest version of a job step.
      azure_rm_jobstep_info: 
        job_agent_name: agent1
        job_name: job1
        resource_group_name: group1
        server_name: server1
        step_name: step1
        

'''

RETURN = '''
job_steps:
  description: >-
    A list of dict results where the key is the name of the JobStep and the
    values are the facts for that JobStep.
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
        step_id:
          description:
            - >-
              The job step's index within the job. If not specified when
              creating the job step, it will be created as the last step. If not
              specified when updating the job step, the step id is not modified.
          returned: always
          type: integer
          sample: null
        target_group:
          description:
            - >-
              The resource ID of the target group that the job step will be
              executed on.
          returned: always
          type: str
          sample: null
        credential:
          description:
            - >-
              The resource ID of the job credential that will be used to connect
              to the targets.
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
                - >-
                  The action value, for example the text of the T-SQL script to
                  execute.
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
                  The resource ID of the credential to use to connect to the
                  output destination.
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
                  Maximum number of times the job step will be reattempted if
                  the first attempt fails.
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
                  The maximum amount of time to wait between retries for job
                  step execution.
              returned: always
              type: integer
              sample: null
            retry_interval_backoff_multiplier:
              description:
                - The backoff multiplier for the time between retries.
              returned: always
              type: number
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
    step_id:
      description:
        - >-
          The job step's index within the job. If not specified when creating
          the job step, it will be created as the last step. If not specified
          when updating the job step, the step id is not modified.
      returned: always
      type: integer
      sample: null
    target_group:
      description:
        - >-
          The resource ID of the target group that the job step will be executed
          on.
      returned: always
      type: str
      sample: null
    credential:
      description:
        - >-
          The resource ID of the job credential that will be used to connect to
          the targets.
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
            - >-
              The action value, for example the text of the T-SQL script to
              execute.
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
              Maximum number of times the job step will be reattempted if the
              first attempt fails.
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


class AzureRMJobStepInfo(AzureRMModuleBase):
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
            job_version=dict(
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
        self.job_version = None
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
        super(AzureRMJobStepInfo, self).__init__(self.module_arg_spec, supports_tags=True)

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
            self.job_version is not None and
            self.step_name is not None):
            self.results['job_steps'] = self.format_item(self.getbyversion())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.job_agent_name is not None and
              self.job_name is not None and
              self.job_version is not None):
            self.results['job_steps'] = self.format_item(self.listbyversion())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.job_agent_name is not None and
              self.job_name is not None and
              self.step_name is not None):
            self.results['job_steps'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.job_agent_name is not None and
              self.job_name is not None):
            self.results['job_steps'] = self.format_item(self.listbyjob())
        return self.results

    def getbyversion(self):
        response = None

        try:
            response = self.mgmt_client.job_steps.get_by_version(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 job_agent_name=self.job_agent_name,
                                                                 job_name=self.job_name,
                                                                 job_version=self.job_version,
                                                                 step_name=self.step_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyversion(self):
        response = None

        try:
            response = self.mgmt_client.job_steps.list_by_version(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  job_agent_name=self.job_agent_name,
                                                                  job_name=self.job_name,
                                                                  job_version=self.job_version)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_steps.get(resource_group_name=self.resource_group_name,
                                                      server_name=self.server_name,
                                                      job_agent_name=self.job_agent_name,
                                                      job_name=self.job_name,
                                                      step_name=self.step_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyjob(self):
        response = None

        try:
            response = self.mgmt_client.job_steps.list_by_job(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              job_agent_name=self.job_agent_name,
                                                              job_name=self.job_name)
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
    AzureRMJobStepInfo()


if __name__ == '__main__':
    main()
