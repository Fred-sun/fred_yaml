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
module: azure_rm_azurebaremetalinstance
version_added: '2.9'
short_description: Manage Azure AzureBareMetalInstance instance.
description:
  - 'Create, update and delete instance of Azure AzureBareMetalInstance.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  azure_bare_metal_instance_name:
    description:
      - Name of the Azure BareMetal on Azure instance.
    required: true
    type: str
  state:
    description:
      - Assert the state of the AzureBareMetalInstance.
      - >-
        Use C(present) to create or update an AzureBareMetalInstance and
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
    - name: Delete an AzureBareMetal instance
      azure_rm_azurebaremetalinstance: 
        azure_bare_metal_instance_name: myAzureBareMetalInstance
        resource_group_name: myResourceGroup
        

    - name: Delete Tags field of an AzureBareMetal instance
      azure_rm_azurebaremetalinstance: 
        azure_bare_metal_instance_name: myABMInstance
        resource_group_name: myResourceGroup
        

    - name: Update Tags field of an AzureBareMetal instance
      azure_rm_azurebaremetalinstance: 
        azure_bare_metal_instance_name: myABMInstance
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
hardware_profile:
  description:
    - Specifies the hardware settings for the AzureBareMetal instance.
  returned: always
  type: dict
  sample: null
  contains:
    hardware_type:
      description:
        - Name of the hardware type (vendor and/or their product name)
      returned: always
      type: str
      sample: null
    azure_bare_metal_instance_size:
      description:
        - Specifies the AzureBareMetal instance SKU.
      returned: always
      type: str
      sample: null
storage_profile:
  description:
    - Specifies the storage settings for the AzureBareMetal instance disks.
  returned: always
  type: dict
  sample: null
  contains:
    nfs_ip_address:
      description:
        - IP Address to connect to storage.
      returned: always
      type: str
      sample: null
    os_disks:
      description:
        - >-
          Specifies information about the operating system disk used by
          baremetal instance.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The disk name.
          returned: always
          type: str
          sample: null
        disk_size_gb:
          description:
            - Specifies the size of an empty data disk in gigabytes.
          returned: always
          type: integer
          sample: null
        lun:
          description:
            - >-
              Specifies the logical unit number of the data disk. This value is
              used to identify data disks within the VM and therefore must be
              unique for each data disk attached to a VM.
          returned: always
          type: integer
          sample: null
os_profile:
  description:
    - Specifies the operating system settings for the AzureBareMetal instance.
  returned: always
  type: dict
  sample: null
  contains:
    computer_name:
      description:
        - Specifies the host OS name of the AzureBareMetal instance.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - This property allows you to specify the type of the OS.
      returned: always
      type: str
      sample: null
    version:
      description:
        - Specifies version of operating system.
      returned: always
      type: str
      sample: null
    ssh_public_key:
      description:
        - Specifies the SSH public key used to access the operating system.
      returned: always
      type: str
      sample: null
network_profile:
  description:
    - Specifies the network settings for the AzureBareMetal instance.
  returned: always
  type: dict
  sample: null
  contains:
    network_interfaces:
      description:
        - Specifies the network interfaces for the AzureBareMetal instance.
      returned: always
      type: list
      sample: null
      contains:
        ip_address:
          description:
            - Specifies the IP address of the network interface.
          returned: always
          type: str
          sample: null
    circuit_id:
      description:
        - Specifies the circuit id for connecting to express route.
      returned: always
      type: str
      sample: null
azure_bare_metal_instance_id:
  description:
    - Specifies the AzureBareMetal instance unique ID.
  returned: always
  type: str
  sample: null
power_state:
  description:
    - Resource power state
  returned: always
  type: str
  sample: null
proximity_placement_group:
  description:
    - Resource proximity placement group
  returned: always
  type: str
  sample: null
hw_revision:
  description:
    - Hardware revision of an AzureBareMetal instance
  returned: always
  type: str
  sample: null
partner_node_id:
  description:
    - >-
      ARM ID of another AzureBareMetalInstance that will share a network with
      this AzureBareMetalInstance
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - State of provisioning of the AzureBareMetalInstance
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
    from azure.mgmt.bare import bareMetalInfrastructureClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAzureBareMetalInstance(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            azure_bare_metal_instance_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.azure_bare_metal_instance_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAzureBareMetalInstance, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(bareMetalInfrastructureClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-06-preview')

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
                response = self.mgmt_client.azure_bare_metal_instances.create()
            else:
                response = self.mgmt_client.azure_bare_metal_instances.update(resource_group_name=self.resource_group_name,
                                                                              azure_bare_metal_instance_name=self.azure_bare_metal_instance_name,
                                                                              tags_parameter=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AzureBareMetalInstance instance.')
            self.fail('Error creating the AzureBareMetalInstance instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.azure_bare_metal_instances.delete(resource_group_name=self.resource_group_name,
                                                                          azure_bare_metal_instance_name=self.azure_bare_metal_instance_name)
        except CloudError as e:
            self.log('Error attempting to delete the AzureBareMetalInstance instance.')
            self.fail('Error deleting the AzureBareMetalInstance instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.azure_bare_metal_instances.get(resource_group_name=self.resource_group_name,
                                                                       azure_bare_metal_instance_name=self.azure_bare_metal_instance_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAzureBareMetalInstance()


if __name__ == '__main__':
    main()
