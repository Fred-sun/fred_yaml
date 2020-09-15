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
module: azure_rm_containergroup
version_added: '2.9'
short_description: Manage Azure ContainerGroup instance.
description:
  - 'Create, update and delete instance of Azure ContainerGroup.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  container_group_name:
    description:
      - The name of the container group.
    required: true
    type: str
  location:
    description:
      - The resource location.
    type: str
  containers:
    description:
      - The containers within the container group.
    type: list
    suboptions:
      name:
        description:
          - The user-provided name of the container instance.
        required: true
        type: str
      image:
        description:
          - The name of the image used to create the container instance.
        required: true
        type: str
      command:
        description:
          - The commands to execute within the container instance in exec form.
        type: list
      ports:
        description:
          - The exposed ports on the container instance.
        type: list
        suboptions:
          protocol:
            description:
              - The protocol associated with the port.
            type: str
            choices:
              - TCP
              - UDP
          port:
            description:
              - The port number exposed within the container group.
            required: true
            type: integer
      environment_variables:
        description:
          - The environment variables to set in the container instance.
        type: list
        suboptions:
          name:
            description:
              - The name of the environment variable.
            required: true
            type: str
          value:
            description:
              - The value of the environment variable.
            type: str
          secure_value:
            description:
              - The value of the secure environment variable.
            type: str
      instance_view:
        description:
          - The instance view of the container instance. Only valid in response.
        type: dict
        suboptions:
          restart_count:
            description:
              - >-
                The number of times that the container instance has been
                restarted.
            type: integer
          current_state:
            description:
              - Current container instance state.
            type: dict
            suboptions:
              state:
                description:
                  - The state of the container instance.
                type: str
              start_time:
                description:
                  - The date-time when the container instance state started.
                type: str
              exit_code:
                description:
                  - >-
                    The container instance exit codes correspond to those from
                    the `docker run` command.
                type: integer
              finish_time:
                description:
                  - The date-time when the container instance state finished.
                type: str
              detail_status:
                description:
                  - The human-readable status of the container instance state.
                type: str
          previous_state:
            description:
              - Previous container instance state.
            type: dict
            suboptions:
              state:
                description:
                  - The state of the container instance.
                type: str
              start_time:
                description:
                  - The date-time when the container instance state started.
                type: str
              exit_code:
                description:
                  - >-
                    The container instance exit codes correspond to those from
                    the `docker run` command.
                type: integer
              finish_time:
                description:
                  - The date-time when the container instance state finished.
                type: str
              detail_status:
                description:
                  - The human-readable status of the container instance state.
                type: str
          events:
            description:
              - The events of the container instance.
            type: list
            suboptions:
              count:
                description:
                  - The count of the event.
                type: integer
              first_timestamp:
                description:
                  - The date-time of the earliest logged event.
                type: str
              last_timestamp:
                description:
                  - The date-time of the latest logged event.
                type: str
              name:
                description:
                  - The event name.
                type: str
              message:
                description:
                  - The event message.
                type: str
              type:
                description:
                  - The event type.
                type: str
      resources:
        description:
          - The resource requirements of the container instance.
        required: true
        type: dict
        suboptions:
          requests:
            description:
              - The resource requests of this container instance.
            required: true
            type: dict
            suboptions:
              memory_in_gb:
                description:
                  - The memory request in GB of this container instance.
                required: true
                type: number
              cpu:
                description:
                  - The CPU request of this container instance.
                required: true
                type: number
              gpu:
                description:
                  - The GPU request of this container instance.
                type: dict
                suboptions:
                  count:
                    description:
                      - The count of the GPU resource.
                    required: true
                    type: integer
                  sku:
                    description:
                      - The SKU of the GPU resource.
                    required: true
                    type: str
                    choices:
                      - K80
                      - P100
                      - V100
          limits:
            description:
              - The resource limits of this container instance.
            type: dict
            suboptions:
              memory_in_gb:
                description:
                  - The memory limit in GB of this container instance.
                type: number
              cpu:
                description:
                  - The CPU limit of this container instance.
                type: number
              gpu:
                description:
                  - The GPU limit of this container instance.
                type: dict
                suboptions:
                  count:
                    description:
                      - The count of the GPU resource.
                    required: true
                    type: integer
                  sku:
                    description:
                      - The SKU of the GPU resource.
                    required: true
                    type: str
                    choices:
                      - K80
                      - P100
                      - V100
      volume_mounts:
        description:
          - The volume mounts available to the container instance.
        type: list
        suboptions:
          name:
            description:
              - The name of the volume mount.
            required: true
            type: str
          mount_path:
            description:
              - >-
                The path within the container where the volume should be
                mounted. Must not contain colon (:).
            required: true
            type: str
          read_only:
            description:
              - The flag indicating whether the volume mount is read-only.
            type: bool
      liveness_probe:
        description:
          - The liveness probe.
        type: dict
        suboptions:
          exec:
            description:
              - The execution command to probe
            type: dict
            suboptions:
              command:
                description:
                  - The commands to execute within the container.
                type: list
          http_get:
            description:
              - The Http Get settings to probe
            type: dict
            suboptions:
              path:
                description:
                  - The path to probe.
                type: str
              port:
                description:
                  - The port number to probe.
                required: true
                type: integer
              scheme:
                description:
                  - The scheme.
                type: str
                choices:
                  - http
                  - https
          initial_delay_seconds:
            description:
              - The initial delay seconds.
            type: integer
          period_seconds:
            description:
              - The period seconds.
            type: integer
          failure_threshold:
            description:
              - The failure threshold.
            type: integer
          success_threshold:
            description:
              - The success threshold.
            type: integer
          timeout_seconds:
            description:
              - The timeout seconds.
            type: integer
      readiness_probe:
        description:
          - The readiness probe.
        type: dict
        suboptions:
          exec:
            description:
              - The execution command to probe
            type: dict
            suboptions:
              command:
                description:
                  - The commands to execute within the container.
                type: list
          http_get:
            description:
              - The Http Get settings to probe
            type: dict
            suboptions:
              path:
                description:
                  - The path to probe.
                type: str
              port:
                description:
                  - The port number to probe.
                required: true
                type: integer
              scheme:
                description:
                  - The scheme.
                type: str
                choices:
                  - http
                  - https
          initial_delay_seconds:
            description:
              - The initial delay seconds.
            type: integer
          period_seconds:
            description:
              - The period seconds.
            type: integer
          failure_threshold:
            description:
              - The failure threshold.
            type: integer
          success_threshold:
            description:
              - The success threshold.
            type: integer
          timeout_seconds:
            description:
              - The timeout seconds.
            type: integer
  image_registry_credentials:
    description:
      - >-
        The image registry credentials by which the container group is created
        from.
    type: list
    suboptions:
      server:
        description:
          - >-
            The Docker image registry server without a protocol such as "http"
            and "https".
        required: true
        type: str
      username:
        description:
          - The username for the private registry.
        required: true
        type: str
      password:
        description:
          - The password for the private registry.
        type: str
  restart_policy:
    description:
      - 'Restart policy for all containers within the container group. '
      - '- `Always` Always restart'
      - '- `OnFailure` Restart on failure'
      - '- `Never` Never restart'
      - ''
    type: str
    choices:
      - Always
      - OnFailure
      - Never
  os_type:
    description:
      - >-
        The operating system type required by the containers in the container
        group.
    type: str
    choices:
      - Windows
      - Linux
  volumes:
    description:
      - >-
        The list of volumes that can be mounted by containers in this container
        group.
    type: list
    suboptions:
      name:
        description:
          - The name of the volume.
        required: true
        type: str
      azure_file:
        description:
          - The Azure File volume.
        type: dict
        suboptions:
          share_name:
            description:
              - The name of the Azure File share to be mounted as a volume.
            required: true
            type: str
          read_only:
            description:
              - >-
                The flag indicating whether the Azure File shared mounted as a
                volume is read-only.
            type: bool
          storage_account_name:
            description:
              - >-
                The name of the storage account that contains the Azure File
                share.
            required: true
            type: str
          storage_account_key:
            description:
              - >-
                The storage account access key used to access the Azure File
                share.
            type: str
      empty_dir:
        description:
          - The empty directory volume.
        type: any
      secret:
        description:
          - The secret volume.
        type: dictionary
      git_repo:
        description:
          - The git repo volume.
        type: dict
        suboptions:
          directory:
            description:
              - >-
                Target directory name. Must not contain or start with '..'.  If
                '.' is supplied, the volume directory will be the git
                repository.  Otherwise, if specified, the volume will contain
                the git repository in the subdirectory with the given name.
            type: str
          repository:
            description:
              - Repository URL
            required: true
            type: str
          revision:
            description:
              - Commit hash for the specified revision.
            type: str
  dns_config:
    description:
      - The DNS config information for a container group.
    type: dict
    suboptions:
      name_servers:
        description:
          - The DNS servers for the container group.
        required: true
        type: list
      search_domains:
        description:
          - The DNS search domains for hostname lookup in the container group.
        type: str
      options:
        description:
          - The DNS options for the container group.
        type: str
  sku:
    description:
      - The SKU for a container group.
    type: str
    choices:
      - Standard
      - Dedicated
  encryption_properties:
    description:
      - The encryption properties for a container group.
    type: dict
    suboptions:
      vault_base_url:
        description:
          - The keyvault base url.
        required: true
        type: str
      key_name:
        description:
          - The encryption key name.
        required: true
        type: str
      key_version:
        description:
          - The encryption key version.
        required: true
        type: str
  init_containers:
    description:
      - The init containers for a container group.
    type: list
    suboptions:
      name:
        description:
          - The name for the init container.
        required: true
        type: str
      image:
        description:
          - The image of the init container.
        type: str
      command:
        description:
          - The command to execute within the init container in exec form.
        type: list
      environment_variables:
        description:
          - The environment variables to set in the init container.
        type: list
        suboptions:
          name:
            description:
              - The name of the environment variable.
            required: true
            type: str
          value:
            description:
              - The value of the environment variable.
            type: str
          secure_value:
            description:
              - The value of the secure environment variable.
            type: str
      instance_view:
        description:
          - The instance view of the init container. Only valid in response.
        type: dict
        suboptions:
          restart_count:
            description:
              - The number of times that the init container has been restarted.
            type: integer
          current_state:
            description:
              - The current state of the init container.
            type: dict
            suboptions:
              state:
                description:
                  - The state of the container instance.
                type: str
              start_time:
                description:
                  - The date-time when the container instance state started.
                type: str
              exit_code:
                description:
                  - >-
                    The container instance exit codes correspond to those from
                    the `docker run` command.
                type: integer
              finish_time:
                description:
                  - The date-time when the container instance state finished.
                type: str
              detail_status:
                description:
                  - The human-readable status of the container instance state.
                type: str
          previous_state:
            description:
              - The previous state of the init container.
            type: dict
            suboptions:
              state:
                description:
                  - The state of the container instance.
                type: str
              start_time:
                description:
                  - The date-time when the container instance state started.
                type: str
              exit_code:
                description:
                  - >-
                    The container instance exit codes correspond to those from
                    the `docker run` command.
                type: integer
              finish_time:
                description:
                  - The date-time when the container instance state finished.
                type: str
              detail_status:
                description:
                  - The human-readable status of the container instance state.
                type: str
          events:
            description:
              - The events of the init container.
            type: list
            suboptions:
              count:
                description:
                  - The count of the event.
                type: integer
              first_timestamp:
                description:
                  - The date-time of the earliest logged event.
                type: str
              last_timestamp:
                description:
                  - The date-time of the latest logged event.
                type: str
              name:
                description:
                  - The event name.
                type: str
              message:
                description:
                  - The event message.
                type: str
              type:
                description:
                  - The event type.
                type: str
      volume_mounts:
        description:
          - The volume mounts available to the init container.
        type: list
        suboptions:
          name:
            description:
              - The name of the volume mount.
            required: true
            type: str
          mount_path:
            description:
              - >-
                The path within the container where the volume should be
                mounted. Must not contain colon (:).
            required: true
            type: str
          read_only:
            description:
              - The flag indicating whether the volume mount is read-only.
            type: bool
  id:
    description:
      - The identifier for a network profile.
    type: str
  log_analytics:
    description:
      - Container group log analytics information.
    type: dict
    suboptions:
      workspace_id:
        description:
          - The workspace id for log analytics
        required: true
        type: str
      workspace_key:
        description:
          - The workspace key for log analytics
        required: true
        type: str
      log_type:
        description:
          - The log type to be used.
        type: str
        choices:
          - ContainerInsights
          - ContainerInstanceLogs
      metadata:
        description:
          - Metadata for log analytics.
        type: dictionary
  ports:
    description:
      - The list of ports exposed on the container group.
    type: list
    suboptions:
      protocol:
        description:
          - The protocol associated with the port.
        type: str
        choices:
          - TCP
          - UDP
      port:
        description:
          - The port number.
        required: true
        type: integer
  type:
    description:
      - Specifies if the IP is exposed to the public internet or private VNET.
    type: str
    choices:
      - Public
      - Private
  ip:
    description:
      - The IP exposed to the public internet.
    type: str
  dns_name_label:
    description:
      - The Dns name label for the IP.
    type: str
  resource_identity_type:
    description:
      - >-
        The type of identity used for the container group. The type
        'SystemAssigned, UserAssigned' includes both an implicitly created
        identity and a set of user assigned identities. The type 'None' will
        remove any identities from the container group.
    type: sealed-choice
  user_assigned_identities:
    description:
      - >-
        The list of user identities associated with the container group. The
        user identity dictionary key references will be ARM resource ids in the
        form:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    type: dictionary
  state:
    description:
      - Assert the state of the ContainerGroup.
      - >-
        Use C(present) to create or update an ContainerGroup and C(absent) to
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
    - name: ContainerGroupsCreateOrUpdate
      azure_rm_containergroup: 
        container_group_name: demo1
        resource_group_name: demo
        

    - name: ContainerGroupsUpdate
      azure_rm_containergroup: 
        container_group_name: demo1
        resource_group_name: demoResource
        

    - name: ContainerGroupsDelete
      azure_rm_containergroup: 
        container_group_name: demo1
        resource_group_name: demo
        

