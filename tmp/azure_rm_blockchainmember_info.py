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
module: azure_rm_blockchainmember_info
version_added: '2.9'
short_description: Get BlockchainMember info.
description:
  - Get info of BlockchainMember.
options:
  blockchain_member_name:
    description:
      - Blockchain member name.
    type: str
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: BlockchainMembers_Get
      azure_rm_blockchainmember_info: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        

    - name: BlockchainMembers_List
      azure_rm_blockchainmember_info: 
        resource_group_name: mygroup
        

    - name: BlockchainMembers_ListAll
      azure_rm_blockchainmember_info: 
        {}
        

    - name: BlockchainMembers_ListConsortiumMembers
      azure_rm_blockchainmember_info: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        

'''

RETURN = '''
blockchain_members:
  description: >-
    A list of dict results where the key is the name of the BlockchainMember and
    the values are the facts for that BlockchainMember.
  returned: always
  type: complex
  contains:
    location:
      description:
        - The GEO location of the blockchain service.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - >-
          Tags of the service which is a list of key value pairs that describes
          the resource.
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - Gets or sets the blockchain member Sku.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Gets or sets Sku name
          returned: always
          type: str
          sample: null
        tier:
          description:
            - Gets or sets Sku tier
          returned: always
          type: str
          sample: null
    protocol:
      description:
        - Gets or sets the blockchain protocol.
      returned: always
      type: str
      sample: null
    validator_nodes_sku:
      description:
        - Gets or sets the blockchain validator nodes Sku.
      returned: always
      type: dict
      sample: null
      contains:
        capacity:
          description:
            - Gets or sets the nodes capacity.
          returned: always
          type: integer
          sample: null
    provisioning_state:
      description:
        - Gets or sets the blockchain member provision state.
      returned: always
      type: str
      sample: null
    dns:
      description:
        - Gets the dns endpoint of the blockchain member.
      returned: always
      type: str
      sample: null
    user_name:
      description:
        - Gets the auth user name of the blockchain member.
      returned: always
      type: str
      sample: null
    password:
      description:
        - Sets the basic auth password of the blockchain member.
      returned: always
      type: str
      sample: null
    consortium:
      description:
        - Gets or sets the consortium for the blockchain member.
      returned: always
      type: str
      sample: null
    consortium_management_account_address:
      description:
        - Gets the managed consortium management account address.
      returned: always
      type: str
      sample: null
    consortium_management_account_password:
      description:
        - Sets the managed consortium management account password.
      returned: always
      type: str
      sample: null
    consortium_role:
      description:
        - Gets the role of the member in the consortium.
      returned: always
      type: str
      sample: null
    consortium_member_display_name:
      description:
        - Gets the display name of the member in the consortium.
      returned: always
      type: str
      sample: null
    root_contract_address:
      description:
        - Gets the Ethereum root contract address of the blockchain.
      returned: always
      type: str
      sample: null
    public_key:
      description:
        - >-
          Gets the public key of the blockchain member (default transaction
          node).
      returned: always
      type: str
      sample: null
    firewall_rules:
      description:
        - Gets or sets firewall rules
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
        - |-
          Gets or sets the collection of blockchain members.
          Gets or sets the collection of consortiums.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - Gets or sets the blockchain member Sku.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Gets or sets Sku name
              returned: always
              type: str
              sample: null
            tier:
              description:
                - Gets or sets Sku tier
              returned: always
              type: str
              sample: null
        protocol:
          description:
            - Gets or sets the blockchain protocol.
          returned: always
          type: str
          sample: null
        validator_nodes_sku:
          description:
            - Gets or sets the blockchain validator nodes Sku.
          returned: always
          type: dict
          sample: null
          contains:
            capacity:
              description:
                - Gets or sets the nodes capacity.
              returned: always
              type: integer
              sample: null
        provisioning_state:
          description:
            - Gets or sets the blockchain member provision state.
          returned: always
          type: str
          sample: null
        dns:
          description:
            - Gets the dns endpoint of the blockchain member.
          returned: always
          type: str
          sample: null
        user_name:
          description:
            - Gets the auth user name of the blockchain member.
          returned: always
          type: str
          sample: null
        password:
          description:
            - Sets the basic auth password of the blockchain member.
          returned: always
          type: str
          sample: null
        consortium:
          description:
            - Gets or sets the consortium for the blockchain member.
          returned: always
          type: str
          sample: null
        consortium_management_account_address:
          description:
            - Gets the managed consortium management account address.
          returned: always
          type: str
          sample: null
        consortium_management_account_password:
          description:
            - Sets the managed consortium management account password.
          returned: always
          type: str
          sample: null
        consortium_role:
          description:
            - Gets the role of the member in the consortium.
          returned: always
          type: str
          sample: null
        consortium_member_display_name:
          description:
            - Gets the display name of the member in the consortium.
          returned: always
          type: str
          sample: null
        root_contract_address:
          description:
            - Gets the Ethereum root contract address of the blockchain.
          returned: always
          type: str
          sample: null
        public_key:
          description:
            - >-
              Gets the public key of the blockchain member (default transaction
              node).
          returned: always
          type: str
          sample: null
        firewall_rules:
          description:
            - Gets or sets firewall rules
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


class AzureRMBlockchainMemberInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            blockchain_member_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            )
        )

        self.blockchain_member_name = None
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
        super(AzureRMBlockchainMemberInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BlockchainManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.blockchain_member_name is not None and
            self.resource_group_name is not None):
            self.results['blockchain_members'] = self.format_item(self.get())
        elif (self.blockchain_member_name is not None and
              self.resource_group_name is not None):
            self.results['blockchain_members'] = self.format_item(self.listconsortiummember())
        elif (self.resource_group_name is not None):
            self.results['blockchain_members'] = self.format_item(self.list())
        else:
            self.results['blockchain_members'] = self.format_item(self.listall())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.blockchain_members.get(blockchain_member_name=self.blockchain_member_name,
                                                               resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listconsortiummember(self):
        response = None

        try:
            response = self.mgmt_client.blockchain_members.list_consortium_member(blockchain_member_name=self.blockchain_member_name,
                                                                                  resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.blockchain_members.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.blockchain_members.list_all()
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
    AzureRMBlockchainMemberInfo()


if __name__ == '__main__':
    main()
