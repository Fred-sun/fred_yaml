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
module: azure_rm_sqlresource_info
version_added: '2.9'
short_description: Get SqlResource info.
description:
  - Get info of SqlResource.
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
  container_name:
    description:
      - Cosmos DB container name.
    type: str
  stored_procedure_name:
    description:
      - Cosmos DB storedProcedure name.
    type: str
  user_defined_function_name:
    description:
      - Cosmos DB userDefinedFunction name.
    type: str
  trigger_name:
    description:
      - Cosmos DB trigger name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CosmosDBSqlDatabaseList
      azure_rm_sqlresource_info: 
        account_name: ddb1
        resource_group_name: rgName
        

    - name: CosmosDBSqlDatabaseGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        database_name: databaseName
        resource_group_name: rg1
        

    - name: CosmosDBSqlDatabaseThroughputGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        database_name: databaseName
        resource_group_name: rg1
        

    - name: CosmosDBSqlContainerList
      azure_rm_sqlresource_info: 
        account_name: ddb1
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBSqlContainerGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBSqlContainerThroughputGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rg1
        

    - name: CosmosDBSqlStoredProcedureList
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBSqlStoredProcedureGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        stored_procedure_name: storedProcedureName
        

    - name: CosmosDBSqlUserDefinedFunctionList
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBSqlUserDefinedFunctionGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        user_defined_function_name: userDefinedFunctionName
        

    - name: CosmosDBSqlTriggerList
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        

    - name: CosmosDBSqlTriggerGet
      azure_rm_sqlresource_info: 
        account_name: ddb1
        container_name: containerName
        database_name: databaseName
        resource_group_name: rgName
        trigger_name: triggerName
        

'''

RETURN = '''
sql_resources:
  description: >-
    A list of dict results where the key is the name of the SqlResource and the
    values are the facts for that SqlResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          List of SQL databases and their properties.
          List of containers and their properties.
          List of storedProcedures and their properties.
          List of userDefinedFunctions and their properties.
          List of triggers and their properties.
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
          contains:
            colls:
              description:
                - >-
                  A system generated property that specified the addressable
                  path of the collections resource.
              returned: always
              type: str
              sample: null
            users:
              description:
                - >-
                  A system generated property that specifies the addressable
                  path of the users resource.
              returned: always
              type: str
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
      contains:
        colls:
          description:
            - >-
              A system generated property that specified the addressable path of
              the collections resource.
          returned: always
          type: str
          sample: null
        users:
          description:
            - >-
              A system generated property that specifies the addressable path of
              the users resource.
          returned: always
          type: str
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


class AzureRMSqlResourceInfo(AzureRMModuleBase):
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
            container_name=dict(
                type='str'
            ),
            stored_procedure_name=dict(
                type='str'
            ),
            user_defined_function_name=dict(
                type='str'
            ),
            trigger_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.database_name = None
        self.container_name = None
        self.stored_procedure_name = None
        self.user_defined_function_name = None
        self.trigger_name = None

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
        super(AzureRMSqlResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.database_name is not None and
            self.container_name is not None and
            self.stored_procedure_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqlstoredprocedure())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None and
              self.user_defined_function_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqluserdefinedfunction())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None and
              self.trigger_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqltrigger())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqlcontainer())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqlcontainerthroughput())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['sql_resources'] = self.format_item(self.listsqlstoredprocedure())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['sql_resources'] = self.format_item(self.listsqluserdefinedfunction())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['sql_resources'] = self.format_item(self.listsqltrigger())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqldatabase())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['sql_resources'] = self.format_item(self.getsqldatabasethroughput())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['sql_resources'] = self.format_item(self.listsqlcontainer())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['sql_resources'] = self.format_item(self.listsqldatabase())
        return self.results

    def getsqlstoredprocedure(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqlstored_procedure(resource_group_name=self.resource_group_name,
                                                                              account_name=self.account_name,
                                                                              database_name=self.database_name,
                                                                              container_name=self.container_name,
                                                                              stored_procedure_name=self.stored_procedure_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsqluserdefinedfunction(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqluser_defined_function(resource_group_name=self.resource_group_name,
                                                                                   account_name=self.account_name,
                                                                                   database_name=self.database_name,
                                                                                   container_name=self.container_name,
                                                                                   user_defined_function_name=self.user_defined_function_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsqltrigger(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqltrigger(resource_group_name=self.resource_group_name,
                                                                     account_name=self.account_name,
                                                                     database_name=self.database_name,
                                                                     container_name=self.container_name,
                                                                     trigger_name=self.trigger_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsqlcontainer(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqlcontainer(resource_group_name=self.resource_group_name,
                                                                       account_name=self.account_name,
                                                                       database_name=self.database_name,
                                                                       container_name=self.container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsqlcontainerthroughput(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqlcontainer_throughput(resource_group_name=self.resource_group_name,
                                                                                  account_name=self.account_name,
                                                                                  database_name=self.database_name,
                                                                                  container_name=self.container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsqlstoredprocedure(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.list_sqlstored_procedure(resource_group_name=self.resource_group_name,
                                                                               account_name=self.account_name,
                                                                               database_name=self.database_name,
                                                                               container_name=self.container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsqluserdefinedfunction(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.list_sqluser_defined_function(resource_group_name=self.resource_group_name,
                                                                                    account_name=self.account_name,
                                                                                    database_name=self.database_name,
                                                                                    container_name=self.container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsqltrigger(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.list_sqltrigger(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      database_name=self.database_name,
                                                                      container_name=self.container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsqldatabase(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqldatabase(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsqldatabasethroughput(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.get_sqldatabase_throughput(resource_group_name=self.resource_group_name,
                                                                                 account_name=self.account_name,
                                                                                 database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsqlcontainer(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.list_sqlcontainer(resource_group_name=self.resource_group_name,
                                                                        account_name=self.account_name,
                                                                        database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsqldatabase(self):
        response = None

        try:
            response = self.mgmt_client.sql_resources.list_sqldatabase(resource_group_name=self.resource_group_name,
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
    AzureRMSqlResourceInfo()


if __name__ == '__main__':
    main()
