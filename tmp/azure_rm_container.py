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
module: azure_rm_container
version_added: '2.9'
short_description: Manage Azure Container instance.
description:
  - 'Create, update and delete instance of Azure Container.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  storage_account_name:
    description:
      - The Storage Account Name
    required: true
    type: str
  container_name:
    description:
      - The container Name
      - The container name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  data_format:
    description:
      - DataFormat for Container
    type: str
    choices:
      - BlockBlob
      - PageBlob
      - AzureFile
  state:
    description:
      - Assert the state of the Container.
      - >-
        Use C(present) to create or update an Container and C(absent) to delete
        it.
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
    - name: ContainerPut
      azure_rm_container: 
        container_name: blobcontainer1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        storage_account_name: storageaccount1
        properties:
          data_format: BlockBlob
        

    - name: ContainerDelete
      azure_rm_container: 
        container_name: blobcontainer1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        storage_account_name: storageaccount1
        

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
          If a refresh job is currently in progress on this share or container,
          this field indicates the ARM resource ID of that job. The field is
          empty if no job is in progress.
      returned: always
      type: str
      sample: null
    last_completed_refresh_job_time_in_utc:
      description:
        - >-
          Indicates the completed time for the last refresh job on this
          particular share or container, if any.This could be a failed job or a
          successful job.
      returned: always
      type: str
      sample: null
    error_manifest_file:
      description:
        - >-
          Indicates the relative path of the error xml for the last refresh job
          on this particular share or container, if any. This could be a failed
          job or a successful job.
      returned: always
      type: str
      sample: null
    last_job:
      description:
        - >-
          Indicates the id of the last refresh job on this particular share or
          container,if any. This could be a failed job or a successful job.
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


class AzureRMContainer(AzureRMModuleBaseExt):
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
            container_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_format=dict(
                type='str',
                disposition='/data_format',
                choices=['BlockBlob',
                         'PageBlob',
                         'AzureFile']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.storage_account_name = None
        self.container_name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContainer, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.containers.create_or_update(device_name=self.device_name,
                                                                    storage_account_name=self.storage_account_name,
                                                                    container_name=self.container_name,
                                                                    resource_group_name=self.resource_group_name,
                                                                    container=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Container instance.')
            self.fail('Error creating the Container instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.containers.delete(device_name=self.device_name,
                                                          storage_account_name=self.storage_account_name,
                                                          container_name=self.container_name,
                                                          resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Container instance.')
            self.fail('Error deleting the Container instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.containers.get(device_name=self.device_name,
                                                       storage_account_name=self.storage_account_name,
                                                       container_name=self.container_name,
                                                       resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContainer()


if __name__ == '__main__':
    main()
