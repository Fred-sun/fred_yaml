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
module: azure_rm_ascoperation_info
version_added: '2.9'
short_description: Get AscOperation info.
description:
  - Get info of AscOperation.
options:
  location:
    description:
      - The region name which the operation will lookup into.
    required: true
    type: str
  operation_id:
    description:
      - The operation id which uniquely identifies the asynchronous operation.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: AscOperations_Get
      azure_rm_ascoperation_info: 
        operation_id: testoperationid
        location: West US
        

'''

RETURN = '''
asc_operations:
  description: >-
    A list of dict results where the key is the name of the AscOperation and the
    values are the facts for that AscOperation.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The operation Id.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The operation name.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - The start time of the operation.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - The end time of the operation.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the operation.
      returned: always
      type: str
      sample: null
    error:
      description:
        - The error detail of the operation if any.
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - Error code
          returned: always
          type: str
          sample: null
        message:
          description:
            - Error message indicating why the operation failed.
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
    from azure.mgmt.storage import StorageCacheManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAscOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            operation_id=dict(
                type='str',
                required=True
            )
        )

        self.location = None
        self.operation_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAscOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageCacheManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.location is not None and
            self.operation_id is not None):
            self.results['asc_operations'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.asc_operations.get(location=self.location,
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
    AzureRMAscOperationInfo()


if __name__ == '__main__':
    main()
