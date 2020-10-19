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
module: azure_rm_account
version_added: '2.9'
short_description: Manage Azure Account instance.
description:
  - 'Create, update and delete instance of Azure Account.'
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    required: true
    type: str
  resource_name:
    description:
      - Name of the resource.
    required: true
    type: str
  account_name:
    description:
      - The account name.
    type: str
  location:
    description:
      - The Azure instance location.
    type: str
  operation_type:
    description:
      - The type of the operation.
    type: sealed-choice
  properties:
    description:
      - The custom properties of the resource.
    type: dictionary
  state:
    description:
      - Assert the state of the Account.
      - >-
        Use C(present) to create or update an Account and C(absent) to delete
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
    - name: Create an account resource
      azure_rm_account: 
        resource_group_name: VS-Example-Group
        resource_name: Example
        account_name: Example
        location: Central US
        operation_type: create
        properties: {}
        tags: {}
        

    - name: Delete an account resource
      azure_rm_account: 
        resource_group_name: VS-Example-Group
        resource_name: Example
        

'''

RETURN = '''
id:
  description:
    - Unique identifier of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Resource properties.
  returned: always
  type: dictionary
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.visual import Visual Studio Resource Provider Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAccount(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                disposition='/account_name'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            operation_type=dict(
                type='sealed-choice',
                disposition='/operation_type'
            ),
            properties=dict(
                type='dictionary',
                disposition='/properties'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAccount, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Visual Studio Resource Provider Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01-preview')

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
            response = self.mgmt_client.accounts.create_or_update(resource_group_name=self.resource_group_name,
                                                                  resource_name=self.resource_name,
                                                                  body=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Account instance.')
            self.fail('Error creating the Account instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.accounts.delete(resource_group_name=self.resource_group_name,
                                                        resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Account instance.')
            self.fail('Error deleting the Account instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.accounts.get(resource_group_name=self.resource_group_name,
                                                     resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAccount()


if __name__ == '__main__':
    main()
