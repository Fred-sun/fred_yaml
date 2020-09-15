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
module: azure_rm_job
version_added: '2.9'
short_description: Manage Azure Job instance.
description:
  - 'Create, update and delete instance of Azure Job.'
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  job_name:
    description:
      - The job Name.
    required: true
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
  state:
    description:
      - Assert the state of the Job.
      - Use C(present) to create or update an Job and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
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
        - 'The number of bytes of data processed till now, as part of the job.'
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
          The average throughput of data processed(bytes/sec), as part of the
          job.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMJob(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            job_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.job_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJob, self).__init__(derived_arg_spec=self.module_arg_spec,
                                         supports_check_mode=True,
                                         supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.jobs.create()
            else:
                response = self.mgmt_client.jobs.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Job instance.')
            self.fail('Error creating the Job instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.jobs.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Job instance.')
            self.fail('Error deleting the Job instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.jobs.get(device_name=self.device_name,
                                                 job_name=self.job_name,
                                                 resource_group_name=self.resource_group_name,
                                                 manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJob()


if __name__ == '__main__':
    main()
