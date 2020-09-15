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
module: azure_rm_restorabledroppedmanageddatabase_info
version_added: '2.9'
short_description: Get RestorableDroppedManagedDatabase info.
description:
  - Get info of RestorableDroppedManagedDatabase.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List restorable dropped databases by managed instances
      azure_rm_restorabledroppedmanageddatabase_info: 
        managed_instance_name: managedInstance
        resource_group_name: Test1
        

    - name: Gets a restorable dropped managed database.
      azure_rm_restorabledroppedmanageddatabase_info: 
        managed_instance_name: managedInstance
        resource_group_name: Test1
        restorable_dropped_database_id: 'testdb,131403269876900000'
        

'''

RETURN = '''
restorable_dropped_managed_databases:
  description: >-
    A list of dict results where the key is the name of the
    RestorableDroppedManagedDatabase and the values are the facts for that
    RestorableDroppedManagedDatabase.
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
        database_name:
          description:
            - The name of the database.
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of the database (ISO8601 format).
          returned: always
          type: str
          sample: null
        deletion_date:
          description:
            - The deletion date of the database (ISO8601 format).
          returned: always
          type: str
          sample: null
        earliest_restore_date:
          description:
            - The earliest restore date of the database (ISO8601 format).
          returned: always
          type: str
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
    database_name:
      description:
        - The name of the database.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of the database (ISO8601 format).
      returned: always
      type: str
      sample: null
    deletion_date:
      description:
        - The deletion date of the database (ISO8601 format).
      returned: always
      type: str
      sample: null
    earliest_restore_date:
      description:
        - The earliest restore date of the database (ISO8601 format).
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


class AzureRMRestorableDroppedManagedDatabaseInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.restorable_dropped_database_id = None

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
        super(AzureRMRestorableDroppedManagedDatabaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.restorable_dropped_database_id is not None):
            self.results['restorable_dropped_managed_databases'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['restorable_dropped_managed_databases'] = self.format_item(self.listbyinstance())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.restorable_dropped_managed_databases.get(resource_group_name=self.resource_group_name,
                                                                                 managed_instance_name=self.managed_instance_name,
                                                                                 restorable_dropped_database_id=self.restorable_dropped_database_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstance(self):
        response = None

        try:
            response = self.mgmt_client.restorable_dropped_managed_databases.list_by_instance(resource_group_name=self.resource_group_name,
                                                                                              managed_instance_name=self.managed_instance_name)
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
    AzureRMRestorableDroppedManagedDatabaseInfo()


if __name__ == '__main__':
    main()
