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
module: azure_rm_peeringservice_info
version_added: '2.9'
short_description: Get PeeringService info.
description:
  - Get info of PeeringService.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  peering_service_name:
    description:
      - The name of the peering.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a peering service
      azure_rm_peeringservice_info: 
        peering_service_name: peeringServiceName
        resource_group_name: rgName
        

    - name: List peering services in a resource group
      azure_rm_peeringservice_info: 
        resource_group_name: rgName
        

    - name: List peering services in a subscription
      azure_rm_peeringservice_info: 
        {}
        

'''

RETURN = '''
peering_services:
  description: >-
    A list of dict results where the key is the name of the PeeringService and
    the values are the facts for that PeeringService.
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
    location:
      description:
        - The location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The resource tags.
      returned: always
      type: dictionary
      sample: null
    peering_service_location:
      description:
        - The PeeringServiceLocation of the Customer.
      returned: always
      type: str
      sample: null
    peering_service_provider:
      description:
        - The MAPS Provider Name.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource.
      returned: always
      type: str
      sample: null
    name_sku_name:
      description:
        - The name of the peering service SKU.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of peering services.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - The location of the resource.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - The resource tags.
          returned: always
          type: dictionary
          sample: null
        peering_service_location:
          description:
            - The PeeringServiceLocation of the Customer.
          returned: always
          type: str
          sample: null
        peering_service_provider:
          description:
            - The MAPS Provider Name.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state of the resource.
          returned: always
          type: str
          sample: null
        name_sku_name:
          description:
            - The name of the peering service SKU.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link to fetch the next page of peering services.
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


class AzureRMPeeringServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            peering_service_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.peering_service_name = None

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
        super(AzureRMPeeringServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.peering_service_name is not None):
            self.results['peering_services'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['peering_services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['peering_services'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.peering_services.get(resource_group_name=self.resource_group_name,
                                                             peering_service_name=self.peering_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.peering_services.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.peering_services.list_by_subscription()
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
    AzureRMPeeringServiceInfo()


if __name__ == '__main__':
    main()