'''

RETURN = '''
id:
  description:
    - The resource id.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - The resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: dictionary
  sample: null
provisioning_state:
  description:
    - >-
      The provisioning state of the container group. This only appears in the
      response.
  returned: always
  type: str
  sample: null
containers:
  description:
    - The containers within the container group.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The user-provided name of the container instance.
      returned: always
      type: str
      sample: null
    image:
      description:
        - The name of the image used to create the container instance.
      returned: always
      type: str
      sample: null
    command:
      description:
        - The commands to execute within the container instance in exec form.
      returned: always
      type: list
      sample: null
    ports:
      description:
        - The exposed ports on the container instance.
      returned: always
      type: list
      sample: null
      contains:
        protocol:
          description:
            - The protocol associated with the port.
          returned: always
          type: str
          sample: null
        port:
          description:
            - The port number exposed within the container group.
          returned: always
          type: integer
          sample: null
    environment_variables:
      description:
        - The environment variables to set in the container instance.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the environment variable.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The value of the environment variable.
          returned: always
          type: str
          sample: null
        secure_value:
          description:
            - The value of the secure environment variable.
          returned: always
          type: str
          sample: null
    instance_view:
      description:
        - The instance view of the container instance. Only valid in response.
      returned: always
      type: dict
      sample: null
      contains:
        restart_count:
          description:
            - >-
              The number of times that the container instance has been
              restarted.
          returned: always
          type: integer
          sample: null
        current_state:
          description:
            - Current container instance state.
          returned: always
          type: dict
          sample: null
          contains:
            state:
              description:
                - The state of the container instance.
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - The date-time when the container instance state started.
              returned: always
              type: str
              sample: null
            exit_code:
              description:
                - >-
                  The container instance exit codes correspond to those from the
                  `docker run` command.
              returned: always
              type: integer
              sample: null
            finish_time:
              description:
                - The date-time when the container instance state finished.
              returned: always
              type: str
              sample: null
            detail_status:
              description:
                - The human-readable status of the container instance state.
              returned: always
              type: str
              sample: null
        previous_state:
          description:
            - Previous container instance state.
          returned: always
          type: dict
          sample: null
          contains:
            state:
              description:
                - The state of the container instance.
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - The date-time when the container instance state started.
              returned: always
              type: str
              sample: null
            exit_code:
              description:
                - >-
                  The container instance exit codes correspond to those from the
                  `docker run` command.
              returned: always
              type: integer
              sample: null
            finish_time:
              description:
                - The date-time when the container instance state finished.
              returned: always
              type: str
              sample: null
            detail_status:
              description:
                - The human-readable status of the container instance state.
              returned: always
              type: str
              sample: null
        events:
          description:
            - The events of the container instance.
          returned: always
          type: list
          sample: null
          contains:
            count:
              description:
                - The count of the event.
              returned: always
              type: integer
              sample: null
            first_timestamp:
              description:
                - The date-time of the earliest logged event.
              returned: always
              type: str
              sample: null
            last_timestamp:
              description:
                - The date-time of the latest logged event.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The event name.
              returned: always
              type: str
              sample: null
            message:
              description:
                - The event message.
              returned: always
              type: str
              sample: null
            type:
              description:
                - The event type.
              returned: always
              type: str
              sample: null
    resources:
      description:
        - The resource requirements of the container instance.
      returned: always
      type: dict
      sample: null
      contains:
        requests:
          description:
            - The resource requests of this container instance.
          returned: always
          type: dict
          sample: null
          contains:
            memory_in_gb:
              description:
                - The memory request in GB of this container instance.
              returned: always
              type: number
              sample: null
            cpu:
              description:
                - The CPU request of this container instance.
              returned: always
              type: number
              sample: null
            gpu:
              description:
                - The GPU request of this container instance.
              returned: always
              type: dict
              sample: null
              contains:
                count:
                  description:
                    - The count of the GPU resource.
                  returned: always
                  type: integer
                  sample: null
                sku:
                  description:
                    - The SKU of the GPU resource.
                  returned: always
                  type: str
                  sample: null
        limits:
          description:
            - The resource limits of this container instance.
          returned: always
          type: dict
          sample: null
          contains:
            memory_in_gb:
              description:
                - The memory limit in GB of this container instance.
              returned: always
              type: number
              sample: null
            cpu:
              description:
                - The CPU limit of this container instance.
              returned: always
              type: number
              sample: null
            gpu:
              description:
                - The GPU limit of this container instance.
              returned: always
              type: dict
              sample: null
              contains:
                count:
                  description:
                    - The count of the GPU resource.
                  returned: always
                  type: integer
                  sample: null
                sku:
                  description:
                    - The SKU of the GPU resource.
                  returned: always
                  type: str
                  sample: null
    volume_mounts:
      description:
        - The volume mounts available to the container instance.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the volume mount.
          returned: always
          type: str
          sample: null
        mount_path:
          description:
            - >-
              The path within the container where the volume should be mounted.
              Must not contain colon (:).
          returned: always
          type: str
          sample: null
        read_only:
          description:
            - The flag indicating whether the volume mount is read-only.
          returned: always
          type: bool
          sample: null
    liveness_probe:
      description:
        - The liveness probe.
      returned: always
      type: dict
      sample: null
      contains:
        exec:
          description:
            - The execution command to probe
          returned: always
          type: dict
          sample: null
          contains:
            command:
              description:
                - The commands to execute within the container.
              returned: always
              type: list
              sample: null
        http_get:
          description:
            - The Http Get settings to probe
          returned: always
          type: dict
          sample: null
          contains:
            path:
              description:
                - The path to probe.
              returned: always
              type: str
              sample: null
            port:
              description:
                - The port number to probe.
              returned: always
              type: integer
              sample: null
            scheme:
              description:
                - The scheme.
              returned: always
              type: str
              sample: null
        initial_delay_seconds:
          description:
            - The initial delay seconds.
          returned: always
          type: integer
          sample: null
        period_seconds:
          description:
            - The period seconds.
          returned: always
          type: integer
          sample: null
        failure_threshold:
          description:
            - The failure threshold.
          returned: always
          type: integer
          sample: null
        success_threshold:
          description:
            - The success threshold.
          returned: always
          type: integer
          sample: null
        timeout_seconds:
          description:
            - The timeout seconds.
          returned: always
          type: integer
          sample: null
    readiness_probe:
      description:
        - The readiness probe.
      returned: always
      type: dict
      sample: null
      contains:
        exec:
          description:
            - The execution command to probe
          returned: always
          type: dict
          sample: null
          contains:
            command:
              description:
                - The commands to execute within the container.
              returned: always
              type: list
              sample: null
        http_get:
          description:
            - The Http Get settings to probe
          returned: always
          type: dict
          sample: null
          contains:
            path:
              description:
                - The path to probe.
              returned: always
              type: str
              sample: null
            port:
              description:
                - The port number to probe.
              returned: always
              type: integer
              sample: null
            scheme:
              description:
                - The scheme.
              returned: always
              type: str
              sample: null
        initial_delay_seconds:
          description:
            - The initial delay seconds.
          returned: always
          type: integer
          sample: null
        period_seconds:
          description:
            - The period seconds.
          returned: always
          type: integer
          sample: null
        failure_threshold:
          description:
            - The failure threshold.
          returned: always
          type: integer
          sample: null
        success_threshold:
          description:
            - The success threshold.
          returned: always
          type: integer
          sample: null
        timeout_seconds:
          description:
            - The timeout seconds.
          returned: always
          type: integer
          sample: null
