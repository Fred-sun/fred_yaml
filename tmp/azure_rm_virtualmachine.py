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
module: azure_rm_virtualmachine
version_added: '2.9'
short_description: Manage Azure VirtualMachine instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachine.'
options:
  resource_group_name:
    description:
      - The name of the resource group
    required: true
    type: str
  virtual_machine_name:
    description:
      - virtual machine name
    required: true
    type: str
  referer:
    description:
      - referer url
    type: str
  location:
    description:
      - Azure region
    type: str
  amount_of_ram:
    description:
      - The amount of memory
    type: integer
  customization:
    description:
      - Virtual machine properties
    type: dict
    suboptions:
      dns_servers:
        description:
          - List of dns servers to use
        type: list
      host_name:
        description:
          - Virtual Machine hostname
        type: str
      password:
        description:
          - Password for login
        type: str
      policy_id:
        description:
          - id of customization policy
        type: str
      username:
        description:
          - Username for login
        type: str
  disks:
    description:
      - The list of Virtual Disks
    type: list
    suboptions:
      controller_id:
        description:
          - Disk's Controller id
        required: true
        type: str
      independence_mode:
        description:
          - Disk's independence mode type
        required: true
        type: sealed-choice
      total_size:
        description:
          - Disk's total size
        required: true
        type: integer
      virtual_disk_id:
        description:
          - Disk's id
        type: str
      virtual_disk_name:
        description:
          - Disk's display name
        type: str
  expose_to_guest_vm:
    description:
      - Expose Guest OS or not
    type: bool
  nics:
    description:
      - The list of Virtual NICs
    type: list
    suboptions:
      customization:
        description:
          - guest OS customization for nic
        type: dict
        suboptions:
          allocation:
            description:
              - IP address allocation method
            type: str
            choices:
              - static
              - dynamic
          dns_servers:
            description:
              - List of dns servers to use
            type: list
          gateway:
            description:
              - Gateway addresses assigned to nic
            type: list
          ip_address:
            description:
              - Static ip address for nic
            type: str
          mask:
            description:
              - Network mask for nic
            type: str
          primary_wins_server:
            description:
              - primary WINS server for Windows
            type: str
          secondary_wins_server:
            description:
              - secondary WINS server for Windows
            type: str
      ip_addresses:
        description:
          - NIC ip address
        type: list
      mac_address:
        description:
          - NIC MAC address
        type: str
      network:
        description:
          - Virtual Network
        required: true
        type: dict
        suboptions:
          assignable:
            description:
              - can be used in vm creation/deletion
            type: bool
          id:
            description:
              - 'virtual network id (privateCloudId:vsphereId)'
            required: true
            type: str
          location:
            description:
              - Azure region
            type: str
          name:
            description:
              - '{VirtualNetworkName}'
            type: str
          type:
            description:
              - '{resourceProviderNamespace}/{resourceType}'
            type: str
          private_cloud_id:
            description:
              - The Private Cloud id
            type: str
      nic_type:
        description:
          - NIC type
        required: true
        type: sealed-choice
      power_on_boot:
        description:
          - Is NIC powered on/off on boot
        type: bool
      virtual_nic_id:
        description:
          - NIC id
        type: str
      virtual_nic_name:
        description:
          - NIC name
        type: str
  number_of_cores:
    description:
      - The number of CPU cores
    type: integer
  password:
    description:
      - Password for login. Deprecated - use customization property
    type: str
  private_cloud_id:
    description:
      - Private Cloud Id
    type: str
  resource_pool:
    description:
      - Virtual Machines Resource Pool
    type: dict
    suboptions:
      id:
        description:
          - 'resource pool id (privateCloudId:vsphereId)'
        required: true
        type: str
      location:
        description:
          - Azure region
        type: str
      name:
        description:
          - '{ResourcePoolName}'
        type: str
      private_cloud_id:
        description:
          - The Private Cloud Id
        type: str
      type:
        description:
          - '{resourceProviderNamespace}/{resourceType}'
        type: str
      full_name:
        description:
          - Hierarchical resource pool name
        type: str
  template_id:
    description:
      - Virtual Machine Template Id
    type: str
  username:
    description:
      - Username for login. Deprecated - use customization property
    type: str
  v_sphere_networks:
    description:
      - The list of Virtual VSphere Networks
    type: list
  state:
    description:
      - Assert the state of the VirtualMachine.
      - >-
        Use C(present) to create or update an VirtualMachine and C(absent) to
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
    - name: CreateVirtualMachine
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        virtual_machine_name: myVirtualMachine
        

    - name: DeleteVirtualMachine
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        virtual_machine_name: myVirtualMachine
        

    - name: PatchVirtualMachine
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        virtual_machine_name: myVirtualMachine
        

