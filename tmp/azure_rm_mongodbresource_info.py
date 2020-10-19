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
module: azure_rm_mongodbresource_info
version_added: '2.9'
short_description: Get MongoDBResource info.
description:
  - Get info of MongoDBResource.
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
  database_name:
    description:
      - Cosmos DB database name.
    type: str
  collection_name:
    description:
      - Cosmos DB collection name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CosmosDBMongoDBDatabaseList
      azure_rm_mongodbresource_info: 
        account_name: ddb1
        resource_group_name: rgName
        

    - name: CosmosDBMongoDBDatabaseGet
      azure_rm_mongodbresource_info: 
        account_name: ddb1
        database_name: databaseName
        resource_group_name: rg1
        

    - name: CosmosDBMongoDBDatabaseThroughputGet
      azure_rm_mongodbresource_info: 
        account_name: ddb1
        database_name: databaseName
        resource_group_name: rg1
        

    - name: CosmosDBMongoDBCollectionList
      azure_rm_mongodbresource_info: 
        account_name: ddb1
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBMongoDBCollectionGet
      azure_rm_mongodbresource_info: 
        account_name: ddb1
        collection_name: collectionName
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBMongoDBCollectionThroughputGet
      azure_rm_mongodbresource_info: 
        account_name: ddb1
        collection_name: collectionName
        database_name: databaseName
        resource_group_name: rg1
        

'''

RETURN = '''
mongo_dbresources:
  description: >-
    A list of dict results where the key is the name of the MongoDBResource and
    the values are the facts for that MongoDBResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          List of MongoDB databases and their properties.
          List of MongoDB collections and their properties.
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


class AzureRMMongoDBResourceInfo(AzureRMModuleBase):
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
            database_name=dict(
                type='str'
            ),
            collection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.database_name = None
        self.collection_name = None

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
        super(AzureRMMongoDBResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.database_name is not None and
            self.collection_name is not None):
            self.results['mongo_dbresources'] = self.format_item(self.getmongodbcollection())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.collection_name is not None):
            self.results['mongo_dbresources'] = self.format_item(self.getmongodbcollectionthroughput())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['mongo_dbresources'] = self.format_item(self.getmongodbdatabase())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['mongo_dbresources'] = self.format_item(self.getmongodbdatabasethroughput())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['mongo_dbresources'] = self.format_item(self.listmongodbcollection())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['mongo_dbresources'] = self.format_item(self.listmongodbdatabase())
        return self.results

    def getmongodbcollection(self):
        response = None

        try:
            response = self.mgmt_client.mongo_dbresources.get_mongo_dbcollection(resource_group_name=self.resource_group_name,
                                                                                 account_name=self.account_name,
                                                                                 database_name=self.database_name,
                                                                                 collection_name=self.collection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getmongodbcollectionthroughput(self):
        response = None

        try:
            response = self.mgmt_client.mongo_dbresources.get_mongo_dbcollection_throughput(resource_group_name=self.resource_group_name,
                                                                                            account_name=self.account_name,
                                                                                            database_name=self.database_name,
                                                                                            collection_name=self.collection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getmongodbdatabase(self):
        response = None

        try:
            response = self.mgmt_client.mongo_dbresources.get_mongo_dbdatabase(resource_group_name=self.resource_group_name,
                                                                               account_name=self.account_name,
                                                                               database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getmongodbdatabasethroughput(self):
        response = None

        try:
            response = self.mgmt_client.mongo_dbresources.get_mongo_dbdatabase_throughput(resource_group_name=self.resource_group_name,
                                                                                          account_name=self.account_name,
                                                                                          database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmongodbcollection(self):
        response = None

        try:
            response = self.mgmt_client.mongo_dbresources.list_mongo_dbcollection(resource_group_name=self.resource_group_name,
                                                                                  account_name=self.account_name,
                                                                                  database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmongodbdatabase(self):
        response = None

        try:
            response = self.mgmt_client.mongo_dbresources.list_mongo_dbdatabase(resource_group_name=self.resource_group_name,
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
    AzureRMMongoDBResourceInfo()


if __name__ == '__main__':
    main()
