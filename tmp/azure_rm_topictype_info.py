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
module: azure_rm_topictype_info
version_added: '2.9'
short_description: Get TopicType info.
description:
  - Get info of TopicType.
options:
  topic_type_name:
    description:
      - Name of the topic type.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: TopicTypes_List
      azure_rm_topictype_info: 
        {}
        

    - name: TopicTypes_Get
      azure_rm_topictype_info: 
        topic_type_name: Microsoft.Storage.StorageAccounts
        

    - name: TopicTypes_ListEventTypes
      azure_rm_topictype_info: 
        topic_type_name: Microsoft.Storage.StorageAccounts
        

'''

RETURN = '''
topic_types:
  description: >-
    A list of dict results where the key is the name of the TopicType and the
    values are the facts for that TopicType.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          A collection of topic types
          A collection of event types
      returned: always
      type: list
      sample: null
      contains:
        provider:
          description:
            - Namespace of the provider of the topic type.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - Display Name for the topic type.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Description of the topic type.
          returned: always
          type: str
          sample: null
        resource_region_type:
          description:
            - Region type of the resource.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state of the topic type
          returned: always
          type: str
          sample: null
        supported_locations:
          description:
            - List of locations supported by this topic type.
          returned: always
          type: list
          sample: null
        source_resource_format:
          description:
            - Source resource format.
          returned: always
          type: str
          sample: null
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
    provider:
      description:
        - Namespace of the provider of the topic type.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Display Name for the topic type.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description of the topic type.
      returned: always
      type: str
      sample: null
    resource_region_type:
      description:
        - Region type of the resource.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the topic type
      returned: always
      type: str
      sample: null
    supported_locations:
      description:
        - List of locations supported by this topic type.
      returned: always
      type: list
      sample: null
    source_resource_format:
      description:
        - Source resource format.
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


class AzureRMTopicTypeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            topic_type_name=dict(
                type='str'
            )
        )

        self.topic_type_name = None

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
        super(AzureRMTopicTypeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.topic_type_name is not None):
            self.results['topic_types'] = self.format_item(self.get())
        elif (self.topic_type_name is not None):
            self.results['topic_types'] = self.format_item(self.listeventtype())
        else:
            self.results['topic_types'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.topic_types.get(topic_type_name=self.topic_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listeventtype(self):
        response = None

        try:
            response = self.mgmt_client.topic_types.list_event_type(topic_type_name=self.topic_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.topic_types.list()
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
    AzureRMTopicTypeInfo()


if __name__ == '__main__':
    main()
