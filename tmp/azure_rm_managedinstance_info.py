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
module: azure_rm_managedinstance_info
version_added: '2.9'
short_description: Get ManagedInstance info.
description:
  - Get info of ManagedInstance.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    type: str
  instance_pool_name:
    description:
      - The instance pool name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List managed instances by resource group
      azure_rm_managedinstance_info: 
        resource_group_name: Test1
        

    - name: Get managed instance
      azure_rm_managedinstance_info: 
        managed_instance_name: testinstance
        resource_group_name: testrg
        

    - name: List managed instances by instance pool
      azure_rm_managedinstance_info: 
        instance_pool_name: pool1
        resource_group_name: Test1
        

    - name: List managed instances
      azure_rm_managedinstance_info: 
        {}
        

'''

RETURN = '''
managed_instances:
  description: >-
    A list of dict results where the key is the name of the ManagedInstance and
    the values are the facts for that ManagedInstance.
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
        sku:
          description:
            - >-
              Managed instance SKU. Allowed values for sku.name: GP_Gen4,
              GP_Gen5, BC_Gen4, BC_Gen5
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the SKU, typically, a letter + Number code, e.g.
                  P3.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - >-
                  The tier or edition of the particular SKU, e.g. Basic,
                  Premium.
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
                  If the service has different generations of hardware, for the
                  same SKU, then that can be captured here.
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
              Administrator username for the managed instance. Can only be
              specified when the managed instance is being created (and is
              required for creation).
          returned: always
          type: str
          sample: null
        administrator_login_password:
          description:
            - >-
              The administrator login password (required for managed instance
              creation).
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
              The license type. Possible values are 'LicenseIncluded' (regular
              price inclusive of a new SQL license) and 'BasePrice' (discounted
              AHB price for bringing your own SQL licenses).
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
              Storage size in GB. Minimum value: 32. Maximum value: 8192.
              Increments of 32 GB allowed only.
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
              The resource id of another managed instance whose DNS zone this
              managed instance will share after creation.
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
              The resource identifier of the source managed instance associated
              with create operation of this instance.
          returned: always
          type: str
          sample: null
        restore_point_in_time:
          description:
            - >-
              Specifies the point in time (ISO8601 format) of the source
              database that will be restored to create the new database.
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
            - >-
              Specifies maintenance configuration id to apply to this managed
              instance.
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
              The storage account type used to store backups for this instance.
              The options are LRS (LocallyRedundantStorage), ZRS
              (ZoneRedundantStorage) and GRS (GeoRedundantStorage)
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
          when the managed instance is being created (and is required for
          creation).
      returned: always
      type: str
      sample: null
    administrator_login_password:
      description:
        - >-
          The administrator login password (required for managed instance
          creation).
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
          inclusive of a new SQL license) and 'BasePrice' (discounted AHB price
          for bringing your own SQL licenses).
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
          Storage size in GB. Minimum value: 32. Maximum value: 8192. Increments
          of 32 GB allowed only.
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
          The resource id of another managed instance whose DNS zone this
          managed instance will share after creation.
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
          Specifies the point in time (ISO8601 format) of the source database
          that will be restored to create the new database.
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
        - >-
          Specifies maintenance configuration id to apply to this managed
          instance.
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
          options are LRS (LocallyRedundantStorage), ZRS (ZoneRedundantStorage)
          and GRS (GeoRedundantStorage)
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagedInstanceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            managed_instance_name=dict(
                type='str'
            ),
            instance_pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.instance_pool_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedInstanceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None):
            self.results['managed_instances'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.instance_pool_name is not None):
            self.results['managed_instances'] = self.format_item(self.listbyinstancepool())
        elif (self.resource_group_name is not None):
            self.results['managed_instances'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['managed_instances'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_instances.get(resource_group_name=self.resource_group_name,
                                                              managed_instance_name=self.managed_instance_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstancepool(self):
        response = None

        try:
            response = self.mgmt_client.managed_instances.list_by_instance_pool(resource_group_name=self.resource_group_name,
                                                                                instance_pool_name=self.instance_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.managed_instances.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.managed_instances.list()
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
    AzureRMManagedInstanceInfo()


if __name__ == '__main__':
    main()
