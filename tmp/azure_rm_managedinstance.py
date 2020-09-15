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
module: azure_rm_managedinstance
version_added: '2.9'
short_description: Manage Azure ManagedInstance instance.
description:
  - 'Create, update and delete instance of Azure ManagedInstance.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  sku:
    description:
      - >-
        Managed instance SKU. Allowed values for sku.name: GP_Gen4, GP_Gen5,
        BC_Gen4, BC_Gen5
      - Managed instance sku
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
  managed_instance_create_mode:
    description:
      - "Specifies the mode of database creation.\r"
      - "\r"
      - "Default: Regular instance creation.\r"
      - "\r"
      - >-
        Restore: Creates an instance by restoring a set of backups to specific
        point in time. RestorePointInTime and SourceManagedInstanceId must be
        specified.
    type: str
    choices:
      - Default
      - PointInTimeRestore
  administrator_login:
    description:
      - >-
        Administrator username for the managed instance. Can only be specified
        when the managed instance is being created (and is required for
        creation).
    type: str
  administrator_login_password:
    description:
      - >-
        The administrator login password (required for managed instance
        creation).
    type: str
  subnet_id:
    description:
      - Subnet resource ID for the managed instance.
    type: str
  license_type:
    description:
      - >-
        The license type. Possible values are 'LicenseIncluded' (regular price
        inclusive of a new SQL license) and 'BasePrice' (discounted AHB price
        for bringing your own SQL licenses).
    type: str
    choices:
      - LicenseIncluded
      - BasePrice
  v_cores:
    description:
      - 'The number of vCores. Allowed values: 8, 16, 24, 32, 40, 64, 80.'
    type: integer
  storage_size_in_gb:
    description:
      - >-
        Storage size in GB. Minimum value: 32. Maximum value: 8192. Increments
        of 32 GB allowed only.
    type: integer
  collation:
    description:
      - Collation of the managed instance.
    type: str
  dns_zone_partner:
    description:
      - >-
        The resource id of another managed instance whose DNS zone this managed
        instance will share after creation.
    type: str
  public_data_endpoint_enabled:
    description:
      - Whether or not the public data endpoint is enabled.
    type: bool
  source_managed_instance_id:
    description:
      - >-
        The resource identifier of the source managed instance associated with
        create operation of this instance.
    type: str
  restore_point_in_time:
    description:
      - >-
        Specifies the point in time (ISO8601 format) of the source database that
        will be restored to create the new database.
    type: str
  proxy_override:
    description:
      - Connection type used for connecting to the instance.
    type: str
    choices:
      - Proxy
      - Redirect
      - Default
  timezone_id:
    description:
      - "Id of the timezone. Allowed values are timezones supported by Windows.\r"
      - "Windows keeps details on supported timezones, including the id, in registry under\r"
      - "KEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones.\r"
      - "You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info.\r"
      - "List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.\r"
      - >-
        An example of valid timezone id is "Pacific Standard Time" or "W. Europe
        Standard Time".
    type: str
  instance_pool_id:
    description:
      - The Id of the instance pool this managed server belongs to.
    type: str
  maintenance_configuration_id:
    description:
      - >-
        Specifies maintenance configuration id to apply to this managed
        instance.
    type: str
  minimal_tls_version:
    description:
      - 'Minimal TLS version. Allowed values: ''None'', ''1.0'', ''1.1'', ''1.2'''
    type: str
  storage_account_type:
    description:
      - >-
        The storage account type used to store backups for this instance. The
        options are LRS (LocallyRedundantStorage), ZRS (ZoneRedundantStorage)
        and GRS (GeoRedundantStorage)
    type: str
    choices:
      - GRS
      - LRS
      - ZRS
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
      - Assert the state of the ManagedInstance.
      - >-
        Use C(present) to create or update an ManagedInstance and C(absent) to
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
    - name: Create managed instance with all properties
      azure_rm_managedinstance: 
        managed_instance_name: testinstance
        resource_group_name: testrg
        location: Japan East
        properties:
          administrator_login: dummylogin
          administrator_login_password: Un53cuRE!
          collation: SQL_Latin1_General_CP1_CI_AS
          dns_zone_partner: >-
            /subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Sql/managedInstances/testinstance
          instance_pool_id: >-
            /subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Sql/instancePools/pool1
          license_type: LicenseIncluded
          maintenance_configuration_id: >-
            /subscriptions/ab0e51c0-83c0-4380-8ae9-025516df392f/providers/Microsoft.Maintenance/publicMaintenanceConfigurations/SQL_WestEurope_MI_Mon_Fri_10PM_6AM
          proxy_override: Redirect
          public_data_endpoint_enabled: false
          storage_account_type: GRS
          storage_size_in_gb: 1024
          subnet_id: >-
            /subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Network/virtualNetworks/vnet1/subnets/subnet1
          timezone_id: UTC
          v_cores: 8
        sku:
          name: GP_Gen5
          tier: GeneralPurpose
        tags:
          tag_key1: TagValue1
        

    - name: Create managed instance with minimal properties
      azure_rm_managedinstance: 
        managed_instance_name: testinstance
        resource_group_name: testrg
        location: Japan East
        properties:
          administrator_login: dummylogin
          administrator_login_password: Un53cuRE!
          license_type: LicenseIncluded
          storage_size_in_gb: 1024
          subnet_id: >-
            /subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Network/virtualNetworks/vnet1/subnets/subnet1
          v_cores: 8
        sku:
          name: GP_Gen4
          tier: GeneralPurpose
        

    - name: Delete managed instance
      azure_rm_managedinstance: 
        managed_instance_name: testinstance
        resource_group_name: testrg
        

    - name: Update managed instance with all properties
      azure_rm_managedinstance: 
        managed_instance_name: testinstance
        resource_group_name: testrg
        properties:
          administrator_login: dummylogin
          administrator_login_password: Un53cuRE!
          collation: SQL_Latin1_General_CP1_CI_AS
          license_type: BasePrice
          maintenance_configuration_id: >-
            /subscriptions/ab0e51c0-83c0-4380-8ae9-025516df392f/providers/Microsoft.Maintenance/publicMaintenanceConfigurations/SQL_WestEurope_MI_Mon_Fri_10PM_6AM
          proxy_override: Redirect
          public_data_endpoint_enabled: false
          storage_size_in_gb: 448
          v_cores: 8
        sku:
          name: GP_Gen4
          capacity: 8
          tier: GeneralPurpose
        tags:
          tag_key1: TagValue1
        

    - name: Update managed instance with minimal properties
      azure_rm_managedinstance: 
        managed_instance_name: testinstance
        resource_group_name: testrg
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
sku:
  description:
    - >-
      Managed instance SKU. Allowed values for sku.name: GP_Gen4, GP_Gen5,
      BC_Gen4, BC_Gen5
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
provisioning_state:
  description:
    - ''
  returned: always
  type: str
  sample: null
