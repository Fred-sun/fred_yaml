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
module: azure_rm_multipleactivationkey_info
version_added: '2.9'
short_description: Get MultipleActivationKey info.
description:
  - Get info of MultipleActivationKey.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  multiple_activation_key_name:
    description:
      - The name of the MAK key.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListMultipleActivationKeys
      azure_rm_multipleactivationkey_info: 
        {}
        

    - name: GetMultipleActivationKey
      azure_rm_multipleactivationkey_info: 
        multiple_activation_key_name: server08-key-2019
        resource_group_name: testgr1
        

'''

RETURN = '''
multiple_activation_keys:
  description: >-
    A list of dict results where the key is the name of the
    MultipleActivationKey and the values are the facts for that
    MultipleActivationKey.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of MAK keys.
      returned: always
      type: list
      sample: null
      contains:
        multiple_activation_key:
          description:
            - MAK 5x5 key.
          returned: always
          type: str
          sample: null
        expiration_date:
          description:
            - End of support of security updates activated by the MAK key.
          returned: always
          type: str
          sample: null
        os_type:
          description:
            - Type of OS for which the key is requested.
          returned: always
          type: str
          sample: null
        support_type:
          description:
            - Type of support
          returned: always
          type: str
          sample: null
        installed_server_number:
          description:
            - Number of activations/servers using the MAK key.
          returned: always
          type: integer
          sample: null
        agreement_number:
          description:
            - Agreement number under which the key is requested.
          returned: always
          type: str
          sample: null
        is_eligible:
          description:
            - >-
              <code> true </code> if user has eligible on-premises Windows
              physical or virtual machines, and that the requested key will only
              be used in their organization; <code> false </code> otherwise.
          returned: always
          type: bool
          sample: null
        provisioning_state:
          description:
            - ''
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to the next page of resources.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    multiple_activation_key:
      description:
        - MAK 5x5 key.
      returned: always
      type: str
      sample: null
    expiration_date:
      description:
        - End of support of security updates activated by the MAK key.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - Type of OS for which the key is requested.
      returned: always
      type: str
      sample: null
    support_type:
      description:
        - Type of support
      returned: always
      type: str
      sample: null
    installed_server_number:
      description:
        - Number of activations/servers using the MAK key.
      returned: always
      type: integer
      sample: null
    agreement_number:
      description:
        - Agreement number under which the key is requested.
      returned: always
      type: str
      sample: null
    is_eligible:
      description:
        - >-
          <code> true </code> if user has eligible on-premises Windows physical
          or virtual machines, and that the requested key will only be used in
          their organization; <code> false </code> otherwise.
      returned: always
      type: bool
      sample: null
    provisioning_state:
      description:
        - ''
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
    from azure.mgmt.windowsesu import windowsesu
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMultipleActivationKeyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            multiple_activation_key_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.multiple_activation_key_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-09-16-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMultipleActivationKeyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(windowsesu,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-09-16-preview')

        if (self.resource_group_name is not None and
            self.multiple_activation_key_name is not None):
            self.results['multiple_activation_keys'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['multiple_activation_keys'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['multiple_activation_keys'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.multiple_activation_keys.get(resource_group_name=self.resource_group_name,
                                                                     multiple_activation_key_name=self.multiple_activation_key_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.multiple_activation_keys.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.multiple_activation_keys.list()
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
    AzureRMMultipleActivationKeyInfo()


if __name__ == '__main__':
    main()
