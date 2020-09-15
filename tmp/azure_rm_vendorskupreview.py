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
module: azure_rm_vendorskupreview
version_added: '2.9'
short_description: Manage Azure VendorSkuPreview instance.
description:
  - 'Create, update and delete instance of Azure VendorSkuPreview.'
options:
  vendor_name:
    description:
      - The name of the vendor.
    required: true
    type: str
  sku_name:
    description:
      - The name of the vendor sku.
    required: true
    type: str
  preview_subscription:
    description:
      - Preview subscription id.
    required: true
    type: str
  state:
    description:
      - Assert the state of the VendorSkuPreview.
      - >-
        Use C(present) to create or update an VendorSkuPreview and C(absent) to
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
    - name: Creates or updates preview subscription of vendor sku sub resource
      azure_rm_vendorskupreview: 
        preview_subscription: previewSub
        sku_name: TestSku
        vendor_name: TestVendor
        

    - name: Deletes preview subscription of vendor sku sub resource
      azure_rm_vendorskupreview: 
        preview_subscription: previewSub
        sku_name: TestSku
        vendor_name: TestVendor
        

'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.hybrid import HybridNetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVendorSkuPreview(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.vendor_name = None
        self.sku_name = None
        self.preview_subscription = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVendorSkuPreview, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HybridNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

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
            response = self.mgmt_client.vendor_sku_preview.create_or_update(vendor_name=self.vendor_name,
                                                                            sku_name=self.sku_name,
                                                                            preview_subscription=self.preview_subscription,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VendorSkuPreview instance.')
            self.fail('Error creating the VendorSkuPreview instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vendor_sku_preview.delete(vendor_name=self.vendor_name,
                                                                  sku_name=self.sku_name,
                                                                  preview_subscription=self.preview_subscription)
        except CloudError as e:
            self.log('Error attempting to delete the VendorSkuPreview instance.')
            self.fail('Error deleting the VendorSkuPreview instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vendor_sku_preview.get(vendor_name=self.vendor_name,
                                                               sku_name=self.sku_name,
                                                               preview_subscription=self.preview_subscription)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVendorSkuPreview()


if __name__ == '__main__':
    main()
