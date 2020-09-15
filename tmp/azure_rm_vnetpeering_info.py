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
module: azure_rm_vnetpeering_info
version_added: '2.9'
short_description: Get vNetPeering info.
description:
  - Get info of vNetPeering.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  workspace_name:
    description:
      - The name of the workspace.
    required: true
    type: str
  peering_name:
    description:
      - The name of the workspace vNet peering.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a workspace with vNet Peering Configured
      azure_rm_vnetpeering_info: 
        peering_name: vNetPeering
        resource_group_name: rg
        workspace_name: myWorkspace
        

    - name: List all vNet Peerings for the workspace
      azure_rm_vnetpeering_info: 
        resource_group_name: rg
        workspace_name: myWorkspace
        

'''

RETURN = '''
v_net_peering:
  description: >-
    A list of dict results where the key is the name of the vNetPeering and the
    values are the facts for that vNetPeering.
  returned: always
  type: complex
  contains:
    name:
      description:
        - Name of the virtual network peering resource
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    type:
      description:
        - type of the virtual network peering resource
      returned: always
      type: str
      sample: null
    allow_virtual_network_access:
      description:
        - >-
          Whether the VMs in the local virtual network space would be able to
          access the VMs in remote virtual network space.
      returned: always
      type: bool
      sample: null
    allow_forwarded_traffic:
      description:
        - >-
          Whether the forwarded traffic from the VMs in the local virtual
          network will be allowed/disallowed in remote virtual network.
      returned: always
      type: bool
      sample: null
    allow_gateway_transit:
      description:
        - >-
          If gateway links can be used in remote virtual networking to link to
          this virtual network.
      returned: always
      type: bool
      sample: null
    use_remote_gateways:
      description:
        - >-
          If remote gateways can be used on this virtual network. If the flag is
          set to true, and allowGatewayTransit on remote peering is also true,
          virtual network will use gateways of remote virtual network for
          transit. Only one peering can have this flag set to true. This flag
          cannot be set if virtual network already has a gateway.
      returned: always
      type: bool
      sample: null
    databricks_address_space:
      description:
        - The reference to the databricks virtual network address space.
      returned: always
      type: dict
      sample: null
      contains:
        address_prefixes:
          description:
            - >-
              A list of address blocks reserved for this virtual network in CIDR
              notation.
          returned: always
          type: list
          sample: null
    remote_address_space:
      description:
        - The reference to the remote virtual network address space.
      returned: always
      type: dict
      sample: null
      contains:
        address_prefixes:
          description:
            - >-
              A list of address blocks reserved for this virtual network in CIDR
              notation.
          returned: always
          type: list
          sample: null
    peering_state:
      description:
        - The status of the virtual network peering.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the virtual network peering resource.
      returned: always
      type: str
      sample: null
    id_properties_remote_virtual_network_id:
      description:
        - The Id of the remote virtual network.
      returned: always
      type: str
      sample: null
    id_properties_databricks_virtual_network_id:
      description:
        - The Id of the databricks virtual network.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of virtual network peerings on workspace.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the virtual network peering resource
          returned: always
          type: str
          sample: null
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        type:
          description:
            - type of the virtual network peering resource
          returned: always
          type: str
          sample: null
        allow_virtual_network_access:
          description:
            - >-
              Whether the VMs in the local virtual network space would be able
              to access the VMs in remote virtual network space.
          returned: always
          type: bool
          sample: null
        allow_forwarded_traffic:
          description:
            - >-
              Whether the forwarded traffic from the VMs in the local virtual
              network will be allowed/disallowed in remote virtual network.
          returned: always
          type: bool
          sample: null
        allow_gateway_transit:
          description:
            - >-
              If gateway links can be used in remote virtual networking to link
              to this virtual network.
          returned: always
          type: bool
          sample: null
        use_remote_gateways:
          description:
            - >-
              If remote gateways can be used on this virtual network. If the
              flag is set to true, and allowGatewayTransit on remote peering is
              also true, virtual network will use gateways of remote virtual
              network for transit. Only one peering can have this flag set to
              true. This flag cannot be set if virtual network already has a
              gateway.
          returned: always
          type: bool
          sample: null
        databricks_address_space:
          description:
            - The reference to the databricks virtual network address space.
          returned: always
          type: dict
          sample: null
          contains:
            address_prefixes:
              description:
                - >-
                  A list of address blocks reserved for this virtual network in
                  CIDR notation.
              returned: always
              type: list
              sample: null
        remote_address_space:
          description:
            - The reference to the remote virtual network address space.
          returned: always
          type: dict
          sample: null
          contains:
            address_prefixes:
              description:
                - >-
                  A list of address blocks reserved for this virtual network in
                  CIDR notation.
              returned: always
              type: list
              sample: null
        peering_state:
          description:
            - The status of the virtual network peering.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state of the virtual network peering resource.
          returned: always
          type: str
          sample: null
        id_properties_remote_virtual_network_id:
          description:
            - The Id of the remote virtual network.
          returned: always
          type: str
          sample: null
        id_properties_databricks_virtual_network_id:
          description:
            - The Id of the databricks virtual network.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          URL to get the next set of virtual network peering list results if
          there are any.
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
    from azure.mgmt.databricks import DatabricksClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMvNetPeeringInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            ),
            peering_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.peering_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMvNetPeeringInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DatabricksClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-04-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.peering_name is not None):
            self.results['v_net_peering'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['v_net_peering'] = self.format_item(self.listbyworkspace())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.v_net_peering.get(resource_group_name=self.resource_group_name,
                                                          workspace_name=self.workspace_name,
                                                          peering_name=self.peering_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyworkspace(self):
        response = None

        try:
            response = self.mgmt_client.v_net_peering.list_by_workspace(resource_group_name=self.resource_group_name,
                                                                        workspace_name=self.workspace_name)
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
    AzureRMvNetPeeringInfo()


if __name__ == '__main__':
    main()
