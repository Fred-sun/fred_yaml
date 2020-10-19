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
module: azure_rm_vendorsku_info
version_added: '2.9'
short_description: Get VendorSku info.
description:
  - Get info of VendorSku.
options:
  vendor_name:
    description:
      - The name of vendor.
      - The name of the vendor.
    required: true
    type: str
  sku_name:
    description:
      - The name of the sku.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get the sku of Vendor resource
      azure_rm_vendorsku_info: 
        sku_name: TestSku
        vendor_name: TestVendor
        

    - name: Lists all the vendor skus of vendor resource
      azure_rm_vendorsku_info: 
        vendor_name: TestVendor
        

'''

RETURN = '''
vendor_skus:
  description: >-
    A list of dict results where the key is the name of the VendorSku and the
    values are the facts for that VendorSku.
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
    provisioning_state:
      description:
        - The provisioning state of the vendor sku sub resource.
      returned: always
      type: str
      sample: null
    sku_type:
      description:
        - Sku type.
      returned: always
      type: str
      sample: null
    deployment_mode:
      description:
        - Sku deployment mode.
      returned: always
      type: str
      sample: null
    preview:
      description:
        - Indicates if the vendor sku is in preview mode.
      returned: always
      type: bool
      sample: null
    managed_application_parameters:
      description:
        - The parameters for the managed application to be supplied by vendor.
      returned: always
      type: any
      sample: null
    managed_application_template:
      description:
        - The template for the managed application deployment.
      returned: always
      type: any
      sample: null
    virutal_network_function_role_configurations:
      description:
        - An array of virtual network function role definitions.
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
        role_type:
          description:
            - Role type.
          returned: always
          type: str
          sample: null
        virtual_machine_size:
          description:
            - The size of the virtual machine.
          returned: always
          type: str
          sample: null
        image_reference:
          description:
            - The definition of image reference.
          returned: always
          type: dict
          sample: null
          contains:
            os_type:
              description:
                - The OS type.
              returned: always
              type: str
              sample: null
            vhd_name:
              description:
                - The VHD name.
              returned: always
              type: str
              sample: null
            vhd_type:
              description:
                - The VHD type.
              returned: always
              type: str
              sample: null
            sas_uri:
              description:
                - The VHD SAS URI.
              returned: always
              type: str
              sample: null
        os_profile:
          description:
            - >-
              Specifies the operating system settings for the role instance.
              This value can be updated during the deployment of virtual network
              function.
          returned: always
          type: dict
          sample: null
          contains:
            admin_username:
              description:
                - >-
                  Specifies the name of the administrator account. <br><br>
                  **Windows-only restriction:** Cannot end in "." <br><br>
                  **Disallowed values:** "administrator", "admin", "user",
                  "user1", "test", "user2", "test1", "user3", "admin1", "1",
                  "123", "a", "actuser", "adm", "admin2", "aspnet", "backup",
                  "console", "david", "guest", "john", "owner", "root",
                  "server", "sql", "support", "support_388945a0", "sys",
                  "test2", "test3", "user4", "user5". <br><br> **Minimum-length
                  (Linux):** 1  character <br><br> **Max-length (Linux):** 64
                  characters <br><br> **Max-length (Windows):** 20 characters 
                  <br><br><li> For root access to the Linux VM, see [Using root
                  privileges on Linux virtual machines in
                  Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)<br><li>
                  For a list of built-in system users on Linux that should not
                  be used in this field, see [Selecting User Names for Linux on
                  Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json).
              returned: always
              type: str
              sample: null
            admin_password:
              description:
                - >-
                  Specifies the password of the administrator account. <br><br>
                  **Minimum-length (Windows):** 8 characters <br><br>
                  **Minimum-length (Linux):** 6 characters <br><br> **Max-length
                  (Windows):** 123 characters <br><br> **Max-length (Linux):**
                  72 characters <br><br> **Complexity requirements:** 3 out of 4
                  conditions below need to be fulfilled <br> Has lower
                  characters <br>Has upper characters <br> Has a digit <br> Has
                  a special character (Regex match [\W_]) <br><br> For resetting
                  the password, see [How to reset the Remote Desktop service or
                  its login password in a Windows
                  VM](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
                  <br><br> For resetting root password, see [Manage users, SSH,
                  and check or repair disks on Azure Linux VMs using the
                  VMAccess
                  Extension](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password).
              returned: always
              type: str
              sample: null
            ssh_public_key:
              description:
                - >-
                  Contains information about SSH certificate public key and the
                  path on the Linux VM where the public key is placed.
              returned: always
              type: str
              sample: null
        user_data_template:
          description:
            - >-
              The user data template for customers. This is json scheme template
              describing the format and data type of user data parameters.
          returned: always
          type: any
          sample: null
        user_data_parameters:
          description:
            - >-
              The user parameters for customers. The format of user data
              parameters has to be matched with the provided user data template.
          returned: always
          type: any
          sample: null
        network_interfaces:
          description:
            - The network interface configurations.
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
        - A list of vendor skus offered by the vendor.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - The provisioning state of the vendor sku sub resource.
          returned: always
          type: str
          sample: null
        sku_type:
          description:
            - Sku type.
          returned: always
          type: str
          sample: null
        deployment_mode:
          description:
            - Sku deployment mode.
          returned: always
          type: str
          sample: null
        preview:
          description:
            - Indicates if the vendor sku is in preview mode.
          returned: always
          type: bool
          sample: null
        managed_application_parameters:
          description:
            - >-
              The parameters for the managed application to be supplied by
              vendor.
          returned: always
          type: any
          sample: null
        managed_application_template:
          description:
            - The template for the managed application deployment.
          returned: always
          type: any
          sample: null
        virutal_network_function_role_configurations:
          description:
            - An array of virtual network function role definitions.
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
            role_type:
              description:
                - Role type.
              returned: always
              type: str
              sample: null
            virtual_machine_size:
              description:
                - The size of the virtual machine.
              returned: always
              type: str
              sample: null
            image_reference:
              description:
                - The definition of image reference.
              returned: always
              type: dict
              sample: null
              contains:
                os_type:
                  description:
                    - The OS type.
                  returned: always
                  type: str
                  sample: null
                vhd_name:
                  description:
                    - The VHD name.
                  returned: always
                  type: str
                  sample: null
                vhd_type:
                  description:
                    - The VHD type.
                  returned: always
                  type: str
                  sample: null
                sas_uri:
                  description:
                    - The VHD SAS URI.
                  returned: always
                  type: str
                  sample: null
            os_profile:
              description:
                - >-
                  Specifies the operating system settings for the role instance.
                  This value can be updated during the deployment of virtual
                  network function.
              returned: always
              type: dict
              sample: null
              contains:
                admin_username:
                  description:
                    - >-
                      Specifies the name of the administrator account. <br><br>
                      **Windows-only restriction:** Cannot end in "." <br><br>
                      **Disallowed values:** "administrator", "admin", "user",
                      "user1", "test", "user2", "test1", "user3", "admin1", "1",
                      "123", "a", "actuser", "adm", "admin2", "aspnet",
                      "backup", "console", "david", "guest", "john", "owner",
                      "root", "server", "sql", "support", "support_388945a0",
                      "sys", "test2", "test3", "user4", "user5". <br><br>
                      **Minimum-length (Linux):** 1  character <br><br>
                      **Max-length (Linux):** 64 characters <br><br>
                      **Max-length (Windows):** 20 characters  <br><br><li> For
                      root access to the Linux VM, see [Using root privileges on
                      Linux virtual machines in
                      Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)<br><li>
                      For a list of built-in system users on Linux that should
                      not be used in this field, see [Selecting User Names for
                      Linux on
                      Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json).
                  returned: always
                  type: str
                  sample: null
                admin_password:
                  description:
                    - >-
                      Specifies the password of the administrator account.
                      <br><br> **Minimum-length (Windows):** 8 characters
                      <br><br> **Minimum-length (Linux):** 6 characters <br><br>
                      **Max-length (Windows):** 123 characters <br><br>
                      **Max-length (Linux):** 72 characters <br><br>
                      **Complexity requirements:** 3 out of 4 conditions below
                      need to be fulfilled <br> Has lower characters <br>Has
                      upper characters <br> Has a digit <br> Has a special
                      character (Regex match [\W_]) <br><br> For resetting the
                      password, see [How to reset the Remote Desktop service or
                      its login password in a Windows
                      VM](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
                      <br><br> For resetting root password, see [Manage users,
                      SSH, and check or repair disks on Azure Linux VMs using
                      the VMAccess
                      Extension](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password).
                  returned: always
                  type: str
                  sample: null
                ssh_public_key:
                  description:
                    - >-
                      Contains information about SSH certificate public key and
                      the path on the Linux VM where the public key is placed.
                  returned: always
                  type: str
                  sample: null
            user_data_template:
              description:
                - >-
                  The user data template for customers. This is json scheme
                  template describing the format and data type of user data
                  parameters.
              returned: always
              type: any
              sample: null
            user_data_parameters:
              description:
                - >-
                  The user parameters for customers. The format of user data
                  parameters has to be matched with the provided user data
                  template.
              returned: always
              type: any
              sample: null
            network_interfaces:
              description:
                - The network interface configurations.
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
        - The URI to get the next set of results.
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


class AzureRMVendorSkuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            vendor_name=dict(
                type='str',
                required=True
            ),
            sku_name=dict(
                type='str'
            )
        )

        self.vendor_name = None
        self.sku_name = None

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
        super(AzureRMVendorSkuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

        if (self.vendor_name is not None and
            self.sku_name is not None):
            self.results['vendor_skus'] = self.format_item(self.get())
        elif (self.vendor_name is not None):
            self.results['vendor_skus'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vendor_skus.get(vendor_name=self.vendor_name,
                                                        sku_name=self.sku_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.vendor_skus.list(vendor_name=self.vendor_name)
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
    AzureRMVendorSkuInfo()


if __name__ == '__main__':
    main()
