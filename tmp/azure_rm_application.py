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
module: azure_rm_application
version_added: '2.9'
short_description: Manage Azure Application instance.
description:
  - 'Create, update and delete instance of Azure Application.'
options:
  resource_group_name:
    description:
      - Azure resource group name
    required: true
    type: str
  application_resource_name:
    description:
      - The identity of the application.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  description:
    description:
      - User readable description of the application.
    type: str
  services:
    description:
      - >-
        Describes the services in the application. This property is used to
        create or modify services of the application. On get only the name of
        the service is returned. The service description can be obtained by
        querying for the service resource.
    type: list
    suboptions:
      provisioning_state:
        description:
          - State of the resource.
        type: str
      os_type:
        description:
          - The operation system required by the code in service.
        required: true
        type: str
        choices:
          - Linux
          - Windows
      code_packages:
        description:
          - >-
            Describes the set of code packages that forms the service. A code
            package describes the container and the properties for running it.
            All the code packages are started together on the same host and
            share the same context (network, process etc.).
        required: true
        type: list
        suboptions:
          name:
            description:
              - The name of the code package.
            required: true
            type: str
          image:
            description:
              - The Container image to use.
            required: true
            type: str
          image_registry_credential:
            description:
              - Image registry credential.
            type: dict
            suboptions:
              server:
                description:
                  - >-
                    Docker image registry server, without protocol such as
                    `http` and `https`.
                required: true
                type: str
              username:
                description:
                  - The username for the private registry.
                required: true
                type: str
              password:
                description:
                  - >-
                    The password for the private registry. The password is
                    required for create or update operations, however it is not
                    returned in the get or list operations.
                type: str
          entrypoint:
            description:
              - Override for the default entry point in the container.
            type: str
          commands:
            description:
              - Command array to execute within the container in exec form.
            type: list
          environment_variables:
            description:
              - The environment variables to set in this container
            type: list
            suboptions:
              name:
                description:
                  - The name of the environment variable.
                type: str
              value:
                description:
                  - The value of the environment variable.
                type: str
          settings:
            description:
              - >-
                The settings to set in this container. The setting file path can
                be fetched from environment variable "Fabric_SettingPath". The
                path for Windows container is "C:\\secrets". The path for Linux
                container is "/var/secrets".
            type: list
            suboptions:
              name:
                description:
                  - The name of the setting.
                type: str
              value:
                description:
                  - The value of the setting.
                type: str
          labels:
            description:
              - The labels to set in this container.
            type: list
            suboptions:
              name:
                description:
                  - The name of the container label.
                required: true
                type: str
              value:
                description:
                  - The value of the container label.
                required: true
                type: str
          endpoints:
            description:
              - The endpoints exposed by this container.
            type: list
            suboptions:
              name:
                description:
                  - The name of the endpoint.
                required: true
                type: str
              port:
                description:
                  - Port used by the container.
                type: integer
          resources:
            description:
              - The resources required by this container.
            required: true
            type: dict
            suboptions:
              requests:
                description:
                  - Describes the requested resources for a given container.
                required: true
                type: dict
                suboptions:
                  memory_in_gb:
                    description:
                      - The memory request in GB for this container.
                    required: true
                    type: number
                  cpu:
                    description:
                      - >-
                        Requested number of CPU cores. At present, only full
                        cores are supported.
                    required: true
                    type: number
              limits:
                description:
                  - >-
                    Describes the maximum limits on the resources for a given
                    container.
                type: dict
                suboptions:
                  memory_in_gb:
                    description:
                      - The memory limit in GB.
                    type: number
                  cpu:
                    description:
                      - >-
                        CPU limits in cores. At present, only full cores are
                        supported.
                    type: number
          volume_refs:
            description:
              - >-
                Volumes to be attached to the container. The lifetime of these
                volumes is independent of the application's lifetime.
            type: list
            suboptions:
              name:
                description:
                  - Name of the volume being referenced.
                required: true
                type: str
              read_only:
                description:
                  - >-
                    The flag indicating whether the volume is read only. Default
                    is 'false'.
                type: bool
              destination_path:
                description:
                  - >-
                    The path within the container at which the volume should be
                    mounted. Only valid path characters are allowed.
                required: true
                type: str
          volumes:
            description:
              - >-
                Volumes to be attached to the container. The lifetime of these
                volumes is scoped to the application's lifetime.
            type: list
            suboptions:
              creation_parameters:
                description:
                  - >-
                    Describes parameters for creating application-scoped
                    volumes.
                required: true
                type: dict
                suboptions:
                  kind:
                    description:
                      - Specifies the application-scoped volume kind.
                    required: true
                    type: str
                    choices:
                      - ServiceFabricVolumeDisk
                  description:
                    description:
                      - User readable description of the volume.
                    type: str
          diagnostics:
            description:
              - Reference to sinks in DiagnosticsDescription.
            type: dict
            suboptions:
              enabled:
                description:
                  - Status of whether or not sinks are enabled.
                type: bool
              sink_refs:
                description:
                  - >-
                    List of sinks to be used if enabled. References the list of
                    sinks in DiagnosticsDescription.
                type: list
          reliable_collections_refs:
            description:
              - >-
                A list of ReliableCollection resources used by this particular
                code package. Please refer to ReliableCollectionsRef for more
                details.
            type: list
            suboptions:
              name:
                description:
                  - >-
                    Name of ReliableCollection resource. Right now it's not used
                    and you can use any string.
                required: true
                type: str
              do_not_persist_state:
                description:
                  - >-
                    False (the default) if ReliableCollections state is
                    persisted to disk as usual. True if you do not want to
                    persist state, in which case replication is still enabled
                    and you can use ReliableCollections as distributed cache.
                type: bool
          instance_view:
            description:
              - Runtime information of a container instance.
            type: dict
            suboptions:
              restart_count:
                description:
                  - The number of times the container has been restarted.
                type: integer
              current_state:
                description:
                  - Current container instance state.
                type: dict
                suboptions:
                  state:
                    description:
                      - The state of this container
                    type: str
                  start_time:
                    description:
                      - Date/time when the container state started.
                    type: str
                  exit_code:
                    description:
                      - The container exit code.
                    type: str
                  finish_time:
                    description:
                      - Date/time when the container state finished.
                    type: str
                  detail_status:
                    description:
                      - Human-readable status of this state.
                    type: str
              previous_state:
                description:
                  - Previous container instance state.
                type: dict
                suboptions:
                  state:
                    description:
                      - The state of this container
                    type: str
                  start_time:
                    description:
                      - Date/time when the container state started.
                    type: str
                  exit_code:
                    description:
                      - The container exit code.
                    type: str
                  finish_time:
                    description:
                      - Date/time when the container state finished.
                    type: str
                  detail_status:
                    description:
                      - Human-readable status of this state.
                    type: str
              events:
                description:
                  - The events of this container instance.
                type: list
                suboptions:
                  name:
                    description:
                      - The name of the container event.
                    type: str
                  count:
                    description:
                      - The count of the event.
                    type: integer
                  first_timestamp:
                    description:
                      - Date/time of the first event.
                    type: str
                  last_timestamp:
                    description:
                      - Date/time of the last event.
                    type: str
                  message:
                    description:
                      - The event message
                    type: str
                  type:
                    description:
                      - The event type.
                    type: str
      network_refs:
        description:
          - >-
            The names of the private networks that this service needs to be part
            of.
        type: list
        suboptions:
          name:
            description:
              - Name of the network
            type: str
          endpoint_refs:
            description:
              - A list of endpoints that are exposed on this network.
            type: list
            suboptions:
              name:
                description:
                  - Name of the endpoint.
                type: str
      diagnostics:
        description:
          - Reference to sinks in DiagnosticsDescription.
        type: dict
        suboptions:
          enabled:
            description:
              - Status of whether or not sinks are enabled.
            type: bool
          sink_refs:
            description:
              - >-
                List of sinks to be used if enabled. References the list of
                sinks in DiagnosticsDescription.
            type: list
      description:
        description:
          - User readable description of the service.
        type: str
      replica_count:
        description:
          - >-
            The number of replicas of the service to create. Defaults to 1 if
            not specified.
        type: integer
      auto_scaling_policies:
        description:
          - Auto scaling policies
        type: list
        suboptions:
          name:
            description:
              - The name of the auto scaling policy.
            required: true
            type: str
          trigger:
            description:
              - Determines when auto scaling operation will be invoked.
            required: true
            type: dict
            suboptions:
              kind:
                description:
                  - The type of auto scaling trigger
                required: true
                type: str
                choices:
                  - AverageLoad
          mechanism:
            description:
              - >-
                The mechanism that is used to scale when auto scaling operation
                is invoked.
            required: true
            type: dict
            suboptions:
              kind:
                description:
                  - The type of auto scaling mechanism.
                required: true
                type: str
                choices:
                  - AddRemoveReplica
      status:
        description:
          - Status of the service.
        type: str
        choices:
          - Unknown
          - Ready
          - Upgrading
          - Creating
          - Deleting
          - Failed
      status_details:
        description:
          - >-
            Gives additional information about the current status of the
            service.
        type: str
      health_state:
        description:
          - Describes the health state of an application resource.
        type: str
        choices:
          - Invalid
          - Ok
          - Warning
          - Error
          - Unknown
      unhealthy_evaluation:
        description:
          - >-
            When the service's health state is not 'Ok', this additional details
            from service fabric Health Manager for the user to know why the
            service is marked unhealthy.
        type: str
  diagnostics:
    description:
      - >-
        Describes the diagnostics definition and usage for an application
        resource.
    type: dict
    suboptions:
      sinks:
        description:
          - List of supported sinks that can be referenced.
        type: list
        suboptions:
          kind:
            description:
              - The kind of DiagnosticsSink.
            required: true
            type: str
            choices:
              - Invalid
              - AzureInternalMonitoringPipeline
          name:
            description:
              - >-
                Name of the sink. This value is referenced by
                DiagnosticsReferenceDescription
            type: str
          description:
            description:
              - A description of the sink.
            type: str
      enabled:
        description:
          - Status of whether or not sinks are enabled.
        type: bool
      default_sink_refs:
        description:
          - >-
            The sinks to be used if diagnostics is enabled. Sink choices can be
            overridden at the service and code package level.
        type: list
  debug_params:
    description:
      - >-
        Internal - used by Visual Studio to setup the debugging session on the
        local development environment.
    type: str
  state:
    description:
      - Assert the state of the Application.
      - >-
        Use C(present) to create or update an Application and C(absent) to
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
    - name: CreateOrUpdateApplication
      azure_rm_application: 
        application_resource_name: sampleApplication
        resource_group_name: sbz_demo
        

    - name: DeleteApplication
      azure_rm_application: 
        application_resource_name: sampleApplication
        resource_group_name: sbz_demo
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - State of the resource.
  returned: always
  type: str
  sample: null