image_registry_credentials:
  description:
    - >-
      The image registry credentials by which the container group is created
      from.
  returned: always
  type: list
  sample: null
  contains:
    server:
      description:
        - >-
          The Docker image registry server without a protocol such as "http" and
          "https".
      returned: always
      type: str
      sample: null
    username:
      description:
        - The username for the private registry.
      returned: always
      type: str
      sample: null
    password:
      description:
        - The password for the private registry.
      returned: always
      type: str
      sample: null
restart_policy:
  description:
    - |
      Restart policy for all containers within the container group. 
      - `Always` Always restart
      - `OnFailure` Restart on failure
      - `Never` Never restart
  returned: always
  type: str
  sample: null
os_type:
  description:
    - >-
      The operating system type required by the containers in the container
      group.
  returned: always
  type: str
  sample: null
volumes:
  description:
    - >-
      The list of volumes that can be mounted by containers in this container
      group.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The name of the volume.
      returned: always
      type: str
      sample: null
    azure_file:
      description:
        - The Azure File volume.
      returned: always
      type: dict
      sample: null
      contains:
        share_name:
          description:
            - The name of the Azure File share to be mounted as a volume.
          returned: always
          type: str
          sample: null
        read_only:
          description:
            - >-
              The flag indicating whether the Azure File shared mounted as a
              volume is read-only.
          returned: always
          type: bool
          sample: null
        storage_account_name:
          description:
            - >-
              The name of the storage account that contains the Azure File
              share.
          returned: always
          type: str
          sample: null
        storage_account_key:
          description:
            - >-
              The storage account access key used to access the Azure File
              share.
          returned: always
          type: str
          sample: null
    empty_dir:
      description:
        - The empty directory volume.
      returned: always
      type: any
      sample: null
    secret:
      description:
        - The secret volume.
      returned: always
      type: dictionary
      sample: null
    git_repo:
      description:
        - The git repo volume.
      returned: always
      type: dict
      sample: null
      contains:
        directory:
          description:
            - >-
              Target directory name. Must not contain or start with '..'.  If
              '.' is supplied, the volume directory will be the git repository. 
              Otherwise, if specified, the volume will contain the git
              repository in the subdirectory with the given name.
          returned: always
          type: str
          sample: null
        repository:
          description:
            - Repository URL
          returned: always
          type: str
          sample: null
        revision:
          description:
            - Commit hash for the specified revision.
          returned: always
          type: str
          sample: null
