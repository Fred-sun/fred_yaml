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
module: azure_rm_virtualmachine_info
version_added: '2.9'
short_description: Get VirtualMachine info.
description:
  - Get info of VirtualMachine.
options:
  filter:
    description:
      - The filter to apply on the list operation
    type: str
  top:
    description:
      - The maximum number of record sets to return
    type: integer
  skip_token:
    description:
      - to be used by nextLink implementation
    type: str
  resource_group_name:
    description:
      - The name of the resource group
    type: str
  virtual_machine_name:
    description:
      - virtual machine name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListVirtualMachines
      azure_rm_virtualmachine_info: 
        {}
        

    - name: ListRGVirtualMachines
      azure_rm_virtualmachine_info: 
        resource_group_name: myResourceGroup
        

    - name: GetVirtualMachine
      azure_rm_virtualmachine_info: 
        resource_group_name: myResourceGroup
        virtual_machine_name: myVirtualMachine
        

'''

RETURN = '''
virtual_machines:
  description: >-
    A list of dict results where the key is the name of the VirtualMachine and
    the values are the facts for that VirtualMachine.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of VirtualMachines
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the VirtualMachine list
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName}
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure region
          returned: always
          type: str
          sample: null
        name:
          description:
            - '{virtualMachineName}'
          returned: always
          type: str
          sample: null
        tags:
          description:
            - The list of tags
          returned: always
          type: dictionary
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
          returned: always
          type: str
          sample: null
        amount_of_ram:
          description:
            - The amount of memory
          returned: always
          type: integer
          sample: null
        controllers:
          description:
            - The list of Virtual Disks' Controllers
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Controller's id
              returned: always
              type: str
              sample: null
            name:
              description:
                - The display name of Controller
              returned: always
              type: str
              sample: null
            sub_type:
              description:
                - >-
                  dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALLEL,
                  LSI_PARALLEL, LSI_SAS)
              returned: always
              type: str
              sample: null
            type:
              description:
                - disk controller type (SCSI)
              returned: always
              type: str
              sample: null
        customization:
          description:
            - Virtual machine properties
          returned: always
          type: dict
          sample: null
          contains:
            dns_servers:
              description:
                - List of dns servers to use
              returned: always
              type: list
              sample: null
            host_name:
              description:
                - Virtual Machine hostname
              returned: always
              type: str
              sample: null
            password:
              description:
                - Password for login
              returned: always
              type: str
              sample: null
            policy_id:
              description:
                - id of customization policy
              returned: always
              type: str
              sample: null
            username:
              description:
                - Username for login
              returned: always
              type: str
              sample: null
        disks:
          description:
            - The list of Virtual Disks
          returned: always
          type: list
          sample: null
          contains:
            controller_id:
              description:
                - Disk's Controller id
              returned: always
              type: str
              sample: null
            independence_mode:
              description:
                - Disk's independence mode type
              returned: always
              type: sealed-choice
              sample: null
            total_size:
              description:
                - Disk's total size
              returned: always
              type: integer
              sample: null
            virtual_disk_id:
              description:
                - Disk's id
              returned: always
              type: str
              sample: null
            virtual_disk_name:
              description:
                - Disk's display name
              returned: always
              type: str
              sample: null
        dnsname:
          description:
            - The DNS name of Virtual Machine in VCenter
          returned: always
          type: str
          sample: null
        expose_to_guest_vm:
          description:
            - Expose Guest OS or not
          returned: always
          type: bool
          sample: null
        folder:
          description:
            - The path to virtual machine folder in VCenter
          returned: always
          type: str
          sample: null
        guest_os:
          description:
            - The name of Guest OS
          returned: always
          type: str
          sample: null
        guest_os_type:
          description:
            - The Guest OS type
          returned: always
          type: sealed-choice
          sample: null
        nics:
          description:
            - The list of Virtual NICs
          returned: always
          type: list
          sample: null
          contains:
            customization:
              description:
                - guest OS customization for nic
              returned: always
              type: dict
              sample: null
              contains:
                allocation:
                  description:
                    - IP address allocation method
                  returned: always
                  type: str
                  sample: null
                dns_servers:
                  description:
                    - List of dns servers to use
                  returned: always
                  type: list
                  sample: null
                gateway:
                  description:
                    - Gateway addresses assigned to nic
                  returned: always
                  type: list
                  sample: null
                ip_address:
                  description:
                    - Static ip address for nic
                  returned: always
                  type: str
                  sample: null
                mask:
                  description:
                    - Network mask for nic
                  returned: always
                  type: str
                  sample: null
                primary_wins_server:
                  description:
                    - primary WINS server for Windows
                  returned: always
                  type: str
                  sample: null
                secondary_wins_server:
                  description:
                    - secondary WINS server for Windows
                  returned: always
                  type: str
                  sample: null
            ip_addresses:
              description:
                - NIC ip address
              returned: always
              type: list
              sample: null
            mac_address:
              description:
                - NIC MAC address
              returned: always
              type: str
              sample: null
            network:
              description:
                - Virtual Network
              returned: always
              type: dict
              sample: null
              contains:
                assignable:
                  description:
                    - can be used in vm creation/deletion
                  returned: always
                  type: bool
                  sample: null
                id:
                  description:
                    - 'virtual network id (privateCloudId:vsphereId)'
                  returned: always
                  type: str
                  sample: null
                location:
                  description:
                    - Azure region
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - '{VirtualNetworkName}'
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - '{resourceProviderNamespace}/{resourceType}'
                  returned: always
                  type: str
                  sample: null
                private_cloud_id:
                  description:
                    - The Private Cloud id
                  returned: always
                  type: str
                  sample: null
            nic_type:
              description:
                - NIC type
              returned: always
              type: sealed-choice
              sample: null
            power_on_boot:
              description:
                - Is NIC powered on/off on boot
              returned: always
              type: bool
              sample: null
            virtual_nic_id:
              description:
                - NIC id
              returned: always
              type: str
              sample: null
            virtual_nic_name:
              description:
                - NIC name
              returned: always
              type: str
              sample: null
        number_of_cores:
          description:
            - The number of CPU cores
          returned: always
          type: integer
          sample: null
        password:
          description:
            - Password for login. Deprecated - use customization property
          returned: always
          type: str
          sample: null
        private_cloud_id:
          description:
            - Private Cloud Id
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning status of the resource
          returned: always
          type: str
          sample: null
        public_ip:
          description:
            - The public ip of Virtual Machine
          returned: always
          type: str
          sample: null
        resource_pool:
          description:
            - Virtual Machines Resource Pool
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - 'resource pool id (privateCloudId:vsphereId)'
              returned: always
              type: str
              sample: null
            location:
              description:
                - Azure region
              returned: always
              type: str
              sample: null
            name:
              description:
                - '{ResourcePoolName}'
              returned: always
              type: str
              sample: null
            private_cloud_id:
              description:
                - The Private Cloud Id
              returned: always
              type: str
              sample: null
            type:
              description:
                - '{resourceProviderNamespace}/{resourceType}'
              returned: always
              type: str
              sample: null
            full_name:
              description:
                - Hierarchical resource pool name
              returned: always
              type: str
              sample: null
        status:
          description:
            - The status of Virtual machine
          returned: always
          type: sealed-choice
          sample: null
        template_id:
          description:
            - Virtual Machine Template Id
          returned: always
          type: str
          sample: null
        username:
          description:
            - Username for login. Deprecated - use customization property
          returned: always
          type: str
          sample: null
        v_sphere_networks:
          description:
            - The list of Virtual VSphere Networks
          returned: always
          type: list
          sample: null
        vm_id:
          description:
            - The internal id of Virtual Machine in VCenter
          returned: always
          type: str
          sample: null
        vmwaretools:
          description:
            - VMware tools version
          returned: always
          type: str
          sample: null
    id:
      description:
        - >-
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName}
      returned: always
      type: str
      sample: null
    location:
      description:
        - Azure region
      returned: always
      type: str
      sample: null
    name:
      description:
        - '{virtualMachineName}'
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The list of tags
      returned: always
      type: dictionary
      sample: null
    type:
      description:
        - '{resourceProviderNamespace}/{resourceType}'
      returned: always
      type: str
      sample: null
    amount_of_ram:
      description:
        - The amount of memory
      returned: always
      type: integer
      sample: null
    controllers:
      description:
        - The list of Virtual Disks' Controllers
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Controller's id
          returned: always
          type: str
          sample: null
        name:
          description:
            - The display name of Controller
          returned: always
          type: str
          sample: null
        sub_type:
          description:
            - >-
              dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALLEL,
              LSI_PARALLEL, LSI_SAS)
          returned: always
          type: str
          sample: null
        type:
          description:
            - disk controller type (SCSI)
          returned: always
          type: str
          sample: null
    customization:
      description:
        - Virtual machine properties
      returned: always
      type: dict
      sample: null
      contains:
        dns_servers:
          description:
            - List of dns servers to use
          returned: always
          type: list
          sample: null
        host_name:
          description:
            - Virtual Machine hostname
          returned: always
          type: str
          sample: null
        password:
          description:
            - Password for login
          returned: always
          type: str
          sample: null
        policy_id:
          description:
            - id of customization policy
          returned: always
          type: str
          sample: null
        username:
          description:
            - Username for login
          returned: always
          type: str
          sample: null
    disks:
      description:
        - The list of Virtual Disks
      returned: always
      type: list
      sample: null
      contains:
        controller_id:
          description:
            - Disk's Controller id
          returned: always
          type: str
          sample: null
        independence_mode:
          description:
            - Disk's independence mode type
          returned: always
          type: sealed-choice
          sample: null
        total_size:
          description:
            - Disk's total size
          returned: always
          type: integer
          sample: null
        virtual_disk_id:
          description:
            - Disk's id
          returned: always
          type: str
          sample: null
        virtual_disk_name:
          description:
            - Disk's display name
          returned: always
          type: str
          sample: null
    dnsname:
      description:
        - The DNS name of Virtual Machine in VCenter
      returned: always
      type: str
      sample: null
    expose_to_guest_vm:
      description:
        - Expose Guest OS or not
      returned: always
      type: bool
      sample: null
    folder:
      description:
        - The path to virtual machine folder in VCenter
      returned: always
      type: str
      sample: null
    guest_os:
      description:
        - The name of Guest OS
      returned: always
      type: str
      sample: null
    guest_os_type:
      description:
        - The Guest OS type
      returned: always
      type: sealed-choice
      sample: null
    nics:
      description:
        - The list of Virtual NICs
      returned: always
      type: list
      sample: null
      contains:
        customization:
          description:
            - guest OS customization for nic
          returned: always
          type: dict
          sample: null
          contains:
            allocation:
              description:
                - IP address allocation method
              returned: always
              type: str
              sample: null
            dns_servers:
              description:
                - List of dns servers to use
              returned: always
              type: list
              sample: null
            gateway:
              description:
                - Gateway addresses assigned to nic
              returned: always
              type: list
              sample: null
            ip_address:
              description:
                - Static ip address for nic
              returned: always
              type: str
              sample: null
            mask:
              description:
                - Network mask for nic
              returned: always
              type: str
              sample: null
            primary_wins_server:
              description:
                - primary WINS server for Windows
              returned: always
              type: str
              sample: null
            secondary_wins_server:
              description:
                - secondary WINS server for Windows
              returned: always
              type: str
              sample: null
        ip_addresses:
          description:
            - NIC ip address
          returned: always
          type: list
          sample: null
        mac_address:
          description:
            - NIC MAC address
          returned: always
          type: str
          sample: null
        network:
          description:
            - Virtual Network
          returned: always
          type: dict
          sample: null
          contains:
            assignable:
              description:
                - can be used in vm creation/deletion
              returned: always
              type: bool
              sample: null
            id:
              description:
                - 'virtual network id (privateCloudId:vsphereId)'
              returned: always
              type: str
              sample: null
            location:
              description:
                - Azure region
              returned: always
              type: str
              sample: null
            name:
              description:
                - '{VirtualNetworkName}'
              returned: always
              type: str
              sample: null
            type:
              description:
                - '{resourceProviderNamespace}/{resourceType}'
              returned: always
              type: str
              sample: null
            private_cloud_id:
              description:
                - The Private Cloud id
              returned: always
              type: str
              sample: null
        nic_type:
          description:
            - NIC type
          returned: always
          type: sealed-choice
          sample: null
        power_on_boot:
          description:
            - Is NIC powered on/off on boot
          returned: always
          type: bool
          sample: null
        virtual_nic_id:
          description:
            - NIC id
          returned: always
          type: str
          sample: null
        virtual_nic_name:
          description:
            - NIC name
          returned: always
          type: str
          sample: null
    number_of_cores:
      description:
        - The number of CPU cores
      returned: always
      type: integer
      sample: null
    password:
      description:
        - Password for login. Deprecated - use customization property
      returned: always
      type: str
      sample: null
    private_cloud_id:
      description:
        - Private Cloud Id
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning status of the resource
      returned: always
      type: str
      sample: null
    public_ip:
      description:
        - The public ip of Virtual Machine
      returned: always
      type: str
      sample: null
    resource_pool:
      description:
        - Virtual Machines Resource Pool
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - 'resource pool id (privateCloudId:vsphereId)'
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure region
          returned: always
          type: str
          sample: null
        name:
          description:
            - '{ResourcePoolName}'
          returned: always
          type: str
          sample: null
        private_cloud_id:
          description:
            - The Private Cloud Id
          returned: always
          type: str
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
          returned: always
          type: str
          sample: null
        full_name:
          description:
            - Hierarchical resource pool name
          returned: always
          type: str
          sample: null
    status:
      description:
        - The status of Virtual machine
      returned: always
      type: sealed-choice
      sample: null
    template_id:
      description:
        - Virtual Machine Template Id
      returned: always
      type: str
      sample: null
    username:
      description:
        - Username for login. Deprecated - use customization property
      returned: always
      type: str
      sample: null
    v_sphere_networks:
      description:
        - The list of Virtual VSphere Networks
      returned: always
      type: list
      sample: null
    vm_id:
      description:
        - The internal id of Virtual Machine in VCenter
      returned: always
      type: str
      sample: null
    vmwaretools:
      description:
        - VMware tools version
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
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip_token=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            virtual_machine_name=dict(
                type='str'
            )
        )

        self.filter = None
        self.top = None
        self.skip_token = None
        self.resource_group_name = None
        self.virtual_machine_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.resource_group_name is not None and
            self.virtual_machine_name is not None):
            self.results['virtual_machines'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['virtual_machines'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['virtual_machines'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.get(resource_group_name=self.resource_group_name,
                                                             virtual_machine_name=self.virtual_machine_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                filter=self.filter,
                                                                                top=self.top,
                                                                                skip_token=self.skip_token)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_by_subscription(filter=self.filter,
                                                                              top=self.top,
                                                                              skip_token=self.skip_token)
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
    AzureRMVirtualMachineInfo()


if __name__ == '__main__':
    main()
