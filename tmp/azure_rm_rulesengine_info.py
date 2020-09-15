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
module: azure_rm_rulesengine_info
version_added: '2.9'
short_description: Get RulesEngine info.
description:
  - Get info of RulesEngine.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
    type: str
  rules_engine_name:
    description:
      - Name of the Rules Engine which is unique within the Front Door.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Rules Engine Configurations in a Front Door
      azure_rm_rulesengine_info: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        

    - name: Get Rules Engine Configuration
      azure_rm_rulesengine_info: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        rules_engine_name: rulesEngine1
        

'''

RETURN = '''
rules_engines:
  description: >-
    A list of dict results where the key is the name of the RulesEngine and the
    values are the facts for that RulesEngine.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of rulesEngines within a Front Door.
      returned: always
      type: list
      sample: null
      contains:
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
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        rules:
          description:
            - >-
              A list of rules that define a particular Rules Engine
              Configuration.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - A name to refer to this specific rule.
              returned: always
              type: str
              sample: null
            priority:
              description:
                - 'A priority assigned to this rule. '
              returned: always
              type: integer
              sample: null
            action:
              description:
                - >-
                  Actions to perform on the request and response if all of the
                  match conditions are met.
              returned: always
              type: dict
              sample: null
              contains:
                request_header_actions:
                  description:
                    - >-
                      A list of header actions to apply from the request from
                      AFD to the origin.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    header_action_type:
                      description:
                        - Which type of manipulation to apply to the header.
                      returned: always
                      type: str
                      sample: null
                    header_name:
                      description:
                        - The name of the header this action will apply to.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - >-
                          The value to update the given header name with. This
                          value is not used if the actionType is Delete.
                      returned: always
                      type: str
                      sample: null
                response_header_actions:
                  description:
                    - >-
                      A list of header actions to apply from the response from
                      AFD to the client.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    header_action_type:
                      description:
                        - Which type of manipulation to apply to the header.
                      returned: always
                      type: str
                      sample: null
                    header_name:
                      description:
                        - The name of the header this action will apply to.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - >-
                          The value to update the given header name with. This
                          value is not used if the actionType is Delete.
                      returned: always
                      type: str
                      sample: null
                route_configuration_override:
                  description:
                    - Override the route configuration.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    odata_type:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
            match_conditions:
              description:
                - >-
                  A list of match conditions that must meet in order for the
                  actions of this rule to run. Having no match conditions means
                  the actions will always run.
              returned: always
              type: list
              sample: null
              contains:
                rules_engine_match_variable:
                  description:
                    - Match Variable
                  returned: always
                  type: str
                  sample: null
                selector:
                  description:
                    - >-
                      Name of selector in RequestHeader or RequestBody to be
                      matched
                  returned: always
                  type: str
                  sample: null
                rules_engine_operator:
                  description:
                    - Describes operator to apply to the match condition.
                  returned: always
                  type: str
                  sample: null
                negate_condition:
                  description:
                    - Describes if this is negate condition or not
                  returned: always
                  type: bool
                  sample: null
                rules_engine_match_value:
                  description:
                    - >-
                      Match values to match against. The operator will apply to
                      each value in here with OR semantics. If any of them match
                      the variable with the given operator this match condition
                      is considered a match.
                  returned: always
                  type: list
                  sample: null
                transforms:
                  description:
                    - List of transforms
                  returned: always
                  type: list
                  sample: null
            match_processing_behavior:
              description:
                - >-
                  If this rule is a match should the rules engine continue
                  running the remaining rules or stop. If not present, defaults
                  to Continue.
              returned: always
              type: str
              sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next set of RulesEngine objects if there are any.
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
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    rules:
      description:
        - A list of rules that define a particular Rules Engine Configuration.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - A name to refer to this specific rule.
          returned: always
          type: str
          sample: null
        priority:
          description:
            - 'A priority assigned to this rule. '
          returned: always
          type: integer
          sample: null
        action:
          description:
            - >-
              Actions to perform on the request and response if all of the match
              conditions are met.
          returned: always
          type: dict
          sample: null
          contains:
            request_header_actions:
              description:
                - >-
                  A list of header actions to apply from the request from AFD to
                  the origin.
              returned: always
              type: list
              sample: null
              contains:
                header_action_type:
                  description:
                    - Which type of manipulation to apply to the header.
                  returned: always
                  type: str
                  sample: null
                header_name:
                  description:
                    - The name of the header this action will apply to.
                  returned: always
                  type: str
                  sample: null
                value:
                  description:
                    - >-
                      The value to update the given header name with. This value
                      is not used if the actionType is Delete.
                  returned: always
                  type: str
                  sample: null
            response_header_actions:
              description:
                - >-
                  A list of header actions to apply from the response from AFD
                  to the client.
              returned: always
              type: list
              sample: null
              contains:
                header_action_type:
                  description:
                    - Which type of manipulation to apply to the header.
                  returned: always
                  type: str
                  sample: null
                header_name:
                  description:
                    - The name of the header this action will apply to.
                  returned: always
                  type: str
                  sample: null
                value:
                  description:
                    - >-
                      The value to update the given header name with. This value
                      is not used if the actionType is Delete.
                  returned: always
                  type: str
                  sample: null
            route_configuration_override:
              description:
                - Override the route configuration.
              returned: always
              type: dict
              sample: null
              contains:
                odata_type:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
        match_conditions:
          description:
            - >-
              A list of match conditions that must meet in order for the actions
              of this rule to run. Having no match conditions means the actions
              will always run.
          returned: always
          type: list
          sample: null
          contains:
            rules_engine_match_variable:
              description:
                - Match Variable
              returned: always
              type: str
              sample: null
            selector:
              description:
                - Name of selector in RequestHeader or RequestBody to be matched
              returned: always
              type: str
              sample: null
            rules_engine_operator:
              description:
                - Describes operator to apply to the match condition.
              returned: always
              type: str
              sample: null
            negate_condition:
              description:
                - Describes if this is negate condition or not
              returned: always
              type: bool
              sample: null
            rules_engine_match_value:
              description:
                - >-
                  Match values to match against. The operator will apply to each
                  value in here with OR semantics. If any of them match the
                  variable with the given operator this match condition is
                  considered a match.
              returned: always
              type: list
              sample: null
            transforms:
              description:
                - List of transforms
              returned: always
              type: list
              sample: null
        match_processing_behavior:
          description:
            - >-
              If this rule is a match should the rules engine continue running
              the remaining rules or stop. If not present, defaults to Continue.
          returned: always
          type: str
          sample: null
    resource_state:
      description:
        - Resource status.
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRulesEngineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            front_door_name=dict(
                type='str',
                required=True
            ),
            rules_engine_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.front_door_name = None
        self.rules_engine_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRulesEngineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.front_door_name is not None and
            self.rules_engine_name is not None):
            self.results['rules_engines'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.front_door_name is not None):
            self.results['rules_engines'] = self.format_item(self.listbyfrontdoor())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.rules_engines.get(resource_group_name=self.resource_group_name,
                                                          front_door_name=self.front_door_name,
                                                          rules_engine_name=self.rules_engine_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyfrontdoor(self):
        response = None

        try:
            response = self.mgmt_client.rules_engines.list_by_front_door(resource_group_name=self.resource_group_name,
                                                                         front_door_name=self.front_door_name)
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
    AzureRMRulesEngineInfo()


if __name__ == '__main__':
    main()
