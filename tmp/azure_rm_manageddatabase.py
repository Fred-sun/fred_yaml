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
module: azure_rm_manageddatabase
version_added: '2.9'
short_description: Manage Azure ManagedDatabase instance.
description:
  - 'Create, update and delete instance of Azure ManagedDatabase.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  database_name:
    description:
      - The name of the database.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  collation:
    description:
      - Collation of the managed database.
    type: str
  restore_point_in_time:
    description:
      - >-
        Conditional. If createMode is PointInTimeRestore, this value is
        required. Specifies the point in time (ISO8601 format) of the source
        database that will be restored to create the new database.
    type: str
  catalog_collation:
    description:
      - Collation of the metadata catalog.
    type: str
    choices:
      - DATABASE_DEFAULT
      - SQL_Latin1_General_CP1_CI_AS
  create_mode:
    description:
      - >-
        Managed database create mode. PointInTimeRestore: Create a database by
        restoring a point in time backup of an existing database.
        SourceDatabaseName, SourceManagedInstanceName and PointInTime must be
        specified. RestoreExternalBackup: Create a database by restoring from
        external backup files. Collation, StorageContainerUri and
        StorageContainerSasToken must be specified. Recovery: Creates a database
        by restoring a geo-replicated backup. RecoverableDatabaseId must be
        specified as the recoverable database resource ID to restore.
        RestoreLongTermRetentionBackup: Create a database by restoring from a
        long term retention backup (longTermRetentionBackupResourceId required).
    type: str
    choices:
      - Default
      - RestoreExternalBackup
      - PointInTimeRestore
      - Recovery
      - RestoreLongTermRetentionBackup
  storage_container_uri:
    description:
      - >-
        Conditional. If createMode is RestoreExternalBackup, this value is
        required. Specifies the uri of the storage container where backups for
        this restore are stored.
    type: str
  source_database_id:
    description:
      - >-
        The resource identifier of the source database associated with create
        operation of this database.
    type: str
  restorable_dropped_database_id:
    description:
      - >-
        The restorable dropped database resource id to restore when creating
        this database.
    type: str
  storage_container_sas_token:
    description:
      - >-
        Conditional. If createMode is RestoreExternalBackup, this value is
        required. Specifies the storage container sas token.
    type: str
  recoverable_database_id:
    description:
      - >-
        The resource identifier of the recoverable database associated with
        create operation of this database.
    type: str
  long_term_retention_backup_resource_id:
    description:
      - >-
        The name of the Long Term Retention backup to be used for restore of
        this managed database.
    type: str
  auto_complete_restore:
    description:
      - Whether to auto complete restore of this managed database.
    type: bool
  last_backup_name:
    description:
      - Last backup file name for restore of this managed database.
    type: str
  state:
    description:
      - Assert the state of the ManagedDatabase.
      - >-
        Use C(present) to create or update an ManagedDatabase and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Creates a new managed database by restoring from an external backup
      azure_rm_manageddatabase: 
        database_name: managedDatabase
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        location: southeastasia
        properties:
          auto_complete_restore: true
          collation: SQL_Latin1_General_CP1_CI_AS
          create_mode: RestoreExternalBackup
          last_backup_name: last_backup_name
          storage_container_sas_token: sv=2015-12-11&sr=c&sp=rl&sig=1234
          storage_container_uri: 'https://myaccountname.blob.core.windows.net/backups'
        

    - name: Creates a new managed database from restoring a geo-replicated backup
      azure_rm_manageddatabase: 
        database_name: testdb_recovered
        managed_instance_name: server1
        resource_group_name: Default-SQL-SouthEastAsia
        location: southeastasia
        properties:
          create_mode: Recovery
          recoverable_database_id: >-
            /subscriptions/11111111-2222-3333-4444-555555555555/resourceGroups/Default-SQL-WestEurope/providers/Microsoft.Sql/managedInstances/testsvr/recoverableDatabases/testdb
        

    - name: Creates a new managed database from restoring a long term retention backup
      azure_rm_manageddatabase: 
        database_name: managedDatabase
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        location: southeastasia
        properties:
          collation: SQL_Latin1_General_CP1_CI_AS
          create_mode: RestoreExternalBackup
          storage_container_sas_token: sv=2015-12-11&sr=c&sp=rl&sig=1234
          storage_container_uri: 'https://myaccountname.blob.core.windows.net/backups'
        

    - name: Creates a new managed database using point in time restore
      azure_rm_manageddatabase: 
        database_name: managedDatabase
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        location: southeastasia
        properties:
          create_mode: PointInTimeRestore
          restore_point_in_time: '2017-07-14T05:35:31.503Z'
          source_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/managedInstances/testsvr/databases/testdb
        

    - name: Creates a new managed database with maximal properties
      azure_rm_manageddatabase: 
        database_name: managedDatabase
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        location: southeastasia
        tags:
          tag_key1: TagValue1
        

    - name: Creates a new managed database with minimal properties
      azure_rm_manageddatabase: 
        database_name: managedDatabase
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        location: southeastasia
        

    - name: Delete managed database
      azure_rm_manageddatabase: 
        database_name: testdb
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        

    - name: Updates a managed database with maximal properties
      azure_rm_manageddatabase: 
        database_name: testdb
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        tags:
          tag_key1: TagValue1
        

    - name: Updates a managed database with minimal properties
      azure_rm_manageddatabase: 
        database_name: testdb
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        tags:
          tag_key1: TagValue1
        

