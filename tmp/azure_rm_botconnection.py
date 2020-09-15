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
module: azure_rm_botconnection
version_added: '2.9'
short_description: Manage Azure BotConnection instance.
description:
  - 'Create, update and delete instance of Azure BotConnection.'
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
  client_id:
    description:
      - Client Id associated with the Connection Setting.
    type: str
  client_secret:
    description:
      - Client Secret associated with the Connection Setting
    type: str
  scopes:
    description:
      - Scopes associated with the Connection Setting
    type: str
  service_provider_id:
    description:
      - Service Provider Id associated with the Connection Setting
    type: str
  service_provider_display_name:
    description:
      - Service Provider Display Name associated with the Connection Setting
    type: str
  parameters:
    description:
      - Service Provider Parameters associated with the Connection Setting
    type: list
    suboptions:
      key:
        description:
          - Key for the Connection Setting Parameter.
        type: str
      value:
        description:
          - Value associated with the Connection Setting Parameter.
        type: str
  state:
    description:
      - Assert the state of the BotConnection.
      - >-
        Use C(present) to create or update an BotConnection and C(absent) to
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
    - name: Create Connection Setting
      azure_rm_botconnection: 
        connection_name: sampleConnection
        parameters:
          etag: etag1
          location: West US
          properties:
            client_id: sampleclientid
            client_secret: samplesecret
            parameters:
              - key: key1
                value: value1
              - key: key2
                value: value2
            scopes: samplescope
            service_provider_id: serviceproviderid
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        etag: etag1
        location: West US
        properties:
          client_id: sampleclientid
          client_secret: samplesecret
          parameters:
            - key: key1
              value: value1
            - key: key2
              value: value2
          scopes: samplescope
          service_provider_id: serviceproviderid
        

    - name: Update Connection Setting
      azure_rm_botconnection: 
        connection_name: sampleConnection
        parameters:
          etag: etag1
          location: global
          properties:
            client_id: sampleclientid
            client_secret: samplesecret
            parameters:
              - key: key1
                value: value1
              - key: key2
                value: value2
            scopes: samplescope
            service_provider_display_name: serviceProviderDisplayName
            service_provider_id: serviceproviderid
        resource_group_name: OneResourceGroupName
        resource_name: samplebotname
        etag: etag1
        location: global
        properties:
          client_id: sampleclientid
          client_secret: samplesecret
          parameters:
            - key: key1
              value: value1
            - key: key2
              value: value2
          scopes: samplescope
          service_provider_display_name: serviceProviderDisplayName
          service_provider_id: serviceproviderid
        

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


class AzureRMBotConnection(AzureRMModuleBaseExt):
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
            client_id=dict(
                type='str',
                disposition='/client_id'
            ),
            client_secret=dict(
                type='str',
                disposition='/client_secret'
            ),
            scopes=dict(
                type='str',
                disposition='/scopes'
            ),
            service_provider_id=dict(
                type='str',
                disposition='/service_provider_id'
            ),
            service_provider_display_name=dict(
                type='str',
                disposition='/service_provider_display_name'
            ),
            parameters=dict(
                type='list',
                disposition='/parameters',
                elements='dict',
                options=dict(
                    key=dict(
                        type='str',
                        disposition='key'
                    ),
                    value=dict(
                        type='str',
                        disposition='value'
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
        self.connection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBotConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.bot_connection.create(resource_group_name=self.resource_group_name,
                                                                  resource_name=self.resource_name,
                                                                  connection_name=self.connection_name,
                                                                  parameters=self.body)
            else:
                response = self.mgmt_client.bot_connection.update(resource_group_name=self.resource_group_name,
                                                                  resource_name=self.resource_name,
                                                                  connection_name=self.connection_name,
                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BotConnection instance.')
            self.fail('Error creating the BotConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.bot_connection.delete(resource_group_name=self.resource_group_name,
                                                              resource_name=self.resource_name,
                                                              connection_name=self.connection_name)
        except CloudError as e:
            self.log('Error attempting to delete the BotConnection instance.')
            self.fail('Error deleting the BotConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.bot_connection.get(resource_group_name=self.resource_group_name,
                                                           resource_name=self.resource_name,
                                                           connection_name=self.connection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBotConnection()


if __name__ == '__main__':
    main()
