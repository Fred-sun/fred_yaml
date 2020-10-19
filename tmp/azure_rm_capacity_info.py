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
module: azure_rm_capacity_info
version_added: '2.9'
short_description: Get Capacity info.
description:
  - Get info of Capacity.
options:
  resource_group_name:
    description:
      - >-
        The name of the Azure Resource group of which a given PowerBIDedicated
        capacity is part. This name must be at least 1 character in length, and
        no more than 90.
    type: str
  dedicated_capacity_name:
    description:
      - >-
        The name of the dedicated capacity. It must be a minimum of 3
        characters, and a maximum of 63.
      - >-
        The name of the Dedicated capacity. It must be at least 3 characters in
        length, and no more than 63.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get details of a capacity
      azure_rm_capacity_info: 
        dedicated_capacity_name: azsdktest
        resource_group_name: TestRG
        

    - name: List capacities in resource group
      azure_rm_capacity_info: 
        resource_group_name: TestRG
        

    - name: List eligible SKUs for a new capacity
      azure_rm_capacity_info: 
        {}
        

    - name: List eligible SKUs for an existing capacity
      azure_rm_capacity_info: 
        dedicated_capacity_name: azsdktest
        resource_group_name: TestRG
        

'''

RETURN = '''
capacities:
  description: >-
    A list of dict results where the key is the name of the Capacity and the
    values are the facts for that Capacity.
  returned: always
  type: complex
  contains:
    id:
      description:
        - An identifier that represents the PowerBI Dedicated resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the PowerBI Dedicated resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the PowerBI Dedicated resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Location of the PowerBI Dedicated resource.
      returned: always
      type: str
      sample: null
    sku:
      description:
        - The SKU of the PowerBI Dedicated resource.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of the SKU level.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The name of the Azure pricing tier to which the SKU applies.
          returned: always
          type: str
          sample: null
    tags:
      description:
        - Key-value pairs of additional resource provisioning properties.
      returned: always
      type: dictionary
      sample: null
    administration:
      description:
        - A collection of Dedicated capacity administrators
      returned: always
      type: dict
      sample: null
      contains:
        members:
          description:
            - An array of administrator user identities.
          returned: always
          type: list
          sample: null
    state:
      description:
        - >-
          The current state of PowerBI Dedicated resource. The state is to
          indicate more states outside of resource provisioning.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The current deployment state of PowerBI Dedicated resource. The
          provisioningState is to indicate states for resource provisioning.
      returned: always
      type: str
      sample: null
    value:
      description:
        - |-
          An array of Dedicated capacities resources.
          The collection of available SKUs for new resources
          The collection of available SKUs for existing resources
      returned: always
      type: list
      sample: null
      contains:
        administration:
          description:
            - A collection of Dedicated capacity administrators
          returned: always
          type: dict
          sample: null
          contains:
            members:
              description:
                - An array of administrator user identities.
              returned: always
              type: list
              sample: null
        state:
          description:
            - >-
              The current state of PowerBI Dedicated resource. The state is to
              indicate more states outside of resource provisioning.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The current deployment state of PowerBI Dedicated resource. The
              provisioningState is to indicate states for resource provisioning.
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
    from azure.mgmt.power import PowerBIDedicated
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCapacityInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            dedicated_capacity_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.dedicated_capacity_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-10-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCapacityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PowerBIDedicated,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01')

        if (self.resource_group_name is not None and
            self.dedicated_capacity_name is not None):
            self.results['capacities'] = self.format_item(self.getdetail())
        elif (self.resource_group_name is not None and
              self.dedicated_capacity_name is not None):
            self.results['capacities'] = self.format_item(self.listskuforcapacity())
        elif (self.resource_group_name is not None):
            self.results['capacities'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['capacities'] = self.format_item(self.list())
        else:
            self.results['capacities'] = self.format_item(self.listsku())
        return self.results

    def getdetail(self):
        response = None

        try:
            response = self.mgmt_client.capacities.get_detail(resource_group_name=self.resource_group_name,
                                                              dedicated_capacity_name=self.dedicated_capacity_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listskuforcapacity(self):
        response = None

        try:
            response = self.mgmt_client.capacities.list_sku_for_capacity(resource_group_name=self.resource_group_name,
                                                                         dedicated_capacity_name=self.dedicated_capacity_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.capacities.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.capacities.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsku(self):
        response = None

        try:
            response = self.mgmt_client.capacities.list_sku()
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
    AzureRMCapacityInfo()


if __name__ == '__main__':
    main()