instance_view:
  description:
    - The instance view of the container group. Only valid in response.
  returned: always
  type: dict
  sample: null
  contains:
    events:
      description:
        - The events of this container group.
      returned: always
      type: list
      sample: null
      contains:
        count:
          description:
            - The count of the event.
          returned: always
          type: integer
          sample: null
        first_timestamp:
          description:
            - The date-time of the earliest logged event.
          returned: always
          type: str
          sample: null
        last_timestamp:
          description:
            - The date-time of the latest logged event.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The event name.
          returned: always
          type: str
          sample: null
        message:
          description:
            - The event message.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The event type.
          returned: always
          type: str
          sample: null
    state:
      description:
        - The state of the container group. Only valid in response.
      returned: always
      type: str
      sample: null
dns_config:
  description:
    - The DNS config information for a container group.
  returned: always
  type: dict
  sample: null
  contains:
    name_servers:
      description:
        - The DNS servers for the container group.
      returned: always
      type: list
      sample: null
    search_domains:
      description:
        - The DNS search domains for hostname lookup in the container group.
      returned: always
      type: str
      sample: null
    options:
      description:
        - The DNS options for the container group.
      returned: always
      type: str
      sample: null
sku:
  description:
    - The SKU for a container group.
  returned: always
  type: str
  sample: null
