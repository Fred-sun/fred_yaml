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
module: azure_rm_creator
version_added: '2.9'
short_description: Manage Azure Creator instance.
description:
  - 'Create, update and delete instance of Azure Creator.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - The name of the Maps Account.
    required: true
    type: str
  creator_name:
    description:
      - The name of the Maps Creator instance.
    required: true
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  state:
    description:
      - Assert the state of the Creator.
      - >-
        Use C(present) to create or update an Creator and C(absent) to delete
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
    - name: CreatePrivateAtlas
      azure_rm_creator: 
        account_name: myMapsAccount
        creator_name: myCreator
        resource_group_name: myResourceGroup
        

    - name: UpdateAccount
      azure_rm_creator: 
        account_name: myMapsAccount
        creator_name: myCreator
        resource_group_name: myResourceGroup
        

    - name: DeletePrivateAtlas
      azure_rm_creator: 
        account_name: myMapsAccount
        creator_name: myCreator
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
properties:
  description:
    - The Creator resource properties.
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_state:
      description:
        - >-
          The state of the resource provisioning, terminal states: Succeeded,
          Failed, Canceled
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
    from azure.mgmt.azure import Azure Maps Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCreator(AzureRMModuleBaseExt):
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
            creator_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.creator_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCreator, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Maps Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-01-preview')

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
            response = self.mgmt_client.creators.create_or_update(resource_group_name=self.resource_group_name,
                                                                  account_name=self.account_name,
                                                                  creator_name=self.creator_name,
                                                                  creator_create_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Creator instance.')
            self.fail('Error creating the Creator instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.creators.delete(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        creator_name=self.creator_name)
        except CloudError as e:
            self.log('Error attempting to delete the Creator instance.')
            self.fail('Error deleting the Creator instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.creators.get(resource_group_name=self.resource_group_name,
                                                     account_name=self.account_name,
                                                     creator_name=self.creator_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCreator()


if __name__ == '__main__':
    main()
