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
module: azure_rm_sqlserver
version_added: '2.9'
short_description: Manage Azure SqlServer instance.
description:
  - 'Create, update and delete instance of Azure SqlServer.'
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  sqlserver_registration_name:
    description:
      - Name of the SQL Server registration.
    required: true
    type: str
  sqlserver_name:
    description:
      - Name of the SQL Server.
    required: true
    type: str
  expand:
    description:
      - The child resources to include in the response.
    type: str
  cores:
    description:
      - Cores of the Sql Server.
    type: integer
  version:
    description:
      - Version of the Sql Server.
    type: str
  edition:
    description:
      - Sql Server Edition.
    type: str
  registration_id:
    description:
      - ID for Parent Sql Server Registration.
    type: str
  property_bag:
    description:
      - Sql Server Json Property Bag.
    type: str
  state:
    description:
      - Assert the state of the SqlServer.
      - >-
        Use C(present) to create or update an SqlServer and C(absent) to delete
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
    - name: Creates or updates a SQL Server in a Registration group.
      azure_rm_sqlserver: 
        resource_group_name: testrg
        properties:
          cores: 8
          edition: Latin
          property_bag: ''
          registration_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.AzureData/SqlServerRegistrations/testsqlregistration
          version: '2008'
        

    - name: Deletes a SQL Server.
      azure_rm_sqlserver: 
        resource_group_name: testrg
        

'''

RETURN = '''
id:
  description:
    - >-
      Fully qualified resource Id for the resource. Ex -
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource. Ex- Microsoft.Compute/virtualMachines or
      Microsoft.Storage/storageAccounts.
  returned: always
  type: str
  sample: null
cores:
  description:
    - Cores of the Sql Server.
  returned: always
  type: integer
  sample: null
version:
  description:
    - Version of the Sql Server.
  returned: always
  type: str
  sample: null
edition:
  description:
    - Sql Server Edition.
  returned: always
  type: str
  sample: null
registration_id:
  description:
    - ID for Parent Sql Server Registration.
  returned: always
  type: str
  sample: null
property_bag:
  description:
    - Sql Server Json Property Bag.
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
    from azure.mgmt.azure import AzureDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSqlServer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sqlserver_registration_name=dict(
                type='str',
                required=True
            ),
            sqlserver_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            cores=dict(
                type='integer',
                disposition='/cores'
            ),
            version=dict(
                type='str',
                disposition='/version'
            ),
            edition=dict(
                type='str',
                disposition='/edition'
            ),
            registration_id=dict(
                type='str',
                disposition='/registration_id'
            ),
            property_bag=dict(
                type='str',
                disposition='/property_bag'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.sqlserver_registration_name = None
        self.sqlserver_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSqlServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AzureDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-24-preview')

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
            response = self.mgmt_client.sql_servers.create_or_update(resource_group_name=self.resource_group_name,
                                                                     sqlserver_registration_name=self.sqlserver_registration_name,
                                                                     sqlserver_name=self.sqlserver_name,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SqlServer instance.')
            self.fail('Error creating the SqlServer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sql_servers.delete(resource_group_name=self.resource_group_name,
                                                           sqlserver_registration_name=self.sqlserver_registration_name,
                                                           sqlserver_name=self.sqlserver_name)
        except CloudError as e:
            self.log('Error attempting to delete the SqlServer instance.')
            self.fail('Error deleting the SqlServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sql_servers.get(resource_group_name=self.resource_group_name,
                                                        sqlserver_registration_name=self.sqlserver_registration_name,
                                                        sqlserver_name=self.sqlserver_name,
                                                        expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSqlServer()


if __name__ == '__main__':
    main()
