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
module: azure_rm_interaction
version_added: '2.9'
short_description: Manage Azure Interaction instance.
description:
  - 'Create, update and delete instance of Azure Interaction.'
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
  interaction_name:
    description:
      - The name of the interaction.
    required: true
    type: str
  attributes:
    description:
      - The attributes for the Type.
    type: dictionary
  description:
    description:
      - Localized descriptions for the property.
    type: dictionary
  display_name:
    description:
      - Localized display names for the property.
    type: dictionary
  localized_attributes:
    description:
      - Any custom localized attributes for the Type.
    type: dictionary
  small_image:
    description:
      - Small Image associated with the Property or EntityType.
    type: str
  medium_image:
    description:
      - Medium Image associated with the Property or EntityType.
    type: str
  large_image:
    description:
      - Large Image associated with the Property or EntityType.
    type: str
  api_entity_set_name:
    description:
      - >-
        The api entity set name. This becomes the odata entity set name for the
        entity Type being referred in this object.
    type: str
  entity_type:
    description:
      - Type of entity.
    type: sealed-choice
  fields:
    description:
      - The properties of the Profile.
    type: list
    suboptions:
      array_value_separator:
        description:
          - Array value separator for properties with isArray set.
        type: str
      enum_valid_values:
        description:
          - Describes valid values for an enum property.
        type: list
        suboptions:
          value:
            description:
              - The integer value of the enum member.
            type: integer
          localized_value_names:
            description:
              - Localized names of the enum member.
            type: dictionary
      field_name:
        description:
          - Name of the property.
        required: true
        type: str
      field_type:
        description:
          - Type of the property.
        required: true
        type: str
      is_array:
        description:
          - >-
            Indicates if the property is actually an array of the fieldType
            above on the data api.
        type: bool
      is_enum:
        description:
          - Indicates if the property is an enum.
        type: bool
      is_flag_enum:
        description:
          - Indicates if the property is an flag enum.
        type: bool
      is_image:
        description:
          - Whether the property is an Image.
        type: bool
      is_localized_string:
        description:
          - Whether the property is a localized string.
        type: bool
      is_name:
        description:
          - Whether the property is a name or a part of name.
        type: bool
      is_required:
        description:
          - >-
            Whether property value is required on instances, IsRequired field
            only for Interaction. Profile Instance will not check for required
            field.
        type: bool
      property_id:
        description:
          - The ID associated with the property.
        type: str
      schema_item_prop_link:
        description:
          - URL encoded schema.org item prop link for the property.
        type: str
      max_length:
        description:
          - Max length of string. Used only if type is string.
        type: integer
      is_available_in_graph:
        description:
          - Whether property is available in graph or not.
        type: bool
      data_source_precedence_rules:
        description:
          - >-
            This is specific to interactions modeled as activities. Data sources
            are used to determine where data is stored and also in precedence
            rules.
        type: list
        suboptions:
          precedence:
            description:
              - the precedence value.
            type: integer
          name:
            description:
              - The data source name
            type: str
          data_source_type:
            description:
              - The data source type.
            type: str
            choices:
              - Connector
              - LinkInteraction
              - SystemDefault
          status:
            description:
              - The data source status.
            type: str
            choices:
              - None
              - Active
              - Deleted
          id:
            description:
              - The data source ID.
            type: integer
          data_source_reference_id:
            description:
              - The data source reference id.
            type: str
  instances_count:
    description:
      - The instance count.
    type: integer
  schema_item_type_link:
    description:
      - >-
        The schema org link. This helps ACI identify and suggest semantic
        models.
    type: str
  timestamp_field_name:
    description:
      - >-
        The timestamp property name. Represents the time when the interaction or
        profile update happened.
    type: str
  type_name:
    description:
      - The name of the entity.
    type: str
  id_property_names:
    description:
      - >-
        The id property names. Properties which uniquely identify an interaction
        instance.
    type: list
  participant_profiles:
    description:
      - Profiles that participated in the interaction.
    type: list
    suboptions:
      profile_type_name:
        description:
          - Profile type name.
        required: true
        type: str
      participant_property_references:
        description:
          - The property references.
        required: true
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
      participant_name:
        description:
          - Participant name.
        required: true
        type: str
      display_name:
        description:
          - Localized display name.
        type: dictionary
      description:
        description:
          - Localized descriptions.
        type: dictionary
      role:
        description:
          - The role that the participant is playing in the interaction.
        type: str
  primary_participant_profile_property_name:
    description:
      - >-
        The primary participant property name for an interaction ,This is used
        to logically represent the agent of the interaction, Specify the
        participant name here from ParticipantName.
    type: str
  is_activity:
    description:
      - >-
        An interaction can be tagged as an activity only during create. This
        enables the interaction to be editable and can enable merging of
        properties from multiple data sources based on precedence, which is
        defined at a link level.
    type: bool
  locale_code:
    description:
      - 'Locale of interaction to retrieve, default is en-us.'
    type: str
  state:
    description:
      - Assert the state of the Interaction.
      - >-
        Use C(present) to create or update an Interaction and C(absent) to
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
    - name: Interactions_CreateOrUpdate
      azure_rm_interaction: 
        hub_name: sdkTestHub
        interaction_name: TestProfileType396
        resource_group_name: TestHubRG
        properties:
          api_entity_set_name: TestInteractionType6358
          fields:
            - field_name: TestInteractionType6358
              field_type: Edm.String
              is_array: false
              is_required: true
            - field_name: profile1
              field_type: Edm.String
          id_property_names:
            - TestInteractionType6358
          large_image: \\Images\\LargeImage
          medium_image: \\Images\\MediumImage
          primary_participant_profile_property_name: profile1
          small_image: \\Images\\smallImage
        

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
attributes:
  description:
    - The attributes for the Type.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - Localized descriptions for the property.
  returned: always
  type: dictionary
  sample: null
