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
module: azure_rm_serverendpoint
version_added: '2.9'
short_description: Manage Azure ServerEndpoint instance.
description:
  - 'Create, update and delete instance of Azure ServerEndpoint.'
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
  server_endpoint_name:
    description:
      - Name of Server Endpoint object.
    required: true
    type: str
  server_local_path:
    description:
      - Server Local path.
    type: str
  cloud_tiering:
    description:
      - Cloud Tiering.
    type: str
    choices:
      - 'on'
      - 'off'
  volume_free_space_percent:
    description:
      - Level of free space to be maintained by Cloud Tiering if it is enabled.
    type: integer
  tier_files_older_than_days:
    description:
      - Tier files older than days.
    type: integer
  friendly_name:
    description:
      - Friendly Name
    type: str
  server_resource_id:
    description:
      - Server Resource Id.
    type: str
  offline_data_transfer:
    description:
      - Offline data transfer
    type: str
    choices:
      - 'on'
      - 'off'
  offline_data_transfer_share_name:
    description:
      - Offline data transfer share name
    type: str
  initial_download_policy:
    description:
      - Policy for how namespace and files are recalled during FastDr.
    type: str
    choices:
      - NamespaceOnly
      - NamespaceThenModifiedFiles
      - AvoidTieredFiles
  local_cache_mode:
    description:
      - >-
        Policy for enabling follow-the-sun business models: link local cache to
        cloud behavior to pre-populate before local access.
    type: str
    choices:
      - DownloadNewAndModifiedFiles
      - UpdateLocallyCachedFiles
  state:
    description:
      - Assert the state of the ServerEndpoint.
      - >-
        Use C(present) to create or update an ServerEndpoint and C(absent) to
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
    - name: ServerEndpoints_Create
      azure_rm_serverendpoint: 
        resource_group_name: SampleResourceGroup_1
        server_endpoint_name: SampleServerEndpoint_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        properties:
          cloud_tiering: 'off'
          initial_download_policy: NamespaceThenModifiedFiles
          local_cache_mode: UpdateLocallyCachedFiles
          offline_data_transfer: 'on'
          offline_data_transfer_share_name: myfileshare
          server_local_path: 'D:\SampleServerEndpoint_1'
          server_resource_id: >-
            /subscriptions/52b8da2f-61e0-4a1f-8dde-336911f367fb/resourceGroups/SampleResourceGroup_1/providers/Microsoft.StorageSync/storageSyncServices/SampleStorageSyncService_1/registeredServers/080d4133-bdb5-40a0-96a0-71a6057bfe9a
          tier_files_older_than_days: 0
          volume_free_space_percent: 100
        

    - name: ServerEndpoints_Update
      azure_rm_serverendpoint: 
        resource_group_name: SampleResourceGroup_1
        server_endpoint_name: SampleServerEndpoint_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        properties:
          cloud_tiering: 'off'
          local_cache_mode: UpdateLocallyCachedFiles
          offline_data_transfer: 'off'
          tier_files_older_than_days: 0
          volume_free_space_percent: 100
        

    - name: ServerEndpoints_Delete
      azure_rm_serverendpoint: 
        resource_group_name: SampleResourceGroup_1
        server_endpoint_name: SampleServerEndpoint_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        

'''

RETURN = '''
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
server_local_path:
  description:
    - Server Local path.
  returned: always
  type: str
  sample: null
cloud_tiering:
  description:
    - Cloud Tiering.
  returned: always
  type: str
  sample: null
volume_free_space_percent:
  description:
    - Level of free space to be maintained by Cloud Tiering if it is enabled.
  returned: always
  type: integer
  sample: null
tier_files_older_than_days:
  description:
    - Tier files older than days.
  returned: always
  type: integer
  sample: null
friendly_name:
  description:
    - Friendly Name
  returned: always
  type: str
  sample: null
server_resource_id:
  description:
    - Server Resource Id.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - ServerEndpoint Provisioning State
  returned: always
  type: str
  sample: null
last_workflow_id:
  description:
    - ServerEndpoint lastWorkflowId
  returned: always
  type: str
  sample: null
last_operation_name:
  description:
    - Resource Last Operation Name
  returned: always
  type: str
  sample: null
