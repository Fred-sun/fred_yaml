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
module: azure_rm_topic
version_added: '2.9'
short_description: Manage Azure Topic instance.
description:
  - 'Create, update and delete instance of Azure Topic.'
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
  default_message_time_to_live:
    description:
      - >-
        ISO 8601 Default message timespan to live value. This is the duration
        after which the message expires, starting from when the message is sent
        to Service Bus. This is the default value used when TimeToLive is not
        set on a message itself.
    type: duration
  max_size_in_megabytes:
    description:
      - >-
        Maximum size of the topic in megabytes, which is the size of the memory
        allocated for the topic. Default is 1024.
    type: integer
  requires_duplicate_detection:
    description:
      - Value indicating if this topic requires duplicate detection.
    type: bool
  duplicate_detection_history_time_window:
    description:
      - >-
        ISO8601 timespan structure that defines the duration of the duplicate
        detection history. The default value is 10 minutes.
    type: duration
  enable_batched_operations:
    description:
      - Value that indicates whether server-side batched operations are enabled.
    type: bool
  status:
    description:
      - Enumerates the possible values for the status of a messaging entity.
    type: sealed-choice
  support_ordering:
    description:
      - Value that indicates whether the topic supports ordering.
    type: bool
  auto_delete_on_idle:
    description:
      - >-
        ISO 8601 timespan idle interval after which the topic is automatically
        deleted. The minimum duration is 5 minutes.
    type: duration
  enable_partitioning:
    description:
      - >-
        Value that indicates whether the topic to be partitioned across multiple
        message brokers is enabled.
    type: bool
  enable_express:
    description:
      - >-
        Value that indicates whether Express Entities are enabled. An express
        topic holds a message in memory temporarily before writing it to
        persistent storage.
    type: bool
  state:
    description:
      - Assert the state of the Topic.
      - Use C(present) to create or update an Topic and C(absent) to delete it.
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
    - name: TopicCreate
      azure_rm_topic: 
        namespace_name: sdk-Namespace-1617
        resource_group_name: ArunMonocle
        topic_name: sdk-Topics-5488
        properties:
          enable_express: true
        

    - name: TopicDelete
      azure_rm_topic: 
        namespace_name: sdk-Namespace-1617
        resource_group_name: ArunMonocle
        topic_name: sdk-Topics-5488
        

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
    - 'Last time the message was sent, or a request was received, for this topic.'
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
      after which the message expires, starting from when the message is sent to
      Service Bus. This is the default value used when TimeToLive is not set on
      a message itself.
  returned: always
  type: duration
  sample: null
max_size_in_megabytes:
  description:
    - >-
      Maximum size of the topic in megabytes, which is the size of the memory
      allocated for the topic. Default is 1024.
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
    - Value that indicates whether server-side batched operations are enabled.
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
      Value that indicates whether the topic to be partitioned across multiple
      message brokers is enabled.
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


class AzureRMTopic(AzureRMModuleBaseExt):
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
            default_message_time_to_live=dict(
                type='duration',
                disposition='/default_message_time_to_live'
            ),
            max_size_in_megabytes=dict(
                type='integer',
                disposition='/max_size_in_megabytes'
            ),
            requires_duplicate_detection=dict(
                type='bool',
                disposition='/requires_duplicate_detection'
            ),
            duplicate_detection_history_time_window=dict(
                type='duration',
                disposition='/duplicate_detection_history_time_window'
            ),
            enable_batched_operations=dict(
                type='bool',
                disposition='/enable_batched_operations'
            ),
            status=dict(
                type='sealed-choice',
                disposition='/status'
            ),
            support_ordering=dict(
                type='bool',
                disposition='/support_ordering'
            ),
            auto_delete_on_idle=dict(
                type='duration',
                disposition='/auto_delete_on_idle'
            ),
            enable_partitioning=dict(
                type='bool',
                disposition='/enable_partitioning'
            ),
            enable_express=dict(
                type='bool',
                disposition='/enable_express'
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTopic, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.topics.create_or_update(resource_group_name=self.resource_group_name,
                                                                namespace_name=self.namespace_name,
                                                                topic_name=self.topic_name,
                                                                parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Topic instance.')
            self.fail('Error creating the Topic instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.topics.delete(resource_group_name=self.resource_group_name,
                                                      namespace_name=self.namespace_name,
                                                      topic_name=self.topic_name)
        except CloudError as e:
            self.log('Error attempting to delete the Topic instance.')
            self.fail('Error deleting the Topic instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.topics.get(resource_group_name=self.resource_group_name,
                                                   namespace_name=self.namespace_name,
                                                   topic_name=self.topic_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTopic()


if __name__ == '__main__':
    main()