display_name:
  description:
    - Localized display names for the property.
  returned: always
  type: dictionary
  sample: null
localized_attributes:
  description:
    - Any custom localized attributes for the Type.
  returned: always
  type: dictionary
  sample: null
small_image:
  description:
    - Small Image associated with the Property or EntityType.
  returned: always
  type: str
  sample: null
medium_image:
  description:
    - Medium Image associated with the Property or EntityType.
  returned: always
  type: str
  sample: null
large_image:
  description:
    - Large Image associated with the Property or EntityType.
  returned: always
  type: str
  sample: null
api_entity_set_name:
  description:
    - >-
      The api entity set name. This becomes the odata entity set name for the
      entity Type being referred in this object.
  returned: always
  type: str
  sample: null
entity_type:
  description:
    - Type of entity.
  returned: always
  type: sealed-choice
  sample: null
fields:
  description:
    - The properties of the Profile.
  returned: always
  type: list
  sample: null
  contains:
    array_value_separator:
      description:
        - Array value separator for properties with isArray set.
      returned: always
      type: str
      sample: null
    enum_valid_values:
      description:
        - Describes valid values for an enum property.
      returned: always
      type: list
      sample: null
      contains:
        value:
          description:
            - The integer value of the enum member.
          returned: always
          type: integer
          sample: null
        localized_value_names:
          description:
            - Localized names of the enum member.
          returned: always
          type: dictionary
          sample: null
    field_name:
      description:
        - Name of the property.
      returned: always
      type: str
      sample: null
    field_type:
      description:
        - Type of the property.
      returned: always
      type: str
      sample: null
    is_array:
      description:
        - >-
          Indicates if the property is actually an array of the fieldType above
          on the data api.
      returned: always
      type: bool
      sample: null
    is_enum:
      description:
        - Indicates if the property is an enum.
      returned: always
      type: bool
      sample: null
    is_flag_enum:
      description:
        - Indicates if the property is an flag enum.
      returned: always
      type: bool
      sample: null
    is_image:
      description:
        - Whether the property is an Image.
      returned: always
      type: bool
      sample: null
    is_localized_string:
      description:
        - Whether the property is a localized string.
      returned: always
      type: bool
      sample: null
    is_name:
      description:
        - Whether the property is a name or a part of name.
      returned: always
      type: bool
      sample: null
    is_required:
      description:
        - >-
          Whether property value is required on instances, IsRequired field only
          for Interaction. Profile Instance will not check for required field.
      returned: always
      type: bool
      sample: null
    property_id:
      description:
        - The ID associated with the property.
      returned: always
      type: str
      sample: null
    schema_item_prop_link:
      description:
        - URL encoded schema.org item prop link for the property.
      returned: always
      type: str
      sample: null
    max_length:
      description:
        - Max length of string. Used only if type is string.
      returned: always
      type: integer
      sample: null
    is_available_in_graph:
      description:
        - Whether property is available in graph or not.
      returned: always
      type: bool
      sample: null
    data_source_precedence_rules:
      description:
        - >-
          This is specific to interactions modeled as activities. Data sources
          are used to determine where data is stored and also in precedence
          rules.
      returned: always
      type: list
      sample: null
      contains:
        precedence:
          description:
            - the precedence value.
          returned: always
          type: integer
          sample: null
        name:
          description:
            - The data source name
          returned: always
          type: str
          sample: null
        data_source_type:
          description:
            - The data source type.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The data source status.
          returned: always
          type: str
          sample: null
        id:
          description:
            - The data source ID.
          returned: always
          type: integer
          sample: null
        data_source_reference_id:
          description:
            - The data source reference id.
          returned: always
          type: str
          sample: null
