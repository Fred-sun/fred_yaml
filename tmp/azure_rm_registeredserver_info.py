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
module: azure_rm_registeredserver_info
version_added: '2.9'
short_description: Get RegisteredServer info.
description:
  - Get info of RegisteredServer.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  storage_sync_service_name:
    description:
      - Name of Storage Sync Service resource.
    required: true
    type: str
  server_id:
    description:
      - GUID identifying the on-premises server.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RegisteredServers_ListByStorageSyncService
      azure_rm_registeredserver_info: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        

    - name: RegisteredServers_Get
      azure_rm_registeredserver_info: 
        resource_group_name: SampleResourceGroup_1
        server_id: 080d4133-bdb5-40a0-96a0-71a6057bfe9a
        storage_sync_service_name: SampleStorageSyncService_1
        

'''

RETURN = '''
registered_servers:
  description: >-
    A list of dict results where the key is the name of the RegisteredServer and
    the values are the facts for that RegisteredServer.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Collection of Registered Server.
      returned: always
      type: list
      sample: null
      contains:
        server_certificate:
          description:
            - Registered Server Certificate
          returned: always
          type: str
          sample: null
        agent_version:
          description:
            - Registered Server Agent Version
          returned: always
          type: str
          sample: null
        server_os_version:
          description:
            - Registered Server OS Version
          returned: always
          type: str
          sample: null
        server_management_error_code:
          description:
            - Registered Server Management Error Code
          returned: always
          type: integer
          sample: null
        last_heart_beat:
          description:
            - Registered Server last heart beat
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Registered Server Provisioning State
          returned: always
          type: str
          sample: null
        server_role:
          description:
            - Registered Server serverRole
          returned: always
          type: str
          sample: null
        cluster_id:
          description:
            - Registered Server clusterId
          returned: always
          type: str
          sample: null
        cluster_name:
          description:
            - Registered Server clusterName
          returned: always
          type: str
          sample: null
        server_id:
          description:
            - Registered Server serverId
          returned: always
          type: str
          sample: null
        storage_sync_service_uid:
          description:
            - Registered Server storageSyncServiceUid
          returned: always
          type: str
          sample: null
        last_workflow_id:
          description:
            - Registered Server lastWorkflowId
          returned: always
          type: str
          sample: null
        last_operation_name:
          description:
            - Resource Last Operation Name
          returned: always
          type: str
          sample: null
        discovery_endpoint_uri:
          description:
            - Resource discoveryEndpointUri
          returned: always
          type: str
          sample: null
        resource_location:
          description:
            - Resource Location
          returned: always
          type: str
          sample: null
        service_location:
          description:
            - Service Location
          returned: always
          type: str
          sample: null
        friendly_name:
          description:
            - Friendly Name
          returned: always
          type: str
          sample: null
        management_endpoint_uri:
          description:
            - Management Endpoint Uri
          returned: always
          type: str
          sample: null
        monitoring_endpoint_uri:
          description:
            - Telemetry Endpoint Uri
          returned: always
          type: str
          sample: null
        monitoring_configuration:
          description:
            - Monitoring Configuration
          returned: always
          type: str
          sample: null
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    server_certificate:
      description:
        - Registered Server Certificate
      returned: always
      type: str
      sample: null
    agent_version:
      description:
        - Registered Server Agent Version
      returned: always
      type: str
      sample: null
    server_os_version:
      description:
        - Registered Server OS Version
      returned: always
      type: str
      sample: null
    server_management_error_code:
      description:
        - Registered Server Management Error Code
      returned: always
      type: integer
      sample: null
    last_heart_beat:
      description:
        - Registered Server last heart beat
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Registered Server Provisioning State
      returned: always
      type: str
      sample: null
    server_role:
      description:
        - Registered Server serverRole
      returned: always
      type: str
      sample: null
    cluster_id:
      description:
        - Registered Server clusterId
      returned: always
      type: str
      sample: null
    cluster_name:
      description:
        - Registered Server clusterName
      returned: always
      type: str
      sample: null
    server_id:
      description:
        - Registered Server serverId
      returned: always
      type: str
      sample: null
    storage_sync_service_uid:
      description:
        - Registered Server storageSyncServiceUid
      returned: always
      type: str
      sample: null
    last_workflow_id:
      description:
        - Registered Server lastWorkflowId
      returned: always
      type: str
      sample: null
    last_operation_name:
      description:
        - Resource Last Operation Name
      returned: always
      type: str
      sample: null
    discovery_endpoint_uri:
      description:
        - Resource discoveryEndpointUri
      returned: always
      type: str
      sample: null
    resource_location:
      description:
        - Resource Location
      returned: always
      type: str
      sample: null
    service_location:
      description:
        - Service Location
      returned: always
      type: str
      sample: null
    friendly_name:
      description:
        - Friendly Name
      returned: always
      type: str
      sample: null
    management_endpoint_uri:
      description:
        - Management Endpoint Uri
      returned: always
      type: str
      sample: null
    monitoring_endpoint_uri:
      description:
        - Telemetry Endpoint Uri
      returned: always
      type: str
      sample: null
    monitoring_configuration:
      description:
        - Monitoring Configuration
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
    from azure.mgmt.microsoft import Microsoft Storage Sync
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRegisteredServerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            storage_sync_service_name=dict(
                type='str',
                required=True
            ),
            server_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.server_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRegisteredServerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.storage_sync_service_name is not None and
            self.server_id is not None):
            self.results['registered_servers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.storage_sync_service_name is not None):
            self.results['registered_servers'] = self.format_item(self.listbystoragesyncservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.registered_servers.get(resource_group_name=self.resource_group_name,
                                                               storage_sync_service_name=self.storage_sync_service_name,
                                                               server_id=self.server_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbystoragesyncservice(self):
        response = None

        try:
            response = self.mgmt_client.registered_servers.list_by_storage_sync_service(resource_group_name=self.resource_group_name,
                                                                                        storage_sync_service_name=self.storage_sync_service_name)
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
    AzureRMRegisteredServerInfo()


if __name__ == '__main__':
    main()
