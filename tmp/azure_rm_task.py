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
module: azure_rm_task
version_added: '2.9'
short_description: Manage Azure Task instance.
description:
  - 'Create, update and delete instance of Azure Task.'
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
    required: true
    type: str
  location:
    description:
      - >-
        The location of the resource. This cannot be changed after the resource
        is created.
    type: str
  status:
    description:
      - The current status of task.
    type: str
    choices:
      - Disabled
      - Enabled
  platform:
    description:
      - The platform properties against which the run has to happen.
    type: dict
    suboptions:
      os:
        description:
          - The operating system type required for the run.
        required: true
        type: str
        choices:
          - Windows
          - Linux
      architecture:
        description:
          - The OS architecture.
        type: str
        choices:
          - amd64
          - x86
          - '386'
          - arm
          - arm64
      variant:
        description:
          - Variant of the CPU.
        type: str
        choices:
          - v6
          - v7
          - v8
  agent_configuration:
    description:
      - The machine configuration of the run agent.
    type: dict
    suboptions:
      cpu:
        description:
          - >-
            The CPU configuration in terms of number of cores required for the
            run.
        type: integer
  agent_pool_name:
    description:
      - The dedicated agent pool for the task.
    type: str
  timeout:
    description:
      - Run timeout in seconds.
    type: integer
  step:
    description:
      - The properties of a task step.
      - The properties for updating a task step.
    type: dict
    suboptions:
      type:
        description:
          - The type of the step.
        required: true
        type: str
        choices:
          - Docker
          - FileTask
          - EncodedTask
      base_image_dependencies:
        description:
          - List of base image dependencies for a step.
        type: list
        suboptions:
          type:
            description:
              - The type of the base image dependency.
            type: str
            choices:
              - BuildTime
              - RunTime
          registry:
            description:
              - The registry login server.
            type: str
          repository:
            description:
              - The repository name.
            type: str
          tag:
            description:
              - The tag name.
            type: str
          digest:
            description:
              - The sha256-based digest of the image manifest.
            type: str
      context_path:
        description:
          - >-
            The URL(absolute or relative) of the source context for the task
            step.
        type: str
      context_access_token:
        description:
          - >-
            The token (git PAT or SAS token of storage account blob) associated
            with the context for a step.
        type: str
  trigger:
    description:
      - The properties that describe all triggers for the task.
      - The properties for updating trigger properties.
    type: dict
    suboptions:
      timer_triggers:
        description:
          - The collection of timer triggers.
        type: list
        suboptions:
          schedule:
            description:
              - The CRON expression for the task schedule
            required: true
            type: str
          status:
            description:
              - The current status of trigger.
            type: str
            choices:
              - Disabled
              - Enabled
          name:
            description:
              - The name of the trigger.
            required: true
            type: str
      source_triggers:
        description:
          - The collection of triggers based on source code repository.
        type: list
        suboptions:
          source_repository:
            description:
              - The properties that describes the source(code) for the task.
            required: true
            type: dict
            suboptions:
              source_control_type:
                description:
                  - The type of source control service.
                required: true
                type: str
                choices:
                  - Github
                  - VisualStudioTeamService
              repository_url:
                description:
                  - The full URL to the source code repository
                required: true
                type: str
              branch:
                description:
                  - The branch name of the source code.
                type: str
              source_control_auth_properties:
                description:
                  - "The authorization properties for accessing the source code repository and to set up\r"
                  - webhooks for notifications.
                type: dict
                suboptions:
                  token_type:
                    description:
                      - The type of Auth token.
                    required: true
                    type: str
                    choices:
                      - PAT
                      - OAuth
                  token:
                    description:
                      - >-
                        The access token used to access the source control
                        provider.
                    required: true
                    type: str
                  refresh_token:
                    description:
                      - The refresh token used to refresh the access token.
                    type: str
                  scope:
                    description:
                      - The scope of the access token.
                    type: str
                  expires_in:
                    description:
                      - Time in seconds that the token remains valid
                    type: integer
          source_trigger_events:
            description:
              - The source event corresponding to the trigger.
            required: true
            type: list
          status:
            description:
              - The current status of trigger.
            type: str
            choices:
              - Disabled
              - Enabled
          name:
            description:
              - The name of the trigger.
            required: true
            type: str
      base_image_trigger:
        description:
          - The trigger based on base image dependencies.
        type: dict
        suboptions:
          base_image_trigger_type:
            description:
              - The type of the auto trigger for base image dependency updates.
            required: true
            type: str
            choices:
              - All
              - Runtime
          update_trigger_endpoint:
            description:
              - The endpoint URL for receiving update triggers.
            type: str
          update_trigger_payload_type:
            description:
              - Type of Payload body for Base image update triggers.
            type: str
            choices:
              - Default
              - Token
          status:
            description:
              - The current status of trigger.
            type: str
            choices:
              - Disabled
              - Enabled
          name:
            description:
              - The name of the trigger.
            required: true
            type: str
  credentials:
    description:
      - >-
        The properties that describes a set of credentials that will be used
        when this run is invoked.
      - >-
        The parameters that describes a set of credentials that will be used
        when this run is invoked.
    type: dict
    suboptions:
      source_registry:
        description:
          - >-
            Describes the credential parameters for accessing the source
            registry.
        type: dict
        suboptions:
          login_mode:
            description:
              - "The authentication mode which determines the source registry login scope. The credentials for the source registry\r"
              - "will be generated using the given scope. These credentials will be used to login to\r"
              - the source registry during the run.
            type: str
            choices:
              - None
              - Default
      custom_registries:
        description:
          - "Describes the credential parameters for accessing other custom registries. The key\r"
          - "for the dictionary item will be the registry login server (myregistry.azurecr.io) and\r"
          - >-
            the value of the item will be the registry credentials for accessing
            the registry.
        type: dictionary
  log_template:
    description:
      - >-
        The template that describes the repository and tag information for run
        log artifact.
    type: str
  is_system_task:
    description:
      - >-
        The value of this property indicates whether the task resource is system
        task or not.
    type: bool
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
      - Assert the state of the Task.
      - Use C(present) to create or update an Task and C(absent) to delete it.
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
    - name: Tasks_Create
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: mytTask
        

    - name: Tasks_Create_QuickTask
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: quicktask
        

    - name: Tasks_Create_WithSystemAndUserIdentities
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: mytTask
        

    - name: Tasks_Create_WithUserIdentities
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: mytTask
        

    - name: Tasks_Create_WithUserIdentities_WithSystemIdentity
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: mytTask
        

    - name: Tasks_Delete
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: myTask
        

    - name: Tasks_Update
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: myTask
        

    - name: Tasks_Update_QuickTask
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: quicktask
        

    - name: Tasks_Update_WithKeyVaultCustomCredentials
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: myTask
        

    - name: Tasks_Update_WithMSICustomCredentials
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: myTask
        

    - name: Tasks_Update_WithOpaqueCustomCredentials
      azure_rm_task: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        task_name: myTask
        

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
    - >-
      The location of the resource. This cannot be changed after the resource is
      created.
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
        - The URL(absolute or relative) of the source context for the task step.
      returned: always
      type: str
      sample: null
    context_access_token:
      description:
        - >-
          The token (git PAT or SAS token of storage account blob) associated
          with the context for a step.
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
            - The type of the auto trigger for base image dependency updates.
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
      The properties that describes a set of credentials that will be used when
      this run is invoked.
  returned: always
  type: dict
  sample: null
  contains:
    source_registry:
      description:
        - Describes the credential parameters for accessing the source registry.
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
      The template that describes the repository and tag information for run log
      artifact.
  returned: always
  type: str
  sample: null
