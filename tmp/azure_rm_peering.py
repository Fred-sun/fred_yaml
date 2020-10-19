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
module: azure_rm_peering
version_added: '2.9'
short_description: Manage Azure Peering instance.
description:
  - 'Create, update and delete instance of Azure Peering.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  peering_name:
    description:
      - The name of the peering.
    required: true
    type: str
  sku:
    description:
      - The SKU that defines the tier and kind of the peering.
    type: dict
    suboptions:
      name:
        description:
          - The name of the peering SKU.
        type: str
      tier:
        description:
          - The tier of the peering SKU.
        type: str
        choices:
          - Basic
          - Premium
      family:
        description:
          - The family of the peering SKU.
        type: str
        choices:
          - Direct
          - Exchange
      size:
        description:
          - The size of the peering SKU.
        type: str
        choices:
          - Free
          - Metered
          - Unlimited
  kind:
    description:
      - The kind of the peering.
    type: str
    choices:
      - Direct
      - Exchange
  location:
    description:
      - The location of the resource.
    type: str
  direct:
    description:
      - The properties that define a direct peering.
    type: dict
    suboptions:
      connections:
        description:
          - The set of connections that constitute a direct peering.
        type: list
        suboptions:
          bandwidth_in_mbps:
            description:
              - The bandwidth of the connection.
            type: integer
          provisioned_bandwidth_in_mbps:
            description:
              - The bandwidth that is actually provisioned.
            type: integer
          session_address_provider:
            description:
              - The field indicating if Microsoft provides session ip addresses.
            type: str
            choices:
              - Microsoft
              - Peer
          use_for_peering_service:
            description:
              - >-
                The flag that indicates whether or not the connection is used
                for peering service.
            type: bool
          peering_dbfacility_id:
            description:
              - >-
                The PeeringDB.com ID of the facility at which the connection has
                to be set up.
            type: integer
          connection_state:
            description:
              - The state of the connection.
            type: str
            choices:
              - None
              - PendingApproval
              - Approved
              - ProvisioningStarted
              - ProvisioningFailed
              - ProvisioningCompleted
              - Validating
              - Active
          bgp_session:
            description:
              - The BGP session associated with the connection.
            type: dict
            suboptions:
              session_prefix_v4:
                description:
                  - The IPv4 prefix that contains both ends' IPv4 addresses.
                type: str
              session_prefix_v6:
                description:
                  - The IPv6 prefix that contains both ends' IPv6 addresses.
                type: str
              microsoft_session_ipv4address:
                description:
                  - The IPv4 session address on Microsoft's end.
                type: str
              microsoft_session_ipv6address:
                description:
                  - The IPv6 session address on Microsoft's end.
                type: str
              peer_session_ipv4address:
                description:
                  - The IPv4 session address on peer's end.
                type: str
              peer_session_ipv6address:
                description:
                  - The IPv6 session address on peer's end.
                type: str
              session_state_v4:
                description:
                  - The state of the IPv4 session.
                type: str
                choices:
                  - None
                  - Idle
                  - Connect
                  - Active
                  - OpenSent
                  - OpenConfirm
                  - OpenReceived
                  - Established
                  - PendingAdd
                  - PendingUpdate
                  - PendingRemove
              session_state_v6:
                description:
                  - The state of the IPv6 session.
                type: str
                choices:
                  - None
                  - Idle
                  - Connect
                  - Active
                  - OpenSent
                  - OpenConfirm
                  - OpenReceived
                  - Established
                  - PendingAdd
                  - PendingUpdate
                  - PendingRemove
              max_prefixes_advertised_v4:
                description:
                  - >-
                    The maximum number of prefixes advertised over the IPv4
                    session.
                type: integer
              max_prefixes_advertised_v6:
                description:
                  - >-
                    The maximum number of prefixes advertised over the IPv6
                    session.
                type: integer
              md5authentication_key:
                description:
                  - The MD5 authentication key of the session.
                type: str
          connection_identifier:
            description:
              - The unique identifier (GUID) for the connection.
            type: str
          error_message:
            description:
              - 'The error message related to the connection state, if any.'
            type: str
      use_for_peering_service:
        description:
          - >-
            The flag that indicates whether or not the peering is used for
            peering service.
        type: bool
      peer_asn:
        description:
          - The reference of the peer ASN.
        type: dict
        suboptions:
          id:
            description:
              - The identifier of the referenced resource.
            type: str
      direct_peering_type:
        description:
          - The type of direct peering.
        type: str
        choices:
          - Edge
          - Transit
          - Cdn
          - Internal
          - Ix
          - IxRs
  exchange:
    description:
      - The properties that define an exchange peering.
    type: dict
    suboptions:
      connections:
        description:
          - The set of connections that constitute an exchange peering.
        type: list
        suboptions:
          peering_dbfacility_id:
            description:
              - >-
                The PeeringDB.com ID of the facility at which the connection has
                to be set up.
            type: integer
          connection_state:
            description:
              - The state of the connection.
            type: str
            choices:
              - None
              - PendingApproval
              - Approved
              - ProvisioningStarted
              - ProvisioningFailed
              - ProvisioningCompleted
              - Validating
              - Active
          bgp_session:
            description:
              - The BGP session associated with the connection.
            type: dict
            suboptions:
              session_prefix_v4:
                description:
                  - The IPv4 prefix that contains both ends' IPv4 addresses.
                type: str
              session_prefix_v6:
                description:
                  - The IPv6 prefix that contains both ends' IPv6 addresses.
                type: str
              microsoft_session_ipv4address:
                description:
                  - The IPv4 session address on Microsoft's end.
                type: str
              microsoft_session_ipv6address:
                description:
                  - The IPv6 session address on Microsoft's end.
                type: str
              peer_session_ipv4address:
                description:
                  - The IPv4 session address on peer's end.
                type: str
              peer_session_ipv6address:
                description:
                  - The IPv6 session address on peer's end.
                type: str
              session_state_v4:
                description:
                  - The state of the IPv4 session.
                type: str
                choices:
                  - None
                  - Idle
                  - Connect
                  - Active
                  - OpenSent
                  - OpenConfirm
                  - OpenReceived
                  - Established
                  - PendingAdd
                  - PendingUpdate
                  - PendingRemove
              session_state_v6:
                description:
                  - The state of the IPv6 session.
                type: str
                choices:
                  - None
                  - Idle
                  - Connect
                  - Active
                  - OpenSent
                  - OpenConfirm
                  - OpenReceived
                  - Established
                  - PendingAdd
                  - PendingUpdate
                  - PendingRemove
              max_prefixes_advertised_v4:
                description:
                  - >-
                    The maximum number of prefixes advertised over the IPv4
                    session.
                type: integer
              max_prefixes_advertised_v6:
                description:
                  - >-
                    The maximum number of prefixes advertised over the IPv6
                    session.
                type: integer
              md5authentication_key:
                description:
                  - The MD5 authentication key of the session.
                type: str
          connection_identifier:
            description:
              - The unique identifier (GUID) for the connection.
            type: str
          error_message:
            description:
              - 'The error message related to the connection state, if any.'
            type: str
      peer_asn:
        description:
          - The reference of the peer ASN.
        type: dict
        suboptions:
          id:
            description:
              - The identifier of the referenced resource.
            type: str
  peering_location:
    description:
      - The location of the peering.
    type: str
  state:
    description:
      - Assert the state of the Peering.
      - >-
        Use C(present) to create or update an Peering and C(absent) to delete
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
    - name: Create a direct peering
      azure_rm_peering: 
        peering_name: peeringName
        resource_group_name: rgName
        kind: Direct
        location: eastus
        properties:
          direct:
            connections:
              - bandwidth_in_mbps: 10000
                bgp_session:
                  max_prefixes_advertised_v4: 1000
                  max_prefixes_advertised_v6: 100
                  md5authentication_key: test-md5-auth-key
                  session_prefix_v4: 192.168.0.0/31
                  session_prefix_v6: 'fd00::0/127'
                connection_identifier: 5F4CB5C7-6B43-4444-9338-9ABC72606C16
                peering_dbfacility_id: 99999
                session_address_provider: Peer
                use_for_peering_service: false
              - bandwidth_in_mbps: 10000
                connection_identifier: 8AB00818-D533-4504-A25A-03A17F61201C
                peering_dbfacility_id: 99999
                session_address_provider: Microsoft
                use_for_peering_service: true
            direct_peering_type: Edge
            peer_asn:
              id: /subscriptions/subId/providers/Microsoft.Peering/peerAsns/myAsn1
          peering_location: peeringLocation0
        sku:
          name: Basic_Direct_Free
        

    - name: Create a peering with exchange route server
      azure_rm_peering: 
        peering_name: peeringName
        resource_group_name: rgName
        kind: Direct
        location: eastus
        properties:
          direct:
            connections:
              - bandwidth_in_mbps: 10000
                bgp_session:
                  max_prefixes_advertised_v4: 1000
                  max_prefixes_advertised_v6: 100
                  microsoft_session_ipv4address: 192.168.0.123
                  peer_session_ipv4address: 192.168.0.234
                  session_prefix_v4: 192.168.0.0/24
                connection_identifier: 5F4CB5C7-6B43-4444-9338-9ABC72606C16
                peering_dbfacility_id: 99999
                session_address_provider: Peer
                use_for_peering_service: true
            direct_peering_type: IxRs
            peer_asn:
              id: /subscriptions/subId/providers/Microsoft.Peering/peerAsns/myAsn1
          peering_location: peeringLocation0
        sku:
          name: Premium_Direct_Free
        

    - name: Create an exchange peering
      azure_rm_peering: 
        peering_name: peeringName
        resource_group_name: rgName
        kind: Exchange
        location: eastus
        properties:
          exchange:
            connections:
              - bgp_session:
                  max_prefixes_advertised_v4: 1000
                  max_prefixes_advertised_v6: 100
                  md5authentication_key: test-md5-auth-key
                  peer_session_ipv4address: 192.168.2.1
                  peer_session_ipv6address: 'fd00::1'
                connection_identifier: CE495334-0E94-4E51-8164-8116D6CD284D
                peering_dbfacility_id: 99999
              - bgp_session:
                  max_prefixes_advertised_v4: 1000
                  max_prefixes_advertised_v6: 100
                  md5authentication_key: test-md5-auth-key
                  peer_session_ipv4address: 192.168.2.2
                  peer_session_ipv6address: 'fd00::2'
                connection_identifier: CDD8E673-CB07-47E6-84DE-3739F778762B
                peering_dbfacility_id: 99999
            peer_asn:
              id: /subscriptions/subId/providers/Microsoft.Peering/peerAsns/myAsn1
          peering_location: peeringLocation0
        sku:
          name: Basic_Exchange_Free
        

    - name: Delete a peering
      azure_rm_peering: 
        peering_name: peeringName
        resource_group_name: rgName
        

    - name: Update peering tags
      azure_rm_peering: 
        peering_name: peeringName
        resource_group_name: rgName
        tags:
          tag0: value0
          tag1: value1
        

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
            - The field indicating if Microsoft provides session ip addresses.
          returned: always
          type: str
          sample: null
        use_for_peering_service:
          description:
            - >-
              The flag that indicates whether or not the connection is used for
              peering service.
          returned: always
          type: bool
          sample: null
        peering_dbfacility_id:
          description:
            - >-
              The PeeringDB.com ID of the facility at which the connection has
              to be set up.
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
                - The IPv4 prefix that contains both ends' IPv4 addresses.
              returned: always
              type: str
              sample: null
            session_prefix_v6:
              description:
                - The IPv6 prefix that contains both ends' IPv6 addresses.
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
                  The maximum number of prefixes advertised over the IPv4
                  session.
              returned: always
              type: integer
              sample: null
            max_prefixes_advertised_v6:
              description:
                - >-
                  The maximum number of prefixes advertised over the IPv6
                  session.
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
          The flag that indicates whether or not the peering is used for peering
          service.
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
              The PeeringDB.com ID of the facility at which the connection has
              to be set up.
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
                - The IPv4 prefix that contains both ends' IPv4 addresses.
              returned: always
              type: str
              sample: null
            session_prefix_v6:
              description:
                - The IPv6 prefix that contains both ends' IPv6 addresses.
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
                  The maximum number of prefixes advertised over the IPv4
                  session.
              returned: always
              type: integer
              sample: null
            max_prefixes_advertised_v6:
              description:
                - >-
                  The maximum number of prefixes advertised over the IPv6
                  session.
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


