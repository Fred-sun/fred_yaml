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
module: azure_rm_virtualnetworkfunction
version_added: '2.9'
short_description: Manage Azure VirtualNetworkFunction instance.
description:
  - 'Create, update and delete instance of Azure VirtualNetworkFunction.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  virtual_network_function_name:
    description:
      - The name of the hybrid network virtual network function.
      - The name of hybrid network virtual network function resource.
      - Resource name for the hybrid network virtual network function resource.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  etag:
    description:
      - A unique read-only string that changes whenever the resource is updated.
    type: str
  device:
    description:
      - The reference to the hybrid network device.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  sku_name:
    description:
      - The sku name for the hybrid network virtual network function.
    type: str
  vendor_name:
    description:
      - The vendor name for the hybrid network virtual network function.
    type: str
  managed_application_parameters:
    description:
      - The parameters for the managed application.
    type: any
  virtual_network_function_user_configurations:
    description:
      - The virtual network function configurations from the user.
    type: list
    suboptions:
      role_name:
        description:
          - The name of the virtual network function role.
        type: str
      user_data_parameters:
        description:
          - The user data parameters from the customer.
        type: any
      network_interfaces:
        description:
          - The network interface configuration.
        type: list
        suboptions:
          network_interface_name:
            description:
              - The name of the network interface.
            type: str
          mac_address:
            description:
              - The MAC address of the network interface.
            type: str
          ip_configurations:
            description:
              - A list of IP configurations of the network interface.
            type: list
            suboptions:
              ip_allocation_method:
                description:
                  - IP address allocation method.
                type: str
                choices:
                  - Unknown
                  - Static
                  - Dynamic
              ip_address:
                description:
                  - The value of the IP address.
                type: str
              subnet:
                description:
                  - The value of the subnet.
                type: str
              gateway:
                description:
                  - The value of the gateway.
                type: str
              ip_version:
                description:
                  - IP address version.
                type: str
                choices:
                  - Unknown
                  - IPv4
              dns_servers:
                description:
                  - The list of DNS servers IP addresses.
                type: list
          vm_switch_type:
            description:
              - The type of VM switch
            type: str
            choices:
              - Unknown
              - Management
              - Wan
              - Lan
              - Internal
  state:
    description:
      - Assert the state of the VirtualNetworkFunction.
      - >-
        Use C(present) to create or update an VirtualNetworkFunction and
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
    - name: Delete hybrid network virtual network function resource
      azure_rm_virtualnetworkfunction: 
        resource_group_name: rg
        virtual_network_function_name: testVnf
        

    - name: Create hybrid network virtual network function resource
      azure_rm_virtualnetworkfunction: 
        resource_group_name: rg
        virtual_network_function_name: testVnf
        location: eastus
        properties:
          device:
            id: >-
              /subscriptions/subid/resourcegroups/rg/providers/Microsoft.HybridNetwork/devices/testDevice
          managed_application_parameters: {}
          sku_name: testSku
          sku_type: SDWAN
          vendor_name: testVendor
          virtual_network_function_user_configurations:
            - network_interfaces:
                - ip_configurations:
                    - dns_servers: {}
                      gateway: ''
                      ip_address: ''
                      ip_allocation_method: Dynamic
                      ip_version: IPv4
                      subnet: ''
                  mac_address: ''
                  network_interface_name: nic1
                  vm_switch_type: Management
                - ip_configurations:
                    - dns_servers: {}
                      gateway: ''
                      ip_address: ''
                      ip_allocation_method: Dynamic
                      ip_version: IPv4
                      subnet: ''
                  mac_address: DC-97-F8-79-16-7D
                  network_interface_name: nic2
                  vm_switch_type: Wan
              role_name: testRole
              user_data_parameters: {}
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - >-
      The provisioning state of the hybrid network virtual network function
      resource.
  returned: always
  type: str
  sample: null
device:
  description:
    - The reference to the hybrid network device.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
sku_name:
  description:
    - The sku name for the hybrid network virtual network function.
  returned: always
  type: str
  sample: null
sku_type:
  description:
    - The sku type for the hybrid network virtual network function.
  returned: always
  type: str
  sample: null
vendor_name:
  description:
    - The vendor name for the hybrid network virtual network function.
  returned: always
  type: str
  sample: null
service_key:
  description:
    - The service key for the virtual network function resource.
  returned: always
  type: str
  sample: null
vendor_provisioning_state:
  description:
    - The vendor provisioning state for the virtual network function resource.
  returned: always
  type: str
  sample: null
managed_application:
  description:
    - The resource URI of the managed application.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
