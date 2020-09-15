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
module: azure_rm_exportpipeline
version_added: '2.9'
short_description: Manage Azure ExportPipeline instance.
description:
  - 'Create, update and delete instance of Azure ExportPipeline.'
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
  export_pipeline_name:
    description:
      - The name of the export pipeline.
    required: true
    type: str
  location:
    description:
      - The location of the export pipeline.
    type: str
  target:
    description:
      - The target properties of the export pipeline.
    type: dict
    suboptions:
      type:
        description:
          - The type of target for the export pipeline.
        type: str
      uri:
        description:
          - "The target uri of the export pipeline.\r"
          - "When 'AzureStorageBlob': \"https://accountName.blob.core.windows.net/containerName/blobName\"\r"
          - >-
            When 'AzureStorageBlobContainer': 
            "https://accountName.blob.core.windows.net/containerName"
        type: str
      key_vault_uri:
        description:
          - They key vault secret uri to obtain the target storage SAS token.
        required: true
        type: str
  options:
    description:
      - The list of all options configured for the pipeline.
    type: list
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
      - Assert the state of the ExportPipeline.
      - >-
        Use C(present) to create or update an ExportPipeline and C(absent) to
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
    - name: ExportPipelineCreate
      azure_rm_exportpipeline: 
        export_pipeline_name: myExportPipeline
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: ExportPipelineDelete
      azure_rm_exportpipeline: 
        export_pipeline_name: myExportPipeline
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
location:
  description:
    - The location of the export pipeline.
  returned: always
  type: str
  sample: null
target:
  description:
    - The target properties of the export pipeline.
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


class AzureRMExportPipeline(AzureRMModuleBaseExt):
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
            export_pipeline_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            target=dict(
                type='dict',
                disposition='/target',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type'
                    ),
                    uri=dict(
                        type='str',
                        disposition='uri'
                    ),
                    key_vault_uri=dict(
                        type='str',
                        disposition='key_vault_uri',
                        required=True
                    )
                )
            ),
            options=dict(
                type='list',
                disposition='/options',
                elements='str'
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
        self.export_pipeline_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExportPipeline, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.export_pipelines.create(resource_group_name=self.resource_group_name,
                                                                    registry_name=self.registry_name,
                                                                    export_pipeline_name=self.export_pipeline_name,
                                                                    export_pipeline_create_parameters=self.body)
            else:
                response = self.mgmt_client.export_pipelines.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ExportPipeline instance.')
            self.fail('Error creating the ExportPipeline instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.export_pipelines.delete(resource_group_name=self.resource_group_name,
                                                                registry_name=self.registry_name,
                                                                export_pipeline_name=self.export_pipeline_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExportPipeline instance.')
            self.fail('Error deleting the ExportPipeline instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.export_pipelines.get(resource_group_name=self.resource_group_name,
                                                             registry_name=self.registry_name,
                                                             export_pipeline_name=self.export_pipeline_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMExportPipeline()


if __name__ == '__main__':
    main()
