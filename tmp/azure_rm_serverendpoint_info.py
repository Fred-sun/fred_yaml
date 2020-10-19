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
module: azure_rm_serverendpoint_info
version_added: '2.9'
short_description: Get ServerEndpoint info.
description:
  - Get info of ServerEndpoint.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ServerEndpoints_Get
      azure_rm_serverendpoint_info: 
        resource_group_name: SampleResourceGroup_1
        server_endpoint_name: SampleServerEndpoint_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        

    - name: ServerEndpoints_ListBySyncGroup
      azure_rm_serverendpoint_info: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        sync_group_name: SampleSyncGroup_1
        

'''

RETURN = '''
server_endpoints:
  description: >-
    A list of dict results where the key is the name of the ServerEndpoint and
    the values are the facts for that ServerEndpoint.
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
        - >-
          Level of free space to be maintained by Cloud Tiering if it is
          enabled.
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
                      Count of persistent files not syncing with the specified
                      error code
                  returned: always
                  type: integer
                  sample: null
                transient_count:
                  description:
                    - >-
                      Count of transient files not syncing with the specified
                      error code
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
                      Count of persistent files not syncing with the specified
                      error code
                  returned: always
                  type: integer
                  sample: null
                transient_count:
                  description:
                    - >-
                      Count of transient files not syncing with the specified
                      error code
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
            - >-
              Information regarding how much local space cloud tiering is
              saving.
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
                  Percentage of total bytes (hit + miss) that were served from
                  the local server
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
          Policy for enabling follow-the-sun business models: link local cache
          to cloud behavior to pre-populate before local access.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Collection of ServerEndpoint.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              Level of free space to be maintained by Cloud Tiering if it is
              enabled.
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
                    - >-
                      Array of per-item errors coming from the last sync
                      session.
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
                          Count of persistent files not syncing with the
                          specified error code
                      returned: always
                      type: integer
                      sample: null
                    transient_count:
                      description:
                        - >-
                          Count of transient files not syncing with the
                          specified error code
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
                    - >-
                      Array of per-item errors coming from the last sync
                      session.
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
                          Count of persistent files not syncing with the
                          specified error code
                      returned: always
                      type: integer
                      sample: null
                    transient_count:
                      description:
                        - >-
                          Count of transient files not syncing with the
                          specified error code
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
                - >-
                  Information regarding how much local space cloud tiering is
                  saving.
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
                  Information regarding how well the local cache on the server
                  is performing.
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
                      Percentage of total bytes (hit + miss) that were served
                      from the local server
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
                      In the case where multiple server endpoints are present in
                      a volume, an effective free space policy is applied.
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
              Policy for enabling follow-the-sun business models: link local
              cache to cloud behavior to pre-populate before local access.
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


class AzureRMServerEndpointInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.sync_group_name = None
        self.server_endpoint_name = None

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
        super(AzureRMServerEndpointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.storage_sync_service_name is not None and
            self.sync_group_name is not None and
            self.server_endpoint_name is not None):
            self.results['server_endpoints'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.storage_sync_service_name is not None and
              self.sync_group_name is not None):
            self.results['server_endpoints'] = self.format_item(self.listbysyncgroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.server_endpoints.get(resource_group_name=self.resource_group_name,
                                                             storage_sync_service_name=self.storage_sync_service_name,
                                                             sync_group_name=self.sync_group_name,
                                                             server_endpoint_name=self.server_endpoint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysyncgroup(self):
        response = None

        try:
            response = self.mgmt_client.server_endpoints.list_by_sync_group(resource_group_name=self.resource_group_name,
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
    AzureRMServerEndpointInfo()


if __name__ == '__main__':
    main()
