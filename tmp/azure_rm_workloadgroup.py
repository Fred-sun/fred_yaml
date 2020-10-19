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
module: azure_rm_workloadgroup
version_added: '2.9'
short_description: Manage Azure WorkloadGroup instance.
description:
  - 'Create, update and delete instance of Azure WorkloadGroup.'
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
  workload_group_name:
    description:
      - The name of the workload group.
      - The name of the workload group to delete.
    required: true
    type: str
  min_resource_percent:
    description:
      - The workload group minimum percentage resource.
    type: integer
  max_resource_percent:
    description:
      - The workload group cap percentage resource.
    type: integer
  min_resource_percent_per_request:
    description:
      - The workload group request minimum grant percentage.
    type: number
  max_resource_percent_per_request:
    description:
      - The workload group request maximum grant percentage.
    type: number
  importance:
    description:
      - The workload group importance level.
    type: str
  query_execution_timeout:
    description:
      - The workload group query execution timeout.
    type: integer
  state:
    description:
      - Assert the state of the WorkloadGroup.
      - >-
        Use C(present) to create or update an WorkloadGroup and C(absent) to
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
    - name: Create a workload group with all properties specified.
      azure_rm_workloadgroup: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_group_name: smallrc
        properties:
          importance: normal
          max_resource_percent: 100
          max_resource_percent_per_request: 3
          min_resource_percent: 0
          min_resource_percent_per_request: 3
          query_execution_timeout: 0
        

    - name: Create a workload group with the required properties specified.
      azure_rm_workloadgroup: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_group_name: smallrc
        properties:
          max_resource_percent: 100
          min_resource_percent: 0
          min_resource_percent_per_request: 3
        

    - name: Delete a workload group
      azure_rm_workloadgroup: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_group_name: wlm_workloadgroup
        

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
min_resource_percent:
  description:
    - The workload group minimum percentage resource.
  returned: always
  type: integer
  sample: null
max_resource_percent:
  description:
    - The workload group cap percentage resource.
  returned: always
  type: integer
  sample: null
min_resource_percent_per_request:
  description:
    - The workload group request minimum grant percentage.
  returned: always
  type: number
  sample: null
max_resource_percent_per_request:
  description:
    - The workload group request maximum grant percentage.
  returned: always
  type: number
  sample: null
importance:
  description:
    - The workload group importance level.
  returned: always
  type: str
  sample: null
query_execution_timeout:
  description:
    - The workload group query execution timeout.
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


class AzureRMWorkloadGroup(AzureRMModuleBaseExt):
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
            workload_group_name=dict(
                type='str',
                required=True
            ),
            min_resource_percent=dict(
                type='integer',
                disposition='/min_resource_percent'
            ),
            max_resource_percent=dict(
                type='integer',
                disposition='/max_resource_percent'
            ),
            min_resource_percent_per_request=dict(
                type='number',
                disposition='/min_resource_percent_per_request'
            ),
            max_resource_percent_per_request=dict(
                type='number',
                disposition='/max_resource_percent_per_request'
            ),
            importance=dict(
                type='str',
                disposition='/importance'
            ),
            query_execution_timeout=dict(
                type='integer',
                disposition='/query_execution_timeout'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.workload_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMWorkloadGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.workload_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         database_name=self.database_name,
                                                                         workload_group_name=self.workload_group_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the WorkloadGroup instance.')
            self.fail('Error creating the WorkloadGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.workload_groups.delete(resource_group_name=self.resource_group_name,
                                                               server_name=self.server_name,
                                                               database_name=self.database_name,
                                                               workload_group_name=self.workload_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the WorkloadGroup instance.')
            self.fail('Error deleting the WorkloadGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.workload_groups.get(resource_group_name=self.resource_group_name,
                                                            server_name=self.server_name,
                                                            database_name=self.database_name,
                                                            workload_group_name=self.workload_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMWorkloadGroup()


if __name__ == '__main__':
    main()
