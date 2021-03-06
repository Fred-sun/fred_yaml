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
module: azure_rm_taskrun
version_added: '2.9'
short_description: Manage Azure TaskRun instance.
description:
  - 'Create, update and delete instance of Azure TaskRun.'
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  registry_name:
    description:
      - The name of the container registry.
    required: true
    type: str
  task_run_name:
    description:
      - The name of the task run.
    required: true
    type: str
  location:
    description:
      - The location of the resource
    type: str
  run_request:
    description:
      - The request (parameters) for the run
      - The request (parameters) for the new run
    type: dict
    suboptions:
      type:
        description:
          - The type of the run request.
        required: true
        type: str
      is_archive_enabled:
        description:
          - >-
            The value that indicates whether archiving is enabled for the run or
            not.
        type: bool
      agent_pool_name:
        description:
          - The dedicated agent pool for the run.
        type: str
      log_template:
        description:
          - >-
            The template that describes the repository and tag information for
            run log artifact.
        type: str
  force_update_tag:
    description:
      - >-
        How the run should be forced to rerun even if the run request
        configuration has not changed
    type: str
  principal_id:
    description:
      - The principal ID of resource identity.
    type: str
  tenant_id:
    description:
      - The tenant ID of resource.
    type: str
  type:
    description:
      - The identity type.
    type: sealed-choice
  user_assigned_identities:
    description:
      - "The list of user identities associated with the resource. The user identity \r"
      - "dictionary key references will be ARM resource ids in the form: \r"
      - "'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/\r"
      - '    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}''.'
    type: dictionary
  state:
    description:
      - Assert the state of the TaskRun.
      - >-
        Use C(present) to create or update an TaskRun and C(absent) to delete
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
    - name: TaskRuns_Create
      azure_rm_taskrun: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_run_name: myRun
        

    - name: TaskRuns_Delete
      azure_rm_taskrun: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_run_name: myRun
        

    - name: TaskRuns_Update
      azure_rm_taskrun: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_run_name: myRun
        

'''

RETURN = '''
id:
  description:
    - The resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of this task run
  returned: always
  type: str
  sample: null
run_request:
  description:
    - The request (parameters) for the run
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - The type of the run request.
      returned: always
      type: str
      sample: null
    is_archive_enabled:
      description:
        - >-
          The value that indicates whether archiving is enabled for the run or
          not.
      returned: always
      type: bool
      sample: null
    agent_pool_name:
      description:
        - The dedicated agent pool for the run.
      returned: always
      type: str
      sample: null
    log_template:
      description:
        - >-
          The template that describes the repository and tag information for run
          log artifact.
      returned: always
      type: str
      sample: null