class AzureRMPeering(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            peering_name=dict(
                type='str',
                required=True
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
                        disposition='tier',
                        choices=['Basic',
                                 'Premium']
                    ),
                    family=dict(
                        type='str',
                        disposition='family',
                        choices=['Direct',
                                 'Exchange']
                    ),
                    size=dict(
                        type='str',
                        disposition='size',
                        choices=['Free',
                                 'Metered',
                                 'Unlimited']
                    )
                )
            ),
            kind=dict(
                type='str',
                disposition='/kind',
                choices=['Direct',
                         'Exchange']
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            direct=dict(
                type='dict',
                disposition='/direct',
                options=dict(
                    connections=dict(
                        type='list',
                        disposition='connections',
                        elements='dict',
                        options=dict(
                            bandwidth_in_mbps=dict(
                                type='integer',
                                disposition='bandwidth_in_mbps'
                            ),
                            provisioned_bandwidth_in_mbps=dict(
                                type='integer',
                                updatable=False,
                                disposition='provisioned_bandwidth_in_mbps'
                            ),
                            session_address_provider=dict(
                                type='str',
                                disposition='session_address_provider',
                                choices=['Microsoft',
                                         'Peer']
                            ),
                            use_for_peering_service=dict(
                                type='bool',
                                disposition='use_for_peering_service'
                            ),
                            peering_dbfacility_id=dict(
                                type='integer',
                                disposition='peering_dbfacility_id'
                            ),
                            connection_state=dict(
                                type='str',
                                updatable=False,
                                disposition='connection_state',
                                choices=['None',
                                         'PendingApproval',
                                         'Approved',
                                         'ProvisioningStarted',
                                         'ProvisioningFailed',
                                         'ProvisioningCompleted',
                                         'Validating',
                                         'Active']
                            ),
                            bgp_session=dict(
                                type='dict',
                                disposition='bgp_session',
                                options=dict(
                                    session_prefix_v4=dict(
                                        type='str',
                                        disposition='session_prefix_v4'
                                    ),
                                    session_prefix_v6=dict(
                                        type='str',
                                        disposition='session_prefix_v6'
                                    ),
                                    microsoft_session_ipv4address=dict(
                                        type='str',
                                        disposition='microsoft_session_ipv4address'
                                    ),
                                    microsoft_session_ipv6address=dict(
                                        type='str',
                                        disposition='microsoft_session_ipv6address'
                                    ),
                                    peer_session_ipv4address=dict(
                                        type='str',
                                        disposition='peer_session_ipv4address'
                                    ),
                                    peer_session_ipv6address=dict(
                                        type='str',
                                        disposition='peer_session_ipv6address'
                                    ),
                                    session_state_v4=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='session_state_v4',
                                        choices=['None',
                                                 'Idle',
                                                 'Connect',
                                                 'Active',
                                                 'OpenSent',
                                                 'OpenConfirm',
                                                 'OpenReceived',
                                                 'Established',
                                                 'PendingAdd',
                                                 'PendingUpdate',
                                                 'PendingRemove']
                                    ),
                                    session_state_v6=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='session_state_v6',
                                        choices=['None',
                                                 'Idle',
                                                 'Connect',
                                                 'Active',
                                                 'OpenSent',
                                                 'OpenConfirm',
                                                 'OpenReceived',
                                                 'Established',
                                                 'PendingAdd',
                                                 'PendingUpdate',
                                                 'PendingRemove']
                                    ),
                                    max_prefixes_advertised_v4=dict(
                                        type='integer',
                                        disposition='max_prefixes_advertised_v4'
                                    ),
                                    max_prefixes_advertised_v6=dict(
                                        type='integer',
                                        disposition='max_prefixes_advertised_v6'
                                    ),
                                    md5authentication_key=dict(
                                        type='str',
                                        disposition='md5authentication_key'
                                    )
                                )
                            ),
                            connection_identifier=dict(
                                type='str',
                                disposition='connection_identifier'
                            ),
                            error_message=dict(
                                type='str',
                                updatable=False,
                                disposition='error_message'
                            )
                        )
                    ),
                    use_for_peering_service=dict(
                        type='bool',
                        updatable=False,
                        disposition='use_for_peering_service'
                    ),
                    peer_asn=dict(
                        type='dict',
                        disposition='peer_asn',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    direct_peering_type=dict(
                        type='str',
                        disposition='direct_peering_type',
                        choices=['Edge',
                                 'Transit',
                                 'Cdn',
                                 'Internal',
                                 'Ix',
                                 'IxRs']
                    )
                )
            ),
            exchange=dict(
                type='dict',
                disposition='/exchange',
                options=dict(
                    connections=dict(
                        type='list',
                        disposition='connections',
                        elements='dict',
                        options=dict(
                            peering_dbfacility_id=dict(
                                type='integer',
                                disposition='peering_dbfacility_id'
                            ),
                            connection_state=dict(
                                type='str',
                                updatable=False,
                                disposition='connection_state',
                                choices=['None',
                                         'PendingApproval',
                                         'Approved',
                                         'ProvisioningStarted',
                                         'ProvisioningFailed',
                                         'ProvisioningCompleted',
                                         'Validating',
                                         'Active']
                            ),
                            bgp_session=dict(
                                type='dict',
                                disposition='bgp_session',
                                options=dict(
                                    session_prefix_v4=dict(
                                        type='str',
                                        disposition='session_prefix_v4'
                                    ),
                                    session_prefix_v6=dict(
                                        type='str',
                                        disposition='session_prefix_v6'
                                    ),
                                    microsoft_session_ipv4address=dict(
                                        type='str',
                                        disposition='microsoft_session_ipv4address'
                                    ),
                                    microsoft_session_ipv6address=dict(
                                        type='str',
                                        disposition='microsoft_session_ipv6address'
                                    ),
                                    peer_session_ipv4address=dict(
                                        type='str',
                                        disposition='peer_session_ipv4address'
                                    ),
                                    peer_session_ipv6address=dict(
                                        type='str',
                                        disposition='peer_session_ipv6address'
                                    ),
                                    session_state_v4=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='session_state_v4',
                                        choices=['None',
                                                 'Idle',
                                                 'Connect',
                                                 'Active',
                                                 'OpenSent',
                                                 'OpenConfirm',
                                                 'OpenReceived',
                                                 'Established',
                                                 'PendingAdd',
                                                 'PendingUpdate',
                                                 'PendingRemove']
                                    ),
                                    session_state_v6=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='session_state_v6',
                                        choices=['None',
                                                 'Idle',
                                                 'Connect',
                                                 'Active',
                                                 'OpenSent',
                                                 'OpenConfirm',
                                                 'OpenReceived',
                                                 'Established',
                                                 'PendingAdd',
                                                 'PendingUpdate',
                                                 'PendingRemove']
                                    ),
                                    max_prefixes_advertised_v4=dict(
                                        type='integer',
                                        disposition='max_prefixes_advertised_v4'
                                    ),
                                    max_prefixes_advertised_v6=dict(
                                        type='integer',
                                        disposition='max_prefixes_advertised_v6'
                                    ),
                                    md5authentication_key=dict(
                                        type='str',
                                        disposition='md5authentication_key'
                                    )
                                )
                            ),
                            connection_identifier=dict(
                                type='str',
                                disposition='connection_identifier'
                            ),
                            error_message=dict(
                                type='str',
                                updatable=False,
                                disposition='error_message'
                            )
                        )
                    ),
                    peer_asn=dict(
                        type='dict',
                        disposition='peer_asn',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    )
                )
            ),
            peering_location=dict(
                type='str',
                disposition='/peering_location'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.peering_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPeering, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.peerings.create_or_update(resource_group_name=self.resource_group_name,
                                                                  peering_name=self.peering_name,
                                                                  peering=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Peering instance.')
            self.fail('Error creating the Peering instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.peerings.delete(resource_group_name=self.resource_group_name,
                                                        peering_name=self.peering_name)
        except CloudError as e:
            self.log('Error attempting to delete the Peering instance.')
            self.fail('Error deleting the Peering instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.peerings.get(resource_group_name=self.resource_group_name,
                                                     peering_name=self.peering_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPeering()


if __name__ == '__main__':
    main()
