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
module: azure_rm_digitaltwinsendpoint_info
version_added: '2.9'
short_description: Get DigitalTwinsEndpoint info.
description:
  - Get info of DigitalTwinsEndpoint.
options:
  resource_group_name:
    description:
      - The name of the resource group that contains the DigitalTwinsInstance.
    required: true
    type: str
  resource_name:
    description:
      - The name of the DigitalTwinsInstance.
    required: true
    type: str
  endpoint_name:
    description:
      - Name of Endpoint Resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a DigitalTwinsInstance endpoints
      azure_rm_digitaltwinsendpoint_info: 
        resource_group_name: resRg
        resource_name: myDigitalTwinsService
        

    - name: Get a DigitalTwinsInstance endpoint
      azure_rm_digitaltwinsendpoint_info: 
        endpoint_name: myServiceBus
        resource_group_name: resRg
        resource_name: myDigitalTwinsService
        

'''

RETURN = '''
digital_twins_endpoint:
  description: >-
    A list of dict results where the key is the name of the DigitalTwinsEndpoint
    and the values are the facts for that DigitalTwinsEndpoint.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - The link used to get the next page of DigitalTwinsInstance Endpoints.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of DigitalTwinsInstance Endpoints.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - DigitalTwinsInstance endpoint resource properties.
          returned: always
          type: dict
          sample: null
          contains:
            endpoint_type:
              description:
                - The type of Digital Twins endpoint
              returned: always
              type: str
              sample: null
            provisioning_state:
              description:
                - The provisioning state.
              returned: always
              type: str
              sample: null
            created_time:
              description:
                - Time when the Endpoint was added to DigitalTwinsInstance.
              returned: always
              type: str
              sample: null
            dead_letter_secret:
              description:
                - Dead letter storage secret. Will be obfuscated during read.
              returned: always
              type: str
              sample: null
    id:
      description:
        - The resource identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Extension resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The resource type.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - DigitalTwinsInstance endpoint resource properties.
      returned: always
      type: dict
      sample: null
      contains:
        endpoint_type:
          description:
            - The type of Digital Twins endpoint
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state.
          returned: always
          type: str
          sample: null
        created_time:
          description:
            - Time when the Endpoint was added to DigitalTwinsInstance.
          returned: always
          type: str
          sample: null
        dead_letter_secret:
          description:
            - Dead letter storage secret. Will be obfuscated during read.
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
    from azure.mgmt.azure import AzureDigitalTwinsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDigitalTwinsEndpointInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            endpoint_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.endpoint_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-10-31'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDigitalTwinsEndpointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureDigitalTwinsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-10-31')

        if (self.resource_group_name is not None and
            self.resource_name is not None and
            self.endpoint_name is not None):
            self.results['digital_twins_endpoint'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['digital_twins_endpoint'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.digital_twins_endpoint.get(resource_group_name=self.resource_group_name,
                                                                   resource_name=self.resource_name,
                                                                   endpoint_name=self.endpoint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.digital_twins_endpoint.list(resource_group_name=self.resource_group_name,
                                                                    resource_name=self.resource_name)
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
    AzureRMDigitalTwinsEndpointInfo()


if __name__ == '__main__':
    main()
