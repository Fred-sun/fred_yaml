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
module: azure_rm_assignmentoperation
version_added: '2.9'
short_description: Manage Azure AssignmentOperation instance.
description:
  - 'Create, update and delete instance of Azure AssignmentOperation.'
options:
  resource_scope:
    description:
      - >-
        The scope of the resource. Valid scopes are: management group (format:
        '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
        subscription (format: '/subscriptions/{subscriptionId}').
    required: true
    type: str
  assignment_name:
    description:
      - Name of the blueprint assignment.
    required: true
    type: str
  assignment_operation_name:
    description:
      - Name of the blueprint assignment operation.
    required: true
    type: str
  state:
    description:
      - Assert the state of the AssignmentOperation.
      - >-
        Use C(present) to create or update an AssignmentOperation and C(absent)
        to delete it.
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
    - String Id used to locate any resource on Azure.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of this resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of this resource.
  returned: always
  type: str
  sample: null
blueprint_version:
  description:
    - >-
      The published version of the blueprint definition used for the blueprint
      assignment operation.
  returned: always
  type: str
  sample: null
assignment_state:
  description:
    - State of this blueprint assignment operation.
  returned: always
  type: str
  sample: null
time_created:
  description:
    - Create time of this blueprint assignment operation.
  returned: always
  type: str
  sample: null
time_started:
  description:
    - Start time of the underlying deployment.
  returned: always
  type: str
  sample: null
time_finished:
  description:
    - Finish time of the overall underlying deployments.
  returned: always
  type: str
  sample: null
deployments:
  description:
    - List of jobs in this blueprint assignment operation.
  returned: always
  type: list
  sample: null
  contains:
    kind:
      description:
        - Kind of job.
      returned: always
      type: str
      sample: null
    action:
      description:
        - Name of the action performed in this job.
      returned: always
      type: str
      sample: null
    job_id:
      description:
        - Id of this job.
      returned: always
      type: str
      sample: null
    job_state:
      description:
        - State of this job.
      returned: always
      type: str
      sample: null
    result:
      description:
        - Deployment job result.
      returned: always
      type: dict
      sample: null
      contains:
        error:
          description:
            - Contains error details if deployment job failed.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - Error code.
              returned: always
              type: str
              sample: null
            message:
              description:
                - Error message.
              returned: always
              type: str
              sample: null
        resources:
          description:
            - Resources created as result of the deployment job.
          returned: always
          type: list
          sample: null
          contains:
            properties:
              description:
                - Additional properties in a dictionary.
              returned: always
              type: dictionary
              sample: null
    history:
      description:
        - Result of this deployment job for each retry.
      returned: always
      type: list
      sample: null
      contains:
        error:
          description:
            - Contains error details if deployment job failed.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - Error code.
              returned: always
              type: str
              sample: null
            message:
              description:
                - Error message.
              returned: always
              type: str
              sample: null
        resources:
          description:
            - Resources created as result of the deployment job.
          returned: always
          type: list
          sample: null
          contains:
            properties:
              description:
                - Additional properties in a dictionary.
              returned: always
              type: dictionary
              sample: null
    request_uri:
      description:
        - Reference to deployment job resource id.
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
    from azure.mgmt.blueprint import BlueprintManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAssignmentOperation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_scope=dict(
                type='str',
                required=True
            ),
            assignment_name=dict(
                type='str',
                required=True
            ),
            assignment_operation_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_scope = None
        self.assignment_name = None
        self.assignment_operation_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAssignmentOperation, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(BlueprintManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-01-preview')

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
                response = self.mgmt_client.assignment_operations.create()
            else:
                response = self.mgmt_client.assignment_operations.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AssignmentOperation instance.')
            self.fail('Error creating the AssignmentOperation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.assignment_operations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the AssignmentOperation instance.')
            self.fail('Error deleting the AssignmentOperation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.assignment_operations.get(resource_scope=self.resource_scope,
                                                                  assignment_name=self.assignment_name,
                                                                  assignment_operation_name=self.assignment_operation_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAssignmentOperation()


if __name__ == '__main__':
    main()