managed_instance_create_mode:
  description:
    - "Specifies the mode of database creation.\r\n\r\nDefault: Regular instance creation.\r\n\r\nRestore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified."
  returned: always
  type: str
  sample: null
fully_qualified_domain_name:
  description:
    - The fully qualified domain name of the managed instance.
  returned: always
  type: str
  sample: null
administrator_login:
  description:
    - >-
      Administrator username for the managed instance. Can only be specified
      when the managed instance is being created (and is required for creation).
  returned: always
  type: str
  sample: null
administrator_login_password:
  description:
    - The administrator login password (required for managed instance creation).
  returned: always
  type: str
  sample: null
subnet_id:
  description:
    - Subnet resource ID for the managed instance.
  returned: always
  type: str
  sample: null
state:
  description:
    - The state of the managed instance.
  returned: always
  type: str
  sample: null
license_type:
  description:
    - >-
      The license type. Possible values are 'LicenseIncluded' (regular price
      inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for
      bringing your own SQL licenses).
  returned: always
  type: str
  sample: null
v_cores:
  description:
    - 'The number of vCores. Allowed values: 8, 16, 24, 32, 40, 64, 80.'
  returned: always
  type: integer
  sample: null
storage_size_in_gb:
  description:
    - >-
      Storage size in GB. Minimum value: 32. Maximum value: 8192. Increments of
      32 GB allowed only.
  returned: always
  type: integer
  sample: null
collation:
  description:
    - Collation of the managed instance.
  returned: always
  type: str
  sample: null
dns_zone:
  description:
    - The Dns Zone that the managed instance is in.
  returned: always
  type: str
  sample: null
