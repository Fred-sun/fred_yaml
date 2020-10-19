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
module: azure_rm_datalakestoreaccount_info
version_added: '2.9'
short_description: Get DataLakeStoreAccount info.
description:
  - Get info of DataLakeStoreAccount.
options:
  resource_group_name:
    description:
      - The name of the Azure resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the Data Lake Analytics account.
    required: true
    type: str
  filter:
    description:
      - OData filter. Optional.
    type: str
  top:
    description:
      - The number of items to return. Optional.
    type: integer
  skip:
    description:
      - The number of items to skip over before returning elements. Optional.
    type: integer
  select:
    description:
      - >-
        OData Select statement. Limits the properties on each entry to just
        those requested, e.g. Categories?$select=CategoryName,Description.
        Optional.
    type: str
  orderby:
    description:
      - >-
        OrderBy clause. One or more comma-separated expressions with an optional
        "asc" (the default) or "desc" depending on the order you'd like the
        values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    type: str
  count:
    description:
      - >-
        The Boolean value of true or false to request a count of the matching
        resources included with the resources in the response, e.g.
        Categories?$count=true. Optional.
    type: bool
  data_lake_store_account_name:
    description:
      - The name of the Data Lake Store account to retrieve
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets the first page of Data Lake Store accounts linked to the specified Data Lake Analytics account
      azure_rm_datalakestoreaccount_info: 
        account_name: contosoadla
        resource_group_name: contosorg
        

    - name: Gets the specified Data Lake Store account details
      azure_rm_datalakestoreaccount_info: 
        account_name: contosoadla
        data_lake_store_account_name: test_adls_account
        resource_group_name: contosorg
        

'''

RETURN = '''
data_lake_store_accounts:
  description: >-
    A list of dict results where the key is the name of the DataLakeStoreAccount
    and the values are the facts for that DataLakeStoreAccount.
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
        suffix:
          description:
            - The optional suffix for the Data Lake Store account.
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
    suffix:
      description:
        - The optional suffix for the Data Lake Store account.
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
    from azure.mgmt.data import DataLakeAnalyticsAccountManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataLakeStoreAccountInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip=dict(
                type='integer'
            ),
            select=dict(
                type='str'
            ),
            orderby=dict(
                type='str'
            ),
            count=dict(
                type='bool'
            ),
            data_lake_store_account_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.filter = None
        self.top = None
        self.skip = None
        self.select = None
        self.orderby = None
        self.count = None
        self.data_lake_store_account_name = None

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
        super(AzureRMDataLakeStoreAccountInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataLakeAnalyticsAccountManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-11-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.data_lake_store_account_name is not None):
            self.results['data_lake_store_accounts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['data_lake_store_accounts'] = self.format_item(self.listbyaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_lake_store_accounts.get(resource_group_name=self.resource_group_name,
                                                                     account_name=self.account_name,
                                                                     data_lake_store_account_name=self.data_lake_store_account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyaccount(self):
        response = None

        try:
            response = self.mgmt_client.data_lake_store_accounts.list_by_account(resource_group_name=self.resource_group_name,
                                                                                 account_name=self.account_name,
                                                                                 filter=self.filter,
                                                                                 top=self.top,
                                                                                 skip=self.skip,
                                                                                 select=self.select,
                                                                                 orderby=self.orderby,
                                                                                 count=self.count)
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
    AzureRMDataLakeStoreAccountInfo()


if __name__ == '__main__':
    main()
