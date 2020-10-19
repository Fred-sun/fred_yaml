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
module: azure_rm_eventsubscription_info
version_added: '2.9'
short_description: Get EventSubscription info.
description:
  - Get info of EventSubscription.
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
    type: str
  event_subscription_name:
    description:
      - Name of the event subscription.
    type: str
  filter:
    description:
      - >-
        The query used to filter the search results using OData syntax.
        Filtering is permitted on the 'name' property only and with limited
        number of OData operations. These operations are: the 'contains'
        function as well as the following logical operations: not, and, or, eq
        (for equal), and ne (for not equal). No arithmetic operations are
        supported. The following is a valid filter example:
        $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following
        is not a valid filter example: $filter=location eq 'westus'.
    type: str
  top:
    description:
      - >-
        The number of results to return per page for the list operation. Valid
        range for top parameter is 1 to 100. If not specified, the default
        number of results to be returned is 20 items per page.
    type: integer
  topic_type_name:
    description:
      - Name of the topic type.
    type: str
  resource_group_name:
    description:
      - The name of the resource group within the user's subscription.
    type: str
  location:
    description:
      - Name of the location.
    type: str
  provider_namespace:
    description:
      - Namespace of the provider of the topic.
    type: str
  resource_type_name:
    description:
      - Name of the resource type.
    type: str
  resource_name:
    description:
      - Name of the resource.
    type: str
  domain_name:
    description:
      - Name of the top level domain.
    type: str
  topic_name:
    description:
      - Name of the domain topic.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: EventSubscriptions_GetForCustomTopic
      azure_rm_eventsubscription_info: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic2
        

    - name: EventSubscriptions_GetForResource
      azure_rm_eventsubscription_info: 
        event_subscription_name: examplesubscription1
        scope: >-
          subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
        

    - name: EventSubscriptions_GetForResourceGroup
      azure_rm_eventsubscription_info: 
        event_subscription_name: examplesubscription2
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
        

    - name: EventSubscriptions_GetForSubscription
      azure_rm_eventsubscription_info: 
        event_subscription_name: examplesubscription3
        scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
        

    - name: EventSubscriptions_ListGlobalBySubscription
      azure_rm_eventsubscription_info: 
        {}
        

    - name: EventSubscriptions_ListGlobalBySubscriptionForTopicType
      azure_rm_eventsubscription_info: 
        topic_type_name: Microsoft.Resources.Subscriptions
        

    - name: EventSubscriptions_ListGlobalByResourceGroup
      azure_rm_eventsubscription_info: 
        resource_group_name: examplerg
        

    - name: EventSubscriptions_ListGlobalByResourceGroupForTopicType
      azure_rm_eventsubscription_info: 
        resource_group_name: examplerg
        topic_type_name: Microsoft.Resources.ResourceGroups
        

    - name: EventSubscriptions_ListRegionalBySubscription
      azure_rm_eventsubscription_info: 
        location: westus2
        

    - name: EventSubscriptions_ListRegionalByResourceGroup
      azure_rm_eventsubscription_info: 
        location: westus2
        resource_group_name: examplerg
        

    - name: EventSubscriptions_ListRegionalBySubscriptionForTopicType
      azure_rm_eventsubscription_info: 
        location: westus2
        topic_type_name: Microsoft.EventHub.namespaces
        

    - name: EventSubscriptions_ListRegionalByResourceGroupForTopicType
      azure_rm_eventsubscription_info: 
        location: westus2
        resource_group_name: examplerg
        topic_type_name: Microsoft.EventHub.namespaces
        

    - name: EventSubscriptions_ListByResource
      azure_rm_eventsubscription_info: 
        provider_namespace: Microsoft.EventGrid
        resource_group_name: examplerg
        resource_name: exampletopic2
        resource_type_name: topics
        

    - name: EventSubscriptions_ListByDomainTopic
      azure_rm_eventsubscription_info: 
        domain_name: domain1
        resource_group_name: examplerg
        topic_name: topic1
        

