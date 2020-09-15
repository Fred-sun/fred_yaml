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
module: azure_rm_assignment
version_added: '2.9'
short_description: Manage Azure Assignment instance.
description:
  - 'Create, update and delete instance of Azure Assignment.'
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
  location:
    description:
      - The location of this blueprint assignment.
    type: str
  display_name:
    description:
      - One-liner string explain this resource.
    type: str
  description:
    description:
      - Multi-line explain this resource.
    type: str
  blueprint_id:
    description:
      - ID of the published version of a blueprint definition.
    type: str
  scope:
    description:
      - >-
        The target subscription scope of the blueprint assignment (format:
        '/subscriptions/{subscriptionId}'). For management group level
        assignments, the property is required.
    type: str
  parameters:
    description:
      - Blueprint assignment parameter values.
    type: dictionary
  resource_groups:
    description:
      - Names and locations of resource group placeholders.
    type: dictionary
  locks:
    description:
      - Defines how resources deployed by a blueprint assignment are locked.
    type: dict
    suboptions:
      mode:
        description:
          - Lock mode.
        type: str
        choices:
          - None
          - AllResourcesReadOnly
          - AllResourcesDoNotDelete
      excluded_principals:
        description:
          - >-
            List of AAD principals excluded from blueprint locks. Up to 5
            principals are permitted.
        type: list
      excluded_actions:
        description:
          - "List\_of\_management\_operations\_that\_are\_excluded\_from\_blueprint\_locks.\_Up\_to\_200\_actions\_are\_permitted. If the lock mode is set to 'AllResourcesReadOnly', then the following actions are automatically appended to 'excludedActions': '*/read', 'Microsoft.Network/virtualNetworks/subnets/join/action' and 'Microsoft.Authorization/locks/delete'. If the lock mode is set to 'AllResourcesDoNotDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will get removed."
        type: list
  type:
    description:
      - Type of the managed identity.
    type: str
    choices:
      - None
      - SystemAssigned
      - UserAssigned
  principal_id:
    description:
      - Azure Active Directory principal ID associated with this Identity.
    type: str
  tenant_id:
    description:
      - ID of the Azure Active Directory.
    type: str
  user_assigned_identities:
    description:
      - >-
        The list of user-assigned managed identities associated with the
        resource. Key is the Azure resource Id of the managed identity.
    type: dictionary
  delete_behavior:
    description:
      - >-
        When deleteBehavior=all, the resources that were created by the
        blueprint assignment will be deleted.
    type: str
    choices:
      - none
      - all
  state:
    description:
      - Assert the state of the Assignment.
      - >-
        Use C(present) to create or update an Assignment and C(absent) to delete
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
    - name: Assignment with system-assigned managed identity at management group scope
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        resource_scope: managementGroups/ContosoOnlineGroup
        identity:
          type: SystemAssigned
        location: eastus
        properties:
          description: enforce pre-defined simpleBlueprint to this XXXXXXXX subscription.
          blueprint_id: >-
            /providers/Microsoft.Management/managementGroups/ContosoOnlineGroup/providers/Microsoft.Blueprint/blueprints/simpleBlueprint
          parameters:
            cost_center:
              value: Contoso/Online/Shopping/Production
            owners:
              value:
                - johnDoe@contoso.com
                - johnsteam@contoso.com
            storage_account_type:
              value: Standard_LRS
          resource_groups:
            storage_rg:
              name: defaultRG
              location: eastus
          scope: subscriptions/00000000-0000-0000-0000-000000000000
        

    - name: Assignment with system-assigned managed identity at subscription scope
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        identity:
          type: SystemAssigned
        location: eastus
        properties:
          description: enforce pre-defined simpleBlueprint to this XXXXXXXX subscription.
          blueprint_id: >-
            /providers/Microsoft.Management/managementGroups/ContosoOnlineGroup/providers/Microsoft.Blueprint/blueprints/simpleBlueprint
          parameters:
            cost_center:
              value: Contoso/Online/Shopping/Production
            owners:
              value:
                - johnDoe@contoso.com
                - johnsteam@contoso.com
            storage_account_type:
              value: Standard_LRS
          resource_groups:
            storage_rg:
              name: defaultRG
              location: eastus
        

    - name: Assignment with user-assigned managed identity at management group scope
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        resource_scope: managementGroups/ContosoOnlineGroup
        identity:
          type: UserAssigned
          user_assigned_identities:
            /subscriptions/00000000-0000-0000-0000-000000000000/resource_groups/contoso-resource-group/providers/microsoft.managed_identity/user_assigned_identities/contoso-identity: {}
        location: eastus
        properties:
          description: enforce pre-defined simpleBlueprint to this XXXXXXXX subscription.
          blueprint_id: >-
            /providers/Microsoft.Management/managementGroups/ContosoOnlineGroup/providers/Microsoft.Blueprint/blueprints/simpleBlueprint
          parameters:
            cost_center:
              value: Contoso/Online/Shopping/Production
            owners:
              value:
                - johnDoe@contoso.com
                - johnsteam@contoso.com
            storage_account_type:
              value: Standard_LRS
          resource_groups:
            storage_rg:
              name: defaultRG
              location: eastus
          scope: subscriptions/00000000-0000-0000-0000-000000000000
        

    - name: Assignment with user-assigned managed identity at subscription scope
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        identity:
          type: UserAssigned
          user_assigned_identities:
            /subscriptions/00000000-0000-0000-0000-000000000000/resource_groups/contoso-resource-group/providers/microsoft.managed_identity/user_assigned_identities/contoso-identity: {}
        location: eastus
        properties:
          description: enforce pre-defined simpleBlueprint to this XXXXXXXX subscription.
          blueprint_id: >-
            /providers/Microsoft.Management/managementGroups/ContosoOnlineGroup/providers/Microsoft.Blueprint/blueprints/simpleBlueprint
          parameters:
            cost_center:
              value: Contoso/Online/Shopping/Production
            owners:
              value:
                - johnDoe@contoso.com
                - johnsteam@contoso.com
            storage_account_type:
              value: Standard_LRS
          resource_groups:
            storage_rg:
              name: defaultRG
              location: eastus
        

    - name: Assignment_Delete at management group scope
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        resource_scope: managementGroups/ContosoOnlineGroup
        

    - name: Assignment_Delete at management group scope, and delete the resources created by the assignment
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        delete_behavior: all
        resource_scope: managementGroups/ContosoOnlineGroup
        

    - name: Assignment_Delete at subscription scope
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        

    - name: Assignment_Delete at subscription scope, and delete the resources created by the assignment
      azure_rm_assignment: 
        assignment_name: assignSimpleBlueprint
        delete_behavior: all
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        