description:
  description:
    - User readable description of the application.
  returned: always
  type: str
  sample: null
services:
  description:
    - >-
      Describes the services in the application. This property is used to create
      or modify services of the application. On get only the name of the service
      is returned. The service description can be obtained by querying for the
      service resource.
  returned: always
  type: list
  sample: null
  contains:
    provisioning_state:
      description:
        - State of the resource.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - The operation system required by the code in service.
      returned: always
      type: str
      sample: null
    code_packages:
      description:
        - >-
          Describes the set of code packages that forms the service. A code
          package describes the container and the properties for running it. All
          the code packages are started together on the same host and share the
          same context (network, process etc.).
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the code package.
          returned: always
          type: str
          sample: null
        image:
          description:
            - The Container image to use.
          returned: always
          type: str
          sample: null
        image_registry_credential:
          description:
            - Image registry credential.
          returned: always
          type: dict
          sample: null
          contains:
            server:
              description:
                - >-
                  Docker image registry server, without protocol such as `http`
                  and `https`.
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
                - >-
                  The password for the private registry. The password is
                  required for create or update operations, however it is not
                  returned in the get or list operations.
              returned: always
              type: str
              sample: null
        entrypoint:
          description:
            - Override for the default entry point in the container.
          returned: always
          type: str
          sample: null
        commands:
          description:
            - Command array to execute within the container in exec form.
          returned: always
          type: list
          sample: null
        environment_variables:
          description:
            - The environment variables to set in this container
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
        settings:
          description:
            - >-
              The settings to set in this container. The setting file path can
              be fetched from environment variable "Fabric_SettingPath". The
              path for Windows container is "C:\\secrets". The path for Linux
              container is "/var/secrets".
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The name of the setting.
              returned: always
              type: str
              sample: null
            value:
              description:
                - The value of the setting.
              returned: always
              type: str
              sample: null
        labels:
          description:
            - The labels to set in this container.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The name of the container label.
              returned: always
              type: str
              sample: null
            value:
              description:
                - The value of the container label.
              returned: always
              type: str
              sample: null
        endpoints:
          description:
            - The endpoints exposed by this container.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The name of the endpoint.
              returned: always
              type: str
              sample: null
            port:
              description:
                - Port used by the container.
              returned: always
              type: integer
              sample: null
        resources:
          description:
            - The resources required by this container.
          returned: always
          type: dict
          sample: null
          contains:
            requests:
              description:
                - Describes the requested resources for a given container.
              returned: always
              type: dict
              sample: null
              contains:
                memory_in_gb:
                  description:
                    - The memory request in GB for this container.
                  returned: always
                  type: number
                  sample: null
                cpu:
                  description:
                    - >-
                      Requested number of CPU cores. At present, only full cores
                      are supported.
                  returned: always
                  type: number
                  sample: null
            limits:
              description:
                - >-
                  Describes the maximum limits on the resources for a given
                  container.
              returned: always
              type: dict
              sample: null
              contains:
                memory_in_gb:
                  description:
                    - The memory limit in GB.
                  returned: always
                  type: number
                  sample: null
                cpu:
                  description:
                    - >-
                      CPU limits in cores. At present, only full cores are
                      supported.
                  returned: always
                  type: number
                  sample: null
        volume_refs:
          description:
            - >-
              Volumes to be attached to the container. The lifetime of these
              volumes is independent of the application's lifetime.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the volume being referenced.
              returned: always
              type: str
              sample: null
            read_only:
              description:
                - >-
                  The flag indicating whether the volume is read only. Default
                  is 'false'.
              returned: always
              type: bool
              sample: null
            destination_path:
              description:
                - >-
                  The path within the container at which the volume should be
                  mounted. Only valid path characters are allowed.
              returned: always
              type: str
              sample: null
        volumes:
          description:
            - >-
              Volumes to be attached to the container. The lifetime of these
              volumes is scoped to the application's lifetime.
          returned: always
          type: list
          sample: null
          contains:
            creation_parameters:
              description:
                - Describes parameters for creating application-scoped volumes.
              returned: always
              type: dict
              sample: null
              contains:
                kind:
                  description:
                    - Specifies the application-scoped volume kind.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - User readable description of the volume.
                  returned: always
                  type: str
                  sample: null
        diagnostics:
          description:
            - Reference to sinks in DiagnosticsDescription.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - Status of whether or not sinks are enabled.
              returned: always
              type: bool
              sample: null
            sink_refs:
              description:
                - >-
                  List of sinks to be used if enabled. References the list of
                  sinks in DiagnosticsDescription.
              returned: always
              type: list
              sample: null
        reliable_collections_refs:
          description:
            - >-
              A list of ReliableCollection resources used by this particular
              code package. Please refer to ReliableCollectionsRef for more
              details.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  Name of ReliableCollection resource. Right now it's not used
                  and you can use any string.
              returned: always
              type: str
              sample: null
            do_not_persist_state:
              description:
                - >-
                  False (the default) if ReliableCollections state is persisted
                  to disk as usual. True if you do not want to persist state, in
                  which case replication is still enabled and you can use
                  ReliableCollections as distributed cache.
              returned: always
              type: bool
              sample: null
        instance_view:
          description:
            - Runtime information of a container instance.
          returned: always
          type: dict
          sample: null
          contains:
            restart_count:
              description:
                - The number of times the container has been restarted.
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
                    - The state of this container
                  returned: always
                  type: str
                  sample: null
                start_time:
                  description:
                    - Date/time when the container state started.
                  returned: always
                  type: str
                  sample: null
                exit_code:
                  description:
                    - The container exit code.
                  returned: always
                  type: str
                  sample: null
                finish_time:
                  description:
                    - Date/time when the container state finished.
                  returned: always
                  type: str
                  sample: null
                detail_status:
                  description:
                    - Human-readable status of this state.
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
                    - The state of this container
                  returned: always
                  type: str
                  sample: null
                start_time:
                  description:
                    - Date/time when the container state started.
                  returned: always
                  type: str
                  sample: null
                exit_code:
                  description:
                    - The container exit code.
                  returned: always
                  type: str
                  sample: null
                finish_time:
                  description:
                    - Date/time when the container state finished.
                  returned: always
                  type: str
                  sample: null
                detail_status:
                  description:
                    - Human-readable status of this state.
                  returned: always
                  type: str
                  sample: null
            events:
              description:
                - The events of this container instance.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - The name of the container event.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - The count of the event.
                  returned: always
                  type: integer
                  sample: null
                first_timestamp:
                  description:
                    - Date/time of the first event.
                  returned: always
                  type: str
                  sample: null
                last_timestamp:
                  description:
                    - Date/time of the last event.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - The event message
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - The event type.
                  returned: always
                  type: str
                  sample: null
    network_refs:
      description:
        - >-
          The names of the private networks that this service needs to be part
          of.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the network
          returned: always
          type: str
          sample: null
        endpoint_refs:
          description:
            - A list of endpoints that are exposed on this network.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the endpoint.
              returned: always
              type: str
              sample: null
    diagnostics:
      description:
        - Reference to sinks in DiagnosticsDescription.
      returned: always
      type: dict
      sample: null
      contains:
        enabled:
          description:
            - Status of whether or not sinks are enabled.
          returned: always
          type: bool
          sample: null
        sink_refs:
          description:
            - >-
              List of sinks to be used if enabled. References the list of sinks
              in DiagnosticsDescription.
          returned: always
          type: list
          sample: null
    description:
      description:
        - User readable description of the service.
      returned: always
      type: str
      sample: null
    replica_count:
      description:
        - >-
          The number of replicas of the service to create. Defaults to 1 if not
          specified.
      returned: always
      type: integer
      sample: null
    auto_scaling_policies:
      description:
        - Auto scaling policies
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the auto scaling policy.
          returned: always
          type: str
          sample: null
        trigger:
          description:
            - Determines when auto scaling operation will be invoked.
          returned: always
          type: dict
          sample: null
          contains:
            kind:
              description:
                - The type of auto scaling trigger
              returned: always
              type: str
              sample: null
        mechanism:
          description:
            - >-
              The mechanism that is used to scale when auto scaling operation is
              invoked.
          returned: always
          type: dict
          sample: null
          contains:
            kind:
              description:
                - The type of auto scaling mechanism.
              returned: always
              type: str
              sample: null
    status:
      description:
        - Status of the service.
      returned: always
      type: str
      sample: null
    status_details:
      description:
        - Gives additional information about the current status of the service.
      returned: always
      type: str
      sample: null
    health_state:
      description:
        - Describes the health state of an application resource.
      returned: always
      type: str
      sample: null
    unhealthy_evaluation:
      description:
        - >-
          When the service's health state is not 'Ok', this additional details
          from service fabric Health Manager for the user to know why the
          service is marked unhealthy.
      returned: always
      type: str
      sample: null
