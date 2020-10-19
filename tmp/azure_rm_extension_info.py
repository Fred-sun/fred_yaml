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
module: azure_rm_extension_info
version_added: '2.9'
short_description: Get Extension info.
description:
  - Get info of Extension.
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    required: true
    type: str
  account_resource_name:
    description:
      - The name of the Visual Studio Team Services account resource.
    required: true
    type: str
  extension_resource_name:
    description:
      - The name of the extension.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a list of extension resources within the resource group
      azure_rm_extension_info: 
        account_resource_name: ExampleAccount
        resource_group_name: VS-Example-Group
        

    - name: Get an extension resource
      azure_rm_extension_info: 
        account_resource_name: ExampleAccount
        extension_resource_name: ms.example
        resource_group_name: VS-Example-Group
        

'''

RETURN = '''
extensions:
  description: >-
    A list of dict results where the key is the name of the Extension and the
    values are the facts for that Extension.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of extension resource details.
      returned: always
      type: list
      sample: null
      contains:
        plan:
          description:
            - The extension plan that was purchased.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the plan.
              returned: always
              type: str
              sample: null
            product:
              description:
                - Product name.
              returned: always
              type: str
              sample: null
            promotion_code:
              description:
                - 'Optional: the promotion code associated with the plan.'
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - Name of the extension publisher.
              returned: always
              type: str
              sample: null
            version:
              description:
                - A string that uniquely identifies the plan version.
              returned: always
              type: str
              sample: null
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
    plan:
      description:
        - The extension plan that was purchased.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of the plan.
          returned: always
          type: str
          sample: null
        product:
          description:
            - Product name.
          returned: always
          type: str
          sample: null
        promotion_code:
          description:
            - 'Optional: the promotion code associated with the plan.'
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - Name of the extension publisher.
          returned: always
          type: str
          sample: null
        version:
          description:
            - A string that uniquely identifies the plan version.
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


class AzureRMExtensionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_resource_name=dict(
                type='str',
                required=True
            ),
            extension_resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_resource_name = None
        self.extension_resource_name = None

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
        super(AzureRMExtensionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Visual Studio Resource Provider Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01-preview')

        if (self.resource_group_name is not None and
            self.account_resource_name is not None and
            self.extension_resource_name is not None):
            self.results['extensions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_resource_name is not None):
            self.results['extensions'] = self.format_item(self.listbyaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.extensions.get(resource_group_name=self.resource_group_name,
                                                       account_resource_name=self.account_resource_name,
                                                       extension_resource_name=self.extension_resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyaccount(self):
        response = None

        try:
            response = self.mgmt_client.extensions.list_by_account(resource_group_name=self.resource_group_name,
                                                                   account_resource_name=self.account_resource_name)
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
    AzureRMExtensionInfo()


if __name__ == '__main__':
    main()