'''

RETURN = '''
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
      The list of user-assigned managed identities associated with the resource.
      Key is the Azure resource Id of the managed identity.
  returned: always
  type: dictionary
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


class AzureRMAssignment(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            blueprint_id=dict(
                type='str',
                disposition='/blueprint_id'
            ),
            scope=dict(
                type='str',
                disposition='/scope'
            ),
            parameters=dict(
                type='dictionary',
                disposition='/parameters'
            ),
            resource_groups=dict(
                type='dictionary',
                disposition='/resource_groups'
            ),
            locks=dict(
                type='dict',
                disposition='/locks',
                options=dict(
                    mode=dict(
                        type='str',
                        disposition='mode',
                        choices=['None',
                                 'AllResourcesReadOnly',
                                 'AllResourcesDoNotDelete']
                    ),
                    excluded_principals=dict(
                        type='list',
                        disposition='excluded_principals',
                        elements='str'
                    ),
                    excluded_actions=dict(
                        type='list',
                        disposition='excluded_actions',
                        elements='str'
                    )
                )
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['None',
                         'SystemAssigned',
                         'UserAssigned']
            ),
            principal_id=dict(
                type='str',
                disposition='/principal_id'
            ),
            tenant_id=dict(
                type='str',
                disposition='/tenant_id'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            delete_behavior=dict(
                type='str',
                choices=['none',
                         'all']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_scope = None
        self.assignment_name = None
        self.delete_behavior = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.assignments.create_or_update(resource_scope=self.resource_scope,
                                                                     assignment_name=self.assignment_name,
                                                                     assignment=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Assignment instance.')
            self.fail('Error creating the Assignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.assignments.delete(resource_scope=self.resource_scope,
                                                           assignment_name=self.assignment_name,
                                                           delete_behavior=self.delete_behavior)
        except CloudError as e:
            self.log('Error attempting to delete the Assignment instance.')
            self.fail('Error deleting the Assignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.assignments.get(resource_scope=self.resource_scope,
                                                        assignment_name=self.assignment_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAssignment()


if __name__ == '__main__':
    main()
