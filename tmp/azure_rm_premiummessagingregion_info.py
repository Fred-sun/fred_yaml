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
module: azure_rm_premiummessagingregion_info
version_added: '2.9'
short_description: Get PremiumMessagingRegion info.
description:
  - Get info of PremiumMessagingRegion.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: PremiumMessagingRegionsList
      azure_rm_premiummessagingregion_info: 
        {}
        

'''

RETURN = '''
premium_messaging_regions:
  description: >-
    A list of dict results where the key is the name of the
    PremiumMessagingRegion and the values are the facts for that
    PremiumMessagingRegion.
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


class AzureRMPremiumMessagingRegionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


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
        super(AzureRMPremiumMessagingRegionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        else:
            self.results['premium_messaging_regions'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.premium_messaging_regions.list()
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
    AzureRMPremiumMessagingRegionInfo()


if __name__ == '__main__':
    main()