encryption_properties:
  description:
    - The encryption properties for a container group.
  returned: always
  type: dict
  sample: null
  contains:
    vault_base_url:
      description:
        - The keyvault base url.
      returned: always
      type: str
      sample: null
    key_name:
      description:
        - The encryption key name.
      returned: always
      type: str
      sample: null
    key_version:
      description:
        - The encryption key version.
      returned: always
      type: str
      sample: null
init_containers:
  description:
    - The init containers for a container group.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The name for the init container.
      returned: always
      type: str
      sample: null
    image:
      description:
        - The image of the init container.
      returned: always
      type: str
      sample: null
    command:
      description:
        - The command to execute within the init container in exec form.
      returned: always
      type: list
      sample: null
    environment_variables:
      description:
        - The environment variables to set in the init container.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the environment variable.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The value of the environment variable.
          returned: always
          type: str
          sample: null
        secure_value:
          description:
            - The value of the secure environment variable.
          returned: always
          type: str
          sample: null
    instance_view:
      description:
        - The instance view of the init container. Only valid in response.
      returned: always
      type: dict
      sample: null
      contains:
        restart_count:
          description:
            - The number of times that the init container has been restarted.
          returned: always
          type: integer
          sample: null
        current_state:
          description:
            - The current state of the init container.
          returned: always
          type: dict
          sample: null
          contains:
            state:
              description:
                - The state of the container instance.
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - The date-time when the container instance state started.
              returned: always
              type: str
              sample: null
            exit_code:
              description:
                - >-
                  The container instance exit codes correspond to those from the
                  `docker run` command.
              returned: always
              type: integer
              sample: null
            finish_time:
              description:
                - The date-time when the container instance state finished.
              returned: always
              type: str
              sample: null
            detail_status:
              description:
                - The human-readable status of the container instance state.
              returned: always
              type: str
              sample: null
        previous_state:
          description:
            - The previous state of the init container.
          returned: always
          type: dict
          sample: null
          contains:
            state:
              description:
                - The state of the container instance.
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - The date-time when the container instance state started.
              returned: always
              type: str
              sample: null
            exit_code:
              description:
                - >-
                  The container instance exit codes correspond to those from the
                  `docker run` command.
              returned: always
              type: integer
              sample: null
            finish_time:
              description:
                - The date-time when the container instance state finished.
              returned: always
              type: str
              sample: null
            detail_status:
              description:
                - The human-readable status of the container instance state.
              returned: always
              type: str
              sample: null
        events:
          description:
            - The events of the init container.
          returned: always
          type: list
          sample: null
          contains:
            count:
              description:
                - The count of the event.
              returned: always
              type: integer
              sample: null
            first_timestamp:
              description:
                - The date-time of the earliest logged event.
              returned: always
              type: str
              sample: null
            last_timestamp:
              description:
                - The date-time of the latest logged event.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The event name.
              returned: always
              type: str
              sample: null
            message:
              description:
                - The event message.
              returned: always
              type: str
              sample: null
            type:
              description:
                - The event type.
              returned: always
              type: str
              sample: null
    volume_mounts:
      description:
        - The volume mounts available to the init container.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the volume mount.
          returned: always
          type: str
          sample: null
        mount_path:
          description:
            - >-
              The path within the container where the volume should be mounted.
              Must not contain colon (:).
          returned: always
          type: str
          sample: null
        read_only:
          description:
            - The flag indicating whether the volume mount is read-only.
          returned: always
          type: bool
          sample: null