run_result:
  description:
    - The result of this task run
  returned: always
  type: dict
  sample: null
  contains:
    run_id:
      description:
        - The unique identifier for the run.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The current status of the run.
      returned: always
      type: str
      sample: null
    last_updated_time:
      description:
        - The last updated time for the run.
      returned: always
      type: str
      sample: null
    run_type:
      description:
        - The type of run.
      returned: always
      type: str
      sample: null
    agent_pool_name:
      description:
        - The dedicated agent pool for the run.
      returned: always
      type: str
      sample: null
    create_time:
      description:
        - The time the run was scheduled.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - The time the run started.
      returned: always
      type: str
      sample: null
    finish_time:
      description:
        - The time the run finished.
      returned: always
      type: str
      sample: null
    output_images:
      description:
        - >-
          The list of all images that were generated from the run. This is
          applicable if the run generates base image dependencies.
      returned: always
      type: list
      sample: null
      contains:
        registry:
          description:
            - The registry login server.
          returned: always
          type: str
          sample: null
        repository:
          description:
            - The repository name.
          returned: always
          type: str
          sample: null
        tag:
          description:
            - The tag name.
          returned: always
          type: str
          sample: null
        digest:
          description:
            - The sha256-based digest of the image manifest.
          returned: always
          type: str
          sample: null
    task:
      description:
        - The task against which run was scheduled.
      returned: always
      type: str
      sample: null
    image_update_trigger:
      description:
        - >-
          The image update trigger that caused the run. This is applicable if
          the task has base image trigger configured.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The unique ID of the trigger.
          returned: always
          type: str
          sample: null
        timestamp:
          description:
            - The timestamp when the image update happened.
          returned: always
          type: str
          sample: null
        images:
          description:
            - The list of image updates that caused the build.
          returned: always
          type: list
          sample: null
          contains:
            registry:
              description:
                - The registry login server.
              returned: always
              type: str
              sample: null
            repository:
              description:
                - The repository name.
              returned: always
              type: str
              sample: null
            tag:
              description:
                - The tag name.
              returned: always
              type: str
              sample: null
            digest:
              description:
                - The sha256-based digest of the image manifest.
              returned: always
              type: str
              sample: null
    source_trigger:
      description:
        - The source trigger that caused the run.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The unique ID of the trigger.
          returned: always
          type: str
          sample: null
        event_type:
          description:
            - The event type of the trigger.
          returned: always
          type: str
          sample: null
        commit_id:
          description:
            - The unique ID that identifies a commit.
          returned: always
          type: str
          sample: null
        pull_request_id:
          description:
            - The unique ID that identifies pull request.
          returned: always
          type: str
          sample: null
        repository_url:
          description:
            - The repository URL.
          returned: always
          type: str
          sample: null
        branch_name:
          description:
            - The branch name in the repository.
          returned: always
          type: str
          sample: null
        provider_type:
          description:
            - The source control provider type.
          returned: always
          type: str
          sample: null
    timer_trigger:
      description:
        - The timer trigger that caused the run.
      returned: always
      type: dict
      sample: null
      contains:
        timer_trigger_name:
          description:
            - The timer trigger name that caused the run.
          returned: always
          type: str
          sample: null
        schedule_occurrence:
          description:
            - The occurrence that triggered the run.
          returned: always
          type: str
          sample: null
    platform:
      description:
        - The platform properties against which the run will happen.
      returned: always
      type: dict
      sample: null
      contains:
        os:
          description:
            - The operating system type required for the run.
          returned: always
          type: str
          sample: null
        architecture:
          description:
            - The OS architecture.
          returned: always
          type: str
          sample: null
        variant:
          description:
            - Variant of the CPU.
          returned: always
          type: str
          sample: null
    agent_configuration:
      description:
        - The machine configuration of the run agent.
      returned: always
      type: dict
      sample: null
      contains:
        cpu:
          description:
            - >-
              The CPU configuration in terms of number of cores required for the
              run.
          returned: always
          type: integer
          sample: null
    source_registry_auth:
      description:
        - >-
          The scope of the credentials that were used to login to the source
          registry during this run.
      returned: always
      type: str
      sample: null
    custom_registries:
      description:
        - The list of custom registries that were logged in during this run.
      returned: always
      type: list
      sample: null
    run_error_message:
      description:
        - >-
          The error message received from backend systems after the run is
          scheduled.
      returned: always
      type: str
      sample: null
    update_trigger_token:
      description:
        - The update trigger token passed for the Run.
      returned: always
      type: str
      sample: null
    log_artifact:
      description:
        - The image description for the log artifact.
      returned: always
      type: dict
      sample: null
      contains:
        registry:
          description:
            - The registry login server.
          returned: always
          type: str
          sample: null
        repository:
          description:
            - The repository name.
          returned: always
          type: str
          sample: null
        tag:
          description:
            - The tag name.
          returned: always
          type: str
          sample: null
        digest:
          description:
            - The sha256-based digest of the image manifest.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of a run.
      returned: always
      type: str
      sample: null
    is_archive_enabled:
      description:
        - The value that indicates whether archiving is enabled or not.
      returned: always
      type: bool
      sample: null
force_update_tag:
  description:
    - >-
      How the run should be forced to rerun even if the run request
      configuration has not changed
  returned: always
  type: str
  sample: null
principal_id:
  description:
    - The principal ID of resource identity.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The tenant ID of resource.
  returned: always
  type: str
  sample: null
type_identity_type:
  description:
    - The identity type.
  returned: always
  type: sealed-choice
  sample: null
user_assigned_identities:
  description:
    - "The list of user identities associated with the resource. The user identity \r\ndictionary key references will be ARM resource ids in the form: \r\n'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/\r\n    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'."
  returned: always
  type: dictionary
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTaskRun(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            task_run_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            run_request=dict(
                type='dict',
                disposition='/run_request',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        required=True
                    ),
                    is_archive_enabled=dict(
                        type='bool',
                        disposition='is_archive_enabled'
                    ),
                    agent_pool_name=dict(
                        type='str',
                        disposition='agent_pool_name'
                    ),
                    log_template=dict(
                        type='str',
                        disposition='log_template'
                    )
                )
            ),
            force_update_tag=dict(
                type='str',
                disposition='/force_update_tag'
            ),
            principal_id=dict(
                type='str',
                disposition='/principal_id'
            ),
            tenant_id=dict(
                type='str',
                disposition='/tenant_id'
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.task_run_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTaskRun, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.task_runs.create(resource_group_name=self.resource_group_name,
                                                             registry_name=self.registry_name,
                                                             task_run_name=self.task_run_name,
                                                             task_run=self.body)
            else:
                response = self.mgmt_client.task_runs.update(resource_group_name=self.resource_group_name,
                                                             registry_name=self.registry_name,
                                                             task_run_name=self.task_run_name,
                                                             update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the TaskRun instance.')
            self.fail('Error creating the TaskRun instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.task_runs.delete(resource_group_name=self.resource_group_name,
                                                         registry_name=self.registry_name,
                                                         task_run_name=self.task_run_name)
        except CloudError as e:
            self.log('Error attempting to delete the TaskRun instance.')
            self.fail('Error deleting the TaskRun instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.task_runs.get(resource_group_name=self.resource_group_name,
                                                      registry_name=self.registry_name,
                                                      task_run_name=self.task_run_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTaskRun()


if __name__ == '__main__':
    main()