'''

RETURN = '''
event_subscriptions:
  description: >-
    A list of dict results where the key is the name of the EventSubscription
    and the values are the facts for that EventSubscription.
  returned: always
  type: complex
  contains:
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
          Information about the destination where events have to be delivered
          for the event subscription.
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
          The retry policy for events. This can be used to configure maximum
          number of delivery attempts and time to live for events.
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
          subscription. If it is desired to subscribe to all default event
          types, set the IncludedEventTypes to null.
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
              The operator type used for filtering, e.g., NumberIn,
              StringContains, BoolEquals and others.
          returned: always
          type: str
          sample: null
        key:
          description:
            - The field/property in the event based on which you want to filter.
          returned: always
          type: str
          sample: null
    value:
      description:
        - A collection of EventSubscriptions
      returned: always
      type: list
      sample: null
      contains:
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
              Information about the destination where events have to be
              delivered for the event subscription.
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
              The retry policy for events. This can be used to configure maximum
              number of delivery attempts and time to live for events.
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
              subscription. If it is desired to subscribe to all default event
              types, set the IncludedEventTypes to null.
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
                  The operator type used for filtering, e.g., NumberIn,
                  StringContains, BoolEquals and others.
              returned: always
              type: str
              sample: null
            key:
              description:
                - >-
                  The field/property in the event based on which you want to
                  filter.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - A link for the next page of event subscriptions
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
    from azure.mgmt.event import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEventSubscriptionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str'
            ),
            event_subscription_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            topic_type_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            provider_namespace=dict(
                type='str'
            ),
            resource_type_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            ),
            domain_name=dict(
                type='str'
            ),
            topic_name=dict(
                type='str'
            )
        )

        self.scope = None
        self.event_subscription_name = None
        self.filter = None
        self.top = None
        self.topic_type_name = None
        self.resource_group_name = None
        self.location = None
        self.provider_namespace = None
        self.resource_type_name = None
        self.resource_name = None
        self.domain_name = None
        self.topic_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEventSubscriptionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.provider_namespace is not None and
            self.resource_type_name is not None and
            self.resource_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listbyresource())
        elif (self.resource_group_name is not None and
              self.location is not None and
              self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbyresourcegroupfortopictype())
        elif (self.resource_group_name is not None and
              self.domain_name is not None and
              self.topic_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listbydomaintopic())
        elif (self.resource_group_name is not None and
              self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listglobalbyresourcegroupfortopictype())
        elif (self.resource_group_name is not None and
              self.location is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbyresourcegroup())
        elif (self.location is not None and
              self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbysubscriptionfortopictype())
        elif (self.scope is not None and
              self.event_subscription_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.get())
        elif (self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listglobalbysubscriptionfortopictype())
        elif (self.resource_group_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listglobalbyresourcegroup())
        elif (self.location is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbysubscription())
        else:
            self.results['event_subscriptions'] = self.format_item(self.listglobalbysubscription())
        return self.results

    def listbyresource(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_by_resource(resource_group_name=self.resource_group_name,
                                                                             provider_namespace=self.provider_namespace,
                                                                             resource_type_name=self.resource_type_name,
                                                                             resource_name=self.resource_name,
                                                                             filter=self.filter,
                                                                             top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listregionalbyresourcegroupfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_resource_group_for_topic_type(resource_group_name=self.resource_group_name,
                                                                                                           location=self.location,
                                                                                                           topic_type_name=self.topic_type_name,
                                                                                                           filter=self.filter,
                                                                                                           top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydomaintopic(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_by_domain_topic(resource_group_name=self.resource_group_name,
                                                                                 domain_name=self.domain_name,
                                                                                 topic_name=self.topic_name,
                                                                                 filter=self.filter,
                                                                                 top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listglobalbyresourcegroupfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_resource_group_for_topic_type(resource_group_name=self.resource_group_name,
                                                                                                         topic_type_name=self.topic_type_name,
                                                                                                         filter=self.filter,
                                                                                                         top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listregionalbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                            location=self.location,
                                                                                            filter=self.filter,
                                                                                            top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listregionalbysubscriptionfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_subscription_for_topic_type(location=self.location,
                                                                                                         topic_type_name=self.topic_type_name,
                                                                                                         filter=self.filter,
                                                                                                         top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.get(scope=self.scope,
                                                                event_subscription_name=self.event_subscription_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listglobalbysubscriptionfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_subscription_for_topic_type(topic_type_name=self.topic_type_name,
                                                                                                       filter=self.filter,
                                                                                                       top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listglobalbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                          filter=self.filter,
                                                                                          top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listregionalbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_subscription(location=self.location,
                                                                                          filter=self.filter,
                                                                                          top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listglobalbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_subscription(filter=self.filter,
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
    AzureRMEventSubscriptionInfo()


if __name__ == '__main__':
    main()
