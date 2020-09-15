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
module: azure_rm_transactionnode_info
version_added: '2.9'
short_description: Get TransactionNode info.
description:
  - Get info of TransactionNode.
options:
  blockchain_member_name:
    description:
      - Blockchain member name.
    required: true
    type: str
  transaction_node_name:
    description:
      - Transaction node name.
    type: str
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: TransactionNodes_Get
      azure_rm_transactionnode_info: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        transaction_node_name: txnode2
        

    - name: TransactionNodes_List
      azure_rm_transactionnode_info: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        

'''

RETURN = '''
transaction_nodes:
  description: >-
    A list of dict results where the key is the name of the TransactionNode and
    the values are the facts for that TransactionNode.
  returned: always
  type: complex
  contains:
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
    value:
      description:
        - Gets or sets the collection of transaction nodes.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              Gets or sets the transaction node dns endpoint basic auth user
              name.
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
    next_link:
      description:
        - "Gets or sets the URL, that the client should use to fetch the next page (per server side paging).\r\nIt's null for now, added for future use."
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
    from azure.mgmt.blockchain import BlockchainManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTransactionNodeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            blockchain_member_name=dict(
                type='str',
                required=True
            ),
            transaction_node_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str',
                required=True
            )
        )

        self.blockchain_member_name = None
        self.transaction_node_name = None
        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTransactionNodeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BlockchainManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.blockchain_member_name is not None and
            self.transaction_node_name is not None and
            self.resource_group_name is not None):
            self.results['transaction_nodes'] = self.format_item(self.get())
        elif (self.blockchain_member_name is not None and
              self.resource_group_name is not None):
            self.results['transaction_nodes'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.transaction_nodes.get(blockchain_member_name=self.blockchain_member_name,
                                                              transaction_node_name=self.transaction_node_name,
                                                              resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.transaction_nodes.list(blockchain_member_name=self.blockchain_member_name,
                                                               resource_group_name=self.resource_group_name)
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
    AzureRMTransactionNodeInfo()


if __name__ == '__main__':
    main()
