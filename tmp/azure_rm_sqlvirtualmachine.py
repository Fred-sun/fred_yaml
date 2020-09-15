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
module: azure_rm_sqlvirtualmachine
version_added: '2.9'
short_description: Manage Azure SqlVirtualMachine instance.
description:
  - 'Create, update and delete instance of Azure SqlVirtualMachine.'
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  sqlvirtual_machine_name:
    description:
      - Name of the SQL virtual machine.
    required: true
    type: str
  expand:
    description:
      - The child resources to include in the response.
    type: str
  location:
    description:
      - Resource location.
    type: str
  virtual_machine_resource_id:
    description:
      - >-
        ARM Resource id of underlying virtual machine created from SQL
        marketplace image.
    type: str
  sqlimage_offer:
    description:
      - 'SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.'
    type: str
  sqlserver_license_type:
    description:
      - SQL Server license type.
    type: str
    choices:
      - PAYG
      - AHUB
      - DR
  sqlmanagement:
    description:
      - SQL Server Management type.
    type: str
    choices:
      - Full
      - LightWeight
      - NoAgent
  sqlimage_sku:
    description:
      - SQL Server edition type.
    type: str
    choices:
      - Developer
      - Express
      - Standard
      - Enterprise
      - Web
  sqlvirtual_machine_group_resource_id:
    description:
      - >-
        ARM resource id of the SQL virtual machine group this SQL virtual
        machine is or will be part of.
    type: str
  wsfc_domain_credentials:
    description:
      - >-
        Domain credentials for setting up Windows Server Failover Cluster for
        SQL availability group.
    type: dict
    suboptions:
      cluster_bootstrap_account_password:
        description:
          - Cluster bootstrap account password.
        type: str
      cluster_operator_account_password:
        description:
          - Cluster operator account password.
        type: str
      sqlservice_account_password:
        description:
          - SQL service account password.
        type: str
  auto_patching_settings:
    description:
      - >-
        Auto patching settings for applying critical security updates to SQL
        virtual machine.
    type: dict
    suboptions:
      enable:
        description:
          - Enable or disable autopatching on SQL virtual machine.
        type: bool
      day_of_week:
        description:
          - Day of week to apply the patch on.
        type: sealed-choice
      maintenance_window_starting_hour:
        description:
          - Hour of the day when patching is initiated. Local VM time.
        type: integer
      maintenance_window_duration:
        description:
          - Duration of patching.
        type: integer
  auto_backup_settings:
    description:
      - Auto backup settings for SQL Server.
    type: dict
    suboptions:
      enable:
        description:
          - Enable or disable autobackup on SQL virtual machine.
        type: bool
      enable_encryption:
        description:
          - Enable or disable encryption for backup on SQL virtual machine.
        type: bool
      retention_period:
        description:
          - 'Retention period of backup: 1-30 days.'
        type: integer
      storage_account_url:
        description:
          - Storage account url where backup will be taken to.
        type: str
      storage_access_key:
        description:
          - Storage account key where backup will be taken to.
        type: str
      password:
        description:
          - Password for encryption on backup.
        type: str
      backup_system_dbs:
        description:
          - Include or exclude system databases from auto backup.
        type: bool
      backup_schedule_type:
        description:
          - Backup schedule type.
        type: str
        choices:
          - Manual
          - Automated
      full_backup_frequency:
        description:
          - >-
            Frequency of full backups. In both cases, full backups begin during
            the next scheduled time window.
        type: str
        choices:
          - Daily
          - Weekly
      full_backup_start_time:
        description:
          - >-
            Start time of a given day during which full backups can take place.
            0-23 hours.
        type: integer
      full_backup_window_hours:
        description:
          - >-
            Duration of the time window of a given day during which full backups
            can take place. 1-23 hours.
        type: integer
      log_backup_frequency:
        description:
          - Frequency of log backups. 5-60 minutes.
        type: integer
  key_vault_credential_settings:
    description:
      - Key vault credential settings.
    type: dict
    suboptions:
      enable:
        description:
          - Enable or disable key vault credential setting.
        type: bool
      credential_name:
        description:
          - Credential name.
        type: str
      azure_key_vault_url:
        description:
          - Azure Key Vault url.
        type: str
      service_principal_name:
        description:
          - Service principal name to access key vault.
        type: str
      service_principal_secret:
        description:
          - Service principal name secret to access key vault.
        type: str
  sqldata_settings:
    description:
      - SQL Server Data Storage Settings.
    type: dict
    suboptions:
      luns:
        description:
          - Logical Unit Numbers for the disks.
        type: list
      default_file_path:
        description:
          - SQL Server default file path
        type: str
  sqllog_settings:
    description:
      - SQL Server Log Storage Settings.
    type: dict
    suboptions:
      luns:
        description:
          - Logical Unit Numbers for the disks.
        type: list
      default_file_path:
        description:
          - SQL Server default file path
        type: str
  sqltemp_dbsettings:
    description:
      - SQL Server TempDb Storage Settings.
    type: dict
    suboptions:
      luns:
        description:
          - Logical Unit Numbers for the disks.
        type: list
      default_file_path:
        description:
          - SQL Server default file path
        type: str
  disk_configuration_type:
    description:
      - Disk configuration to apply to SQL Server.
    type: str
    choices:
      - NEW
      - EXTEND
      - ADD
  storage_workload_type:
    description:
      - Storage workload type.
    type: str
    choices:
      - GENERAL
      - OLTP
      - DW
  sqlconnectivity_update_settings:
    description:
      - SQL connectivity type settings.
    type: dict
    suboptions:
      connectivity_type:
        description:
          - SQL Server connectivity option.
        type: str
        choices:
          - LOCAL
          - PRIVATE
          - PUBLIC
      port:
        description:
          - SQL Server port.
        type: integer
      sqlauth_update_user_name:
        description:
          - SQL Server sysadmin login to create.
        type: str
      sqlauth_update_password:
        description:
          - SQL Server sysadmin login password.
        type: str
  sqlstorage_update_settings:
    description:
      - SQL storage update settings.
    type: dict
    suboptions:
      disk_count:
        description:
          - Virtual machine disk count.
        type: integer
      starting_device_id:
        description:
          - Device id of the first disk to be updated.
        type: integer
      disk_configuration_type:
        description:
          - Disk configuration to apply to SQL Server.
        type: str
        choices:
          - NEW
          - EXTEND
          - ADD
  is_rservices_enabled:
    description:
      - Enable or disable R services (SQL 2016 onwards).
    type: bool
  sqlworkload_type:
    description:
      - SQL Server workload type.
    type: str
    choices:
      - GENERAL
      - OLTP
      - DW
  type:
    description:
      - >-
        The identity type. Set this to 'SystemAssigned' in order to
        automatically create and assign an Azure Active Directory principal for
        the resource.
    type: str
    choices:
      - SystemAssigned
  state:
    description:
      - Assert the state of the SqlVirtualMachine.
      - >-
        Use C(present) to create or update an SqlVirtualMachine and C(absent) to
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
    - name: Creates or updates a SQL virtual machine and joins it to a SQL virtual machine group.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        location: northeurope
        properties:
          sql_virtual_machine_group_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachineGroups/testvmgroup
          virtual_machine_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Compute/virtualMachines/testvm2
          wsfc_domain_credentials:
            cluster_bootstrap_account_password: <Password>
            cluster_operator_account_password: <Password>
            sql_service_account_password: <Password>
        

    - name: Creates or updates a SQL virtual machine for Storage Configuration Settings to EXTEND Data, Log or TempDB storage pool.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        location: northeurope
        properties:
          storage_configuration_settings:
            disk_configuration_type: EXTEND
            sql_data_settings:
              luns:
                - 2
          virtual_machine_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Compute/virtualMachines/testvm
        

    - name: Creates or updates a SQL virtual machine for Storage Configuration Settings to NEW Data, Log and TempDB storage pool.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        location: northeurope
        properties:
          storage_configuration_settings:
            disk_configuration_type: NEW
            sql_data_settings:
              default_file_path: 'F:\folderpath\'
              luns:
                - 0
            sql_log_settings:
              default_file_path: 'G:\folderpath\'
              luns:
                - 1
            sql_temp_db_settings:
              default_file_path: 'D:\TEMP'
            storage_workload_type: OLTP
          virtual_machine_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Compute/virtualMachines/testvm
        

    - name: Creates or updates a SQL virtual machine with max parameters.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        location: northeurope
        properties:
          auto_backup_settings:
            backup_schedule_type: Manual
            backup_system_dbs: true
            enable: true
            enable_encryption: true
            full_backup_frequency: Daily
            full_backup_start_time: 6
            full_backup_window_hours: 11
            log_backup_frequency: 10
            password: <Password>
            retention_period: 17
            storage_access_key: <primary storage access key>
            storage_account_url: 'https://teststorage.blob.core.windows.net/'
          auto_patching_settings:
            day_of_week: Sunday
            enable: true
            maintenance_window_duration: 60
            maintenance_window_starting_hour: 2
          key_vault_credential_settings:
            enable: false
          server_configurations_management_settings:
            additional_features_server_configurations:
              is_rservices_enabled: false
            sql_connectivity_update_settings:
              connectivity_type: PRIVATE
              port: 1433
              sql_auth_update_password: <password>
              sql_auth_update_user_name: sqllogin
            sql_storage_update_settings:
              disk_configuration_type: NEW
              disk_count: 1
              starting_device_id: 2
            sql_workload_type_update_settings:
              sql_workload_type: OLTP
          sql_image_sku: Enterprise
          sql_management: Full
          sql_server_license_type: PAYG
          virtual_machine_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Compute/virtualMachines/testvm
        

    - name: Creates or updates a SQL virtual machine with min parameters.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        location: northeurope
        properties:
          virtual_machine_resource_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Compute/virtualMachines/testvm
        

    - name: Deletes a SQL virtual machine.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        

    - name: Updates a SQL virtual machine tags.
      azure_rm_sqlvirtualmachine: 
        resource_group_name: testrg
        tags:
          mytag: myval
        

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
virtual_machine_resource_id:
  description:
    - >-
      ARM Resource id of underlying virtual machine created from SQL marketplace
      image.
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
      ARM resource id of the SQL virtual machine group this SQL virtual machine
      is or will be part of.
  returned: always
  type: str
  sample: null
