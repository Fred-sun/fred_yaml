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
module: azure_rm_managedinstancelongtermretentionpolicy_info
version_added: '2.9'
short_description: Get ManagedInstanceLongTermRetentionPolicy info.
description:
  - Get info of ManagedInstanceLongTermRetentionPolicy.
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
  database_name:
    description:
      - The name of the database.
    required: true
    type: str
  policy_name:
    description:
      - The policy name. Should always be Default.
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get the long term retention policy for the managed database.
      azure_rm_managedinstancelongtermretentionpolicy_info: 
        database_name: testDatabase
        managed_instance_name: testInstance
        policy_name: default
        resource_group_name: testResourceGroup
        

    - name: Get the long term retention policies for the managed database.
      azure_rm_managedinstancelongtermretentionpolicy_info: 
        database_name: testDatabase
        managed_instance_name: testInstance
        resource_group_name: testResourceGroup
        

'''

RETURN = '''
managed_instance_long_term_retention_policies:
  description: >-
    A list of dict results where the key is the name of the
    ManagedInstanceLongTermRetentionPolicy and the values are the facts for that
    ManagedInstanceLongTermRetentionPolicy.
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
    weekly_retention:
      description:
        - The weekly retention policy for an LTR backup in an ISO 8601 format.
      returned: always
      type: str
      sample: null
    monthly_retention:
      description:
        - The monthly retention policy for an LTR backup in an ISO 8601 format.
      returned: always
      type: str
      sample: null
    yearly_retention:
      description:
        - The yearly retention policy for an LTR backup in an ISO 8601 format.
      returned: always
      type: str
      sample: null
    week_of_year:
      description:
        - The week of year to take the yearly backup in an ISO 8601 format.
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
        weekly_retention:
          description:
            - >-
              The weekly retention policy for an LTR backup in an ISO 8601
              format.
          returned: always
          type: str
          sample: null
        monthly_retention:
          description:
            - >-
              The monthly retention policy for an LTR backup in an ISO 8601
              format.
          returned: always
          type: str
          sample: null
        yearly_retention:
          description:
            - >-
              The yearly retention policy for an LTR backup in an ISO 8601
              format.
          returned: always
          type: str
          sample: null
        week_of_year:
          description:
            - The week of year to take the yearly backup in an ISO 8601 format.
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


class AzureRMManagedInstanceLongTermRetentionPolicyInfo(AzureRMModuleBase):
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
            database_name=dict(
                type='str',
                required=True
            ),
            policy_name=dict(
                type='str',
                choices=['default']
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.database_name = None
        self.policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedInstanceLongTermRetentionPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.database_name is not None and
            self.policy_name is not None):
            self.results['managed_instance_long_term_retention_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None and
              self.database_name is not None):
            self.results['managed_instance_long_term_retention_policies'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_long_term_retention_policies.get(resource_group_name=self.resource_group_name,
                                                                                          managed_instance_name=self.managed_instance_name,
                                                                                          database_name=self.database_name,
                                                                                          policy_name=self.policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_long_term_retention_policies.list_by_database(resource_group_name=self.resource_group_name,
                                                                                                       managed_instance_name=self.managed_instance_name,
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
    AzureRMManagedInstanceLongTermRetentionPolicyInfo()


if __name__ == '__main__':
    main()
