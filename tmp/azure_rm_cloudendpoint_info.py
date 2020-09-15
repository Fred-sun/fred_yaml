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
module: azure_rm_cloudendpoint_info
version_added: '2.9'
short_description: Get CloudEndpoint info.
description:
  - Get info of CloudEndpoint.
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
  sync_group_name:
    description:
      - Name of Sync Group resource.
    required: true
    type: str
  cloud_endpoint_name:
    description:
      - Name of Cloud Endpoint object.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CloudEndpoints_Get
      azure_rm_cloudendpoint_info: 
        cloud_endpoint_name: SampleCloudEndpoint_1
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        

    - name: CloudEndpoints_ListBySyncGroup
      azure_rm_cloudendpoint_info: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        

'''

RETURN = '''
cloud_endpoints:
  description: >-
    A list of dict results where the key is the name of the CloudEndpoint and
    the values are the facts for that CloudEndpoint.
  returned: always
  type: complex
  contains:
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
    storage_account_resource_id:
      description:
        - Storage Account Resource Id
      returned: always
      type: str
      sample: null
    azure_file_share_name:
      description:
        - Azure file share name
      returned: always
      type: str
      sample: null
    storage_account_tenant_id:
      description:
        - Storage Account Tenant Id
      returned: always
      type: str
      sample: null
    partnership_id:
      description:
        - Partnership Id
      returned: always
      type: str
      sample: null
    friendly_name:
      description:
        - Friendly Name
      returned: always
      type: str
      sample: null
    backup_enabled:
      description:
        - Backup Enabled
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - CloudEndpoint Provisioning State
      returned: always
      type: str
      sample: null
    last_workflow_id:
      description:
        - CloudEndpoint lastWorkflowId
      returned: always
      type: str
      sample: null
    last_operation_name:
      description:
        - Resource Last Operation Name
      returned: always
      type: str
      sample: null
    value:
      description:
        - Collection of CloudEndpoint.
      returned: always
      type: list
      sample: null
      contains:
        storage_account_resource_id:
          description:
            - Storage Account Resource Id
          returned: always
          type: str
          sample: null
        azure_file_share_name:
          description:
            - Azure file share name
          returned: always
          type: str
          sample: null
        storage_account_tenant_id:
          description:
            - Storage Account Tenant Id
          returned: always
          type: str
          sample: null
        partnership_id:
          description:
            - Partnership Id
          returned: always
          type: str
          sample: null
        friendly_name:
          description:
            - Friendly Name
          returned: always
          type: str
          sample: null
        backup_enabled:
          description:
            - Backup Enabled
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - CloudEndpoint Provisioning State
          returned: always
          type: str
          sample: null
        last_workflow_id:
          description:
            - CloudEndpoint lastWorkflowId
          returned: always
          type: str
          sample: null
        last_operation_name:
          description:
            - Resource Last Operation Name
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


class AzureRMCloudEndpointInfo(AzureRMModuleBase):
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
            sync_group_name=dict(
                type='str',
                required=True
            ),
            cloud_endpoint_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.sync_group_name = None
        self.cloud_endpoint_name = None

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
        super(AzureRMCloudEndpointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.storage_sync_service_name is not None and
            self.sync_group_name is not None and
            self.cloud_endpoint_name is not None):
            self.results['cloud_endpoints'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.storage_sync_service_name is not None and
              self.sync_group_name is not None):
            self.results['cloud_endpoints'] = self.format_item(self.listbysyncgroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.cloud_endpoints.get(resource_group_name=self.resource_group_name,
                                                            storage_sync_service_name=self.storage_sync_service_name,
                                                            sync_group_name=self.sync_group_name,
                                                            cloud_endpoint_name=self.cloud_endpoint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysyncgroup(self):
        response = None

        try:
            response = self.mgmt_client.cloud_endpoints.list_by_sync_group(resource_group_name=self.resource_group_name,
                                                                           storage_sync_service_name=self.storage_sync_service_name,
                                                                           sync_group_name=self.sync_group_name)
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
    AzureRMCloudEndpointInfo()


if __name__ == '__main__':
    main()
