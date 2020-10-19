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
module: azure_rm_bot
version_added: '2.9'
short_description: Manage Azure Bot instance.
description:
  - 'Create, update and delete instance of Azure Bot.'
options:
  resource_group_name:
    description:
      - The name of the Bot resource group in the user subscription.
    required: true
    type: str
  resource_name:
    description:
      - The name of the Bot resource.
    required: true
    type: str
  location:
    description:
      - Specifies the location of the resource.
    type: str
  kind:
    description:
      - Required. Gets or sets the Kind of the resource.
    type: str
    choices:
      - sdk
      - designer
      - bot
      - function
  etag:
    description:
      - Entity Tag
    type: str
  name:
    description:
      - The sku name
    type: str
    choices:
      - F0
      - S1
  properties:
    description:
      - The set of properties specific to bot resource
    type: dict
    suboptions:
      display_name:
        description:
          - The Name of the bot
        required: true
        type: str
      description:
        description:
          - The description of the bot
        type: str
      icon_url:
        description:
          - The Icon Url of the bot
        type: str
      endpoint:
        description:
          - The bot's endpoint
        required: true
        type: str
      endpoint_version:
        description:
          - The bot's endpoint version
        type: str
      msa_app_id:
        description:
          - Microsoft App Id for the bot
        required: true
        type: str
      configured_channels:
        description:
          - Collection of channels for which the bot is configured
        type: list
      enabled_channels:
        description:
          - Collection of channels for which the bot is enabled
        type: list
      developer_app_insight_key:
        description:
          - The Application Insights key
        type: str
      developer_app_insights_api_key:
        description:
          - The Application Insights Api Key
        type: str
      developer_app_insights_application_id:
        description:
          - The Application Insights App Id
        type: str
      luis_app_ids:
        description:
          - Collection of LUIS App Ids
        type: list
      luis_key:
        description:
          - The LUIS Key
        type: str
  state:
    description:
      - Assert the state of the Bot.
      - Use C(present) to create or update an Bot and C(absent) to delete it.
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
    - name: Create Bot
      azure_rm_bot: 
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        etag: etag1
        kind: sdk
        location: West US
        properties:
          description: The description of the bot
          developer_app_insight_key: appinsightskey
          developer_app_insights_api_key: appinsightsapikey
          developer_app_insights_application_id: appinsightsappid
          display_name: The Name of the bot
          endpoint: 'http://mybot.coffee'
          icon_url: 'http://myicon'
          luis_app_ids:
            - luisappid1
            - luisappid2
          luis_key: luiskey
          msa_app_id: exampleappid
        sku:
          name: S1
        tags:
          tag1: value1
          tag2: value2
        

    - name: Update Bot
      azure_rm_bot: 
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        etag: etag1
        kind: sdk
        location: West US
        properties:
          description: The description of the bot
          developer_app_insight_key: appinsightskey
          developer_app_insights_api_key: appinsightsapikey
          developer_app_insights_application_id: appinsightsappid
          display_name: The Name of the bot
          endpoint: 'http://mybot.coffee'
          icon_url: 'http://myicon'
          luis_app_ids:
            - luisappid1
            - luisappid2
          luis_key: luiskey
          msa_app_id: msaappid
        sku:
          name: S1
        tags:
          tag1: value1
          tag2: value2
        

    - name: Delete Bot
      azure_rm_bot: 
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        

'''

RETURN = '''
id:
  description:
    - Specifies the resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Specifies the name of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - Specifies the location of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - Specifies the type of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Contains resource tags defined as key/value pairs.
  returned: always
  type: dictionary
  sample: null
kind:
  description:
    - Required. Gets or sets the Kind of the resource.
  returned: always
  type: str
  sample: null
etag:
  description:
    - Entity Tag
  returned: always
  type: str
  sample: null
name_sku_name:
  description:
    - The sku name
  returned: always
  type: str
  sample: null
