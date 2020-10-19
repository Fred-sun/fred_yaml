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
module: azure_rm__info
version_added: '2.9'
short_description: Get  info.
description:
  - Get info of .
options:
  default:
    description:
      - Default parameter. Leave the value as "default".
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all Serial Console management operations supported by Serial Console RP
      azure_rm__info: 
        {}
        

    - name: Get the Serial Console disabled status for a subscription
      azure_rm__info: 
        default: default
        

'''

RETURN = '''
'':
  description: >-
    A list of dict results where the key is the name of the  and the values are
    the facts for that .
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of Serial Console operations
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - ''
          returned: always
          type: str
          sample: null
        is_data_action:
          description:
            - ''
          returned: always
          type: str
          sample: null
        display:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            provider:
              description:
                - ''
              returned: always
              type: str
              sample: null
            resource:
              description:
                - ''
              returned: always
              type: str
              sample: null
            operation:
              description:
                - ''
              returned: always
              type: str
              sample: null
            description:
              description:
                - ''
              returned: always
              type: str
              sample: null
    disabled:
      description:
        - Whether or not Serial Console is disabled.
      returned: always
      type: bool
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.microsoft import MicrosoftSerialConsoleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            default=dict(
                type='str'
            )
        )

        self.default = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MicrosoftSerialConsoleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-05-01')

        if (self.default is not None):
            self.results[''] = self.format_item(self.getconsolestatus())
        else:
            self.results[''] = self.format_item(self.listoperation())
        return self.results

    def getconsolestatus(self):
        response = None

        try:
            response = self.mgmt_client..get_console_status(default=self.default)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listoperation(self):
        response = None

        try:
            response = self.mgmt_client..list_operation()
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
    AzureRMInfo()


if __name__ == '__main__':
    main()
