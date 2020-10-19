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
module: azure_rm_region_info
version_added: '2.9'
short_description: Get Region info.
description:
  - Get info of Region.
options:
  sku:
    description:
      - The sku type.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RegionsListBySku
      azure_rm_region_info: 
        sku: Basic
        

'''

RETURN = '''
regions:
  description: >-
    A list of dict results where the key is the name of the Region and the
    values are the facts for that Region.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Result of the List PremiumMessagingRegions type.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - Region code
              returned: always
              type: str
              sample: null
            full_name:
              description:
                - Full name of the region
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of PremiumMessagingRegions.
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
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRegionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            sku=dict(
                type='str',
                required=True
            )
        )

        self.sku = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRegionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.sku is not None):
            self.results['regions'] = self.format_item(self.listbysku())
        return self.results

    def listbysku(self):
        response = None

        try:
            response = self.mgmt_client.regions.list_by_sku(sku=self.sku)
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
    AzureRMRegionInfo()


if __name__ == '__main__':
    main()
