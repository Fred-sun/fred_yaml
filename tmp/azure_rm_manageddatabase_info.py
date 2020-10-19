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
module: azure_rm_manageddatabase_info
version_added: '2.9'
short_description: Get ManagedDatabase info.
description:
  - Get info of ManagedDatabase.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List databases by managed instances
      azure_rm_manageddatabase_info: 
        managed_instance_name: managedInstance
        resource_group_name: Test1
        

    - name: Gets a managed database
      azure_rm_manageddatabase_info: 
        database_name: managedDatabase
        managed_instance_name: managedInstance
        resource_group_name: Test1
        

    - name: List inaccessible managed databases by managed instances
      azure_rm_manageddatabase_info: 
        managed_instance_name: testcl
        resource_group_name: testrg
        

'''

RETURN = '''
managed_databases:
  description: >-
    A list of dict results where the key is the name of the ManagedDatabase and
    the values are the facts for that ManagedDatabase.
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
              Conditional. If createMode is PointInTimeRestore, this value is
              required. Specifies the point in time (ISO8601 format) of the
              source database that will be restored to create the new database.
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
              Managed database create mode. PointInTimeRestore: Create a
              database by restoring a point in time backup of an existing
              database. SourceDatabaseName, SourceManagedInstanceName and
              PointInTime must be specified. RestoreExternalBackup: Create a
              database by restoring from external backup files. Collation,
              StorageContainerUri and StorageContainerSasToken must be
              specified. Recovery: Creates a database by restoring a
              geo-replicated backup. RecoverableDatabaseId must be specified as
              the recoverable database resource ID to restore.
              RestoreLongTermRetentionBackup: Create a database by restoring
              from a long term retention backup
              (longTermRetentionBackupResourceId required).
          returned: always
          type: str
          sample: null
        storage_container_uri:
          description:
            - >-
              Conditional. If createMode is RestoreExternalBackup, this value is
              required. Specifies the uri of the storage container where backups
              for this restore are stored.
          returned: always
          type: str
          sample: null
        source_database_id:
          description:
            - >-
              The resource identifier of the source database associated with
              create operation of this database.
          returned: always
          type: str
          sample: null
        restorable_dropped_database_id:
          description:
            - >-
              The restorable dropped database resource id to restore when
              creating this database.
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
              Instance Failover Group resource identifier that this managed
              database belongs to.
          returned: always
          type: str
          sample: null
        recoverable_database_id:
          description:
            - >-
              The resource identifier of the recoverable database associated
              with create operation of this database.
          returned: always
          type: str
          sample: null
        long_term_retention_backup_resource_id:
          description:
            - >-
              The name of the Long Term Retention backup to be used for restore
              of this managed database.
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
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
          Conditional. If createMode is PointInTimeRestore, this value is
          required. Specifies the point in time (ISO8601 format) of the source
          database that will be restored to create the new database.
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
          StorageContainerSasToken must be specified. Recovery: Creates a
          database by restoring a geo-replicated backup. RecoverableDatabaseId
          must be specified as the recoverable database resource ID to restore.
          RestoreLongTermRetentionBackup: Create a database by restoring from a
          long term retention backup (longTermRetentionBackupResourceId
          required).
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
          The restorable dropped database resource id to restore when creating
          this database.
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
          The resource identifier of the recoverable database associated with
          create operation of this database.
      returned: always
      type: str
      sample: null
    long_term_retention_backup_resource_id:
      description:
        - >-
          The name of the Long Term Retention backup to be used for restore of
          this managed database.
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


class AzureRMManagedDatabaseInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.database_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-02-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedDatabaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-02-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.database_name is not None):
            self.results['managed_databases'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['managed_databases'] = self.format_item(self.listbyinstance())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['managed_databases'] = self.format_item(self.listinaccessiblebyinstance())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_databases.get(resource_group_name=self.resource_group_name,
                                                              managed_instance_name=self.managed_instance_name,
                                                              database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstance(self):
        response = None

        try:
            response = self.mgmt_client.managed_databases.list_by_instance(resource_group_name=self.resource_group_name,
                                                                           managed_instance_name=self.managed_instance_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listinaccessiblebyinstance(self):
        response = None

        try:
            response = self.mgmt_client.managed_databases.list_inaccessible_by_instance(resource_group_name=self.resource_group_name,
                                                                                        managed_instance_name=self.managed_instance_name)
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
    AzureRMManagedDatabaseInfo()


if __name__ == '__main__':
    main()
