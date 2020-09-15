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
module: azure_rm_sku_info
version_added: '2.9'
short_description: Get Sku info.
description:
  - Get info of Sku.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Skus_List
      azure_rm_sku_info: 
        {}
        

'''

RETURN = '''
skus:
  description: >-
    A list of dict results where the key is the name of the Sku and the values
    are the facts for that Sku.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - The URI to fetch the next page of Cache SKUs.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of SKUs available for the subscription.
      returned: always
      type: list
      sample: null
      contains:
        resource_type:
          description:
            - The type of resource the SKU applies to.
          returned: always
          type: str
          sample: null
        capabilities:
          description:
            - 'A list of capabilities of this SKU, such as throughput or ops/sec.'
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - 'Name of a capability, such as ops/sec.'
              returned: always
              type: str
              sample: null
            value:
              description:
                - 'Quantity, if the capability is measured by quantity.'
              returned: always
              type: str
              sample: null
        locations:
          description:
            - >-
              The set of locations that the SKU is available. This will be
              supported and registered Azure Geo Regions (e.g., West US, East
              US, Southeast Asia, etc.).
          returned: always
          type: list
          sample: null
        location_info:
          description:
            - The set of locations that the SKU is available.
          returned: always
          type: list
          sample: null
          contains:
            location:
              description:
                - Location where this SKU is available.
              returned: always
              type: str
              sample: null
            zones:
              description:
                - Zones if any.
              returned: always
              type: list
              sample: null
        name:
          description:
            - The name of this SKU.
          returned: always
          type: str
          sample: null
        restrictions:
          description:
            - >-
              The restrictions preventing this SKU from being used. This is
              empty if there are no restrictions.
          returned: always
          type: list
          sample: null
          contains:
            type:
              description:
                - >-
                  The type of restrictions. In this version, the only possible
                  value for this is location.
              returned: always
              type: str
              sample: null
            values:
              description:
                - >-
                  The value of restrictions. If the restriction type is set to
                  location, then this would be the different locations where the
                  SKU is restricted.
              returned: always
              type: list
              sample: null
            reason_code:
              description:
                - >-
                  The reason for the restriction. As of now this can be
                  "QuotaId" or "NotAvailableForSubscription". "QuotaId" is set
                  when the SKU has requiredQuotas parameter as the subscription
                  does not belong to that quota. "NotAvailableForSubscription"
                  is related to capacity at the datacenter.
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
    from azure.mgmt.storage import StorageCacheManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSkuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSkuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageCacheManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        else:
            self.results['skus'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.skus.list()
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
    AzureRMSkuInfo()


if __name__ == '__main__':
    main()
