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
module: azure_rm_vnetpeering
version_added: '2.9'
short_description: Manage Azure vNetPeering instance.
description:
  - 'Create, update and delete instance of Azure vNetPeering.'
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
    required: true
    type: str
  allow_virtual_network_access:
    description:
      - >-
        Whether the VMs in the local virtual network space would be able to
        access the VMs in remote virtual network space.
    type: bool
  allow_forwarded_traffic:
    description:
      - >-
        Whether the forwarded traffic from the VMs in the local virtual network
        will be allowed/disallowed in remote virtual network.
    type: bool
  allow_gateway_transit:
    description:
      - >-
        If gateway links can be used in remote virtual networking to link to
        this virtual network.
    type: bool
  use_remote_gateways:
    description:
      - >-
        If remote gateways can be used on this virtual network. If the flag is
        set to true, and allowGatewayTransit on remote peering is also true,
        virtual network will use gateways of remote virtual network for transit.
        Only one peering can have this flag set to true. This flag cannot be set
        if virtual network already has a gateway.
    type: bool
  databricks_address_space:
    description:
      - The reference to the databricks virtual network address space.
    type: dict
    suboptions:
      address_prefixes:
        description:
          - >-
            A list of address blocks reserved for this virtual network in CIDR
            notation.
        type: list
  remote_address_space:
    description:
      - The reference to the remote virtual network address space.
    type: dict
    suboptions:
      address_prefixes:
        description:
          - >-
            A list of address blocks reserved for this virtual network in CIDR
            notation.
        type: list
  id:
    description:
      - The Id of the remote virtual network.
    type: str
  virtual_network_peering_properties_format_databricks_virtual_network_id:
    description:
      - The Id of the databricks virtual network.
    type: str
  state:
    description:
      - Assert the state of the vNetPeering.
      - >-
        Use C(present) to create or update an vNetPeering and C(absent) to
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
    - name: Delete a workspace vNet Peering
      azure_rm_vnetpeering: 
        peering_name: vNetPeering
        resource_group_name: rg
        workspace_name: myWorkspace
        

    - name: Create vNet Peering for Workspace
      azure_rm_vnetpeering: 
        peering_name: vNetPeeringTest
        resource_group_name: rg
        workspace_name: myWorkspace
        

'''

RETURN = '''
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
      Whether the VMs in the local virtual network space would be able to access
      the VMs in remote virtual network space.
  returned: always
  type: bool
  sample: null
allow_forwarded_traffic:
  description:
    - >-
      Whether the forwarded traffic from the VMs in the local virtual network
      will be allowed/disallowed in remote virtual network.
  returned: always
  type: bool
  sample: null
allow_gateway_transit:
  description:
    - >-
      If gateway links can be used in remote virtual networking to link to this
      virtual network.
  returned: always
  type: bool
  sample: null
use_remote_gateways:
  description:
    - >-
      If remote gateways can be used on this virtual network. If the flag is set
      to true, and allowGatewayTransit on remote peering is also true, virtual
      network will use gateways of remote virtual network for transit. Only one
      peering can have this flag set to true. This flag cannot be set if virtual
      network already has a gateway.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.databricks import DatabricksClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMvNetPeering(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            allow_virtual_network_access=dict(
                type='bool',
                disposition='/allow_virtual_network_access'
            ),
            allow_forwarded_traffic=dict(
                type='bool',
                disposition='/allow_forwarded_traffic'
            ),
            allow_gateway_transit=dict(
                type='bool',
                disposition='/allow_gateway_transit'
            ),
            use_remote_gateways=dict(
                type='bool',
                disposition='/use_remote_gateways'
            ),
            databricks_address_space=dict(
                type='dict',
                disposition='/databricks_address_space',
                options=dict(
                    address_prefixes=dict(
                        type='list',
                        disposition='address_prefixes',
                        elements='str'
                    )
                )
            ),
            remote_address_space=dict(
                type='dict',
                disposition='/remote_address_space',
                options=dict(
                    address_prefixes=dict(
                        type='list',
                        disposition='address_prefixes',
                        elements='str'
                    )
                )
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            virtual_network_peering_properties_format_databricks_virtual_network_id=dict(
                type='str',
                disposition='/virtual_network_peering_properties_format_databricks_virtual_network_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.peering_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMvNetPeering, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DatabricksClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-04-01')

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
            response = self.mgmt_client.v_net_peering.create_or_update(resource_group_name=self.resource_group_name,
                                                                       workspace_name=self.workspace_name,
                                                                       peering_name=self.peering_name,
                                                                       virtual_network_peering_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the vNetPeering instance.')
            self.fail('Error creating the vNetPeering instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.v_net_peering.delete(resource_group_name=self.resource_group_name,
                                                             workspace_name=self.workspace_name,
                                                             peering_name=self.peering_name)
        except CloudError as e:
            self.log('Error attempting to delete the vNetPeering instance.')
            self.fail('Error deleting the vNetPeering instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.v_net_peering.get(resource_group_name=self.resource_group_name,
                                                          workspace_name=self.workspace_name,
                                                          peering_name=self.peering_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMvNetPeering()


if __name__ == '__main__':
    main()
