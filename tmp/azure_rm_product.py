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
module: azure_rm_product
version_added: '2.9'
short_description: Manage Azure Product instance.
description:
  - 'Create, update and delete instance of Azure Product.'
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
    required: true
    type: str
  state:
    description:
      - Assert the state of the Product.
      - >-
        Use C(present) to create or update an Product and C(absent) to delete
        it.
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
'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import AzureStackManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMProduct(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.registration_name = None
        self.product_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMProduct, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AzureStackManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
                response = self.mgmt_client.products.create()
            else:
                response = self.mgmt_client.products.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Product instance.')
            self.fail('Error creating the Product instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.products.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Product instance.')
            self.fail('Error deleting the Product instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.products.get(resource_group=self.resource_group,
                                                     registration_name=self.registration_name,
                                                     product_name=self.product_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMProduct()


if __name__ == '__main__':
    main()
