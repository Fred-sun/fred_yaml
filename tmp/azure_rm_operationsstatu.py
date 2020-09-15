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
module: azure_rm_operationsstatu
version_added: '2.9'
short_description: Manage Azure OperationsStatu instance.
description:
  - 'Create, update and delete instance of Azure OperationsStatu.'
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
  state:
    description:
      - Assert the state of the OperationsStatu.
      - >-
        Use C(present) to create or update an OperationsStatu and C(absent) to
        delete it.
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
      Local share/remote container relative path to the error manifest file of
      the refresh.
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
      If only subfolders need to be refreshed, then the subfolder path inside
      the share or container. (The path is empty if there are no subfolders.)
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
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOperationsStatu(AzureRMModuleBaseExt):
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
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOperationsStatu, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

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
                response = self.mgmt_client.operations_status.create()
            else:
                response = self.mgmt_client.operations_status.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the OperationsStatu instance.')
            self.fail('Error creating the OperationsStatu instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.operations_status.delete()
        except CloudError as e:
            self.log('Error attempting to delete the OperationsStatu instance.')
            self.fail('Error deleting the OperationsStatu instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.operations_status.get(device_name=self.device_name,
                                                              name=self.name,
                                                              resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOperationsStatu()


if __name__ == '__main__':
    main()
