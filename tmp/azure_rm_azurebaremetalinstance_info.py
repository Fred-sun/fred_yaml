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
module: azure_rm_azurebaremetalinstance_info
version_added: '2.9'
short_description: Get AzureBareMetalInstance info.
description:
  - Get info of AzureBareMetalInstance.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  azure_bare_metal_instance_name:
    description:
      - Name of the Azure BareMetal on Azure instance.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all AzureBareMetal instances in a subscription
      azure_rm_azurebaremetalinstance_info: 
        {}
        

    - name: List all AzureBareMetal instances in a resource group
      azure_rm_azurebaremetalinstance_info: 
        resource_group_name: myResourceGroup
        

    - name: Get an AzureBareMetal instance
      azure_rm_azurebaremetalinstance_info: 
        azure_bare_metal_instance_name: myAzureBareMetalInstance
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
azure_bare_metal_instances:
  description: >-
    A list of dict results where the key is the name of the
    AzureBareMetalInstance and the values are the facts for that
    AzureBareMetalInstance.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of Azure BareMetal instances.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              Specifies the storage settings for the AzureBareMetal instance
              disks.
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
                      Specifies the logical unit number of the data disk. This
                      value is used to identify data disks within the VM and
                      therefore must be unique for each data disk attached to a
                      VM.
                  returned: always
                  type: integer
                  sample: null
        os_profile:
          description:
            - >-
              Specifies the operating system settings for the AzureBareMetal
              instance.
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
                - >-
                  Specifies the SSH public key used to access the operating
                  system.
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
                - >-
                  Specifies the network interfaces for the AzureBareMetal
                  instance.
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
              ARM ID of another AzureBareMetalInstance that will share a network
              with this AzureBareMetalInstance
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - State of provisioning of the AzureBareMetalInstance
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of AzureBareMetal instances.
      returned: always
      type: str
      sample: null
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
                  Specifies the logical unit number of the data disk. This value
                  is used to identify data disks within the VM and therefore
                  must be unique for each data disk attached to a VM.
              returned: always
              type: integer
              sample: null
    os_profile:
      description:
        - >-
          Specifies the operating system settings for the AzureBareMetal
          instance.
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
          ARM ID of another AzureBareMetalInstance that will share a network
          with this AzureBareMetalInstance
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.bare import bareMetalInfrastructureClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAzureBareMetalInstanceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            azure_bare_metal_instance_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.azure_bare_metal_instance_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-08-06-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAzureBareMetalInstanceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(bareMetalInfrastructureClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-06-preview')

        if (self.resource_group_name is not None and
            self.azure_bare_metal_instance_name is not None):
            self.results['azure_bare_metal_instances'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['azure_bare_metal_instances'] = self.format_item(self.list())
        else:
            self.results['azure_bare_metal_instances'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.azure_bare_metal_instances.get(resource_group_name=self.resource_group_name,
                                                                       azure_bare_metal_instance_name=self.azure_bare_metal_instance_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.azure_bare_metal_instances.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.azure_bare_metal_instances.list_by_subscription()
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
    AzureRMAzureBareMetalInstanceInfo()


if __name__ == '__main__':
    main()