diagnostics:
  description:
    - >-
      Describes the diagnostics definition and usage for an application
      resource.
  returned: always
  type: dict
  sample: null
  contains:
    sinks:
      description:
        - List of supported sinks that can be referenced.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - The kind of DiagnosticsSink.
          returned: always
          type: str
          sample: null
        name:
          description:
            - >-
              Name of the sink. This value is referenced by
              DiagnosticsReferenceDescription
          returned: always
          type: str
          sample: null
        description:
          description:
            - A description of the sink.
          returned: always
          type: str
          sample: null
    enabled:
      description:
        - Status of whether or not sinks are enabled.
      returned: always
      type: bool
      sample: null
    default_sink_refs:
      description:
        - >-
          The sinks to be used if diagnostics is enabled. Sink choices can be
          overridden at the service and code package level.
      returned: always
      type: list
      sample: null
debug_params:
  description:
    - >-
      Internal - used by Visual Studio to setup the debugging session on the
      local development environment.
  returned: always
  type: str
  sample: null
service_names:
  description:
    - Names of the services in the application.
  returned: always
  type: list
  sample: null
status:
  description:
    - Status of the application.
  returned: always
  type: str
  sample: null
status_details:
  description:
    - Gives additional information about the current status of the application.
  returned: always
  type: str
  sample: null
