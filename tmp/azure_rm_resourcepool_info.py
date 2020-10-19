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
module: azure_rm_resourcepool_info
version_added: '2.9'
short_description: Get ResourcePool info.
description:
  - Get info of ResourcePool.
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
      - resource pool id (vsphereId)
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListResourcePools
      azure_rm_resourcepool_info: 
        pc_name: myPrivateCloud
        region_id: westus2
        

    - name: GetResourcePool
      azure_rm_resourcepool_info: 
        pc_name: myPrivateCloud
        region_id: westus2
        resource_pool_name: resgroup-26
        

'''

RETURN = '''
resource_pools:
  description: >-
    A list of dict results where the key is the name of the ResourcePool and the
    values are the facts for that ResourcePool.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of ResourcePoolsList
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the Resource pools list
      returned: always
      type: list
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


class AzureRMResourcePoolInfo(AzureRMModuleBase):
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
            )
        )

        self.region_id = None
        self.pc_name = None
        self.resource_pool_name = None

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
        super(AzureRMResourcePoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.region_id is not None and
            self.pc_name is not None and
            self.resource_pool_name is not None):
            self.results['resource_pools'] = self.format_item(self.get())
        elif (self.region_id is not None and
              self.pc_name is not None):
            self.results['resource_pools'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.resource_pools.get(region_id=self.region_id,
                                                           pc_name=self.pc_name,
                                                           resource_pool_name=self.resource_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.resource_pools.list(region_id=self.region_id,
                                                            pc_name=self.pc_name)
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
    AzureRMResourcePoolInfo()


if __name__ == '__main__':
    main()
