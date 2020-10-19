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
module: azure_rm_receivedroute_info
version_added: '2.9'
short_description: Get ReceivedRoute info.
description:
  - Get info of ReceivedRoute.
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
  prefix:
    description:
      - The optional prefix that can be used to filter the routes.
    required: true
    type: str
  as_path:
    description:
      - The optional AS path that can be used to filter the routes.
    required: true
    type: str
  origin_as_validation_state:
    description:
      - >-
        The optional origin AS validation state that can be used to filter the
        routes.
    required: true
    type: str
  rpki_validation_state:
    description:
      - >-
        The optional RPKI validation state that can be used to filter the
        routes.
    required: true
    type: str
  skip_token:
    description:
      - >-
        The optional page continuation token that is used in the event of
        paginated result.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists the prefixes received over the specified peering under the given subscription and resource group.
      azure_rm_receivedroute_info: 
        as_path: 123 456
        origin_as_validation_state: Valid
        peering_name: peeringName
        prefix: 1.1.1.0/24
        resource_group_name: rgName
        rpki_validation_state: Valid
        

'''

RETURN = '''
received_routes:
  description: >-
    A list of dict results where the key is the name of the ReceivedRoute and
    the values are the facts for that ReceivedRoute.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of received routes for the peering.
      returned: always
      type: list
      sample: null
      contains:
        prefix:
          description:
            - The prefix.
          returned: always
          type: str
          sample: null
        next_hop:
          description:
            - The next hop for the prefix.
          returned: always
          type: str
          sample: null
        as_path:
          description:
            - The AS path for the prefix.
          returned: always
          type: str
          sample: null
        origin_as_validation_state:
          description:
            - The origin AS change information for the prefix.
          returned: always
          type: str
          sample: null
        rpki_validation_state:
          description:
            - >-
              The RPKI validation state for the prefix and origin AS that's
              listed in the AS path.
          returned: always
          type: str
          sample: null
        trust_anchor:
          description:
            - >-
              The authority which holds the Route Origin Authorization record
              for the prefix, if any.
          returned: always
          type: str
          sample: null
        received_timestamp:
          description:
            - The received timestamp associated with the prefix.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link to fetch the next page of received routes for the peering.
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


class AzureRMReceivedRouteInfo(AzureRMModuleBase):
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
            prefix=dict(
                type='str',
                required=True
            ),
            as_path=dict(
                type='str',
                required=True
            ),
            origin_as_validation_state=dict(
                type='str',
                required=True
            ),
            rpki_validation_state=dict(
                type='str',
                required=True
            ),
            skip_token=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.peering_name = None
        self.prefix = None
        self.as_path = None
        self.origin_as_validation_state = None
        self.rpki_validation_state = None
        self.skip_token = None

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
        super(AzureRMReceivedRouteInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.peering_name is not None):
            self.results['received_routes'] = self.format_item(self.listbypeering())
        return self.results

    def listbypeering(self):
        response = None

        try:
            response = self.mgmt_client.received_routes.list_by_peering(resource_group_name=self.resource_group_name,
                                                                        peering_name=self.peering_name,
                                                                        prefix=self.prefix,
                                                                        as_path=self.as_path,
                                                                        origin_as_validation_state=self.origin_as_validation_state,
                                                                        rpki_validation_state=self.rpki_validation_state,
                                                                        skip_token=self.skip_token)
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
    AzureRMReceivedRouteInfo()


if __name__ == '__main__':
    main()
