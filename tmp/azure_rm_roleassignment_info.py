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
module: azure_rm_roleassignment_info
version_added: '2.9'
short_description: Get RoleAssignment info.
description:
  - Get info of RoleAssignment.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  hub_name:
    description:
      - The name of the hub.
    required: true
    type: str
  assignment_name:
    description:
      - The name of the role assignment.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RoleAssignments_ListByHub
      azure_rm_roleassignment_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

    - name: RoleAssignments_Get
      azure_rm_roleassignment_info: 
        assignment_name: assignmentName8976
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
role_assignments:
  description: >-
    A list of dict results where the key is the name of the RoleAssignment and
    the values are the facts for that RoleAssignment.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        tenant_id:
          description:
            - The hub name.
          returned: always
          type: str
          sample: null
        assignment_name:
          description:
            - The name of the metadata object.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - Localized display names for the metadata.
          returned: always
          type: dictionary
          sample: null
        description:
          description:
            - Localized description for the metadata.
          returned: always
          type: dictionary
          sample: null
        provisioning_state:
          description:
            - Provisioning state.
          returned: always
          type: str
          sample: null
        role:
          description:
            - Type of roles.
          returned: always
          type: sealed-choice
          sample: null
        principals:
          description:
            - The principals being assigned to.
          returned: always
          type: list
          sample: null
          contains:
            principal_id:
              description:
                - The principal id being assigned to.
              returned: always
              type: str
              sample: null
            principal_type:
              description:
                - The Type of the principal ID.
              returned: always
              type: str
              sample: null
            principal_metadata:
              description:
                - Other metadata for the principal.
              returned: always
              type: dictionary
              sample: null
        profiles:
          description:
            - Profiles set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        interactions:
          description:
            - Interactions set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        links:
          description:
            - Links set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        kpis:
          description:
            - Kpis set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        sas_policies:
          description:
            - Sas Policies set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        connectors:
          description:
            - Connectors set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        views:
          description:
            - Views set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        relationship_links:
          description:
            - The Role assignments set for the relationship links.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        relationships:
          description:
            - The Role assignments set for the relationships.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        widget_types:
          description:
            - Widget types set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        role_assignments:
          description:
            - The Role assignments set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        conflation_policies:
          description:
            - Widget types set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
        segments:
          description:
            - The Role assignments set for the assignment.
          returned: always
          type: dict
          sample: null
          contains:
            elements:
              description:
                - The elements included in the set.
              returned: always
              type: list
              sample: null
            exceptions:
              description:
                - >-
                  The elements that are not included in the set, in case
                  elements contains '*' indicating 'all'.
              returned: always
              type: list
              sample: null
    next_link:
      description:
        - Link to the next set of results.
      returned: always
      type: str
      sample: null
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
    tenant_id:
      description:
        - The hub name.
      returned: always
      type: str
      sample: null
    assignment_name:
      description:
        - The name of the metadata object.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Localized display names for the metadata.
      returned: always
      type: dictionary
      sample: null
    description:
      description:
        - Localized description for the metadata.
      returned: always
      type: dictionary
      sample: null
    provisioning_state:
      description:
        - Provisioning state.
      returned: always
      type: str
      sample: null
    role:
      description:
        - Type of roles.
      returned: always
      type: sealed-choice
      sample: null
    principals:
      description:
        - The principals being assigned to.
      returned: always
      type: list
      sample: null
      contains:
        principal_id:
          description:
            - The principal id being assigned to.
          returned: always
          type: str
          sample: null
        principal_type:
          description:
            - The Type of the principal ID.
          returned: always
          type: str
          sample: null
        principal_metadata:
          description:
            - Other metadata for the principal.
          returned: always
          type: dictionary
          sample: null
    profiles:
      description:
        - Profiles set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    interactions:
      description:
        - Interactions set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    links:
      description:
        - Links set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    kpis:
      description:
        - Kpis set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    sas_policies:
      description:
        - Sas Policies set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    connectors:
      description:
        - Connectors set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    views:
      description:
        - Views set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    relationship_links:
      description:
        - The Role assignments set for the relationship links.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    relationships:
      description:
        - The Role assignments set for the relationships.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    widget_types:
      description:
        - Widget types set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    role_assignments:
      description:
        - The Role assignments set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    conflation_policies:
      description:
        - Widget types set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
          returned: always
          type: list
          sample: null
    segments:
      description:
        - The Role assignments set for the assignment.
      returned: always
      type: dict
      sample: null
      contains:
        elements:
          description:
            - The elements included in the set.
          returned: always
          type: list
          sample: null
        exceptions:
          description:
            - >-
              The elements that are not included in the set, in case elements
              contains '*' indicating 'all'.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRoleAssignmentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            hub_name=dict(
                type='str',
                required=True
            ),
            assignment_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.assignment_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-26'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRoleAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.assignment_name is not None):
            self.results['role_assignments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['role_assignments'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.get(resource_group_name=self.resource_group_name,
                                                             hub_name=self.hub_name,
                                                             assignment_name=self.assignment_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.list_by_hub(resource_group_name=self.resource_group_name,
                                                                     hub_name=self.hub_name)
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
    AzureRMRoleAssignmentInfo()


if __name__ == '__main__':
    main()
