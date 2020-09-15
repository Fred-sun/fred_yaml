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
module: azure_rm_virtualnetworkrule_info
version_added: '2.9'
short_description: Get VirtualNetworkRule info.
description:
  - Get info of VirtualNetworkRule.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a virtual network rule
      azure_rm_virtualnetworkrule_info: 
        resource_group_name: Default
        server_name: vnet-test-svr
        virtual_network_rule_name: vnet-firewall-rule
        

    - name: List virtual network rules
      azure_rm_virtualnetworkrule_info: 
        resource_group_name: Default
        server_name: vnet-test-svr
        

'''

RETURN = '''
virtual_network_rules:
  description: >-
    A list of dict results where the key is the name of the VirtualNetworkRule
    and the values are the facts for that VirtualNetworkRule.
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
    virtual_network_subnet_id:
      description:
        - The ARM resource id of the virtual network subnet.
      returned: always
      type: str
      sample: null
    ignore_missing_vnet_service_endpoint:
      description:
        - >-
          Create firewall rule before the virtual network has vnet service
          endpoint enabled.
      returned: always
      type: bool
      sample: null
    state:
      description:
        - Virtual Network Rule State
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        virtual_network_subnet_id:
          description:
            - The ARM resource id of the virtual network subnet.
          returned: always
          type: str
          sample: null
        ignore_missing_vnet_service_endpoint:
          description:
            - >-
              Create firewall rule before the virtual network has vnet service
              endpoint enabled.
          returned: always
          type: bool
          sample: null
        state:
          description:
            - Virtual Network Rule State
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualNetworkRuleInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.virtual_network_rule_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualNetworkRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.virtual_network_rule_name is not None):
            self.results['virtual_network_rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['virtual_network_rules'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_rules.get(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  virtual_network_rule_name=self.virtual_network_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_rules.list_by_server(resource_group_name=self.resource_group_name,
                                                                             server_name=self.server_name)
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
    AzureRMVirtualNetworkRuleInfo()


if __name__ == '__main__':
    main()