id_properties_network_profile_id:
  description:
    - The identifier for a network profile.
  returned: always
  type: str
  sample: null
log_analytics:
  description:
    - Container group log analytics information.
  returned: always
  type: dict
  sample: null
  contains:
    workspace_id:
      description:
        - The workspace id for log analytics
      returned: always
      type: str
      sample: null
    workspace_key:
      description:
        - The workspace key for log analytics
      returned: always
      type: str
      sample: null
    log_type:
      description:
        - The log type to be used.
      returned: always
      type: str
      sample: null
    metadata:
      description:
        - Metadata for log analytics.
      returned: always
      type: dictionary
      sample: null
ports:
  description:
    - The list of ports exposed on the container group.
  returned: always
  type: list
  sample: null
  contains:
    protocol:
      description:
        - The protocol associated with the port.
      returned: always
      type: str
      sample: null
    port:
      description:
        - The port number.
      returned: always
      type: integer
      sample: null
type_properties_ip_address_type:
  description:
    - Specifies if the IP is exposed to the public internet or private VNET.
  returned: always
  type: str
  sample: null
ip:
  description:
    - The IP exposed to the public internet.
  returned: always
  type: str
  sample: null
dns_name_label:
  description:
    - The Dns name label for the IP.
  returned: always
  type: str
  sample: null
fqdn:
  description:
    - The FQDN for the IP.
  returned: always
  type: str
  sample: null
principal_id:
  description:
    - >-
      The principal id of the container group identity. This property will only
      be provided for a system assigned identity.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - >-
      The tenant id associated with the container group. This property will only
      be provided for a system assigned identity.
  returned: always
  type: str
  sample: null
type_identity_type:
  description:
    - >-
      The type of identity used for the container group. The type
      'SystemAssigned, UserAssigned' includes both an implicitly created
      identity and a set of user assigned identities. The type 'None' will
      remove any identities from the container group.
  returned: always
  type: sealed-choice
  sample: null
