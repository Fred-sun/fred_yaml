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
module: azure_rm_legacypeering_info
version_added: '2.9'
short_description: Get LegacyPeering info.
description:
  - Get info of LegacyPeering.
options:
  peering_location:
    description:
      - The location of the peering.
    required: true
    type: str
  kind:
    description:
      - The kind of the peering.
    required: true
    type: str
    choices:
      - Direct
      - Exchange
  asn:
    description:
      - The ASN number associated with a legacy peering.
    required: true
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List legacy peerings
      azure_rm_legacypeering_info: 
        kind: Exchange
        peering_location: peeringLocation0
        

'''

RETURN = '''
legacy_peerings:
  description: >-
    A list of dict results where the key is the name of the LegacyPeering and
    the values are the facts for that LegacyPeering.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of peerings.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - The SKU that defines the tier and kind of the peering.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The name of the peering SKU.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - The tier of the peering SKU.
              returned: always
              type: str
              sample: null
            family:
              description:
                - The family of the peering SKU.
              returned: always
              type: str
              sample: null
            size:
              description:
                - The size of the peering SKU.
              returned: always
              type: str
              sample: null
        kind:
          description:
            - The kind of the peering.
          returned: always
          type: str
          sample: null
        location:
          description:
            - The location of the resource.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - The resource tags.
          returned: always
          type: dictionary
          sample: null
        direct:
          description:
            - The properties that define a direct peering.
          returned: always
          type: dict
          sample: null
          contains:
            connections:
              description:
                - The set of connections that constitute a direct peering.
              returned: always
              type: list
              sample: null
              contains:
                bandwidth_in_mbps:
                  description:
                    - The bandwidth of the connection.
                  returned: always
                  type: integer
                  sample: null
                provisioned_bandwidth_in_mbps:
                  description:
                    - The bandwidth that is actually provisioned.
                  returned: always
                  type: integer
                  sample: null
                session_address_provider:
                  description:
                    - >-
                      The field indicating if Microsoft provides session ip
                      addresses.
                  returned: always
                  type: str
                  sample: null
                use_for_peering_service:
                  description:
                    - >-
                      The flag that indicates whether or not the connection is
                      used for peering service.
                  returned: always
                  type: bool
                  sample: null
                peering_dbfacility_id:
                  description:
                    - >-
                      The PeeringDB.com ID of the facility at which the
                      connection has to be set up.
                  returned: always
                  type: integer
                  sample: null
                connection_state:
                  description:
                    - The state of the connection.
                  returned: always
                  type: str
                  sample: null
                bgp_session:
                  description:
                    - The BGP session associated with the connection.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    session_prefix_v4:
                      description:
                        - >-
                          The IPv4 prefix that contains both ends' IPv4
                          addresses.
                      returned: always
                      type: str
                      sample: null
                    session_prefix_v6:
                      description:
                        - >-
                          The IPv6 prefix that contains both ends' IPv6
                          addresses.
                      returned: always
                      type: str
                      sample: null
                    microsoft_session_ipv4address:
                      description:
                        - The IPv4 session address on Microsoft's end.
                      returned: always
                      type: str
                      sample: null
                    microsoft_session_ipv6address:
                      description:
                        - The IPv6 session address on Microsoft's end.
                      returned: always
                      type: str
                      sample: null
                    peer_session_ipv4address:
                      description:
                        - The IPv4 session address on peer's end.
                      returned: always
                      type: str
                      sample: null
                    peer_session_ipv6address:
                      description:
                        - The IPv6 session address on peer's end.
                      returned: always
                      type: str
                      sample: null
                    session_state_v4:
                      description:
                        - The state of the IPv4 session.
                      returned: always
                      type: str
                      sample: null
                    session_state_v6:
                      description:
                        - The state of the IPv6 session.
                      returned: always
                      type: str
                      sample: null
                    max_prefixes_advertised_v4:
                      description:
                        - >-
                          The maximum number of prefixes advertised over the
                          IPv4 session.
                      returned: always
                      type: integer
                      sample: null
                    max_prefixes_advertised_v6:
                      description:
                        - >-
                          The maximum number of prefixes advertised over the
                          IPv6 session.
                      returned: always
                      type: integer
                      sample: null
                    md5authentication_key:
                      description:
                        - The MD5 authentication key of the session.
                      returned: always
                      type: str
                      sample: null
                connection_identifier:
                  description:
                    - The unique identifier (GUID) for the connection.
                  returned: always
                  type: str
                  sample: null
                error_message:
                  description:
                    - 'The error message related to the connection state, if any.'
                  returned: always
                  type: str
                  sample: null
            use_for_peering_service:
              description:
                - >-
                  The flag that indicates whether or not the peering is used for
                  peering service.
              returned: always
              type: bool
              sample: null
            peer_asn:
              description:
                - The reference of the peer ASN.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - The identifier of the referenced resource.
                  returned: always
                  type: str
                  sample: null
            direct_peering_type:
              description:
                - The type of direct peering.
              returned: always
              type: str
              sample: null
        exchange:
          description:
            - The properties that define an exchange peering.
          returned: always
          type: dict
          sample: null
          contains:
            connections:
              description:
                - The set of connections that constitute an exchange peering.
              returned: always
              type: list
              sample: null
              contains:
                peering_dbfacility_id:
                  description:
                    - >-
                      The PeeringDB.com ID of the facility at which the
                      connection has to be set up.
                  returned: always
                  type: integer
                  sample: null
                connection_state:
                  description:
                    - The state of the connection.
                  returned: always
                  type: str
                  sample: null
                bgp_session:
                  description:
                    - The BGP session associated with the connection.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    session_prefix_v4:
                      description:
                        - >-
                          The IPv4 prefix that contains both ends' IPv4
                          addresses.
                      returned: always
                      type: str
                      sample: null
                    session_prefix_v6:
                      description:
                        - >-
                          The IPv6 prefix that contains both ends' IPv6
                          addresses.
                      returned: always
                      type: str
                      sample: null
                    microsoft_session_ipv4address:
                      description:
                        - The IPv4 session address on Microsoft's end.
                      returned: always
                      type: str
                      sample: null
                    microsoft_session_ipv6address:
                      description:
                        - The IPv6 session address on Microsoft's end.
                      returned: always
                      type: str
                      sample: null
                    peer_session_ipv4address:
                      description:
                        - The IPv4 session address on peer's end.
                      returned: always
                      type: str
                      sample: null
                    peer_session_ipv6address:
                      description:
                        - The IPv6 session address on peer's end.
                      returned: always
                      type: str
                      sample: null
                    session_state_v4:
                      description:
                        - The state of the IPv4 session.
                      returned: always
                      type: str
                      sample: null
                    session_state_v6:
                      description:
                        - The state of the IPv6 session.
                      returned: always
                      type: str
                      sample: null
                    max_prefixes_advertised_v4:
                      description:
                        - >-
                          The maximum number of prefixes advertised over the
                          IPv4 session.
                      returned: always
                      type: integer
                      sample: null
                    max_prefixes_advertised_v6:
                      description:
                        - >-
                          The maximum number of prefixes advertised over the
                          IPv6 session.
                      returned: always
                      type: integer
                      sample: null
                    md5authentication_key:
                      description:
                        - The MD5 authentication key of the session.
                      returned: always
                      type: str
                      sample: null
                connection_identifier:
                  description:
                    - The unique identifier (GUID) for the connection.
                  returned: always
                  type: str
                  sample: null
                error_message:
                  description:
                    - 'The error message related to the connection state, if any.'
                  returned: always
                  type: str
                  sample: null
            peer_asn:
              description:
                - The reference of the peer ASN.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - The identifier of the referenced resource.
                  returned: always
                  type: str
                  sample: null
        peering_location:
          description:
            - The location of the peering.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state of the resource.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link to fetch the next page of peerings.
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


class AzureRMLegacyPeeringInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            peering_location=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='str',
                choices=['Direct',
                         'Exchange'],
                required=True
            ),
            asn=dict(
                type='integer',
                required=True
            )
        )

        self.peering_location = None
        self.kind = None
        self.asn = None

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
        super(AzureRMLegacyPeeringInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.peering_location is not None and
            self.kind is not None):
            self.results['legacy_peerings'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.legacy_peerings.list(peering_location=self.peering_location,
                                                             kind=self.kind,
                                                             asn=self.asn)
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
    AzureRMLegacyPeeringInfo()


if __name__ == '__main__':
    main()
