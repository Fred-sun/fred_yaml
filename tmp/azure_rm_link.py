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
module: azure_rm_link
version_added: '2.9'
short_description: Manage Azure Link instance.
description:
  - 'Create, update and delete instance of Azure Link.'
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
  link_name:
    description:
      - The name of the link.
    required: true
    type: str
  source_entity_type:
    description:
      - Type of source entity.
    type: sealed-choice
  target_entity_type:
    description:
      - Type of target entity.
    type: sealed-choice
  source_entity_type_name:
    description:
      - Name of the source Entity Type.
    type: str
  target_entity_type_name:
    description:
      - Name of the target Entity Type.
    type: str
  display_name:
    description:
      - Localized display name for the Link.
    type: dictionary
  description:
    description:
      - Localized descriptions for the Link.
    type: dictionary
  mappings:
    description:
      - The set of properties mappings between the source and target Types.
    type: list
    suboptions:
      source_property_name:
        description:
          - ' Property name on the source Entity Type.'
        required: true
        type: str
      target_property_name:
        description:
          - Property name on the target Entity Type.
        required: true
        type: str
      link_type:
        description:
          - Link type.
        type: sealed-choice
  participant_property_references:
    description:
      - The properties that represent the participating profile.
    type: list
    suboptions:
      source_property_name:
        description:
          - The source property that maps to the target property.
        required: true
        type: str
      target_property_name:
        description:
          - The target property that maps to the source property.
        required: true
        type: str
  reference_only:
    description:
      - >-
        Indicating whether the link is reference only link. This flag is ignored
        if the Mappings are defined. If the mappings are not defined and it is
        set to true, links processing will not create or update profiles.
    type: bool
  operation_type:
    description:
      - >-
        Determines whether this link is supposed to create or delete instances
        if Link is NOT Reference Only.
    type: sealed-choice
  state:
    description:
      - Assert the state of the Link.
      - Use C(present) to create or update an Link and C(absent) to delete it.
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
    - name: Links_CreateOrUpdate
      azure_rm_link: 
        hub_name: sdkTestHub
        link_name: linkTest4806
        resource_group_name: TestHubRG
        properties:
          description:
            en-us: Link Description
          display_name:
            en-us: Link DisplayName
          link_name: linkTest4806
          mappings:
            - link_type: UpdateAlways
              source_property_name: testInteraction1949
              target_property_name: testProfile1446
          participant_property_references:
            - source_property_name: testInteraction1949
              target_property_name: ProfileId
          source_entity_type: Interaction
          source_entity_type_name: testInteraction1949
          target_entity_type: Profile
          target_entity_type_name: testProfile1446
        

    - name: Links_Delete
      azure_rm_link: 
        hub_name: sdkTestHub
        link_name: linkTest4806
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
link_name:
  description:
    - The link name.
  returned: always
  type: str
  sample: null
source_entity_type:
  description:
    - Type of source entity.
  returned: always
  type: sealed-choice
  sample: null
target_entity_type:
  description:
    - Type of target entity.
  returned: always
  type: sealed-choice
  sample: null
source_entity_type_name:
  description:
    - Name of the source Entity Type.
  returned: always
  type: str
  sample: null
target_entity_type_name:
  description:
    - Name of the target Entity Type.
  returned: always
  type: str
  sample: null
display_name:
  description:
    - Localized display name for the Link.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - Localized descriptions for the Link.
  returned: always
  type: dictionary
  sample: null
mappings:
  description:
    - The set of properties mappings between the source and target Types.
  returned: always
  type: list
  sample: null
  contains:
    source_property_name:
      description:
        - ' Property name on the source Entity Type.'
      returned: always
      type: str
      sample: null
    target_property_name:
      description:
        - Property name on the target Entity Type.
      returned: always
      type: str
      sample: null
    link_type:
      description:
        - Link type.
      returned: always
      type: sealed-choice
      sample: null
participant_property_references:
  description:
    - The properties that represent the participating profile.
  returned: always
  type: list
  sample: null
  contains:
    source_property_name:
      description:
        - The source property that maps to the target property.
      returned: always
      type: str
      sample: null
    target_property_name:
      description:
        - The target property that maps to the source property.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - Provisioning state.
  returned: always
  type: str
  sample: null
reference_only:
  description:
    - >-
      Indicating whether the link is reference only link. This flag is ignored
      if the Mappings are defined. If the mappings are not defined and it is set
      to true, links processing will not create or update profiles.
  returned: always
  type: bool
  sample: null
operation_type:
  description:
    - >-
      Determines whether this link is supposed to create or delete instances if
      Link is NOT Reference Only.
  returned: always
  type: sealed-choice
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


class AzureRMLink(AzureRMModuleBaseExt):
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
            link_name=dict(
                type='str',
                required=True
            ),
            source_entity_type=dict(
                type='sealed-choice',
                disposition='/source_entity_type'
            ),
            target_entity_type=dict(
                type='sealed-choice',
                disposition='/target_entity_type'
            ),
            source_entity_type_name=dict(
                type='str',
                disposition='/source_entity_type_name'
            ),
            target_entity_type_name=dict(
                type='str',
                disposition='/target_entity_type_name'
            ),
            display_name=dict(
                type='dictionary',
                disposition='/display_name'
            ),
            description=dict(
                type='dictionary',
                disposition='/description'
            ),
            mappings=dict(
                type='list',
                disposition='/mappings',
                elements='dict',
                options=dict(
                    source_property_name=dict(
                        type='str',
                        disposition='source_property_name',
                        required=True
                    ),
                    target_property_name=dict(
                        type='str',
                        disposition='target_property_name',
                        required=True
                    ),
                    link_type=dict(
                        type='sealed-choice',
                        disposition='link_type'
                    )
                )
            ),
            participant_property_references=dict(
                type='list',
                disposition='/participant_property_references',
                elements='dict',
                options=dict(
                    source_property_name=dict(
                        type='str',
                        disposition='source_property_name',
                        required=True
                    ),
                    target_property_name=dict(
                        type='str',
                        disposition='target_property_name',
                        required=True
                    )
                )
            ),
            reference_only=dict(
                type='bool',
                disposition='/reference_only'
            ),
            operation_type=dict(
                type='sealed-choice',
                disposition='/operation_type'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.link_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLink, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.links.create_or_update(resource_group_name=self.resource_group_name,
                                                               hub_name=self.hub_name,
                                                               link_name=self.link_name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Link instance.')
            self.fail('Error creating the Link instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.links.delete(resource_group_name=self.resource_group_name,
                                                     hub_name=self.hub_name,
                                                     link_name=self.link_name)
        except CloudError as e:
            self.log('Error attempting to delete the Link instance.')
            self.fail('Error deleting the Link instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.links.get(resource_group_name=self.resource_group_name,
                                                  hub_name=self.hub_name,
                                                  link_name=self.link_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLink()


if __name__ == '__main__':
    main()
