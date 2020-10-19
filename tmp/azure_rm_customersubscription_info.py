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
module: azure_rm_customersubscription_info
version_added: '2.9'
short_description: Get CustomerSubscription info.
description:
  - Get info of CustomerSubscription.
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
  customer_subscription_name:
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
      azure_rm_customersubscription_info: 
        registration_name: testregistration
        resource_group: azurestack
        

    - name: Returns the specified product.
      azure_rm_customersubscription_info: 
        customer_subscription_name: E09A4E93-29A7-4EBA-A6D4-76202383F07F
        registration_name: testregistration
        resource_group: azurestack
        

'''

RETURN = '''
customer_subscriptions:
  description: >-
    A list of dict results where the key is the name of the CustomerSubscription
    and the values are the facts for that CustomerSubscription.
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
        - List of customer subscriptions.
      returned: always
      type: list
      sample: null
      contains:
        tenant_id:
          description:
            - Tenant Id.
          returned: always
          type: str
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
    tenant_id:
      description:
        - Tenant Id.
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
    from azure.mgmt.azure import AzureStackManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCustomerSubscriptionInfo(AzureRMModuleBase):
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
            customer_subscription_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.registration_name = None
        self.customer_subscription_name = None

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
        super(AzureRMCustomerSubscriptionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureStackManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group is not None and
            self.registration_name is not None and
            self.customer_subscription_name is not None):
            self.results['customer_subscriptions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.registration_name is not None):
            self.results['customer_subscriptions'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.customer_subscriptions.get(resource_group=self.resource_group,
                                                                   registration_name=self.registration_name,
                                                                   customer_subscription_name=self.customer_subscription_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.customer_subscriptions.list(resource_group=self.resource_group,
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
    AzureRMCustomerSubscriptionInfo()


if __name__ == '__main__':
    main()
