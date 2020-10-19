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
module: azure_rm_provideroperation_info
version_added: '2.9'
short_description: Get ProviderOperation info.
description:
  - Get info of ProviderOperation.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
provider_operations:
  description: >-
    A list of dict results where the key is the name of the ProviderOperation
    and the values are the facts for that ProviderOperation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of operations supported by the resource provider.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - 'Operation name: {provider}/{resource}/{operation}'
          returned: always
          type: str
          sample: null
        display:
          description:
            - The object that describes the operations
          returned: always
          type: dict
          sample: null
          contains:
            provider:
              description:
                - Friendly name of the resource provider
              returned: always
              type: str
              sample: null
            resource:
              description:
                - Resource type on which the operation is performed.
              returned: always
              type: str
              sample: null
            operation:
              description:
                - 'Operation type: read, write, delete, listKeys/action, etc.'
              returned: always
              type: str
              sample: null
            description:
              description:
                - Friendly name of the operation
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - URL to get the next set of operation list results if there are any.
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
    from azure.mgmt.managed import ManagedLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProviderOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-10-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProviderOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-15')

        else:
            self.results['provider_operations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.provider_operations.list()
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
    AzureRMProviderOperationInfo()


if __name__ == '__main__':
    main()
