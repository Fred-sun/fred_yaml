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
module: azure_rm_trustedidprovider_info
version_added: '2.9'
short_description: Get TrustedIdProvider info.
description:
  - Get info of TrustedIdProvider.
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
      - The name of the trusted identity provider to retrieve.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account
      azure_rm_trustedidprovider_info: 
        account_name: contosoadla
        resource_group_name: contosorg
        

    - name: Gets the specified Data Lake Store trusted identity provider
      azure_rm_trustedidprovider_info: 
        account_name: contosoadla
        resource_group_name: contosorg
        trusted_id_provider_name: test_trusted_id_provider_name
        

'''

RETURN = '''
trusted_id_providers:
  description: >-
    A list of dict results where the key is the name of the TrustedIdProvider
    and the values are the facts for that TrustedIdProvider.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        id_provider:
          description:
            - The URL of this trusted identity provider.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link (url) to the next page of results.
      returned: always
      type: str
      sample: null
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataLakeStoreAccountManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTrustedIdProviderInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.trusted_id_provider_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTrustedIdProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataLakeStoreAccountManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-11-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.trusted_id_provider_name is not None):
            self.results['trusted_id_providers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['trusted_id_providers'] = self.format_item(self.listbyaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.trusted_id_providers.get(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name,
                                                                 trusted_id_provider_name=self.trusted_id_provider_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyaccount(self):
        response = None

        try:
            response = self.mgmt_client.trusted_id_providers.list_by_account(resource_group_name=self.resource_group_name,
                                                                             account_name=self.account_name)
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
    AzureRMTrustedIdProviderInfo()


if __name__ == '__main__':
    main()
