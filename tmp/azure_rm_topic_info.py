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
module: azure_rm_topic_info
version_added: '2.9'
short_description: Get Topic info.
description:
  - Get info of Topic.
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
    type: str
  authorization_rule_name:
    description:
      - The authorization rule name.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: TopicAuthorizationRuleListAll
      azure_rm_topic_info: 
        namespace_name: sdk-Namespace-6261
        resource_group_name: ArunMonocle
        topic_name: sdk-Topics-1984
        

    - name: TopicAuthorizationRuleGet
      azure_rm_topic_info: 
        authorization_rule_name: sdk-AuthRules-4310
        namespace_name: sdk-Namespace-6261
        resource_group_name: ArunMonocle
        topic_name: sdk-Topics-1984
        

    - name: TopicGet
      azure_rm_topic_info: 
        namespace_name: sdk-Namespace-1617
        resource_group_name: Default-ServiceBus-WestUS
        

'''

RETURN = '''
topics:
  description: >-
    A list of dict results where the key is the name of the Topic and the values
    are the facts for that Topic.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          Result of the List Authorization Rules operation.
          Result of the List Topics operation.
      returned: always
      type: list
      sample: null
      contains:
        rights:
          description:
            - The rights associated with the rule.
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of Authorization Rules.

          Link to the next set of results. Not empty if Value contains
          incomplete list of topics.
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
    rights:
      description:
        - The rights associated with the rule.
      returned: always
      type: list
      sample: null
    size_in_bytes:
      description:
        - 'Size of the topic, in bytes.'
      returned: always
      type: integer
      sample: null
    created_at:
      description:
        - Exact time the message was created.
      returned: always
      type: str
      sample: null
    updated_at:
      description:
        - The exact time the message was updated.
      returned: always
      type: str
      sample: null
    accessed_at:
      description:
        - >-
          Last time the message was sent, or a request was received, for this
          topic.
      returned: always
      type: str
      sample: null
    subscription_count:
      description:
        - Number of subscriptions.
      returned: always
      type: integer
      sample: null
    count_details:
      description:
        - Message count details
      returned: always
      type: dict
      sample: null
      contains:
        active_message_count:
          description:
            - 'Number of active messages in the queue, topic, or subscription.'
          returned: always
          type: integer
          sample: null
        dead_letter_message_count:
          description:
            - Number of messages that are dead lettered.
          returned: always
          type: integer
          sample: null
        scheduled_message_count:
          description:
            - Number of scheduled messages.
          returned: always
          type: integer
          sample: null
        transfer_message_count:
          description:
            - >-
              Number of messages transferred to another queue, topic, or
              subscription.
          returned: always
          type: integer
          sample: null
        transfer_dead_letter_message_count:
          description:
            - Number of messages transferred into dead letters.
          returned: always
          type: integer
          sample: null
    default_message_time_to_live:
      description:
        - >-
          ISO 8601 Default message timespan to live value. This is the duration
          after which the message expires, starting from when the message is
          sent to Service Bus. This is the default value used when TimeToLive is
          not set on a message itself.
      returned: always
      type: duration
      sample: null
    max_size_in_megabytes:
      description:
        - >-
          Maximum size of the topic in megabytes, which is the size of the
          memory allocated for the topic. Default is 1024.
      returned: always
      type: integer
      sample: null
    requires_duplicate_detection:
      description:
        - Value indicating if this topic requires duplicate detection.
      returned: always
      type: bool
      sample: null
    duplicate_detection_history_time_window:
      description:
        - >-
          ISO8601 timespan structure that defines the duration of the duplicate
          detection history. The default value is 10 minutes.
      returned: always
      type: duration
      sample: null
    enable_batched_operations:
      description:
        - >-
          Value that indicates whether server-side batched operations are
          enabled.
      returned: always
      type: bool
      sample: null
    status:
      description:
        - Enumerates the possible values for the status of a messaging entity.
      returned: always
      type: sealed-choice
      sample: null
    support_ordering:
      description:
        - Value that indicates whether the topic supports ordering.
      returned: always
      type: bool
      sample: null
    auto_delete_on_idle:
      description:
        - >-
          ISO 8601 timespan idle interval after which the topic is automatically
          deleted. The minimum duration is 5 minutes.
      returned: always
      type: duration
      sample: null
    enable_partitioning:
      description:
        - >-
          Value that indicates whether the topic to be partitioned across
          multiple message brokers is enabled.
      returned: always
      type: bool
      sample: null
    enable_express:
      description:
        - >-
          Value that indicates whether Express Entities are enabled. An express
          topic holds a message in memory temporarily before writing it to
          persistent storage.
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


class AzureRMTopicInfo(AzureRMModuleBase):
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
                type='str'
            ),
            authorization_rule_name=dict(
                type='str'
            ),
            skip=dict(
                type='integer'
            ),
            top=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.topic_name = None
        self.authorization_rule_name = None
        self.skip = None
        self.top = None

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
        super(AzureRMTopicInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.topic_name is not None and
            self.authorization_rule_name is not None):
            self.results['topics'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.topic_name is not None):
            self.results['topics'] = self.format_item(self.listauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.topic_name is not None):
            self.results['topics'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['topics'] = self.format_item(self.listbynamespace())
        return self.results

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.topics.get_authorization_rule(resource_group_name=self.resource_group_name,
                                                                      namespace_name=self.namespace_name,
                                                                      topic_name=self.topic_name,
                                                                      authorization_rule_name=self.authorization_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.topics.list_authorization_rule(resource_group_name=self.resource_group_name,
                                                                       namespace_name=self.namespace_name,
                                                                       topic_name=self.topic_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.topics.get(resource_group_name=self.resource_group_name,
                                                   namespace_name=self.namespace_name,
                                                   topic_name=self.topic_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbynamespace(self):
        response = None

        try:
            response = self.mgmt_client.topics.list_by_namespace(resource_group_name=self.resource_group_name,
                                                                 namespace_name=self.namespace_name,
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
    AzureRMTopicInfo()


if __name__ == '__main__':
    main()
