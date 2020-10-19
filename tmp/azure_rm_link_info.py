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
module: azure_rm_link_info
version_added: '2.9'
short_description: Get Link info.
description:
  - Get info of Link.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Links_Get
      azure_rm_link_info: 
        hub_name: sdkTestHub
        link_name: linkTest4806
        resource_group_name: TestHubRG
        

    - name: Links_ListByHub
      azure_rm_link_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
links:
  description: >-
    A list of dict results where the key is the name of the Link and the values
    are the facts for that Link.
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
          Indicating whether the link is reference only link. This flag is
          ignored if the Mappings are defined. If the mappings are not defined
          and it is set to true, links processing will not create or update
          profiles.
      returned: always
      type: bool
      sample: null
    operation_type:
      description:
        - >-
          Determines whether this link is supposed to create or delete instances
          if Link is NOT Reference Only.
      returned: always
      type: sealed-choice
      sample: null
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
            - >-
              The set of properties mappings between the source and target
              Types.
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
              Indicating whether the link is reference only link. This flag is
              ignored if the Mappings are defined. If the mappings are not
              defined and it is set to true, links processing will not create or
              update profiles.
          returned: always
          type: bool
          sample: null
        operation_type:
          description:
            - >-
              Determines whether this link is supposed to create or delete
              instances if Link is NOT Reference Only.
          returned: always
          type: sealed-choice
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


class AzureRMLinkInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.link_name = None

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
        super(AzureRMLinkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.link_name is not None):
            self.results['links'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['links'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.links.get(resource_group_name=self.resource_group_name,
                                                  hub_name=self.hub_name,
                                                  link_name=self.link_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.links.list_by_hub(resource_group_name=self.resource_group_name,
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
    AzureRMLinkInfo()


if __name__ == '__main__':
    main()
