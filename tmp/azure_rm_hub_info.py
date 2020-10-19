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
module: azure_rm_hub_info
version_added: '2.9'
short_description: Get Hub info.
description:
  - Get info of Hub.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  hub_name:
    description:
      - The name of the hub.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Hubs_Get
      azure_rm_hub_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

    - name: Hubs_ListByResourceGroup
      azure_rm_hub_info: 
        resource_group_name: TestHubRG
        

    - name: Hubs_List
      azure_rm_hub_info: 
        {}
        

'''

RETURN = '''
hubs:
  description: >-
    A list of dict results where the key is the name of the Hub and the values
    are the facts for that Hub.
  returned: always
  type: complex
  contains:
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
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    api_endpoint:
      description:
        - API endpoint URL of the hub.
      returned: always
      type: str
      sample: null
    web_endpoint:
      description:
        - Web endpoint URL of the hub.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the hub.
      returned: always
      type: str
      sample: null
    tenant_features:
      description:
        - >-
          The bit flags for enabled hub features. Bit 0 is set to 1 indicates
          graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates
          the hub is disabled, or enabled if set to 0.
      returned: always
      type: integer
      sample: null
    hub_billing_info:
      description:
        - Billing settings of the hub.
      returned: always
      type: dict
      sample: null
      contains:
        sku_name:
          description:
            - The sku name.
          returned: always
          type: str
          sample: null
        min_units:
          description:
            - >-
              The minimum number of units will be billed. One unit is 10,000
              Profiles and 100,000 Interactions.
          returned: always
          type: integer
          sample: null
        max_units:
          description:
            - >-
              The maximum number of units can be used.  One unit is 10,000
              Profiles and 100,000 Interactions.
          returned: always
          type: integer
          sample: null
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        api_endpoint:
          description:
            - API endpoint URL of the hub.
          returned: always
          type: str
          sample: null
        web_endpoint:
          description:
            - Web endpoint URL of the hub.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state of the hub.
          returned: always
          type: str
          sample: null
        tenant_features:
          description:
            - >-
              The bit flags for enabled hub features. Bit 0 is set to 1
              indicates graph is enabled, or disabled if set to 0. Bit 1 is set
              to 1 indicates the hub is disabled, or enabled if set to 0.
          returned: always
          type: integer
          sample: null
        hub_billing_info:
          description:
            - Billing settings of the hub.
          returned: always
          type: dict
          sample: null
          contains:
            sku_name:
              description:
                - The sku name.
              returned: always
              type: str
              sample: null
            min_units:
              description:
                - >-
                  The minimum number of units will be billed. One unit is 10,000
                  Profiles and 100,000 Interactions.
              returned: always
              type: integer
              sample: null
            max_units:
              description:
                - >-
                  The maximum number of units can be used.  One unit is 10,000
                  Profiles and 100,000 Interactions.
              returned: always
              type: integer
              sample: null
    next_link:
      description:
        - Link for next set of results.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMHubInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            hub_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-26'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMHubInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None):
            self.results['hubs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['hubs'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['hubs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.hubs.get(resource_group_name=self.resource_group_name,
                                                 hub_name=self.hub_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.hubs.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.hubs.list()
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
    AzureRMHubInfo()


if __name__ == '__main__':
    main()
