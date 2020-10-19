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
module: azure_rm_serverblobauditingpolicy
version_added: '2.9'
short_description: Manage Azure ServerBlobAuditingPolicy instance.
description:
  - 'Create, update and delete instance of Azure ServerBlobAuditingPolicy.'
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
  blobauditingpolicyname:
    description:
      - The name of the blob auditing policy.
    required: true
    type: constant
  state:
    description:
      - Assert the state of the ServerBlobAuditingPolicy.
      - >-
        Use C(present) to create or update an ServerBlobAuditingPolicy and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
  storage_endpoint:
    description:
      - >-
        Specifies the blob storage endpoint (e.g.
        https://MyAccount.blob.core.windows.net). If state is Enabled,
        storageEndpoint or isAzureMonitorTargetEnabled is required.
    type: str
  storage_account_access_key:
    description:
      - "Specifies the identifier key of the auditing storage account. \r"
      - "If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage.\r"
      - "Prerequisites for using managed identity authentication:\r"
      - "1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD).\r"
      - "2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity.\r"
      - >-
        For more information, see [Auditing to storage using Managed Identity
        authentication](https://go.microsoft.com/fwlink/?linkid=2114355)
    type: str
  retention_days:
    description:
      - >-
        Specifies the number of days to keep in the audit logs in the storage
        account.
    type: integer
  audit_actions_and_groups:
    description:
      - "Specifies the Actions-Groups and Actions to audit.\r"
      - "\r"
      - "The recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins:\r"
      - "\r"
      - "BATCH_COMPLETED_GROUP,\r"
      - "SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,\r"
      - "FAILED_DATABASE_AUTHENTICATION_GROUP.\r"
      - "\r"
      - "This above combination is also the set that is configured by default when enabling auditing from the Azure portal.\r"
      - "\r"
      - "The supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records):\r"
      - "\r"
      - "APPLICATION_ROLE_CHANGE_PASSWORD_GROUP\r"
      - "BACKUP_RESTORE_GROUP\r"
      - "DATABASE_LOGOUT_GROUP\r"
      - "DATABASE_OBJECT_CHANGE_GROUP\r"
      - "DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP\r"
      - "DATABASE_OBJECT_PERMISSION_CHANGE_GROUP\r"
      - "DATABASE_OPERATION_GROUP\r"
      - "DATABASE_PERMISSION_CHANGE_GROUP\r"
      - "DATABASE_PRINCIPAL_CHANGE_GROUP\r"
      - "DATABASE_PRINCIPAL_IMPERSONATION_GROUP\r"
      - "DATABASE_ROLE_MEMBER_CHANGE_GROUP\r"
      - "FAILED_DATABASE_AUTHENTICATION_GROUP\r"
      - "SCHEMA_OBJECT_ACCESS_GROUP\r"
      - "SCHEMA_OBJECT_CHANGE_GROUP\r"
      - "SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP\r"
      - "SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP\r"
      - "SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP\r"
      - "USER_CHANGE_PASSWORD_GROUP\r"
      - "BATCH_STARTED_GROUP\r"
      - "BATCH_COMPLETED_GROUP\r"
      - "\r"
      - "These are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs.\r"
      - "\r"
      - "For more information, see [Database-Level Audit Action Groups](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-action-groups).\r"
      - "\r"
      - "For Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are:\r"
      - "SELECT\r"
      - "UPDATE\r"
      - "INSERT\r"
      - "DELETE\r"
      - "EXECUTE\r"
      - "RECEIVE\r"
      - "REFERENCES\r"
      - "\r"
      - "The general form for defining an action to be audited is:\r"
      - "{action} ON {object} BY {principal}\r"
      - "\r"
      - "Note that <object> in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms DATABASE::{db_name} and SCHEMA::{schema_name} are used, respectively.\r"
      - "\r"
      - "For example:\r"
      - "SELECT on dbo.myTable by public\r"
      - "SELECT on DATABASE::myDatabase by public\r"
      - "SELECT on SCHEMA::mySchema by public\r"
      - "\r"
      - >-
        For more information, see [Database-Level Audit
        Actions](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-actions)
    type: list
  storage_account_subscription_id:
    description:
      - Specifies the blob storage subscription Id.
    type: uuid
  is_storage_secondary_key_in_use:
    description:
      - >-
        Specifies whether storageAccountAccessKey value is the storage's
        secondary key.
    type: bool
  is_azure_monitor_target_enabled:
    description:
      - "Specifies whether audit events are sent to Azure Monitor. \r"
      - "In order to send the events to Azure Monitor, specify 'state' as 'Enabled' and 'isAzureMonitorTargetEnabled' as true.\r"
      - "\r"
      - "When using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created.\r"
      - "Note that for server level audit you should use the 'master' database as {databaseName}.\r"
      - "\r"
      - "Diagnostic Settings URI format:\r"
      - "PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview\r"
      - "\r"
      - "For more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)\r"
      - "or [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)\r"
      - ''
    type: bool
  queue_delay_ms:
    description:
      - "Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed.\r"
      - >-
        The default minimum value is 1000 (1 second). The maximum is
        2,147,483,647.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Update a server's blob auditing policy with all parameters
      azure_rm_serverblobauditingpolicy: 
        resource_group_name: blobauditingtest-4799
        server_name: blobauditingtest-6440
        properties:
          audit_actions_and_groups:
            - SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP
            - FAILED_DATABASE_AUTHENTICATION_GROUP
            - BATCH_COMPLETED_GROUP
          is_azure_monitor_target_enabled: true
          is_storage_secondary_key_in_use: false
          queue_delay_ms: 4000
          retention_days: 6
          state: Enabled
          storage_account_access_key: >-
            sdlfkjabc+sdlfkjsdlkfsjdfLDKFTERLKFDFKLjsdfksjdflsdkfD2342309432849328476458/3RSD==
          storage_account_subscription_id: 00000000-1234-0000-5678-000000000000
          storage_endpoint: 'https://mystorage.blob.core.windows.net'
        

    - name: Update a server's blob auditing policy with minimal parameters
      azure_rm_serverblobauditingpolicy: 
        resource_group_name: blobauditingtest-4799
        server_name: blobauditingtest-6440
        properties:
          state: Enabled
          storage_account_access_key: >-
            sdlfkjabc+sdlfkjsdlkfsjdfLDKFTERLKFDFKLjsdfksjdflsdkfD2342309432849328476458/3RSD==
          storage_endpoint: 'https://mystorage.blob.core.windows.net'
        

'''

RETURN = '''
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
state:
  description:
    - >-
      Specifies the state of the policy. If state is Enabled, storageEndpoint or
      isAzureMonitorTargetEnabled are required.
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
      Specifies whether storageAccountAccessKey value is the storage's secondary
      key.
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


class AzureRMServerBlobAuditingPolicy(AzureRMModuleBaseExt):
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
            blobauditingpolicyname=dict(
                type='constant',
                required=True
            ),
            state=dict(
                type='sealed-choice',
                disposition='/state'
            ),
            storage_endpoint=dict(
                type='str',
                disposition='/storage_endpoint'
            ),
            storage_account_access_key=dict(
                type='str',
                disposition='/storage_account_access_key'
            ),
            retention_days=dict(
                type='integer',
                disposition='/retention_days'
            ),
            audit_actions_and_groups=dict(
                type='list',
                disposition='/audit_actions_and_groups',
                elements='str'
            ),
            storage_account_subscription_id=dict(
                type='uuid',
                disposition='/storage_account_subscription_id'
            ),
            is_storage_secondary_key_in_use=dict(
                type='bool',
                disposition='/is_storage_secondary_key_in_use'
            ),
            is_azure_monitor_target_enabled=dict(
                type='bool',
                disposition='/is_azure_monitor_target_enabled'
            ),
            queue_delay_ms=dict(
                type='integer',
                disposition='/queue_delay_ms'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.blobauditingpolicyname = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServerBlobAuditingPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-03-01-preview')

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
            response = self.mgmt_client.server_blob_auditing_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                                       server_name=self.server_name,
                                                                                       blobauditingpolicyname=self.blobauditingpolicyname,
                                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ServerBlobAuditingPolicy instance.')
            self.fail('Error creating the ServerBlobAuditingPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.server_blob_auditing_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ServerBlobAuditingPolicy instance.')
            self.fail('Error deleting the ServerBlobAuditingPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.server_blob_auditing_policies.get(resource_group_name=self.resource_group_name,
                                                                          server_name=self.server_name,
                                                                          blobauditingpolicyname=self.blobauditingpolicyname)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServerBlobAuditingPolicy()


if __name__ == '__main__':
    main()
