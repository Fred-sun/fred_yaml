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
module: azure_rm_channel_info
version_added: '2.9'
short_description: Get Channel info.
description:
  - Get info of Channel.
options:
  resource_group_name:
    description:
      - Resource Group Name
    required: true
    type: str
  account_name:
    description:
      - Account Name
    required: true
    type: str
  channel_name:
    description:
      - Channel Name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ChannelsGetExample
      azure_rm_channel_info: 
        account_name: ExampleAccount
        channel_name: ExampleChannel
        resource_group_name: ExampleRg
        

    - name: ChannelsListExample
      azure_rm_channel_info: 
        account_name: ExampleAccount
        resource_group_name: ExampleRg
        

'''

RETURN = '''
channels:
  description: >-
    A list of dict results where the key is the name of the Channel and the
    values are the facts for that Channel.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The ID of the resource
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - The fully qualified type of the resource
      returned: always
      type: str
      sample: null
    channel_type:
      description:
        - The channel type
      returned: always
      type: str
      sample: null
    channel_functions:
      description:
        - The functions to be enabled for the channel
      returned: always
      type: list
      sample: null
    credentials:
      description:
        - The channel credentials
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - EngagementFabric channels
      returned: always
      type: list
      sample: null
      contains:
        channel_type:
          description:
            - The channel type
          returned: always
          type: str
          sample: null
        channel_functions:
          description:
            - The functions to be enabled for the channel
          returned: always
          type: list
          sample: null
        credentials:
          description:
            - The channel credentials
          returned: always
          type: dictionary
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.engagement import EngagementFabric
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMChannelInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            channel_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.channel_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMChannelInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EngagementFabric,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.channel_name is not None):
            self.results['channels'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['channels'] = self.format_item(self.listbyaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.channels.get(resource_group_name=self.resource_group_name,
                                                     account_name=self.account_name,
                                                     channel_name=self.channel_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyaccount(self):
        response = None

        try:
            response = self.mgmt_client.channels.list_by_account(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name)
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
    AzureRMChannelInfo()


if __name__ == '__main__':
    main()
