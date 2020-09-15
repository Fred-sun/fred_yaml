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
module: azure_rm_adcoperation_info
version_added: '2.9'
short_description: Get ADCOperation info.
description:
  - Get info of ADCOperation.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Operations
      azure_rm_adcoperation_info: 
        {}
        

'''

RETURN = '''
adcoperations:
  description: >-
    A list of dict results where the key is the name of the ADCOperation and the
    values are the facts for that ADCOperation.
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
            - The operation supported by Azure Data Catalog Service.
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
                - 'Service provider: Azure Data Catalog Service.'
              returned: always
              type: str
              sample: null
            resource:
              description:
                - Resource on which the operation is performed.
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
    from azure.mgmt.data import DataCatalogRestClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMADCOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-03-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMADCOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataCatalogRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-30')

        else:
            self.results['adcoperations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.adcoperations.list()
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
    AzureRMADCOperationInfo()


if __name__ == '__main__':
    main()