tier:
  description:
    - Gets the sku tier. This is based on the SKU name.
  returned: always
  type: str
  sample: null
properties:
  description:
    - The set of properties specific to bot resource
  returned: always
  type: dict
  sample: null
  contains:
    display_name:
      description:
        - The Name of the bot
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the bot
      returned: always
      type: str
      sample: null
    icon_url:
      description:
        - The Icon Url of the bot
      returned: always
      type: str
      sample: null
    endpoint:
      description:
        - The bot's endpoint
      returned: always
      type: str
      sample: null
    endpoint_version:
      description:
        - The bot's endpoint version
      returned: always
      type: str
      sample: null
    msa_app_id:
      description:
        - Microsoft App Id for the bot
      returned: always
      type: str
      sample: null
    configured_channels:
      description:
        - Collection of channels for which the bot is configured
      returned: always
      type: list
      sample: null
    enabled_channels:
      description:
        - Collection of channels for which the bot is enabled
      returned: always
      type: list
      sample: null
    developer_app_insight_key:
      description:
        - The Application Insights key
      returned: always
      type: str
      sample: null
    developer_app_insights_api_key:
      description:
        - The Application Insights Api Key
      returned: always
      type: str
      sample: null
    developer_app_insights_application_id:
      description:
        - The Application Insights App Id
      returned: always
      type: str
      sample: null
    luis_app_ids:
      description:
        - Collection of LUIS App Ids
      returned: always
      type: list
      sample: null
    luis_key:
      description:
        - The LUIS Key
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
    from azure.mgmt.azure import Azure Bot Service
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBot(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            kind=dict(
                type='str',
                disposition='/kind',
                choices=['sdk',
                         'designer',
                         'bot',
                         'function']
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            name=dict(
                type='str',
                disposition='/name',
                choices=['F0',
                         'S1']
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    display_name=dict(
                        type='str',
                        disposition='display_name',
                        required=True
                    ),
                    description=dict(
                        type='str',
                        disposition='description'
                    ),
                    icon_url=dict(
                        type='str',
                        disposition='icon_url'
                    ),
                    endpoint=dict(
                        type='str',
                        disposition='endpoint',
                        required=True
                    ),
                    endpoint_version=dict(
                        type='str',
                        updatable=False,
                        disposition='endpoint_version'
                    ),
                    msa_app_id=dict(
                        type='str',
                        disposition='msa_app_id',
                        required=True
                    ),
                    configured_channels=dict(
                        type='list',
                        updatable=False,
                        disposition='configured_channels',
                        elements='str'
                    ),
                    enabled_channels=dict(
                        type='list',
                        updatable=False,
                        disposition='enabled_channels',
                        elements='str'
                    ),
                    developer_app_insight_key=dict(
                        type='str',
                        disposition='developer_app_insight_key'
                    ),
                    developer_app_insights_api_key=dict(
                        type='str',
                        disposition='developer_app_insights_api_key'
                    ),
                    developer_app_insights_application_id=dict(
                        type='str',
                        disposition='developer_app_insights_application_id'
                    ),
                    luis_app_ids=dict(
                        type='list',
                        disposition='luis_app_ids',
                        elements='str'
                    ),
                    luis_key=dict(
                        type='str',
                        disposition='luis_key'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBot, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Bot Service,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-02')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.bots.create(resource_group_name=self.resource_group_name,
                                                        resource_name=self.resource_name,
                                                        parameters=self.body)
            else:
                response = self.mgmt_client.bots.update(resource_group_name=self.resource_group_name,
                                                        resource_name=self.resource_name,
                                                        parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Bot instance.')
            self.fail('Error creating the Bot instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.bots.delete(resource_group_name=self.resource_group_name,
                                                    resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Bot instance.')
            self.fail('Error deleting the Bot instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.bots.get(resource_group_name=self.resource_group_name,
                                                 resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBot()


if __name__ == '__main__':
    main()
