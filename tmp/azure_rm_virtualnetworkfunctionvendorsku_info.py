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
module: azure_rm_virtualnetworkfunctionvendorsku_info
version_added: '2.9'
short_description: Get VirtualNetworkFunctionVendorSku info.
description:
  - Get info of VirtualNetworkFunctionVendorSku.
options:
  vendor_name:
    description:
      - The name of the hybrid network virtual network function vendor.
    required: true
    type: str
  vendor_sku_name:
    description:
      - The name of the hybrid network virtual network function sku.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List hybrid network vendors and skus.
      azure_rm_virtualnetworkfunctionvendorsku_info: 
        vendor_name: testVendor
        

    - name: Get virtual network function sku details
      azure_rm_virtualnetworkfunctionvendorsku_info: 
        vendor_name: testVendor
        vendor_sku_name: testSku
        

'''

RETURN = '''
virtual_network_function_vendor_skus:
  description: >-
    A list of dict results where the key is the name of the
    VirtualNetworkFunctionVendorSku and the values are the facts for that
    VirtualNetworkFunctionVendorSku.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          The virtual network function vendor sku overview properties.
          The virtual network function sku role details.
      returned: always
      type: list
      sample: null
      contains:
        sku_name:
          description:
            - The vendor sku name.
          returned: always
          type: str
          sample: null
        sku_type:
          description:
            - The vendor sku type.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of results.
      returned: always
      type: str
      sample: null
    sku_type:
      description:
        - The virtual network function sku type.
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
    from azure.mgmt.hybrid import HybridNetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualNetworkFunctionVendorSkuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            vendor_name=dict(
                type='str',
                required=True
            ),
            vendor_sku_name=dict(
                type='str'
            )
        )

        self.vendor_name = None
        self.vendor_sku_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualNetworkFunctionVendorSkuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

        if (self.vendor_name is not None and
            self.vendor_sku_name is not None):
            self.results['virtual_network_function_vendor_skus'] = self.format_item(self.list())
        elif (self.vendor_name is not None):
            self.results['virtual_network_function_vendor_skus'] = self.format_item(self.listbyvendor())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_function_vendor_skus.list(vendor_name=self.vendor_name,
                                                                                  vendor_sku_name=self.vendor_sku_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyvendor(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_function_vendor_skus.list_by_vendor(vendor_name=self.vendor_name)
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
    AzureRMVirtualNetworkFunctionVendorSkuInfo()


if __name__ == '__main__':
    main()
