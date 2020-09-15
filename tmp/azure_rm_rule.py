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
module: azure_rm_rule
version_added: '2.9'
short_description: Manage Azure Rule instance.
description:
  - 'Create, update and delete instance of Azure Rule.'
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
  topic_name:
    description:
      - The topic name.
    required: true
    type: str
  subscription_name:
    description:
      - The subscription name.
    required: true
    type: str
  rule_name:
    description:
      - The rule name.
    required: true
    type: str
  action:
    description:
      - >-
        Represents the filter actions which are allowed for the transformation
        of a message that have been matched by a filter expression.
    type: dict
    suboptions:
      sqlexpression:
        description:
          - SQL expression. e.g. MyProperty='ABC'
        type: str
      compatibility_level:
        description:
          - >-
            This property is reserved for future use. An integer value showing
            the compatibility level, currently hard-coded to 20.
        type: integer
      requires_preprocessing:
        description:
          - Value that indicates whether the rule action requires preprocessing.
        type: bool
  filter_type:
    description:
      - Filter type that is evaluated against a BrokeredMessage.
    type: sealed-choice
  sqlfilter:
    description:
      - Properties of sqlFilter
    type: dict
    suboptions:
      sqlexpression:
        description:
          - The SQL expression. e.g. MyProperty='ABC'
        type: str
      compatibility_level:
        description:
          - >-
            This property is reserved for future use. An integer value showing
            the compatibility level, currently hard-coded to 20.
        type: integer
      requires_preprocessing:
        description:
          - Value that indicates whether the rule action requires preprocessing.
        type: bool
  properties:
    description:
      - dictionary object for custom filters
    type: dictionary
  correlation_id:
    description:
      - Identifier of the correlation.
    type: str
  message_id:
    description:
      - Identifier of the message.
    type: str
  to:
    description:
      - Address to send to.
    type: str
  reply_to:
    description:
      - Address of the queue to reply to.
    type: str
  label:
    description:
      - Application specific label.
    type: str
  session_id:
    description:
      - Session identifier.
    type: str
  reply_to_session_id:
    description:
      - Session identifier to reply to.
    type: str
  content_type:
    description:
      - Content type of the message.
    type: str
  requires_preprocessing:
    description:
      - Value that indicates whether the rule action requires preprocessing.
    type: bool
  state:
    description:
      - Assert the state of the Rule.
      - Use C(present) to create or update an Rule and C(absent) to delete it.
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
    - name: RulesCreateCorrelationFilter
      azure_rm_rule: 
        namespace_name: sdk-Namespace-1319
        resource_group_name: resourceGroupName
        rule_name: sdk-Rules-6571
        subscription_name: sdk-Subscriptions-8691
        topic_name: sdk-Topics-2081
        properties:
          correlation_filter:
            properties:
              topic_hint: Crop
          filter_type: CorrelationFilter
        

    - name: RulesCreateOrUpdate
      azure_rm_rule: 
        namespace_name: sdk-Namespace-1319
        resource_group_name: resourceGroupName
        rule_name: sdk-Rules-6571
        subscription_name: sdk-Subscriptions-8691
        topic_name: sdk-Topics-2081
        

    - name: RulesCreateSqlFilter
      azure_rm_rule: 
        namespace_name: sdk-Namespace-1319
        resource_group_name: resourceGroupName
        rule_name: sdk-Rules-6571
        subscription_name: sdk-Subscriptions-8691
        topic_name: sdk-Topics-2081
        properties:
          filter_type: SqlFilter
          sql_filter:
            sql_expression: myproperty=test
        

    - name: RulesDelete
      azure_rm_rule: 
        namespace_name: sdk-Namespace-1319
        resource_group_name: ArunMonocle
        rule_name: sdk-Rules-6571
        subscription_name: sdk-Subscriptions-8691
        topic_name: sdk-Topics-2081
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
action:
  description:
    - >-
      Represents the filter actions which are allowed for the transformation of
      a message that have been matched by a filter expression.
  returned: always
  type: dict
  sample: null
  contains:
    sqlexpression:
      description:
        - SQL expression. e.g. MyProperty='ABC'
      returned: always
      type: str
      sample: null
    compatibility_level:
      description:
        - >-
          This property is reserved for future use. An integer value showing the
          compatibility level, currently hard-coded to 20.
      returned: always
      type: integer
      sample: null
    requires_preprocessing:
      description:
        - Value that indicates whether the rule action requires preprocessing.
      returned: always
      type: bool
      sample: null
