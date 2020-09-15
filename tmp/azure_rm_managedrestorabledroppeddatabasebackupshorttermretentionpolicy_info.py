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
module: azure_rm_managedrestorabledroppeddatabasebackupshorttermretentionpolicy_info
version_added: '2.9'
short_description: Get ManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicy info.
description:
  - Get info of ManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicy.
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
  restorable_dropped_database_id:
    description:
      - undefined
    required: true
    type: str
  policy_name:
    description:
      - The policy name.
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get the short term retention policy for the database.
      azure_rm_managedrestorabledroppeddatabasebackupshorttermretentionpolicy_info: 
        managed_instance_name: testsvr
        policy_name: default
        resource_group_name: Default-SQL-SouthEastAsia
        restorable_dropped_database_id: 'testdb,131403269876900000'
        

    - name: Get the short term retention policy list for the database.
      azure_rm_managedrestorabledroppeddatabasebackupshorttermretentionpolicy_info: 
        managed_instance_name: testsvr
        resource_group_name: Default-SQL-SouthEastAsia
        restorable_dropped_database_id: 'testdb,131403269876900000'
        

'''

RETURN = '''
managed_restorable_dropped_database_backup_short_term_retention_policies:
  description: >-
    A list of dict results where the key is the name of the
    ManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicy and the
    values are the facts for that
    ManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicy.
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
    retention_days:
      description:
        - >-
          The backup retention period in days. This is how many days
          Point-in-Time Restore will be supported.
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
        retention_days:
          description:
            - >-
              The backup retention period in days. This is how many days
              Point-in-Time Restore will be supported.
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


class AzureRMManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicyInfo(AzureRMModuleBase):
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
            restorable_dropped_database_id=dict(
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
        self.restorable_dropped_database_id = None
        self.policy_name = None

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
        super(AzureRMManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.restorable_dropped_database_id is not None and
            self.policy_name is not None):
            self.results['managed_restorable_dropped_database_backup_short_term_retention_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None and
              self.restorable_dropped_database_id is not None):
            self.results['managed_restorable_dropped_database_backup_short_term_retention_policies'] = self.format_item(self.listbyrestorabledroppeddatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_restorable_dropped_database_backup_short_term_retention_policies.get(resource_group_name=self.resource_group_name,
                                                                                                                     managed_instance_name=self.managed_instance_name,
                                                                                                                     restorable_dropped_database_id=self.restorable_dropped_database_id,
                                                                                                                     policy_name=self.policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyrestorabledroppeddatabase(self):
        response = None

        try:
            response = self.mgmt_client.managed_restorable_dropped_database_backup_short_term_retention_policies.list_by_restorable_dropped_database(resource_group_name=self.resource_group_name,
                                                                                                                                                     managed_instance_name=self.managed_instance_name,
                                                                                                                                                     restorable_dropped_database_id=self.restorable_dropped_database_id)
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
    AzureRMManagedRestorableDroppedDatabaseBackupShortTermRetentionPolicyInfo()


if __name__ == '__main__':
    main()