health_state:
  description:
    - Describes the health state of an application resource.
  returned: always
  type: str
  sample: null
unhealthy_evaluation:
  description:
    - >-
      When the application's health state is not 'Ok', this additional details
      from service fabric Health Manager for the user to know why the
      application is marked unhealthy.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApplication(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            application_resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            services=dict(
                type='list',
                disposition='/services',
                elements='dict',
                options=dict(
                    provisioning_state=dict(
                        type='str',
                        updatable=False,
                        disposition='provisioning_state'
                    ),
                    os_type=dict(
                        type='str',
                        disposition='os_type',
                        choices=['Linux',
                                 'Windows'],
                        required=True
                    ),
                    code_packages=dict(
                        type='list',
                        disposition='code_packages',
                        required=True,
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
                            image_registry_credential=dict(
                                type='dict',
                                disposition='image_registry_credential',
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
                            entrypoint=dict(
                                type='str',
                                disposition='entrypoint'
                            ),
                            commands=dict(
                                type='list',
                                disposition='commands',
                                elements='str'
                            ),
                            environment_variables=dict(
                                type='list',
                                disposition='environment_variables',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value'
                                    )
                                )
                            ),
                            settings=dict(
                                type='list',
                                disposition='settings',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value'
                                    )
                                )
                            ),
                            labels=dict(
                                type='list',
                                disposition='labels',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value',
                                        required=True
                                    )
                                )
                            ),
                            endpoints=dict(
                                type='list',
                                disposition='endpoints',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    port=dict(
                                        type='integer',
                                        disposition='port'
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
                                            )
                                        )
                                    )
                                )
                            ),
                            volume_refs=dict(
                                type='list',
                                disposition='volume_refs',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    read_only=dict(
                                        type='bool',
                                        disposition='read_only'
                                    ),
                                    destination_path=dict(
                                        type='str',
                                        disposition='destination_path',
                                        required=True
                                    )
                                )
                            ),
                            volumes=dict(
                                type='list',
                                disposition='volumes',
                                elements='dict',
                                options=dict(
                                    creation_parameters=dict(
                                        type='dict',
                                        disposition='creation_parameters',
                                        required=True,
                                        options=dict(
                                            kind=dict(
                                                type='str',
                                                disposition='kind',
                                                choices=['ServiceFabricVolumeDisk'],
                                                required=True
                                            ),
                                            description=dict(
                                                type='str',
                                                disposition='description'
                                            )
                                        )
                                    )
                                )
                            ),
                            diagnostics=dict(
                                type='dict',
                                disposition='diagnostics',
                                options=dict(
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    ),
                                    sink_refs=dict(
                                        type='list',
                                        disposition='sink_refs',
                                        elements='str'
                                    )
                                )
                            ),
                            reliable_collections_refs=dict(
                                type='list',
                                disposition='reliable_collections_refs',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    do_not_persist_state=dict(
                                        type='bool',
                                        disposition='do_not_persist_state'
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
                                        disposition='restart_count'
                                    ),
                                    current_state=dict(
                                        type='dict',
                                        disposition='current_state',
                                        options=dict(
                                            state=dict(
                                                type='str',
                                                disposition='state'
                                            ),
                                            start_time=dict(
                                                type='str',
                                                disposition='start_time'
                                            ),
                                            exit_code=dict(
                                                type='str',
                                                disposition='exit_code'
                                            ),
                                            finish_time=dict(
                                                type='str',
                                                disposition='finish_time'
                                            ),
                                            detail_status=dict(
                                                type='str',
                                                disposition='detail_status'
                                            )
                                        )
                                    ),
                                    previous_state=dict(
                                        type='dict',
                                        disposition='previous_state',
                                        options=dict(
                                            state=dict(
                                                type='str',
                                                disposition='state'
                                            ),
                                            start_time=dict(
                                                type='str',
                                                disposition='start_time'
                                            ),
                                            exit_code=dict(
                                                type='str',
                                                disposition='exit_code'
                                            ),
                                            finish_time=dict(
                                                type='str',
                                                disposition='finish_time'
                                            ),
                                            detail_status=dict(
                                                type='str',
                                                disposition='detail_status'
                                            )
                                        )
                                    ),
                                    events=dict(
                                        type='list',
                                        disposition='events',
                                        elements='dict',
                                        options=dict(
                                            name=dict(
                                                type='str',
                                                disposition='name'
                                            ),
                                            count=dict(
                                                type='integer',
                                                disposition='count'
                                            ),
                                            first_timestamp=dict(
                                                type='str',
                                                disposition='first_timestamp'
                                            ),
                                            last_timestamp=dict(
                                                type='str',
                                                disposition='last_timestamp'
                                            ),
                                            message=dict(
                                                type='str',
                                                disposition='message'
                                            ),
                                            type=dict(
                                                type='str',
                                                disposition='type'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    network_refs=dict(
                        type='list',
                        disposition='network_refs',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            endpoint_refs=dict(
                                type='list',
                                disposition='endpoint_refs',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    )
                                )
                            )
                        )
                    ),
                    diagnostics=dict(
                        type='dict',
                        disposition='diagnostics',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled'
                            ),
                            sink_refs=dict(
                                type='list',
                                disposition='sink_refs',
                                elements='str'
                            )
                        )
                    ),
                    description=dict(
                        type='str',
                        disposition='description'
                    ),
                    replica_count=dict(
                        type='integer',
                        disposition='replica_count'
                    ),
                    auto_scaling_policies=dict(
                        type='list',
                        disposition='auto_scaling_policies',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            trigger=dict(
                                type='dict',
                                disposition='trigger',
                                required=True,
                                options=dict(
                                    kind=dict(
                                        type='str',
                                        disposition='kind',
                                        choices=['AverageLoad'],
                                        required=True
                                    )
                                )
                            ),
                            mechanism=dict(
                                type='dict',
                                disposition='mechanism',
                                required=True,
                                options=dict(
                                    kind=dict(
                                        type='str',
                                        disposition='kind',
                                        choices=['AddRemoveReplica'],
                                        required=True
                                    )
                                )
                            )
                        )
                    ),
                    status=dict(
                        type='str',
                        updatable=False,
                        disposition='status',
                        choices=['Unknown',
                                 'Ready',
                                 'Upgrading',
                                 'Creating',
                                 'Deleting',
                                 'Failed']
                    ),
                    status_details=dict(
                        type='str',
                        updatable=False,
                        disposition='status_details'
                    ),
                    health_state=dict(
                        type='str',
                        updatable=False,
                        disposition='health_state',
                        choices=['Invalid',
                                 'Ok',
                                 'Warning',
                                 'Error',
                                 'Unknown']
                    ),
                    unhealthy_evaluation=dict(
                        type='str',
                        updatable=False,
                        disposition='unhealthy_evaluation'
                    )
                )
            ),
            diagnostics=dict(
                type='dict',
                disposition='/diagnostics',
                options=dict(
                    sinks=dict(
                        type='list',
                        disposition='sinks',
                        elements='dict',
                        options=dict(
                            kind=dict(
                                type='str',
                                disposition='kind',
                                choices=['Invalid',
                                         'AzureInternalMonitoringPipeline'],
                                required=True
                            ),
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            description=dict(
                                type='str',
                                disposition='description'
                            )
                        )
                    ),
                    enabled=dict(
                        type='bool',
                        disposition='enabled'
                    ),
                    default_sink_refs=dict(
                        type='list',
                        disposition='default_sink_refs',
                        elements='str'
                    )
                )
            ),
            debug_params=dict(
                type='str',
                disposition='/debug_params'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.application_resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplication, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

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
                response = self.mgmt_client.application.create(resource_group_name=self.resource_group_name,
                                                               application_resource_name=self.application_resource_name,
                                                               application_resource_description=self.body)
            else:
                response = self.mgmt_client.application.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Application instance.')
            self.fail('Error creating the Application instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.application.delete(resource_group_name=self.resource_group_name,
                                                           application_resource_name=self.application_resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Application instance.')
            self.fail('Error deleting the Application instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.application.get(resource_group_name=self.resource_group_name,
                                                        application_resource_name=self.application_resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApplication()


if __name__ == '__main__':
    main()