'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualMachine(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            virtual_machine_name=dict(
                type='str',
                required=True
            ),
            referer=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            amount_of_ram=dict(
                type='integer',
                disposition='/amount_of_ram'
            ),
            customization=dict(
                type='dict',
                disposition='/customization',
                options=dict(
                    dns_servers=dict(
                        type='list',
                        disposition='dns_servers',
                        elements='str'
                    ),
                    host_name=dict(
                        type='str',
                        disposition='host_name'
                    ),
                    password=dict(
                        type='str',
                        disposition='password'
                    ),
                    policy_id=dict(
                        type='str',
                        disposition='policy_id'
                    ),
                    username=dict(
                        type='str',
                        disposition='username'
                    )
                )
            ),
            disks=dict(
                type='list',
                disposition='/disks',
                elements='dict',
                options=dict(
                    controller_id=dict(
                        type='str',
                        disposition='controller_id',
                        required=True
                    ),
                    independence_mode=dict(
                        type='sealed-choice',
                        disposition='independence_mode',
                        required=True
                    ),
                    total_size=dict(
                        type='integer',
                        disposition='total_size',
                        required=True
                    ),
                    virtual_disk_id=dict(
                        type='str',
                        disposition='virtual_disk_id'
                    ),
                    virtual_disk_name=dict(
                        type='str',
                        updatable=False,
                        disposition='virtual_disk_name'
                    )
                )
            ),
            expose_to_guest_vm=dict(
                type='bool',
                disposition='/expose_to_guest_vm'
            ),
            nics=dict(
                type='list',
                disposition='/nics',
                elements='dict',
                options=dict(
                    customization=dict(
                        type='dict',
                        disposition='customization',
                        options=dict(
                            allocation=dict(
                                type='str',
                                disposition='allocation',
                                choices=['static',
                                         'dynamic']
                            ),
                            dns_servers=dict(
                                type='list',
                                disposition='dns_servers',
                                elements='str'
                            ),
                            gateway=dict(
                                type='list',
                                disposition='gateway',
                                elements='str'
                            ),
                            ip_address=dict(
                                type='str',
                                disposition='ip_address'
                            ),
                            mask=dict(
                                type='str',
                                disposition='mask'
                            ),
                            primary_wins_server=dict(
                                type='str',
                                disposition='primary_wins_server'
                            ),
                            secondary_wins_server=dict(
                                type='str',
                                disposition='secondary_wins_server'
                            )
                        )
                    ),
                    ip_addresses=dict(
                        type='list',
                        disposition='ip_addresses',
                        elements='str'
                    ),
                    mac_address=dict(
                        type='str',
                        disposition='mac_address'
                    ),
                    network=dict(
                        type='dict',
                        disposition='network',
                        required=True,
                        options=dict(
                            assignable=dict(
                                type='bool',
                                updatable=False,
                                disposition='assignable'
                            ),
                            id=dict(
                                type='str',
                                disposition='id',
                                required=True
                            ),
                            location=dict(
                                type='str',
                                updatable=False,
                                disposition='location'
                            ),
                            name=dict(
                                type='str',
                                updatable=False,
                                disposition='name'
                            ),
                            type=dict(
                                type='str',
                                updatable=False,
                                disposition='type'
                            ),
                            private_cloud_id=dict(
                                type='str',
                                updatable=False,
                                disposition='private_cloud_id'
                            )
                        )
                    ),
                    nic_type=dict(
                        type='sealed-choice',
                        disposition='nic_type',
                        required=True
                    ),
                    power_on_boot=dict(
                        type='bool',
                        disposition='power_on_boot'
                    ),
                    virtual_nic_id=dict(
                        type='str',
                        disposition='virtual_nic_id'
                    ),
                    virtual_nic_name=dict(
                        type='str',
                        updatable=False,
                        disposition='virtual_nic_name'
                    )
                )
            ),
            number_of_cores=dict(
                type='integer',
                disposition='/number_of_cores'
            ),
            password=dict(
                type='str',
                disposition='/password'
            ),
            private_cloud_id=dict(
                type='str',
                disposition='/private_cloud_id'
            ),
            resource_pool=dict(
                type='dict',
                disposition='/resource_pool',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id',
                        required=True
                    ),
                    location=dict(
                        type='str',
                        updatable=False,
                        disposition='location'
                    ),
                    name=dict(
                        type='str',
                        updatable=False,
                        disposition='name'
                    ),
                    private_cloud_id=dict(
                        type='str',
                        updatable=False,
                        disposition='private_cloud_id'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    full_name=dict(
                        type='str',
                        updatable=False,
                        disposition='full_name'
                    )
                )
            ),
            template_id=dict(
                type='str',
                disposition='/template_id'
            ),
            username=dict(
                type='str',
                disposition='/username'
            ),
            v_sphere_networks=dict(
                type='list',
                disposition='/v_sphere_networks',
                elements='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.virtual_machine_name = None
        self.referer = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachine, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

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
            response = self.mgmt_client.virtual_machines.create_or_update(resource_group_name=self.resource_group_name,
                                                                          referer=self.referer,
                                                                          virtual_machine_name=self.virtual_machine_name,
                                                                          virtual_machine_request=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachine instance.')
            self.fail('Error creating the VirtualMachine instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machines.delete(resource_group_name=self.resource_group_name,
                                                                referer=self.referer,
                                                                virtual_machine_name=self.virtual_machine_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachine instance.')
            self.fail('Error deleting the VirtualMachine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machines.get(resource_group_name=self.resource_group_name,
                                                             virtual_machine_name=self.virtual_machine_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachine()


if __name__ == '__main__':
    main()
