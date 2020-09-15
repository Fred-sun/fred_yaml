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
module: azure_rm_database
version_added: '2.9'
short_description: Manage Azure Database instance.
description:
  - 'Create, update and delete instance of Azure Database.'
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
  location:
    description:
      - Resource location.
    type: str
  sku:
    description:
      - "The database SKU.\r"
      - "\r"
      - "The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands:\r"
      - "\r"
      - "```azurecli\r"
      - "az sql db list-editions -l <location> -o table\r"
      - "````\r"
      - "\r"
      - "```powershell\r"
      - "Get-AzSqlServerServiceObjective -Location <location>\r"
      - "````\r"
      - ''
      - The name and tier of the SKU.
    type: dict
    suboptions:
      name:
        description:
          - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
        required: true
        type: str
      tier:
        description:
          - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
        type: str
      size:
        description:
          - Size of the particular SKU
        type: str
      family:
        description:
          - >-
            If the service has different generations of hardware, for the same
            SKU, then that can be captured here.
        type: str
      capacity:
        description:
          - Capacity of the particular SKU.
        type: integer
  create_mode:
    description:
      - "Specifies the mode of database creation.\r"
      - "\r"
      - "Default: regular database creation.\r"
      - "\r"
      - "Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.\r"
      - "\r"
      - "Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.\r"
      - "\r"
      - "PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.\r"
      - "\r"
      - "Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.\r"
      - "\r"
      - "Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.\r"
      - "\r"
      - "RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.\r"
      - "\r"
      - >-
        Copy, Secondary, and RestoreLongTermRetentionBackup are not supported
        for DataWarehouse edition.
    type: str
    choices:
      - Default
      - Copy
      - Secondary
      - PointInTimeRestore
      - Restore
      - Recovery
      - RestoreExternalBackup
      - RestoreExternalBackupSecondary
      - RestoreLongTermRetentionBackup
      - OnlineSecondary
  collation:
    description:
      - The collation of the database.
    type: str
  max_size_bytes:
    description:
      - The max size of the database expressed in bytes.
    type: integer
  sample_name:
    description:
      - The name of the sample schema to apply when creating this database.
    type: str
    choices:
      - AdventureWorksLT
      - WideWorldImportersStd
      - WideWorldImportersFull
  elastic_pool_id:
    description:
      - The resource identifier of the elastic pool containing this database.
    type: str
  source_database_id:
    description:
      - >-
        The resource identifier of the source database associated with create
        operation of this database.
    type: str
  restore_point_in_time:
    description:
      - >-
        Specifies the point in time (ISO8601 format) of the source database that
        will be restored to create the new database.
    type: str
  source_database_deletion_date:
    description:
      - Specifies the time that the database was deleted.
    type: str
  recovery_services_recovery_point_id:
    description:
      - >-
        The resource identifier of the recovery point associated with create
        operation of this database.
    type: str
  long_term_retention_backup_resource_id:
    description:
      - >-
        The resource identifier of the long term retention backup associated
        with create operation of this database.
    type: str
  recoverable_database_id:
    description:
      - >-
        The resource identifier of the recoverable database associated with
        create operation of this database.
    type: str
  restorable_dropped_database_id:
    description:
      - >-
        The resource identifier of the restorable dropped database associated
        with create operation of this database.
    type: str
  catalog_collation:
    description:
      - Collation of the metadata catalog.
    type: str
    choices:
      - DATABASE_DEFAULT
      - SQL_Latin1_General_CP1_CI_AS
  zone_redundant:
    description:
      - >-
        Whether or not this database is zone redundant, which means the replicas
        of this database will be spread across multiple availability zones.
    type: bool
  license_type:
    description:
      - >-
        The license type to apply for this database. `LicenseIncluded` if you
        need a license, or `BasePrice` if you have a license and are eligible
        for the Azure Hybrid Benefit.
    type: str
    choices:
      - LicenseIncluded
      - BasePrice
  read_scale:
    description:
      - >-
        The state of read-only routing. If enabled, connections that have
        application intent set to readonly in their connection string may be
        routed to a readonly secondary replica in the same region.
    type: str
    choices:
      - Enabled
      - Disabled
  read_replica_count:
    description:
      - The number of readonly secondary replicas associated with the database.
    type: integer
  auto_pause_delay:
    description:
      - >-
        Time in minutes after which database is automatically paused. A value of
        -1 means that automatic pause is disabled
    type: integer
  storage_account_type:
    description:
      - >-
        The storage account type used to store backups for this database.
        Currently the only supported option is GRS (GeoRedundantStorage).
    type: str
    choices:
      - GRS
      - LRS
      - ZRS
  min_capacity:
    description:
      - 'Minimal capacity that database will always have allocated, if not paused'
    type: number
  state:
    description:
      - Assert the state of the Database.
      - >-
        Use C(present) to create or update an Database and C(absent) to delete
        it.
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
    - name: Creates a VCore database by specifying service objective name.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        sku:
          name: BC
          capacity: 2
          family: Gen4
        

    - name: Creates a VCore database by specifying sku name and capacity.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        sku:
          name: BC_Gen4
          capacity: 2
        

    - name: Creates a data warehouse by specifying service objective name.
      azure_rm_database: 
        database_name: testdw
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: westus
        sku:
          name: DW1000c
        

    - name: Creates a database as a copy.
      azure_rm_database: 
        database_name: dbcopy
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          create_mode: Copy
          source_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/servers/testsvr/databases/testdb
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database as an on-line secondary.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          create_mode: Secondary
          source_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-NorthEurope/providers/Microsoft.Sql/servers/testsvr1/databases/testdb
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database from PointInTimeRestore.
      azure_rm_database: 
        database_name: dbpitr
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          create_mode: PointInTimeRestore
          restore_point_in_time: '2017-07-14T05:35:31.503Z'
          source_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/servers/testsvr/databases/testdb
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database from recoverableDatabaseId.
      azure_rm_database: 
        database_name: dbrestore
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          create_mode: Restore
          restorable_dropped_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/servers/testsvr/restorableDroppedDatabases/testdb2,131444841315030000
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database from restore with database deletion time.
      azure_rm_database: 
        database_name: dbrestore
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          create_mode: Restore
          source_database_deletion_date: '2017-07-14T06:41:06.613Z'
          source_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/servers/testsvr/databases/testdb
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database from restore with restorableDroppedDatabaseId.
      azure_rm_database: 
        database_name: dbcopy
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          create_mode: Copy
          source_database_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/servers/testsvr/databases/testdb
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database with default mode.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        properties:
          collation: SQL_Latin1_General_CP1_CI_AS
          create_mode: Default
          max_size_bytes: 1073741824
        sku:
          name: S0
          tier: Standard
        

    - name: Creates a database with minimum number of parameters.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        location: southeastasia
        

    - name: Deletes a database.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        

    - name: Updates a database.
      azure_rm_database: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        properties:
          collation: SQL_Latin1_General_CP1_CI_AS
          max_size_bytes: 1073741824
        sku:
          name: S1
          tier: Standard
        

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
sku:
  description:
    - "The database SKU.\r\n\r\nThe list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands:\r\n\r\n```azurecli\r\naz sql db list-editions -l <location> -o table\r\n````\r\n\r\n```powershell\r\nGet-AzSqlServerServiceObjective -Location <location>\r\n````\r\n"
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
      returned: always
      type: str
      sample: null
    tier:
      description:
        - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
      returned: always
      type: str
      sample: null
    size:
      description:
        - Size of the particular SKU
      returned: always
      type: str
      sample: null
    family:
      description:
        - >-
          If the service has different generations of hardware, for the same
          SKU, then that can be captured here.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - Capacity of the particular SKU.
      returned: always
      type: integer
      sample: null
