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
module: azure_rm_database_info
version_added: '2.9'
short_description: Get Database info.
description:
  - Get info of Database.
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
    type: str
  filter:
    description:
      - An OData filter expression that describes a subset of metrics to return.
    type: str
  elastic_pool_name:
    description:
      - The name of the elastic pool.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List database usage metrics
      azure_rm_database_info: 
        database_name: '3481'
        resource_group_name: sqlcrudtest-6730
        server_name: sqlcrudtest-9007
        

    - name: Gets a list of databases.
      azure_rm_database_info: 
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        

    - name: Gets a database.
      azure_rm_database_info: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        

    - name: Gets a list of databases in an elastic pool.
      azure_rm_database_info: 
        elastic_pool_name: pool1
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        

    - name: Gets a list of inaccessible databases in a logical server
      azure_rm_database_info: 
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        

'''

RETURN = '''
databases:
  description: >-
    A list of dict results where the key is the name of the Database and the
    values are the facts for that Database.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          The list of metrics for the database.
          The list of metric definitions for the database.
          Array of results.
      returned: always
      type: list
      sample: null
      contains:
        start_time:
          description:
            - The start time for the metric (ISO-8601 format).
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The end time for the metric (ISO-8601 format).
          returned: always
          type: str
          sample: null
        time_grain:
          description:
            - The time step to be used to summarize the metric values.
          returned: always
          type: str
          sample: null
        unit:
          description:
            - The unit of the metric.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name information for the metric.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - The name of the database metric.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - The friendly name of the database metric.
              returned: always
              type: str
              sample: null
        metric_values:
          description:
            - The metric values for the specified time window and timestep.
          returned: always
          type: list
          sample: null
          contains:
            count:
              description:
                - The number of values for the metric.
              returned: always
              type: integer
              sample: null
            average:
              description:
                - The average value of the metric.
              returned: always
              type: number
              sample: null
            maximum:
              description:
                - The max value of the metric.
              returned: always
              type: number
              sample: null
            minimum:
              description:
                - The min value of the metric.
              returned: always
              type: number
              sample: null
            timestamp:
              description:
                - The metric timestamp (ISO-8601 format).
              returned: always
              type: str
              sample: null
            total:
              description:
                - The total value of the metric.
              returned: always
              type: number
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
        - >-
          Kind of database. This is metadata used for the Azure portal
          experience.
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
          Specifies the point in time (ISO8601 format) of the source database
          that will be restored to create the new database.
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
          The resource identifier of the long term retention backup associated
          with create operation of this database.
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
    restorable_dropped_database_id:
      description:
        - >-
          The resource identifier of the restorable dropped database associated
          with create operation of this database.
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
          Whether or not this database is zone redundant, which means the
          replicas of this database will be spread across multiple availability
          zones.
      returned: always
      type: bool
      sample: null
    license_type:
      description:
        - >-
          The license type to apply for this database. `LicenseIncluded` if you
          need a license, or `BasePrice` if you have a license and are eligible
          for the Azure Hybrid Benefit.
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
          This records the earliest start date and time that restore is
          available for this database (ISO8601 format).
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
        - >-
          The number of readonly secondary replicas associated with the
          database.
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
          Time in minutes after which database is automatically paused. A value
          of -1 means that automatic pause is disabled
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
        - >-
          Minimal capacity that database will always have allocated, if not
          paused
      returned: always
      type: number
      sample: null
    paused_date:
      description:
        - >-
          The date when database was paused by user configuration or
          action(ISO8601 format). Null if the database is ready.
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


class AzureRMDatabaseInfo(AzureRMModuleBase):
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
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            elastic_pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.filter = None
        self.elastic_pool_name = None

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
        super(AzureRMDatabaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.filter is not None):
            self.results['databases'] = self.format_item(self.listmetric())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['databases'] = self.format_item(self.listmetricdefinition())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['databases'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.elastic_pool_name is not None):
            self.results['databases'] = self.format_item(self.listbyelasticpool())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['databases'] = self.format_item(self.listbyserver())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['databases'] = self.format_item(self.listinaccessiblebyserver())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.databases.list_metric(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              database_name=self.database_name,
                                                              filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.databases.list_metric_definition(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.databases.get(resource_group_name=self.resource_group_name,
                                                      server_name=self.server_name,
                                                      database_name=self.database_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyelasticpool(self):
        response = None

        try:
            response = self.mgmt_client.databases.list_by_elastic_pool(resource_group_name=self.resource_group_name,
                                                                       server_name=self.server_name,
                                                                       elastic_pool_name=self.elastic_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.databases.list_by_server(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listinaccessiblebyserver(self):
        response = None

        try:
            response = self.mgmt_client.databases.list_inaccessible_by_server(resource_group_name=self.resource_group_name,
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
    AzureRMDatabaseInfo()


if __name__ == '__main__':
    main()
