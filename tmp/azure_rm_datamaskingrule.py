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
module: azure_rm_datamaskingrule
version_added: '2.9'
short_description: Manage Azure DataMaskingRule instance.
description:
  - 'Create, update and delete instance of Azure DataMaskingRule.'
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
  data_masking_rule_name:
    description:
      - The name of the data masking rule.
    required: true
    type: str
  alias_name:
    description:
      - The alias name. This is a legacy parameter and is no longer used.
    required: true
    type: str
  rule_state:
    description:
      - >-
        The rule state. Used to delete a rule. To delete an existing rule,
        specify the schemaName, tableName, columnName, maskingFunction, and
        specify ruleState as disabled. However, if the rule doesn't already
        exist, the rule will be created with ruleState set to enabled,
        regardless of the provided value of ruleState.
    required: true
    type: sealed-choice
  schema_name:
    description:
      - The schema name on which the data masking rule is applied.
    required: true
    type: str
  table_name:
    description:
      - The table name on which the data masking rule is applied.
    required: true
    type: str
  column_name:
    description:
      - The column name on which the data masking rule is applied.
    required: true
    type: str
  masking_function:
    description:
      - The masking function that is used for the data masking rule.
    required: true
    type: sealed-choice
  number_from:
    description:
      - >-
        The numberFrom property of the masking rule. Required if maskingFunction
        is set to Number, otherwise this parameter will be ignored.
    required: true
    type: str
  number_to:
    description:
      - >-
        The numberTo property of the data masking rule. Required if
        maskingFunction is set to Number, otherwise this parameter will be
        ignored.
    required: true
    type: str
  prefix_size:
    description:
      - >-
        If maskingFunction is set to Text, the number of characters to show
        unmasked in the beginning of the string. Otherwise, this parameter will
        be ignored.
    required: true
    type: str
  suffix_size:
    description:
      - >-
        If maskingFunction is set to Text, the number of characters to show
        unmasked at the end of the string. Otherwise, this parameter will be
        ignored.
    required: true
    type: str
  replacement_string:
    description:
      - >-
        If maskingFunction is set to Text, the character to use for masking the
        unexposed part of the string. Otherwise, this parameter will be ignored.
    required: true
    type: str
  state:
    description:
      - Assert the state of the DataMaskingRule.
      - >-
        Use C(present) to create or update an DataMaskingRule and C(absent) to
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
    - name: Create/Update data masking rule for default max
      azure_rm_datamaskingrule: 
        data_masking_rule_name: rule1
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        properties:
          alias_name: nickname
          column_name: test1
          masking_function: Default
          rule_state: Enabled
          schema_name: dbo
          table_name: Table_1
        

    - name: Create/Update data masking rule for default min
      azure_rm_datamaskingrule: 
        data_masking_rule_name: rule1
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        properties:
          column_name: test1
          masking_function: Default
          schema_name: dbo
          table_name: Table_1
        

    - name: Create/Update data masking rule for numbers
      azure_rm_datamaskingrule: 
        data_masking_rule_name: rule1
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        properties:
          column_name: test1
          masking_function: Number
          number_from: '0'
          number_to: '2'
          schema_name: dbo
          table_name: Table_1
        

    - name: Create/Update data masking rule for text
      azure_rm_datamaskingrule: 
        data_masking_rule_name: rule1
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        properties:
          column_name: test1
          masking_function: Text
          prefix_size: '1'
          replacement_string: asdf
          schema_name: dbo
          suffix_size: '0'
          table_name: Table_1
        

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
      The rule state. Used to delete a rule. To delete an existing rule, specify
      the schemaName, tableName, columnName, maskingFunction, and specify
      ruleState as disabled. However, if the rule doesn't already exist, the
      rule will be created with ruleState set to enabled, regardless of the
      provided value of ruleState.
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
      The numberFrom property of the masking rule. Required if maskingFunction
      is set to Number, otherwise this parameter will be ignored.
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
      If maskingFunction is set to Text, the number of characters to show
      unmasked in the beginning of the string. Otherwise, this parameter will be
      ignored.
  returned: always
  type: str
  sample: null
suffix_size:
  description:
    - >-
      If maskingFunction is set to Text, the number of characters to show
      unmasked at the end of the string. Otherwise, this parameter will be
      ignored.
  returned: always
  type: str
  sample: null
replacement_string:
  description:
    - >-
      If maskingFunction is set to Text, the character to use for masking the
      unexposed part of the string. Otherwise, this parameter will be ignored.
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


class AzureRMDataMaskingRule(AzureRMModuleBaseExt):
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
            ),
            data_masking_rule_name=dict(
                type='str',
                required=True
            ),
            alias_name=dict(
                type='str',
                disposition='/alias_name',
                required=True
            ),
            rule_state=dict(
                type='sealed-choice',
                disposition='/rule_state',
                required=True
            ),
            schema_name=dict(
                type='str',
                disposition='/schema_name',
                required=True
            ),
            table_name=dict(
                type='str',
                disposition='/table_name',
                required=True
            ),
            column_name=dict(
                type='str',
                disposition='/column_name',
                required=True
            ),
            masking_function=dict(
                type='sealed-choice',
                disposition='/masking_function',
                required=True
            ),
            number_from=dict(
                type='str',
                disposition='/number_from',
                required=True
            ),
            number_to=dict(
                type='str',
                disposition='/number_to',
                required=True
            ),
            prefix_size=dict(
                type='str',
                disposition='/prefix_size',
                required=True
            ),
            suffix_size=dict(
                type='str',
                disposition='/suffix_size',
                required=True
            ),
            replacement_string=dict(
                type='str',
                disposition='/replacement_string',
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
        self.database_name = None
        self.datamaskingpolicyname = None
        self.data_masking_rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataMaskingRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.data_masking_rules.create_or_update(resource_group_name=self.resource_group_name,
                                                                            server_name=self.server_name,
                                                                            database_name=self.database_name,
                                                                            datamaskingpolicyname=self.datamaskingpolicyname,
                                                                            data_masking_rule_name=self.data_masking_rule_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DataMaskingRule instance.')
            self.fail('Error creating the DataMaskingRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.data_masking_rules.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DataMaskingRule instance.')
            self.fail('Error deleting the DataMaskingRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.data_masking_rules.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDataMaskingRule()


if __name__ == '__main__':
    main()
