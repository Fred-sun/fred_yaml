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
module: azure_rm_trustedidprovider
version_added: '2.9'
short_description: Manage Azure TrustedIdProvider instance.
description:
  - 'Create, update and delete instance of Azure TrustedIdProvider.'
options:
  resource_group_name:
    description:
      - The name of the Azure resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the Data Lake Store account.
    required: true
    type: str
  trusted_id_provider_name:
    description:
      - >-
        The name of the trusted identity provider. This is used for
        differentiation of providers in the account.
      - The name of the trusted identity provider to retrieve.
      - The name of the trusted identity provider to delete.
    required: true
    type: str
  id_provider:
    description:
      - The URL of this trusted identity provider.
    type: str
  state:
    description:
      - Assert the state of the TrustedIdProvider.
      - >-
        Use C(present) to create or update an TrustedIdProvider and C(absent) to
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
    - name: Creates or updates the specified trusted identity provider. During update, the trusted identity provider with the specified name will be replaced with this new provider
      azure_rm_trustedidprovider: 
        account_name: contosoadla
        resource_group_name: contosorg
        trusted_id_provider_name: test_trusted_id_provider_name
        properties:
          id_provider: 'https://sts.windows.net/ea9ec534-a3e3-4e45-ad36-3afc5bb291c1'
        

    - name: Updates the specified trusted identity provider
      azure_rm_trustedidprovider: 
        account_name: contosoadla
        resource_group_name: contosorg
        trusted_id_provider_name: test_trusted_id_provider_name
        properties:
          id_provider: 'https://sts.windows.net/ea9ec534-a3e3-4e45-ad36-3afc5bb291c1'
        

    - name: Deletes the specified trusted identity provider from the specified Data Lake Store account
      azure_rm_trustedidprovider: 
        account_name: contosoadla
        resource_group_name: contosorg
        trusted_id_provider_name: test_trusted_id_provider_name
        

'''

RETURN = '''
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
id_provider:
  description:
    - The URL of this trusted identity provider.
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
    from azure.mgmt.data import DataLakeStoreAccountManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTrustedIdProvider(AzureRMModuleBaseExt):
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
            trusted_id_provider_name=dict(
                type='str',
                required=True
            ),
            id_provider=dict(
                type='str',
                disposition='/id_provider'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.trusted_id_provider_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTrustedIdProvider, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataLakeStoreAccountManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-11-01')

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
            response = self.mgmt_client.trusted_id_providers.create_or_update(resource_group_name=self.resource_group_name,
                                                                              account_name=self.account_name,
                                                                              trusted_id_provider_name=self.trusted_id_provider_name,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the TrustedIdProvider instance.')
            self.fail('Error creating the TrustedIdProvider instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.trusted_id_providers.delete(resource_group_name=self.resource_group_name,
                                                                    account_name=self.account_name,
                                                                    trusted_id_provider_name=self.trusted_id_provider_name)
        except CloudError as e:
            self.log('Error attempting to delete the TrustedIdProvider instance.')
            self.fail('Error deleting the TrustedIdProvider instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.trusted_id_providers.get(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name,
                                                                 trusted_id_provider_name=self.trusted_id_provider_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTrustedIdProvider()


if __name__ == '__main__':
    main()
