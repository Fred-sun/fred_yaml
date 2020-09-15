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
module: azure_rm_taskrun_info
version_added: '2.9'
short_description: Get TaskRun info.
description:
  - Get info of TaskRun.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: TaskRuns_Get
      azure_rm_taskrun_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_run_name: myRun
        

    - name: TaskRuns_List
      azure_rm_taskrun_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
task_runs:
  description: >-
    A list of dict results where the key is the name of the TaskRun and the
    values are the facts for that TaskRun.
  returned: always
  type: complex
  contains:
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
              The value that indicates whether archiving is enabled for the run
              or not.
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
              The template that describes the repository and tag information for
              run log artifact.
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
              The image update trigger that caused the run. This is applicable
              if the task has base image trigger configured.
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
                  The CPU configuration in terms of number of cores required for
                  the run.
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
    value:
      description:
        - The collection value.
      returned: always
      type: list
      sample: null
      contains:
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
                  The value that indicates whether archiving is enabled for the
                  run or not.
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
                  The template that describes the repository and tag information
                  for run log artifact.
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
                  The list of all images that were generated from the run. This
                  is applicable if the run generates base image dependencies.
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
                  The image update trigger that caused the run. This is
                  applicable if the task has base image trigger configured.
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
                      The CPU configuration in terms of number of cores required
                      for the run.
                  returned: always
                  type: integer
                  sample: null
            source_registry_auth:
              description:
                - >-
                  The scope of the credentials that were used to login to the
                  source registry during this run.
              returned: always
              type: str
              sample: null
            custom_registries:
              description:
                - >-
                  The list of custom registries that were logged in during this
                  run.
              returned: always
              type: list
              sample: null
            run_error_message:
              description:
                - >-
                  The error message received from backend systems after the run
                  is scheduled.
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
    next_link:
      description:
        - The URI that can be used to request the next set of paged results.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTaskRunInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.task_run_name = None

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
        super(AzureRMTaskRunInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.task_run_name is not None):
            self.results['task_runs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['task_runs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.task_runs.get(resource_group_name=self.resource_group_name,
                                                      registry_name=self.registry_name,
                                                      task_run_name=self.task_run_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.task_runs.list(resource_group_name=self.resource_group_name,
                                                       registry_name=self.registry_name)
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
    AzureRMTaskRunInfo()


if __name__ == '__main__':
    main()