sync_status:
  description:
    - Server Endpoint sync status
  returned: always
  type: dict
  sample: null
  contains:
    download_health:
      description:
        - Download Health Status.
      returned: always
      type: str
      sample: null
    upload_health:
      description:
        - Upload Health Status.
      returned: always
      type: str
      sample: null
    combined_health:
      description:
        - Combined Health Status.
      returned: always
      type: str
      sample: null
    sync_activity:
      description:
        - Sync activity
      returned: always
      type: str
      sample: null
    total_persistent_files_not_syncing_count:
      description:
        - >-
          Total count of persistent files not syncing (combined upload +
          download).
      returned: always
      type: integer
      sample: null
    last_updated_timestamp:
      description:
        - Last Updated Timestamp
      returned: always
      type: str
      sample: null
    upload_status:
      description:
        - Upload Status
      returned: always
      type: dict
      sample: null
      contains:
        last_sync_result:
          description:
            - Last sync result (HResult)
          returned: always
          type: integer
          sample: null
        last_sync_timestamp:
          description:
            - Last sync timestamp
          returned: always
          type: str
          sample: null
        last_sync_success_timestamp:
          description:
            - Last sync success timestamp
          returned: always
          type: str
          sample: null
        last_sync_per_item_error_count:
          description:
            - Last sync per item error count.
          returned: always
          type: integer
          sample: null
        persistent_files_not_syncing_count:
          description:
            - Count of persistent files not syncing.
          returned: always
          type: integer
          sample: null
        transient_files_not_syncing_count:
          description:
            - Count of transient files not syncing.
          returned: always
          type: integer
          sample: null
        files_not_syncing_errors:
          description:
            - Array of per-item errors coming from the last sync session.
          returned: always
          type: list
          sample: null
          contains:
            error_code:
              description:
                - Error code (HResult)
              returned: always
              type: integer
              sample: null
            persistent_count:
              description:
                - >-
                  Count of persistent files not syncing with the specified error
                  code
              returned: always
              type: integer
              sample: null
            transient_count:
              description:
                - >-
                  Count of transient files not syncing with the specified error
                  code
              returned: always
              type: integer
              sample: null
    download_status:
      description:
        - Download Status
      returned: always
      type: dict
      sample: null
      contains:
        last_sync_result:
          description:
            - Last sync result (HResult)
          returned: always
          type: integer
          sample: null
        last_sync_timestamp:
          description:
            - Last sync timestamp
          returned: always
          type: str
          sample: null
        last_sync_success_timestamp:
          description:
            - Last sync success timestamp
          returned: always
          type: str
          sample: null
        last_sync_per_item_error_count:
          description:
            - Last sync per item error count.
          returned: always
          type: integer
          sample: null
        persistent_files_not_syncing_count:
          description:
            - Count of persistent files not syncing.
          returned: always
          type: integer
          sample: null
        transient_files_not_syncing_count:
          description:
            - Count of transient files not syncing.
          returned: always
          type: integer
          sample: null
        files_not_syncing_errors:
          description:
            - Array of per-item errors coming from the last sync session.
          returned: always
          type: list
          sample: null
          contains:
            error_code:
              description:
                - Error code (HResult)
              returned: always
              type: integer
              sample: null
            persistent_count:
              description:
                - >-
                  Count of persistent files not syncing with the specified error
                  code
              returned: always
              type: integer
              sample: null
            transient_count:
              description:
                - >-
                  Count of transient files not syncing with the specified error
                  code
              returned: always
              type: integer
              sample: null
    upload_activity:
      description:
        - Upload sync activity
      returned: always
      type: dict
      sample: null
      contains:
        timestamp:
          description:
            - Timestamp when properties were updated
          returned: always
          type: str
          sample: null
        per_item_error_count:
          description:
            - Per item error count
          returned: always
          type: integer
          sample: null
        applied_item_count:
          description:
            - Applied item count.
          returned: always
          type: integer
          sample: null
        total_item_count:
          description:
            - Total item count (if available)
          returned: always
          type: integer
          sample: null
        applied_bytes:
          description:
            - Applied bytes
          returned: always
          type: integer
          sample: null
        total_bytes:
          description:
            - Total bytes (if available)
          returned: always
          type: integer
          sample: null
    download_activity:
      description:
        - Download sync activity
      returned: always
      type: dict
      sample: null
      contains:
        timestamp:
          description:
            - Timestamp when properties were updated
          returned: always
          type: str
          sample: null
        per_item_error_count:
          description:
            - Per item error count
          returned: always
          type: integer
          sample: null
        applied_item_count:
          description:
            - Applied item count.
          returned: always
          type: integer
          sample: null
        total_item_count:
          description:
            - Total item count (if available)
          returned: always
          type: integer
          sample: null
        applied_bytes:
          description:
            - Applied bytes
          returned: always
          type: integer
          sample: null
        total_bytes:
          description:
            - Total bytes (if available)
          returned: always
          type: integer
          sample: null
    offline_data_transfer_status:
      description:
        - Offline Data Transfer State
      returned: always
      type: str
      sample: null
