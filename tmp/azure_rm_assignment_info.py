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
module: azure_rm_assignment_info
version_added: '2.9'
short_description: Get Assignment info.
description:
  - Get info of Assignment.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Assignment at management group scope
      azure_rm_assignment_info: 
        assignment_name: assignSimpleBlueprint
        resource_scope: managementGroups/ContosoOnlineGroup
        

    - name: Assignment at subscription scope
      azure_rm_assignment_info: 
        assignment_name: assignSimpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        

'''

RETURN = '''
assignments:
  description: >-
    A list of dict results where the key is the name of the Assignment and the
    values are the facts for that Assignment.
  returned: always
  type: complex
  contains:
    location:
      description:
        - The location of this blueprint assignment.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - One-liner string explain this resource.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Multi-line explain this resource.
      returned: always
      type: str
      sample: null
    blueprint_id:
      description:
        - ID of the published version of a blueprint definition.
      returned: always
      type: str
      sample: null
    scope:
      description:
        - >-
          The target subscription scope of the blueprint assignment (format:
          '/subscriptions/{subscriptionId}'). For management group level
          assignments, the property is required.
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - Blueprint assignment parameter values.
      returned: always
      type: dictionary
      sample: null
    resource_groups:
      description:
        - Names and locations of resource group placeholders.
      returned: always
      type: dictionary
      sample: null
    status:
      description:
        - Status of blueprint assignment. This field is readonly.
      returned: always
      type: dict
      sample: null
      contains:
        managed_resources:
          description:
            - List of resources that were created by the blueprint assignment.
          returned: always
          type: list
          sample: null
    locks:
      description:
        - Defines how resources deployed by a blueprint assignment are locked.
      returned: always
      type: dict
      sample: null
      contains:
        mode:
          description:
            - Lock mode.
          returned: always
          type: str
          sample: null
        excluded_principals:
          description:
            - >-
              List of AAD principals excluded from blueprint locks. Up to 5
              principals are permitted.
          returned: always
          type: list
          sample: null
        excluded_actions:
          description:
            - "List\_of\_management\_operations\_that\_are\_excluded\_from\_blueprint\_locks.\_Up\_to\_200\_actions\_are\_permitted. If the lock mode is set to 'AllResourcesReadOnly', then the following actions are automatically appended to 'excludedActions': '*/read', 'Microsoft.Network/virtualNetworks/subnets/join/action' and 'Microsoft.Authorization/locks/delete'. If the lock mode is set to 'AllResourcesDoNotDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will get removed."
          returned: always
          type: list
          sample: null
    provisioning_state:
      description:
        - State of the blueprint assignment.
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - Type of the managed identity.
      returned: always
      type: str
      sample: null
    principal_id:
      description:
        - Azure Active Directory principal ID associated with this Identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - ID of the Azure Active Directory.
      returned: always
      type: str
      sample: null
    user_assigned_identities:
      description:
        - >-
          The list of user-assigned managed identities associated with the
          resource. Key is the Azure resource Id of the managed identity.
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - List of blueprint assignments.
      returned: always
      type: list
      sample: null
      contains:
        display_name:
          description:
            - One-liner string explain this resource.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Multi-line explain this resource.
          returned: always
          type: str
          sample: null
        blueprint_id:
          description:
            - ID of the published version of a blueprint definition.
          returned: always
          type: str
          sample: null
        scope:
          description:
            - >-
              The target subscription scope of the blueprint assignment (format:
              '/subscriptions/{subscriptionId}'). For management group level
              assignments, the property is required.
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - Blueprint assignment parameter values.
          returned: always
          type: dictionary
          sample: null
        resource_groups:
          description:
            - Names and locations of resource group placeholders.
          returned: always
          type: dictionary
          sample: null
        status:
          description:
            - Status of blueprint assignment. This field is readonly.
          returned: always
          type: dict
          sample: null
          contains:
            managed_resources:
              description:
                - >-
                  List of resources that were created by the blueprint
                  assignment.
              returned: always
              type: list
              sample: null
        locks:
          description:
            - >-
              Defines how resources deployed by a blueprint assignment are
              locked.
          returned: always
          type: dict
          sample: null
          contains:
            mode:
              description:
                - Lock mode.
              returned: always
              type: str
              sample: null
            excluded_principals:
              description:
                - >-
                  List of AAD principals excluded from blueprint locks. Up to 5
                  principals are permitted.
              returned: always
              type: list
              sample: null
            excluded_actions:
              description:
                - "List\_of\_management\_operations\_that\_are\_excluded\_from\_blueprint\_locks.\_Up\_to\_200\_actions\_are\_permitted. If the lock mode is set to 'AllResourcesReadOnly', then the following actions are automatically appended to 'excludedActions': '*/read', 'Microsoft.Network/virtualNetworks/subnets/join/action' and 'Microsoft.Authorization/locks/delete'. If the lock mode is set to 'AllResourcesDoNotDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will get removed."
              returned: always
              type: list
              sample: null
        provisioning_state:
          description:
            - State of the blueprint assignment.
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - Type of the managed identity.
          returned: always
          type: str
          sample: null
        principal_id:
          description:
            - Azure Active Directory principal ID associated with this Identity.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - ID of the Azure Active Directory.
          returned: always
          type: str
          sample: null
        user_assigned_identities:
          description:
            - >-
              The list of user-assigned managed identities associated with the
              resource. Key is the Azure resource Id of the managed identity.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - Link to the next page of results.
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


class AzureRMAssignmentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_scope=dict(
                type='str',
                required=True
            ),
            assignment_name=dict(
                type='str'
            )
        )

        self.resource_scope = None
        self.assignment_name = None

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
        super(AzureRMAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BlueprintManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-01-preview')

        if (self.resource_scope is not None and
            self.assignment_name is not None):
            self.results['assignments'] = self.format_item(self.get())
        elif (self.resource_scope is not None):
            self.results['assignments'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.assignments.get(resource_scope=self.resource_scope,
                                                        assignment_name=self.assignment_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.assignments.list(resource_scope=self.resource_scope)
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
    AzureRMAssignmentInfo()


if __name__ == '__main__':
    main()
