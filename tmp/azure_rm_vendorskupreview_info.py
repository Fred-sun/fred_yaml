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
module: azure_rm_vendorskupreview_info
version_added: '2.9'
short_description: Get VendorSkuPreview info.
description:
  - Get info of VendorSkuPreview.
options:
  vendor_name:
    description:
      - The name of the vendor.
    required: true
    type: str
  sku_name:
    description:
      - The name of the sku.
      - The name of the vendor sku.
    required: true
    type: str
  preview_subscription:
    description:
      - Preview subscription id.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all preview subscriptions of vendor sku sub resource
      azure_rm_vendorskupreview_info: 
        sku_name: TestSku
        vendor_name: TestVendor
        

    - name: Gets preview subscription of vendor sku sub resource
      azure_rm_vendorskupreview_info: 
        preview_subscription: previewSub
        sku_name: TestSku
        vendor_name: TestVendor
        

'''

RETURN = '''
vendor_sku_preview:
  description: >-
    A list of dict results where the key is the name of the VendorSkuPreview and
    the values are the facts for that VendorSkuPreview.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of preview subscriptions.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Preview subscription id
          returned: always
          type: str
          sample: null
        id:
          description:
            - ARM id of the resource
          returned: always
          type: str
          sample: null
        type:
          description:
            - Type of the resource
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of results.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Preview subscription id
      returned: always
      type: str
      sample: null
    id:
      description:
        - ARM id of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the resource
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


class AzureRMVendorSkuPreviewInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            vendor_name=dict(
                type='str',
                required=True
            ),
            sku_name=dict(
                type='str',
                required=True
            ),
            preview_subscription=dict(
                type='str'
            )
        )

        self.vendor_name = None
        self.sku_name = None
        self.preview_subscription = None

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
        super(AzureRMVendorSkuPreviewInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

        if (self.vendor_name is not None and
            self.sku_name is not None and
            self.preview_subscription is not None):
            self.results['vendor_sku_preview'] = self.format_item(self.get())
        elif (self.vendor_name is not None and
              self.sku_name is not None):
            self.results['vendor_sku_preview'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vendor_sku_preview.get(vendor_name=self.vendor_name,
                                                               sku_name=self.sku_name,
                                                               preview_subscription=self.preview_subscription)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.vendor_sku_preview.list(vendor_name=self.vendor_name,
                                                                sku_name=self.sku_name)
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
    AzureRMVendorSkuPreviewInfo()


if __name__ == '__main__':
    main()
