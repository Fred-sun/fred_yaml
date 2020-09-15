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
module: azure_rm_pipelinerun_info
version_added: '2.9'
short_description: Get PipelineRun info.
description:
  - Get info of PipelineRun.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: PipelineRunGet
      azure_rm_pipelinerun_info: 
        pipeline_run_name: myPipelineRun
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: PipelineRunList
      azure_rm_pipelinerun_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
pipeline_runs:
  description: >-
    A list of dict results where the key is the name of the PipelineRun and the
    values are the facts for that PipelineRun.
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
                - >-
                  They key vault secret uri to obtain the source storage SAS
                  token.
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
                - >-
                  They key vault secret uri to obtain the target storage SAS
                  token.
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
          How the pipeline run should be forced to recreate even if the pipeline
          run configuration has not changed.
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
    value:
      description:
        - >-
          The list of pipeline runs. Since this list may be incomplete, the
          nextLink field should be used to request the next list of pipeline
          runs.
      returned: always
      type: list
      sample: null
      contains:
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
                    - >-
                      They key vault secret uri to obtain the source storage SAS
                      token.
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
                    - >-
                      They key vault secret uri to obtain the target storage SAS
                      token.
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
              How the pipeline run should be forced to recreate even if the
              pipeline run configuration has not changed.
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
    next_link:
      description:
        - The URI that can be used to request the next list of pipeline runs.
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


class AzureRMPipelineRunInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.pipeline_run_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPipelineRunInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.pipeline_run_name is not None):
            self.results['pipeline_runs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['pipeline_runs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.pipeline_runs.get(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name,
                                                          pipeline_run_name=self.pipeline_run_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.pipeline_runs.list(resource_group_name=self.resource_group_name,
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
    AzureRMPipelineRunInfo()


if __name__ == '__main__':
    main()
