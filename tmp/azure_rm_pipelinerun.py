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
module: azure_rm_pipelinerun
version_added: '2.9'
short_description: Manage Azure PipelineRun instance.
description:
  - 'Create, update and delete instance of Azure PipelineRun.'
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
  pipeline_run_name:
    description:
      - The name of the pipeline run.
    required: true
    type: str
  force_update_tag:
    description:
      - >-
        How the pipeline run should be forced to recreate even if the pipeline
        run configuration has not changed.
    type: str
  pipeline_resource_id:
    description:
      - The resource ID of the pipeline to run.
    type: str
  artifacts:
    description:
      - "List of source artifacts to be transferred by the pipeline. \r"
      - "Specify an image by repository ('hello-world'). This will use the 'latest' tag.\r"
      - "Specify an image by tag ('hello-world:latest').\r"
      - >-
        Specify an image by sha256-based manifest digest
        ('hello-world@sha256:abc123').
    type: list
  source:
    description:
      - The source properties of the pipeline run.
    type: dict
    suboptions:
      type:
        description:
          - The type of the source.
        type: str
        choices:
          - AzureStorageBlob
      name:
        description:
          - The name of the source.
        type: str
  target:
    description:
      - The target properties of the pipeline run.
    type: dict
    suboptions:
      type:
        description:
          - The type of the target.
        type: str
        choices:
          - AzureStorageBlob
      name:
        description:
          - The name of the target.
        type: str
  catalog_digest:
    description:
      - The digest of the tar used to transfer the artifacts.
    type: str
  state:
    description:
      - Assert the state of the PipelineRun.
      - >-
        Use C(present) to create or update an PipelineRun and C(absent) to
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
    - name: PipelineRunCreate_Export
      azure_rm_pipelinerun: 
        pipeline_run_name: myPipelineRun
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: PipelineRunCreate_Import
      azure_rm_pipelinerun: 
        pipeline_run_name: myPipelineRun
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: PipelineRunDelete
      azure_rm_pipelinerun: 
        pipeline_run_name: myPipelineRun
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

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
provisioning_state:
  description:
    - The provisioning state of a pipeline run.
  returned: always
  type: str
  sample: null
response:
  description:
    - The response of a pipeline run.
  returned: always
  type: dict
  sample: null
  contains:
    status:
      description:
        - The current status of the pipeline run.
      returned: always
      type: str
      sample: null
    imported_artifacts:
      description:
        - The artifacts imported in the pipeline run.
      returned: always
      type: list
      sample: null
    progress:
      description:
        - The current progress of the copy operation.
      returned: always
      type: dict
      sample: null
      contains:
        percentage:
          description:
            - The percentage complete of the copy operation.
          returned: always
          type: str
          sample: null
    start_time:
      description:
        - The time the pipeline run started.
      returned: always
      type: str
      sample: null
    finish_time:
      description:
        - The time the pipeline run finished.
      returned: always
      type: str
      sample: null
    source:
      description:
        - The source of the pipeline run.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - The type of source for the import pipeline.
          returned: always
          type: str
          sample: null
        uri:
          description:
            - "The source uri of the import pipeline.\r\nWhen 'AzureStorageBlob': \"https://accountName.blob.core.windows.net/containerName/blobName\"\r\nWhen 'AzureStorageBlobContainer': \"https://accountName.blob.core.windows.net/containerName\""
          returned: always
          type: str
          sample: null
        key_vault_uri:
          description:
            - They key vault secret uri to obtain the source storage SAS token.
          returned: always
          type: str
          sample: null
    target:
      description:
        - The target of the pipeline run.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - The type of target for the export pipeline.
          returned: always
          type: str
          sample: null
        uri:
          description:
            - "The target uri of the export pipeline.\r\nWhen 'AzureStorageBlob': \"https://accountName.blob.core.windows.net/containerName/blobName\"\r\nWhen 'AzureStorageBlobContainer':  \"https://accountName.blob.core.windows.net/containerName\""
          returned: always
          type: str
          sample: null
        key_vault_uri:
          description:
            - They key vault secret uri to obtain the target storage SAS token.
          returned: always
          type: str
          sample: null
    catalog_digest:
      description:
        - The digest of the tar used to transfer the artifacts.
      returned: always
      type: str
      sample: null
    trigger:
      description:
        - The trigger that caused the pipeline run.
      returned: always
      type: dict
      sample: null
      contains:
        source_trigger:
          description:
            - The source trigger that caused the pipeline run.
          returned: always
          type: dict
          sample: null
          contains:
            timestamp:
              description:
                - The timestamp when the source update happened.
              returned: always
              type: str
              sample: null
    pipeline_run_error_message:
      description:
        - >-
          The detailed error message for the pipeline run in the case of
          failure.
      returned: always
      type: str
      sample: null
force_update_tag:
  description:
    - >-
      How the pipeline run should be forced to recreate even if the pipeline run
      configuration has not changed.
  returned: always
  type: str
  sample: null
pipeline_resource_id:
  description:
    - The resource ID of the pipeline to run.
  returned: always
  type: str
  sample: null
artifacts:
  description:
    - "List of source artifacts to be transferred by the pipeline. \r\nSpecify an image by repository ('hello-world'). This will use the 'latest' tag.\r\nSpecify an image by tag ('hello-world:latest').\r\nSpecify an image by sha256-based manifest digest ('hello-world@sha256:abc123')."
  returned: always
  type: list
  sample: null
source:
  description:
    - The source properties of the pipeline run.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - The type of the source.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the source.
      returned: always
      type: str
      sample: null
target:
  description:
    - The target properties of the pipeline run.
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
    name:
      description:
        - The name of the target.
      returned: always
      type: str
      sample: null
catalog_digest:
  description:
    - The digest of the tar used to transfer the artifacts.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPipelineRun(AzureRMModuleBaseExt):
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
            pipeline_run_name=dict(
                type='str',
                required=True
            ),
            force_update_tag=dict(
                type='str',
                disposition='/force_update_tag'
            ),
            pipeline_resource_id=dict(
                type='str',
                disposition='/pipeline_resource_id'
            ),
            artifacts=dict(
                type='list',
                disposition='/artifacts',
                elements='str'
            ),
            source=dict(
                type='dict',
                disposition='/source',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['AzureStorageBlob']
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    )
                )
            ),
            target=dict(
                type='dict',
                disposition='/target',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['AzureStorageBlob']
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    )
                )
            ),
            catalog_digest=dict(
                type='str',
                disposition='/catalog_digest'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.pipeline_run_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPipelineRun, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-12-01-preview')

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
                response = self.mgmt_client.pipeline_runs.create(resource_group_name=self.resource_group_name,
                                                                 registry_name=self.registry_name,
                                                                 pipeline_run_name=self.pipeline_run_name,
                                                                 pipeline_run_create_parameters=self.body)
            else:
                response = self.mgmt_client.pipeline_runs.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PipelineRun instance.')
            self.fail('Error creating the PipelineRun instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.pipeline_runs.delete(resource_group_name=self.resource_group_name,
                                                             registry_name=self.registry_name,
                                                             pipeline_run_name=self.pipeline_run_name)
        except CloudError as e:
            self.log('Error attempting to delete the PipelineRun instance.')
            self.fail('Error deleting the PipelineRun instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.pipeline_runs.get(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name,
                                                          pipeline_run_name=self.pipeline_run_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPipelineRun()


if __name__ == '__main__':
    main()