offline_data_transfer:
  description:
    - Offline data transfer
  returned: always
  type: str
  sample: null
offline_data_transfer_storage_account_resource_id:
  description:
    - Offline data transfer storage account resource ID
  returned: always
  type: str
  sample: null
offline_data_transfer_storage_account_tenant_id:
  description:
    - Offline data transfer storage account tenant ID
  returned: always
  type: str
  sample: null
offline_data_transfer_share_name:
  description:
    - Offline data transfer share name
  returned: always
  type: str
  sample: null
cloud_tiering_status:
  description:
    - Cloud tiering status. Only populated if cloud tiering is enabled.
  returned: always
  type: dict
  sample: null
  contains:
    last_updated_timestamp:
      description:
        - Last updated timestamp
      returned: always
      type: str
      sample: null
    health:
      description:
        - Cloud tiering health state.
      returned: always
      type: str
      sample: null
    health_last_updated_timestamp:
      description:
        - The last updated timestamp of health state
      returned: always
      type: str
      sample: null
    last_cloud_tiering_result:
      description:
        - Last cloud tiering result (HResult)
      returned: always
      type: integer
      sample: null
    last_success_timestamp:
      description:
        - Last cloud tiering success timestamp
      returned: always
      type: str
      sample: null
    space_savings:
      description:
        - Information regarding how much local space cloud tiering is saving.
      returned: always
      type: dict
      sample: null
      contains:
        last_updated_timestamp:
          description:
            - Last updated timestamp
          returned: always
          type: str
          sample: null
        volume_size_bytes:
          description:
            - Volume size
          returned: always
          type: integer
          sample: null
        total_size_cloud_bytes:
          description:
            - Total size of content in the azure file share
          returned: always
          type: integer
          sample: null
        cached_size_bytes:
          description:
            - Cached content size on the server
          returned: always
          type: integer
          sample: null
        space_savings_percent:
          description:
            - Percentage of cached size over total size
          returned: always
          type: integer
          sample: null
        space_savings_bytes:
          description:
            - Count of bytes saved on the server
          returned: always
          type: integer
          sample: null
    cache_performance:
      description:
        - >-
          Information regarding how well the local cache on the server is
          performing.
      returned: always
      type: dict
      sample: null
      contains:
        last_updated_timestamp:
          description:
            - Last updated timestamp
          returned: always
          type: str
          sample: null
        cache_hit_bytes:
          description:
            - Count of bytes that were served from the local server
          returned: always
          type: integer
          sample: null
        cache_miss_bytes:
          description:
            - Count of bytes that were served from the cloud
          returned: always
          type: integer
          sample: null
        cache_hit_bytes_percent:
          description:
            - >-
              Percentage of total bytes (hit + miss) that were served from the
              local server
          returned: always
          type: integer
          sample: null
    files_not_tiering:
      description:
        - Information regarding files that failed to be tiered
      returned: always
      type: dict
      sample: null
      contains:
        last_updated_timestamp:
          description:
            - Last updated timestamp
          returned: always
          type: str
          sample: null
        total_file_count:
          description:
            - Last cloud tiering result (HResult)
          returned: always
          type: integer
          sample: null
        errors:
          description:
            - Array of tiering errors
          returned: always
          type: list
          sample: null
          contains:
            error_code:
              description:
                - Error code (HResult)
              returned: always
              type: integer
              sample: null
            file_count:
              description:
                - Count of files with this error
              returned: always
              type: integer
              sample: null
    volume_free_space_policy_status:
      description:
        - Status of the volume free space policy
      returned: always
      type: dict
      sample: null
      contains:
        last_updated_timestamp:
          description:
            - Last updated timestamp
          returned: always
          type: str
          sample: null
        effective_volume_free_space_policy:
          description:
            - >-
              In the case where multiple server endpoints are present in a
              volume, an effective free space policy is applied.
          returned: always
          type: integer
          sample: null
        current_volume_free_space_percent:
          description:
            - Current volume free space percentage.
          returned: always
          type: integer
          sample: null
    date_policy_status:
      description:
        - Status of the date policy
      returned: always
      type: dict
      sample: null
      contains:
        last_updated_timestamp:
          description:
            - Last updated timestamp
          returned: always
          type: str
          sample: null
        tiered_files_most_recent_access_timestamp:
          description:
            - Most recent access time of tiered files
          returned: always
          type: str
          sample: null
