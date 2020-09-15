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
module: azure_rm_oucontaineroperation_info
version_added: '2.9'
short_description: Get OuContainerOperation info.
description:
  - Get info of OuContainerOperation.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Operations
      azure_rm_oucontaineroperation_info: 
        {}
        

'''

RETURN = '''
ou_container_operations:
  description: >-
    A list of dict results where the key is the name of the OuContainerOperation
    and the values are the facts for that OuContainerOperation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of operations.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - 'Operation name: {provider}/{resource}/{operation}.'
          returned: always
          type: str
          sample: null
        display:
          description:
            - The operation supported by Domain Services.
          returned: always
          type: dict
          sample: null
          contains:
            description:
              description:
                - The description of the operation.
              returned: always
              type: str
              sample: null
            operation:
              description:
                - >-
                  The action that users can perform, based on their permission
                  level.
              returned: always
              type: str
              sample: null
            provider:
              description:
                - 'Service provider: Domain Services.'
              returned: always
              type: str
              sample: null
            resource:
              description:
                - Resource on which the operation is performed.
              returned: always
              type: str
              sample: null
        origin:
          description:
            - The origin of the operation.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The continuation token for the next page of results.
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
    from azure.mgmt.domain import Domain Services Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOuContainerOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOuContainerOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Domain Services Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        else:
            self.results['ou_container_operations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.ou_container_operations.list()
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
    AzureRMOuContainerOperationInfo()


if __name__ == '__main__':
    main()
