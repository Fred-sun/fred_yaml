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
module: azure_rm_job_info
version_added: '2.9'
short_description: Get Job info.
description:
  - Get info of Job.
options:
  device_name:
    description:
      - The device name
    type: str
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  filter:
    description:
      - OData Filter options
    type: str
  job_name:
    description:
      - The job Name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: JobsListByDevice
      azure_rm_job_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: JobsGet
      azure_rm_job_info: 
        device_name: sca07forsdktest
        job_name: 70a29339-de6d-48e8-b24f-e25ee6769a00
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: JobsListByManager
      azure_rm_job_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
jobs:
  description: >-
    A list of dict results where the key is the name of the Job and the values
    are the facts for that Job.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        status:
          description:
            - The current status of the job.
          returned: always
          type: sealed-choice
          sample: null
        start_time:
          description:
            - The UTC time at which the job was started.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The UTC time at which the job completed.
          returned: always
          type: str
          sample: null
        percent_complete:
          description:
            - The percentage of the job that is already complete.
          returned: always
          type: integer
          sample: null
        error:
          description:
            - 'The error details, if any, for the job.'
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
                    - The error code intended for programmatic access.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      The error message intended to describe the error in
                      detail.
                  returned: always
                  type: str
                  sample: null
            code:
              description:
                - The error code intended for programmatic access.
              returned: always
              type: str
              sample: null
            message:
              description:
                - The error message intended to describe the error in detail.
              returned: always
              type: str
              sample: null
        job_type:
          description:
            - The type of the job.
          returned: always
          type: sealed-choice
          sample: null
        data_stats:
          description:
            - The data statistics properties of the job.
          returned: always
          type: dict
          sample: null
          contains:
            total_data:
              description:
                - 'The total bytes of data to be processed, as part of the job.'
              returned: always
              type: integer
              sample: null
            processed_data:
              description:
                - >-
                  The number of bytes of data processed till now, as part of the
                  job.
              returned: always
              type: integer
              sample: null
            cloud_data:
              description:
                - >-
                  The number of bytes of data written to cloud, as part of the
                  job.
              returned: always
              type: integer
              sample: null
            throughput:
              description:
                - >-
                  The average throughput of data processed(bytes/sec), as part
                  of the job.
              returned: always
              type: integer
              sample: null
        entity_label:
          description:
            - The entity identifier for which the job ran.
          returned: always
          type: str
          sample: null
        entity_type:
          description:
            - The entity type for which the job ran.
          returned: always
          type: str
          sample: null
        job_stages:
          description:
            - The job stages.
          returned: always
          type: list
          sample: null
          contains:
            message:
              description:
                - The message of the job stage.
              returned: always
              type: str
              sample: null
            stage_status:
              description:
                - The stage status.
              returned: always
              type: sealed-choice
              sample: null
            detail:
              description:
                - The details of the stage.
              returned: always
              type: str
              sample: null
            error_code:
              description:
                - The error code of the stage if any.
              returned: always
              type: str
              sample: null
        device_id:
          description:
            - The device ID in which the job ran.
          returned: always
          type: str
          sample: null
        is_cancellable:
          description:
            - Represents whether the job is cancellable or not.
          returned: always
          type: bool
          sample: null
        backup_type:
          description:
            - >-
              The backup type (CloudSnapshot | LocalSnapshot). Applicable only
              for backup jobs.
          returned: always
          type: sealed-choice
          sample: null
        source_device_id:
          description:
            - The source device ID of the failover job.
          returned: always
          type: str
          sample: null
        backup_point_in_time:
          description:
            - The time of the backup used for the failover.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The NextLink.
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
    kind:
      description:
        - The Kind of the object. Currently only Series8000 is supported
      returned: always
      type: constant
      sample: null
    status:
      description:
        - The current status of the job.
      returned: always
      type: sealed-choice
      sample: null
    start_time:
      description:
        - The UTC time at which the job was started.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - The UTC time at which the job completed.
      returned: always
      type: str
      sample: null
    percent_complete:
      description:
        - The percentage of the job that is already complete.
      returned: always
      type: integer
      sample: null
    error:
      description:
        - 'The error details, if any, for the job.'
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
                - The error code intended for programmatic access.
              returned: always
              type: str
              sample: null
            message:
              description:
                - The error message intended to describe the error in detail.
              returned: always
              type: str
              sample: null
        code:
          description:
            - The error code intended for programmatic access.
          returned: always
          type: str
          sample: null
        message:
          description:
            - The error message intended to describe the error in detail.
          returned: always
          type: str
          sample: null
    job_type:
      description:
        - The type of the job.
      returned: always
      type: sealed-choice
      sample: null
    data_stats:
      description:
        - The data statistics properties of the job.
      returned: always
      type: dict
      sample: null
      contains:
        total_data:
          description:
            - 'The total bytes of data to be processed, as part of the job.'
          returned: always
          type: integer
          sample: null
        processed_data:
          description:
            - >-
              The number of bytes of data processed till now, as part of the
              job.
          returned: always
          type: integer
          sample: null
        cloud_data:
          description:
            - 'The number of bytes of data written to cloud, as part of the job.'
          returned: always
          type: integer
          sample: null
        throughput:
          description:
            - >-
              The average throughput of data processed(bytes/sec), as part of
              the job.
          returned: always
          type: integer
          sample: null
    entity_label:
      description:
        - The entity identifier for which the job ran.
      returned: always
      type: str
      sample: null
    entity_type:
      description:
        - The entity type for which the job ran.
      returned: always
      type: str
      sample: null
    job_stages:
      description:
        - The job stages.
      returned: always
      type: list
      sample: null
      contains:
        message:
          description:
            - The message of the job stage.
          returned: always
          type: str
          sample: null
        stage_status:
          description:
            - The stage status.
          returned: always
          type: sealed-choice
          sample: null
        detail:
          description:
            - The details of the stage.
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - The error code of the stage if any.
          returned: always
          type: str
          sample: null
    device_id:
      description:
        - The device ID in which the job ran.
      returned: always
      type: str
      sample: null
    is_cancellable:
      description:
        - Represents whether the job is cancellable or not.
      returned: always
      type: bool
      sample: null
    backup_type:
      description:
        - >-
          The backup type (CloudSnapshot | LocalSnapshot). Applicable only for
          backup jobs.
      returned: always
      type: sealed-choice
      sample: null
    source_device_id:
      description:
        - The source device ID of the failover job.
      returned: always
      type: str
      sample: null
    backup_point_in_time:
      description:
        - The time of the backup used for the failover.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMJobInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            job_name=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.filter = None
        self.job_name = None

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
        super(AzureRMJobInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.job_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['jobs'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['jobs'] = self.format_item(self.listbydevice())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['jobs'] = self.format_item(self.listbymanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.jobs.get(device_name=self.device_name,
                                                 job_name=self.job_name,
                                                 resource_group_name=self.resource_group_name,
                                                 manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.jobs.list_by_device(device_name=self.device_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name,
                                                            filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanager(self):
        response = None

        try:
            response = self.mgmt_client.jobs.list_by_manager(resource_group_name=self.resource_group_name,
                                                             manager_name=self.manager_name,
                                                             filter=self.filter)
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
    AzureRMJobInfo()


if __name__ == '__main__':
    main()
