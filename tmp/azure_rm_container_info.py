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
module: azure_rm_container_info
version_added: '2.9'
short_description: Get Container info.
description:
  - Get info of Container.
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  storage_account_name:
    description:
      - The storage Account name.
      - The Storage Account Name
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  container_name:
    description:
      - The container Name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ContainerListAllInDevice
      azure_rm_container_info: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        storage_account_name: storageaccount1
        

    - name: ContainerGet
      azure_rm_container_info: 
        container_name: blobcontainer1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        storage_account_name: storageaccount1
        

'''

RETURN = '''
containers:
  description: >-
    A list of dict results where the key is the name of the Container and the
    values are the facts for that Container.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of containers.
      returned: always
      type: list
      sample: null
      contains:
        container_status:
          description:
            - Current status of the container.
          returned: always
          type: str
          sample: null
        data_format:
          description:
            - DataFormat for Container
          returned: always
          type: str
          sample: null
        refresh_details:
          description:
            - Details of the refresh job on this container.
          returned: always
          type: dict
          sample: null
          contains:
            in_progress_refresh_job_id:
              description:
                - >-
                  If a refresh job is currently in progress on this share or
                  container, this field indicates the ARM resource ID of that
                  job. The field is empty if no job is in progress.
              returned: always
              type: str
              sample: null
            last_completed_refresh_job_time_in_utc:
              description:
                - >-
                  Indicates the completed time for the last refresh job on this
                  particular share or container, if any.This could be a failed
                  job or a successful job.
              returned: always
              type: str
              sample: null
            error_manifest_file:
              description:
                - >-
                  Indicates the relative path of the error xml for the last
                  refresh job on this particular share or container, if any.
                  This could be a failed job or a successful job.
              returned: always
              type: str
              sample: null
            last_job:
              description:
                - >-
                  Indicates the id of the last refresh job on this particular
                  share or container,if any. This could be a failed job or a
                  successful job.
              returned: always
              type: str
              sample: null
        created_date_time:
          description:
            - The UTC time when container got created.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The path ID that uniquely identifies the object.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The object name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The hierarchical type of the object.
      returned: always
      type: str
      sample: null
    container_status:
      description:
        - Current status of the container.
      returned: always
      type: str
      sample: null
    data_format:
      description:
        - DataFormat for Container
      returned: always
      type: str
      sample: null
    refresh_details:
      description:
        - Details of the refresh job on this container.
      returned: always
      type: dict
      sample: null
      contains:
        in_progress_refresh_job_id:
          description:
            - >-
              If a refresh job is currently in progress on this share or
              container, this field indicates the ARM resource ID of that job.
              The field is empty if no job is in progress.
          returned: always
          type: str
          sample: null
        last_completed_refresh_job_time_in_utc:
          description:
            - >-
              Indicates the completed time for the last refresh job on this
              particular share or container, if any.This could be a failed job
              or a successful job.
          returned: always
          type: str
          sample: null
        error_manifest_file:
          description:
            - >-
              Indicates the relative path of the error xml for the last refresh
              job on this particular share or container, if any. This could be a
              failed job or a successful job.
          returned: always
          type: str
          sample: null
        last_job:
          description:
            - >-
              Indicates the id of the last refresh job on this particular share
              or container,if any. This could be a failed job or a successful
              job.
          returned: always
          type: str
          sample: null
    created_date_time:
      description:
        - The UTC time when container got created.
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


class AzureRMContainerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            storage_account_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            container_name=dict(
                type='str'
            )
        )

        self.device_name = None
        self.storage_account_name = None
        self.resource_group_name = None
        self.container_name = None

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
        super(AzureRMContainerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

        if (self.device_name is not None and
            self.storage_account_name is not None and
            self.container_name is not None and
            self.resource_group_name is not None):
            self.results['containers'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.storage_account_name is not None and
              self.resource_group_name is not None):
            self.results['containers'] = self.format_item(self.listbystorageaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.containers.get(device_name=self.device_name,
                                                       storage_account_name=self.storage_account_name,
                                                       container_name=self.container_name,
                                                       resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbystorageaccount(self):
        response = None

        try:
            response = self.mgmt_client.containers.list_by_storage_account(device_name=self.device_name,
                                                                           storage_account_name=self.storage_account_name,
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
    AzureRMContainerInfo()


if __name__ == '__main__':
    main()
