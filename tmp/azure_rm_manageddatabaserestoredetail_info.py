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
module: azure_rm_manageddatabaserestoredetail_info
version_added: '2.9'
short_description: Get ManagedDatabaseRestoreDetail info.
description:
  - Get info of ManagedDatabaseRestoreDetail.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
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
  restore_details_name:
    description:
      - The name of the restore details to retrieve.
    required: true
    type: str
    choices:
      - Default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Managed database restore details.
      azure_rm_manageddatabaserestoredetail_info: 
        database_name: testdb
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        restore_details_name: Default
        tags:
          tag_key1: TagValue1
        

'''

RETURN = '''
managed_database_restore_details:
  description: >-
    A list of dict results where the key is the name of the
    ManagedDatabaseRestoreDetail and the values are the facts for that
    ManagedDatabaseRestoreDetail.
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
    status:
      description:
        - Restore status.
      returned: always
      type: str
      sample: null
    current_restoring_file_name:
      description:
        - Current restoring file name.
      returned: always
      type: str
      sample: null
    last_restored_file_name:
      description:
        - Last restored file name.
      returned: always
      type: str
      sample: null
    last_restored_file_time:
      description:
        - Last restored file time.
      returned: always
      type: str
      sample: null
    percent_completed:
      description:
        - Percent completed.
      returned: always
      type: number
      sample: null
    unrestorable_files:
      description:
        - List of unrestorable files.
      returned: always
      type: list
      sample: null
    number_of_files_detected:
      description:
        - Number of files detected.
      returned: always
      type: integer
      sample: null
    last_uploaded_file_name:
      description:
        - Last uploaded file name.
      returned: always
      type: str
      sample: null
    last_uploaded_file_time:
      description:
        - Last uploaded file time.
      returned: always
      type: str
      sample: null
    block_reason:
      description:
        - The reason why restore is in Blocked state.
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


class AzureRMManagedDatabaseRestoreDetailInfo(AzureRMModuleBase):
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
            restore_details_name=dict(
                type='str',
                choices=['Default'],
                required=True
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.database_name = None
        self.restore_details_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-02-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedDatabaseRestoreDetailInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-02-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.database_name is not None and
            self.restore_details_name is not None):
            self.results['managed_database_restore_details'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_database_restore_details.get(resource_group_name=self.resource_group_name,
                                                                             managed_instance_name=self.managed_instance_name,
                                                                             database_name=self.database_name,
                                                                             restore_details_name=self.restore_details_name)
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
    AzureRMManagedDatabaseRestoreDetailInfo()


if __name__ == '__main__':
    main()
