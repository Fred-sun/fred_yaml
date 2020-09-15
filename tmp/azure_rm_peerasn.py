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
module: azure_rm_peerasn
version_added: '2.9'
short_description: Manage Azure PeerAsn instance.
description:
  - 'Create, update and delete instance of Azure PeerAsn.'
options:
  peer_asn_name:
    description:
      - The peer ASN name.
    required: true
    type: str
  peer_asn:
    description:
      - The Autonomous System Number (ASN) of the peer.
    type: integer
  peer_contact_detail:
    description:
      - The contact details of the peer.
    type: list
    suboptions:
      role:
        description:
          - The role of the contact.
        type: str
        choices:
          - Noc
          - Policy
          - Technical
          - Service
          - Escalation
          - Other
      email:
        description:
          - The e-mail address of the contact.
        type: str
      phone:
        description:
          - The phone number of the contact.
        type: str
  peer_name:
    description:
      - The name of the peer.
    type: str
  validation_state:
    description:
      - The validation state of the ASN associated with the peer.
    type: str
    choices:
      - None
      - Pending
      - Approved
      - Failed
  state:
    description:
      - Assert the state of the PeerAsn.
      - >-
        Use C(present) to create or update an PeerAsn and C(absent) to delete
        it.
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
    - name: Create a peer ASN
      azure_rm_peerasn: 
        peer_asn:
          properties:
            peer_asn: 65000
            peer_contact_detail:
              - email: noc@contoso.com
                phone: +1 (234) 567-8999
                role: Noc
              - email: abc@contoso.com
                phone: +1 (234) 567-8900
                role: Policy
              - email: xyz@contoso.com
                phone: +1 (234) 567-8900
                role: Technical
            peer_name: Contoso
        peer_asn_name: peerAsnName
        

    - name: Delete a peer ASN
      azure_rm_peerasn: 
        peer_asn_name: peerAsnName
        

'''

RETURN = '''
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
id:
  description:
    - The ID of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
peer_asn:
  description:
    - The Autonomous System Number (ASN) of the peer.
  returned: always
  type: integer
  sample: null
peer_contact_detail:
  description:
    - The contact details of the peer.
  returned: always
  type: list
  sample: null
  contains:
    role:
      description:
        - The role of the contact.
      returned: always
      type: str
      sample: null
    email:
      description:
        - The e-mail address of the contact.
      returned: always
      type: str
      sample: null
    phone:
      description:
        - The phone number of the contact.
      returned: always
      type: str
      sample: null
peer_name:
  description:
    - The name of the peer.
  returned: always
  type: str
  sample: null
validation_state:
  description:
    - The validation state of the ASN associated with the peer.
  returned: always
  type: str
  sample: null
error_message:
  description:
    - The error message for the validation state
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
    from azure.mgmt.peering import PeeringManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPeerAsn(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            peer_asn_name=dict(
                type='str',
                required=True
            ),
            peer_asn=dict(
                type='integer',
                disposition='/peer_asn'
            ),
            peer_contact_detail=dict(
                type='list',
                disposition='/peer_contact_detail',
                elements='dict',
                options=dict(
                    role=dict(
                        type='str',
                        disposition='role',
                        choices=['Noc',
                                 'Policy',
                                 'Technical',
                                 'Service',
                                 'Escalation',
                                 'Other']
                    ),
                    email=dict(
                        type='str',
                        disposition='email'
                    ),
                    phone=dict(
                        type='str',
                        disposition='phone'
                    )
                )
            ),
            peer_name=dict(
                type='str',
                disposition='/peer_name'
            ),
            validation_state=dict(
                type='str',
                disposition='/validation_state',
                choices=['None',
                         'Pending',
                         'Approved',
                         'Failed']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.peer_asn_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPeerAsn, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

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
            response = self.mgmt_client.peer_asns.create_or_update(peer_asn_name=self.peer_asn_name,
                                                                   peer_asn=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PeerAsn instance.')
            self.fail('Error creating the PeerAsn instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.peer_asns.delete(peer_asn_name=self.peer_asn_name)
        except CloudError as e:
            self.log('Error attempting to delete the PeerAsn instance.')
            self.fail('Error deleting the PeerAsn instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.peer_asns.get(peer_asn_name=self.peer_asn_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPeerAsn()


if __name__ == '__main__':
    main()
