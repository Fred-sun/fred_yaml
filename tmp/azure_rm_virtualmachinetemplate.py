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
module: azure_rm_virtualmachinetemplate
version_added: '2.9'
short_description: Manage Azure VirtualMachineTemplate instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineTemplate.'
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  virtual_machine_template_name:
    description:
      - virtual machine template id (vsphereId)
    required: true
    type: str
  state:
    description:
      - Assert the state of the VirtualMachineTemplate.
      - >-
        Use C(present) to create or update an VirtualMachineTemplate and
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
'''

RETURN = '''
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


class AzureRMVirtualMachineTemplate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=True
            ),
            pc_name=dict(
                type='str',
                required=True
            ),
            virtual_machine_template_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.region_id = None
        self.pc_name = None
        self.virtual_machine_template_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineTemplate, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.virtual_machine_templates.create()
            else:
                response = self.mgmt_client.virtual_machine_templates.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineTemplate instance.')
            self.fail('Error creating the VirtualMachineTemplate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_templates.delete()
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineTemplate instance.')
            self.fail('Error deleting the VirtualMachineTemplate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_templates.get(region_id=self.region_id,
                                                                      pc_name=self.pc_name,
                                                                      virtual_machine_template_name=self.virtual_machine_template_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineTemplate()


if __name__ == '__main__':
    main()