kind:
  description:
    - Kind of database. This is metadata used for the Azure portal experience.
  returned: always
  type: str
  sample: null
managed_by:
  description:
    - Resource that manages the database.
  returned: always
  type: str
  sample: null
create_mode:
  description:
    - "Specifies the mode of database creation.\r\n\r\nDefault: regular database creation.\r\n\r\nCopy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.\r\n\r\nSecondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.\r\n\r\nPointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.\r\n\r\nRecovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.\r\n\r\nRestore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.\r\n\r\nRestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.\r\n\r\nCopy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition."
  returned: always
  type: str
  sample: null
collation:
  description:
    - The collation of the database.
  returned: always
  type: str
  sample: null
max_size_bytes:
  description:
    - The max size of the database expressed in bytes.
  returned: always
  type: integer
  sample: null
sample_name:
  description:
    - The name of the sample schema to apply when creating this database.
  returned: always
  type: str
  sample: null
elastic_pool_id:
  description:
    - The resource identifier of the elastic pool containing this database.
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
status:
  description:
    - The status of the database.
  returned: always
  type: str
  sample: null
database_id:
  description:
    - The ID of the database.
  returned: always
  type: uuid
  sample: null
creation_date:
  description:
    - The creation date of the database (ISO8601 format).
  returned: always
  type: str
  sample: null
