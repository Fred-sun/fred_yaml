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
module: azure_rm_blueprint_info
version_added: '2.9'
short_description: Get Blueprint info.
description:
  - Get info of Blueprint.
options:
  resource_scope:
    description:
      - >-
        The scope of the resource. Valid scopes are: management group (format:
        '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
        subscription (format: '/subscriptions/{subscriptionId}').
    required: true
    type: str
  blueprint_name:
    description:
      - Name of the blueprint definition.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ManagementGroupBlueprint
      azure_rm_blueprint_info: 
        blueprint_name: simpleBlueprint
        resource_scope: providers/Microsoft.Management/managementGroups/ContosoOnlineGroup
        

    - name: SubscriptionBlueprint
      azure_rm_blueprint_info: 
        blueprint_name: simpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        

'''

RETURN = '''
blueprints:
  description: >-
    A list of dict results where the key is the name of the Blueprint and the
    values are the facts for that Blueprint.
  returned: always
  type: complex
  contains:
    id:
      description:
        - String Id used to locate any resource on Azure.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of this resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of this resource.
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
    status:
      description:
        - Status of the blueprint. This field is readonly.
      returned: always
      type: dict
      sample: null
      contains:
        time_created:
          description:
            - Creation time of this blueprint definition.
          returned: always
          type: str
          sample: null
        last_modified:
          description:
            - Last modified time of this blueprint definition.
          returned: always
          type: str
          sample: null
    target_scope:
      description:
        - The scope where this blueprint definition can be assigned.
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - Parameters required by this blueprint definition.
      returned: always
      type: dictionary
      sample: null
    resource_groups:
      description:
        - Resource group placeholders defined by this blueprint definition.
      returned: always
      type: dictionary
      sample: null
    versions:
      description:
        - Published versions of this blueprint definition.
      returned: always
      type: any
      sample: null
    layout:
      description:
        - Layout view of the blueprint definition for UI reference.
      returned: always
      type: any
      sample: null
    value:
      description:
        - List of blueprint definitions.
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
        status:
          description:
            - Status of the blueprint. This field is readonly.
          returned: always
          type: dict
          sample: null
          contains:
            time_created:
              description:
                - Creation time of this blueprint definition.
              returned: always
              type: str
              sample: null
            last_modified:
              description:
                - Last modified time of this blueprint definition.
              returned: always
              type: str
              sample: null
        target_scope:
          description:
            - The scope where this blueprint definition can be assigned.
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - Parameters required by this blueprint definition.
          returned: always
          type: dictionary
          sample: null
        resource_groups:
          description:
            - Resource group placeholders defined by this blueprint definition.
          returned: always
          type: dictionary
          sample: null
        versions:
          description:
            - Published versions of this blueprint definition.
          returned: always
          type: any
          sample: null
        layout:
          description:
            - Layout view of the blueprint definition for UI reference.
          returned: always
          type: any
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


class AzureRMBlueprintInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_scope=dict(
                type='str',
                required=True
            ),
            blueprint_name=dict(
                type='str'
            )
        )

        self.resource_scope = None
        self.blueprint_name = None

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
        super(AzureRMBlueprintInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BlueprintManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-01-preview')

        if (self.resource_scope is not None and
            self.blueprint_name is not None):
            self.results['blueprints'] = self.format_item(self.get())
        elif (self.resource_scope is not None):
            self.results['blueprints'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.blueprints.get(resource_scope=self.resource_scope,
                                                       blueprint_name=self.blueprint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.blueprints.list(resource_scope=self.resource_scope)
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
    AzureRMBlueprintInfo()


if __name__ == '__main__':
    main()
