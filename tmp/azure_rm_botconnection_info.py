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
module: azure_rm_botconnection_info
version_added: '2.9'
short_description: Get BotConnection info.
description:
  - Get info of BotConnection.
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
  connection_name:
    description:
      - The name of the Bot Service Connection Setting resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Update Connection Setting
      azure_rm_botconnection_info: 
        connection_name: sampleConnection
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        

    - name: List Connection Settings
      azure_rm_botconnection_info: 
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        

'''

RETURN = '''
bot_connection:
  description: >-
    A list of dict results where the key is the name of the BotConnection and
    the values are the facts for that BotConnection.
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
    client_id:
      description:
        - Client Id associated with the Connection Setting.
      returned: always
      type: str
      sample: null
    setting_id:
      description:
        - Setting Id set by the service for the Connection Setting.
      returned: always
      type: str
      sample: null
    client_secret:
      description:
        - Client Secret associated with the Connection Setting
      returned: always
      type: str
      sample: null
    scopes:
      description:
        - Scopes associated with the Connection Setting
      returned: always
      type: str
      sample: null
    service_provider_id:
      description:
        - Service Provider Id associated with the Connection Setting
      returned: always
      type: str
      sample: null
    service_provider_display_name:
      description:
        - Service Provider Display Name associated with the Connection Setting
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - Service Provider Parameters associated with the Connection Setting
      returned: always
      type: list
      sample: null
      contains:
        key:
          description:
            - Key for the Connection Setting Parameter.
          returned: always
          type: str
          sample: null
        value:
          description:
            - Value associated with the Connection Setting Parameter.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          The link used to get the next page of bot service connection setting
          resources.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Gets the list of bot service connection settings and their properties.
      returned: always
      type: list
      sample: null
      contains:
        client_id:
          description:
            - Client Id associated with the Connection Setting.
          returned: always
          type: str
          sample: null
        setting_id:
          description:
            - Setting Id set by the service for the Connection Setting.
          returned: always
          type: str
          sample: null
        client_secret:
          description:
            - Client Secret associated with the Connection Setting
          returned: always
          type: str
          sample: null
        scopes:
          description:
            - Scopes associated with the Connection Setting
          returned: always
          type: str
          sample: null
        service_provider_id:
          description:
            - Service Provider Id associated with the Connection Setting
          returned: always
          type: str
          sample: null
        service_provider_display_name:
          description:
            - >-
              Service Provider Display Name associated with the Connection
              Setting
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - Service Provider Parameters associated with the Connection Setting
          returned: always
          type: list
          sample: null
          contains:
            key:
              description:
                - Key for the Connection Setting Parameter.
              returned: always
              type: str
              sample: null
            value:
              description:
                - Value associated with the Connection Setting Parameter.
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


class AzureRMBotConnectionInfo(AzureRMModuleBase):
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
            connection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.connection_name = None

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
        super(AzureRMBotConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Bot Service,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-02')

        if (self.resource_group_name is not None and
            self.resource_name is not None and
            self.connection_name is not None):
            self.results['bot_connection'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['bot_connection'] = self.format_item(self.listbybotservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.bot_connection.get(resource_group_name=self.resource_group_name,
                                                           resource_name=self.resource_name,
                                                           connection_name=self.connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbybotservice(self):
        response = None

        try:
            response = self.mgmt_client.bot_connection.list_by_bot_service(resource_group_name=self.resource_group_name,
                                                                           resource_name=self.resource_name)
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
    AzureRMBotConnectionInfo()


if __name__ == '__main__':
    main()
