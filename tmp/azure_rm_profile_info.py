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
module: azure_rm_profile_info
version_added: '2.9'
short_description: Get Profile info.
description:
  - Get info of Profile.
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
  profile_name:
    description:
      - The name of the profile.
    type: str
  locale_code:
    description:
      - 'Locale of profile to retrieve, default is en-us.'
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Profiles_Get
      azure_rm_profile_info: 
        hub_name: sdkTestHub
        profile_name: TestProfileType396
        resource_group_name: TestHubRG
        

    - name: Profiles_ListByHub
      azure_rm_profile_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
profiles:
  description: >-
    A list of dict results where the key is the name of the Profile and the
    values are the facts for that Profile.
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
          The api entity set name. This becomes the odata entity set name for
          the entity Type being referred in this object.
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
              Indicates if the property is actually an array of the fieldType
              above on the data api.
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
              Whether property value is required on instances, IsRequired field
              only for Interaction. Profile Instance will not check for required
              field.
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
              This is specific to interactions modeled as activities. Data
              sources are used to determine where data is stored and also in
              precedence rules.
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
        - >-
          The schema org link. This helps ACI identify and suggest semantic
          models.
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
          The timestamp property name. Represents the time when the interaction
          or profile update happened.
      returned: always
      type: str
      sample: null
    type_name:
      description:
        - The name of the entity.
      returned: always
      type: str
      sample: null
    strong_ids:
      description:
        - The strong IDs.
      returned: always
      type: list
      sample: null
      contains:
        key_property_names:
          description:
            - The properties which make up the unique ID.
          returned: always
          type: list
          sample: null
        strong_id_name:
          description:
            - The Name identifying the strong ID.
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
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
              The api entity set name. This becomes the odata entity set name
              for the entity Type being referred in this object.
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
                  Indicates if the property is actually an array of the
                  fieldType above on the data api.
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
                  Whether property value is required on instances, IsRequired
                  field only for Interaction. Profile Instance will not check
                  for required field.
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
                  This is specific to interactions modeled as activities. Data
                  sources are used to determine where data is stored and also in
                  precedence rules.
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
            - >-
              The schema org link. This helps ACI identify and suggest semantic
              models.
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
              The timestamp property name. Represents the time when the
              interaction or profile update happened.
          returned: always
          type: str
          sample: null
        type_name:
          description:
            - The name of the entity.
          returned: always
          type: str
          sample: null
        strong_ids:
          description:
            - The strong IDs.
          returned: always
          type: list
          sample: null
          contains:
            key_property_names:
              description:
                - The properties which make up the unique ID.
              returned: always
              type: list
              sample: null
            strong_id_name:
              description:
                - The Name identifying the strong ID.
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
    next_link:
      description:
        - Link to the next set of results.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProfileInfo(AzureRMModuleBase):
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
            profile_name=dict(
                type='str'
            ),
            locale_code=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.profile_name = None
        self.locale_code = None

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
        super(AzureRMProfileInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.profile_name is not None):
            self.results['profiles'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['profiles'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.profiles.get(resource_group_name=self.resource_group_name,
                                                     hub_name=self.hub_name,
                                                     profile_name=self.profile_name,
                                                     locale_code=self.locale_code)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.profiles.list_by_hub(resource_group_name=self.resource_group_name,
                                                             hub_name=self.hub_name,
                                                             locale_code=self.locale_code)
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
    AzureRMProfileInfo()


if __name__ == '__main__':
    main()