instances_count:
  description:
    - The instance count.
  returned: always
  type: integer
  sample: null
last_changed_utc:
  description:
    - The last changed time for the type definition.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state.
  returned: always
  type: str
  sample: null
schema_item_type_link:
  description:
    - The schema org link. This helps ACI identify and suggest semantic models.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The hub name.
  returned: always
  type: str
  sample: null
timestamp_field_name:
  description:
    - >-
      The timestamp property name. Represents the time when the interaction or
      profile update happened.
  returned: always
  type: str
  sample: null
type_name:
  description:
    - The name of the entity.
  returned: always
  type: str
  sample: null
id_property_names:
  description:
    - >-
      The id property names. Properties which uniquely identify an interaction
      instance.
  returned: always
  type: list
  sample: null
participant_profiles:
  description:
    - Profiles that participated in the interaction.
  returned: always
  type: list
  sample: null
  contains:
    profile_type_name:
      description:
        - Profile type name.
      returned: always
      type: str
      sample: null
    participant_property_references:
      description:
        - The property references.
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
    participant_name:
      description:
        - Participant name.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Localized display name.
      returned: always
      type: dictionary
      sample: null
    description:
      description:
        - Localized descriptions.
      returned: always
      type: dictionary
      sample: null
    role:
      description:
        - The role that the participant is playing in the interaction.
      returned: always
      type: str
      sample: null
primary_participant_profile_property_name:
  description:
    - >-
      The primary participant property name for an interaction ,This is used to
      logically represent the agent of the interaction, Specify the participant
      name here from ParticipantName.
  returned: always
  type: str
  sample: null
data_source_precedence_rules:
  description:
    - >-
      This is specific to interactions modeled as activities. Data sources are
      used to determine where data is stored and also in precedence rules.
  returned: always
  type: list
  sample: null
  contains:
    precedence:
      description:
        - the precedence value.
      returned: always
      type: integer
      sample: null
    name:
      description:
        - The data source name
      returned: always
      type: str
      sample: null
    data_source_type:
      description:
        - The data source type.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The data source status.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The data source ID.
      returned: always
      type: integer
      sample: null
    data_source_reference_id:
      description:
        - The data source reference id.
      returned: always
      type: str
      sample: null
is_activity:
  description:
    - >-
      An interaction can be tagged as an activity only during create. This
      enables the interaction to be editable and can enable merging of
      properties from multiple data sources based on precedence, which is
      defined at a link level.
  returned: always
  type: bool
  sample: null
name_properties_default_data_source_name:
  description:
    - The data source name
  returned: always
  type: str
  sample: null
data_source_type:
  description:
    - The data source type.
  returned: always
  type: str
  sample: null
status:
  description:
    - The data source status.
  returned: always
  type: str
  sample: null
id_properties_default_data_source_id:
  description:
    - The data source ID.
  returned: always
  type: integer
  sample: null
data_source_reference_id:
  description:
    - The data source reference id.
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


