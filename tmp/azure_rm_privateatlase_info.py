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
module: azure_rm_privateatlase_info
version_added: '2.9'
short_description: Get PrivateAtlase info.
description:
  - Get info of PrivateAtlase.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - The name of the Maps Account.
    required: true
    type: str
  private_atlas_name:
    description:
      - The name of the Private Atlas instance.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetPrivateAtlas
      azure_rm_privateatlase_info: 
        account_name: myMapsAccount
        private_atlas_name: myPrivateAtlas
        resource_group_name: myResourceGroup
        

    - name: ListPrivateAtlasByAccount
      azure_rm_privateatlase_info: 
        account_name: myMapsAccount
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
private_atlases:
  description: >-
    A list of dict results where the key is the name of the PrivateAtlase and
    the values are the facts for that PrivateAtlase.
  returned: always
  type: complex
  contains:
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
    properties:
      description:
        - The Private Atlas resource properties.
      returned: always
      type: dict
      sample: null
      contains:
        provisioning_state:
          description:
            - >-
              The state of the resource provisioning, terminal states:
              Succeeded, Failed, Canceled
          returned: always
          type: str
          sample: null
    value:
      description:
        - a Private Atlas.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - The Private Atlas resource properties.
          returned: always
          type: dict
          sample: null
          contains:
            provisioning_state:
              description:
                - >-
                  The state of the resource provisioning, terminal states:
                  Succeeded, Failed, Canceled
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
    from azure.mgmt.azure import Azure Maps Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPrivateAtlaseInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            private_atlas_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.private_atlas_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPrivateAtlaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Maps Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-01-preview')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.private_atlas_name is not None):
            self.results['private_atlases'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['private_atlases'] = self.format_item(self.listbyaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.private_atlases.get(resource_group_name=self.resource_group_name,
                                                            account_name=self.account_name,
                                                            private_atlas_name=self.private_atlas_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyaccount(self):
        response = None

        try:
            response = self.mgmt_client.private_atlases.list_by_account(resource_group_name=self.resource_group_name,
                                                                        account_name=self.account_name)
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
    AzureRMPrivateAtlaseInfo()


if __name__ == '__main__':
    main()
