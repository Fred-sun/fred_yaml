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
module: azure_rm_querytext_info
version_added: '2.9'
short_description: Get QueryText info.
description:
  - Get info of QueryText.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  query_id:
    description:
      - The Query-Store query identifier.
    type: str
  query_ids:
    description:
      - The query identifiers
    type: list
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: QueryTextsGet
      azure_rm_querytext_info: 
        query_id: 1
        resource_group_name: testResourceGroupName
        server_name: testServerName
        

    - name: QueryTextsListByServer
      azure_rm_querytext_info: 
        query_ids:
          - '1'
          - '2'
        resource_group_name: testResourceGroupName
        server_name: testServerName
        

'''

RETURN = '''
query_texts:
  description: >-
    A list of dict results where the key is the name of the QueryText and the
    values are the facts for that QueryText.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    query_id:
      description:
        - Query identifier unique to the server.
      returned: always
      type: str
      sample: null
    query_text:
      description:
        - Query text.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of query texts.
      returned: always
      type: list
      sample: null
      contains:
        query_id:
          description:
            - Query identifier unique to the server.
          returned: always
          type: str
          sample: null
        query_text:
          description:
            - Query text.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.my import MySQLManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMQueryTextInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            query_id=dict(
                type='str'
            ),
            query_ids=dict(
                type='list',
                elements='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.query_id = None
        self.query_ids = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMQueryTextInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.query_id is not None):
            self.results['query_texts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.query_ids is not None):
            self.results['query_texts'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.query_texts.get(resource_group_name=self.resource_group_name,
                                                        server_name=self.server_name,
                                                        query_id=self.query_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.query_texts.list_by_server(resource_group_name=self.resource_group_name,
                                                                   server_name=self.server_name,
                                                                   query_ids=self.query_ids)
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
    AzureRMQueryTextInfo()


if __name__ == '__main__':
    main()
