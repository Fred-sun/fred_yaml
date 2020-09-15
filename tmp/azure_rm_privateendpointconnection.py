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
module: azure_rm_privateendpointconnection
version_added: '2.9'
short_description: Manage Azure PrivateEndpointConnection instance.
description:
  - 'Create, update and delete instance of Azure PrivateEndpointConnection.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  storage_sync_service_name:
    description:
      - >-
        The name of the storage sync service name within the specified resource
        group.
    required: true
    type: str
  private_endpoint_connection_name:
    description:
      - >-
        The name of the private endpoint connection associated with the Azure
        resource
    required: true
    type: str
  private_link_service_connection_state:
    description:
      - >-
        A collection of information about the state of the connection between
        service consumer and provider.
    type: dict
    suboptions:
      status:
        description:
          - >-
            Indicates whether the connection has been Approved/Rejected/Removed
            by the owner of the service.
        type: str
        choices:
          - Pending
          - Approved
          - Rejected
      description:
        description:
          - The reason for approval/rejection of the connection.
        type: str
      actions_required:
        description:
          - >-
            A message indicating if changes on the service provider require any
            updates on the consumer.
        type: str
  state:
    description:
      - Assert the state of the PrivateEndpointConnection.
      - >-
        Use C(present) to create or update an PrivateEndpointConnection and
        C(absent) to delete it.
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
    - name: PrivateEndpointConnections_Create
      azure_rm_privateendpointconnection: 
        private_endpoint_connection_name: '{privateEndpointConnectionName}'
        resource_group_name: res7687
        storage_sync_service_name: sss2527
        properties:
          private_link_service_connection_state:
            description: Auto-Approved
            status: Approved
        

    - name: PrivateEndpointConnections_Delete
      azure_rm_privateendpointconnection: 
        private_endpoint_connection_name: '{privateEndpointConnectionName}'
        resource_group_name: res6977
        storage_sync_service_name: sss2527
        

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
          Indicates whether the connection has been Approved/Rejected/Removed by
          the owner of the service.
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
          A message indicating if changes on the service provider require any
          updates on the consumer.
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


class AzureRMPrivateEndpointConnection(AzureRMModuleBaseExt):
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
            private_endpoint_connection_name=dict(
                type='str',
                required=True
            ),
            private_link_service_connection_state=dict(
                type='dict',
                disposition='/private_link_service_connection_state',
                options=dict(
                    status=dict(
                        type='str',
                        disposition='status',
                        choices=['Pending',
                                 'Approved',
                                 'Rejected']
                    ),
                    description=dict(
                        type='str',
                        disposition='description'
                    ),
                    actions_required=dict(
                        type='str',
                        disposition='actions_required'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.private_endpoint_connection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPrivateEndpointConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.private_endpoint_connections.create(resource_group_name=self.resource_group_name,
                                                                                storage_sync_service_name=self.storage_sync_service_name,
                                                                                private_endpoint_connection_name=self.private_endpoint_connection_name,
                                                                                properties=self.body)
            else:
                response = self.mgmt_client.private_endpoint_connections.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PrivateEndpointConnection instance.')
            self.fail('Error creating the PrivateEndpointConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.private_endpoint_connections.delete(resource_group_name=self.resource_group_name,
                                                                            storage_sync_service_name=self.storage_sync_service_name,
                                                                            private_endpoint_connection_name=self.private_endpoint_connection_name)
        except CloudError as e:
            self.log('Error attempting to delete the PrivateEndpointConnection instance.')
            self.fail('Error deleting the PrivateEndpointConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.private_endpoint_connections.get(resource_group_name=self.resource_group_name,
                                                                         storage_sync_service_name=self.storage_sync_service_name,
                                                                         private_endpoint_connection_name=self.private_endpoint_connection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPrivateEndpointConnection()


if __name__ == '__main__':
    main()
