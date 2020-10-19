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
module: azure_rm_eventsubscription
version_added: '2.9'
short_description: Manage Azure EventSubscription instance.
description:
  - 'Create, update and delete instance of Azure EventSubscription.'
options:
  scope:
    description:
      - >-
        The scope of the event subscription. The scope can be a subscription, or
        a resource group, or a top level resource belonging to a resource
        provider namespace, or an EventGrid topic. For example, use
        '/subscriptions/{subscriptionId}/' for a subscription,
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for
        a resource group, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}'
        for a resource, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}'
        for an EventGrid topic.
      - >-
        The identifier of the resource to which the event subscription needs to
        be created or updated. The scope can be a subscription, or a resource
        group, or a top level resource belonging to a resource provider
        namespace, or an EventGrid topic. For example, use
        '/subscriptions/{subscriptionId}/' for a subscription,
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for
        a resource group, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}'
        for a resource, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}'
        for an EventGrid topic.
      - >-
        The scope of existing event subscription. The scope can be a
        subscription, or a resource group, or a top level resource belonging to
        a resource provider namespace, or an EventGrid topic. For example, use
        '/subscriptions/{subscriptionId}/' for a subscription,
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for
        a resource group, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}'
        for a resource, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}'
        for an EventGrid topic.
    required: true
    type: str
  event_subscription_name:
    description:
      - Name of the event subscription.
      - >-
        Name of the event subscription. Event subscription names must be between
        3 and 64 characters in length and should use alphanumeric letters only.
      - Name of the event subscription to be updated.
    required: true
    type: str
  destination:
    description:
      - >-
        Information about the destination where events have to be delivered for
        the event subscription.
    type: dict
    suboptions:
      endpoint_type:
        description:
          - Type of the endpoint for the event subscription destination.
        required: true
        type: str
        choices:
          - WebHook
          - EventHub
          - StorageQueue
          - HybridConnection
          - ServiceBusQueue
          - ServiceBusTopic
          - AzureFunction
  labels:
    description:
      - List of user defined labels.
    type: list
  expiration_time_utc:
    description:
      - Expiration time of the event subscription.
      - Information about the expiration time for the event subscription.
    type: str
  event_delivery_schema:
    description:
      - The event delivery schema for the event subscription.
    type: str
    choices:
      - EventGridSchema
      - CustomInputSchema
      - CloudEventSchemaV1_0
  retry_policy:
    description:
      - >-
        The retry policy for events. This can be used to configure maximum
        number of delivery attempts and time to live for events.
    type: dict
    suboptions:
      max_delivery_attempts:
        description:
          - Maximum number of delivery retry attempts for events.
        type: integer
      event_time_to_live_in_minutes:
        description:
          - Time To Live (in minutes) for events.
        type: integer
  dead_letter_destination:
    description:
      - The DeadLetter destination of the event subscription.
    type: dict
    suboptions:
      endpoint_type:
        description:
          - Type of the endpoint for the dead letter destination
        required: true
        type: str
        choices:
          - StorageBlob
  subject_begins_with:
    description:
      - "An optional string to filter events for an event subscription based on a resource path prefix.\r"
      - "The format of this depends on the publisher of the events.\r"
      - Wildcard characters are not supported in this path.
    type: str
  subject_ends_with:
    description:
      - "An optional string to filter events for an event subscription based on a resource path suffix.\r"
      - Wildcard characters are not supported in this path.
    type: str
  included_event_types:
    description:
      - >-
        A list of applicable event types that need to be part of the event
        subscription. If it is desired to subscribe to all default event types,
        set the IncludedEventTypes to null.
    type: list
  is_subject_case_sensitive:
    description:
      - "Specifies if the SubjectBeginsWith and SubjectEndsWith properties of the filter\r"
      - should be compared in a case sensitive manner.
    type: bool
  advanced_filters:
    description:
      - >-
        An array of advanced filters that are used for filtering event
        subscriptions.
    type: list
    suboptions:
      operator_type:
        description:
          - >-
            The operator type used for filtering, e.g., NumberIn,
            StringContains, BoolEquals and others.
        required: true
        type: str
        choices:
          - NumberIn
          - NumberNotIn
          - NumberLessThan
          - NumberGreaterThan
          - NumberLessThanOrEquals
          - NumberGreaterThanOrEquals
          - BoolEquals
          - StringIn
          - StringNotIn
          - StringBeginsWith
          - StringEndsWith
          - StringContains
      key:
        description:
          - The field/property in the event based on which you want to filter.
        type: str
  state:
    description:
      - Assert the state of the EventSubscription.
      - >-
        Use C(present) to create or update an EventSubscription and C(absent) to
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
    - name: EventSubscriptions_CreateOrUpdateForCustomTopic_EventHubDestination
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
        

    - name: EventSubscriptions_CreateOrUpdateForCustomTopic_HybridConnectionDestination
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
        

    - name: EventSubscriptions_CreateOrUpdateForCustomTopic_StorageQueueDestination
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
        

    - name: EventSubscriptions_CreateOrUpdateForCustomTopic_WebhookDestination
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
        

    - name: EventSubscriptions_CreateOrUpdateForResource
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription10
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
        

    - name: EventSubscriptions_CreateOrUpdateForResourceGroup
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription2
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
        

    - name: EventSubscriptions_CreateOrUpdateForSubscription
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription3
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
        

    - name: EventSubscriptions_DeleteForCustomTopic
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
        

    - name: EventSubscriptions_DeleteForResource
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription10
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
        

    - name: EventSubscriptions_DeleteForResourceGroup
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription2
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
        

    - name: EventSubscriptions_DeleteForSubscription
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription3
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
        

    - name: EventSubscriptions_UpdateForCustomTopic
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic2
        

    - name: EventSubscriptions_UpdateForResource
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
        

    - name: EventSubscriptions_UpdateForResourceGroup
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription2
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
        

    - name: EventSubscriptions_UpdateForSubscription
      azure_rm_eventsubscription: 
        event_subscription_name: examplesubscription3
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
        

