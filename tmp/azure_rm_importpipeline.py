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
module: azure_rm_importpipeline
version_added: '2.9'
short_description: Manage Azure ImportPipeline instance.
description:
  - 'Create, update and delete instance of Azure ImportPipeline.'
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
    required: true
    type: str
  location:
    description:
      - The location of the import pipeline.
    type: str
  source:
    description:
      - The source properties of the import pipeline.
    type: dict
    suboptions:
      type:
        description:
          - The type of source for the import pipeline.
        type: str
        choices:
          - AzureStorageBlobContainer
      uri:
        description:
          - "The source uri of the import pipeline.\r"
          - "When 'AzureStorageBlob': \"https://accountName.blob.core.windows.net/containerName/blobName\"\r"
          - >-
            When 'AzureStorageBlobContainer':
            "https://accountName.blob.core.windows.net/containerName"
        type: str
      key_vault_uri:
        description:
          - They key vault secret uri to obtain the source storage SAS token.
        required: true
        type: str
  options:
    description:
      - The list of all options configured for the pipeline.
    type: list
  status:
    description:
      - The current status of the source trigger.
    type: str
    choices:
      - Disabled
      - Enabled
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
      - Assert the state of the ImportPipeline.
      - >-
        Use C(present) to create or update an ImportPipeline and C(absent) to
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
    - name: ImportPipelineCreate
      azure_rm_importpipeline: 
        import_pipeline_name: myImportPipeline
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: ImportPipelineDelete
      azure_rm_importpipeline: 
        import_pipeline_name: myImportPipeline
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


class AzureRMImportPipeline(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            source=dict(
                type='dict',
                disposition='/source',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['AzureStorageBlobContainer']
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
            status=dict(
                type='str',
                disposition='/status',
                choices=['Disabled',
                         'Enabled']
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
        self.import_pipeline_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMImportPipeline, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.import_pipelines.create(resource_group_name=self.resource_group_name,
                                                                    registry_name=self.registry_name,
                                                                    import_pipeline_name=self.import_pipeline_name,
                                                                    import_pipeline_create_parameters=self.body)
            else:
                response = self.mgmt_client.import_pipelines.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ImportPipeline instance.')
            self.fail('Error creating the ImportPipeline instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.import_pipelines.delete(resource_group_name=self.resource_group_name,
                                                                registry_name=self.registry_name,
                                                                import_pipeline_name=self.import_pipeline_name)
        except CloudError as e:
            self.log('Error attempting to delete the ImportPipeline instance.')
            self.fail('Error deleting the ImportPipeline instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.import_pipelines.get(resource_group_name=self.resource_group_name,
                                                             registry_name=self.registry_name,
                                                             import_pipeline_name=self.import_pipeline_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMImportPipeline()


if __name__ == '__main__':
    main()
