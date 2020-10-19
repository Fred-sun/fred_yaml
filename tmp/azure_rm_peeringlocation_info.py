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
module: azure_rm_peeringlocation_info
version_added: '2.9'
short_description: Get PeeringLocation info.
description:
  - Get info of PeeringLocation.
options:
  kind:
    description:
      - The kind of the peering.
    required: true
    type: str
    choices:
      - Direct
      - Exchange
  direct_peering_type:
    description:
      - The type of direct peering.
    required: true
    type: str
    choices:
      - Edge
      - Transit
      - Cdn
      - Internal
      - Ix
      - IxRs
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List direct peering locations
      azure_rm_peeringlocation_info: 
        kind: Direct
        

    - name: List exchange peering locations
      azure_rm_peeringlocation_info: 
        kind: Exchange
        

'''

RETURN = '''
peering_locations:
  description: >-
    A list of dict results where the key is the name of the PeeringLocation and
    the values are the facts for that PeeringLocation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of peering locations.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - The kind of peering that the peering location supports.
          returned: always
          type: str
          sample: null
        direct:
          description:
            - The properties that define a direct peering location.
          returned: always
          type: dict
          sample: null
          contains:
            peering_facilities:
              description:
                - The list of direct peering facilities at the peering location.
              returned: always
              type: list
              sample: null
              contains:
                address:
                  description:
                    - The address of the direct peering facility.
                  returned: always
                  type: str
                  sample: null
                direct_peering_type:
                  description:
                    - The type of the direct peering.
                  returned: always
                  type: str
                  sample: null
                peering_dbfacility_id:
                  description:
                    - The PeeringDB.com ID of the facility.
                  returned: always
                  type: integer
                  sample: null
                peering_dbfacility_link:
                  description:
                    - The PeeringDB.com URL of the facility.
                  returned: always
                  type: str
                  sample: null
            bandwidth_offers:
              description:
                - >-
                  The list of bandwidth offers available at the peering
                  location.
              returned: always
              type: list
              sample: null
              contains:
                offer_name:
                  description:
                    - The name of the bandwidth offer.
                  returned: always
                  type: str
                  sample: null
                value_in_mbps:
                  description:
                    - The value of the bandwidth offer in Mbps.
                  returned: always
                  type: integer
                  sample: null
        exchange:
          description:
            - The properties that define an exchange peering location.
          returned: always
          type: dict
          sample: null
          contains:
            peering_facilities:
              description:
                - >-
                  The list of exchange peering facilities at the peering
                  location.
              returned: always
              type: list
              sample: null
              contains:
                exchange_name:
                  description:
                    - The name of the exchange peering facility.
                  returned: always
                  type: str
                  sample: null
                bandwidth_in_mbps:
                  description:
                    - >-
                      The bandwidth of the connection between Microsoft and the
                      exchange peering facility.
                  returned: always
                  type: integer
                  sample: null
                microsoft_ipv4address:
                  description:
                    - >-
                      The IPv4 address of Microsoft at the exchange peering
                      facility.
                  returned: always
                  type: str
                  sample: null
                microsoft_ipv6address:
                  description:
                    - >-
                      The IPv6 address of Microsoft at the exchange peering
                      facility.
                  returned: always
                  type: str
                  sample: null
                facility_ipv4prefix:
                  description:
                    - >-
                      The IPv4 prefixes associated with the exchange peering
                      facility.
                  returned: always
                  type: str
                  sample: null
                facility_ipv6prefix:
                  description:
                    - >-
                      The IPv6 prefixes associated with the exchange peering
                      facility.
                  returned: always
                  type: str
                  sample: null
                peering_dbfacility_id:
                  description:
                    - The PeeringDB.com ID of the facility.
                  returned: always
                  type: integer
                  sample: null
                peering_dbfacility_link:
                  description:
                    - The PeeringDB.com URL of the facility.
                  returned: always
                  type: str
                  sample: null
        peering_location:
          description:
            - The name of the peering location.
          returned: always
          type: str
          sample: null
        country:
          description:
            - The country in which the peering location exists.
          returned: always
          type: str
          sample: null
        azure_region:
          description:
            - The Azure region associated with the peering location.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link to fetch the next page of peering locations.
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


class AzureRMPeeringLocationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            kind=dict(
                type='str',
                choices=['Direct',
                         'Exchange'],
                required=True
            ),
            direct_peering_type=dict(
                type='str',
                choices=['Edge',
                         'Transit',
                         'Cdn',
                         'Internal',
                         'Ix',
                         'IxRs'],
                required=True
            )
        )

        self.kind = None
        self.direct_peering_type = None

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
        super(AzureRMPeeringLocationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.kind is not None):
            self.results['peering_locations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.peering_locations.list(kind=self.kind,
                                                               direct_peering_type=self.direct_peering_type)
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
    AzureRMPeeringLocationInfo()


if __name__ == '__main__':
    main()
