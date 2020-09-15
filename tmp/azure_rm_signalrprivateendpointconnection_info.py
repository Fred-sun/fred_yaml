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
module: azure_rm_signalrprivateendpointconnection_info
version_added: '2.9'
short_description: Get SignalRPrivateEndpointConnection info.
description:
  - Get info of SignalRPrivateEndpointConnection.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SignalRPrivateEndpointConnections_Get
      azure_rm_signalrprivateendpointconnection_info: 
        private_endpoint_connection_name: mySignalRService.1fa229cd-bf3f-47f0-8c49-afb36723997e
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        

'''

RETURN = '''
signal_rprivate_endpoint_connections:
  description: >-
    A list of dict results where the key is the name of the
    SignalRPrivateEndpointConnection and the values are the facts for that
    SignalRPrivateEndpointConnection.
  returned: always
  type: complex
  contains:
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
    id_properties_private_endpoint_id:
      description:
        - Full qualified Id of the private endpoint
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
    from azure.mgmt.signal import SignalRManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSignalRPrivateEndpointConnectionInfo(AzureRMModuleBase):
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
            )
        )

        self.private_endpoint_connection_name = None
        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSignalRPrivateEndpointConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SignalRManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

        if (self.private_endpoint_connection_name is not None and
            self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['signal_rprivate_endpoint_connections'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.signal_rprivate_endpoint_connections.get(private_endpoint_connection_name=self.private_endpoint_connection_name,
                                                                                 resource_group_name=self.resource_group_name,
                                                                                 resource_name=self.resource_name)
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
    AzureRMSignalRPrivateEndpointConnectionInfo()


if __name__ == '__main__':
    main()
