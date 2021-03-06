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
module: azure_rm_virtualmachinetemplate_info
version_added: '2.9'
short_description: Get VirtualMachineTemplate info.
description:
  - Get info of VirtualMachineTemplate.
options:
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  resource_pool_name:
    description:
      - Resource pool used to derive vSphere cluster which contains VM templates
    type: str
  virtual_machine_template_name:
    description:
      - virtual machine template id (vsphereId)
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListVirtualMachineTemplates
      azure_rm_virtualmachinetemplate_info: 
        pc_name: myPrivateCloud
        region_id: westus2
        resource_pool_name: >-
          /subscriptions/{subscription-id}/providers/Microsoft.VMwareCloudSimple/locations/westus2/privateClouds/myPrivateCloud/resourcePools/resgroup-26
        

    - name: GetVirtualMachineTemplate
      azure_rm_virtualmachinetemplate_info: 
        pc_name: myPrivateCloud
        region_id: westus2
        virtual_machine_template_name: vm-34
        

'''

RETURN = '''
virtual_machine_templates:
  description: >-
    A list of dict results where the key is the name of the
    VirtualMachineTemplate and the values are the facts for that
    VirtualMachineTemplate.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of VirtualMachineTemplate
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the VM template list
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - 'virtual machine template id (privateCloudId:vsphereId)'
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
            - '{virtualMachineTemplateName}'
          returned: always
          type: str
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
            - The list of Virtual Disk Controllers
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
        description:
          description:
            - The description of Virtual Machine Template
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
        expose_to_guest_vm:
          description:
            - Expose Guest OS or not
          returned: always
          type: bool
          sample: null
        guest_os:
          description:
            - The Guest OS
          returned: always
          type: str
          sample: null
        guest_os_type:
          description:
            - The Guest OS types
          returned: always
          type: str
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
        path:
          description:
            - path to folder
          returned: always
          type: str
          sample: null
        private_cloud_id:
          description:
            - The Private Cloud Id
          returned: always
          type: str
          sample: null
        v_sphere_networks:
          description:
            - The list of VSphere networks
          returned: always
          type: list
          sample: null
        v_sphere_tags:
          description:
            - The tags from VSphere
          returned: always
          type: list
          sample: null
        vmwaretools:
          description:
            - The VMware tools version
          returned: always
          type: str
          sample: null
    id:
      description:
        - 'virtual machine template id (privateCloudId:vsphereId)'
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
        - '{virtualMachineTemplateName}'
      returned: always
      type: str
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
        - The list of Virtual Disk Controllers
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
    description:
      description:
        - The description of Virtual Machine Template
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
    expose_to_guest_vm:
      description:
        - Expose Guest OS or not
      returned: always
      type: bool
      sample: null
    guest_os:
      description:
        - The Guest OS
      returned: always
      type: str
      sample: null
    guest_os_type:
      description:
        - The Guest OS types
      returned: always
      type: str
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
    path:
      description:
        - path to folder
      returned: always
      type: str
      sample: null
    private_cloud_id:
      description:
        - The Private Cloud Id
      returned: always
      type: str
      sample: null
    v_sphere_networks:
      description:
        - The list of VSphere networks
      returned: always
      type: list
      sample: null
    v_sphere_tags:
      description:
        - The tags from VSphere
      returned: always
      type: list
      sample: null
    vmwaretools:
      description:
        - The VMware tools version
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


class AzureRMVirtualMachineTemplateInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            pc_name=dict(
                type='str',
                required=True
            ),
            region_id=dict(
                type='str',
                required=True
            ),
            resource_pool_name=dict(
                type='str'
            ),
            virtual_machine_template_name=dict(
                type='str'
            )
        )

        self.pc_name = None
        self.region_id = None
        self.resource_pool_name = None
        self.virtual_machine_template_name = None

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
        super(AzureRMVirtualMachineTemplateInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.pc_name is not None and
            self.region_id is not None and
            self.resource_pool_name is not None):
            self.results['virtual_machine_templates'] = self.format_item(self.list())
        elif (self.region_id is not None and
              self.pc_name is not None and
              self.virtual_machine_template_name is not None):
            self.results['virtual_machine_templates'] = self.format_item(self.get())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_templates.list(pc_name=self.pc_name,
                                                                       region_id=self.region_id,
                                                                       resource_pool_name=self.resource_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_templates.get(region_id=self.region_id,
                                                                      pc_name=self.pc_name,
                                                                      virtual_machine_template_name=self.virtual_machine_template_name)
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
    AzureRMVirtualMachineTemplateInfo()


if __name__ == '__main__':
    main()
