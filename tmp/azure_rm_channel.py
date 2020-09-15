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
module: azure_rm_channel
version_added: '2.9'
short_description: Manage Azure Channel instance.
description:
  - 'Create, update and delete instance of Azure Channel.'
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
      - The EngagementFabric channel name
    required: true
    type: str
  channel_type:
    description:
      - The channel type
    type: str
  channel_functions:
    description:
      - The functions to be enabled for the channel
    type: list
  credentials:
    description:
      - The channel credentials
    type: dictionary
  state:
    description:
      - Assert the state of the Channel.
      - >-
        Use C(present) to create or update an Channel and C(absent) to delete
        it.
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
    - name: ChannelsCreateOrUpdateExample
      azure_rm_channel: 
        account_name: ExampleAccount
        channel_name: ExampleChannel
        resource_group_name: ExampleRg
        properties:
          channel_functions:
            - MockFunction1
            - MockFunction2
          channel_type: MockChannel
          credentials:
            app_id: exampleApp
            app_key: exampleAppKey
        

    - name: ChannelsDeleteExample
      azure_rm_channel: 
        account_name: ExampleAccount
        channel_name: ExampleChannel
        resource_group_name: ExampleRg
        

'''

RETURN = '''
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.engagement import EngagementFabric
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMChannel(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            channel_type=dict(
                type='str',
                disposition='/channel_type'
            ),
            channel_functions=dict(
                type='list',
                disposition='/channel_functions',
                elements='str'
            ),
            credentials=dict(
                type='dictionary',
                disposition='/credentials'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.channel_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMChannel, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(EngagementFabric,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

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
            response = self.mgmt_client.channels.create_or_update(resource_group_name=self.resource_group_name,
                                                                  account_name=self.account_name,
                                                                  channel_name=self.channel_name,
                                                                  channel=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Channel instance.')
            self.fail('Error creating the Channel instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.channels.delete(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        channel_name=self.channel_name)
        except CloudError as e:
            self.log('Error attempting to delete the Channel instance.')
            self.fail('Error deleting the Channel instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.channels.get(resource_group_name=self.resource_group_name,
                                                     account_name=self.account_name,
                                                     channel_name=self.channel_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMChannel()


if __name__ == '__main__':
    main()
