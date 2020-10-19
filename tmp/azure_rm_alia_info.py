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
module: azure_rm_alia_info
version_added: '2.9'
short_description: Get Alia info.
description:
  - Get info of Alia.
options:
  alias_name:
    description:
      - Alias Name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetAlias
      azure_rm_alia_info: 
        alias_name: aliasForNewSub
        

'''

RETURN = '''
alias:
  description: >-
    A list of dict results where the key is the name of the Alia and the values
    are the facts for that Alia.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Fully qualified ID for the alias resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Alias ID.
      returned: always
      type: str
      sample: null
    type:
      description:
        - 'Resource type, Microsoft.Subscription/aliases.'
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Put Alias response properties.
      returned: always
      type: dict
      sample: null
      contains:
        subscription_id:
          description:
            - Newly created subscription Id.
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
        - The list of alias.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Fully qualified ID for the alias resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Alias ID.
          returned: always
          type: str
          sample: null
        type:
          description:
            - 'Resource type, Microsoft.Subscription/aliases.'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Put Alias response properties.
          returned: always
          type: dict
          sample: null
          contains:
            subscription_id:
              description:
                - Newly created subscription Id.
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
        - The link (url) to the next page of results.
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
    from azure.mgmt.subscription import SubscriptionClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAliaInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            alias_name=dict(
                type='str'
            )
        )

        self.alias_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-09-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAliaInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SubscriptionClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01')

        if (self.alias_name is not None):
            self.results['alias'] = self.format_item(self.get())
        else:
            self.results['alias'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.alias.get(alias_name=self.alias_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.alias.list()
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
    AzureRMAliaInfo()


if __name__ == '__main__':
    main()
