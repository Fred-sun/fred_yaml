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
module: azure_rm_firewallrule
version_added: '2.9'
short_description: Manage Azure FirewallRule instance.
description:
  - 'Create, update and delete instance of Azure FirewallRule.'
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
  firewall_rule_name:
    description:
      - The name of the firewall rule.
    required: true
    type: str
  start_ip_address:
    description:
      - >-
        The start IP address of the firewall rule. Must be IPv4 format. Use
        value '0.0.0.0' to represent all Azure-internal IP addresses.
    type: str
  end_ip_address:
    description:
      - >-
        The end IP address of the firewall rule. Must be IPv4 format. Must be
        greater than or equal to startIpAddress. Use value '0.0.0.0' to
        represent all Azure-internal IP addresses.
    type: str
  state:
    description:
      - Assert the state of the FirewallRule.
      - >-
        Use C(present) to create or update an FirewallRule and C(absent) to
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
    - name: Create a firewall rule max/min
      azure_rm_firewallrule: 
        firewall_rule_name: firewallrulecrudtest-5370
        resource_group_name: firewallrulecrudtest-12
        server_name: firewallrulecrudtest-6285
        properties:
          end_ip_address: 0.0.0.3
          start_ip_address: 0.0.0.3
        

    - name: Update a firewall rule max/min
      azure_rm_firewallrule: 
        firewall_rule_name: firewallrulecrudtest-3927
        resource_group_name: firewallrulecrudtest-12
        server_name: firewallrulecrudtest-6285
        properties:
          end_ip_address: 0.0.0.1
          start_ip_address: 0.0.0.1
        

    - name: Delete a firewall rule
      azure_rm_firewallrule: 
        firewall_rule_name: firewallrulecrudtest-7011
        resource_group_name: firewallrulecrudtest-9886
        server_name: firewallrulecrudtest-2368
        

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
kind:
  description:
    - Kind of server that contains this firewall rule.
  returned: always
  type: str
  sample: null
location:
  description:
    - Location of the server that contains this firewall rule.
  returned: always
  type: str
  sample: null
start_ip_address:
  description:
    - >-
      The start IP address of the firewall rule. Must be IPv4 format. Use value
      '0.0.0.0' to represent all Azure-internal IP addresses.
  returned: always
  type: str
  sample: null
end_ip_address:
  description:
    - >-
      The end IP address of the firewall rule. Must be IPv4 format. Must be
      greater than or equal to startIpAddress. Use value '0.0.0.0' to represent
      all Azure-internal IP addresses.
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


class AzureRMFirewallRule(AzureRMModuleBaseExt):
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
            firewall_rule_name=dict(
                type='str',
                required=True
            ),
            start_ip_address=dict(
                type='str',
                disposition='/start_ip_address'
            ),
            end_ip_address=dict(
                type='str',
                disposition='/end_ip_address'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.firewall_rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFirewallRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2014-04-01')

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
            response = self.mgmt_client.firewall_rules.create_or_update(resource_group_name=self.resource_group_name,
                                                                        server_name=self.server_name,
                                                                        firewall_rule_name=self.firewall_rule_name,
                                                                        parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FirewallRule instance.')
            self.fail('Error creating the FirewallRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.firewall_rules.delete(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              firewall_rule_name=self.firewall_rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the FirewallRule instance.')
            self.fail('Error deleting the FirewallRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.firewall_rules.get(resource_group_name=self.resource_group_name,
                                                           server_name=self.server_name,
                                                           firewall_rule_name=self.firewall_rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFirewallRule()


if __name__ == '__main__':
    main()