filter_type:
  description:
    - Filter type that is evaluated against a BrokeredMessage.
  returned: always
  type: sealed-choice
  sample: null
sqlfilter:
  description:
    - Properties of sqlFilter
  returned: always
  type: dict
  sample: null
  contains:
    sqlexpression:
      description:
        - The SQL expression. e.g. MyProperty='ABC'
      returned: always
      type: str
      sample: null
    compatibility_level:
      description:
        - >-
          This property is reserved for future use. An integer value showing the
          compatibility level, currently hard-coded to 20.
      returned: always
      type: integer
      sample: null
    requires_preprocessing:
      description:
        - Value that indicates whether the rule action requires preprocessing.
      returned: always
      type: bool
      sample: null
properties:
  description:
    - dictionary object for custom filters
  returned: always
  type: dictionary
  sample: null
correlation_id:
  description:
    - Identifier of the correlation.
  returned: always
  type: str
  sample: null
message_id:
  description:
    - Identifier of the message.
  returned: always
  type: str
  sample: null
to:
  description:
    - Address to send to.
  returned: always
  type: str
  sample: null
reply_to:
  description:
    - Address of the queue to reply to.
  returned: always
  type: str
  sample: null
label:
  description:
    - Application specific label.
  returned: always
  type: str
  sample: null
session_id:
  description:
    - Session identifier.
  returned: always
  type: str
  sample: null
reply_to_session_id:
  description:
    - Session identifier to reply to.
  returned: always
  type: str
  sample: null
content_type:
  description:
    - Content type of the message.
  returned: always
  type: str
  sample: null
requires_preprocessing:
  description:
    - Value that indicates whether the rule action requires preprocessing.
  returned: always
  type: bool
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRule(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            ),
            topic_name=dict(
                type='str',
                required=True
            ),
            subscription_name=dict(
                type='str',
                required=True
            ),
            rule_name=dict(
                type='str',
                required=True
            ),
            action=dict(
                type='dict',
                disposition='/action',
                options=dict(
                    sqlexpression=dict(
                        type='str',
                        disposition='sqlexpression'
                    ),
                    compatibility_level=dict(
                        type='integer',
                        disposition='compatibility_level'
                    ),
                    requires_preprocessing=dict(
                        type='bool',
                        disposition='requires_preprocessing'
                    )
                )
            ),
            filter_type=dict(
                type='sealed-choice',
                disposition='/filter_type'
            ),
            sqlfilter=dict(
                type='dict',
                disposition='/sqlfilter',
                options=dict(
                    sqlexpression=dict(
                        type='str',
                        disposition='sqlexpression'
                    ),
                    compatibility_level=dict(
                        type='integer',
                        disposition='compatibility_level'
                    ),
                    requires_preprocessing=dict(
                        type='bool',
                        disposition='requires_preprocessing'
                    )
                )
            ),
            properties=dict(
                type='dictionary',
                disposition='/properties'
            ),
            correlation_id=dict(
                type='str',
                disposition='/correlation_id'
            ),
            message_id=dict(
                type='str',
                disposition='/message_id'
            ),
            to=dict(
                type='str',
                disposition='/to'
            ),
            reply_to=dict(
                type='str',
                disposition='/reply_to'
            ),
            label=dict(
                type='str',
                disposition='/label'
            ),
            session_id=dict(
                type='str',
                disposition='/session_id'
            ),
            reply_to_session_id=dict(
                type='str',
                disposition='/reply_to_session_id'
            ),
            content_type=dict(
                type='str',
                disposition='/content_type'
            ),
            requires_preprocessing=dict(
                type='bool',
                disposition='/requires_preprocessing'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.topic_name = None
        self.subscription_name = None
        self.rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

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
            response = self.mgmt_client.rules.create_or_update(resource_group_name=self.resource_group_name,
                                                               namespace_name=self.namespace_name,
                                                               topic_name=self.topic_name,
                                                               subscription_name=self.subscription_name,
                                                               rule_name=self.rule_name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Rule instance.')
            self.fail('Error creating the Rule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.rules.delete(resource_group_name=self.resource_group_name,
                                                     namespace_name=self.namespace_name,
                                                     topic_name=self.topic_name,
                                                     subscription_name=self.subscription_name,
                                                     rule_name=self.rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the Rule instance.')
            self.fail('Error deleting the Rule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.rules.get(resource_group_name=self.resource_group_name,
                                                  namespace_name=self.namespace_name,
                                                  topic_name=self.topic_name,
                                                  subscription_name=self.subscription_name,
                                                  rule_name=self.rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRule()


if __name__ == '__main__':
    main()
