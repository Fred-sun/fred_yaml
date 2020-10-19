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
module: azure_rm_virtualnetwork_info
version_added: '2.9'
short_description: Get VirtualNetwork info.
description:
  - Get info of VirtualNetwork.
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
  resource_pool_name:
    description:
      - >-
        Resource pool used to derive vSphere cluster which contains virtual
        networks
    type: str
  virtual_network_name:
    description:
      - virtual network id (vsphereId)
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListVirtualNetworks
      azure_rm_virtualnetwork_info: 
        pc_name: myPrivateCloud
        region_id: westus2
        resource_pool_name: >-
          /subscriptions/{subscription-id}/providers/Microsoft.VMwareCloudSimple/locations/westus2/privateClouds/myPrivateCloud/resourcePools/resgroup-26
        

    - name: GetVirtualNetwork
      azure_rm_virtualnetwork_info: 
        pc_name: myPrivateCloud
        region_id: westus2
        virtual_network_name: dvportgroup-19
        

'''

RETURN = '''
virtual_networks:
  description: >-
    A list of dict results where the key is the name of the VirtualNetwork and
    the values are the facts for that VirtualNetwork.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of VirtualNetwork
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the VirtualNetwork list
      returned: always
      type: list
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


class AzureRMVirtualNetworkInfo(AzureRMModuleBase):
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
            resource_pool_name=dict(
                type='str'
            ),
            virtual_network_name=dict(
                type='str'
            )
        )

        self.region_id = None
        self.pc_name = None
        self.resource_pool_name = None
        self.virtual_network_name = None

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
        super(AzureRMVirtualNetworkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.region_id is not None and
            self.pc_name is not None and
            self.resource_pool_name is not None):
            self.results['virtual_networks'] = self.format_item(self.list())
        elif (self.region_id is not None and
              self.pc_name is not None and
              self.virtual_network_name is not None):
            self.results['virtual_networks'] = self.format_item(self.get())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_networks.list(region_id=self.region_id,
                                                              pc_name=self.pc_name,
                                                              resource_pool_name=self.resource_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_networks.get(region_id=self.region_id,
                                                             pc_name=self.pc_name,
                                                             virtual_network_name=self.virtual_network_name)
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
    AzureRMVirtualNetworkInfo()


if __name__ == '__main__':
    main()
