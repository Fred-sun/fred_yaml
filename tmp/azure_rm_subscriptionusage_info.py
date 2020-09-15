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
module: azure_rm_subscriptionusage_info
version_added: '2.9'
short_description: Get SubscriptionUsage info.
description:
  - Get info of SubscriptionUsage.
options:
  location_name:
    description:
      - The name of the region where the resource is located.
    required: true
    type: str
  usage_name:
    description:
      - Name of usage metric to return.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List subscription usages in the given location.
      azure_rm_subscriptionusage_info: 
        location_name: WestUS
        

    - name: Get specific subscription usage in the given location.
      azure_rm_subscriptionusage_info: 
        location_name: WestUS
        usage_name: ServerQuota
        

'''

RETURN = '''
subscription_usages:
  description: >-
    A list of dict results where the key is the name of the SubscriptionUsage
    and the values are the facts for that SubscriptionUsage.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        display_name:
          description:
            - User-readable name of the metric.
          returned: always
          type: str
          sample: null
        current_value:
          description:
            - Current value of the metric.
          returned: always
          type: number
          sample: null
        limit:
          description:
            - Boundary value of the metric.
          returned: always
          type: number
          sample: null
        unit:
          description:
            - Unit of the metric.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - User-readable name of the metric.
      returned: always
      type: str
      sample: null
    current_value:
      description:
        - Current value of the metric.
      returned: always
      type: number
      sample: null
    limit:
      description:
        - Boundary value of the metric.
      returned: always
      type: number
      sample: null
    unit:
      description:
        - Unit of the metric.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSubscriptionUsageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            usage_name=dict(
                type='str'
            )
        )

        self.location_name = None
        self.usage_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSubscriptionUsageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

        if (self.location_name is not None and
            self.usage_name is not None):
            self.results['subscription_usages'] = self.format_item(self.get())
        elif (self.location_name is not None):
            self.results['subscription_usages'] = self.format_item(self.listbylocation())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.subscription_usages.get(location_name=self.location_name,
                                                                usage_name=self.usage_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.subscription_usages.list_by_location(location_name=self.location_name)
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
    AzureRMSubscriptionUsageInfo()


if __name__ == '__main__':
    main()
