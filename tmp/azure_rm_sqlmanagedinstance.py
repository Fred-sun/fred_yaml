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
module: azure_rm_sqlmanagedinstance
version_added: '2.9'
short_description: Manage Azure SqlManagedInstance instance.
description:
  - 'Create, update and delete instance of Azure SqlManagedInstance.'
options:
  resource_group_name:
    description:
      - The name of the Azure resource group
    required: true
    type: str
  sqlmanaged_instance_name:
    description:
      - Name of SQL Managed Instance
      - The name of SQL Managed Instances
      - The name of Sql Managed Instances
      - Name of sqlManagedInstance
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  data_controller_id:
    description:
      - 'null'
    type: str
  instance_endpoint:
    description:
      - The on premise instance endpoint
    type: str
  admin:
    description:
      - The instance admin user
    type: str
  start_time:
    description:
      - The instance start time
    type: str
  end_time:
    description:
      - The instance end time
    type: str
  v_core:
    description:
      - The instance vCore
    type: str
  state:
    description:
      - Assert the state of the SqlManagedInstance.
      - >-
        Use C(present) to create or update an SqlManagedInstance and C(absent)
        to delete it.
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
    - name: Updates a SQL Managed Instance tags.
      azure_rm_sqlmanagedinstance: 
        resource_group_name: testrg
        location: northeurope
        properties:
          admin: Admin user
          end_time: Instance end time
          instance_endpoint: The on premise instance endpoint
          start_time: Instance start time
        tags:
          mytag: myval
        

    - name: Delete a SQL Instance.
      azure_rm_sqlmanagedinstance: 
        resource_group_name: testrg
        

    - name: Updates a sql Instance tags.
      azure_rm_sqlmanagedinstance: 
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
data_controller_id:
  description:
    - 'null'
  returned: always
  type: str
  sample: null
instance_endpoint:
  description:
    - The on premise instance endpoint
  returned: always
  type: str
  sample: null
admin:
  description:
    - The instance admin user
  returned: always
  type: str
  sample: null
start_time:
  description:
    - The instance start time
  returned: always
  type: str
  sample: null
end_time:
  description:
    - The instance end time
  returned: always
  type: str
  sample: null
v_core:
  description:
    - The instance vCore
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


class AzureRMSqlManagedInstance(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sqlmanaged_instance_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            data_controller_id=dict(
                type='str',
                disposition='/data_controller_id'
            ),
            instance_endpoint=dict(
                type='str',
                disposition='/instance_endpoint'
            ),
            admin=dict(
                type='str',
                disposition='/admin'
            ),
            start_time=dict(
                type='str',
                disposition='/start_time'
            ),
            end_time=dict(
                type='str',
                disposition='/end_time'
            ),
            v_core=dict(
                type='str',
                disposition='/v_core'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.sqlmanaged_instance_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSqlManagedInstance, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.sql_managed_instances.create(resource_group_name=self.resource_group_name,
                                                                         sqlmanaged_instance_name=self.sqlmanaged_instance_name,
                                                                         parameters=self.body)
            else:
                response = self.mgmt_client.sql_managed_instances.update(resource_group_name=self.resource_group_name,
                                                                         sqlmanaged_instance_name=self.sqlmanaged_instance_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SqlManagedInstance instance.')
            self.fail('Error creating the SqlManagedInstance instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sql_managed_instances.delete(resource_group_name=self.resource_group_name,
                                                                     sqlmanaged_instance_name=self.sqlmanaged_instance_name)
        except CloudError as e:
            self.log('Error attempting to delete the SqlManagedInstance instance.')
            self.fail('Error deleting the SqlManagedInstance instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sql_managed_instances.get(resource_group_name=self.resource_group_name,
                                                                  sqlmanaged_instance_name=self.sqlmanaged_instance_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSqlManagedInstance()


if __name__ == '__main__':
    main()
