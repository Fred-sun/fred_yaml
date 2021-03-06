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
module: azure_rm_transactionnode
version_added: '2.9'
short_description: Manage Azure TransactionNode instance.
description:
  - 'Create, update and delete instance of Azure TransactionNode.'
options:
  blockchain_member_name:
    description:
      - Blockchain member name.
    required: true
    type: str
  transaction_node_name:
    description:
      - Transaction node name.
    required: true
    type: str
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  location:
    description:
      - Gets or sets the transaction node location.
    type: str
  password:
    description:
      - Sets the transaction node dns endpoint basic auth password.
    type: str
  firewall_rules:
    description:
      - Gets or sets the firewall rules.
    type: list
    suboptions:
      rule_name:
        description:
          - Gets or sets the name of the firewall rules.
        type: str
      start_ip_address:
        description:
          - Gets or sets the start IP address of the firewall rule range.
        type: str
      end_ip_address:
        description:
          - Gets or sets the end IP address of the firewall rule range.
        type: str
  state:
    description:
      - Assert the state of the TransactionNode.
      - >-
        Use C(present) to create or update an TransactionNode and C(absent) to
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
    - name: TransactionNodes_Create
      azure_rm_transactionnode: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        transaction_node_name: txnode2
        

    - name: TransactionNodes_Delete
      azure_rm_transactionnode: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        transaction_node_name: txNode2
        

    - name: TransactionNodes_Update
      azure_rm_transactionnode: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        transaction_node_name: txnode2
        

'''

RETURN = '''
id:
  description:
    - Fully qualified resource Id of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the service - e.g. "Microsoft.Blockchain"
  returned: always
  type: str
  sample: null
location:
  description:
    - Gets or sets the transaction node location.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Gets or sets the blockchain member provision state.
  returned: always
  type: str
  sample: null
dns:
  description:
    - Gets or sets the transaction node dns endpoint.
  returned: always
  type: str
  sample: null
public_key:
  description:
    - Gets or sets the transaction node public key.
  returned: always
  type: str
  sample: null
user_name:
  description:
    - Gets or sets the transaction node dns endpoint basic auth user name.
  returned: always
  type: str
  sample: null
password:
  description:
    - Sets the transaction node dns endpoint basic auth password.
  returned: always
  type: str
  sample: null
firewall_rules:
  description:
    - Gets or sets the firewall rules.
  returned: always
  type: list
  sample: null
  contains:
    rule_name:
      description:
        - Gets or sets the name of the firewall rules.
      returned: always
      type: str
      sample: null
    start_ip_address:
      description:
        - Gets or sets the start IP address of the firewall rule range.
      returned: always
      type: str
      sample: null
    end_ip_address:
      description:
        - Gets or sets the end IP address of the firewall rule range.
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
    from azure.mgmt.blockchain import BlockchainManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTransactionNode(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            blockchain_member_name=dict(
                type='str',
                required=True
            ),
            transaction_node_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            password=dict(
                type='str',
                disposition='/password'
            ),
            firewall_rules=dict(
                type='list',
                disposition='/firewall_rules',
                elements='dict',
                options=dict(
                    rule_name=dict(
                        type='str',
                        disposition='rule_name'
                    ),
                    start_ip_address=dict(
                        type='str',
                        disposition='start_ip_address'
                    ),
                    end_ip_address=dict(
                        type='str',
                        disposition='end_ip_address'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.blockchain_member_name = None
        self.transaction_node_name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTransactionNode, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(BlockchainManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

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
                response = self.mgmt_client.transaction_nodes.create(blockchain_member_name=self.blockchain_member_name,
                                                                     transaction_node_name=self.transaction_node_name,
                                                                     resource_group_name=self.resource_group_name,
                                                                     transaction_node=self.body)
            else:
                response = self.mgmt_client.transaction_nodes.update(blockchain_member_name=self.blockchain_member_name,
                                                                     transaction_node_name=self.transaction_node_name,
                                                                     resource_group_name=self.resource_group_name,
                                                                     transaction_node=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the TransactionNode instance.')
            self.fail('Error creating the TransactionNode instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.transaction_nodes.delete(blockchain_member_name=self.blockchain_member_name,
                                                                 transaction_node_name=self.transaction_node_name,
                                                                 resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the TransactionNode instance.')
            self.fail('Error deleting the TransactionNode instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.transaction_nodes.get(blockchain_member_name=self.blockchain_member_name,
                                                              transaction_node_name=self.transaction_node_name,
                                                              resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTransactionNode()


if __name__ == '__main__':
    main()
