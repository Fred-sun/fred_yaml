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
module: azure_rm_task_info
version_added: '2.9'
short_description: Get Task info.
description:
  - Get info of Task.
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
  task_name:
    description:
      - The name of the container registry task.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Tasks_List
      azure_rm_task_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: Tasks_Get
      azure_rm_task_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: myTask
        

'''

RETURN = '''
tasks:
  description: >-
    A list of dict results where the key is the name of the Task and the values
    are the facts for that Task.
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
        provisioning_state:
          description:
            - The provisioning state of the task.
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of task.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The current status of task.
          returned: always
          type: str
          sample: null
        platform:
          description:
            - The platform properties against which the run has to happen.
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
        agent_pool_name:
          description:
            - The dedicated agent pool for the task.
          returned: always
          type: str
          sample: null
        timeout:
          description:
            - Run timeout in seconds.
          returned: always
          type: integer
          sample: null
        step:
          description:
            - The properties of a task step.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of the step.
              returned: always
              type: str
              sample: null
            base_image_dependencies:
              description:
                - List of base image dependencies for a step.
              returned: always
              type: list
              sample: null
              contains:
                type:
                  description:
                    - The type of the base image dependency.
                  returned: always
                  type: str
                  sample: null
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
            context_path:
              description:
                - >-
                  The URL(absolute or relative) of the source context for the
                  task step.
              returned: always
              type: str
              sample: null
            context_access_token:
              description:
                - >-
                  The token (git PAT or SAS token of storage account blob)
                  associated with the context for a step.
              returned: always
              type: str
              sample: null
        trigger:
          description:
            - The properties that describe all triggers for the task.
          returned: always
          type: dict
          sample: null
          contains:
            timer_triggers:
              description:
                - The collection of timer triggers.
              returned: always
              type: list
              sample: null
              contains:
                schedule:
                  description:
                    - The CRON expression for the task schedule
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - The current status of trigger.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The name of the trigger.
                  returned: always
                  type: str
                  sample: null
            source_triggers:
              description:
                - The collection of triggers based on source code repository.
              returned: always
              type: list
              sample: null
              contains:
                source_repository:
                  description:
                    - >-
                      The properties that describes the source(code) for the
                      task.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    source_control_type:
                      description:
                        - The type of source control service.
                      returned: always
                      type: str
                      sample: null
                    repository_url:
                      description:
                        - The full URL to the source code repository
                      returned: always
                      type: str
                      sample: null
                    branch:
                      description:
                        - The branch name of the source code.
                      returned: always
                      type: str
                      sample: null
                    source_control_auth_properties:
                      description:
                        - "The authorization properties for accessing the source code repository and to set up\r\nwebhooks for notifications."
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        token_type:
                          description:
                            - The type of Auth token.
                          returned: always
                          type: str
                          sample: null
                        token:
                          description:
                            - >-
                              The access token used to access the source control
                              provider.
                          returned: always
                          type: str
                          sample: null
                        refresh_token:
                          description:
                            - >-
                              The refresh token used to refresh the access
                              token.
                          returned: always
                          type: str
                          sample: null
                        scope:
                          description:
                            - The scope of the access token.
                          returned: always
                          type: str
                          sample: null
                        expires_in:
                          description:
                            - Time in seconds that the token remains valid
                          returned: always
                          type: integer
                          sample: null
                source_trigger_events:
                  description:
                    - The source event corresponding to the trigger.
                  returned: always
                  type: list
                  sample: null
                status:
                  description:
                    - The current status of trigger.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The name of the trigger.
                  returned: always
                  type: str
                  sample: null
            base_image_trigger:
              description:
                - The trigger based on base image dependencies.
              returned: always
              type: dict
              sample: null
              contains:
                base_image_trigger_type:
                  description:
                    - >-
                      The type of the auto trigger for base image dependency
                      updates.
                  returned: always
                  type: str
                  sample: null
                update_trigger_endpoint:
                  description:
                    - The endpoint URL for receiving update triggers.
                  returned: always
                  type: str
                  sample: null
                update_trigger_payload_type:
                  description:
                    - Type of Payload body for Base image update triggers.
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - The current status of trigger.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The name of the trigger.
                  returned: always
                  type: str
                  sample: null
        credentials:
          description:
            - >-
              The properties that describes a set of credentials that will be
              used when this run is invoked.
          returned: always
          type: dict
          sample: null
          contains:
            source_registry:
              description:
                - >-
                  Describes the credential parameters for accessing the source
                  registry.
              returned: always
              type: dict
              sample: null
              contains:
                login_mode:
                  description:
                    - "The authentication mode which determines the source registry login scope. The credentials for the source registry\r\nwill be generated using the given scope. These credentials will be used to login to\r\nthe source registry during the run."
                  returned: always
                  type: str
                  sample: null
            custom_registries:
              description:
                - "Describes the credential parameters for accessing other custom registries. The key\r\nfor the dictionary item will be the registry login server (myregistry.azurecr.io) and\r\nthe value of the item will be the registry credentials for accessing the registry."
              returned: always
              type: dictionary
              sample: null
        log_template:
          description:
            - >-
              The template that describes the repository and tag information for
              run log artifact.
          returned: always
          type: str
          sample: null
        is_system_task:
          description:
            - >-
              The value of this property indicates whether the task resource is
              system task or not.
          returned: always
          type: bool
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
        - >-
          The location of the resource. This cannot be changed after the
          resource is created.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the task.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of task.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The current status of task.
      returned: always
      type: str
      sample: null
    platform:
      description:
        - The platform properties against which the run has to happen.
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
    agent_pool_name:
      description:
        - The dedicated agent pool for the task.
      returned: always
      type: str
      sample: null
    timeout:
      description:
        - Run timeout in seconds.
      returned: always
      type: integer
      sample: null
    step:
      description:
        - The properties of a task step.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - The type of the step.
          returned: always
          type: str
          sample: null
        base_image_dependencies:
          description:
            - List of base image dependencies for a step.
          returned: always
          type: list
          sample: null
          contains:
            type:
              description:
                - The type of the base image dependency.
              returned: always
              type: str
              sample: null
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
        context_path:
          description:
            - >-
              The URL(absolute or relative) of the source context for the task
              step.
          returned: always
          type: str
          sample: null
        context_access_token:
          description:
            - >-
              The token (git PAT or SAS token of storage account blob)
              associated with the context for a step.
          returned: always
          type: str
          sample: null
    trigger:
      description:
        - The properties that describe all triggers for the task.
      returned: always
      type: dict
      sample: null
      contains:
        timer_triggers:
          description:
            - The collection of timer triggers.
          returned: always
          type: list
          sample: null
          contains:
            schedule:
              description:
                - The CRON expression for the task schedule
              returned: always
              type: str
              sample: null
            status:
              description:
                - The current status of trigger.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the trigger.
              returned: always
              type: str
              sample: null
        source_triggers:
          description:
            - The collection of triggers based on source code repository.
          returned: always
          type: list
          sample: null
          contains:
            source_repository:
              description:
                - The properties that describes the source(code) for the task.
              returned: always
              type: dict
              sample: null
              contains:
                source_control_type:
                  description:
                    - The type of source control service.
                  returned: always
                  type: str
                  sample: null
                repository_url:
                  description:
                    - The full URL to the source code repository
                  returned: always
                  type: str
                  sample: null
                branch:
                  description:
                    - The branch name of the source code.
                  returned: always
                  type: str
                  sample: null
                source_control_auth_properties:
                  description:
                    - "The authorization properties for accessing the source code repository and to set up\r\nwebhooks for notifications."
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    token_type:
                      description:
                        - The type of Auth token.
                      returned: always
                      type: str
                      sample: null
                    token:
                      description:
                        - >-
                          The access token used to access the source control
                          provider.
                      returned: always
                      type: str
                      sample: null
                    refresh_token:
                      description:
                        - The refresh token used to refresh the access token.
                      returned: always
                      type: str
                      sample: null
                    scope:
                      description:
                        - The scope of the access token.
                      returned: always
                      type: str
                      sample: null
                    expires_in:
                      description:
                        - Time in seconds that the token remains valid
                      returned: always
                      type: integer
                      sample: null
            source_trigger_events:
              description:
                - The source event corresponding to the trigger.
              returned: always
              type: list
              sample: null
            status:
              description:
                - The current status of trigger.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the trigger.
              returned: always
              type: str
              sample: null
        base_image_trigger:
          description:
            - The trigger based on base image dependencies.
          returned: always
          type: dict
          sample: null
          contains:
            base_image_trigger_type:
              description:
                - >-
                  The type of the auto trigger for base image dependency
                  updates.
              returned: always
              type: str
              sample: null
            update_trigger_endpoint:
              description:
                - The endpoint URL for receiving update triggers.
              returned: always
              type: str
              sample: null
            update_trigger_payload_type:
              description:
                - Type of Payload body for Base image update triggers.
              returned: always
              type: str
              sample: null
            status:
              description:
                - The current status of trigger.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the trigger.
              returned: always
              type: str
              sample: null
    credentials:
      description:
        - >-
          The properties that describes a set of credentials that will be used
          when this run is invoked.
      returned: always
      type: dict
      sample: null
      contains:
        source_registry:
          description:
            - >-
              Describes the credential parameters for accessing the source
              registry.
          returned: always
          type: dict
          sample: null
          contains:
            login_mode:
              description:
                - "The authentication mode which determines the source registry login scope. The credentials for the source registry\r\nwill be generated using the given scope. These credentials will be used to login to\r\nthe source registry during the run."
              returned: always
              type: str
              sample: null
        custom_registries:
          description:
            - "Describes the credential parameters for accessing other custom registries. The key\r\nfor the dictionary item will be the registry login server (myregistry.azurecr.io) and\r\nthe value of the item will be the registry credentials for accessing the registry."
          returned: always
          type: dictionary
          sample: null
    log_template:
      description:
        - >-
          The template that describes the repository and tag information for run
          log artifact.
      returned: always
      type: str
      sample: null
    is_system_task:
      description:
        - >-
          The value of this property indicates whether the task resource is
          system task or not.
      returned: always
      type: bool
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


class AzureRMTaskInfo(AzureRMModuleBase):
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
            task_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.task_name = None

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
        super(AzureRMTaskInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.task_name is not None):
            self.results['tasks'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['tasks'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.tasks.get(resource_group_name=self.resource_group_name,
                                                  registry_name=self.registry_name,
                                                  task_name=self.task_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.tasks.list(resource_group_name=self.resource_group_name,
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
    AzureRMTaskInfo()


if __name__ == '__main__':
    main()