recall_status:
  description:
    - Recall status. Only populated if cloud tiering is enabled.
  returned: always
  type: dict
  sample: null
  contains:
    last_updated_timestamp:
      description:
        - Last updated timestamp
      returned: always
      type: str
      sample: null
    total_recall_errors_count:
      description:
        - Total count of recall errors.
      returned: always
      type: integer
      sample: null
    recall_errors:
      description:
        - Array of recall errors
      returned: always
      type: list
      sample: null
      contains:
        error_code:
          description:
            - Error code (HResult)
          returned: always
          type: integer
          sample: null
        count:
          description:
            - Count of occurences of the error
          returned: always
          type: integer
          sample: null
initial_download_policy:
  description:
    - Policy for how namespace and files are recalled during FastDr.
  returned: always
  type: str
  sample: null
local_cache_mode:
  description:
    - >-
      Policy for enabling follow-the-sun business models: link local cache to
      cloud behavior to pre-populate before local access.
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
    from azure.mgmt.microsoft import Microsoft Storage Sync
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMServerEndpoint(AzureRMModuleBaseExt):
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
            server_endpoint_name=dict(
                type='str',
                required=True
            ),
            server_local_path=dict(
                type='str',
                disposition='/server_local_path'
            ),
            cloud_tiering=dict(
                type='str',
                disposition='/cloud_tiering',
                choices=['on',
                         'off']
            ),
            volume_free_space_percent=dict(
                type='integer',
                disposition='/volume_free_space_percent'
            ),
            tier_files_older_than_days=dict(
                type='integer',
                disposition='/tier_files_older_than_days'
            ),
            friendly_name=dict(
                type='str',
                disposition='/friendly_name'
            ),
            server_resource_id=dict(
                type='str',
                disposition='/server_resource_id'
            ),
            offline_data_transfer=dict(
                type='str',
                disposition='/offline_data_transfer',
                choices=['on',
                         'off']
            ),
            offline_data_transfer_share_name=dict(
                type='str',
                disposition='/offline_data_transfer_share_name'
            ),
            initial_download_policy=dict(
                type='str',
                disposition='/initial_download_policy',
                choices=['NamespaceOnly',
                         'NamespaceThenModifiedFiles',
                         'AvoidTieredFiles']
            ),
            local_cache_mode=dict(
                type='str',
                disposition='/local_cache_mode',
                choices=['DownloadNewAndModifiedFiles',
                         'UpdateLocallyCachedFiles']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.sync_group_name = None
        self.server_endpoint_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServerEndpoint, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

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
                response = self.mgmt_client.server_endpoints.create(resource_group_name=self.resource_group_name,
                                                                    storage_sync_service_name=self.storage_sync_service_name,
                                                                    sync_group_name=self.sync_group_name,
                                                                    server_endpoint_name=self.server_endpoint_name,
                                                                    parameters=self.body)
            else:
                response = self.mgmt_client.server_endpoints.update(resource_group_name=self.resource_group_name,
                                                                    storage_sync_service_name=self.storage_sync_service_name,
                                                                    sync_group_name=self.sync_group_name,
                                                                    server_endpoint_name=self.server_endpoint_name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ServerEndpoint instance.')
            self.fail('Error creating the ServerEndpoint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.server_endpoints.delete(resource_group_name=self.resource_group_name,
                                                                storage_sync_service_name=self.storage_sync_service_name,
                                                                sync_group_name=self.sync_group_name,
                                                                server_endpoint_name=self.server_endpoint_name)
        except CloudError as e:
            self.log('Error attempting to delete the ServerEndpoint instance.')
            self.fail('Error deleting the ServerEndpoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.server_endpoints.get(resource_group_name=self.resource_group_name,
                                                             storage_sync_service_name=self.storage_sync_service_name,
                                                             sync_group_name=self.sync_group_name,
                                                             server_endpoint_name=self.server_endpoint_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServerEndpoint()


if __name__ == '__main__':
    main()
