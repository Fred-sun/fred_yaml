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
module: azure_rm_account_info
version_added: '2.9'
short_description: Get Account info.
description:
  - Get info of Account.
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    required: true
    type: str
  resource_name:
    description:
      - Name of the resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a list of account resources in the resource group
      azure_rm_account_info: 
        resource_group_name: VS-Example-Group
        

    - name: Get an account resource
      azure_rm_account_info: 
        resource_group_name: VS-Example-Group
        resource_name: Example
        

'''

RETURN = '''
accounts:
  description: >-
    A list of dict results where the key is the name of the Account and the
    values are the facts for that Account.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of resource details.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - Resource properties.
          returned: always
          type: dictionary
          sample: null
    id:
      description:
        - Unique identifier of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Resource properties.
      returned: always
      type: dictionary
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.visual import Visual Studio Resource Provider Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAccountInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAccountInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Visual Studio Resource Provider Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01-preview')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['accounts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['accounts'] = self.format_item(self.listbyresourcegroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.accounts.get(resource_group_name=self.resource_group_name,
                                                     resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.accounts.list_by_resource_group(resource_group_name=self.resource_group_name)
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
    AzureRMAccountInfo()


if __name__ == '__main__':
    main()
