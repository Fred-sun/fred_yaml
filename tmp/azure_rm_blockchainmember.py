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
module: azure_rm_blockchainmember
version_added: '2.9'
short_description: Manage Azure BlockchainMember instance.
description:
  - 'Create, update and delete instance of Azure BlockchainMember.'
options:
  blockchain_member_name:
    description:
      - Blockchain member name.
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
      - The GEO location of the blockchain service.
    type: str
  sku:
    description:
      - Gets or sets the blockchain member Sku.
    type: dict
    suboptions:
      name:
        description:
          - Gets or sets Sku name
        type: str
      tier:
        description:
          - Gets or sets Sku tier
        type: str
  protocol:
    description:
      - Gets or sets the blockchain protocol.
    type: str
    choices:
      - NotSpecified
      - Parity
      - Quorum
      - Corda
  validator_nodes_sku:
    description:
      - Gets or sets the blockchain validator nodes Sku.
    type: dict
    suboptions:
      capacity:
        description:
          - Gets or sets the nodes capacity.
        type: integer
  password:
    description:
      - Sets the basic auth password of the blockchain member.
      - Sets the transaction node dns endpoint basic auth password.
    type: str
  consortium:
    description:
      - Gets or sets the consortium for the blockchain member.
    type: str
  consortium_management_account_password:
    description:
      - Sets the managed consortium management account password.
    type: str
  consortium_role:
    description:
      - Gets the role of the member in the consortium.
    type: str
  consortium_member_display_name:
    description:
      - Gets the display name of the member in the consortium.
    type: str
  firewall_rules:
    description:
      - Gets or sets firewall rules
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
      - Assert the state of the BlockchainMember.
      - >-
        Use C(present) to create or update an BlockchainMember and C(absent) to
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
    - name: BlockchainMembers_Create
      azure_rm_blockchainmember: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        

    - name: BlockchainMembers_Delete
      azure_rm_blockchainmember: 
        blockchain_member_name: contosemember1
        resource_group_name: mygroup
        

    - name: BlockchainMembers_Update
      azure_rm_blockchainmember: 
        blockchain_member_name: ContoseMember1
        resource_group_name: mygroup
        

'''

RETURN = '''
location:
  description:
    - The GEO location of the blockchain service.
  returned: always
  type: str
  sample: null
tags:
  description:
    - >-
      Tags of the service which is a list of key value pairs that describes the
      resource.
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
    - Gets the public key of the blockchain member (default transaction node).
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


class AzureRMBlockchainMember(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            blockchain_member_name=dict(
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
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    )
                )
            ),
            protocol=dict(
                type='str',
                disposition='/protocol',
                choices=['NotSpecified',
                         'Parity',
                         'Quorum',
                         'Corda']
            ),
            validator_nodes_sku=dict(
                type='dict',
                disposition='/validator_nodes_sku',
                options=dict(
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            password=dict(
                type='str',
                disposition='/password'
            ),
            consortium=dict(
                type='str',
                disposition='/consortium'
            ),
            consortium_management_account_password=dict(
                type='str',
                disposition='/consortium_management_account_password'
            ),
            consortium_role=dict(
                type='str',
                disposition='/consortium_role'
            ),
            consortium_member_display_name=dict(
                type='str',
                disposition='/consortium_member_display_name'
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
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBlockchainMember, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.blockchain_members.create(blockchain_member_name=self.blockchain_member_name,
                                                                      resource_group_name=self.resource_group_name,
                                                                      blockchain_member=self.body)
            else:
                response = self.mgmt_client.blockchain_members.update(blockchain_member_name=self.blockchain_member_name,
                                                                      resource_group_name=self.resource_group_name,
                                                                      blockchain_member=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BlockchainMember instance.')
            self.fail('Error creating the BlockchainMember instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.blockchain_members.delete(blockchain_member_name=self.blockchain_member_name,
                                                                  resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the BlockchainMember instance.')
            self.fail('Error deleting the BlockchainMember instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.blockchain_members.get(blockchain_member_name=self.blockchain_member_name,
                                                               resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBlockchainMember()


if __name__ == '__main__':
    main()
