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
module: azure_rm_registeredprefix_info
version_added: '2.9'
short_description: Get RegisteredPrefix info.
description:
  - Get info of RegisteredPrefix.
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
  registered_prefix_name:
    description:
      - The name of the registered prefix.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a registered prefix associated with the peering
      azure_rm_registeredprefix_info: 
        peering_name: peeringName
        registered_prefix_name: registeredPrefixName
        resource_group_name: rgName
        

    - name: List all the registered prefixes associated with the peering
      azure_rm_registeredprefix_info: 
        peering_name: peeringName
        resource_group_name: rgName
        

'''

RETURN = '''
registered_prefixes:
  description: >-
    A list of dict results where the key is the name of the RegisteredPrefix and
    the values are the facts for that RegisteredPrefix.
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
    prefix:
      description:
        - The customer's prefix from which traffic originates.
      returned: always
      type: str
      sample: null
    prefix_validation_state:
      description:
        - The prefix validation state.
      returned: always
      type: str
      sample: null
    peering_service_prefix_key:
      description:
        - The peering service prefix key that is to be shared with the customer.
      returned: always
      type: str
      sample: null
    error_message:
      description:
        - 'The error message associated with the validation state, if any.'
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of peering registered prefixes.
      returned: always
      type: list
      sample: null
      contains:
        prefix:
          description:
            - The customer's prefix from which traffic originates.
          returned: always
          type: str
          sample: null
        prefix_validation_state:
          description:
            - The prefix validation state.
          returned: always
          type: str
          sample: null
        peering_service_prefix_key:
          description:
            - >-
              The peering service prefix key that is to be shared with the
              customer.
          returned: always
          type: str
          sample: null
        error_message:
          description:
            - 'The error message associated with the validation state, if any.'
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state of the resource.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link to fetch the next page of peering registered prefixes.
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


class AzureRMRegisteredPrefixInfo(AzureRMModuleBase):
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
            registered_prefix_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.peering_name = None
        self.registered_prefix_name = None

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
        super(AzureRMRegisteredPrefixInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.peering_name is not None and
            self.registered_prefix_name is not None):
            self.results['registered_prefixes'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.peering_name is not None):
            self.results['registered_prefixes'] = self.format_item(self.listbypeering())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.registered_prefixes.get(resource_group_name=self.resource_group_name,
                                                                peering_name=self.peering_name,
                                                                registered_prefix_name=self.registered_prefix_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbypeering(self):
        response = None

        try:
            response = self.mgmt_client.registered_prefixes.list_by_peering(resource_group_name=self.resource_group_name,
                                                                            peering_name=self.peering_name)
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
    AzureRMRegisteredPrefixInfo()


if __name__ == '__main__':
    main()
