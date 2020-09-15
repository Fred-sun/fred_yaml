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
module: azure_rm_relationshiplink
version_added: '2.9'
short_description: Manage Azure RelationshipLink instance.
description:
  - 'Create, update and delete instance of Azure RelationshipLink.'
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
  relationship_link_name:
    description:
      - The name of the relationship link.
      - The name of the relationship.
    required: true
    type: str
  display_name:
    description:
      - Localized display name for the Relationship Link.
    type: dictionary
  description:
    description:
      - Localized descriptions for the Relationship Link.
    type: dictionary
  interaction_type:
    description:
      - The InteractionType associated with the Relationship Link.
    type: str
  mappings:
    description:
      - The mappings between Interaction and Relationship fields.
    type: list
    suboptions:
      interaction_field_name:
        description:
          - The field name on the Interaction Type.
        required: true
        type: str
      link_type:
        description:
          - Link type.
        type: sealed-choice
      relationship_field_name:
        description:
          - The field name on the Relationship metadata.
        required: true
        type: str
  profile_property_references:
    description:
      - The property references for the Profile of the Relationship.
    type: list
    suboptions:
      interaction_property_name:
        description:
          - >-
            The source interaction property that maps to the target profile
            property.
        required: true
        type: str
      profile_property_name:
        description:
          - >-
            The target profile property that maps to the source interaction
            property.
        required: true
        type: str
  related_profile_property_references:
    description:
      - The property references for the Related Profile of the Relationship.
    type: list
    suboptions:
      interaction_property_name:
        description:
          - >-
            The source interaction property that maps to the target profile
            property.
        required: true
        type: str
      profile_property_name:
        description:
          - >-
            The target profile property that maps to the source interaction
            property.
        required: true
        type: str
  relationship_name:
    description:
      - The Relationship associated with the Link.
    type: str
  state:
    description:
      - Assert the state of the RelationshipLink.
      - >-
        Use C(present) to create or update an RelationshipLink and C(absent) to
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
    - name: RelationshipLinks_CreateOrUpdate
      azure_rm_relationshiplink: 
        hub_name: sdkTestHub
        relationship_link_name: Somelink
        resource_group_name: TestHubRG
        properties:
          description:
            en-us: Link Description
          display_name:
            en-us: Link DisplayName
          interaction_type: testInteraction4332
          link_name: Somelink
          profile_property_references:
            - interaction_property_name: profile1
              profile_property_name: ProfileId
          related_profile_property_references:
            - interaction_property_name: profile1
              profile_property_name: ProfileId
          relationship_name: testProfile2326994
        

    - name: RelationshipLinks_Delete
      azure_rm_relationshiplink: 
        hub_name: sdkTestHub
        relationship_link_name: Somelink
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
display_name:
  description:
    - Localized display name for the Relationship Link.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - Localized descriptions for the Relationship Link.
  returned: always
  type: dictionary
  sample: null
interaction_type:
  description:
    - The InteractionType associated with the Relationship Link.
  returned: always
  type: str
  sample: null
link_name:
  description:
    - The name of the Relationship Link.
  returned: always
  type: str
  sample: null
mappings:
  description:
    - The mappings between Interaction and Relationship fields.
  returned: always
  type: list
  sample: null
  contains:
    interaction_field_name:
      description:
        - The field name on the Interaction Type.
      returned: always
      type: str
      sample: null
    link_type:
      description:
        - Link type.
      returned: always
      type: sealed-choice
      sample: null
    relationship_field_name:
      description:
        - The field name on the Relationship metadata.
      returned: always
      type: str
      sample: null
profile_property_references:
  description:
    - The property references for the Profile of the Relationship.
  returned: always
  type: list
  sample: null
  contains:
    interaction_property_name:
      description:
        - >-
          The source interaction property that maps to the target profile
          property.
      returned: always
      type: str
      sample: null
    profile_property_name:
      description:
        - >-
          The target profile property that maps to the source interaction
          property.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - Provisioning state.
  returned: always
  type: str
  sample: null
related_profile_property_references:
  description:
    - The property references for the Related Profile of the Relationship.
  returned: always
  type: list
  sample: null
  contains:
    interaction_property_name:
      description:
        - >-
          The source interaction property that maps to the target profile
          property.
      returned: always
      type: str
      sample: null
    profile_property_name:
      description:
        - >-
          The target profile property that maps to the source interaction
          property.
      returned: always
      type: str
      sample: null
relationship_name:
  description:
    - The Relationship associated with the Link.
  returned: always
  type: str
  sample: null
relationship_guid_id:
  description:
    - The relationship guid id.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The hub name.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRelationshipLink(AzureRMModuleBaseExt):
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
            relationship_link_name=dict(
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
            interaction_type=dict(
                type='str',
                disposition='/interaction_type'
            ),
            mappings=dict(
                type='list',
                disposition='/mappings',
                elements='dict',
                options=dict(
                    interaction_field_name=dict(
                        type='str',
                        disposition='interaction_field_name',
                        required=True
                    ),
                    link_type=dict(
                        type='sealed-choice',
                        disposition='link_type'
                    ),
                    relationship_field_name=dict(
                        type='str',
                        disposition='relationship_field_name',
                        required=True
                    )
                )
            ),
            profile_property_references=dict(
                type='list',
                disposition='/profile_property_references',
                elements='dict',
                options=dict(
                    interaction_property_name=dict(
                        type='str',
                        disposition='interaction_property_name',
                        required=True
                    ),
                    profile_property_name=dict(
                        type='str',
                        disposition='profile_property_name',
                        required=True
                    )
                )
            ),
            related_profile_property_references=dict(
                type='list',
                disposition='/related_profile_property_references',
                elements='dict',
                options=dict(
                    interaction_property_name=dict(
                        type='str',
                        disposition='interaction_property_name',
                        required=True
                    ),
                    profile_property_name=dict(
                        type='str',
                        disposition='profile_property_name',
                        required=True
                    )
                )
            ),
            relationship_name=dict(
                type='str',
                disposition='/relationship_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.relationship_link_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRelationshipLink, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.relationship_links.create_or_update(resource_group_name=self.resource_group_name,
                                                                            hub_name=self.hub_name,
                                                                            relationship_link_name=self.relationship_link_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RelationshipLink instance.')
            self.fail('Error creating the RelationshipLink instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.relationship_links.delete(resource_group_name=self.resource_group_name,
                                                                  hub_name=self.hub_name,
                                                                  relationship_link_name=self.relationship_link_name)
        except CloudError as e:
            self.log('Error attempting to delete the RelationshipLink instance.')
            self.fail('Error deleting the RelationshipLink instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.relationship_links.get(resource_group_name=self.resource_group_name,
                                                               hub_name=self.hub_name,
                                                               relationship_link_name=self.relationship_link_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRelationshipLink()


if __name__ == '__main__':
    main()
