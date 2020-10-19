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
module: azure_rm_assignmentoperation_info
version_added: '2.9'
short_description: Get AssignmentOperation info.
description:
  - Get info of AssignmentOperation.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Assignment at management group scope
      azure_rm_assignmentoperation_info: 
        assignment_name: assignSimpleBlueprint
        resource_scope: managementGroups/ContosoOnlineGroup
        

    - name: Assignment at subscription scope
      azure_rm_assignmentoperation_info: 
        assignment_name: assignSimpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        

'''

RETURN = '''
assignment_operations:
  description: >-
    A list of dict results where the key is the name of the AssignmentOperation
    and the values are the facts for that AssignmentOperation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of AssignmentOperation.
      returned: always
      type: list
      sample: null
      contains:
        blueprint_version:
          description:
            - >-
              The published version of the blueprint definition used for the
              blueprint assignment operation.
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
    next_link:
      description:
        - Link to the next page of results.
      returned: always
      type: str
      sample: null
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
          The published version of the blueprint definition used for the
          blueprint assignment operation.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.blueprint import BlueprintManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAssignmentOperationInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_scope = None
        self.assignment_name = None
        self.assignment_operation_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-11-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAssignmentOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BlueprintManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-01-preview')

        if (self.resource_scope is not None and
            self.assignment_name is not None and
            self.assignment_operation_name is not None):
            self.results['assignment_operations'] = self.format_item(self.get())
        elif (self.resource_scope is not None and
              self.assignment_name is not None):
            self.results['assignment_operations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.assignment_operations.get(resource_scope=self.resource_scope,
                                                                  assignment_name=self.assignment_name,
                                                                  assignment_operation_name=self.assignment_operation_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.assignment_operations.list(resource_scope=self.resource_scope,
                                                                   assignment_name=self.assignment_name)
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
    AzureRMAssignmentOperationInfo()


if __name__ == '__main__':
    main()
