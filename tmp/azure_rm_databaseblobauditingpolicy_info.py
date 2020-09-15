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
module: azure_rm_databaseblobauditingpolicy_info
version_added: '2.9'
short_description: Get DatabaseBlobAuditingPolicy info.
description:
  - Get info of DatabaseBlobAuditingPolicy.
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
  blobauditingpolicyname:
    description:
      - The name of the blob auditing policy.
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a database's blob auditing policy
      azure_rm_databaseblobauditingpolicy_info: 
        database_name: testdb
        resource_group_name: blobauditingtest-6852
        server_name: blobauditingtest-2080
        

    - name: List audit settings of a database
      azure_rm_databaseblobauditingpolicy_info: 
        database_name: testdb
        resource_group_name: blobauditingtest-6852
        server_name: blobauditingtest-2080
        

'''

RETURN = '''
database_blob_auditing_policies:
  description: >-
    A list of dict results where the key is the name of the
    DatabaseBlobAuditingPolicy and the values are the facts for that
    DatabaseBlobAuditingPolicy.
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
    kind:
      description:
        - Resource kind.
      returned: always
      type: str
      sample: null
    state:
      description:
        - >-
          Specifies the state of the policy. If state is Enabled,
          storageEndpoint or isAzureMonitorTargetEnabled are required.
      returned: always
      type: sealed-choice
      sample: null
    storage_endpoint:
      description:
        - >-
          Specifies the blob storage endpoint (e.g.
          https://MyAccount.blob.core.windows.net). If state is Enabled,
          storageEndpoint or isAzureMonitorTargetEnabled is required.
      returned: always
      type: str
      sample: null
    storage_account_access_key:
      description:
        - "Specifies the identifier key of the auditing storage account. \r\nIf state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage.\r\nPrerequisites for using managed identity authentication:\r\n1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD).\r\n2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity.\r\nFor more information, see [Auditing to storage using Managed Identity authentication](https://go.microsoft.com/fwlink/?linkid=2114355)"
      returned: always
      type: str
      sample: null
    retention_days:
      description:
        - >-
          Specifies the number of days to keep in the audit logs in the storage
          account.
      returned: always
      type: integer
      sample: null
    audit_actions_and_groups:
      description:
        - "Specifies the Actions-Groups and Actions to audit.\r\n\r\nThe recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins:\r\n\r\nBATCH_COMPLETED_GROUP,\r\nSUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,\r\nFAILED_DATABASE_AUTHENTICATION_GROUP.\r\n\r\nThis above combination is also the set that is configured by default when enabling auditing from the Azure portal.\r\n\r\nThe supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records):\r\n\r\nAPPLICATION_ROLE_CHANGE_PASSWORD_GROUP\r\nBACKUP_RESTORE_GROUP\r\nDATABASE_LOGOUT_GROUP\r\nDATABASE_OBJECT_CHANGE_GROUP\r\nDATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP\r\nDATABASE_OBJECT_PERMISSION_CHANGE_GROUP\r\nDATABASE_OPERATION_GROUP\r\nDATABASE_PERMISSION_CHANGE_GROUP\r\nDATABASE_PRINCIPAL_CHANGE_GROUP\r\nDATABASE_PRINCIPAL_IMPERSONATION_GROUP\r\nDATABASE_ROLE_MEMBER_CHANGE_GROUP\r\nFAILED_DATABASE_AUTHENTICATION_GROUP\r\nSCHEMA_OBJECT_ACCESS_GROUP\r\nSCHEMA_OBJECT_CHANGE_GROUP\r\nSCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP\r\nSCHEMA_OBJECT_PERMISSION_CHANGE_GROUP\r\nSUCCESSFUL_DATABASE_AUTHENTICATION_GROUP\r\nUSER_CHANGE_PASSWORD_GROUP\r\nBATCH_STARTED_GROUP\r\nBATCH_COMPLETED_GROUP\r\n\r\nThese are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs.\r\n\r\nFor more information, see [Database-Level Audit Action Groups](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-action-groups).\r\n\r\nFor Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are:\r\nSELECT\r\nUPDATE\r\nINSERT\r\nDELETE\r\nEXECUTE\r\nRECEIVE\r\nREFERENCES\r\n\r\nThe general form for defining an action to be audited is:\r\n{action} ON {object} BY {principal}\r\n\r\nNote that <object> in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms DATABASE::{db_name} and SCHEMA::{schema_name} are used, respectively.\r\n\r\nFor example:\r\nSELECT on dbo.myTable by public\r\nSELECT on DATABASE::myDatabase by public\r\nSELECT on SCHEMA::mySchema by public\r\n\r\nFor more information, see [Database-Level Audit Actions](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-actions)"
      returned: always
      type: list
      sample: null
    storage_account_subscription_id:
      description:
        - Specifies the blob storage subscription Id.
      returned: always
      type: uuid
      sample: null
    is_storage_secondary_key_in_use:
      description:
        - >-
          Specifies whether storageAccountAccessKey value is the storage's
          secondary key.
      returned: always
      type: bool
      sample: null
    is_azure_monitor_target_enabled:
      description:
        - "Specifies whether audit events are sent to Azure Monitor. \r\nIn order to send the events to Azure Monitor, specify 'state' as 'Enabled' and 'isAzureMonitorTargetEnabled' as true.\r\n\r\nWhen using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created.\r\nNote that for server level audit you should use the 'master' database as {databaseName}.\r\n\r\nDiagnostic Settings URI format:\r\nPUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview\r\n\r\nFor more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)\r\nor [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)\r\n"
      returned: always
      type: bool
      sample: null
    queue_delay_ms:
      description:
        - "Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed.\r\nThe default minimum value is 1000 (1 second). The maximum is 2,147,483,647."
      returned: always
      type: integer
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - Resource kind.
          returned: always
          type: str
          sample: null
        state:
          description:
            - >-
              Specifies the state of the policy. If state is Enabled,
              storageEndpoint or isAzureMonitorTargetEnabled are required.
          returned: always
          type: sealed-choice
          sample: null
        storage_endpoint:
          description:
            - >-
              Specifies the blob storage endpoint (e.g.
              https://MyAccount.blob.core.windows.net). If state is Enabled,
              storageEndpoint or isAzureMonitorTargetEnabled is required.
          returned: always
          type: str
          sample: null
        storage_account_access_key:
          description:
            - "Specifies the identifier key of the auditing storage account. \r\nIf state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage.\r\nPrerequisites for using managed identity authentication:\r\n1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD).\r\n2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity.\r\nFor more information, see [Auditing to storage using Managed Identity authentication](https://go.microsoft.com/fwlink/?linkid=2114355)"
          returned: always
          type: str
          sample: null
        retention_days:
          description:
            - >-
              Specifies the number of days to keep in the audit logs in the
              storage account.
          returned: always
          type: integer
          sample: null
        audit_actions_and_groups:
          description:
            - "Specifies the Actions-Groups and Actions to audit.\r\n\r\nThe recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins:\r\n\r\nBATCH_COMPLETED_GROUP,\r\nSUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,\r\nFAILED_DATABASE_AUTHENTICATION_GROUP.\r\n\r\nThis above combination is also the set that is configured by default when enabling auditing from the Azure portal.\r\n\r\nThe supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records):\r\n\r\nAPPLICATION_ROLE_CHANGE_PASSWORD_GROUP\r\nBACKUP_RESTORE_GROUP\r\nDATABASE_LOGOUT_GROUP\r\nDATABASE_OBJECT_CHANGE_GROUP\r\nDATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP\r\nDATABASE_OBJECT_PERMISSION_CHANGE_GROUP\r\nDATABASE_OPERATION_GROUP\r\nDATABASE_PERMISSION_CHANGE_GROUP\r\nDATABASE_PRINCIPAL_CHANGE_GROUP\r\nDATABASE_PRINCIPAL_IMPERSONATION_GROUP\r\nDATABASE_ROLE_MEMBER_CHANGE_GROUP\r\nFAILED_DATABASE_AUTHENTICATION_GROUP\r\nSCHEMA_OBJECT_ACCESS_GROUP\r\nSCHEMA_OBJECT_CHANGE_GROUP\r\nSCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP\r\nSCHEMA_OBJECT_PERMISSION_CHANGE_GROUP\r\nSUCCESSFUL_DATABASE_AUTHENTICATION_GROUP\r\nUSER_CHANGE_PASSWORD_GROUP\r\nBATCH_STARTED_GROUP\r\nBATCH_COMPLETED_GROUP\r\n\r\nThese are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs.\r\n\r\nFor more information, see [Database-Level Audit Action Groups](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-action-groups).\r\n\r\nFor Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are:\r\nSELECT\r\nUPDATE\r\nINSERT\r\nDELETE\r\nEXECUTE\r\nRECEIVE\r\nREFERENCES\r\n\r\nThe general form for defining an action to be audited is:\r\n{action} ON {object} BY {principal}\r\n\r\nNote that <object> in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms DATABASE::{db_name} and SCHEMA::{schema_name} are used, respectively.\r\n\r\nFor example:\r\nSELECT on dbo.myTable by public\r\nSELECT on DATABASE::myDatabase by public\r\nSELECT on SCHEMA::mySchema by public\r\n\r\nFor more information, see [Database-Level Audit Actions](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-actions)"
          returned: always
          type: list
          sample: null
        storage_account_subscription_id:
          description:
            - Specifies the blob storage subscription Id.
          returned: always
          type: uuid
          sample: null
        is_storage_secondary_key_in_use:
          description:
            - >-
              Specifies whether storageAccountAccessKey value is the storage's
              secondary key.
          returned: always
          type: bool
          sample: null
        is_azure_monitor_target_enabled:
          description:
            - "Specifies whether audit events are sent to Azure Monitor. \r\nIn order to send the events to Azure Monitor, specify 'state' as 'Enabled' and 'isAzureMonitorTargetEnabled' as true.\r\n\r\nWhen using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created.\r\nNote that for server level audit you should use the 'master' database as {databaseName}.\r\n\r\nDiagnostic Settings URI format:\r\nPUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview\r\n\r\nFor more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)\r\nor [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)\r\n"
          returned: always
          type: bool
          sample: null
        queue_delay_ms:
          description:
            - "Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed.\r\nThe default minimum value is 1000 (1 second). The maximum is 2,147,483,647."
          returned: always
          type: integer
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


class AzureRMDatabaseBlobAuditingPolicyInfo(AzureRMModuleBase):
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
            blobauditingpolicyname=dict(
                type='constant'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.blobauditingpolicyname = None

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
        super(AzureRMDatabaseBlobAuditingPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.blobauditingpolicyname is not None):
            self.results['database_blob_auditing_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['database_blob_auditing_policies'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.database_blob_auditing_policies.get(resource_group_name=self.resource_group_name,
                                                                            server_name=self.server_name,
                                                                            database_name=self.database_name,
                                                                            blobauditingpolicyname=self.blobauditingpolicyname)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.database_blob_auditing_policies.list_by_database(resource_group_name=self.resource_group_name,
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
    AzureRMDatabaseBlobAuditingPolicyInfo()


if __name__ == '__main__':
    main()
