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
module: azure_rm_containergroup_info
version_added: '2.9'
short_description: Get ContainerGroup info.
description:
  - Get info of ContainerGroup.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  container_group_name:
    description:
      - The name of the container group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ContainerGroupsList
      azure_rm_containergroup_info: 
        {}
        

    - name: ContainerGroupsListByResourceGroup
      azure_rm_containergroup_info: 
        resource_group_name: demo
        

    - name: ContainerGroupsGet_Failed
      azure_rm_containergroup_info: 
        container_group_name: demo1
        resource_group_name: demo
        

    - name: ContainerGroupsGet_Succeeded
      azure_rm_containergroup_info: 
        container_group_name: demo1
        resource_group_name: demo
        

'''

RETURN = '''
container_groups:
  description: >-
    A list of dict results where the key is the name of the ContainerGroup and
    the values are the facts for that ContainerGroup.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of container groups.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - >-
              The provisioning state of the container group. This only appears
              in the response.
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
                - >-
                  The commands to execute within the container instance in exec
                  form.
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
                - >-
                  The instance view of the container instance. Only valid in
                  response.
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
                        - >-
                          The date-time when the container instance state
                          started.
                      returned: always
                      type: str
                      sample: null
                    exit_code:
                      description:
                        - >-
                          The container instance exit codes correspond to those
                          from the `docker run` command.
                      returned: always
                      type: integer
                      sample: null
                    finish_time:
                      description:
                        - >-
                          The date-time when the container instance state
                          finished.
                      returned: always
                      type: str
                      sample: null
                    detail_status:
                      description:
                        - >-
                          The human-readable status of the container instance
                          state.
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
                        - >-
                          The date-time when the container instance state
                          started.
                      returned: always
                      type: str
                      sample: null
                    exit_code:
                      description:
                        - >-
                          The container instance exit codes correspond to those
                          from the `docker run` command.
                      returned: always
                      type: integer
                      sample: null
                    finish_time:
                      description:
                        - >-
                          The date-time when the container instance state
                          finished.
                      returned: always
                      type: str
                      sample: null
                    detail_status:
                      description:
                        - >-
                          The human-readable status of the container instance
                          state.
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
                      The path within the container where the volume should be
                      mounted. Must not contain colon (:).
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
              The image registry credentials by which the container group is
              created from.
          returned: always
          type: list
          sample: null
          contains:
            server:
              description:
                - >-
                  The Docker image registry server without a protocol such as
                  "http" and "https".
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
              The operating system type required by the containers in the
              container group.
          returned: always
          type: str
          sample: null
        volumes:
          description:
            - >-
              The list of volumes that can be mounted by containers in this
              container group.
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
                    - >-
                      The name of the Azure File share to be mounted as a
                      volume.
                  returned: always
                  type: str
                  sample: null
                read_only:
                  description:
                    - >-
                      The flag indicating whether the Azure File shared mounted
                      as a volume is read-only.
                  returned: always
                  type: bool
                  sample: null
                storage_account_name:
                  description:
                    - >-
                      The name of the storage account that contains the Azure
                      File share.
                  returned: always
                  type: str
                  sample: null
                storage_account_key:
                  description:
                    - >-
                      The storage account access key used to access the Azure
                      File share.
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
                      Target directory name. Must not contain or start with
                      '..'.  If '.' is supplied, the volume directory will be
                      the git repository.  Otherwise, if specified, the volume
                      will contain the git repository in the subdirectory with
                      the given name.
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
                - >-
                  The DNS search domains for hostname lookup in the container
                  group.
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
                - >-
                  The instance view of the init container. Only valid in
                  response.
              returned: always
              type: dict
              sample: null
              contains:
                restart_count:
                  description:
                    - >-
                      The number of times that the init container has been
                      restarted.
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
                        - >-
                          The date-time when the container instance state
                          started.
                      returned: always
                      type: str
                      sample: null
                    exit_code:
                      description:
                        - >-
                          The container instance exit codes correspond to those
                          from the `docker run` command.
                      returned: always
                      type: integer
                      sample: null
                    finish_time:
                      description:
                        - >-
                          The date-time when the container instance state
                          finished.
                      returned: always
                      type: str
                      sample: null
                    detail_status:
                      description:
                        - >-
                          The human-readable status of the container instance
                          state.
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
                        - >-
                          The date-time when the container instance state
                          started.
                      returned: always
                      type: str
                      sample: null
                    exit_code:
                      description:
                        - >-
                          The container instance exit codes correspond to those
                          from the `docker run` command.
                      returned: always
                      type: integer
                      sample: null
                    finish_time:
                      description:
                        - >-
                          The date-time when the container instance state
                          finished.
                      returned: always
                      type: str
                      sample: null
                    detail_status:
                      description:
                        - >-
                          The human-readable status of the container instance
                          state.
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
                      The path within the container where the volume should be
                      mounted. Must not contain colon (:).
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
            - >-
              Specifies if the IP is exposed to the public internet or private
              VNET.
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
              The principal id of the container group identity. This property
              will only be provided for a system assigned identity.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              The tenant id associated with the container group. This property
              will only be provided for a system assigned identity.
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - >-
              The type of identity used for the container group. The type
              'SystemAssigned, UserAssigned' includes both an implicitly created
              identity and a set of user assigned identities. The type 'None'
              will remove any identities from the container group.
          returned: always
          type: sealed-choice
          sample: null
        user_assigned_identities:
          description:
            - >-
              The list of user identities associated with the container group.
              The user identity dictionary key references will be ARM resource
              ids in the form:
              '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - The URI to fetch the next page of container groups.
      returned: always
      type: str
      sample: null
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
          The provisioning state of the container group. This only appears in
          the response.
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
            - >-
              The commands to execute within the container instance in exec
              form.
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
            - >-
              The instance view of the container instance. Only valid in
              response.
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
                      The container instance exit codes correspond to those from
                      the `docker run` command.
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
                      The container instance exit codes correspond to those from
                      the `docker run` command.
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
                  The path within the container where the volume should be
                  mounted. Must not contain colon (:).
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
              The Docker image registry server without a protocol such as "http"
              and "https".
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
          The list of volumes that can be mounted by containers in this
          container group.
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
                  Target directory name. Must not contain or start with '..'. 
                  If '.' is supplied, the volume directory will be the git
                  repository.  Otherwise, if specified, the volume will contain
                  the git repository in the subdirectory with the given name.
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
                - >-
                  The number of times that the init container has been
                  restarted.
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
                      The container instance exit codes correspond to those from
                      the `docker run` command.
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
                      The container instance exit codes correspond to those from
                      the `docker run` command.
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
                  The path within the container where the volume should be
                  mounted. Must not contain colon (:).
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
          The principal id of the container group identity. This property will
          only be provided for a system assigned identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - >-
          The tenant id associated with the container group. This property will
          only be provided for a system assigned identity.
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
          The list of user identities associated with the container group. The
          user identity dictionary key references will be ARM resource ids in
          the form:
          '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
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
    from azure.mgmt.container import ContainerInstanceManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMContainerGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            container_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.container_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMContainerGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerInstanceManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group_name is not None and
            self.container_group_name is not None):
            self.results['container_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['container_groups'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['container_groups'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.container_groups.get(resource_group_name=self.resource_group_name,
                                                             container_group_name=self.container_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.container_groups.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.container_groups.list()
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
    AzureRMContainerGroupInfo()


if __name__ == '__main__':
    main()
