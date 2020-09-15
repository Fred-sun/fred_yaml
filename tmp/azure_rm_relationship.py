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
module: azure_rm_relationship
version_added: '2.9'
short_description: Manage Azure Relationship instance.
description:
  - 'Create, update and delete instance of Azure Relationship.'
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
  relationship_name:
    description:
      - The name of the Relationship.
      - The name of the relationship.
    required: true
    type: str
  cardinality:
    description:
      - The Relationship Cardinality.
    type: sealed-choice
  display_name:
    description:
      - Localized display name for the Relationship.
    type: dictionary
  description:
    description:
      - Localized descriptions for the Relationship.
    type: dictionary
  expiry_date_time_utc:
    description:
      - The expiry date time in UTC.
    type: str
  fields:
    description:
      - The properties of the Relationship.
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
  lookup_mappings:
    description:
      - >-
        Optional property to be used to map fields in profile to their strong
        ids in related profile.
    type: list
    suboptions:
      field_mappings:
        description:
          - >-
            Maps a profile property with the StrongId of related profile. This
            is an array to support StrongIds that are composite key as well.
        required: true
        type: list
        suboptions:
          profile_field_name:
            description:
              - Specifies the fieldName in profile.
            required: true
            type: str
          related_profile_key_property:
            description:
              - >-
                Specifies the KeyProperty (from StrongId) of the related
                profile.
            required: true
            type: str
  profile_type:
    description:
      - Profile type.
    type: str
  related_profile_type:
    description:
      - Related profile being referenced.
    type: str
  state:
    description:
      - Assert the state of the Relationship.
      - >-
        Use C(present) to create or update an Relationship and C(absent) to
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
    - name: Relationships_CreateOrUpdate
      azure_rm_relationship: 
        hub_name: sdkTestHub
        relationship_name: SomeRelationship
        resource_group_name: TestHubRG
        properties:
          description:
            en-us: Relationship Description
          cardinality: OneToOne
          display_name:
            en-us: Relationship DisplayName
          fields: []
          profile_type: testProfile2326994
          related_profile_type: testProfile2326994
        

    - name: Relationships_Delete
      azure_rm_relationship: 
        hub_name: sdkTestHub
        relationship_name: SomeRelationship
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
cardinality:
  description:
    - The Relationship Cardinality.
  returned: always
  type: sealed-choice
  sample: null
display_name:
  description:
    - Localized display name for the Relationship.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - Localized descriptions for the Relationship.
  returned: always
  type: dictionary
  sample: null
expiry_date_time_utc:
  description:
    - The expiry date time in UTC.
  returned: always
  type: str
  sample: null
fields:
  description:
    - The properties of the Relationship.
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
lookup_mappings:
  description:
    - >-
      Optional property to be used to map fields in profile to their strong ids
      in related profile.
  returned: always
  type: list
  sample: null
  contains:
    field_mappings:
      description:
        - >-
          Maps a profile property with the StrongId of related profile. This is
          an array to support StrongIds that are composite key as well.
      returned: always
      type: list
      sample: null
      contains:
        profile_field_name:
          description:
            - Specifies the fieldName in profile.
          returned: always
          type: str
          sample: null
        related_profile_key_property:
          description:
            - Specifies the KeyProperty (from StrongId) of the related profile.
          returned: always
          type: str
          sample: null
profile_type:
  description:
    - Profile type.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state.
  returned: always
  type: str
  sample: null
relationship_name:
  description:
    - The Relationship name.
  returned: always
  type: str
  sample: null
related_profile_type:
  description:
    - Related profile being referenced.
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


class AzureRMRelationship(AzureRMModuleBaseExt):
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
            relationship_name=dict(
                type='str',
                required=True
            ),
            cardinality=dict(
                type='sealed-choice',
                disposition='/cardinality'
            ),
            display_name=dict(
                type='dictionary',
                disposition='/display_name'
            ),
            description=dict(
                type='dictionary',
                disposition='/description'
            ),
            expiry_date_time_utc=dict(
                type='str',
                disposition='/expiry_date_time_utc'
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
            lookup_mappings=dict(
                type='list',
                disposition='/lookup_mappings',
                elements='dict',
                options=dict(
                    field_mappings=dict(
                        type='list',
                        disposition='field_mappings',
                        required=True,
                        elements='dict',
                        options=dict(
                            profile_field_name=dict(
                                type='str',
                                disposition='profile_field_name',
                                required=True
                            ),
                            related_profile_key_property=dict(
                                type='str',
                                disposition='related_profile_key_property',
                                required=True
                            )
                        )
                    )
                )
            ),
            profile_type=dict(
                type='str',
                disposition='/profile_type'
            ),
            related_profile_type=dict(
                type='str',
                disposition='/related_profile_type'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.relationship_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRelationship, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.relationships.create_or_update(resource_group_name=self.resource_group_name,
                                                                       hub_name=self.hub_name,
                                                                       relationship_name=self.relationship_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Relationship instance.')
            self.fail('Error creating the Relationship instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.relationships.delete(resource_group_name=self.resource_group_name,
                                                             hub_name=self.hub_name,
                                                             relationship_name=self.relationship_name)
        except CloudError as e:
            self.log('Error attempting to delete the Relationship instance.')
            self.fail('Error deleting the Relationship instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.relationships.get(resource_group_name=self.resource_group_name,
                                                          hub_name=self.hub_name,
                                                          relationship_name=self.relationship_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRelationship()


if __name__ == '__main__':
    main()
