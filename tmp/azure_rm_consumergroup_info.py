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
module: azure_rm_consumergroup_info
version_added: '2.9'
short_description: Get ConsumerGroup info.
description:
  - Get info of ConsumerGroup.
options:
  resource_group_name:
    description:
      - Name of the resource group within the azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The Namespace name
    required: true
    type: str
  event_hub_name:
    description:
      - The Event Hub name
    required: true
    type: str
  consumer_group_name:
    description:
      - The consumer group name
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
    - name: ConsumerGroupGet
      azure_rm_consumergroup_info: 
        consumer_group_name: sdk-ConsumerGroup-5563
        event_hub_name: sdk-EventHub-6681
        namespace_name: sdk-Namespace-2661
        resource_group_name: ArunMonocle
        

    - name: ConsumerGroupsListAll
      azure_rm_consumergroup_info: 
        event_hub_name: sdk-EventHub-6681
        namespace_name: sdk-Namespace-2661
        resource_group_name: ArunMonocle
        

'''

RETURN = '''
consumer_groups:
  description: >-
    A list of dict results where the key is the name of the ConsumerGroup and
    the values are the facts for that ConsumerGroup.
  returned: always
  type: complex
  contains:
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
    user_metadata:
      description:
        - >-
          User Metadata is a placeholder to store user-defined string data with
          maximum length 1024. e.g. it can be used to store descriptive data,
          such as list of teams and their contact information also user-defined
          configuration settings can be stored.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Result of the List Consumer Group operation.
      returned: always
      type: list
      sample: null
      contains:
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
        user_metadata:
          description:
            - >-
              User Metadata is a placeholder to store user-defined string data
              with maximum length 1024. e.g. it can be used to store descriptive
              data, such as list of teams and their contact information also
              user-defined configuration settings can be stored.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of Consumer Group
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
    from azure.mgmt.event import EventHubManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConsumerGroupInfo(AzureRMModuleBase):
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
            event_hub_name=dict(
                type='str',
                required=True
            ),
            consumer_group_name=dict(
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
        self.event_hub_name = None
        self.consumer_group_name = None
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
        super(AzureRMConsumerGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventHubManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.event_hub_name is not None and
            self.consumer_group_name is not None):
            self.results['consumer_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.event_hub_name is not None):
            self.results['consumer_groups'] = self.format_item(self.listbyeventhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.consumer_groups.get(resource_group_name=self.resource_group_name,
                                                            namespace_name=self.namespace_name,
                                                            event_hub_name=self.event_hub_name,
                                                            consumer_group_name=self.consumer_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyeventhub(self):
        response = None

        try:
            response = self.mgmt_client.consumer_groups.list_by_event_hub(resource_group_name=self.resource_group_name,
                                                                          namespace_name=self.namespace_name,
                                                                          event_hub_name=self.event_hub_name,
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
    AzureRMConsumerGroupInfo()


if __name__ == '__main__':
    main()
