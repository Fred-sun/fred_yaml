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
module: azure_rm_operationsstatu_info
version_added: '2.9'
short_description: Get OperationsStatu info.
description:
  - Get info of OperationsStatu.
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  name:
    description:
      - The job name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: OperationsStatusGet
      azure_rm_operationsstatu_info: 
        name: 159a00c7-8543-4343-9435-263ac87df3bb
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
operations_status:
  description: >-
    A list of dict results where the key is the name of the OperationsStatu and
    the values are the facts for that OperationsStatu.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The path ID that uniquely identifies the object.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the object.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The hierarchical type of the object.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The current status of the job.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - The UTC date and time at which the job started.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - The UTC date and time at which the job completed.
      returned: always
      type: str
      sample: null
    percent_complete:
      description:
        - The percentage of the job that is complete.
      returned: always
      type: integer
      sample: null
    error:
      description:
        - The error details.
      returned: always
      type: dict
      sample: null
      contains:
        error_details:
          description:
            - The error details.
          returned: always
          type: list
          sample: null
          contains:
            recommendations:
              description:
                - The recommended actions.
              returned: always
              type: list
              sample: null
            code:
              description:
                - The code intended for programmatic access.
              returned: always
              type: str
              sample: null
            message:
              description:
                - The message that describes the error in detail.
              returned: always
              type: str
              sample: null
        code:
          description:
            - The code intended for programmatic access.
          returned: always
          type: str
          sample: null
        message:
          description:
            - The message that describes the error in detail.
          returned: always
          type: str
          sample: null
    job_type:
      description:
        - The type of the job.
      returned: always
      type: str
      sample: null
    current_stage:
      description:
        - Current stage of the update operation.
      returned: always
      type: str
      sample: null
    download_progress:
      description:
        - The download progress.
      returned: always
      type: dict
      sample: null
      contains:
        download_phase:
          description:
            - The download phase.
          returned: always
          type: str
          sample: null
        percent_complete:
          description:
            - Percentage of completion.
          returned: always
          type: integer
          sample: null
        total_bytes_to_download:
          description:
            - Total bytes to download.
          returned: always
          type: number
          sample: null
        total_bytes_downloaded:
          description:
            - Total bytes downloaded.
          returned: always
          type: number
          sample: null
        number_of_updates_to_download:
          description:
            - Number of updates to download.
          returned: always
          type: integer
          sample: null
        number_of_updates_downloaded:
          description:
            - Number of updates downloaded.
          returned: always
          type: integer
          sample: null
    install_progress:
      description:
        - The install progress.
      returned: always
      type: dict
      sample: null
      contains:
        percent_complete:
          description:
            - Percentage completed.
          returned: always
          type: integer
          sample: null
        number_of_updates_to_install:
          description:
            - Number of updates to install.
          returned: always
          type: integer
          sample: null
        number_of_updates_installed:
          description:
            - Number of updates installed.
          returned: always
          type: integer
          sample: null
    total_refresh_errors:
      description:
        - Total number of errors encountered during the refresh process.
      returned: always
      type: integer
      sample: null
    error_manifest_file:
      description:
        - >-
          Local share/remote container relative path to the error manifest file
          of the refresh.
      returned: always
      type: str
      sample: null
    refreshed_entity_id:
      description:
        - ARM ID of the entity that was refreshed.
      returned: always
      type: str
      sample: null
    folder:
      description:
        - >-
          If only subfolders need to be refreshed, then the subfolder path
          inside the share or container. (The path is empty if there are no
          subfolders.)
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
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationsStatuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            )
        )

        self.device_name = None
        self.name = None
        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationsStatuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

        if (self.device_name is not None and
            self.name is not None and
            self.resource_group_name is not None):
            self.results['operations_status'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.operations_status.get(device_name=self.device_name,
                                                              name=self.name,
                                                              resource_group_name=self.resource_group_name)
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
    AzureRMOperationsStatuInfo()


if __name__ == '__main__':
    main()