'''

RETURN = '''
id:
  description:
    - Fully qualified identifier of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of the resource.
  returned: always
  type: str
  sample: null
topic:
  description:
    - Name of the topic of the event subscription.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state of the event subscription.
  returned: always
  type: str
  sample: null
destination:
  description:
    - >-
      Information about the destination where events have to be delivered for
      the event subscription.
  returned: always
  type: dict
  sample: null
  contains:
    endpoint_type:
      description:
        - Type of the endpoint for the event subscription destination.
      returned: always
      type: str
      sample: null
labels:
  description:
    - List of user defined labels.
  returned: always
  type: list
  sample: null
expiration_time_utc:
  description:
    - Expiration time of the event subscription.
  returned: always
  type: str
  sample: null
event_delivery_schema:
  description:
    - The event delivery schema for the event subscription.
  returned: always
  type: str
  sample: null
retry_policy:
  description:
    - >-
      The retry policy for events. This can be used to configure maximum number
      of delivery attempts and time to live for events.
  returned: always
  type: dict
  sample: null
  contains:
    max_delivery_attempts:
      description:
        - Maximum number of delivery retry attempts for events.
      returned: always
      type: integer
      sample: null
    event_time_to_live_in_minutes:
      description:
        - Time To Live (in minutes) for events.
      returned: always
      type: integer
      sample: null
dead_letter_destination:
  description:
    - The DeadLetter destination of the event subscription.
  returned: always
  type: dict
  sample: null
  contains:
    endpoint_type:
      description:
        - Type of the endpoint for the dead letter destination
      returned: always
      type: str
      sample: null
subject_begins_with:
  description:
    - "An optional string to filter events for an event subscription based on a resource path prefix.\r\nThe format of this depends on the publisher of the events.\r\nWildcard characters are not supported in this path."
  returned: always
  type: str
  sample: null
subject_ends_with:
  description:
    - "An optional string to filter events for an event subscription based on a resource path suffix.\r\nWildcard characters are not supported in this path."
  returned: always
  type: str
  sample: null
included_event_types:
  description:
    - >-
      A list of applicable event types that need to be part of the event
      subscription. If it is desired to subscribe to all default event types,
      set the IncludedEventTypes to null.
  returned: always
  type: list
  sample: null
