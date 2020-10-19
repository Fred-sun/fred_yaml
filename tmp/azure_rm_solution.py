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
module: azure_rm_solution
version_added: '2.9'
short_description: Manage Azure Solution instance.
description:
  - 'Create, update and delete instance of Azure Solution.'
options:
  resource_group_name:
    description:
      - The name of the resource group to get. The name is case insensitive.
    required: true
    type: str
  solution_name:
    description:
      - User Solution Name.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  plan:
    description:
      - >-
        Plan for solution object supported by the OperationsManagement resource
        provider.
    type: dict
    suboptions:
      name:
        description:
          - >-
            name of the solution to be created. For Microsoft published solution
            it should be in the format of solutionType(workspaceName).
            SolutionType part is case sensitive. For third party solution, it
            can be anything.
        type: str
      publisher:
        description:
          - 'Publisher name. For gallery solution, it is Microsoft.'
        type: str
      promotion_code:
        description:
          - 'promotionCode, Not really used now, can you left as empty'
        type: str
      product:
        description:
          - >-
            name of the solution to enabled/add. For Microsoft published gallery
            solution it should be in the format of OMSGallery/<solutionType>.
            This is case sensitive
        type: str
  properties:
    description:
      - >-
        Properties for solution object supported by the OperationsManagement
        resource provider.
    type: dict
    suboptions:
      workspace_resource_id:
        description:
          - >-
            The azure resourceId for the workspace where the solution will be
            deployed/enabled.
        required: true
        type: str
      provisioning_state:
        description:
          - The provisioning state for the solution.
        type: str
      contained_resources:
        description:
          - >-
            The azure resources that will be contained within the solutions.
            They will be locked and gets deleted automatically when the solution
            is deleted.
        type: list
      referenced_resources:
        description:
          - >-
            The resources that will be referenced from this solution. Deleting
            any of those solution out of band will break the solution.
        type: list
  state:
    description:
      - Assert the state of the Solution.
      - >-
        Use C(present) to create or update an Solution and C(absent) to delete
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
    - name: SolutionCreate
      azure_rm_solution: 
        resource_group_name: rg1
        solution_name: solution1
        location: East US
        plan:
          name: name1
          product: product1
          promotion_code: promocode1
          publisher: publisher1
        properties:
          contained_resources:
            - >-
              /subscriptions/sub2/resourceGroups/rg2/providers/provider1/resources/resource1
            - >-
              /subscriptions/sub2/resourceGroups/rg2/providers/provider2/resources/resource2
          referenced_resources:
            - >-
              /subscriptions/sub2/resourceGroups/rg2/providers/provider1/resources/resource2
            - >-
              /subscriptions/sub2/resourceGroups/rg2/providers/provider2/resources/resource3
          workspace_resource_id: >-
            /subscriptions/sub2/resourceGroups/rg2/providers/Microsoft.OperationalInsights/workspaces/ws1
        

    - name: SolutionUpdate
      azure_rm_solution: 
        resource_group_name: rg1
        solution_name: solution1
        tags:
          dept: IT
          environment: Test
        

    - name: SolutionDelete
      azure_rm_solution: 
        resource_group_name: rg1
        solution_name: solution1
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
plan:
  description:
    - >-
      Plan for solution object supported by the OperationsManagement resource
      provider.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - >-
          name of the solution to be created. For Microsoft published solution
          it should be in the format of solutionType(workspaceName).
          SolutionType part is case sensitive. For third party solution, it can
          be anything.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - 'Publisher name. For gallery solution, it is Microsoft.'
      returned: always
      type: str
      sample: null
    promotion_code:
      description:
        - 'promotionCode, Not really used now, can you left as empty'
      returned: always
      type: str
      sample: null
    product:
      description:
        - >-
          name of the solution to enabled/add. For Microsoft published gallery
          solution it should be in the format of OMSGallery/<solutionType>. This
          is case sensitive
      returned: always
      type: str
      sample: null
properties:
  description:
    - >-
      Properties for solution object supported by the OperationsManagement
      resource provider.
  returned: always
  type: dict
  sample: null
  contains:
    workspace_resource_id:
      description:
        - >-
          The azure resourceId for the workspace where the solution will be
          deployed/enabled.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state for the solution.
      returned: always
      type: str
      sample: null
    contained_resources:
      description:
        - >-
          The azure resources that will be contained within the solutions. They
          will be locked and gets deleted automatically when the solution is
          deleted.
      returned: always
      type: list
      sample: null
    referenced_resources:
      description:
        - >-
          The resources that will be referenced from this solution. Deleting any
          of those solution out of band will break the solution.
      returned: always
      type: list
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.operations import OperationsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSolution(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            solution_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            plan=dict(
                type='dict',
                disposition='/plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='promotion_code'
                    ),
                    product=dict(
                        type='str',
                        disposition='product'
                    )
                )
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    workspace_resource_id=dict(
                        type='str',
                        disposition='workspace_resource_id',
                        required=True
                    ),
                    provisioning_state=dict(
                        type='str',
                        updatable=False,
                        disposition='provisioning_state'
                    ),
                    contained_resources=dict(
                        type='list',
                        disposition='contained_resources',
                        elements='str'
                    ),
                    referenced_resources=dict(
                        type='list',
                        disposition='referenced_resources',
                        elements='str'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.solution_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSolution, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(OperationsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-11-01-preview')

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
            response = self.mgmt_client.solutions.create_or_update(resource_group_name=self.resource_group_name,
                                                                   solution_name=self.solution_name,
                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Solution instance.')
            self.fail('Error creating the Solution instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.solutions.delete(resource_group_name=self.resource_group_name,
                                                         solution_name=self.solution_name)
        except CloudError as e:
            self.log('Error attempting to delete the Solution instance.')
            self.fail('Error deleting the Solution instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.solutions.get(resource_group_name=self.resource_group_name,
                                                      solution_name=self.solution_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSolution()


if __name__ == '__main__':
    main()
