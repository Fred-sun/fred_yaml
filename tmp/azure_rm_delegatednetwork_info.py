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
module: azure_rm_delegatednetwork_info
version_added: '2.9'
short_description: Get DelegatedNetwork info.
description:
  - Get info of DelegatedNetwork.
options:
  resource_group_name:
    description:
      - >-
        The name of the Azure Resource group of which a given DelegatedNetwork
        resource is part. This name must be at least 1 character in length, and
        no more than 90.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get DelegatedController resources by subscription
      azure_rm_delegatednetwork_info: 
        {}
        

    - name: Get DelegatedNetwork resources by resource group
      azure_rm_delegatednetwork_info: 
        resource_group_name: testRG
        

'''

RETURN = '''
delegated_network:
  description: >-
    A list of dict results where the key is the name of the DelegatedNetwork and
    the values are the facts for that DelegatedNetwork.
  returned: always
  type: complex
  contains:
    value:
      description:
        - An array of Delegated controller resources.
      returned: always
      type: list
      sample: null
      contains:
        state:
          description:
            - The current state of dnc controller resource.
          returned: always
          type: str
          sample: null
        type_properties_type:
          description:
            - Type of dnc controller.
          returned: always
          type: str
          sample: null
        resource_guid:
          description:
            - Gets or sets resource GUID property of the controller resource.
          returned: always
          type: str
          sample: null
        dnc_app_id:
          description:
            - Get controller AAD ID.
          returned: always
          type: str
          sample: null
        dnc_endpoint:
          description:
            - Dnc Endpoint url.
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
    from azure.mgmt.dnc import DNC
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDelegatedNetworkInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-08-08-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDelegatedNetworkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DNC,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-08-preview')

        if (self.resource_group_name is not None):
            self.results['delegated_network'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['delegated_network'] = self.format_item(self.listbysubscription())
        return self.results

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.delegated_network.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.delegated_network.list_by_subscription()
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
    AzureRMDelegatedNetworkInfo()


if __name__ == '__main__':
    main()
