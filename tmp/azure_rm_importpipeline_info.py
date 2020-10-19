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
module: azure_rm_importpipeline_info
version_added: '2.9'
short_description: Get ImportPipeline info.
description:
  - Get info of ImportPipeline.
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
  import_pipeline_name:
    description:
      - The name of the import pipeline.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ImportPipelineGet
      azure_rm_importpipeline_info: 
        import_pipeline_name: myImportPipeline
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: ImportPipelineList
      azure_rm_importpipeline_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
import_pipelines:
  description: >-
    A list of dict results where the key is the name of the ImportPipeline and
    the values are the facts for that ImportPipeline.
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
        - The location of the import pipeline.
      returned: always
      type: str
      sample: null
    source:
      description:
        - The source properties of the import pipeline.
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
    options:
      description:
        - The list of all options configured for the pipeline.
      returned: always
      type: list
      sample: null
    provisioning_state:
      description:
        - >-
          The provisioning state of the pipeline at the time the operation was
          called.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The current status of the source trigger.
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
        - >-
          The list of import pipelines. Since this list may be incomplete, the
          nextLink field should be used to request the next list of import
          pipelines.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - The location of the import pipeline.
          returned: always
          type: str
          sample: null
        source:
          description:
            - The source properties of the import pipeline.
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
        options:
          description:
            - The list of all options configured for the pipeline.
          returned: always
          type: list
          sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the pipeline at the time the operation
              was called.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The current status of the source trigger.
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


class AzureRMImportPipelineInfo(AzureRMModuleBase):
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
            import_pipeline_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.import_pipeline_name = None

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
        super(AzureRMImportPipelineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.import_pipeline_name is not None):
            self.results['import_pipelines'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['import_pipelines'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.import_pipelines.get(resource_group_name=self.resource_group_name,
                                                             registry_name=self.registry_name,
                                                             import_pipeline_name=self.import_pipeline_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.import_pipelines.list(resource_group_name=self.resource_group_name,
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
    AzureRMImportPipelineInfo()


if __name__ == '__main__':
    main()
