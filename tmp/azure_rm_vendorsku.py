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
module: azure_rm_vendorsku
version_added: '2.9'
short_description: Manage Azure VendorSku instance.
description:
  - 'Create, update and delete instance of Azure VendorSku.'
options:
  vendor_name:
    description:
      - The name of the vendor.
      - The name of vendor.
    required: true
    type: str
  sku_name:
    description:
      - The name of the sku.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  sku_type:
    description:
      - Sku type.
    type: str
    choices:
      - Unknown
      - EvolvedPacketCore
      - SDWAN
  deployment_mode:
    description:
      - Sku deployment mode.
    type: str
    choices:
      - Unknown
      - Azure
      - PrivateEdgeZone
  preview:
    description:
      - Indicates if the vendor sku is in preview mode.
    type: bool
  managed_application_parameters:
    description:
      - The parameters for the managed application to be supplied by vendor.
    type: any
  managed_application_template:
    description:
      - The template for the managed application deployment.
    type: any
  virutal_network_function_role_configurations:
    description:
      - An array of virtual network function role definitions.
    type: list
    suboptions:
      role_name:
        description:
          - The name of the virtual network function role.
        type: str
      role_type:
        description:
          - Role type.
        type: str
        choices:
          - Unknown
          - VirtualMachine
      virtual_machine_size:
        description:
          - The size of the virtual machine.
        type: str
        choices:
          - Unknown
          - Standard_D1_v2
          - Standard_D2_v2
          - Standard_D3_v2
          - Standard_D4_v2
          - Standard_D5_v2
          - Standard_D11_v2
          - Standard_D12_v2
          - Standard_D13_v2
          - Standard_DS1_v2
          - Standard_DS2_v2
          - Standard_DS3_v2
          - Standard_DS4_v2
          - Standard_DS5_v2
          - Standard_DS11_v2
          - Standard_DS12_v2
          - Standard_DS13_v2
      image_reference:
        description:
          - The definition of image reference.
        type: dict
        suboptions:
          os_type:
            description:
              - The OS type.
            type: str
            choices:
              - Unknown
              - Windows
              - Linux
          vhd_name:
            description:
              - The VHD name.
            type: str
          vhd_type:
            description:
              - The VHD type.
            type: str
            choices:
              - Unknown
              - VHD
              - VHDX
          sas_uri:
            description:
              - The VHD SAS URI.
            type: str
      os_profile:
        description:
          - >-
            Specifies the operating system settings for the role instance. This
            value can be updated during the deployment of virtual network
            function.
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
      user_data_template:
        description:
          - >-
            The user data template for customers. This is json scheme template
            describing the format and data type of user data parameters.
        type: any
      user_data_parameters:
        description:
          - >-
            The user parameters for customers. The format of user data
            parameters has to be matched with the provided user data template.
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
      - Assert the state of the VendorSku.
      - >-
        Use C(present) to create or update an VendorSku and C(absent) to delete
        it.
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
    - name: Delete the sku of vendor resource
      azure_rm_vendorsku: 
        sku_name: TestSku
        vendor_name: TestVendor
        

    - name: Create or update the sku of Vendor resource
      azure_rm_vendorsku: 
        sku_name: TestSku
        vendor_name: TestVendor
        properties:
          deployment_mode: PrivateEdgeZone
          managed_application_template: {}
          preview: true
          virtual_network_function_template:
            virutal_network_function_role_configurations:
              - image_reference:
                  os_type: Linux
                  sas_uri: >-
                    https://<yourstorage>.blob.core.windows.net/<yourcontainer>/<yourfile>?sp=rl&st=st>Z&se=<se>Z&sv=<sv>&sr=b&sig=<signature>
                  vhd_name: vhdName
                  vhd_type: VHD
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
                    vm_switch_type: Wan
                  - ip_configurations:
                      - dns_servers: {}
                        gateway: ''
                        ip_address: ''
                        ip_allocation_method: Dynamic
                        ip_version: IPv4
                        subnet: ''
                    mac_address: ''
                    network_interface_name: nic2
                    vm_switch_type: Management
                os_profile:
                  admin_password: dummypassword
                  admin_username: dummyuser
                  ssh_public_key: {}
                role_name: test
                role_type: VirtualMachine
                virtual_machine_size: Standard_D3_v2
        

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
          Specifies the operating system settings for the role instance. This
          value can be updated during the deployment of virtual network
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
          The user parameters for customers. The format of user data parameters
          has to be matched with the provided user data template.
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


class AzureRMVendorSku(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            vendor_name=dict(
                type='str',
                required=True
            ),
            sku_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku_type=dict(
                type='str',
                disposition='/sku_type',
                choices=['Unknown',
                         'EvolvedPacketCore',
                         'SDWAN']
            ),
            deployment_mode=dict(
                type='str',
                disposition='/deployment_mode',
                choices=['Unknown',
                         'Azure',
                         'PrivateEdgeZone']
            ),
            preview=dict(
                type='bool',
                disposition='/preview'
            ),
            managed_application_parameters=dict(
                type='any',
                disposition='/managed_application_parameters'
            ),
            managed_application_template=dict(
                type='any',
                disposition='/managed_application_template'
            ),
            virutal_network_function_role_configurations=dict(
                type='list',
                disposition='/virutal_network_function_role_configurations',
                elements='dict',
                options=dict(
                    role_name=dict(
                        type='str',
                        disposition='role_name'
                    ),
                    role_type=dict(
                        type='str',
                        disposition='role_type',
                        choices=['Unknown',
                                 'VirtualMachine']
                    ),
                    virtual_machine_size=dict(
                        type='str',
                        disposition='virtual_machine_size',
                        choices=['Unknown',
                                 'Standard_D1_v2',
                                 'Standard_D2_v2',
                                 'Standard_D3_v2',
                                 'Standard_D4_v2',
                                 'Standard_D5_v2',
                                 'Standard_D11_v2',
                                 'Standard_D12_v2',
                                 'Standard_D13_v2',
                                 'Standard_DS1_v2',
                                 'Standard_DS2_v2',
                                 'Standard_DS3_v2',
                                 'Standard_DS4_v2',
                                 'Standard_DS5_v2',
                                 'Standard_DS11_v2',
                                 'Standard_DS12_v2',
                                 'Standard_DS13_v2']
                    ),
                    image_reference=dict(
                        type='dict',
                        disposition='image_reference',
                        options=dict(
                            os_type=dict(
                                type='str',
                                disposition='os_type',
                                choices=['Unknown',
                                         'Windows',
                                         'Linux']
                            ),
                            vhd_name=dict(
                                type='str',
                                disposition='vhd_name'
                            ),
                            vhd_type=dict(
                                type='str',
                                disposition='vhd_type',
                                choices=['Unknown',
                                         'VHD',
                                         'VHDX']
                            ),
                            sas_uri=dict(
                                type='str',
                                disposition='sas_uri'
                            )
                        )
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
                    user_data_template=dict(
                        type='any',
                        disposition='user_data_template'
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

        self.vendor_name = None
        self.sku_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVendorSku, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.vendor_skus.create_or_update(vendor_name=self.vendor_name,
                                                                     sku_name=self.sku_name,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VendorSku instance.')
            self.fail('Error creating the VendorSku instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vendor_skus.delete(vendor_name=self.vendor_name,
                                                           sku_name=self.sku_name)
        except CloudError as e:
            self.log('Error attempting to delete the VendorSku instance.')
            self.fail('Error deleting the VendorSku instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vendor_skus.get(vendor_name=self.vendor_name,
                                                        sku_name=self.sku_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVendorSku()


if __name__ == '__main__':
    main()
