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
module: azure_rm_product_info
version_added: '2.9'
short_description: Get Product info.
description:
  - Get info of Product.
options:
  resource_group:
    description:
      - Name of the resource group.
    required: true
    type: str
  registration_name:
    description:
      - Name of the Azure Stack registration.
    required: true
    type: str
  product_name:
    description:
      - Name of the product.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Returns a list of products.
      azure_rm_product_info: 
        registration_name: testregistration
        resource_group: azurestack
        

    - name: Returns the specified product.
      azure_rm_product_info: 
        product_name: Microsoft.OSTCExtensions.VMAccessForLinux.1.4.7.1
        registration_name: testregistration
        resource_group: azurestack
        

'''

RETURN = '''
products:
  description: >-
    A list of dict results where the key is the name of the Product and the
    values are the facts for that Product.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URI to the next page.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of products.
      returned: always
      type: list
      sample: null
      contains:
        display_name:
          description:
            - The display name of the product.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The description of the product.
          returned: always
          type: str
          sample: null
        publisher_display_name:
          description:
            - The user-friendly name of the product publisher.
          returned: always
          type: str
          sample: null
        publisher_identifier:
          description:
            - Publisher identifier.
          returned: always
          type: str
          sample: null
        offer:
          description:
            - The offer representing the product.
          returned: always
          type: str
          sample: null
        offer_version:
          description:
            - The version of the product offer.
          returned: always
          type: str
          sample: null
        sku:
          description:
            - The product SKU.
          returned: always
          type: str
          sample: null
        billing_part_number:
          description:
            - The part number used for billing purposes.
          returned: always
          type: str
          sample: null
        vm_extension_type:
          description:
            - The type of the Virtual Machine Extension.
          returned: always
          type: str
          sample: null
        gallery_item_identity:
          description:
            - The identifier of the gallery item corresponding to the product.
          returned: always
          type: str
          sample: null
        icon_uris:
          description:
            - Additional links available for this product.
          returned: always
          type: dict
          sample: null
          contains:
            large:
              description:
                - URI to large icon.
              returned: always
              type: str
              sample: null
            wide:
              description:
                - URI to wide icon.
              returned: always
              type: str
              sample: null
            medium:
              description:
                - URI to medium icon.
              returned: always
              type: str
              sample: null
            small:
              description:
                - URI to small icon.
              returned: always
              type: str
              sample: null
            hero:
              description:
                - URI to hero icon.
              returned: always
              type: str
              sample: null
        links:
          description:
            - Additional links available for this product.
          returned: always
          type: list
          sample: null
          contains:
            display_name:
              description:
                - The description of the link.
              returned: always
              type: str
              sample: null
            uri:
              description:
                - The URI corresponding to the link.
              returned: always
              type: str
              sample: null
        legal_terms:
          description:
            - The legal terms.
          returned: always
          type: str
          sample: null
        privacy_policy:
          description:
            - The privacy policy.
          returned: always
          type: str
          sample: null
        payload_length:
          description:
            - The length of product content.
          returned: always
          type: integer
          sample: null
        product_kind:
          description:
            - >-
              The kind of the product (virtualMachine or
              virtualMachineExtension)
          returned: always
          type: str
          sample: null
        product_properties:
          description:
            - Additional properties for the product.
          returned: always
          type: dict
          sample: null
          contains:
            version:
              description:
                - The version.
              returned: always
              type: str
              sample: null
        compatibility:
          description:
            - Product compatibility with current device.
          returned: always
          type: dict
          sample: null
          contains:
            is_compatible:
              description:
                - Tells if product is compatible with current device
              returned: always
              type: bool
              sample: null
            message:
              description:
                - Short error message if any compatibility issues are found
              returned: always
              type: str
              sample: null
            description:
              description:
                - Full error message if any compatibility issues are found
              returned: always
              type: str
              sample: null
            issues:
              description:
                - List of all issues found
              returned: always
              type: list
              sample: null
    id:
      description:
        - ID of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of Resource.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          The entity tag used for optimistic concurrency when modifying the
          resource.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - The display name of the product.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the product.
      returned: always
      type: str
      sample: null
    publisher_display_name:
      description:
        - The user-friendly name of the product publisher.
      returned: always
      type: str
      sample: null
    publisher_identifier:
      description:
        - Publisher identifier.
      returned: always
      type: str
      sample: null
    offer:
      description:
        - The offer representing the product.
      returned: always
      type: str
      sample: null
    offer_version:
      description:
        - The version of the product offer.
      returned: always
      type: str
      sample: null
    sku:
      description:
        - The product SKU.
      returned: always
      type: str
      sample: null
    billing_part_number:
      description:
        - The part number used for billing purposes.
      returned: always
      type: str
      sample: null
    vm_extension_type:
      description:
        - The type of the Virtual Machine Extension.
      returned: always
      type: str
      sample: null
    gallery_item_identity:
      description:
        - The identifier of the gallery item corresponding to the product.
      returned: always
      type: str
      sample: null
    icon_uris:
      description:
        - Additional links available for this product.
      returned: always
      type: dict
      sample: null
      contains:
        large:
          description:
            - URI to large icon.
          returned: always
          type: str
          sample: null
        wide:
          description:
            - URI to wide icon.
          returned: always
          type: str
          sample: null
        medium:
          description:
            - URI to medium icon.
          returned: always
          type: str
          sample: null
        small:
          description:
            - URI to small icon.
          returned: always
          type: str
          sample: null
        hero:
          description:
            - URI to hero icon.
          returned: always
          type: str
          sample: null
    links:
      description:
        - Additional links available for this product.
      returned: always
      type: list
      sample: null
      contains:
        display_name:
          description:
            - The description of the link.
          returned: always
          type: str
          sample: null
        uri:
          description:
            - The URI corresponding to the link.
          returned: always
          type: str
          sample: null
    legal_terms:
      description:
        - The legal terms.
      returned: always
      type: str
      sample: null
    privacy_policy:
      description:
        - The privacy policy.
      returned: always
      type: str
      sample: null
    payload_length:
      description:
        - The length of product content.
      returned: always
      type: integer
      sample: null
    product_kind:
      description:
        - The kind of the product (virtualMachine or virtualMachineExtension)
      returned: always
      type: str
      sample: null
    product_properties:
      description:
        - Additional properties for the product.
      returned: always
      type: dict
      sample: null
      contains:
        version:
          description:
            - The version.
          returned: always
          type: str
          sample: null
    compatibility:
      description:
        - Product compatibility with current device.
      returned: always
      type: dict
      sample: null
      contains:
        is_compatible:
          description:
            - Tells if product is compatible with current device
          returned: always
          type: bool
          sample: null
        message:
          description:
            - Short error message if any compatibility issues are found
          returned: always
          type: str
          sample: null
        description:
          description:
            - Full error message if any compatibility issues are found
          returned: always
          type: str
          sample: null
        issues:
          description:
            - List of all issues found
          returned: always
          type: list
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import AzureStackManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProductInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            registration_name=dict(
                type='str',
                required=True
            ),
            product_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.registration_name = None
        self.product_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProductInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureStackManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group is not None and
            self.registration_name is not None and
            self.product_name is not None):
            self.results['products'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.registration_name is not None):
            self.results['products'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.products.get(resource_group=self.resource_group,
                                                     registration_name=self.registration_name,
                                                     product_name=self.product_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.products.list(resource_group=self.resource_group,
                                                      registration_name=self.registration_name)
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
    AzureRMProductInfo()


if __name__ == '__main__':
    main()
