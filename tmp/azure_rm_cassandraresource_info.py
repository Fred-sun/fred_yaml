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
module: azure_rm_cassandraresource_info
version_added: '2.9'
short_description: Get CassandraResource info.
description:
  - Get info of CassandraResource.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    required: true
    type: str
  keyspace_name:
    description:
      - Cosmos DB keyspace name.
    type: str
  table_name:
    description:
      - Cosmos DB table name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CosmosDBCassandraKeyspaceList
      azure_rm_cassandraresource_info: 
        account_name: ddb1
        resource_group_name: rgName
        

    - name: CosmosDBCassandraKeyspaceGet
      azure_rm_cassandraresource_info: 
        account_name: ddb1
        keyspace_name: keyspaceName
        resource_group_name: rg1
        

    - name: CosmosDBCassandraKeyspaceThroughputGet
      azure_rm_cassandraresource_info: 
        account_name: ddb1
        keyspace_name: keyspaceName
        resource_group_name: rg1
        

    - name: CosmosDBCassandraTableList
      azure_rm_cassandraresource_info: 
        account_name: ddb1
        keyspace_name: keyspaceName
        resource_group_name: rgName
        

    - name: CosmosDBCassandraTableGet
      azure_rm_cassandraresource_info: 
        account_name: ddb1
        keyspace_name: keyspaceName
        resource_group_name: rg1
        table_name: tableName
        

    - name: CosmosDBCassandraTableThroughputGet
      azure_rm_cassandraresource_info: 
        account_name: ddb1
        keyspace_name: keyspaceName
        resource_group_name: rg1
        table_name: tableName
        

'''

RETURN = '''
cassandra_resources:
  description: >-
    A list of dict results where the key is the name of the CassandraResource
    and the values are the facts for that CassandraResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          List of Cassandra keyspaces and their properties.
          List of Cassandra tables and their properties.
      returned: always
      type: list
      sample: null
      contains:
        resource:
          description:
            - ''
          returned: always
          type: dict
          sample: null
        options:
          description:
            - Cosmos DB options resource object
          returned: always
          type: dict
          sample: null
          contains:
            throughput:
              description:
                - >-
                  Value of the Cosmos DB resource throughput or
                  autoscaleSettings. Use the ThroughputSetting resource when
                  retrieving offer details.
              returned: always
              type: integer
              sample: null
            autoscale_settings:
              description:
                - Specifies the Autoscale settings.
              returned: always
              type: dict
              sample: null
              contains:
                max_throughput:
                  description:
                    - >-
                      Represents maximum throughput, the resource can scale up
                      to.
                  returned: always
                  type: integer
                  sample: null
    id:
      description:
        - The unique resource identifier of the ARM resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the ARM resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of Azure resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The location of the resource group to which the resource belongs.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - >-
          Tags are a list of key-value pairs that describe the resource. These
          tags can be used in viewing and grouping this resource (across
          resource groups). A maximum of 15 tags can be provided for a resource.
          Each tag must have a key no greater than 128 characters and value no
          greater than 256 characters. For example, the default experience for a
          template type is set with "defaultExperience": "Cassandra". Current
          "defaultExperience" values also include "Table", "Graph",
          "DocumentDB", and "MongoDB".
      returned: always
      type: dictionary
      sample: null
    resource:
      description:
        - ''
      returned: always
      type: dict
      sample: null
    options:
      description:
        - Cosmos DB options resource object
      returned: always
      type: dict
      sample: null
      contains:
        throughput:
          description:
            - >-
              Value of the Cosmos DB resource throughput or autoscaleSettings.
              Use the ThroughputSetting resource when retrieving offer details.
          returned: always
          type: integer
          sample: null
        autoscale_settings:
          description:
            - Specifies the Autoscale settings.
          returned: always
          type: dict
          sample: null
          contains:
            max_throughput:
              description:
                - 'Represents maximum throughput, the resource can scale up to.'
              returned: always
              type: integer
              sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.cosmos import CosmosDBManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCassandraResourceInfo(AzureRMModuleBase):
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
            keyspace_name=dict(
                type='str'
            ),
            table_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.keyspace_name = None
        self.table_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCassandraResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.keyspace_name is not None and
            self.table_name is not None):
            self.results['cassandra_resources'] = self.format_item(self.getcassandratable())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.keyspace_name is not None and
              self.table_name is not None):
            self.results['cassandra_resources'] = self.format_item(self.getcassandratablethroughput())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.keyspace_name is not None):
            self.results['cassandra_resources'] = self.format_item(self.getcassandrakeyspace())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.keyspace_name is not None):
            self.results['cassandra_resources'] = self.format_item(self.getcassandrakeyspacethroughput())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.keyspace_name is not None):
            self.results['cassandra_resources'] = self.format_item(self.listcassandratable())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['cassandra_resources'] = self.format_item(self.listcassandrakeyspace())
        return self.results

    def getcassandratable(self):
        response = None

        try:
            response = self.mgmt_client.cassandra_resources.get_cassandra_table(resource_group_name=self.resource_group_name,
                                                                                account_name=self.account_name,
                                                                                keyspace_name=self.keyspace_name,
                                                                                table_name=self.table_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getcassandratablethroughput(self):
        response = None

        try:
            response = self.mgmt_client.cassandra_resources.get_cassandra_table_throughput(resource_group_name=self.resource_group_name,
                                                                                           account_name=self.account_name,
                                                                                           keyspace_name=self.keyspace_name,
                                                                                           table_name=self.table_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getcassandrakeyspace(self):
        response = None

        try:
            response = self.mgmt_client.cassandra_resources.get_cassandra_keyspace(resource_group_name=self.resource_group_name,
                                                                                   account_name=self.account_name,
                                                                                   keyspace_name=self.keyspace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getcassandrakeyspacethroughput(self):
        response = None

        try:
            response = self.mgmt_client.cassandra_resources.get_cassandra_keyspace_throughput(resource_group_name=self.resource_group_name,
                                                                                              account_name=self.account_name,
                                                                                              keyspace_name=self.keyspace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listcassandratable(self):
        response = None

        try:
            response = self.mgmt_client.cassandra_resources.list_cassandra_table(resource_group_name=self.resource_group_name,
                                                                                 account_name=self.account_name,
                                                                                 keyspace_name=self.keyspace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listcassandrakeyspace(self):
        response = None

        try:
            response = self.mgmt_client.cassandra_resources.list_cassandra_keyspace(resource_group_name=self.resource_group_name,
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
    AzureRMCassandraResourceInfo()


if __name__ == '__main__':
    main()
