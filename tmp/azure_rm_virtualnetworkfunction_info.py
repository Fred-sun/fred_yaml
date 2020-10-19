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
module: azure_rm_virtualnetworkfunction_info
version_added: '2.9'
short_description: Get VirtualNetworkFunction info.
description:
  - Get info of VirtualNetworkFunction.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  virtual_network_function_name:
    description:
      - The name of hybrid network virtual network function resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get hybrid network virtual network function resource
      azure_rm_virtualnetworkfunction_info: 
        resource_group_name: rg
        virtual_network_function_name: testVnf
        

    - name: List all hybrid network virtual network function resources in subscription.
      azure_rm_virtualnetworkfunction_info: 
        {}
        

    - name: List hybrid network virtual network function in resource group
      azure_rm_virtualnetworkfunction_info: 
        resource_group_name: rg
        

'''

RETURN = '''
virtual_network_functions:
  description: >-
    A list of dict results where the key is the name of the
    VirtualNetworkFunction and the values are the facts for that
    VirtualNetworkFunction.
  returned: always
  type: complex
  contains:
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
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
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
        - >-
          The vendor provisioning state for the virtual network function
          resource.
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
    value:
      description:
        - >-
          A list of hybrid network virtual network function resources in a
          subscription or resource group.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - >-
              A unique read-only string that changes whenever the resource is
              updated.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the hybrid network virtual network
              function resource.
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
            - >-
              The vendor provisioning state for the virtual network function
              resource.
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
    next_link:
      description:
        - The URL to get the next set of results.
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
    from azure.mgmt.hybrid import HybridNetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualNetworkFunctionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            virtual_network_function_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.virtual_network_function_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualNetworkFunctionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

        if (self.resource_group_name is not None and
            self.virtual_network_function_name is not None):
            self.results['virtual_network_functions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['virtual_network_functions'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['virtual_network_functions'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_functions.get(resource_group_name=self.resource_group_name,
                                                                      virtual_network_function_name=self.virtual_network_function_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_functions.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_functions.list_by_subscription()
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
    AzureRMVirtualNetworkFunctionInfo()


if __name__ == '__main__':
    main()
