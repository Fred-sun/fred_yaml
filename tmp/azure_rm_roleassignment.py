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
module: azure_rm_roleassignment
version_added: '2.9'
short_description: Manage Azure RoleAssignment instance.
description:
  - 'Create, update and delete instance of Azure RoleAssignment.'
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
      - The assignment name
      - The name of the role assignment.
    required: true
    type: str
  display_name:
    description:
      - Localized display names for the metadata.
    type: dictionary
  description:
    description:
      - Localized description for the metadata.
    type: dictionary
  role:
    description:
      - Type of roles.
    type: sealed-choice
  principals:
    description:
      - The principals being assigned to.
    type: list
    suboptions:
      principal_id:
        description:
          - The principal id being assigned to.
        required: true
        type: str
      principal_type:
        description:
          - The Type of the principal ID.
        required: true
        type: str
      principal_metadata:
        description:
          - Other metadata for the principal.
        type: dictionary
  profiles:
    description:
      - Profiles set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  interactions:
    description:
      - Interactions set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  links:
    description:
      - Links set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  kpis:
    description:
      - Kpis set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  sas_policies:
    description:
      - Sas Policies set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  connectors:
    description:
      - Connectors set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  views:
    description:
      - Views set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  relationship_links:
    description:
      - The Role assignments set for the relationship links.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  relationships:
    description:
      - The Role assignments set for the relationships.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  widget_types:
    description:
      - Widget types set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  role_assignments:
    description:
      - The Role assignments set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  conflation_policies:
    description:
      - Widget types set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  segments:
    description:
      - The Role assignments set for the assignment.
    type: dict
    suboptions:
      elements:
        description:
          - The elements included in the set.
        type: list
      exceptions:
        description:
          - >-
            The elements that are not included in the set, in case elements
            contains '*' indicating 'all'.
        type: list
  state:
    description:
      - Assert the state of the RoleAssignment.
      - >-
        Use C(present) to create or update an RoleAssignment and C(absent) to
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
    - name: RoleAssignments_CreateOrUpdate
      azure_rm_roleassignment: 
        assignment_name: assignmentName8976
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        properties:
          principals:
            - principal_id: 4c54c38ffa9b416ba5a6d6c8a20cbe7e
              principal_type: User
            - principal_id: 93061d15a5054f2b9948ae25724cf9d5
              principal_type: User
          role: Admin
        

    - name: RoleAssignments_Delete
      azure_rm_roleassignment: 
        assignment_name: assignmentName8976
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRoleAssignment(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            display_name=dict(
                type='dictionary',
                disposition='/display_name'
            ),
            description=dict(
                type='dictionary',
                disposition='/description'
            ),
            role=dict(
                type='sealed-choice',
                disposition='/role'
            ),
            principals=dict(
                type='list',
                disposition='/principals',
                elements='dict',
                options=dict(
                    principal_id=dict(
                        type='str',
                        disposition='principal_id',
                        required=True
                    ),
                    principal_type=dict(
                        type='str',
                        disposition='principal_type',
                        required=True
                    ),
                    principal_metadata=dict(
                        type='dictionary',
                        disposition='principal_metadata'
                    )
                )
            ),
            profiles=dict(
                type='dict',
                disposition='/profiles',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            interactions=dict(
                type='dict',
                disposition='/interactions',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            links=dict(
                type='dict',
                disposition='/links',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            kpis=dict(
                type='dict',
                disposition='/kpis',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            sas_policies=dict(
                type='dict',
                disposition='/sas_policies',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            connectors=dict(
                type='dict',
                disposition='/connectors',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            views=dict(
                type='dict',
                disposition='/views',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            relationship_links=dict(
                type='dict',
                disposition='/relationship_links',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            relationships=dict(
                type='dict',
                disposition='/relationships',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            widget_types=dict(
                type='dict',
                disposition='/widget_types',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            role_assignments=dict(
                type='dict',
                disposition='/role_assignments',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            conflation_policies=dict(
                type='dict',
                disposition='/conflation_policies',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
                        elements='str'
                    )
                )
            ),
            segments=dict(
                type='dict',
                disposition='/segments',
                options=dict(
                    elements=dict(
                        type='list',
                        disposition='elements',
                        elements='str'
                    ),
                    exceptions=dict(
                        type='list',
                        disposition='exceptions',
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
        self.hub_name = None
        self.assignment_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRoleAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

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
            response = self.mgmt_client.role_assignments.create_or_update(resource_group_name=self.resource_group_name,
                                                                          hub_name=self.hub_name,
                                                                          assignment_name=self.assignment_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RoleAssignment instance.')
            self.fail('Error creating the RoleAssignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.role_assignments.delete(resource_group_name=self.resource_group_name,
                                                                hub_name=self.hub_name,
                                                                assignment_name=self.assignment_name)
        except CloudError as e:
            self.log('Error attempting to delete the RoleAssignment instance.')
            self.fail('Error deleting the RoleAssignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.role_assignments.get(resource_group_name=self.resource_group_name,
                                                             hub_name=self.hub_name,
                                                             assignment_name=self.assignment_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRoleAssignment()


if __name__ == '__main__':
    main()
