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
module: azure_rm_storagesyncservice_info
version_added: '2.9'
short_description: Get StorageSyncService info.
description:
  - Get info of StorageSyncService.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  storage_sync_service_name:
    description:
      - Name of Storage Sync Service resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageSyncServices_Get
      azure_rm_storagesyncservice_info: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        

    - name: StorageSyncServices_ListByResourceGroup
      azure_rm_storagesyncservice_info: 
        resource_group_name: SampleResourceGroup_1
        

    - name: StorageSyncServices_ListBySubscription
      azure_rm_storagesyncservice_info: 
        {}
        

'''

RETURN = '''
storage_sync_services:
  description: >-
    A list of dict results where the key is the name of the StorageSyncService
    and the values are the facts for that StorageSyncService.
  returned: always
  type: complex
  contains:
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
    incoming_traffic_policy:
      description:
        - Incoming Traffic Policy
      returned: always
      type: str
      sample: null
    storage_sync_service_status:
      description:
        - Storage Sync service status.
      returned: always
      type: integer
      sample: null
    storage_sync_service_uid:
      description:
        - Storage Sync service Uid
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - StorageSyncService Provisioning State
      returned: always
      type: str
      sample: null
    last_workflow_id:
      description:
        - StorageSyncService lastWorkflowId
      returned: always
      type: str
      sample: null
    last_operation_name:
      description:
        - Resource Last Operation Name
      returned: always
      type: str
      sample: null
    private_endpoint_connections:
      description:
        - >-
          List of private endpoint connection associated with the specified
          storage sync service
      returned: always
      type: list
      sample: null
      contains:
        private_endpoint:
          description:
            - The resource of private end point.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - The ARM identifier for Private Endpoint
              returned: always
              type: str
              sample: null
        private_link_service_connection_state:
          description:
            - >-
              A collection of information about the state of the connection
              between service consumer and provider.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  Indicates whether the connection has been
                  Approved/Rejected/Removed by the owner of the service.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The reason for approval/rejection of the connection.
              returned: always
              type: str
              sample: null
            actions_required:
              description:
                - >-
                  A message indicating if changes on the service provider
                  require any updates on the consumer.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the private endpoint connection
              resource.
          returned: always
          type: str
          sample: null
    value:
      description:
        - Collection of StorageSyncServices.
      returned: always
      type: list
      sample: null
      contains:
        incoming_traffic_policy:
          description:
            - Incoming Traffic Policy
          returned: always
          type: str
          sample: null
        storage_sync_service_status:
          description:
            - Storage Sync service status.
          returned: always
          type: integer
          sample: null
        storage_sync_service_uid:
          description:
            - Storage Sync service Uid
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - StorageSyncService Provisioning State
          returned: always
          type: str
          sample: null
        last_workflow_id:
          description:
            - StorageSyncService lastWorkflowId
          returned: always
          type: str
          sample: null
        last_operation_name:
          description:
            - Resource Last Operation Name
          returned: always
          type: str
          sample: null
        private_endpoint_connections:
          description:
            - >-
              List of private endpoint connection associated with the specified
              storage sync service
          returned: always
          type: list
          sample: null
          contains:
            private_endpoint:
              description:
                - The resource of private end point.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - The ARM identifier for Private Endpoint
                  returned: always
                  type: str
                  sample: null
            private_link_service_connection_state:
              description:
                - >-
                  A collection of information about the state of the connection
                  between service consumer and provider.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - >-
                      Indicates whether the connection has been
                      Approved/Rejected/Removed by the owner of the service.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - The reason for approval/rejection of the connection.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - >-
                      A message indicating if changes on the service provider
                      require any updates on the consumer.
                  returned: always
                  type: str
                  sample: null
            provisioning_state:
              description:
                - >-
                  The provisioning state of the private endpoint connection
                  resource.
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


class AzureRMStorageSyncServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            storage_sync_service_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None

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
        super(AzureRMStorageSyncServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.storage_sync_service_name is not None):
            self.results['storage_sync_services'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['storage_sync_services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['storage_sync_services'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.storage_sync_services.get(resource_group_name=self.resource_group_name,
                                                                  storage_sync_service_name=self.storage_sync_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.storage_sync_services.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.storage_sync_services.list_by_subscription()
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
    AzureRMStorageSyncServiceInfo()


if __name__ == '__main__':
    main()
