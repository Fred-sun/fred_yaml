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
module: azure_rm_restorabledroppeddatabase
version_added: '2.9'
short_description: Manage Azure RestorableDroppedDatabase instance.
description:
  - 'Create, update and delete instance of Azure RestorableDroppedDatabase.'
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
  restorable_droppeded_database_id:
    description:
      - >-
        The id of the deleted database in the form of
        databaseName,deletionTimeInFileTimeFormat
    required: true
    type: str
  state:
    description:
      - Assert the state of the RestorableDroppedDatabase.
      - >-
        Use C(present) to create or update an RestorableDroppedDatabase and
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
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
database_name:
  description:
    - The name of the database
  returned: always
  type: str
  sample: null
edition:
  description:
    - The edition of the database
  returned: always
  type: str
  sample: null
max_size_bytes:
  description:
    - The max size in bytes of the database
  returned: always
  type: str
  sample: null
service_level_objective:
  description:
    - The service level objective name of the database
  returned: always
  type: str
  sample: null
elastic_pool_name:
  description:
    - The elastic pool name of the database
  returned: always
  type: str
  sample: null
creation_date:
  description:
    - The creation date of the database (ISO8601 format)
  returned: always
  type: str
  sample: null
deletion_date:
  description:
    - The deletion date of the database (ISO8601 format)
  returned: always
  type: str
  sample: null
earliest_restore_date:
  description:
    - The earliest restore date of the database (ISO8601 format)
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRestorableDroppedDatabase(AzureRMModuleBaseExt):
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
            restorable_droppeded_database_id=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.restorable_droppeded_database_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRestorableDroppedDatabase, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2014-04-01')

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
                response = self.mgmt_client.restorable_dropped_databases.create()
            else:
                response = self.mgmt_client.restorable_dropped_databases.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RestorableDroppedDatabase instance.')
            self.fail('Error creating the RestorableDroppedDatabase instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.restorable_dropped_databases.delete()
        except CloudError as e:
            self.log('Error attempting to delete the RestorableDroppedDatabase instance.')
            self.fail('Error deleting the RestorableDroppedDatabase instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.restorable_dropped_databases.get(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         restorable_droppeded_database_id=self.restorable_droppeded_database_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRestorableDroppedDatabase()


if __name__ == '__main__':
    main()
