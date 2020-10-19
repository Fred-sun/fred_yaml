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
module: azure_rm_servicereplica_info
version_added: '2.9'
short_description: Get ServiceReplica info.
description:
  - Get info of ServiceReplica.
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
  service_resource_name:
    description:
      - The identity of the service.
    required: true
    type: str
  replica_name:
    description:
      - Service Fabric replica name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ReplicaGet
      azure_rm_servicereplica_info: 
        application_resource_name: helloWorldApp
        replica_name: '0'
        resource_group_name: sbz_demo
        service_resource_name: helloWorldService
        

    - name: ReplicasGetAll
      azure_rm_servicereplica_info: 
        application_resource_name: sampleApplication
        resource_group_name: sbz_demo
        service_resource_name: helloWorldService
        

'''

RETURN = '''
service_replica:
  description: >-
    A list of dict results where the key is the name of the ServiceReplica and
    the values are the facts for that ServiceReplica.
  returned: always
  type: complex
  contains:
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
    replica_name:
      description:
        - Name of the replica.
      returned: always
      type: str
      sample: null
    value:
      description:
        - One page of the list.
      returned: always
      type: list
      sample: null
      contains:
        replica_name:
          description:
            - Name of the replica.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URI to fetch the next page of the list.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMServiceReplicaInfo(AzureRMModuleBase):
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
            service_resource_name=dict(
                type='str',
                required=True
            ),
            replica_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.application_resource_name = None
        self.service_resource_name = None
        self.replica_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMServiceReplicaInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.application_resource_name is not None and
            self.service_resource_name is not None and
            self.replica_name is not None):
            self.results['service_replica'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.application_resource_name is not None and
              self.service_resource_name is not None):
            self.results['service_replica'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.service_replica.get(resource_group_name=self.resource_group_name,
                                                            application_resource_name=self.application_resource_name,
                                                            service_resource_name=self.service_resource_name,
                                                            replica_name=self.replica_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.service_replica.list(resource_group_name=self.resource_group_name,
                                                             application_resource_name=self.application_resource_name,
                                                             service_resource_name=self.service_resource_name)
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
    AzureRMServiceReplicaInfo()


if __name__ == '__main__':
    main()