managed_application_parameters:
  description:
    - The parameters for the managed application.
  returned: always
  type: any
  sample: null
virtual_network_function_user_configurations:
  description:
    - The virtual network function configurations from the user.
  returned: always
  type: list
  sample: null
  contains:
    role_name:
      description:
        - The name of the virtual network function role.
      returned: always
      type: str
      sample: null
    user_data_parameters:
      description:
        - The user data parameters from the customer.
      returned: always
      type: any
      sample: null
    network_interfaces:
      description:
        - The network interface configuration.
      returned: always
      type: list
      sample: null
      contains:
        network_interface_name:
          description:
            - The name of the network interface.
          returned: always
          type: str
          sample: null
        mac_address:
          description:
            - The MAC address of the network interface.
          returned: always
          type: str
          sample: null
        ip_configurations:
          description:
            - A list of IP configurations of the network interface.
          returned: always
          type: list
          sample: null
          contains:
            ip_allocation_method:
              description:
                - IP address allocation method.
              returned: always
              type: str
              sample: null
            ip_address:
              description:
                - The value of the IP address.
              returned: always
              type: str
              sample: null
            subnet:
              description:
                - The value of the subnet.
              returned: always
              type: str
              sample: null
            gateway:
              description:
                - The value of the gateway.
              returned: always
              type: str
              sample: null
            ip_version:
              description:
                - IP address version.
              returned: always
              type: str
              sample: null
            dns_servers:
              description:
                - The list of DNS servers IP addresses.
              returned: always
              type: list
              sample: null
        vm_switch_type:
          description:
            - The type of VM switch
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
    from azure.mgmt.hybrid import HybridNetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualNetworkFunction(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            virtual_network_function_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            device=dict(
                type='dict',
                disposition='/device',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            sku_name=dict(
                type='str',
                disposition='/sku_name'
            ),
            vendor_name=dict(
                type='str',
                disposition='/vendor_name'
            ),
            managed_application_parameters=dict(
                type='any',
                disposition='/managed_application_parameters'
            ),
            virtual_network_function_user_configurations=dict(
                type='list',
                disposition='/virtual_network_function_user_configurations',
                elements='dict',
                options=dict(
                    role_name=dict(
                        type='str',
                        disposition='role_name'
                    ),
                    user_data_parameters=dict(
                        type='any',
                        disposition='user_data_parameters'
                    ),
                    network_interfaces=dict(
                        type='list',
                        disposition='network_interfaces',
                        elements='dict',
                        options=dict(
                            network_interface_name=dict(
                                type='str',
                                disposition='network_interface_name'
                            ),
                            mac_address=dict(
                                type='str',
                                disposition='mac_address'
                            ),
                            ip_configurations=dict(
                                type='list',
                                disposition='ip_configurations',
                                elements='dict',
                                options=dict(
                                    ip_allocation_method=dict(
                                        type='str',
                                        disposition='ip_allocation_method',
                                        choices=['Unknown',
                                                 'Static',
                                                 'Dynamic']
                                    ),
                                    ip_address=dict(
                                        type='str',
                                        disposition='ip_address'
                                    ),
                                    subnet=dict(
                                        type='str',
                                        disposition='subnet'
                                    ),
                                    gateway=dict(
                                        type='str',
                                        disposition='gateway'
                                    ),
                                    ip_version=dict(
                                        type='str',
                                        disposition='ip_version',
                                        choices=['Unknown',
                                                 'IPv4']
                                    ),
                                    dns_servers=dict(
                                        type='list',
                                        disposition='dns_servers',
                                        elements='str'
                                    )
                                )
                            ),
                            vm_switch_type=dict(
                                type='str',
                                disposition='vm_switch_type',
                                choices=['Unknown',
                                         'Management',
                                         'Wan',
                                         'Lan',
                                         'Internal']
                            )
                        )
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
        self.virtual_network_function_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworkFunction, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HybridNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

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
            response = self.mgmt_client.virtual_network_functions.create_or_update(resource_group_name=self.resource_group_name,
                                                                                   virtual_network_function_name=self.virtual_network_function_name,
                                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetworkFunction instance.')
            self.fail('Error creating the VirtualNetworkFunction instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_network_functions.delete(resource_group_name=self.resource_group_name,
                                                                         virtual_network_function_name=self.virtual_network_function_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetworkFunction instance.')
            self.fail('Error deleting the VirtualNetworkFunction instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_network_functions.get(resource_group_name=self.resource_group_name,
                                                                      virtual_network_function_name=self.virtual_network_function_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualNetworkFunction()


if __name__ == '__main__':
    main()
