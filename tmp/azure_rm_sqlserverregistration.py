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
module: azure_rm_sqlserverregistration
version_added: '2.9'
short_description: Manage Azure SqlServerRegistration instance.
description:
  - 'Create, update and delete instance of Azure SqlServerRegistration.'
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
  location:
    description:
      - The geo-location where the resource lives
    type: str
  resource_group:
    description:
      - Resource Group Name
    type: str
  property_bag:
    description:
      - Optional Properties as JSON string
    type: str
  state:
    description:
      - Assert the state of the SqlServerRegistration.
      - >-
        Use C(present) to create or update an SqlServerRegistration and
        C(absent) to delete it.
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
    - name: Creates or updates a SQL Server registration.
      azure_rm_sqlserverregistration: 
        resource_group_name: testrg
        location: northeurope
        properties: {}
        tags:
          mytag: myval
        

    - name: Deletes a SQL Server registration.
      azure_rm_sqlserverregistration: 
        resource_group_name: testrg
        

    - name: Updates a SQL Server Registration tags.
      azure_rm_sqlserverregistration: 
        resource_group_name: testrg
        tags:
          mytag: myval
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
system_data:
  description:
    - Read only system data
  returned: always
  type: dict
  sample: null
  contains:
    created_by:
      description:
        - An identifier for the identity that created the resource
      returned: always
      type: str
      sample: null
    created_by_type:
      description:
        - The type of identity that created the resource
      returned: always
      type: str
      sample: null
    created_at:
      description:
        - The timestamp of resource creation (UTC)
      returned: always
      type: str
      sample: null
    last_modified_by:
      description:
        - An identifier for the identity that last modified the resource
      returned: always
      type: str
      sample: null
    last_modified_by_type:
      description:
        - The type of identity that last modified the resource
      returned: always
      type: str
      sample: null
    last_modified_at:
      description:
        - The timestamp of resource last modification (UTC)
      returned: always
      type: str
      sample: null
subscription_id:
  description:
    - Subscription Id
  returned: always
  type: str
  sample: null
resource_group:
  description:
    - Resource Group Name
  returned: always
  type: str
  sample: null
property_bag:
  description:
    - Optional Properties as JSON string
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


class AzureRMSqlServerRegistration(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            resource_group=dict(
                type='str',
                disposition='/resource_group'
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSqlServerRegistration, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.sql_server_registrations.create_or_update(resource_group_name=self.resource_group_name,
                                                                                  sqlserver_registration_name=self.sqlserver_registration_name,
                                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SqlServerRegistration instance.')
            self.fail('Error creating the SqlServerRegistration instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sql_server_registrations.delete(resource_group_name=self.resource_group_name,
                                                                        sqlserver_registration_name=self.sqlserver_registration_name)
        except CloudError as e:
            self.log('Error attempting to delete the SqlServerRegistration instance.')
            self.fail('Error deleting the SqlServerRegistration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sql_server_registrations.get(resource_group_name=self.resource_group_name,
                                                                     sqlserver_registration_name=self.sqlserver_registration_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSqlServerRegistration()


if __name__ == '__main__':
    main()
