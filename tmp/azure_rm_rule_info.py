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
module: azure_rm_rule_info
version_added: '2.9'
short_description: Get Rule info.
description:
  - Get info of Rule.
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
  skip:
    description:
      - >-
        Skip is only used if a previous operation returned a partial result. If
        a previous response contains a nextLink element, the value of the
        nextLink element will include a skip parameter that specifies a starting
        point to use for subsequent calls.
    type: integer
  top:
    description:
      - >-
        May be used to limit the number of results to the most recent N
        usageDetails.
    type: integer
  rule_name:
    description:
      - The rule name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RulesListBySubscriptions
      azure_rm_rule_info: 
        namespace_name: sdk-Namespace-1319
        resource_group_name: ArunMonocle
        subscription_name: sdk-Subscriptions-8691
        topic_name: sdk-Topics-2081
        

    - name: RulesGet
      azure_rm_rule_info: 
        namespace_name: sdk-Namespace-1319
        resource_group_name: ArunMonocle
        rule_name: sdk-Rules-6571
        subscription_name: sdk-Subscriptions-8691
        topic_name: sdk-Topics-2081
        

'''

RETURN = '''
rules:
  description: >-
    A list of dict results where the key is the name of the Rule and the values
    are the facts for that Rule.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Result of the List Rules operation.
      returned: always
      type: list
      sample: null
      contains:
        action:
          description:
            - >-
              Represents the filter actions which are allowed for the
              transformation of a message that have been matched by a filter
              expression.
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
                  This property is reserved for future use. An integer value
                  showing the compatibility level, currently hard-coded to 20.
              returned: always
              type: integer
              sample: null
            requires_preprocessing:
              description:
                - >-
                  Value that indicates whether the rule action requires
                  preprocessing.
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
                  This property is reserved for future use. An integer value
                  showing the compatibility level, currently hard-coded to 20.
              returned: always
              type: integer
              sample: null
            requires_preprocessing:
              description:
                - >-
                  Value that indicates whether the rule action requires
                  preprocessing.
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
            - >-
              Value that indicates whether the rule action requires
              preprocessing.
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of rules
      returned: always
      type: str
      sample: null
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
          Represents the filter actions which are allowed for the transformation
          of a message that have been matched by a filter expression.
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
              This property is reserved for future use. An integer value showing
              the compatibility level, currently hard-coded to 20.
          returned: always
          type: integer
          sample: null
        requires_preprocessing:
          description:
            - >-
              Value that indicates whether the rule action requires
              preprocessing.
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
              This property is reserved for future use. An integer value showing
              the compatibility level, currently hard-coded to 20.
          returned: always
          type: integer
          sample: null
        requires_preprocessing:
          description:
            - >-
              Value that indicates whether the rule action requires
              preprocessing.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRuleInfo(AzureRMModuleBase):
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
            skip=dict(
                type='integer'
            ),
            top=dict(
                type='integer'
            ),
            rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.topic_name = None
        self.subscription_name = None
        self.skip = None
        self.top = None
        self.rule_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.topic_name is not None and
            self.subscription_name is not None and
            self.rule_name is not None):
            self.results['rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.topic_name is not None and
              self.subscription_name is not None):
            self.results['rules'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.rules.get(resource_group_name=self.resource_group_name,
                                                  namespace_name=self.namespace_name,
                                                  topic_name=self.topic_name,
                                                  subscription_name=self.subscription_name,
                                                  rule_name=self.rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.rules.list_by_subscription(resource_group_name=self.resource_group_name,
                                                                   namespace_name=self.namespace_name,
                                                                   topic_name=self.topic_name,
                                                                   subscription_name=self.subscription_name,
                                                                   skip=self.skip,
                                                                   top=self.top)
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
    AzureRMRuleInfo()


if __name__ == '__main__':
    main()