user_assigned_identities:
  description:
    - >-
      The list of user identities associated with the container group. The user
      identity dictionary key references will be ARM resource ids in the form:
      '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
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
    from azure.mgmt.container import ContainerInstanceManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMContainerGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            container_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            containers=dict(
                type='list',
                disposition='/containers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    image=dict(
                        type='str',
                        disposition='image',
                        required=True
                    ),
                    command=dict(
                        type='list',
                        disposition='command',
                        elements='str'
                    ),
                    ports=dict(
                        type='list',
                        disposition='ports',
                        elements='dict',
                        options=dict(
                            protocol=dict(
                                type='str',
                                disposition='protocol',
                                choices=['TCP',
                                         'UDP']
                            ),
                            port=dict(
                                type='integer',
                                disposition='port',
                                required=True
                            )
                        )
                    ),
                    environment_variables=dict(
                        type='list',
                        disposition='environment_variables',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            value=dict(
                                type='str',
                                disposition='value'
                            ),
                            secure_value=dict(
                                type='str',
                                disposition='secure_value'
                            )
                        )
                    ),
                    instance_view=dict(
                        type='dict',
                        updatable=False,
                        disposition='instance_view',
                        options=dict(
                            restart_count=dict(
                                type='integer',
                                updatable=False,
                                disposition='restart_count'
                            ),
                            current_state=dict(
                                type='dict',
                                updatable=False,
                                disposition='current_state',
                                options=dict(
                                    state=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='state'
                                    ),
                                    start_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='start_time'
                                    ),
                                    exit_code=dict(
                                        type='integer',
                                        updatable=False,
                                        disposition='exit_code'
                                    ),
                                    finish_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='finish_time'
                                    ),
                                    detail_status=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='detail_status'
                                    )
                                )
                            ),
                            previous_state=dict(
                                type='dict',
                                updatable=False,
                                disposition='previous_state',
                                options=dict(
                                    state=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='state'
                                    ),
                                    start_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='start_time'
                                    ),
                                    exit_code=dict(
                                        type='integer',
                                        updatable=False,
                                        disposition='exit_code'
                                    ),
                                    finish_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='finish_time'
                                    ),
                                    detail_status=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='detail_status'
                                    )
                                )
                            ),
                            events=dict(
                                type='list',
                                updatable=False,
                                disposition='events',
                                elements='dict',
                                options=dict(
                                    count=dict(
                                        type='integer',
                                        updatable=False,
                                        disposition='count'
                                    ),
                                    first_timestamp=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='first_timestamp'
                                    ),
                                    last_timestamp=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='last_timestamp'
                                    ),
                                    name=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='name'
                                    ),
                                    message=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='message'
                                    ),
                                    type=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='type'
                                    )
                                )
                            )
                        )
                    ),
                    resources=dict(
                        type='dict',
                        disposition='resources',
                        required=True,
                        options=dict(
                            requests=dict(
                                type='dict',
                                disposition='requests',
                                required=True,
                                options=dict(
                                    memory_in_gb=dict(
                                        type='number',
                                        disposition='memory_in_gb',
                                        required=True
                                    ),
                                    cpu=dict(
                                        type='number',
                                        disposition='cpu',
                                        required=True
                                    ),
                                    gpu=dict(
                                        type='dict',
                                        disposition='gpu',
                                        options=dict(
                                            count=dict(
                                                type='integer',
                                                disposition='count',
                                                required=True
                                            ),
                                            sku=dict(
                                                type='str',
                                                disposition='sku',
                                                choices=['K80',
                                                         'P100',
                                                         'V100'],
                                                required=True
                                            )
                                        )
                                    )
                                )
                            ),
                            limits=dict(
                                type='dict',
                                disposition='limits',
                                options=dict(
                                    memory_in_gb=dict(
                                        type='number',
                                        disposition='memory_in_gb'
                                    ),
                                    cpu=dict(
                                        type='number',
                                        disposition='cpu'
                                    ),
                                    gpu=dict(
                                        type='dict',
                                        disposition='gpu',
                                        options=dict(
                                            count=dict(
                                                type='integer',
                                                disposition='count',
                                                required=True
                                            ),
                                            sku=dict(
                                                type='str',
                                                disposition='sku',
                                                choices=['K80',
                                                         'P100',
                                                         'V100'],
                                                required=True
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    volume_mounts=dict(
                        type='list',
                        disposition='volume_mounts',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            mount_path=dict(
                                type='str',
                                disposition='mount_path',
                                required=True
                            ),
                            read_only=dict(
                                type='bool',
                                disposition='read_only'
                            )
                        )
                    ),
                    liveness_probe=dict(
                        type='dict',
                        disposition='liveness_probe',
                        options=dict(
                            exec=dict(
                                type='dict',
                                disposition='exec',
                                options=dict(
                                    command=dict(
                                        type='list',
                                        disposition='command',
                                        elements='str'
                                    )
                                )
                            ),
                            http_get=dict(
                                type='dict',
                                disposition='http_get',
                                options=dict(
                                    path=dict(
                                        type='str',
                                        disposition='path'
                                    ),
                                    port=dict(
                                        type='integer',
                                        disposition='port',
                                        required=True
                                    ),
                                    scheme=dict(
                                        type='str',
                                        disposition='scheme',
                                        choices=['http',
                                                 'https']
                                    )
                                )
                            ),
                            initial_delay_seconds=dict(
                                type='integer',
                                disposition='initial_delay_seconds'
                            ),
                            period_seconds=dict(
                                type='integer',
                                disposition='period_seconds'
                            ),
                            failure_threshold=dict(
                                type='integer',
                                disposition='failure_threshold'
                            ),
                            success_threshold=dict(
                                type='integer',
                                disposition='success_threshold'
                            ),
                            timeout_seconds=dict(
                                type='integer',
                                disposition='timeout_seconds'
                            )
                        )
                    ),
                    readiness_probe=dict(
                        type='dict',
                        disposition='readiness_probe',
                        options=dict(
                            exec=dict(
                                type='dict',
                                disposition='exec',
                                options=dict(
                                    command=dict(
                                        type='list',
                                        disposition='command',
                                        elements='str'
                                    )
                                )
                            ),
                            http_get=dict(
                                type='dict',
                                disposition='http_get',
                                options=dict(
                                    path=dict(
                                        type='str',
                                        disposition='path'
                                    ),
                                    port=dict(
                                        type='integer',
                                        disposition='port',
                                        required=True
                                    ),
                                    scheme=dict(
                                        type='str',
                                        disposition='scheme',
                                        choices=['http',
                                                 'https']
                                    )
                                )
                            ),
                            initial_delay_seconds=dict(
                                type='integer',
                                disposition='initial_delay_seconds'
                            ),
                            period_seconds=dict(
                                type='integer',
                                disposition='period_seconds'
                            ),
                            failure_threshold=dict(
                                type='integer',
                                disposition='failure_threshold'
                            ),
                            success_threshold=dict(
                                type='integer',
                                disposition='success_threshold'
                            ),
                            timeout_seconds=dict(
                                type='integer',
                                disposition='timeout_seconds'
                            )
                        )
                    )
                )
            ),
            image_registry_credentials=dict(
                type='list',
                disposition='/image_registry_credentials',
                elements='dict',
                options=dict(
                    server=dict(
                        type='str',
                        disposition='server',
                        required=True
                    ),
                    username=dict(
                        type='str',
                        disposition='username',
                        required=True
                    ),
                    password=dict(
                        type='str',
                        disposition='password'
                    )
                )
            ),
            restart_policy=dict(
                type='str',
                disposition='/restart_policy',
                choices=['Always',
                         'OnFailure',
                         'Never']
            ),
            os_type=dict(
                type='str',
                disposition='/os_type',
                choices=['Windows',
                         'Linux']
            ),
            volumes=dict(
                type='list',
                disposition='/volumes',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    azure_file=dict(
                        type='dict',
                        disposition='azure_file',
                        options=dict(
                            share_name=dict(
                                type='str',
                                disposition='share_name',
                                required=True
                            ),
                            read_only=dict(
                                type='bool',
                                disposition='read_only'
                            ),
                            storage_account_name=dict(
                                type='str',
                                disposition='storage_account_name',
                                required=True
                            ),
                            storage_account_key=dict(
                                type='str',
                                disposition='storage_account_key'
                            )
                        )
                    ),
                    empty_dir=dict(
                        type='any',
                        disposition='empty_dir'
                    ),
                    secret=dict(
                        type='dictionary',
                        disposition='secret'
                    ),
                    git_repo=dict(
                        type='dict',
                        disposition='git_repo',
                        options=dict(
                            directory=dict(
                                type='str',
                                disposition='directory'
                            ),
                            repository=dict(
                                type='str',
                                disposition='repository',
                                required=True
                            ),
                            revision=dict(
                                type='str',
                                disposition='revision'
                            )
                        )
                    )
                )
            ),
            dns_config=dict(
                type='dict',
                disposition='/dns_config',
                options=dict(
                    name_servers=dict(
                        type='list',
                        disposition='name_servers',
                        required=True,
                        elements='str'
                    ),
                    search_domains=dict(
                        type='str',
                        disposition='search_domains'
                    ),
                    options=dict(
                        type='str',
                        disposition='options'
                    )
                )
            ),
            sku=dict(
                type='str',
                disposition='/sku',
                choices=['Standard',
                         'Dedicated']
            ),
            encryption_properties=dict(
                type='dict',
                disposition='/encryption_properties',
                options=dict(
                    vault_base_url=dict(
                        type='str',
                        disposition='vault_base_url',
                        required=True
                    ),
                    key_name=dict(
                        type='str',
                        disposition='key_name',
                        required=True
                    ),
                    key_version=dict(
                        type='str',
                        disposition='key_version',
                        required=True
                    )
                )
            ),
            init_containers=dict(
                type='list',
                disposition='/init_containers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    image=dict(
                        type='str',
                        disposition='image'
                    ),
                    command=dict(
                        type='list',
                        disposition='command',
                        elements='str'
                    ),
                    environment_variables=dict(
                        type='list',
                        disposition='environment_variables',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            value=dict(
                                type='str',
                                disposition='value'
                            ),
                            secure_value=dict(
                                type='str',
                                disposition='secure_value'
                            )
                        )
                    ),
                    instance_view=dict(
                        type='dict',
                        updatable=False,
                        disposition='instance_view',
                        options=dict(
                            restart_count=dict(
                                type='integer',
                                updatable=False,
                                disposition='restart_count'
                            ),
                            current_state=dict(
                                type='dict',
                                updatable=False,
                                disposition='current_state',
                                options=dict(
                                    state=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='state'
                                    ),
                                    start_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='start_time'
                                    ),
                                    exit_code=dict(
                                        type='integer',
                                        updatable=False,
                                        disposition='exit_code'
                                    ),
                                    finish_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='finish_time'
                                    ),
                                    detail_status=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='detail_status'
                                    )
                                )
                            ),
                            previous_state=dict(
                                type='dict',
                                updatable=False,
                                disposition='previous_state',
                                options=dict(
                                    state=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='state'
                                    ),
                                    start_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='start_time'
                                    ),
                                    exit_code=dict(
                                        type='integer',
                                        updatable=False,
                                        disposition='exit_code'
                                    ),
                                    finish_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='finish_time'
                                    ),
                                    detail_status=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='detail_status'
                                    )
                                )
                            ),
                            events=dict(
                                type='list',
                                updatable=False,
                                disposition='events',
                                elements='dict',
                                options=dict(
                                    count=dict(
                                        type='integer',
                                        updatable=False,
                                        disposition='count'
                                    ),
                                    first_timestamp=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='first_timestamp'
                                    ),
                                    last_timestamp=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='last_timestamp'
                                    ),
                                    name=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='name'
                                    ),
                                    message=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='message'
                                    ),
                                    type=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='type'
                                    )
                                )
                            )
                        )
                    ),
                    volume_mounts=dict(
                        type='list',
                        disposition='volume_mounts',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            mount_path=dict(
                                type='str',
                                disposition='mount_path',
                                required=True
                            ),
                            read_only=dict(
                                type='bool',
                                disposition='read_only'
                            )
                        )
                    )
                )
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            log_analytics=dict(
                type='dict',
                disposition='/log_analytics',
                options=dict(
                    workspace_id=dict(
                        type='str',
                        disposition='workspace_id',
                        required=True
                    ),
                    workspace_key=dict(
                        type='str',
                        disposition='workspace_key',
                        required=True
                    ),
                    log_type=dict(
                        type='str',
                        disposition='log_type',
                        choices=['ContainerInsights',
                                 'ContainerInstanceLogs']
                    ),
                    metadata=dict(
                        type='dictionary',
                        disposition='metadata'
                    )
                )
            ),
            ports=dict(
                type='list',
                disposition='/ports',
                elements='dict',
                options=dict(
                    protocol=dict(
                        type='str',
                        disposition='protocol',
                        choices=['TCP',
                                 'UDP']
                    ),
                    port=dict(
                        type='integer',
                        disposition='port',
                        required=True
                    )
                )
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['Public',
                         'Private']
            ),
            ip=dict(
                type='str',
                disposition='/ip'
            ),
            dns_name_label=dict(
                type='str',
                disposition='/dns_name_label'
            ),
            resource_identity_type=dict(
                type='sealed-choice',
                disposition='/resource_identity_type'
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
        self.container_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContainerGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ContainerInstanceManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

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
            response = self.mgmt_client.container_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                          container_group_name=self.container_group_name,
                                                                          container_group=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ContainerGroup instance.')
            self.fail('Error creating the ContainerGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.container_groups.delete(resource_group_name=self.resource_group_name,
                                                                container_group_name=self.container_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the ContainerGroup instance.')
            self.fail('Error deleting the ContainerGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.container_groups.get(resource_group_name=self.resource_group_name,
                                                             container_group_name=self.container_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContainerGroup()


if __name__ == '__main__':
    main()
