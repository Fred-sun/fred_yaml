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
module: azure_rm_restorepoint_info
version_added: '2.9'
short_description: Get RestorePoint info.
description:
  - Get info of RestorePoint.
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
  database_name:
    description:
      - The name of the database.
    required: true
    type: str
  restore_point_name:
    description:
      - The name of the restore point.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List database restore points.
      azure_rm_restorepoint_info: 
        database_name: '3481'
        resource_group_name: sqlcrudtest-6730
        server_name: sqlcrudtest-9007
        

    - name: List datawarehouse database restore points.
      azure_rm_restorepoint_info: 
        database_name: testDatabase
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testserver
        

    - name: Gets a database restore point.
      azure_rm_restorepoint_info: 
        database_name: testDatabase
        resource_group_name: Default-SQL-SouthEastAsia
        restore_point_name: '131546477590000000'
        server_name: testserver
        

    - name: Gets a datawarehouse database restore point.
      azure_rm_restorepoint_info: 
        database_name: testDatabase
        resource_group_name: Default-SQL-SouthEastAsia
        restore_point_name: '131546477590000000'
        server_name: testserver
        

'''

RETURN = '''
restore_points:
  description: >-
    A list of dict results where the key is the name of the RestorePoint and the
    values are the facts for that RestorePoint.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
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
        restore_point_type:
          description:
            - The type of restore point
          returned: always
          type: sealed-choice
          sample: null
        earliest_restore_date:
          description:
            - The earliest time to which this database can be restored
          returned: always
          type: str
          sample: null
        restore_point_creation_date:
          description:
            - The time the backup was taken
          returned: always
          type: str
          sample: null
        restore_point_label:
          description:
            - The label of restore point for backup request by user
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
        - Resource location.
      returned: always
      type: str
      sample: null
    restore_point_type:
      description:
        - The type of restore point
      returned: always
      type: sealed-choice
      sample: null
    earliest_restore_date:
      description:
        - The earliest time to which this database can be restored
      returned: always
      type: str
      sample: null
    restore_point_creation_date:
      description:
        - The time the backup was taken
      returned: always
      type: str
      sample: null
    restore_point_label:
      description:
        - The label of restore point for backup request by user
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


class AzureRMRestorePointInfo(AzureRMModuleBase):
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
            database_name=dict(
                type='str',
                required=True
            ),
            restore_point_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.restore_point_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRestorePointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.restore_point_name is not None):
            self.results['restore_points'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['restore_points'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.restore_points.get(resource_group_name=self.resource_group_name,
                                                           server_name=self.server_name,
                                                           database_name=self.database_name,
                                                           restore_point_name=self.restore_point_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.restore_points.list_by_database(resource_group_name=self.resource_group_name,
                                                                        server_name=self.server_name,
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
    AzureRMRestorePointInfo()


if __name__ == '__main__':
    main()