is_subject_case_sensitive:
  description:
    - "Specifies if the SubjectBeginsWith and SubjectEndsWith properties of the filter\r\nshould be compared in a case sensitive manner."
  returned: always
  type: bool
  sample: null
advanced_filters:
  description:
    - >-
      An array of advanced filters that are used for filtering event
      subscriptions.
  returned: always
  type: list
  sample: null
  contains:
    operator_type:
      description:
        - >-
          The operator type used for filtering, e.g., NumberIn, StringContains,
          BoolEquals and others.
      returned: always
      type: str
      sample: null
    key:
      description:
        - The field/property in the event based on which you want to filter.
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
    from azure.mgmt.event import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMEventSubscription(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            event_subscription_name=dict(
                type='str',
                required=True
            ),
            destination=dict(
                type='dict',
                disposition='/destination',
                options=dict(
                    endpoint_type=dict(
                        type='str',
                        disposition='endpoint_type',
                        choices=['WebHook',
                                 'EventHub',
                                 'StorageQueue',
                                 'HybridConnection',
                                 'ServiceBusQueue',
                                 'ServiceBusTopic',
                                 'AzureFunction'],
                        required=True
                    )
                )
            ),
            labels=dict(
                type='list',
                disposition='/labels',
                elements='str'
            ),
            expiration_time_utc=dict(
                type='str',
                disposition='/expiration_time_utc'
            ),
            event_delivery_schema=dict(
                type='str',
                disposition='/event_delivery_schema',
                choices=['EventGridSchema',
                         'CustomInputSchema',
                         'CloudEventSchemaV1_0']
            ),
            retry_policy=dict(
                type='dict',
                disposition='/retry_policy',
                options=dict(
                    max_delivery_attempts=dict(
                        type='integer',
                        disposition='max_delivery_attempts'
                    ),
                    event_time_to_live_in_minutes=dict(
                        type='integer',
                        disposition='event_time_to_live_in_minutes'
                    )
                )
            ),
            dead_letter_destination=dict(
                type='dict',
                disposition='/dead_letter_destination',
                options=dict(
                    endpoint_type=dict(
                        type='str',
                        disposition='endpoint_type',
                        choices=['StorageBlob'],
                        required=True
                    )
                )
            ),
            subject_begins_with=dict(
                type='str',
                disposition='/subject_begins_with'
            ),
            subject_ends_with=dict(
                type='str',
                disposition='/subject_ends_with'
            ),
            included_event_types=dict(
                type='list',
                disposition='/included_event_types',
                elements='str'
            ),
            is_subject_case_sensitive=dict(
                type='bool',
                disposition='/is_subject_case_sensitive'
            ),
            advanced_filters=dict(
                type='list',
                disposition='/advanced_filters',
                elements='dict',
                options=dict(
                    operator_type=dict(
                        type='str',
                        disposition='operator_type',
                        choices=['NumberIn',
                                 'NumberNotIn',
                                 'NumberLessThan',
                                 'NumberGreaterThan',
                                 'NumberLessThanOrEquals',
                                 'NumberGreaterThanOrEquals',
                                 'BoolEquals',
                                 'StringIn',
                                 'StringNotIn',
                                 'StringBeginsWith',
                                 'StringEndsWith',
                                 'StringContains'],
                        required=True
                    ),
                    key=dict(
                        type='str',
                        disposition='key'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.event_subscription_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEventSubscription, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.event_subscriptions.create_or_update(scope=self.scope,
                                                                             event_subscription_name=self.event_subscription_name,
                                                                             event_subscription_info=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the EventSubscription instance.')
            self.fail('Error creating the EventSubscription instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.event_subscriptions.delete(scope=self.scope,
                                                                   event_subscription_name=self.event_subscription_name)
        except CloudError as e:
            self.log('Error attempting to delete the EventSubscription instance.')
            self.fail('Error deleting the EventSubscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.event_subscriptions.get(scope=self.scope,
                                                                event_subscription_name=self.event_subscription_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEventSubscription()


if __name__ == '__main__':
    main()
