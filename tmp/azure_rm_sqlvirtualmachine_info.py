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
module: azure_rm_sqlvirtualmachine_info
version_added: '2.9'
short_description: Get SqlVirtualMachine info.
description:
  - Get info of SqlVirtualMachine.
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    type: str
  sqlvirtual_machine_group_name:
    description:
      - Name of the SQL virtual machine group.
    type: str
  sqlvirtual_machine_name:
    description:
      - Name of the SQL virtual machine.
    type: str
  expand:
    description:
      - The child resources to include in the response.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets the list of sql virtual machines in a SQL virtual machine group.
      azure_rm_sqlvirtualmachine_info: 
        resource_group_name: testrg
        

    - name: Gets all SQL virtual machines in a subscription.
      azure_rm_sqlvirtualmachine_info: 
        {}
        

    - name: Gets a SQL virtual machine.
      azure_rm_sqlvirtualmachine_info: 
        resource_group_name: testrg
        

    - name: Gets all SQL virtual machines in a resource group.
      azure_rm_sqlvirtualmachine_info: 
        resource_group_name: testrg
        

'''

RETURN = '''
sql_virtual_machines:
  description: >-
    A list of dict results where the key is the name of the SqlVirtualMachine
    and the values are the facts for that SqlVirtualMachine.
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
        virtual_machine_resource_id:
          description:
            - >-
              ARM Resource id of underlying virtual machine created from SQL
              marketplace image.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state to track the async operation status.
          returned: always
          type: str
          sample: null
        sqlimage_offer:
          description:
            - 'SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.'
          returned: always
          type: str
          sample: null
        sqlserver_license_type:
          description:
            - SQL Server license type.
          returned: always
          type: str
          sample: null
        sqlmanagement:
          description:
            - SQL Server Management type.
          returned: always
          type: str
          sample: null
        sqlimage_sku:
          description:
            - SQL Server edition type.
          returned: always
          type: str
          sample: null
        sqlvirtual_machine_group_resource_id:
          description:
            - >-
              ARM resource id of the SQL virtual machine group this SQL virtual
              machine is or will be part of.
          returned: always
          type: str
          sample: null
        wsfc_domain_credentials:
          description:
            - >-
              Domain credentials for setting up Windows Server Failover Cluster
              for SQL availability group.
          returned: always
          type: dict
          sample: null
          contains:
            cluster_bootstrap_account_password:
              description:
                - Cluster bootstrap account password.
              returned: always
              type: str
              sample: null
            cluster_operator_account_password:
              description:
                - Cluster operator account password.
              returned: always
              type: str
              sample: null
            sqlservice_account_password:
              description:
                - SQL service account password.
              returned: always
              type: str
              sample: null
        auto_patching_settings:
          description:
            - >-
              Auto patching settings for applying critical security updates to
              SQL virtual machine.
          returned: always
          type: dict
          sample: null
          contains:
            enable:
              description:
                - Enable or disable autopatching on SQL virtual machine.
              returned: always
              type: bool
              sample: null
            day_of_week:
              description:
                - Day of week to apply the patch on.
              returned: always
              type: sealed-choice
              sample: null
            maintenance_window_starting_hour:
              description:
                - Hour of the day when patching is initiated. Local VM time.
              returned: always
              type: integer
              sample: null
            maintenance_window_duration:
              description:
                - Duration of patching.
              returned: always
              type: integer
              sample: null
        auto_backup_settings:
          description:
            - Auto backup settings for SQL Server.
          returned: always
          type: dict
          sample: null
          contains:
            enable:
              description:
                - Enable or disable autobackup on SQL virtual machine.
              returned: always
              type: bool
              sample: null
            enable_encryption:
              description:
                - >-
                  Enable or disable encryption for backup on SQL virtual
                  machine.
              returned: always
              type: bool
              sample: null
            retention_period:
              description:
                - 'Retention period of backup: 1-30 days.'
              returned: always
              type: integer
              sample: null
            storage_account_url:
              description:
                - Storage account url where backup will be taken to.
              returned: always
              type: str
              sample: null
            storage_access_key:
              description:
                - Storage account key where backup will be taken to.
              returned: always
              type: str
              sample: null
            password:
              description:
                - Password for encryption on backup.
              returned: always
              type: str
              sample: null
            backup_system_dbs:
              description:
                - Include or exclude system databases from auto backup.
              returned: always
              type: bool
              sample: null
            backup_schedule_type:
              description:
                - Backup schedule type.
              returned: always
              type: str
              sample: null
            full_backup_frequency:
              description:
                - >-
                  Frequency of full backups. In both cases, full backups begin
                  during the next scheduled time window.
              returned: always
              type: str
              sample: null
            full_backup_start_time:
              description:
                - >-
                  Start time of a given day during which full backups can take
                  place. 0-23 hours.
              returned: always
              type: integer
              sample: null
            full_backup_window_hours:
              description:
                - >-
                  Duration of the time window of a given day during which full
                  backups can take place. 1-23 hours.
              returned: always
              type: integer
              sample: null
            log_backup_frequency:
              description:
                - Frequency of log backups. 5-60 minutes.
              returned: always
              type: integer
              sample: null
        key_vault_credential_settings:
          description:
            - Key vault credential settings.
          returned: always
          type: dict
          sample: null
          contains:
            enable:
              description:
                - Enable or disable key vault credential setting.
              returned: always
              type: bool
              sample: null
            credential_name:
              description:
                - Credential name.
              returned: always
              type: str
              sample: null
            azure_key_vault_url:
              description:
                - Azure Key Vault url.
              returned: always
              type: str
              sample: null
            service_principal_name:
              description:
                - Service principal name to access key vault.
              returned: always
              type: str
              sample: null
            service_principal_secret:
              description:
                - Service principal name secret to access key vault.
              returned: always
              type: str
              sample: null
        sqldata_settings:
          description:
            - SQL Server Data Storage Settings.
          returned: always
          type: dict
          sample: null
          contains:
            luns:
              description:
                - Logical Unit Numbers for the disks.
              returned: always
              type: list
              sample: null
            default_file_path:
              description:
                - SQL Server default file path
              returned: always
              type: str
              sample: null
        sqllog_settings:
          description:
            - SQL Server Log Storage Settings.
          returned: always
          type: dict
          sample: null
          contains:
            luns:
              description:
                - Logical Unit Numbers for the disks.
              returned: always
              type: list
              sample: null
            default_file_path:
              description:
                - SQL Server default file path
              returned: always
              type: str
              sample: null
        sqltemp_dbsettings:
          description:
            - SQL Server TempDb Storage Settings.
          returned: always
          type: dict
          sample: null
          contains:
            luns:
              description:
                - Logical Unit Numbers for the disks.
              returned: always
              type: list
              sample: null
            default_file_path:
              description:
                - SQL Server default file path
              returned: always
              type: str
              sample: null
        disk_configuration_type:
          description:
            - Disk configuration to apply to SQL Server.
          returned: always
          type: str
          sample: null
        storage_workload_type:
          description:
            - Storage workload type.
          returned: always
          type: str
          sample: null
        sqlconnectivity_update_settings:
          description:
            - SQL connectivity type settings.
          returned: always
          type: dict
          sample: null
          contains:
            connectivity_type:
              description:
                - SQL Server connectivity option.
              returned: always
              type: str
              sample: null
            port:
              description:
                - SQL Server port.
              returned: always
              type: integer
              sample: null
            sqlauth_update_user_name:
              description:
                - SQL Server sysadmin login to create.
              returned: always
              type: str
              sample: null
            sqlauth_update_password:
              description:
                - SQL Server sysadmin login password.
              returned: always
              type: str
              sample: null
        sqlstorage_update_settings:
          description:
            - SQL storage update settings.
          returned: always
          type: dict
          sample: null
          contains:
            disk_count:
              description:
                - Virtual machine disk count.
              returned: always
              type: integer
              sample: null
            starting_device_id:
              description:
                - Device id of the first disk to be updated.
              returned: always
              type: integer
              sample: null
            disk_configuration_type:
              description:
                - Disk configuration to apply to SQL Server.
              returned: always
              type: str
              sample: null
        is_rservices_enabled:
          description:
            - Enable or disable R services (SQL 2016 onwards).
          returned: always
          type: bool
          sample: null
        sqlworkload_type:
          description:
            - SQL Server workload type.
          returned: always
          type: str
          sample: null
        principal_id:
          description:
            - The Azure Active Directory principal id.
          returned: always
          type: uuid
          sample: null
        type_identity_type:
          description:
            - >-
              The identity type. Set this to 'SystemAssigned' in order to
              automatically create and assign an Azure Active Directory
              principal for the resource.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The Azure Active Directory tenant id.
          returned: always
          type: uuid
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
    virtual_machine_resource_id:
      description:
        - >-
          ARM Resource id of underlying virtual machine created from SQL
          marketplace image.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state to track the async operation status.
      returned: always
      type: str
      sample: null
    sqlimage_offer:
      description:
        - 'SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.'
      returned: always
      type: str
      sample: null
    sqlserver_license_type:
      description:
        - SQL Server license type.
      returned: always
      type: str
      sample: null
    sqlmanagement:
      description:
        - SQL Server Management type.
      returned: always
      type: str
      sample: null
    sqlimage_sku:
      description:
        - SQL Server edition type.
      returned: always
      type: str
      sample: null
    sqlvirtual_machine_group_resource_id:
      description:
        - >-
          ARM resource id of the SQL virtual machine group this SQL virtual
          machine is or will be part of.
      returned: always
      type: str
      sample: null
    wsfc_domain_credentials:
      description:
        - >-
          Domain credentials for setting up Windows Server Failover Cluster for
          SQL availability group.
      returned: always
      type: dict
      sample: null
      contains:
        cluster_bootstrap_account_password:
          description:
            - Cluster bootstrap account password.
          returned: always
          type: str
          sample: null
        cluster_operator_account_password:
          description:
            - Cluster operator account password.
          returned: always
          type: str
          sample: null
        sqlservice_account_password:
          description:
            - SQL service account password.
          returned: always
          type: str
          sample: null
    auto_patching_settings:
      description:
        - >-
          Auto patching settings for applying critical security updates to SQL
          virtual machine.
      returned: always
      type: dict
      sample: null
      contains:
        enable:
          description:
            - Enable or disable autopatching on SQL virtual machine.
          returned: always
          type: bool
          sample: null
        day_of_week:
          description:
            - Day of week to apply the patch on.
          returned: always
          type: sealed-choice
          sample: null
        maintenance_window_starting_hour:
          description:
            - Hour of the day when patching is initiated. Local VM time.
          returned: always
          type: integer
          sample: null
        maintenance_window_duration:
          description:
            - Duration of patching.
          returned: always
          type: integer
          sample: null
    auto_backup_settings:
      description:
        - Auto backup settings for SQL Server.
      returned: always
      type: dict
      sample: null
      contains:
        enable:
          description:
            - Enable or disable autobackup on SQL virtual machine.
          returned: always
          type: bool
          sample: null
        enable_encryption:
          description:
            - Enable or disable encryption for backup on SQL virtual machine.
          returned: always
          type: bool
          sample: null
        retention_period:
          description:
            - 'Retention period of backup: 1-30 days.'
          returned: always
          type: integer
          sample: null
        storage_account_url:
          description:
            - Storage account url where backup will be taken to.
          returned: always
          type: str
          sample: null
        storage_access_key:
          description:
            - Storage account key where backup will be taken to.
          returned: always
          type: str
          sample: null
        password:
          description:
            - Password for encryption on backup.
          returned: always
          type: str
          sample: null
        backup_system_dbs:
          description:
            - Include or exclude system databases from auto backup.
          returned: always
          type: bool
          sample: null
        backup_schedule_type:
          description:
            - Backup schedule type.
          returned: always
          type: str
          sample: null
        full_backup_frequency:
          description:
            - >-
              Frequency of full backups. In both cases, full backups begin
              during the next scheduled time window.
          returned: always
          type: str
          sample: null
        full_backup_start_time:
          description:
            - >-
              Start time of a given day during which full backups can take
              place. 0-23 hours.
          returned: always
          type: integer
          sample: null
        full_backup_window_hours:
          description:
            - >-
              Duration of the time window of a given day during which full
              backups can take place. 1-23 hours.
          returned: always
          type: integer
          sample: null
        log_backup_frequency:
          description:
            - Frequency of log backups. 5-60 minutes.
          returned: always
          type: integer
          sample: null
    key_vault_credential_settings:
      description:
        - Key vault credential settings.
      returned: always
      type: dict
      sample: null
      contains:
        enable:
          description:
            - Enable or disable key vault credential setting.
          returned: always
          type: bool
          sample: null
        credential_name:
          description:
            - Credential name.
          returned: always
          type: str
          sample: null
        azure_key_vault_url:
          description:
            - Azure Key Vault url.
          returned: always
          type: str
          sample: null
        service_principal_name:
          description:
            - Service principal name to access key vault.
          returned: always
          type: str
          sample: null
        service_principal_secret:
          description:
            - Service principal name secret to access key vault.
          returned: always
          type: str
          sample: null
    sqldata_settings:
      description:
        - SQL Server Data Storage Settings.
      returned: always
      type: dict
      sample: null
      contains:
        luns:
          description:
            - Logical Unit Numbers for the disks.
          returned: always
          type: list
          sample: null
        default_file_path:
          description:
            - SQL Server default file path
          returned: always
          type: str
          sample: null
    sqllog_settings:
      description:
        - SQL Server Log Storage Settings.
      returned: always
      type: dict
      sample: null
      contains:
        luns:
          description:
            - Logical Unit Numbers for the disks.
          returned: always
          type: list
          sample: null
        default_file_path:
          description:
            - SQL Server default file path
          returned: always
          type: str
          sample: null
    sqltemp_dbsettings:
      description:
        - SQL Server TempDb Storage Settings.
      returned: always
      type: dict
      sample: null
      contains:
        luns:
          description:
            - Logical Unit Numbers for the disks.
          returned: always
          type: list
          sample: null
        default_file_path:
          description:
            - SQL Server default file path
          returned: always
          type: str
          sample: null
    disk_configuration_type:
      description:
        - Disk configuration to apply to SQL Server.
      returned: always
      type: str
      sample: null
    storage_workload_type:
      description:
        - Storage workload type.
      returned: always
      type: str
      sample: null
    sqlconnectivity_update_settings:
      description:
        - SQL connectivity type settings.
      returned: always
      type: dict
      sample: null
      contains:
        connectivity_type:
          description:
            - SQL Server connectivity option.
          returned: always
          type: str
          sample: null
        port:
          description:
            - SQL Server port.
          returned: always
          type: integer
          sample: null
        sqlauth_update_user_name:
          description:
            - SQL Server sysadmin login to create.
          returned: always
          type: str
          sample: null
        sqlauth_update_password:
          description:
            - SQL Server sysadmin login password.
          returned: always
          type: str
          sample: null
    sqlstorage_update_settings:
      description:
        - SQL storage update settings.
      returned: always
      type: dict
      sample: null
      contains:
        disk_count:
          description:
            - Virtual machine disk count.
          returned: always
          type: integer
          sample: null
        starting_device_id:
          description:
            - Device id of the first disk to be updated.
          returned: always
          type: integer
          sample: null
        disk_configuration_type:
          description:
            - Disk configuration to apply to SQL Server.
          returned: always
          type: str
          sample: null
    is_rservices_enabled:
      description:
        - Enable or disable R services (SQL 2016 onwards).
      returned: always
      type: bool
      sample: null
    sqlworkload_type:
      description:
        - SQL Server workload type.
      returned: always
      type: str
      sample: null
    principal_id:
      description:
        - The Azure Active Directory principal id.
      returned: always
      type: uuid
      sample: null
    type_identity_type:
      description:
        - >-
          The identity type. Set this to 'SystemAssigned' in order to
          automatically create and assign an Azure Active Directory principal
          for the resource.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The Azure Active Directory tenant id.
      returned: always
      type: uuid
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlVirtualMachineManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSqlVirtualMachineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            sqlvirtual_machine_group_name=dict(
                type='str'
            ),
            sqlvirtual_machine_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.sqlvirtual_machine_group_name = None
        self.sqlvirtual_machine_name = None
        self.expand = None

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
        super(AzureRMSqlVirtualMachineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlVirtualMachineManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.sqlvirtual_machine_name is not None):
            self.results['sql_virtual_machines'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.sqlvirtual_machine_group_name is not None):
            self.results['sql_virtual_machines'] = self.format_item(self.listbysqlvmgroup())
        elif (self.resource_group_name is not None):
            self.results['sql_virtual_machines'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['sql_virtual_machines'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machines.get(resource_group_name=self.resource_group_name,
                                                                 sqlvirtual_machine_name=self.sqlvirtual_machine_name,
                                                                 expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysqlvmgroup(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machines.list_by_sqlvm_group(resource_group_name=self.resource_group_name,
                                                                                 sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machines.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machines.list()
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
    AzureRMSqlVirtualMachineInfo()


if __name__ == '__main__':
    main()
