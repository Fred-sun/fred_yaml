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
module: azure_rm_longtermretentionmanagedinstancebackup_info
version_added: '2.9'
short_description: Get LongTermRetentionManagedInstanceBackup info.
description:
  - Get info of LongTermRetentionManagedInstanceBackup.
options:
  location_name:
    description:
      - The location of the database.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    type: str
  database_name:
    description:
      - The name of the managed database.
    type: str
  backup_name:
    description:
      - The backup name.
    type: str
  only_latest_per_database:
    description:
      - Whether or not to only get the latest backup for each database.
    type: bool
  database_state:
    description:
      - >-
        Whether to query against just live databases, just deleted databases, or
        all databases.
    type: str
    choices:
      - All
      - Live
      - Deleted
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get the long term retention backup of a managed database.
      azure_rm_longtermretentionmanagedinstancebackup_info: 
        backup_name: 55555555-6666-7777-8888-999999999999;131637960820000000
        database_name: testDatabase
        location_name: japaneast
        managed_instance_name: testInstance
        

    - name: Get all long term retention backups under the database.
      azure_rm_longtermretentionmanagedinstancebackup_info: 
        database_name: testDatabase
        location_name: japaneast
        managed_instance_name: testInstance
        

    - name: Get all long term retention backups under the managed instance.
      azure_rm_longtermretentionmanagedinstancebackup_info: 
        location_name: japaneast
        managed_instance_name: testInstance
        

    - name: Get all long term retention backups under the location.
      azure_rm_longtermretentionmanagedinstancebackup_info: 
        location_name: japaneast
        

    - name: Get the long term retention backup.
      azure_rm_longtermretentionmanagedinstancebackup_info: 
        backup_name: 55555555-6666-7777-8888-999999999999;131637960820000000
        database_name: testDatabase
        location_name: japaneast
        managed_instance_name: testInstance
        resource_group_name: testResourceGroup
        

'''

RETURN = '''
long_term_retention_managed_instance_backups:
  description: >-
    A list of dict results where the key is the name of the
    LongTermRetentionManagedInstanceBackup and the values are the facts for that
    LongTermRetentionManagedInstanceBackup.
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
    managed_instance_name:
      description:
        - The managed instance that the backup database belongs to.
      returned: always
      type: str
      sample: null
    managed_instance_create_time:
      description:
        - The create time of the instance.
      returned: always
      type: str
      sample: null
    database_name:
      description:
        - The name of the database the backup belong to
      returned: always
      type: str
      sample: null
    database_deletion_time:
      description:
        - The delete time of the database
      returned: always
      type: str
      sample: null
    backup_time:
      description:
        - The time the backup was taken
      returned: always
      type: str
      sample: null
    backup_expiration_time:
      description:
        - The time the long term retention backup will expire.
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
        managed_instance_name:
          description:
            - The managed instance that the backup database belongs to.
          returned: always
          type: str
          sample: null
        managed_instance_create_time:
          description:
            - The create time of the instance.
          returned: always
          type: str
          sample: null
        database_name:
          description:
            - The name of the database the backup belong to
          returned: always
          type: str
          sample: null
        database_deletion_time:
          description:
            - The delete time of the database
          returned: always
          type: str
          sample: null
        backup_time:
          description:
            - The time the backup was taken
          returned: always
          type: str
          sample: null
        backup_expiration_time:
          description:
            - The time the long term retention backup will expire.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLongTermRetentionManagedInstanceBackupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str'
            ),
            database_name=dict(
                type='str'
            ),
            backup_name=dict(
                type='str'
            ),
            only_latest_per_database=dict(
                type='bool'
            ),
            database_state=dict(
                type='str',
                choices=['All',
                         'Live',
                         'Deleted']
            ),
            resource_group_name=dict(
                type='str'
            )
        )

        self.location_name = None
        self.managed_instance_name = None
        self.database_name = None
        self.backup_name = None
        self.only_latest_per_database = None
        self.database_state = None
        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLongTermRetentionManagedInstanceBackupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.resource_group_name is not None and
            self.location_name is not None and
            self.managed_instance_name is not None and
            self.database_name is not None and
            self.backup_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.getbyresourcegroup())
        elif (self.resource_group_name is not None and
              self.location_name is not None and
              self.managed_instance_name is not None and
              self.database_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.listbyresourcegroupdatabase())
        elif (self.location_name is not None and
              self.managed_instance_name is not None and
              self.database_name is not None and
              self.backup_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.get())
        elif (self.location_name is not None and
              self.managed_instance_name is not None and
              self.database_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.listbydatabase())
        elif (self.resource_group_name is not None and
              self.location_name is not None and
              self.managed_instance_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.listbyresourcegroupinstance())
        elif (self.location_name is not None and
              self.managed_instance_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.listbyinstance())
        elif (self.resource_group_name is not None and
              self.location_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.listbyresourcegrouplocation())
        elif (self.location_name is not None):
            self.results['long_term_retention_managed_instance_backups'] = self.format_item(self.listbylocation())
        return self.results

    def getbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.get_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                                           location_name=self.location_name,
                                                                                                           managed_instance_name=self.managed_instance_name,
                                                                                                           database_name=self.database_name,
                                                                                                           backup_name=self.backup_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroupdatabase(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.list_by_resource_group_database(resource_group_name=self.resource_group_name,
                                                                                                                     location_name=self.location_name,
                                                                                                                     managed_instance_name=self.managed_instance_name,
                                                                                                                     database_name=self.database_name,
                                                                                                                     only_latest_per_database=self.only_latest_per_database,
                                                                                                                     database_state=self.database_state)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.get(location_name=self.location_name,
                                                                                         managed_instance_name=self.managed_instance_name,
                                                                                         database_name=self.database_name,
                                                                                         backup_name=self.backup_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.list_by_database(location_name=self.location_name,
                                                                                                      managed_instance_name=self.managed_instance_name,
                                                                                                      database_name=self.database_name,
                                                                                                      only_latest_per_database=self.only_latest_per_database,
                                                                                                      database_state=self.database_state)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroupinstance(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.list_by_resource_group_instance(resource_group_name=self.resource_group_name,
                                                                                                                     location_name=self.location_name,
                                                                                                                     managed_instance_name=self.managed_instance_name,
                                                                                                                     only_latest_per_database=self.only_latest_per_database,
                                                                                                                     database_state=self.database_state)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstance(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.list_by_instance(location_name=self.location_name,
                                                                                                      managed_instance_name=self.managed_instance_name,
                                                                                                      only_latest_per_database=self.only_latest_per_database,
                                                                                                      database_state=self.database_state)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegrouplocation(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.list_by_resource_group_location(resource_group_name=self.resource_group_name,
                                                                                                                     location_name=self.location_name,
                                                                                                                     only_latest_per_database=self.only_latest_per_database,
                                                                                                                     database_state=self.database_state)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.long_term_retention_managed_instance_backups.list_by_location(location_name=self.location_name,
                                                                                                      only_latest_per_database=self.only_latest_per_database,
                                                                                                      database_state=self.database_state)
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
    AzureRMLongTermRetentionManagedInstanceBackupInfo()


if __name__ == '__main__':
    main()
