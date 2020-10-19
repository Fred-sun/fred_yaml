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
module: azure_rm_pool_info
version_added: '2.9'
short_description: Get Pool info.
description:
  - Get info of Pool.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the NetApp account
    required: true
    type: str
  pool_name:
    description:
      - The name of the capacity pool
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Pools_List
      azure_rm_pool_info: 
        account_name: account1
        resource_group_name: myRG
        

    - name: Pools_Get
      azure_rm_pool_info: 
        account_name: account1
        pool_name: pool1
        resource_group_name: myRG
        

'''

RETURN = '''
pools:
  description: >-
    A list of dict results where the key is the name of the Pool and the values
    are the facts for that Pool.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Capacity pools
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags
          returned: always
          type: dictionary
          sample: null
        pool_id:
          description:
            - UUID v4 used to identify the Pool
          returned: always
          type: str
          sample: null
        size:
          description:
            - >-
              Provisioned size of the pool (in bytes). Allowed values are in
              4TiB chunks (value must be multiply of 4398046511104).
          returned: always
          type: integer
          sample: null
        service_level:
          description:
            - The service level of the file system
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Azure lifecycle management
          returned: always
          type: str
          sample: null
        total_throughput_mibps:
          description:
            - Total throughput of pool in Mibps
          returned: always
          type: number
          sample: null
        utilized_throughput_mibps:
          description:
            - Utilized throughput of pool in Mibps
          returned: always
          type: number
          sample: null
        qos_type:
          description:
            - The qos type of the pool
          returned: always
          type: str
          sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    pool_id:
      description:
        - UUID v4 used to identify the Pool
      returned: always
      type: str
      sample: null
    size:
      description:
        - >-
          Provisioned size of the pool (in bytes). Allowed values are in 4TiB
          chunks (value must be multiply of 4398046511104).
      returned: always
      type: integer
      sample: null
    service_level:
      description:
        - The service level of the file system
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Azure lifecycle management
      returned: always
      type: str
      sample: null
    total_throughput_mibps:
      description:
        - Total throughput of pool in Mibps
      returned: always
      type: number
      sample: null
    utilized_throughput_mibps:
      description:
        - Utilized throughput of pool in Mibps
      returned: always
      type: number
      sample: null
    qos_type:
      description:
        - The qos type of the pool
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
    from azure.mgmt.net import NetAppManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPoolInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.pool_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetAppManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.pool_name is not None):
            self.results['pools'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['pools'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.pools.get(resource_group_name=self.resource_group_name,
                                                  account_name=self.account_name,
                                                  pool_name=self.pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.pools.list(resource_group_name=self.resource_group_name,
                                                   account_name=self.account_name)
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
    AzureRMPoolInfo()


if __name__ == '__main__':
    main()
