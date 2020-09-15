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
module: azure_rm_blockchainmemberoperationresult_info
version_added: '2.9'
short_description: Get BlockchainMemberOperationResult info.
description:
  - Get info of BlockchainMemberOperationResult.
options:
  location_name:
    description:
      - Location name.
    required: true
    type: str
  operation_id:
    description:
      - Operation Id.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: BlockchainMemberOperationResults_Get
      azure_rm_blockchainmemberoperationresult_info: 
        operation_id: 12f4b309-01e3-4fcf-bc0b-1cc034ca03f8
        location_name: southeastasia
        

'''

RETURN = '''
blockchain_member_operation_results:
  description: >-
    A list of dict results where the key is the name of the
    BlockchainMemberOperationResult and the values are the facts for that
    BlockchainMemberOperationResult.
  returned: always
  type: complex
  contains:
    name:
      description:
        - Gets or sets the operation name.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - Gets or sets the operation start time.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - Gets or sets the operation end time.
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
    from azure.mgmt.blockchain import BlockchainManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBlockchainMemberOperationResultInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            operation_id=dict(
                type='str',
                required=True
            )
        )

        self.location_name = None
        self.operation_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMBlockchainMemberOperationResultInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BlockchainManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.location_name is not None and
            self.operation_id is not None):
            self.results['blockchain_member_operation_results'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.blockchain_member_operation_results.get(location_name=self.location_name,
                                                                                operation_id=self.operation_id)
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
    AzureRMBlockchainMemberOperationResultInfo()


if __name__ == '__main__':
    main()
