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
module: azure_rm_restorabledroppeddatabase_info
version_added: '2.9'
short_description: Get RestorableDroppedDatabase info.
description:
  - Get info of RestorableDroppedDatabase.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  restorable_droppeded_database_id:
    description:
      - >-
        The id of the deleted database in the form of
        databaseName,deletionTimeInFileTimeFormat
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a restorable dropped database
      azure_rm_restorabledroppeddatabase_info: 
        resource_group_name: restorabledroppeddatabasetest-1257
        restorable_droppeded_database_id: 'restorabledroppeddatabasetest-7654,131403269876900000'
        server_name: restorabledroppeddatabasetest-2389
        

    - name: Get list of restorable dropped databases
      azure_rm_restorabledroppeddatabase_info: 
        resource_group_name: restorabledroppeddatabasetest-1349
        server_name: restorabledroppeddatabasetest-1840
        

'''

RETURN = '''
restorable_dropped_databases:
  description: >-
    A list of dict results where the key is the name of the
    RestorableDroppedDatabase and the values are the facts for that
    RestorableDroppedDatabase.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    database_name:
      description:
        - The name of the database
      returned: always
      type: str
      sample: null
    edition:
      description:
        - The edition of the database
      returned: always
      type: str
      sample: null
    max_size_bytes:
      description:
        - The max size in bytes of the database
      returned: always
      type: str
      sample: null
    service_level_objective:
      description:
        - The service level objective name of the database
      returned: always
      type: str
      sample: null
    elastic_pool_name:
      description:
        - The elastic pool name of the database
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of the database (ISO8601 format)
      returned: always
      type: str
      sample: null
    deletion_date:
      description:
        - The deletion date of the database (ISO8601 format)
      returned: always
      type: str
      sample: null
    earliest_restore_date:
      description:
        - The earliest restore date of the database (ISO8601 format)
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of restorable dropped databases
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - The geo-location where the resource lives
          returned: always
          type: str
          sample: null
        database_name:
          description:
            - The name of the database
          returned: always
          type: str
          sample: null
        edition:
          description:
            - The edition of the database
          returned: always
          type: str
          sample: null
        max_size_bytes:
          description:
            - The max size in bytes of the database
          returned: always
          type: str
          sample: null
        service_level_objective:
          description:
            - The service level objective name of the database
          returned: always
          type: str
          sample: null
        elastic_pool_name:
          description:
            - The elastic pool name of the database
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of the database (ISO8601 format)
          returned: always
          type: str
          sample: null
        deletion_date:
          description:
            - The deletion date of the database (ISO8601 format)
          returned: always
          type: str
          sample: null
        earliest_restore_date:
          description:
            - The earliest restore date of the database (ISO8601 format)
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRestorableDroppedDatabaseInfo(AzureRMModuleBase):
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
            restorable_droppeded_database_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.restorable_droppeded_database_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRestorableDroppedDatabaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.restorable_droppeded_database_id is not None):
            self.results['restorable_dropped_databases'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['restorable_dropped_databases'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.restorable_dropped_databases.get(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         restorable_droppeded_database_id=self.restorable_droppeded_database_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.restorable_dropped_databases.list_by_server(resource_group_name=self.resource_group_name,
                                                                                    server_name=self.server_name)
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
    AzureRMRestorableDroppedDatabaseInfo()


if __name__ == '__main__':
    main()