class AzureRMInteraction(AzureRMModuleBaseExt):
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
            interaction_name=dict(
                type='str',
                required=True
            ),
            attributes=dict(
                type='dictionary',
                disposition='/attributes'
            ),
            description=dict(
                type='dictionary',
                disposition='/description'
            ),
            display_name=dict(
                type='dictionary',
                disposition='/display_name'
            ),
            localized_attributes=dict(
                type='dictionary',
                disposition='/localized_attributes'
            ),
            small_image=dict(
                type='str',
                disposition='/small_image'
            ),
            medium_image=dict(
                type='str',
                disposition='/medium_image'
            ),
            large_image=dict(
                type='str',
                disposition='/large_image'
            ),
            api_entity_set_name=dict(
                type='str',
                disposition='/api_entity_set_name'
            ),
            entity_type=dict(
                type='sealed-choice',
                disposition='/entity_type'
            ),
            fields=dict(
                type='list',
                disposition='/fields',
                elements='dict',
                options=dict(
                    array_value_separator=dict(
                        type='str',
                        disposition='array_value_separator'
                    ),
                    enum_valid_values=dict(
                        type='list',
                        disposition='enum_valid_values',
                        elements='dict',
                        options=dict(
                            value=dict(
                                type='integer',
                                disposition='value'
                            ),
                            localized_value_names=dict(
                                type='dictionary',
                                disposition='localized_value_names'
                            )
                        )
                    ),
                    field_name=dict(
                        type='str',
                        disposition='field_name',
                        required=True
                    ),
                    field_type=dict(
                        type='str',
                        disposition='field_type',
                        required=True
                    ),
                    is_array=dict(
                        type='bool',
                        disposition='is_array'
                    ),
                    is_enum=dict(
                        type='bool',
                        disposition='is_enum'
                    ),
                    is_flag_enum=dict(
                        type='bool',
                        disposition='is_flag_enum'
                    ),
                    is_image=dict(
                        type='bool',
                        disposition='is_image'
                    ),
                    is_localized_string=dict(
                        type='bool',
                        disposition='is_localized_string'
                    ),
                    is_name=dict(
                        type='bool',
                        disposition='is_name'
                    ),
                    is_required=dict(
                        type='bool',
                        disposition='is_required'
                    ),
                    property_id=dict(
                        type='str',
                        disposition='property_id'
                    ),
                    schema_item_prop_link=dict(
                        type='str',
                        disposition='schema_item_prop_link'
                    ),
                    max_length=dict(
                        type='integer',
                        disposition='max_length'
                    ),
                    is_available_in_graph=dict(
                        type='bool',
                        disposition='is_available_in_graph'
                    ),
                    data_source_precedence_rules=dict(
                        type='list',
                        updatable=False,
                        disposition='data_source_precedence_rules',
                        elements='dict',
                        options=dict(
                            precedence=dict(
                                type='integer',
                                disposition='precedence'
                            ),
                            name=dict(
                                type='str',
                                updatable=False,
                                disposition='name'
                            ),
                            data_source_type=dict(
                                type='str',
                                updatable=False,
                                disposition='data_source_type',
                                choices=['Connector',
                                         'LinkInteraction',
                                         'SystemDefault']
                            ),
                            status=dict(
                                type='str',
                                updatable=False,
                                disposition='status',
                                choices=['None',
                                         'Active',
                                         'Deleted']
                            ),
                            id=dict(
                                type='integer',
                                updatable=False,
                                disposition='id'
                            ),
                            data_source_reference_id=dict(
                                type='str',
                                updatable=False,
                                disposition='data_source_reference_id'
                            )
                        )
                    )
                )
            ),
            instances_count=dict(
                type='integer',
                disposition='/instances_count'
            ),
            schema_item_type_link=dict(
                type='str',
                disposition='/schema_item_type_link'
            ),
            timestamp_field_name=dict(
                type='str',
                disposition='/timestamp_field_name'
            ),
            type_name=dict(
                type='str',
                disposition='/type_name'
            ),
            id_property_names=dict(
                type='list',
                disposition='/id_property_names',
                elements='str'
            ),
            participant_profiles=dict(
                type='list',
                disposition='/participant_profiles',
                elements='dict',
                options=dict(
                    profile_type_name=dict(
                        type='str',
                        disposition='profile_type_name',
                        required=True
                    ),
                    participant_property_references=dict(
                        type='list',
                        disposition='participant_property_references',
                        required=True,
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
                    participant_name=dict(
                        type='str',
                        disposition='participant_name',
                        required=True
                    ),
                    display_name=dict(
                        type='dictionary',
                        disposition='display_name'
                    ),
                    description=dict(
                        type='dictionary',
                        disposition='description'
                    ),
                    role=dict(
                        type='str',
                        disposition='role'
                    )
                )
            ),
            primary_participant_profile_property_name=dict(
                type='str',
                disposition='/primary_participant_profile_property_name'
            ),
            is_activity=dict(
                type='bool',
                disposition='/is_activity'
            ),
            locale_code=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.interaction_name = None
        self.locale_code = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMInteraction, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.interactions.create_or_update(resource_group_name=self.resource_group_name,
                                                                      hub_name=self.hub_name,
                                                                      interaction_name=self.interaction_name,
                                                                      parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Interaction instance.')
            self.fail('Error creating the Interaction instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.interactions.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Interaction instance.')
            self.fail('Error deleting the Interaction instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.interactions.get(resource_group_name=self.resource_group_name,
                                                         hub_name=self.hub_name,
                                                         interaction_name=self.interaction_name,
                                                         locale_code=self.locale_code)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMInteraction()


if __name__ == '__main__':
    main()
