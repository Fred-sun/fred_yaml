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
module: azure_rm_bot_info
version_added: '2.9'
short_description: Get Bot info.
description:
  - Get info of Bot.
options:
  resource_group_name:
    description:
      - The name of the Bot resource group in the user subscription.
    type: str
  resource_name:
    description:
      - The name of the Bot resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Bot
      azure_rm_bot_info: 
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        

    - name: List Bots by Resource Group
      azure_rm_bot_info: 
        resource_group_name: OneResourceGroupName
        

    - name: List Bots by Subscription
      azure_rm_bot_info: 
        {}
        

'''

RETURN = '''
bots:
  description: >-
    A list of dict results where the key is the name of the Bot and the values
    are the facts for that Bot.
  returned: always
  type: complex
  contains:
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
    next_link:
      description:
        - The link used to get the next page of bot service resources.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Gets the list of bot service results and their properties.
      returned: always
      type: list
      sample: null
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Bot Service
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBotInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-02'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMBotInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Bot Service,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-02')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['bots'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['bots'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['bots'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.bots.get(resource_group_name=self.resource_group_name,
                                                 resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.bots.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.bots.list()
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
    AzureRMBotInfo()


if __name__ == '__main__':
    main()
