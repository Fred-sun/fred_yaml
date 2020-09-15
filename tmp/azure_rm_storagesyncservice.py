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
module: azure_rm_storagesyncservice
version_added: '2.9'
short_description: Manage Azure StorageSyncService instance.
description:
  - 'Create, update and delete instance of Azure StorageSyncService.'
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
  location:
    description:
      - >-
        Required. Gets or sets the location of the resource. This will be one of
        the supported and registered Azure Geo Regions (e.g. West US, East US,
        Southeast Asia, etc.). The geo region of a resource cannot be changed
        once it is created, but if an identical geo region is specified on
        update, the request will succeed.
    type: str
  incoming_traffic_policy:
    description:
      - Incoming Traffic Policy
    type: str
    choices:
      - AllowAllTraffic
      - AllowVirtualNetworksOnly
  state:
    description:
      - Assert the state of the StorageSyncService.
      - >-
        Use C(present) to create or update an StorageSyncService and C(absent)
        to delete it.
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
    - name: StorageSyncServices_Create
      azure_rm_storagesyncservice: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        location: WestUS
        properties:
          incoming_traffic_policy: AllowAllTraffic
        tags: {}
        

    - name: StorageSyncServices_Update
      azure_rm_storagesyncservice: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        properties:
          incoming_traffic_policy: AllowAllTraffic
        tags:
          dept: IT
          environment: Test
        

    - name: StorageSyncServices_Delete
      azure_rm_storagesyncservice: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        

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
      List of private endpoint connection associated with the specified storage
      sync service
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
          A collection of information about the state of the connection between
          service consumer and provider.
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
              A message indicating if changes on the service provider require
              any updates on the consumer.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the private endpoint connection resource.
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


class AzureRMStorageSyncService(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            incoming_traffic_policy=dict(
                type='str',
                disposition='/incoming_traffic_policy',
                choices=['AllowAllTraffic',
                         'AllowVirtualNetworksOnly']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStorageSyncService, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.storage_sync_services.create(resource_group_name=self.resource_group_name,
                                                                         storage_sync_service_name=self.storage_sync_service_name,
                                                                         parameters=self.body)
            else:
                response = self.mgmt_client.storage_sync_services.update(resource_group_name=self.resource_group_name,
                                                                         storage_sync_service_name=self.storage_sync_service_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StorageSyncService instance.')
            self.fail('Error creating the StorageSyncService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.storage_sync_services.delete(resource_group_name=self.resource_group_name,
                                                                     storage_sync_service_name=self.storage_sync_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the StorageSyncService instance.')
            self.fail('Error deleting the StorageSyncService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.storage_sync_services.get(resource_group_name=self.resource_group_name,
                                                                  storage_sync_service_name=self.storage_sync_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStorageSyncService()


if __name__ == '__main__':
    main()