current_service_objective_name:
  description:
    - The current service level objective name of the database.
  returned: always
  type: str
  sample: null
requested_service_objective_name:
  description:
    - The requested service level objective name of the database.
  returned: always
  type: str
  sample: null
default_secondary_location:
  description:
    - The default secondary region for this database.
  returned: always
  type: str
  sample: null
failover_group_id:
  description:
    - Failover Group resource identifier that this database belongs to.
  returned: always
  type: str
  sample: null
restore_point_in_time:
  description:
    - >-
      Specifies the point in time (ISO8601 format) of the source database that
      will be restored to create the new database.
  returned: always
  type: str
  sample: null
source_database_deletion_date:
  description:
    - Specifies the time that the database was deleted.
  returned: always
  type: str
  sample: null
recovery_services_recovery_point_id:
  description:
    - >-
      The resource identifier of the recovery point associated with create
      operation of this database.
  returned: always
  type: str
  sample: null
long_term_retention_backup_resource_id:
  description:
    - >-
      The resource identifier of the long term retention backup associated with
      create operation of this database.
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
restorable_dropped_database_id:
  description:
    - >-
      The resource identifier of the restorable dropped database associated with
      create operation of this database.
  returned: always
  type: str
  sample: null
catalog_collation:
  description:
    - Collation of the metadata catalog.
  returned: always
  type: str
  sample: null
zone_redundant:
  description:
    - >-
      Whether or not this database is zone redundant, which means the replicas
      of this database will be spread across multiple availability zones.
  returned: always
  type: bool
  sample: null
license_type:
  description:
    - >-
      The license type to apply for this database. `LicenseIncluded` if you need
      a license, or `BasePrice` if you have a license and are eligible for the
      Azure Hybrid Benefit.
  returned: always
  type: str
  sample: null
max_log_size_bytes:
  description:
    - The max log size for this database.
  returned: always
  type: integer
  sample: null
earliest_restore_date:
  description:
    - >-
      This records the earliest start date and time that restore is available
      for this database (ISO8601 format).
  returned: always
  type: str
  sample: null
read_scale:
  description:
    - >-
      The state of read-only routing. If enabled, connections that have
      application intent set to readonly in their connection string may be
      routed to a readonly secondary replica in the same region.
  returned: always
  type: str
  sample: null
read_replica_count:
  description:
    - The number of readonly secondary replicas associated with the database.
  returned: always
  type: integer
  sample: null
current_sku:
  description:
    - The name and tier of the SKU.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
      returned: always
      type: str
      sample: null
    tier:
      description:
        - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
      returned: always
      type: str
      sample: null
    size:
      description:
        - Size of the particular SKU
      returned: always
      type: str
      sample: null
    family:
      description:
        - >-
          If the service has different generations of hardware, for the same
          SKU, then that can be captured here.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - Capacity of the particular SKU.
      returned: always
      type: integer
      sample: null
auto_pause_delay:
  description:
    - >-
      Time in minutes after which database is automatically paused. A value of
      -1 means that automatic pause is disabled
  returned: always
  type: integer
  sample: null
