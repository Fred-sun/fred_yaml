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
module: azure_rm_vendorvirtualnetworkfunction
version_added: '2.9'
short_description: Manage Azure VendorVirtualNetworkFunction instance.
description:
  - 'Create, update and delete instance of Azure VendorVirtualNetworkFunction.'
options:
  location_name:
    description:
      - >-
        The azure region where the virtual network function sub resource was
        created by customer.
      - >-
        The azure region where the virtual network function resource was created
        by customer.
    required: true
    type: str
  vendor_name:
    description:
      - The name of the vendor.
    required: true
    type: str
  service_key:
    description:
      - The unique GUID for the virtual network function.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  vendor_provisioning_state:
    description:
      - >-
        Vendor controlled provisioning state of the vendor virtual network
        function.
    type: str
    choices:
      - Unknown
      - NotProvisioned
      - Provisioning
      - Provisioned
      - Deprovisioned
      - UserDataValidationFailed
  virtual_network_function_vendor_configurations:
    description:
      - An array of virtual network function vendor configurations.
    type: list
    suboptions:
      role_name:
        description:
          - The name of the virtual network function role.
        type: str
      custom_data:
        description:
          - >-
            Specifies a base-64 encoded string of custom data. The base-64
            encoded string is decoded to a binary array that is saved as a file
            on the virtual machine. The maximum length of the binary array is
            65535 bytes. <br><br> **Note: Do not pass any secrets or passwords
            in customData property** <br><br> This property cannot be updated
            after the VM is created. <br><br> customData is passed to the VM to
            be saved as a file, for more information see [Custom Data on Azure
            VMs](https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/)
            <br><br> For using cloud-init for your Linux VM, see [Using
            cloud-init to customize a Linux VM during
            creation](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)
        type: str
      os_profile:
        description:
          - Specifies the operating system settings for the role instance.
        type: dict
        suboptions:
          admin_username:
            description:
              - >-
                Specifies the name of the administrator account. <br><br>
                **Windows-only restriction:** Cannot end in "." <br><br>
                **Disallowed values:** "administrator", "admin", "user",
                "user1", "test", "user2", "test1", "user3", "admin1", "1",
                "123", "a", "actuser", "adm", "admin2", "aspnet", "backup",
                "console", "david", "guest", "john", "owner", "root", "server",
                "sql", "support", "support_388945a0", "sys", "test2", "test3",
                "user4", "user5". <br><br> **Minimum-length (Linux):** 1 
                character <br><br> **Max-length (Linux):** 64 characters
                <br><br> **Max-length (Windows):** 20 characters  <br><br><li>
                For root access to the Linux VM, see [Using root privileges on
                Linux virtual machines in
                Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)<br><li>
                For a list of built-in system users on Linux that should not be
                used in this field, see [Selecting User Names for Linux on
                Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json).
            type: str
          admin_password:
            description:
              - >-
                Specifies the password of the administrator account. <br><br>
                **Minimum-length (Windows):** 8 characters <br><br>
                **Minimum-length (Linux):** 6 characters <br><br> **Max-length
                (Windows):** 123 characters <br><br> **Max-length (Linux):** 72
                characters <br><br> **Complexity requirements:** 3 out of 4
                conditions below need to be fulfilled <br> Has lower characters
                <br>Has upper characters <br> Has a digit <br> Has a special
                character (Regex match [\W_]) <br><br> For resetting the
                password, see [How to reset the Remote Desktop service or its
                login password in a Windows
                VM](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
                <br><br> For resetting root password, see [Manage users, SSH,
                and check or repair disks on Azure Linux VMs using the VMAccess
                Extension](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password).
            type: str
          ssh_public_key:
            description:
              - >-
                Contains information about SSH certificate public key and the
                path on the Linux VM where the public key is placed.
            type: str
      user_data_parameters:
        description:
          - The user parameters from the customer.
        type: any
      network_interfaces:
        description:
          - The network interface configurations.
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
      - Assert the state of the VendorVirtualNetworkFunction.
      - >-
        Use C(present) to create or update an VendorVirtualNetworkFunction and
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
    - name: Update vendor virtual network function sub resource
      azure_rm_vendorvirtualnetworkfunction: 
        location_name: eastus
        service_key: testServiceKey
        vendor_name: testVendor
        location: eastus
        properties:
          sku_type: SDWAN
          vendor_provisioning_state: Provisioning
          virtual_network_function_vendor_configurations:
            - custom_data: base-64 encoded string of custom data
              network_interfaces:
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
              os_profile:
                admin_password: dummypassword
                admin_username: dummyuser
                ssh_public_key: {}
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
provisioning_state:
  description:
    - >-
      The provisioning state of the vendor virtual network function sub
      resource.
  returned: always
  type: str
  sample: null
vendor_provisioning_state:
  description:
    - >-
      Vendor controlled provisioning state of the vendor virtual network
      function.
  returned: always
  type: str
  sample: null
sku_name:
  description:
    - Name of the sku
  returned: always
  type: str
  sample: null
sku_type:
  description:
    - Sku type.
  returned: always
  type: str
  sample: null
virtual_network_function_vendor_configurations:
  description:
    - An array of virtual network function vendor configurations.
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
    custom_data:
      description:
        - >-
          Specifies a base-64 encoded string of custom data. The base-64 encoded
          string is decoded to a binary array that is saved as a file on the
          virtual machine. The maximum length of the binary array is 65535
          bytes. <br><br> **Note: Do not pass any secrets or passwords in
          customData property** <br><br> This property cannot be updated after
          the VM is created. <br><br> customData is passed to the VM to be saved
          as a file, for more information see [Custom Data on Azure
          VMs](https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/)
          <br><br> For using cloud-init for your Linux VM, see [Using cloud-init
          to customize a Linux VM during
          creation](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)
      returned: always
      type: str
      sample: null
    os_profile:
      description:
        - Specifies the operating system settings for the role instance.
      returned: always
      type: dict
      sample: null
      contains:
        admin_username:
          description:
            - >-
              Specifies the name of the administrator account. <br><br>
              **Windows-only restriction:** Cannot end in "." <br><br>
              **Disallowed values:** "administrator", "admin", "user", "user1",
              "test", "user2", "test1", "user3", "admin1", "1", "123", "a",
              "actuser", "adm", "admin2", "aspnet", "backup", "console",
              "david", "guest", "john", "owner", "root", "server", "sql",
              "support", "support_388945a0", "sys", "test2", "test3", "user4",
              "user5". <br><br> **Minimum-length (Linux):** 1  character
              <br><br> **Max-length (Linux):** 64 characters <br><br>
              **Max-length (Windows):** 20 characters  <br><br><li> For root
              access to the Linux VM, see [Using root privileges on Linux
              virtual machines in
              Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)<br><li>
              For a list of built-in system users on Linux that should not be
              used in this field, see [Selecting User Names for Linux on
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
              (Windows):** 123 characters <br><br> **Max-length (Linux):** 72
              characters <br><br> **Complexity requirements:** 3 out of 4
              conditions below need to be fulfilled <br> Has lower characters
              <br>Has upper characters <br> Has a digit <br> Has a special
              character (Regex match [\W_]) <br><br> For resetting the password,
              see [How to reset the Remote Desktop service or its login password
              in a Windows
              VM](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
              <br><br> For resetting root password, see [Manage users, SSH, and
              check or repair disks on Azure Linux VMs using the VMAccess
              Extension](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password).
          returned: always
          type: str
          sample: null
        ssh_public_key:
          description:
            - >-
              Contains information about SSH certificate public key and the path
              on the Linux VM where the public key is placed.
          returned: always
          type: str
          sample: null
    user_data_parameters:
      description:
        - The user parameters from the customer.
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


class AzureRMVendorVirtualNetworkFunction(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            vendor_name=dict(
                type='str',
                required=True
            ),
            service_key=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            vendor_provisioning_state=dict(
                type='str',
                disposition='/vendor_provisioning_state',
                choices=['Unknown',
                         'NotProvisioned',
                         'Provisioning',
                         'Provisioned',
                         'Deprovisioned',
                         'UserDataValidationFailed']
            ),
            virtual_network_function_vendor_configurations=dict(
                type='list',
                disposition='/virtual_network_function_vendor_configurations',
                elements='dict',
                options=dict(
                    role_name=dict(
                        type='str',
                        disposition='role_name'
                    ),
                    custom_data=dict(
                        type='str',
                        disposition='custom_data'
                    ),
                    os_profile=dict(
                        type='dict',
                        disposition='os_profile',
                        options=dict(
                            admin_username=dict(
                                type='str',
                                disposition='admin_username'
                            ),
                            admin_password=dict(
                                type='str',
                                disposition='admin_password'
                            ),
                            ssh_public_key=dict(
                                type='str',
                                disposition='ssh_public_key'
                            )
                        )
                    ),
                    user_data_parameters=dict(
                        type='any',
                        updatable=False,
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

        self.location_name = None
        self.vendor_name = None
        self.service_key = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVendorVirtualNetworkFunction, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.vendor_virtual_network_functions.create_or_update(location_name=self.location_name,
                                                                                          vendor_name=self.vendor_name,
                                                                                          service_key=self.service_key,
                                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VendorVirtualNetworkFunction instance.')
            self.fail('Error creating the VendorVirtualNetworkFunction instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vendor_virtual_network_functions.delete()
        except CloudError as e:
            self.log('Error attempting to delete the VendorVirtualNetworkFunction instance.')
            self.fail('Error deleting the VendorVirtualNetworkFunction instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vendor_virtual_network_functions.get(location_name=self.location_name,
                                                                             vendor_name=self.vendor_name,
                                                                             service_key=self.service_key)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVendorVirtualNetworkFunction()


if __name__ == '__main__':
    main()
