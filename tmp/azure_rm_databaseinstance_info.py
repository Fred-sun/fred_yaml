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
module: azure_rm_databaseinstance_info
version_added: '2.9'
short_description: Get DatabaseInstance info.
description:
  - Get info of DatabaseInstance.
options:
  resource_group_name:
    description:
      - Name of the Azure Resource Group that migrate project is part of.
    required: true
    type: str
  migrate_project_name:
    description:
      - Name of the Azure Migrate project.
    required: true
    type: str
  continuation_token:
    description:
      - The continuation token.
    type: str
  page_size:
    description:
      - >-
        The number of items to be returned in a single page. This value is
        honored only if it is less than the 100.
    type: integer
  acceptlanguage:
    description:
      - >-
        Standard request header. Used by service to respond to client in
        appropriate language.
    required: true
    type: str
  database_instance_name:
    description:
      - Unique name of a database instance in Azure migration hub.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DatabaseInstances_List
      azure_rm_databaseinstance_info: 
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

    - name: DatabaseInstances_Get
      azure_rm_databaseinstance_info: 
        database_instance_name: myinstance
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
database_instances:
  description: >-
    A list of dict results where the key is the name of the DatabaseInstance and
    the values are the facts for that DatabaseInstance.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Gets or sets the database instances.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Gets or sets the relative URL to get to this REST resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Gets or sets the name of this REST resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Gets the type of this REST resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Gets or sets the properties of the machine.
          returned: always
          type: dict
          sample: null
          contains:
            discovery_data:
              description:
                - >-
                  Gets or sets the assessment details of the database instance
                  published by various sources.
              returned: always
              type: list
              sample: null
              contains:
                last_updated_time:
                  description:
                    - >-
                      Gets or sets the time of the last modification of the
                      database instance details.
                  returned: always
                  type: str
                  sample: null
                instance_id:
                  description:
                    - Gets or sets the database instance Id.
                  returned: always
                  type: str
                  sample: null
                enqueue_time:
                  description:
                    - Gets or sets the time the message was enqueued.
                  returned: always
                  type: str
                  sample: null
                solution_name:
                  description:
                    - Gets or sets the name of the solution that sent the data.
                  returned: always
                  type: str
                  sample: null
                instance_name:
                  description:
                    - Gets or sets the database instance name.
                  returned: always
                  type: str
                  sample: null
                instance_version:
                  description:
                    - Gets or sets the database instance version.
                  returned: always
                  type: str
                  sample: null
                instance_type:
                  description:
                    - Gets or sets the database instance type.
                  returned: always
                  type: str
                  sample: null
                host_name:
                  description:
                    - Gets or sets the host name of the database server.
                  returned: always
                  type: str
                  sample: null
                ip_address:
                  description:
                    - >-
                      Gets or sets the IP addresses of the database server. IP
                      addresses could be IP V4 or IP V6.
                  returned: always
                  type: str
                  sample: null
                port_number:
                  description:
                    - Gets or sets the port number of the database server.
                  returned: always
                  type: integer
                  sample: null
                extended_info:
                  description:
                    - >-
                      Gets or sets the extended properties of the database
                      server.
                  returned: always
                  type: dictionary
                  sample: null
            summary:
              description:
                - >-
                  Gets or sets the database instances summary per solution. The
                  key of dictionary is the solution name and value is the
                  corresponding database instance summary object.
              returned: always
              type: dictionary
              sample: null
            last_updated_time:
              description:
                - >-
                  Gets or sets the time of the last modification of the
                  database.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Gets or sets the value of nextLink.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Gets or sets the relative URL to get to this REST resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Gets or sets the name of this REST resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Gets the type of this REST resource.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Gets or sets the properties of the machine.
      returned: always
      type: dict
      sample: null
      contains:
        discovery_data:
          description:
            - >-
              Gets or sets the assessment details of the database instance
              published by various sources.
          returned: always
          type: list
          sample: null
          contains:
            last_updated_time:
              description:
                - >-
                  Gets or sets the time of the last modification of the database
                  instance details.
              returned: always
              type: str
              sample: null
            instance_id:
              description:
                - Gets or sets the database instance Id.
              returned: always
              type: str
              sample: null
            enqueue_time:
              description:
                - Gets or sets the time the message was enqueued.
              returned: always
              type: str
              sample: null
            solution_name:
              description:
                - Gets or sets the name of the solution that sent the data.
              returned: always
              type: str
              sample: null
            instance_name:
              description:
                - Gets or sets the database instance name.
              returned: always
              type: str
              sample: null
            instance_version:
              description:
                - Gets or sets the database instance version.
              returned: always
              type: str
              sample: null
            instance_type:
              description:
                - Gets or sets the database instance type.
              returned: always
              type: str
              sample: null
            host_name:
              description:
                - Gets or sets the host name of the database server.
              returned: always
              type: str
              sample: null
            ip_address:
              description:
                - >-
                  Gets or sets the IP addresses of the database server. IP
                  addresses could be IP V4 or IP V6.
              returned: always
              type: str
              sample: null
            port_number:
              description:
                - Gets or sets the port number of the database server.
              returned: always
              type: integer
              sample: null
            extended_info:
              description:
                - Gets or sets the extended properties of the database server.
              returned: always
              type: dictionary
              sample: null
        summary:
          description:
            - >-
              Gets or sets the database instances summary per solution. The key
              of dictionary is the solution name and value is the corresponding
              database instance summary object.
          returned: always
          type: dictionary
          sample: null
        last_updated_time:
          description:
            - Gets or sets the time of the last modification of the database.
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
    from azure.mgmt.azure import Azure Migrate Hub
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDatabaseInstanceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            migrate_project_name=dict(
                type='str',
                required=True
            ),
            continuation_token=dict(
                type='str'
            ),
            page_size=dict(
                type='integer'
            ),
            acceptlanguage=dict(
                type='str',
                required=True
            ),
            database_instance_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.migrate_project_name = None
        self.continuation_token = None
        self.page_size = None
        self.acceptlanguage = None
        self.database_instance_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDatabaseInstanceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Migrate Hub,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.migrate_project_name is not None and
            self.database_instance_name is not None):
            self.results['database_instances'] = self.format_item(self.getdatabaseinstance())
        elif (self.resource_group_name is not None and
              self.migrate_project_name is not None):
            self.results['database_instances'] = self.format_item(self.enumeratedatabaseinstance())
        return self.results

    def getdatabaseinstance(self):
        response = None

        try:
            response = self.mgmt_client.database_instances.get_database_instance(resource_group_name=self.resource_group_name,
                                                                                 migrate_project_name=self.migrate_project_name,
                                                                                 database_instance_name=self.database_instance_name,
                                                                                 acceptlanguage=self.acceptlanguage)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def enumeratedatabaseinstance(self):
        response = None

        try:
            response = self.mgmt_client.database_instances.enumerate_database_instance(resource_group_name=self.resource_group_name,
                                                                                       migrate_project_name=self.migrate_project_name,
                                                                                       continuation_token=self.continuation_token,
                                                                                       page_size=self.page_size,
                                                                                       acceptlanguage=self.acceptlanguage)
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
    AzureRMDatabaseInstanceInfo()


if __name__ == '__main__':
    main()
