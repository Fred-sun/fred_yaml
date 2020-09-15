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
module: azure_rm_skusavailability_info
version_added: '2.9'
short_description: Get SkusAvailability info.
description:
  - Get info of SkusAvailability.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  sku_id:
    description:
      - 'sku id, if no sku is passed availability for all skus will be returned'
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListAvailabilities
      azure_rm_skusavailability_info: 
        region_id: westus2
        

'''

RETURN = '''
skus_availability:
  description: >-
    A list of dict results where the key is the name of the SkusAvailability and
    the values are the facts for that SkusAvailability.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of DedicatedCloudNode
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the DedicatedPlacementGroupSkuAvailability list
      returned: always
      type: list
      sample: null
      contains:
        dedicated_availability_zone_id:
          description:
            - CloudSimple Availability Zone id
          returned: always
          type: str
          sample: null
        dedicated_availability_zone_name:
          description:
            - CloudSimple Availability Zone Name
          returned: always
          type: str
          sample: null
        dedicated_placement_group_id:
          description:
            - CloudSimple Placement Group Id
          returned: always
          type: str
          sample: null
        dedicated_placement_group_name:
          description:
            - CloudSimple Placement Group name
          returned: always
          type: str
          sample: null
        limit:
          description:
            - >-
              indicates how many resources of a given SKU is available in a
              AZ->PG
          returned: always
          type: integer
          sample: null
        resource_type:
          description:
            - resource type e.g. DedicatedCloudNodes
          returned: always
          type: str
          sample: null
        sku_id:
          description:
            - sku id
          returned: always
          type: str
          sample: null
        sku_name:
          description:
            - sku name
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
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSkusAvailabilityInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=True
            ),
            sku_id=dict(
                type='str',
                required=True
            )
        )

        self.region_id = None
        self.sku_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSkusAvailabilityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.region_id is not None):
            self.results['skus_availability'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.skus_availability.list(region_id=self.region_id,
                                                               sku_id=self.sku_id)
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
    AzureRMSkusAvailabilityInfo()


if __name__ == '__main__':
    main()
