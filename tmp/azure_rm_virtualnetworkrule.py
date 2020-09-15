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
module: azure_rm_virtualnetworkrule
version_added: '2.9'
short_description: Manage Azure VirtualNetworkRule instance.
description:
  - 'Create, update and delete instance of Azure VirtualNetworkRule.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  virtual_network_rule_name:
    description:
      - The name of the virtual network rule.
    required: true
    type: str
  virtual_network_subnet_id:
    description:
      - The ARM resource id of the virtual network subnet.
    type: str
  ignore_missing_vnet_service_endpoint:
    description:
      - >-
        Create firewall rule before the virtual network has vnet service
        endpoint enabled.
    type: bool
  state:
    description:
      - Assert the state of the VirtualNetworkRule.
      - >-
        Use C(present) to create or update an VirtualNetworkRule and C(absent)
        to delete it.
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
    - name: Create or update a virtual network rule
      azure_rm_virtualnetworkrule: 
        resource_group_name: Default
        server_name: vnet-test-svr
        virtual_network_rule_name: vnet-firewall-rule
        properties:
          ignore_missing_vnet_service_endpoint: false
          virtual_network_subnet_id: >-
            /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Network/virtualNetworks/testvnet/subnets/testsubnet
        

    - name: Delete a virtual network rule
      azure_rm_virtualnetworkrule: 
        resource_group_name: Default
        server_name: vnet-test-svr
        virtual_network_rule_name: vnet-firewall-rule
        

'''

RETURN = '''
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
virtual_network_subnet_id:
  description:
    - The ARM resource id of the virtual network subnet.
  returned: always
  type: str
  sample: null
ignore_missing_vnet_service_endpoint:
  description:
    - >-
      Create firewall rule before the virtual network has vnet service endpoint
      enabled.
  returned: always
  type: bool
  sample: null
state:
  description:
    - Virtual Network Rule State
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualNetworkRule(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            virtual_network_rule_name=dict(
                type='str',
                required=True
            ),
            virtual_network_subnet_id=dict(
                type='str',
                disposition='/virtual_network_subnet_id'
            ),
            ignore_missing_vnet_service_endpoint=dict(
                type='bool',
                disposition='/ignore_missing_vnet_service_endpoint'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.virtual_network_rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworkRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

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
            response = self.mgmt_client.virtual_network_rules.create_or_update(resource_group_name=self.resource_group_name,
                                                                               server_name=self.server_name,
                                                                               virtual_network_rule_name=self.virtual_network_rule_name,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetworkRule instance.')
            self.fail('Error creating the VirtualNetworkRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_network_rules.delete(resource_group_name=self.resource_group_name,
                                                                     server_name=self.server_name,
                                                                     virtual_network_rule_name=self.virtual_network_rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetworkRule instance.')
            self.fail('Error deleting the VirtualNetworkRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_network_rules.get(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  virtual_network_rule_name=self.virtual_network_rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualNetworkRule()


if __name__ == '__main__':
    main()
