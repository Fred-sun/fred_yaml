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
module: azure_rm_sqlserver_info
version_added: '2.9'
short_description: Get SqlServer info.
description:
  - Get info of SqlServer.
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  sqlserver_registration_name:
    description:
      - Name of the SQL Server registration.
    required: true
    type: str
  sqlserver_name:
    description:
      - Name of the SQL Server.
    type: str
  expand:
    description:
      - The child resources to include in the response.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a SQL Server.
      azure_rm_sqlserver_info: 
        resource_group_name: testrg
        

    - name: Gets all SQL Servers in a SQL Server Registration.
      azure_rm_sqlserver_info: 
        resource_group_name: testrg
        

'''

RETURN = '''
sql_servers:
  description: >-
    A list of dict results where the key is the name of the SqlServer and the
    values are the facts for that SqlServer.
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
    cores:
      description:
        - Cores of the Sql Server.
      returned: always
      type: integer
      sample: null
    version:
      description:
        - Version of the Sql Server.
      returned: always
      type: str
      sample: null
    edition:
      description:
        - Sql Server Edition.
      returned: always
      type: str
      sample: null
    registration_id:
      description:
        - ID for Parent Sql Server Registration.
      returned: always
      type: str
      sample: null
    property_bag:
      description:
        - Sql Server Json Property Bag.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        cores:
          description:
            - Cores of the Sql Server.
          returned: always
          type: integer
          sample: null
        version:
          description:
            - Version of the Sql Server.
          returned: always
          type: str
          sample: null
        edition:
          description:
            - Sql Server Edition.
          returned: always
          type: str
          sample: null
        registration_id:
          description:
            - ID for Parent Sql Server Registration.
          returned: always
          type: str
          sample: null
        property_bag:
          description:
            - Sql Server Json Property Bag.
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
    from azure.mgmt.azure import AzureDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSqlServerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sqlserver_registration_name=dict(
                type='str',
                required=True
            ),
            sqlserver_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.sqlserver_registration_name = None
        self.sqlserver_name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-24-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSqlServerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-24-preview')

        if (self.resource_group_name is not None and
            self.sqlserver_registration_name is not None and
            self.sqlserver_name is not None):
            self.results['sql_servers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.sqlserver_registration_name is not None):
            self.results['sql_servers'] = self.format_item(self.listbyresourcegroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sql_servers.get(resource_group_name=self.resource_group_name,
                                                        sqlserver_registration_name=self.sqlserver_registration_name,
                                                        sqlserver_name=self.sqlserver_name,
                                                        expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.sql_servers.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                           sqlserver_registration_name=self.sqlserver_registration_name,
                                                                           expand=self.expand)
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
    AzureRMSqlServerInfo()


if __name__ == '__main__':
    main()
