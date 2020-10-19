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
module: azure_rm_customersubscription
version_added: '2.9'
short_description: Manage Azure CustomerSubscription instance.
description:
  - 'Create, update and delete instance of Azure CustomerSubscription.'
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
    required: true
    type: str
  etag:
    description:
      - >-
        The entity tag used for optimistic concurrency when modifying the
        resource.
    type: str
  tenant_id:
    description:
      - Tenant Id.
    type: str
  state:
    description:
      - Assert the state of the CustomerSubscription.
      - >-
        Use C(present) to create or update an CustomerSubscription and C(absent)
        to delete it.
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
    - name: Deletes a customer subscription under a registration.
      azure_rm_customersubscription: 
        customer_subscription_name: E09A4E93-29A7-4EBA-A6D4-76202383F07F
        registration_name: testregistration
        resource_group: azurestack
        

    - name: Creates a new customer subscription under a registration.
      azure_rm_customersubscription: 
        customer_subscription_name: E09A4E93-29A7-4EBA-A6D4-76202383F07F
        registration_name: testregistration
        resource_group: azurestack
        

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
tenant_id:
  description:
    - Tenant Id.
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
    from azure.mgmt.azure import AzureStackManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCustomerSubscription(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            tenant_id=dict(
                type='str',
                disposition='/tenant_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.registration_name = None
        self.customer_subscription_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCustomerSubscription, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.customer_subscriptions.create(resource_group=self.resource_group,
                                                                          registration_name=self.registration_name,
                                                                          customer_subscription_name=self.customer_subscription_name,
                                                                          customer_creation_parameters=self.body)
            else:
                response = self.mgmt_client.customer_subscriptions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the CustomerSubscription instance.')
            self.fail('Error creating the CustomerSubscription instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.customer_subscriptions.delete(resource_group=self.resource_group,
                                                                      registration_name=self.registration_name,
                                                                      customer_subscription_name=self.customer_subscription_name)
        except CloudError as e:
            self.log('Error attempting to delete the CustomerSubscription instance.')
            self.fail('Error deleting the CustomerSubscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.customer_subscriptions.get(resource_group=self.resource_group,
                                                                   registration_name=self.registration_name,
                                                                   customer_subscription_name=self.customer_subscription_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCustomerSubscription()


if __name__ == '__main__':
    main()
