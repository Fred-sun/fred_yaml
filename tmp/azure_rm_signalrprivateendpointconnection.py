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
module: azure_rm_signalrprivateendpointconnection
version_added: '2.9'
short_description: Manage Azure SignalRPrivateEndpointConnection instance.
description:
  - >-
    Create, update and delete instance of Azure
    SignalRPrivateEndpointConnection.
options:
  private_endpoint_connection_name:
    description:
      - >-
        The name of the private endpoint connection associated with the SignalR
        resource.
    required: true
    type: str
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  resource_name:
    description:
      - The name of the SignalR resource.
    required: true
    type: str
  private_link_service_connection_state:
    description:
      - Connection state
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
          - Disconnected
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
  id:
    description:
      - Full qualified Id of the private endpoint
    type: str
  state:
    description:
      - Assert the state of the SignalRPrivateEndpointConnection.
      - >-
        Use C(present) to create or update an SignalRPrivateEndpointConnection
        and C(absent) to delete it.
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
    - name: SignalRPrivateEndpointConnections_Update
      azure_rm_signalrprivateendpointconnection: 
        private_endpoint_connection_name: mySignalRService.1fa229cd-bf3f-47f0-8c49-afb36723997e
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        properties:
          private_endpoint:
            id: >-
              /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/myResourceGroup/providers/Microsoft.Network/privateEndpoints/myPrivateEndpoint
          private_link_service_connection_state:
            description: {}
            actions_required: None
            status: Approved
        

    - name: SignalRPrivateEndpointConnections_Delete
      azure_rm_signalrprivateendpointconnection: 
        private_endpoint_connection_name: mySignalRService.1fa229cd-bf3f-47f0-8c49-afb36723997e
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        

'''

RETURN = '''
id:
  description:
    - Fully qualified resource Id for the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource - e.g. "Microsoft.SignalRService/SignalR"
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state of the private endpoint connection
  returned: always
  type: str
  sample: null
private_link_service_connection_state:
  description:
    - Connection state
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
id_properties_private_endpoint_id:
  description:
    - Full qualified Id of the private endpoint
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
    from azure.mgmt.signal import SignalRManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSignalRPrivateEndpointConnection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            private_endpoint_connection_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
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
                                 'Rejected',
                                 'Disconnected']
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
            id=dict(
                type='str',
                disposition='/id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.private_endpoint_connection_name = None
        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSignalRPrivateEndpointConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SignalRManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

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
                response = self.mgmt_client.signal_rprivate_endpoint_connections.create()
            else:
                response = self.mgmt_client.signal_rprivate_endpoint_connections.update(private_endpoint_connection_name=self.private_endpoint_connection_name,
                                                                                        resource_group_name=self.resource_group_name,
                                                                                        resource_name=self.resource_name,
                                                                                        parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SignalRPrivateEndpointConnection instance.')
            self.fail('Error creating the SignalRPrivateEndpointConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.signal_rprivate_endpoint_connections.delete(private_endpoint_connection_name=self.private_endpoint_connection_name,
                                                                                    resource_group_name=self.resource_group_name,
                                                                                    resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the SignalRPrivateEndpointConnection instance.')
            self.fail('Error deleting the SignalRPrivateEndpointConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.signal_rprivate_endpoint_connections.get(private_endpoint_connection_name=self.private_endpoint_connection_name,
                                                                                 resource_group_name=self.resource_group_name,
                                                                                 resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSignalRPrivateEndpointConnection()


if __name__ == '__main__':
    main()
