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
module: azure_rm_instancepool_info
version_added: '2.9'
short_description: Get InstancePool info.
description:
  - Get info of InstancePool.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
  instance_pool_name:
    description:
      - The name of the instance pool to be retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an instance pool
      azure_rm_instancepool_info: 
        instance_pool_name: testIP
        resource_group_name: group1
        

    - name: List instance pools by resource group
      azure_rm_instancepool_info: 
        resource_group_name: group1
        

    - name: List instance pools in the subscription
      azure_rm_instancepool_info: 
        {}
        

'''

RETURN = '''
instance_pools:
  description: >-
    A list of dict results where the key is the name of the InstancePool and the
    values are the facts for that InstancePool.
  returned: always
  type: complex
  contains:
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
    sku:
      description:
        - The name and tier of the SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
          returned: always
          type: str
          sample: null
        tier:
          description:
            - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
          returned: always
          type: str
          sample: null
        size:
          description:
            - Size of the particular SKU
          returned: always
          type: str
          sample: null
        family:
          description:
            - >-
              If the service has different generations of hardware, for the same
              SKU, then that can be captured here.
          returned: always
          type: str
          sample: null
        capacity:
          description:
            - Capacity of the particular SKU.
          returned: always
          type: integer
          sample: null
    subnet_id:
      description:
        - Resource ID of the subnet to place this instance pool in.
      returned: always
      type: str
      sample: null
    v_cores:
      description:
        - Count of vCores belonging to this instance pool.
      returned: always
      type: integer
      sample: null
    license_type:
      description:
        - >-
          The license type. Possible values are 'LicenseIncluded' (price for SQL
          license is included) and 'BasePrice' (without SQL license price).
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - The name and tier of the SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the SKU, typically, a letter + Number code, e.g.
                  P3.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - >-
                  The tier or edition of the particular SKU, e.g. Basic,
                  Premium.
              returned: always
              type: str
              sample: null
            size:
              description:
                - Size of the particular SKU
              returned: always
              type: str
              sample: null
            family:
              description:
                - >-
                  If the service has different generations of hardware, for the
                  same SKU, then that can be captured here.
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - Capacity of the particular SKU.
              returned: always
              type: integer
              sample: null
        subnet_id:
          description:
            - Resource ID of the subnet to place this instance pool in.
          returned: always
          type: str
          sample: null
        v_cores:
          description:
            - Count of vCores belonging to this instance pool.
          returned: always
          type: integer
          sample: null
        license_type:
          description:
            - >-
              The license type. Possible values are 'LicenseIncluded' (price for
              SQL license is included) and 'BasePrice' (without SQL license
              price).
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMInstancePoolInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            instance_pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.instance_pool_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMInstancePoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.resource_group_name is not None and
            self.instance_pool_name is not None):
            self.results['instance_pools'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['instance_pools'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['instance_pools'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.instance_pools.get(resource_group_name=self.resource_group_name,
                                                           instance_pool_name=self.instance_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.instance_pools.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.instance_pools.list()
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
    AzureRMInstancePoolInfo()


if __name__ == '__main__':
    main()