wsfc_domain_credentials:
  description:
    - >-
      Domain credentials for setting up Windows Server Failover Cluster for SQL
      availability group.
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
          Frequency of full backups. In both cases, full backups begin during
          the next scheduled time window.
      returned: always
      type: str
      sample: null
    full_backup_start_time:
      description:
        - >-
          Start time of a given day during which full backups can take place.
          0-23 hours.
      returned: always
      type: integer
      sample: null
    full_backup_window_hours:
      description:
        - >-
          Duration of the time window of a given day during which full backups
          can take place. 1-23 hours.
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
      The identity type. Set this to 'SystemAssigned' in order to automatically
      create and assign an Azure Active Directory principal for the resource.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlVirtualMachineManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSqlVirtualMachine(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sqlvirtual_machine_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            virtual_machine_resource_id=dict(
                type='str',
                disposition='/virtual_machine_resource_id'
            ),
            sqlimage_offer=dict(
                type='str',
                disposition='/sqlimage_offer'
            ),
            sqlserver_license_type=dict(
                type='str',
                disposition='/sqlserver_license_type',
                choices=['PAYG',
                         'AHUB',
                         'DR']
            ),
            sqlmanagement=dict(
                type='str',
                disposition='/sqlmanagement',
                choices=['Full',
                         'LightWeight',
                         'NoAgent']
            ),
            sqlimage_sku=dict(
                type='str',
                disposition='/sqlimage_sku',
                choices=['Developer',
                         'Express',
                         'Standard',
                         'Enterprise',
                         'Web']
            ),
            sqlvirtual_machine_group_resource_id=dict(
                type='str',
                disposition='/sqlvirtual_machine_group_resource_id'
            ),
            wsfc_domain_credentials=dict(
                type='dict',
                disposition='/wsfc_domain_credentials',
                options=dict(
                    cluster_bootstrap_account_password=dict(
                        type='str',
                        disposition='cluster_bootstrap_account_password'
                    ),
                    cluster_operator_account_password=dict(
                        type='str',
                        disposition='cluster_operator_account_password'
                    ),
                    sqlservice_account_password=dict(
                        type='str',
                        disposition='sqlservice_account_password'
                    )
                )
            ),
            auto_patching_settings=dict(
                type='dict',
                disposition='/auto_patching_settings',
                options=dict(
                    enable=dict(
                        type='bool',
                        disposition='enable'
                    ),
                    day_of_week=dict(
                        type='sealed-choice',
                        disposition='day_of_week'
                    ),
                    maintenance_window_starting_hour=dict(
                        type='integer',
                        disposition='maintenance_window_starting_hour'
                    ),
                    maintenance_window_duration=dict(
                        type='integer',
                        disposition='maintenance_window_duration'
                    )
                )
            ),
            auto_backup_settings=dict(
                type='dict',
                disposition='/auto_backup_settings',
                options=dict(
                    enable=dict(
                        type='bool',
                        disposition='enable'
                    ),
                    enable_encryption=dict(
                        type='bool',
                        disposition='enable_encryption'
                    ),
                    retention_period=dict(
                        type='integer',
                        disposition='retention_period'
                    ),
                    storage_account_url=dict(
                        type='str',
                        disposition='storage_account_url'
                    ),
                    storage_access_key=dict(
                        type='str',
                        disposition='storage_access_key'
                    ),
                    password=dict(
                        type='str',
                        disposition='password'
                    ),
                    backup_system_dbs=dict(
                        type='bool',
                        disposition='backup_system_dbs'
                    ),
                    backup_schedule_type=dict(
                        type='str',
                        disposition='backup_schedule_type',
                        choices=['Manual',
                                 'Automated']
                    ),
                    full_backup_frequency=dict(
                        type='str',
                        disposition='full_backup_frequency',
                        choices=['Daily',
                                 'Weekly']
                    ),
                    full_backup_start_time=dict(
                        type='integer',
                        disposition='full_backup_start_time'
                    ),
                    full_backup_window_hours=dict(
                        type='integer',
                        disposition='full_backup_window_hours'
                    ),
                    log_backup_frequency=dict(
                        type='integer',
                        disposition='log_backup_frequency'
                    )
                )
            ),
            key_vault_credential_settings=dict(
                type='dict',
                disposition='/key_vault_credential_settings',
                options=dict(
                    enable=dict(
                        type='bool',
                        disposition='enable'
                    ),
                    credential_name=dict(
                        type='str',
                        disposition='credential_name'
                    ),
                    azure_key_vault_url=dict(
                        type='str',
                        disposition='azure_key_vault_url'
                    ),
                    service_principal_name=dict(
                        type='str',
                        disposition='service_principal_name'
                    ),
                    service_principal_secret=dict(
                        type='str',
                        disposition='service_principal_secret'
                    )
                )
            ),
            sqldata_settings=dict(
                type='dict',
                disposition='/sqldata_settings',
                options=dict(
                    luns=dict(
                        type='list',
                        disposition='luns',
                        elements='integer'
                    ),
                    default_file_path=dict(
                        type='str',
                        disposition='default_file_path'
                    )
                )
            ),
            sqllog_settings=dict(
                type='dict',
                disposition='/sqllog_settings',
                options=dict(
                    luns=dict(
                        type='list',
                        disposition='luns',
                        elements='integer'
                    ),
                    default_file_path=dict(
                        type='str',
                        disposition='default_file_path'
                    )
                )
            ),
            sqltemp_dbsettings=dict(
                type='dict',
                disposition='/sqltemp_dbsettings',
                options=dict(
                    luns=dict(
                        type='list',
                        disposition='luns',
                        elements='integer'
                    ),
                    default_file_path=dict(
                        type='str',
                        disposition='default_file_path'
                    )
                )
            ),
            disk_configuration_type=dict(
                type='str',
                disposition='/disk_configuration_type',
                choices=['NEW',
                         'EXTEND',
                         'ADD']
            ),
            storage_workload_type=dict(
                type='str',
                disposition='/storage_workload_type',
                choices=['GENERAL',
                         'OLTP',
                         'DW']
            ),
            sqlconnectivity_update_settings=dict(
                type='dict',
                disposition='/sqlconnectivity_update_settings',
                options=dict(
                    connectivity_type=dict(
                        type='str',
                        disposition='connectivity_type',
                        choices=['LOCAL',
                                 'PRIVATE',
                                 'PUBLIC']
                    ),
                    port=dict(
                        type='integer',
                        disposition='port'
                    ),
                    sqlauth_update_user_name=dict(
                        type='str',
                        disposition='sqlauth_update_user_name'
                    ),
                    sqlauth_update_password=dict(
                        type='str',
                        disposition='sqlauth_update_password'
                    )
                )
            ),
            sqlstorage_update_settings=dict(
                type='dict',
                disposition='/sqlstorage_update_settings',
                options=dict(
                    disk_count=dict(
                        type='integer',
                        disposition='disk_count'
                    ),
                    starting_device_id=dict(
                        type='integer',
                        disposition='starting_device_id'
                    ),
                    disk_configuration_type=dict(
                        type='str',
                        disposition='disk_configuration_type',
                        choices=['NEW',
                                 'EXTEND',
                                 'ADD']
                    )
                )
            ),
            is_rservices_enabled=dict(
                type='bool',
                disposition='/is_rservices_enabled'
            ),
            sqlworkload_type=dict(
                type='str',
                disposition='/sqlworkload_type',
                choices=['GENERAL',
                         'OLTP',
                         'DW']
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['SystemAssigned']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.sqlvirtual_machine_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSqlVirtualMachine, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlVirtualMachineManagementClient,
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
            response = self.mgmt_client.sql_virtual_machines.create_or_update(resource_group_name=self.resource_group_name,
                                                                              sqlvirtual_machine_name=self.sqlvirtual_machine_name,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SqlVirtualMachine instance.')
            self.fail('Error creating the SqlVirtualMachine instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sql_virtual_machines.delete(resource_group_name=self.resource_group_name,
                                                                    sqlvirtual_machine_name=self.sqlvirtual_machine_name)
        except CloudError as e:
            self.log('Error attempting to delete the SqlVirtualMachine instance.')
            self.fail('Error deleting the SqlVirtualMachine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sql_virtual_machines.get(resource_group_name=self.resource_group_name,
                                                                 sqlvirtual_machine_name=self.sqlvirtual_machine_name,
                                                                 expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSqlVirtualMachine()


if __name__ == '__main__':
    main()
