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
module: azure_rm_dataconnection_info
version_added: '2.9'
short_description: Get DataConnection info.
description:
  - Get info of DataConnection.
options:
  resource_group_name:
    description:
      - The name of the resource group containing the Kusto cluster.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the Kusto cluster.
    required: true
    type: str
  database_name:
    description:
      - The name of the database in the Kusto cluster.
    required: true
    type: str
  data_connection_name:
    description:
      - The name of the data connection.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: KustoDatabasesListByCluster
      azure_rm_dataconnection_info: 
        cluster_name: kustoclusterrptest4
        database_name: KustoDatabase8
        resource_group_name: kustorptest
        

    - name: KustoDataConnectionsGet
      azure_rm_dataconnection_info: 
        cluster_name: kustoclusterrptest4
        data_connection_name: DataConnections8
        database_name: KustoDatabase8
        resource_group_name: kustorptest
        

'''

RETURN = '''
data_connections:
  description: >-
    A list of dict results where the key is the name of the DataConnection and
    the values are the facts for that DataConnection.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of Kusto data connections.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        kind:
          description:
            - Kind of the endpoint for the data connection
          returned: always
          type: str
          sample: null
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
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    kind:
      description:
        - Kind of the endpoint for the data connection
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
    from azure.mgmt.kusto import KustoManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataConnectionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            data_connection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.database_name = None
        self.data_connection_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-14'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDataConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(KustoManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-14')

        if (self.resource_group_name is not None and
            self.cluster_name is not None and
            self.database_name is not None and
            self.data_connection_name is not None):
            self.results['data_connections'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.cluster_name is not None and
              self.database_name is not None):
            self.results['data_connections'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_connections.get(resource_group_name=self.resource_group_name,
                                                             cluster_name=self.cluster_name,
                                                             database_name=self.database_name,
                                                             data_connection_name=self.data_connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.data_connections.list_by_database(resource_group_name=self.resource_group_name,
                                                                          cluster_name=self.cluster_name,
                                                                          database_name=self.database_name)
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
    AzureRMDataConnectionInfo()


if __name__ == '__main__':
    main()
