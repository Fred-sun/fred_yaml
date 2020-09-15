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
module: azure_rm_jobcollection
version_added: '2.9'
short_description: Manage Azure JobCollection instance.
description:
  - 'Create, update and delete instance of Azure JobCollection.'
options:
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  job_collection_name:
    description:
      - The job collection name.
    required: true
    type: str
  name:
    description:
      - Gets or sets the job collection resource name.
    type: str
  location:
    description:
      - Gets or sets the storage account location.
    type: str
  state:
    description:
      - Assert the state of the JobCollection.
      - >-
        Use C(present) to create or update an JobCollection and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
  max_job_count:
    description:
      - Gets or set the maximum job count.
    type: integer
  max_job_occurrence:
    description:
      - Gets or sets the maximum job occurrence.
    type: integer
  max_recurrence:
    description:
      - Gets or set the maximum recurrence.
    type: dict
    suboptions:
      frequency:
        description:
          - >-
            Gets or sets the frequency of recurrence (second, minute, hour, day,
            week, month).
        type: sealed-choice
      interval:
        description:
          - Gets or sets the interval between retries.
        type: integer
  sku_definition_name:
    description:
      - Gets or set the SKU.
    type: sealed-choice
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
    - Gets the job collection resource identifier.
  returned: always
  type: str
  sample: null
type:
  description:
    - Gets the job collection resource type.
  returned: always
  type: str
  sample: null
name:
  description:
    - Gets or sets the job collection resource name.
  returned: always
  type: str
  sample: null
location:
  description:
    - Gets or sets the storage account location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Gets or sets the tags.
  returned: always
  type: dictionary
  sample: null
state:
  description:
    - Gets or sets the state.
  returned: always
  type: sealed-choice
  sample: null
max_job_count:
  description:
    - Gets or set the maximum job count.
  returned: always
  type: integer
  sample: null
max_job_occurrence:
  description:
    - Gets or sets the maximum job occurrence.
  returned: always
  type: integer
  sample: null
max_recurrence:
  description:
    - Gets or set the maximum recurrence.
  returned: always
  type: dict
  sample: null
  contains:
    frequency:
      description:
        - >-
          Gets or sets the frequency of recurrence (second, minute, hour, day,
          week, month).
      returned: always
      type: sealed-choice
      sample: null
    interval:
      description:
        - Gets or sets the interval between retries.
      returned: always
      type: integer
      sample: null
name_properties_sku_name:
  description:
    - Gets or set the SKU.
  returned: always
  type: sealed-choice
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.scheduler import SchedulerManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMJobCollection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            job_collection_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            state=dict(
                type='sealed-choice',
                disposition='/state'
            ),
            max_job_count=dict(
                type='integer',
                disposition='/max_job_count'
            ),
            max_job_occurrence=dict(
                type='integer',
                disposition='/max_job_occurrence'
            ),
            max_recurrence=dict(
                type='dict',
                disposition='/max_recurrence',
                options=dict(
                    frequency=dict(
                        type='sealed-choice',
                        disposition='frequency'
                    ),
                    interval=dict(
                        type='integer',
                        disposition='interval'
                    )
                )
            ),
            sku_definition_name=dict(
                type='sealed-choice',
                disposition='/sku_definition_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.job_collection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobCollection, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SchedulerManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-01')

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
            response = self.mgmt_client.job_collections.create_or_update(resource_group_name=self.resource_group_name,
                                                                         job_collection_name=self.job_collection_name,
                                                                         job_collection=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobCollection instance.')
            self.fail('Error creating the JobCollection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.job_collections.delete(resource_group_name=self.resource_group_name,
                                                               job_collection_name=self.job_collection_name)
        except CloudError as e:
            self.log('Error attempting to delete the JobCollection instance.')
            self.fail('Error deleting the JobCollection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.job_collections.get(resource_group_name=self.resource_group_name,
                                                            job_collection_name=self.job_collection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobCollection()


if __name__ == '__main__':
    main()
