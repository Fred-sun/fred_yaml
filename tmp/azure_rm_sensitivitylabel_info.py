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
module: azure_rm_sensitivitylabel_info
version_added: '2.9'
short_description: Get SensitivityLabel info.
description:
  - Get info of SensitivityLabel.
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
  filter:
    description:
      - An OData filter expression that filters elements in the collection.
    type: str
  include_disabled_recommendations:
    description:
      - Specifies whether to include disabled recommendations or not.
    type: bool
  skip_token:
    description:
      - undefined
    type: str
  schema_name:
    description:
      - The name of the schema.
    type: str
  table_name:
    description:
      - The name of the table.
    type: str
  column_name:
    description:
      - The name of the column.
    type: str
  sensitivity_label_source:
    description:
      - The source of the sensitivity label.
    type: sealed-choice
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets the current sensitivity labels of a given database
      azure_rm_sensitivitylabel_info: 
        database_name: myDatabase
        resource_group_name: myRG
        server_name: myServer
        

    - name: Gets the recommended sensitivity labels of a given database
      azure_rm_sensitivitylabel_info: 
        database_name: myDatabase
        resource_group_name: myRG
        server_name: myServer
        

    - name: Gets the sensitivity label of a given column
      azure_rm_sensitivitylabel_info: 
        column_name: myColumn
        database_name: myDatabase
        resource_group_name: myRG
        schema_name: dbo
        sensitivity_label_source: current
        server_name: myServer
        table_name: myTable
        

'''

RETURN = '''
sensitivity_labels:
  description: >-
    A list of dict results where the key is the name of the SensitivityLabel and
    the values are the facts for that SensitivityLabel.
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
              sensitivity label only. Specifies whether the sensitivity
              recommendation on this column is disabled (dismissed) or not.
          returned: always
          type: bool
          sample: null
        rank:
          description:
            - ''
          returned: always
          type: sealed-choice
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
          sensitivity label only. Specifies whether the sensitivity
          recommendation on this column is disabled (dismissed) or not.
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


class AzureRMSensitivityLabelInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            include_disabled_recommendations=dict(
                type='bool'
            ),
            skip_token=dict(
                type='str'
            ),
            schema_name=dict(
                type='str'
            ),
            table_name=dict(
                type='str'
            ),
            column_name=dict(
                type='str'
            ),
            sensitivity_label_source=dict(
                type='sealed-choice'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.filter = None
        self.include_disabled_recommendations = None
        self.skip_token = None
        self.schema_name = None
        self.table_name = None
        self.column_name = None
        self.sensitivity_label_source = None

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
        super(AzureRMSensitivityLabelInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.schema_name is not None and
            self.table_name is not None and
            self.column_name is not None and
            self.sensitivity_label_source is not None):
            self.results['sensitivity_labels'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['sensitivity_labels'] = self.format_item(self.listrecommendedbydatabase())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['sensitivity_labels'] = self.format_item(self.listcurrentbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sensitivity_labels.get(resource_group_name=self.resource_group_name,
                                                               server_name=self.server_name,
                                                               database_name=self.database_name,
                                                               schema_name=self.schema_name,
                                                               table_name=self.table_name,
                                                               column_name=self.column_name,
                                                               sensitivity_label_source=self.sensitivity_label_source)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listrecommendedbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.sensitivity_labels.list_recommended_by_database(resource_group_name=self.resource_group_name,
                                                                                        server_name=self.server_name,
                                                                                        database_name=self.database_name,
                                                                                        include_disabled_recommendations=self.include_disabled_recommendations,
                                                                                        skip_token=self.skip_token,
                                                                                        filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listcurrentbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.sensitivity_labels.list_current_by_database(resource_group_name=self.resource_group_name,
                                                                                    server_name=self.server_name,
                                                                                    database_name=self.database_name,
                                                                                    filter=self.filter)
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
    AzureRMSensitivityLabelInfo()


if __name__ == '__main__':
    main()
