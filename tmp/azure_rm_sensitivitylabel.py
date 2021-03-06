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
module: azure_rm_sensitivitylabel
version_added: '2.9'
short_description: Manage Azure SensitivityLabel instance.
description:
  - 'Create, update and delete instance of Azure SensitivityLabel.'
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
  schema_name:
    description:
      - The name of the schema.
    required: true
    type: str
  table_name:
    description:
      - The name of the table.
    required: true
    type: str
  column_name:
    description:
      - The name of the column.
    required: true
    type: str
  sensitivity_label_source:
    description:
      - The source of the sensitivity label.
    type: sealed-choice
  sensitivitylabelsource:
    description:
      - The source of the sensitivity label.
    type: constant
  label_name:
    description:
      - The label name.
    type: str
  label_id:
    description:
      - The label ID.
    type: str
  information_type:
    description:
      - The information type.
    type: str
  information_type_id:
    description:
      - The information type ID.
    type: str
  rank:
    description:
      - undefined
    type: sealed-choice
  state:
    description:
      - Assert the state of the SensitivityLabel.
      - >-
        Use C(present) to create or update an SensitivityLabel and C(absent) to
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
    - name: Updates the sensitivity label of a given column with all parameters
      azure_rm_sensitivitylabel: 
        column_name: myColumn
        database_name: myDatabase
        resource_group_name: myRG
        schema_name: dbo
        server_name: myServer
        table_name: myTable
        properties:
          information_type: PhoneNumber
          information_type_id: d22fa6e9-5ee4-3bde-4c2b-a409604c4646
          label_id: bf91e08c-f4f0-478a-b016-25164b2a65ff
          label_name: PII
        

    - name: Deletes the sensitivity label of a given column
      azure_rm_sensitivitylabel: 
        column_name: myColumn
        database_name: myDatabase
        resource_group_name: myRG
        schema_name: dbo
        server_name: myServer
        table_name: myTable
        

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
label_name:
  description:
    - The label name.
  returned: always
  type: str
  sample: null
label_id:
  description:
    - The label ID.
  returned: always
  type: str
  sample: null
information_type:
  description:
    - The information type.
  returned: always
  type: str
  sample: null
information_type_id:
  description:
    - The information type ID.
  returned: always
  type: str
  sample: null
is_disabled:
  description:
    - >-
      Is sensitivity recommendation disabled. Applicable for recommended
      sensitivity label only. Specifies whether the sensitivity recommendation
      on this column is disabled (dismissed) or not.
  returned: always
  type: bool
  sample: null
rank:
  description:
    - ''
  returned: always
  type: sealed-choice
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


class AzureRMSensitivityLabel(AzureRMModuleBaseExt):
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
            schema_name=dict(
                type='str',
                required=True
            ),
            table_name=dict(
                type='str',
                required=True
            ),
            column_name=dict(
                type='str',
                required=True
            ),
            sensitivity_label_source=dict(
                type='sealed-choice'
            ),
            sensitivitylabelsource=dict(
                type='constant'
            ),
            label_name=dict(
                type='str',
                disposition='/label_name'
            ),
            label_id=dict(
                type='str',
                disposition='/label_id'
            ),
            information_type=dict(
                type='str',
                disposition='/information_type'
            ),
            information_type_id=dict(
                type='str',
                disposition='/information_type_id'
            ),
            rank=dict(
                type='sealed-choice',
                disposition='/rank'
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
        self.schema_name = None
        self.table_name = None
        self.column_name = None
        self.sensitivity_label_source = None
        self.sensitivitylabelsource = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSensitivityLabel, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-03-01-preview')

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
            response = self.mgmt_client.sensitivity_labels.create_or_update(resource_group_name=self.resource_group_name,
                                                                            server_name=self.server_name,
                                                                            database_name=self.database_name,
                                                                            schema_name=self.schema_name,
                                                                            table_name=self.table_name,
                                                                            column_name=self.column_name,
                                                                            sensitivitylabelsource=self.sensitivitylabelsource,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SensitivityLabel instance.')
            self.fail('Error creating the SensitivityLabel instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sensitivity_labels.delete(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  database_name=self.database_name,
                                                                  schema_name=self.schema_name,
                                                                  table_name=self.table_name,
                                                                  column_name=self.column_name,
                                                                  sensitivitylabelsource=self.sensitivitylabelsource)
        except CloudError as e:
            self.log('Error attempting to delete the SensitivityLabel instance.')
            self.fail('Error deleting the SensitivityLabel instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sensitivity_labels.get(resource_group_name=self.resource_group_name,
                                                               server_name=self.server_name,
                                                               database_name=self.database_name,
                                                               schema_name=self.schema_name,
                                                               table_name=self.table_name,
                                                               column_name=self.column_name,
                                                               sensitivity_label_source=self.sensitivity_label_source)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSensitivityLabel()


if __name__ == '__main__':
    main()
