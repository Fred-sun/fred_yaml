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
module: azure_rm_run_info
version_added: '2.9'
short_description: Get Run info.
description:
  - Get info of Run.
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
  filter:
    description:
      - >-
        The runs filter to apply on the operation. Arithmetic operators are not
        supported. The allowed string function is 'contains'. All logical
        operators except 'Not', 'Has', 'All' are allowed.
    type: str
  top:
    description:
      - >-
        $top is supported for get list of runs, which limits the maximum number
        of runs to return.
    type: integer
  run_id:
    description:
      - The run ID.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Runs_List
      azure_rm_run_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: Runs_Get
      azure_rm_run_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        run_id: 0accec26-d6de-4757-8e74-d080f38eaaab
        

'''

RETURN = '''
runs:
  description: >-
    A list of dict results where the key is the name of the Run and the values
    are the facts for that Run.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The collection value.
      returned: always
      type: list
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
    next_link:
      description:
        - The URI that can be used to request the next set of paged results.
      returned: always
      type: str
      sample: null
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


class AzureRMRunInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            run_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.filter = None
        self.top = None
        self.run_id = None

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
        super(AzureRMRunInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.run_id is not None):
            self.results['runs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['runs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.runs.get(resource_group_name=self.resource_group_name,
                                                 registry_name=self.registry_name,
                                                 run_id=self.run_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.runs.list(resource_group_name=self.resource_group_name,
                                                  registry_name=self.registry_name,
                                                  filter=self.filter,
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
    AzureRMRunInfo()


if __name__ == '__main__':
    main()
