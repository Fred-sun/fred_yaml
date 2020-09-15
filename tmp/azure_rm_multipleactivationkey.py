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
module: azure_rm_multipleactivationkey
version_added: '2.9'
short_description: Manage Azure MultipleActivationKey instance.
description:
  - 'Create, update and delete instance of Azure MultipleActivationKey.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  multiple_activation_key_name:
    description:
      - The name of the MAK key.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  os_type:
    description:
      - Type of OS for which the key is requested.
    type: str
    choices:
      - Windows7
      - WindowsServer2008
      - WindowsServer2008R2
  support_type:
    description:
      - Type of support
    type: str
    choices:
      - SupplementalServicing
      - PremiumAssurance
  installed_server_number:
    description:
      - Number of activations/servers using the MAK key.
    type: integer
  agreement_number:
    description:
      - Agreement number under which the key is requested.
    type: str
  is_eligible:
    description:
      - >-
        <code> true </code> if user has eligible on-premises Windows physical or
        virtual machines, and that the requested key will only be used in their
        organization; <code> false </code> otherwise.
    type: bool
  state:
    description:
      - Assert the state of the MultipleActivationKey.
      - >-
        Use C(present) to create or update an MultipleActivationKey and
        C(absent) to delete it.
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
    - name: CreateMultipleActivationKey
      azure_rm_multipleactivationkey: 
        multiple_activation_key_name: server08-key-2019
        resource_group_name: testgr1
        

    - name: UpdateMultipleActivationKey
      azure_rm_multipleactivationkey: 
        multiple_activation_key_name: server08-key-2019
        resource_group_name: testgr1
        

    - name: DeleteMultipleActivationKey
      azure_rm_multipleactivationkey: 
        multiple_activation_key_name: server08-key-2019
        resource_group_name: testgr1
        

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
multiple_activation_key:
  description:
    - MAK 5x5 key.
  returned: always
  type: str
  sample: null
expiration_date:
  description:
    - End of support of security updates activated by the MAK key.
  returned: always
  type: str
  sample: null
os_type:
  description:
    - Type of OS for which the key is requested.
  returned: always
  type: str
  sample: null
support_type:
  description:
    - Type of support
  returned: always
  type: str
  sample: null
installed_server_number:
  description:
    - Number of activations/servers using the MAK key.
  returned: always
  type: integer
  sample: null
agreement_number:
  description:
    - Agreement number under which the key is requested.
  returned: always
  type: str
  sample: null
is_eligible:
  description:
    - >-
      <code> true </code> if user has eligible on-premises Windows physical or
      virtual machines, and that the requested key will only be used in their
      organization; <code> false </code> otherwise.
  returned: always
  type: bool
  sample: null
provisioning_state:
  description:
    - ''
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
    from azure.mgmt.windowsesu import windowsesu
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMultipleActivationKey(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            multiple_activation_key_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            os_type=dict(
                type='str',
                disposition='/os_type',
                choices=['Windows7',
                         'WindowsServer2008',
                         'WindowsServer2008R2']
            ),
            support_type=dict(
                type='str',
                disposition='/support_type',
                choices=['SupplementalServicing',
                         'PremiumAssurance']
            ),
            installed_server_number=dict(
                type='integer',
                disposition='/installed_server_number'
            ),
            agreement_number=dict(
                type='str',
                disposition='/agreement_number'
            ),
            is_eligible=dict(
                type='bool',
                disposition='/is_eligible'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.multiple_activation_key_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMultipleActivationKey, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(windowsesu,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-09-16-preview')

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
                response = self.mgmt_client.multiple_activation_keys.create(resource_group_name=self.resource_group_name,
                                                                            multiple_activation_key_name=self.multiple_activation_key_name,
                                                                            multiple_activation_key=self.body)
            else:
                response = self.mgmt_client.multiple_activation_keys.update(resource_group_name=self.resource_group_name,
                                                                            multiple_activation_key_name=self.multiple_activation_key_name,
                                                                            multiple_activation_key=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MultipleActivationKey instance.')
            self.fail('Error creating the MultipleActivationKey instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.multiple_activation_keys.delete(resource_group_name=self.resource_group_name,
                                                                        multiple_activation_key_name=self.multiple_activation_key_name)
        except CloudError as e:
            self.log('Error attempting to delete the MultipleActivationKey instance.')
            self.fail('Error deleting the MultipleActivationKey instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.multiple_activation_keys.get(resource_group_name=self.resource_group_name,
                                                                     multiple_activation_key_name=self.multiple_activation_key_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMultipleActivationKey()


if __name__ == '__main__':
    main()
