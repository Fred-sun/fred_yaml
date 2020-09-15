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
module: azure_rm_computepolicy
version_added: '2.9'
short_description: Manage Azure ComputePolicy instance.
description:
  - 'Create, update and delete instance of Azure ComputePolicy.'
options:
  resource_group_name:
    description:
      - The name of the Azure resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the Data Lake Analytics account.
    required: true
    type: str
  compute_policy_name:
    description:
      - The name of the compute policy to create or update.
      - The name of the compute policy to retrieve.
      - The name of the compute policy to update.
      - The name of the compute policy to delete.
    required: true
    type: str
  object_id:
    description:
      - The AAD object identifier for the entity to create a policy for.
    type: uuid
  object_type:
    description:
      - The type of AAD object the object identifier refers to.
    type: str
    choices:
      - User
      - Group
      - ServicePrincipal
  max_degree_of_parallelism_per_job:
    description:
      - >-
        The maximum degree of parallelism per job this user can use to submit
        jobs. This property, the min priority per job property, or both must be
        passed.
    type: integer
  min_priority_per_job:
    description:
      - >-
        The minimum priority per job this user can use to submit jobs. This
        property, the max degree of parallelism per job property, or both must
        be passed.
    type: integer
  state:
    description:
      - Assert the state of the ComputePolicy.
      - >-
        Use C(present) to create or update an ComputePolicy and C(absent) to
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
    - name: Creates or updates the specified compute policy
      azure_rm_computepolicy: 
        account_name: contosoadla
        compute_policy_name: test_policy
        resource_group_name: contosorg
        properties:
          max_degree_of_parallelism_per_job: 10
          min_priority_per_job: 30
          object_id: 776b9091-8916-4638-87f7-9c989a38da98
          object_type: User
        

    - name: Updates the specified compute policy
      azure_rm_computepolicy: 
        account_name: contosoadla
        compute_policy_name: test_policy
        resource_group_name: contosorg
        properties:
          max_degree_of_parallelism_per_job: 11
          min_priority_per_job: 31
        

    - name: Deletes the specified compute policy from the adla account
      azure_rm_computepolicy: 
        account_name: contosoadla
        compute_policy_name: test_policy
        resource_group_name: contosorg
        

'''

RETURN = '''
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
object_id:
  description:
    - The AAD object identifier for the entity to create a policy for.
  returned: always
  type: uuid
  sample: null
object_type:
  description:
    - The type of AAD object the object identifier refers to.
  returned: always
  type: str
  sample: null
max_degree_of_parallelism_per_job:
  description:
    - >-
      The maximum degree of parallelism per job this user can use to submit
      jobs.
  returned: always
  type: integer
  sample: null
min_priority_per_job:
  description:
    - The minimum priority per job this user can use to submit jobs.
  returned: always
  type: integer
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataLakeAnalyticsAccountManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMComputePolicy(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            compute_policy_name=dict(
                type='str',
                required=True
            ),
            object_id=dict(
                type='uuid',
                disposition='/object_id'
            ),
            object_type=dict(
                type='str',
                disposition='/object_type',
                choices=['User',
                         'Group',
                         'ServicePrincipal']
            ),
            max_degree_of_parallelism_per_job=dict(
                type='integer',
                disposition='/max_degree_of_parallelism_per_job'
            ),
            min_priority_per_job=dict(
                type='integer',
                disposition='/min_priority_per_job'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.compute_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMComputePolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataLakeAnalyticsAccountManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-11-01')

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
            response = self.mgmt_client.compute_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                          account_name=self.account_name,
                                                                          compute_policy_name=self.compute_policy_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ComputePolicy instance.')
            self.fail('Error creating the ComputePolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.compute_policies.delete(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                compute_policy_name=self.compute_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the ComputePolicy instance.')
            self.fail('Error deleting the ComputePolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.compute_policies.get(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name,
                                                             compute_policy_name=self.compute_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMComputePolicy()


if __name__ == '__main__':
    main()