is_system_task:
  description:
    - >-
      The value of this property indicates whether the task resource is system
      task or not.
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


class AzureRMTask(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['Disabled',
                         'Enabled']
            ),
            platform=dict(
                type='dict',
                disposition='/platform',
                options=dict(
                    os=dict(
                        type='str',
                        disposition='os',
                        choices=['Windows',
                                 'Linux'],
                        required=True
                    ),
                    architecture=dict(
                        type='str',
                        disposition='architecture',
                        choices=['amd64',
                                 'x86',
                                 '386',
                                 'arm',
                                 'arm64']
                    ),
                    variant=dict(
                        type='str',
                        disposition='variant',
                        choices=['v6',
                                 'v7',
                                 'v8']
                    )
                )
            ),
            agent_configuration=dict(
                type='dict',
                disposition='/agent_configuration',
                options=dict(
                    cpu=dict(
                        type='integer',
                        disposition='cpu'
                    )
                )
            ),
            agent_pool_name=dict(
                type='str',
                disposition='/agent_pool_name'
            ),
            timeout=dict(
                type='integer',
                disposition='/timeout'
            ),
            step=dict(
                type='dict',
                disposition='/step',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['Docker',
                                 'FileTask',
                                 'EncodedTask'],
                        required=True
                    ),
                    base_image_dependencies=dict(
                        type='list',
                        updatable=False,
                        disposition='base_image_dependencies',
                        elements='dict',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                choices=['BuildTime',
                                         'RunTime']
                            ),
                            registry=dict(
                                type='str',
                                disposition='registry'
                            ),
                            repository=dict(
                                type='str',
                                disposition='repository'
                            ),
                            tag=dict(
                                type='str',
                                disposition='tag'
                            ),
                            digest=dict(
                                type='str',
                                disposition='digest'
                            )
                        )
                    ),
                    context_path=dict(
                        type='str',
                        disposition='context_path'
                    ),
                    context_access_token=dict(
                        type='str',
                        disposition='context_access_token'
                    )
                )
            ),
            trigger=dict(
                type='dict',
                disposition='/trigger',
                options=dict(
                    timer_triggers=dict(
                        type='list',
                        disposition='timer_triggers',
                        elements='dict',
                        options=dict(
                            schedule=dict(
                                type='str',
                                disposition='schedule',
                                required=True
                            ),
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Disabled',
                                         'Enabled']
                            ),
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            )
                        )
                    ),
                    source_triggers=dict(
                        type='list',
                        disposition='source_triggers',
                        elements='dict',
                        options=dict(
                            source_repository=dict(
                                type='dict',
                                disposition='source_repository',
                                required=True,
                                options=dict(
                                    source_control_type=dict(
                                        type='str',
                                        disposition='source_control_type',
                                        choices=['Github',
                                                 'VisualStudioTeamService'],
                                        required=True
                                    ),
                                    repository_url=dict(
                                        type='str',
                                        disposition='repository_url',
                                        required=True
                                    ),
                                    branch=dict(
                                        type='str',
                                        disposition='branch'
                                    ),
                                    source_control_auth_properties=dict(
                                        type='dict',
                                        disposition='source_control_auth_properties',
                                        options=dict(
                                            token_type=dict(
                                                type='str',
                                                disposition='token_type',
                                                choices=['PAT',
                                                         'OAuth'],
                                                required=True
                                            ),
                                            token=dict(
                                                type='str',
                                                disposition='token',
                                                required=True
                                            ),
                                            refresh_token=dict(
                                                type='str',
                                                disposition='refresh_token'
                                            ),
                                            scope=dict(
                                                type='str',
                                                disposition='scope'
                                            ),
                                            expires_in=dict(
                                                type='integer',
                                                disposition='expires_in'
                                            )
                                        )
                                    )
                                )
                            ),
                            source_trigger_events=dict(
                                type='list',
                                disposition='source_trigger_events',
                                required=True,
                                elements='str'
                            ),
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Disabled',
                                         'Enabled']
                            ),
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            )
                        )
                    ),
                    base_image_trigger=dict(
                        type='dict',
                        disposition='base_image_trigger',
                        options=dict(
                            base_image_trigger_type=dict(
                                type='str',
                                disposition='base_image_trigger_type',
                                choices=['All',
                                         'Runtime'],
                                required=True
                            ),
                            update_trigger_endpoint=dict(
                                type='str',
                                disposition='update_trigger_endpoint'
                            ),
                            update_trigger_payload_type=dict(
                                type='str',
                                disposition='update_trigger_payload_type',
                                choices=['Default',
                                         'Token']
                            ),
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Disabled',
                                         'Enabled']
                            ),
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            )
                        )
                    )
                )
            ),
            credentials=dict(
                type='dict',
                disposition='/credentials',
                options=dict(
                    source_registry=dict(
                        type='dict',
                        disposition='source_registry',
                        options=dict(
                            login_mode=dict(
                                type='str',
                                disposition='login_mode',
                                choices=['None',
                                         'Default']
                            )
                        )
                    ),
                    custom_registries=dict(
                        type='dictionary',
                        disposition='custom_registries'
                    )
                )
            ),
            log_template=dict(
                type='str',
                disposition='/log_template'
            ),
            is_system_task=dict(
                type='bool',
                disposition='/is_system_task'
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
        self.task_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTask, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.tasks.create(resource_group_name=self.resource_group_name,
                                                         registry_name=self.registry_name,
                                                         task_name=self.task_name,
                                                         task_create_parameters=self.body)
            else:
                response = self.mgmt_client.tasks.update(resource_group_name=self.resource_group_name,
                                                         registry_name=self.registry_name,
                                                         task_name=self.task_name,
                                                         task_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Task instance.')
            self.fail('Error creating the Task instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.tasks.delete(resource_group_name=self.resource_group_name,
                                                     registry_name=self.registry_name,
                                                     task_name=self.task_name)
        except CloudError as e:
            self.log('Error attempting to delete the Task instance.')
            self.fail('Error deleting the Task instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.tasks.get(resource_group_name=self.resource_group_name,
                                                  registry_name=self.registry_name,
                                                  task_name=self.task_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTask()


if __name__ == '__main__':
    main()
