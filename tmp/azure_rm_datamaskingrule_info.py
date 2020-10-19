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
module: azure_rm_datamaskingrule_info
version_added: '2.9'
short_description: Get DataMaskingRule info.
description:
  - Get info of DataMaskingRule.
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
  datamaskingpolicyname:
    description:
      - The name of the database for which the data masking rule applies.
    required: true
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List data masking rules
      azure_rm_datamaskingrule_info: 
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        

'''

RETURN = '''
data_masking_rules:
  description: >-
    A list of dict results where the key is the name of the DataMaskingRule and
    the values are the facts for that DataMaskingRule.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of database data masking rules.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - The location of the data masking rule.
          returned: always
          type: str
          sample: null
        kind:
          description:
            - 'The kind of Data Masking Rule. Metadata, used for Azure portal.'
          returned: always
          type: str
          sample: null
        id_properties_id:
          description:
            - The rule Id.
          returned: always
          type: str
          sample: null
        alias_name:
          description:
            - The alias name. This is a legacy parameter and is no longer used.
          returned: always
          type: str
          sample: null
        rule_state:
          description:
            - >-
              The rule state. Used to delete a rule. To delete an existing rule,
              specify the schemaName, tableName, columnName, maskingFunction,
              and specify ruleState as disabled. However, if the rule doesn't
              already exist, the rule will be created with ruleState set to
              enabled, regardless of the provided value of ruleState.
          returned: always
          type: sealed-choice
          sample: null
        schema_name:
          description:
            - The schema name on which the data masking rule is applied.
          returned: always
          type: str
          sample: null
        table_name:
          description:
            - The table name on which the data masking rule is applied.
          returned: always
          type: str
          sample: null
        column_name:
          description:
            - The column name on which the data masking rule is applied.
          returned: always
          type: str
          sample: null
        masking_function:
          description:
            - The masking function that is used for the data masking rule.
          returned: always
          type: sealed-choice
          sample: null
        number_from:
          description:
            - >-
              The numberFrom property of the masking rule. Required if
              maskingFunction is set to Number, otherwise this parameter will be
              ignored.
          returned: always
          type: str
          sample: null
        number_to:
          description:
            - >-
              The numberTo property of the data masking rule. Required if
              maskingFunction is set to Number, otherwise this parameter will be
              ignored.
          returned: always
          type: str
          sample: null
        prefix_size:
          description:
            - >-
              If maskingFunction is set to Text, the number of characters to
              show unmasked in the beginning of the string. Otherwise, this
              parameter will be ignored.
          returned: always
          type: str
          sample: null
        suffix_size:
          description:
            - >-
              If maskingFunction is set to Text, the number of characters to
              show unmasked at the end of the string. Otherwise, this parameter
              will be ignored.
          returned: always
          type: str
          sample: null
        replacement_string:
          description:
            - >-
              If maskingFunction is set to Text, the character to use for
              masking the unexposed part of the string. Otherwise, this
              parameter will be ignored.
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


class AzureRMDataMaskingRuleInfo(AzureRMModuleBase):
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
            datamaskingpolicyname=dict(
                type='constant',
                required=True
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.datamaskingpolicyname = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDataMaskingRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.datamaskingpolicyname is not None):
            self.results['data_masking_rules'] = self.format_item(self.listbydatabase())
        return self.results

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.data_masking_rules.list_by_database(resource_group_name=self.resource_group_name,
                                                                            server_name=self.server_name,
                                                                            database_name=self.database_name,
                                                                            datamaskingpolicyname=self.datamaskingpolicyname)
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
    AzureRMDataMaskingRuleInfo()


if __name__ == '__main__':
    main()
