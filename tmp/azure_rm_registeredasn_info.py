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
module: azure_rm_registeredasn_info
version_added: '2.9'
short_description: Get RegisteredAsn info.
description:
  - Get info of RegisteredAsn.
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
  registered_asn_name:
    description:
      - The name of the registered ASN.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a registered ASN associated with the peering
      azure_rm_registeredasn_info: 
        peering_name: peeringName
        registered_asn_name: registeredAsnName0
        resource_group_name: rgName
        

    - name: List all the registered ASNs associated with the peering
      azure_rm_registeredasn_info: 
        peering_name: peeringName
        resource_group_name: rgName
        

'''

RETURN = '''
registered_asns:
  description: >-
    A list of dict results where the key is the name of the RegisteredAsn and
    the values are the facts for that RegisteredAsn.
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
    asn:
      description:
        - The customer's ASN from which traffic originates.
      returned: always
      type: integer
      sample: null
    peering_service_prefix_key:
      description:
        - The peering service prefix key that is to be shared with the customer.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of peering registered ASNs.
      returned: always
      type: list
      sample: null
      contains:
        asn:
          description:
            - The customer's ASN from which traffic originates.
          returned: always
          type: integer
          sample: null
        peering_service_prefix_key:
          description:
            - >-
              The peering service prefix key that is to be shared with the
              customer.
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
        - The link to fetch the next page of peering registered ASNs.
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


class AzureRMRegisteredAsnInfo(AzureRMModuleBase):
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
            registered_asn_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.peering_name = None
        self.registered_asn_name = None

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
        super(AzureRMRegisteredAsnInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.peering_name is not None and
            self.registered_asn_name is not None):
            self.results['registered_asns'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.peering_name is not None):
            self.results['registered_asns'] = self.format_item(self.listbypeering())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.registered_asns.get(resource_group_name=self.resource_group_name,
                                                            peering_name=self.peering_name,
                                                            registered_asn_name=self.registered_asn_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbypeering(self):
        response = None

        try:
            response = self.mgmt_client.registered_asns.list_by_peering(resource_group_name=self.resource_group_name,
                                                                        peering_name=self.peering_name)
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
    AzureRMRegisteredAsnInfo()


if __name__ == '__main__':
    main()