'''

RETURN = '''
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
collation:
  description:
    - Collation of the managed database.
  returned: always
  type: str
  sample: null
status:
  description:
    - Status of the database.
  returned: always
  type: str
  sample: null
creation_date:
  description:
    - Creation date of the database.
  returned: always
  type: str
  sample: null
earliest_restore_point:
  description:
    - Earliest restore point in time for point in time restore.
  returned: always
  type: str
  sample: null
restore_point_in_time:
  description:
    - >-
      Conditional. If createMode is PointInTimeRestore, this value is required.
      Specifies the point in time (ISO8601 format) of the source database that
      will be restored to create the new database.
  returned: always
  type: str
  sample: null
default_secondary_location:
  description:
    - Geo paired region.
  returned: always
  type: str
  sample: null
catalog_collation:
  description:
    - Collation of the metadata catalog.
  returned: always
  type: str
  sample: null
create_mode:
  description:
    - >-
      Managed database create mode. PointInTimeRestore: Create a database by
      restoring a point in time backup of an existing database.
      SourceDatabaseName, SourceManagedInstanceName and PointInTime must be
      specified. RestoreExternalBackup: Create a database by restoring from
      external backup files. Collation, StorageContainerUri and
      StorageContainerSasToken must be specified. Recovery: Creates a database
      by restoring a geo-replicated backup. RecoverableDatabaseId must be
      specified as the recoverable database resource ID to restore.
      RestoreLongTermRetentionBackup: Create a database by restoring from a long
      term retention backup (longTermRetentionBackupResourceId required).
  returned: always
  type: str
  sample: null
storage_container_uri:
  description:
    - >-
      Conditional. If createMode is RestoreExternalBackup, this value is
      required. Specifies the uri of the storage container where backups for
      this restore are stored.
  returned: always
  type: str
  sample: null
source_database_id:
  description:
    - >-
      The resource identifier of the source database associated with create
      operation of this database.
  returned: always
  type: str
  sample: null
restorable_dropped_database_id:
  description:
    - >-
      The restorable dropped database resource id to restore when creating this
      database.
  returned: always
  type: str
  sample: null
storage_container_sas_token:
  description:
    - >-
      Conditional. If createMode is RestoreExternalBackup, this value is
      required. Specifies the storage container sas token.
  returned: always
  type: str
  sample: null
failover_group_id:
  description:
    - >-
      Instance Failover Group resource identifier that this managed database
      belongs to.
  returned: always
  type: str
  sample: null
recoverable_database_id:
  description:
    - >-
      The resource identifier of the recoverable database associated with create
      operation of this database.
  returned: always
  type: str
  sample: null
long_term_retention_backup_resource_id:
  description:
    - >-
      The name of the Long Term Retention backup to be used for restore of this
      managed database.
  returned: always
  type: str
  sample: null
auto_complete_restore:
  description:
    - Whether to auto complete restore of this managed database.
  returned: always
  type: bool
  sample: null
last_backup_name:
  description:
    - Last backup file name for restore of this managed database.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagedDatabase(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            collation=dict(
                type='str',
                disposition='/collation'
            ),
            restore_point_in_time=dict(
                type='str',
                disposition='/restore_point_in_time'
            ),
            catalog_collation=dict(
                type='str',
                disposition='/catalog_collation',
                choices=['DATABASE_DEFAULT',
                         'SQL_Latin1_General_CP1_CI_AS']
            ),
            create_mode=dict(
                type='str',
                disposition='/create_mode',
                choices=['Default',
                         'RestoreExternalBackup',
                         'PointInTimeRestore',
                         'Recovery',
                         'RestoreLongTermRetentionBackup']
            ),
            storage_container_uri=dict(
                type='str',
                disposition='/storage_container_uri'
            ),
            source_database_id=dict(
                type='str',
                disposition='/source_database_id'
            ),
            restorable_dropped_database_id=dict(
                type='str',
                disposition='/restorable_dropped_database_id'
            ),
            storage_container_sas_token=dict(
                type='str',
                disposition='/storage_container_sas_token'
            ),
            recoverable_database_id=dict(
                type='str',
                disposition='/recoverable_database_id'
            ),
            long_term_retention_backup_resource_id=dict(
                type='str',
                disposition='/long_term_retention_backup_resource_id'
            ),
            auto_complete_restore=dict(
                type='bool',
                disposition='/auto_complete_restore'
            ),
            last_backup_name=dict(
                type='str',
                disposition='/last_backup_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.database_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedDatabase, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                     supports_check_mode=True,
                                                     supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-02-preview')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.managed_databases.create_or_update(resource_group_name=self.resource_group_name,
                                                                           managed_instance_name=self.managed_instance_name,
                                                                           database_name=self.database_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedDatabase instance.')
            self.fail('Error creating the ManagedDatabase instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_databases.delete(resource_group_name=self.resource_group_name,
                                                                 managed_instance_name=self.managed_instance_name,
                                                                 database_name=self.database_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagedDatabase instance.')
            self.fail('Error deleting the ManagedDatabase instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_databases.get(resource_group_name=self.resource_group_name,
                                                              managed_instance_name=self.managed_instance_name,
                                                              database_name=self.database_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedDatabase()


if __name__ == '__main__':
    main()
