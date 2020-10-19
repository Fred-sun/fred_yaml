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
module: azure_rm_solution_info
version_added: '2.9'
short_description: Get Solution info.
description:
  - Get info of Solution.
options:
  resource_group_name:
    description:
      - The name of the resource group to get. The name is case insensitive.
    type: str
  solution_name:
    description:
      - User Solution Name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SolutionGet
      azure_rm_solution_info: 
        resource_group_name: rg1
        solution_name: solution1
        

    - name: SolutionList
      azure_rm_solution_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
solutions:
  description: >-
    A list of dict results where the key is the name of the Solution and the
    values are the facts for that Solution.
  returned: always
  type: complex
  contains:
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
          Plan for solution object supported by the OperationsManagement
          resource provider.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              name of the solution to be created. For Microsoft published
              solution it should be in the format of
              solutionType(workspaceName). SolutionType part is case sensitive.
              For third party solution, it can be anything.
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
              name of the solution to enabled/add. For Microsoft published
              gallery solution it should be in the format of
              OMSGallery/<solutionType>. This is case sensitive
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
              The azure resources that will be contained within the solutions.
              They will be locked and gets deleted automatically when the
              solution is deleted.
          returned: always
          type: list
          sample: null
        referenced_resources:
          description:
            - >-
              The resources that will be referenced from this solution. Deleting
              any of those solution out of band will break the solution.
          returned: always
          type: list
          sample: null
    value:
      description:
        - List of solution properties within the subscription.
      returned: always
      type: list
      sample: null
      contains:
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
              Plan for solution object supported by the OperationsManagement
              resource provider.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  name of the solution to be created. For Microsoft published
                  solution it should be in the format of
                  solutionType(workspaceName). SolutionType part is case
                  sensitive. For third party solution, it can be anything.
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
                  name of the solution to enabled/add. For Microsoft published
                  gallery solution it should be in the format of
                  OMSGallery/<solutionType>. This is case sensitive
              returned: always
              type: str
              sample: null
        properties:
          description:
            - >-
              Properties for solution object supported by the
              OperationsManagement resource provider.
          returned: always
          type: dict
          sample: null
          contains:
            workspace_resource_id:
              description:
                - >-
                  The azure resourceId for the workspace where the solution will
                  be deployed/enabled.
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
                  The azure resources that will be contained within the
                  solutions. They will be locked and gets deleted automatically
                  when the solution is deleted.
              returned: always
              type: list
              sample: null
            referenced_resources:
              description:
                - >-
                  The resources that will be referenced from this solution.
                  Deleting any of those solution out of band will break the
                  solution.
              returned: always
              type: list
              sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.operations import OperationsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSolutionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            solution_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.solution_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-11-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSolutionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(OperationsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-11-01-preview')

        if (self.resource_group_name is not None and
            self.solution_name is not None):
            self.results['solutions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['solutions'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['solutions'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.solutions.get(resource_group_name=self.resource_group_name,
                                                      solution_name=self.solution_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.solutions.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.solutions.list_by_subscription()
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
    AzureRMSolutionInfo()


if __name__ == '__main__':
    main()
