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
module: azure_rm_operationstatu_info
version_added: '2.9'
short_description: Get OperationStatu info.
description:
  - Get info of OperationStatu.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  location_name:
    description:
      - The desired region to obtain information from.
    required: true
    type: str
  workflow_id:
    description:
      - workflow Id
    required: true
    type: str
  operation_id:
    description:
      - operation Id
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Workflows_Get
      azure_rm_operationstatu_info: 
        operation_id: 14b50e24-f68d-4b29-a882-38be9dfb8bd1
        location_name: westus
        resource_group_name: SampleResourceGroup_1
        workflow_id: 828219ea-083e-48b5-89ea-8fd9991b2e75
        

'''

RETURN = '''
operation_status:
  description: >-
    A list of dict results where the key is the name of the OperationStatu and
    the values are the facts for that OperationStatu.
  returned: always
  type: complex
  contains:
    name:
      description:
        - Operation Id
      returned: always
      type: str
      sample: null
    status:
      description:
        - Operation status
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - Start time of the operation
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - End time of the operation
      returned: always
      type: str
      sample: null
    error:
      description:
        - Error details.
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - Error code of the given entry.
          returned: always
          type: str
          sample: null
        message:
          description:
            - Error message of the given entry.
          returned: always
          type: str
          sample: null
        target:
          description:
            - Target of the given error entry.
          returned: always
          type: str
          sample: null
        details:
          description:
            - Error details of the given entry.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - Error code of the given entry.
              returned: always
              type: str
              sample: null
            message:
              description:
                - Error message of the given entry.
              returned: always
              type: str
              sample: null
            target:
              description:
                - Target of the given entry.
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
    from azure.mgmt.microsoft import Microsoft Storage Sync
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationStatuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            location_name=dict(
                type='str',
                required=True
            ),
            workflow_id=dict(
                type='str',
                required=True
            ),
            operation_id=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.location_name = None
        self.workflow_id = None
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
        super(AzureRMOperationStatuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.location_name is not None and
            self.workflow_id is not None and
            self.operation_id is not None):
            self.results['operation_status'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.operation_status.get(resource_group_name=self.resource_group_name,
                                                             location_name=self.location_name,
                                                             workflow_id=self.workflow_id,
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
    AzureRMOperationStatuInfo()


if __name__ == '__main__':
    main()
