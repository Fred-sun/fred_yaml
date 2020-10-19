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
module: azure_rm_jobstepexecution
version_added: '2.9'
short_description: Manage Azure JobStepExecution instance.
description:
  - 'Create, update and delete instance of Azure JobStepExecution.'
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
      - The unique id of the job execution
    required: true
    type: uuid
  step_name:
    description:
      - The name of the step.
    required: true
    type: str
  state:
    description:
      - Assert the state of the JobStepExecution.
      - >-
        Use C(present) to create or update an JobStepExecution and C(absent) to
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


class AzureRMJobStepExecution(AzureRMModuleBaseExt):
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
            step_name=dict(
                type='str',
                required=True
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
        self.job_execution_id = None
        self.step_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobStepExecution, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.job_step_executions.create()
            else:
                response = self.mgmt_client.job_step_executions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobStepExecution instance.')
            self.fail('Error creating the JobStepExecution instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.job_step_executions.delete()
        except CloudError as e:
            self.log('Error attempting to delete the JobStepExecution instance.')
            self.fail('Error deleting the JobStepExecution instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.job_step_executions.get(resource_group_name=self.resource_group_name,
                                                                server_name=self.server_name,
                                                                job_agent_name=self.job_agent_name,
                                                                job_name=self.job_name,
                                                                job_execution_id=self.job_execution_id,
                                                                step_name=self.step_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobStepExecution()


if __name__ == '__main__':
    main()