dns_zone_partner:
  description:
    - >-
      The resource id of another managed instance whose DNS zone this managed
      instance will share after creation.
  returned: always
  type: str
  sample: null
public_data_endpoint_enabled:
  description:
    - Whether or not the public data endpoint is enabled.
  returned: always
  type: bool
  sample: null
source_managed_instance_id:
  description:
    - >-
      The resource identifier of the source managed instance associated with
      create operation of this instance.
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
proxy_override:
  description:
    - Connection type used for connecting to the instance.
  returned: always
  type: str
  sample: null
timezone_id:
  description:
    - "Id of the timezone. Allowed values are timezones supported by Windows.\r\nWindows keeps details on supported timezones, including the id, in registry under\r\nKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones.\r\nYou can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info.\r\nList of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.\r\nAn example of valid timezone id is \"Pacific Standard Time\" or \"W. Europe Standard Time\"."
  returned: always
  type: str
  sample: null
instance_pool_id:
  description:
    - The Id of the instance pool this managed server belongs to.
  returned: always
  type: str
  sample: null
maintenance_configuration_id:
  description:
    - Specifies maintenance configuration id to apply to this managed instance.
  returned: always
  type: str
  sample: null
minimal_tls_version:
  description:
    - 'Minimal TLS version. Allowed values: ''None'', ''1.0'', ''1.1'', ''1.2'''
  returned: always
  type: str
  sample: null
storage_account_type:
  description:
    - >-
      The storage account type used to store backups for this instance. The
      options are LRS (LocallyRedundantStorage), ZRS (ZoneRedundantStorage) and
      GRS (GeoRedundantStorage)
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagedInstance(AzureRMModuleBaseExt):
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
            managed_instance_create_mode=dict(
                type='str',
                disposition='/managed_instance_create_mode',
                choices=['Default',
                         'PointInTimeRestore']
            ),
            administrator_login=dict(
                type='str',
                disposition='/administrator_login'
            ),
            administrator_login_password=dict(
                type='str',
                disposition='/administrator_login_password'
            ),
            subnet_id=dict(
                type='str',
                disposition='/subnet_id'
            ),
            license_type=dict(
                type='str',
                disposition='/license_type',
                choices=['LicenseIncluded',
                         'BasePrice']
            ),
            v_cores=dict(
                type='integer',
                disposition='/v_cores'
            ),
            storage_size_in_gb=dict(
                type='integer',
                disposition='/storage_size_in_gb'
            ),
            collation=dict(
                type='str',
                disposition='/collation'
            ),
            dns_zone_partner=dict(
                type='str',
                disposition='/dns_zone_partner'
            ),
            public_data_endpoint_enabled=dict(
                type='bool',
                disposition='/public_data_endpoint_enabled'
            ),
            source_managed_instance_id=dict(
                type='str',
                disposition='/source_managed_instance_id'
            ),
            restore_point_in_time=dict(
                type='str',
                disposition='/restore_point_in_time'
            ),
            proxy_override=dict(
                type='str',
                disposition='/proxy_override',
                choices=['Proxy',
                         'Redirect',
                         'Default']
            ),
            timezone_id=dict(
                type='str',
                disposition='/timezone_id'
            ),
            instance_pool_id=dict(
                type='str',
                disposition='/instance_pool_id'
            ),
            maintenance_configuration_id=dict(
                type='str',
                disposition='/maintenance_configuration_id'
            ),
            minimal_tls_version=dict(
                type='str',
                disposition='/minimal_tls_version'
            ),
            storage_account_type=dict(
                type='str',
                disposition='/storage_account_type',
                choices=['GRS',
                         'LRS',
                         'ZRS']
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
        self.managed_instance_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedInstance, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-06-01-preview')

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
            response = self.mgmt_client.managed_instances.create_or_update(resource_group_name=self.resource_group_name,
                                                                           managed_instance_name=self.managed_instance_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedInstance instance.')
            self.fail('Error creating the ManagedInstance instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_instances.delete(resource_group_name=self.resource_group_name,
                                                                 managed_instance_name=self.managed_instance_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagedInstance instance.')
            self.fail('Error deleting the ManagedInstance instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_instances.get(resource_group_name=self.resource_group_name,
                                                              managed_instance_name=self.managed_instance_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedInstance()


if __name__ == '__main__':
    main()