storage_account_type:
  description:
    - >-
      The storage account type used to store backups for this database.
      Currently the only supported option is GRS (GeoRedundantStorage).
  returned: always
  type: str
  sample: null
min_capacity:
  description:
    - 'Minimal capacity that database will always have allocated, if not paused'
  returned: always
  type: number
  sample: null
paused_date:
  description:
    - >-
      The date when database was paused by user configuration or action(ISO8601
      format). Null if the database is ready.
  returned: always
  type: str
  sample: null
resumed_date:
  description:
    - >-
      The date when database was resumed by user action or database login
      (ISO8601 format). Null if the database is paused.
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


class AzureRMDatabase(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    size=dict(
                        type='str',
                        disposition='size'
                    ),
                    family=dict(
                        type='str',
                        disposition='family'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            create_mode=dict(
                type='str',
                disposition='/create_mode',
                choices=['Default',
                         'Copy',
                         'Secondary',
                         'PointInTimeRestore',
                         'Restore',
                         'Recovery',
                         'RestoreExternalBackup',
                         'RestoreExternalBackupSecondary',
                         'RestoreLongTermRetentionBackup',
                         'OnlineSecondary']
            ),
            collation=dict(
                type='str',
                disposition='/collation'
            ),
            max_size_bytes=dict(
                type='integer',
                disposition='/max_size_bytes'
            ),
            sample_name=dict(
                type='str',
                disposition='/sample_name',
                choices=['AdventureWorksLT',
                         'WideWorldImportersStd',
                         'WideWorldImportersFull']
            ),
            elastic_pool_id=dict(
                type='str',
                disposition='/elastic_pool_id'
            ),
            source_database_id=dict(
                type='str',
                disposition='/source_database_id'
            ),
            restore_point_in_time=dict(
                type='str',
                disposition='/restore_point_in_time'
            ),
            source_database_deletion_date=dict(
                type='str',
                disposition='/source_database_deletion_date'
            ),
            recovery_services_recovery_point_id=dict(
                type='str',
                disposition='/recovery_services_recovery_point_id'
            ),
            long_term_retention_backup_resource_id=dict(
                type='str',
                disposition='/long_term_retention_backup_resource_id'
            ),
            recoverable_database_id=dict(
                type='str',
                disposition='/recoverable_database_id'
            ),
            restorable_dropped_database_id=dict(
                type='str',
                disposition='/restorable_dropped_database_id'
            ),
            catalog_collation=dict(
                type='str',
                disposition='/catalog_collation',
                choices=['DATABASE_DEFAULT',
                         'SQL_Latin1_General_CP1_CI_AS']
            ),
            zone_redundant=dict(
                type='bool',
                disposition='/zone_redundant'
            ),
            license_type=dict(
                type='str',
                disposition='/license_type',
                choices=['LicenseIncluded',
                         'BasePrice']
            ),
            read_scale=dict(
                type='str',
                disposition='/read_scale',
                choices=['Enabled',
                         'Disabled']
            ),
            read_replica_count=dict(
                type='integer',
                disposition='/read_replica_count'
            ),
            auto_pause_delay=dict(
                type='integer',
                disposition='/auto_pause_delay'
            ),
            storage_account_type=dict(
                type='str',
                disposition='/storage_account_type',
                choices=['GRS',
                         'LRS',
                         'ZRS']
            ),
            min_capacity=dict(
                type='number',
                disposition='/min_capacity'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDatabase, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2014-04-01')

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
            response = self.mgmt_client.databases.create_or_update(resource_group_name=self.resource_group_name,
                                                                   server_name=self.server_name,
                                                                   database_name=self.database_name,
                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Database instance.')
            self.fail('Error creating the Database instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.databases.delete(resource_group_name=self.resource_group_name,
                                                         server_name=self.server_name,
                                                         database_name=self.database_name)
        except CloudError as e:
            self.log('Error attempting to delete the Database instance.')
            self.fail('Error deleting the Database instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.databases.get(resource_group_name=self.resource_group_name,
                                                      server_name=self.server_name,
                                                      database_name=self.database_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDatabase()


if __name__ == '__main__':
    main()
