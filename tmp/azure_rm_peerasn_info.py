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
module: azure_rm_peerasn_info
version_added: '2.9'
short_description: Get PeerAsn info.
description:
  - Get info of PeerAsn.
options:
  peer_asn_name:
    description:
      - The peer ASN name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a peer ASN
      azure_rm_peerasn_info: 
        peer_asn_name: peerAsnName
        

    - name: List peer ASNs in a subscription
      azure_rm_peerasn_info: 
        {}
        

'''

RETURN = '''
peer_asns:
  description: >-
    A list of dict results where the key is the name of the PeerAsn and the
    values are the facts for that PeerAsn.
  returned: always
  type: complex
  contains:
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
    value:
      description:
        - The list of peer ASNs.
      returned: always
      type: list
      sample: null
      contains:
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
    next_link:
      description:
        - The link to fetch the next page of peer ASNs.
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
    from azure.mgmt.peering import PeeringManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPeerAsnInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            peer_asn_name=dict(
                type='str'
            )
        )

        self.peer_asn_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPeerAsnInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.peer_asn_name is not None):
            self.results['peer_asns'] = self.format_item(self.get())
        else:
            self.results['peer_asns'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.peer_asns.get(peer_asn_name=self.peer_asn_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.peer_asns.list_by_subscription()
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
    AzureRMPeerAsnInfo()


if __name__ == '__main__':
    main()
