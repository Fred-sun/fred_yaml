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
module: azure_rm_relationshiplink_info
version_added: '2.9'
short_description: Get RelationshipLink info.
description:
  - Get info of RelationshipLink.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RelationshipLinks_Get
      azure_rm_relationshiplink_info: 
        hub_name: sdkTestHub
        relationship_link_name: Somelink
        resource_group_name: TestHubRG
        

    - name: RelationshipLinks_ListByHub
      azure_rm_relationshiplink_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
relationship_links:
  description: >-
    A list of dict results where the key is the name of the RelationshipLink and
    the values are the facts for that RelationshipLink.
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
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
                  The source interaction property that maps to the target
                  profile property.
              returned: always
              type: str
              sample: null
            profile_property_name:
              description:
                - >-
                  The target profile property that maps to the source
                  interaction property.
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
            - >-
              The property references for the Related Profile of the
              Relationship.
          returned: always
          type: list
          sample: null
          contains:
            interaction_property_name:
              description:
                - >-
                  The source interaction property that maps to the target
                  profile property.
              returned: always
              type: str
              sample: null
            profile_property_name:
              description:
                - >-
                  The target profile property that maps to the source
                  interaction property.
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


class AzureRMRelationshipLinkInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.relationship_link_name = None

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
        super(AzureRMRelationshipLinkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.relationship_link_name is not None):
            self.results['relationship_links'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['relationship_links'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.relationship_links.get(resource_group_name=self.resource_group_name,
                                                               hub_name=self.hub_name,
                                                               relationship_link_name=self.relationship_link_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.relationship_links.list_by_hub(resource_group_name=self.resource_group_name,
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
    AzureRMRelationshipLinkInfo()


if __name__ == '__main__':
    main()
