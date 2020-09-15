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
module: azure_rm_rulesengine
version_added: '2.9'
short_description: Manage Azure RulesEngine instance.
description:
  - 'Create, update and delete instance of Azure RulesEngine.'
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
    required: true
    type: str
  rules:
    description:
      - A list of rules that define a particular Rules Engine Configuration.
    type: list
    suboptions:
      name:
        description:
          - A name to refer to this specific rule.
        required: true
        type: str
      priority:
        description:
          - 'A priority assigned to this rule. '
        required: true
        type: integer
      action:
        description:
          - >-
            Actions to perform on the request and response if all of the match
            conditions are met.
        required: true
        type: dict
        suboptions:
          request_header_actions:
            description:
              - >-
                A list of header actions to apply from the request from AFD to
                the origin.
            type: list
            suboptions:
              header_action_type:
                description:
                  - Which type of manipulation to apply to the header.
                required: true
                type: str
                choices:
                  - Append
                  - Delete
                  - Overwrite
              header_name:
                description:
                  - The name of the header this action will apply to.
                required: true
                type: str
              value:
                description:
                  - >-
                    The value to update the given header name with. This value
                    is not used if the actionType is Delete.
                type: str
          response_header_actions:
            description:
              - >-
                A list of header actions to apply from the response from AFD to
                the client.
            type: list
            suboptions:
              header_action_type:
                description:
                  - Which type of manipulation to apply to the header.
                required: true
                type: str
                choices:
                  - Append
                  - Delete
                  - Overwrite
              header_name:
                description:
                  - The name of the header this action will apply to.
                required: true
                type: str
              value:
                description:
                  - >-
                    The value to update the given header name with. This value
                    is not used if the actionType is Delete.
                type: str
          route_configuration_override:
            description:
              - Override the route configuration.
            type: dict
            suboptions:
              odata_type:
                description:
                  - undefined
                required: true
                type: str
      match_conditions:
        description:
          - >-
            A list of match conditions that must meet in order for the actions
            of this rule to run. Having no match conditions means the actions
            will always run.
        type: list
        suboptions:
          rules_engine_match_variable:
            description:
              - Match Variable
            required: true
            type: str
            choices:
              - IsMobile
              - RemoteAddr
              - RequestMethod
              - QueryString
              - PostArgs
              - RequestUri
              - RequestPath
              - RequestFilename
              - RequestFilenameExtension
              - RequestHeader
              - RequestBody
              - RequestScheme
          selector:
            description:
              - Name of selector in RequestHeader or RequestBody to be matched
            type: str
          rules_engine_operator:
            description:
              - Describes operator to apply to the match condition.
            required: true
            type: str
            choices:
              - Any
              - IPMatch
              - GeoMatch
              - Equal
              - Contains
              - LessThan
              - GreaterThan
              - LessThanOrEqual
              - GreaterThanOrEqual
              - BeginsWith
              - EndsWith
          negate_condition:
            description:
              - Describes if this is negate condition or not
            type: bool
          rules_engine_match_value:
            description:
              - >-
                Match values to match against. The operator will apply to each
                value in here with OR semantics. If any of them match the
                variable with the given operator this match condition is
                considered a match.
            required: true
            type: list
          transforms:
            description:
              - List of transforms
            type: list
      match_processing_behavior:
        description:
          - >-
            If this rule is a match should the rules engine continue running the
            remaining rules or stop. If not present, defaults to Continue.
        type: str
        choices:
          - Continue
          - Stop
  state:
    description:
      - Assert the state of the RulesEngine.
      - >-
        Use C(present) to create or update an RulesEngine and C(absent) to
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
    - name: Create or update a specific Rules Engine Configuration
      azure_rm_rulesengine: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        rules_engine_name: rulesEngine1
        

    - name: Delete Rules Engine Configuration
      azure_rm_rulesengine: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        rules_engine_name: rulesEngine1
        

'''

RETURN = '''
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
              A list of header actions to apply from the request from AFD to the
              origin.
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
                  The value to update the given header name with. This value is
                  not used if the actionType is Delete.
              returned: always
              type: str
              sample: null
        response_header_actions:
          description:
            - >-
              A list of header actions to apply from the response from AFD to
              the client.
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
                  The value to update the given header name with. This value is
                  not used if the actionType is Delete.
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
          A list of match conditions that must meet in order for the actions of
          this rule to run. Having no match conditions means the actions will
          always run.
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
              value in here with OR semantics. If any of them match the variable
              with the given operator this match condition is considered a
              match.
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
          If this rule is a match should the rules engine continue running the
          remaining rules or stop. If not present, defaults to Continue.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRulesEngine(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            rules=dict(
                type='list',
                disposition='/rules',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    priority=dict(
                        type='integer',
                        disposition='priority',
                        required=True
                    ),
                    action=dict(
                        type='dict',
                        disposition='action',
                        required=True,
                        options=dict(
                            request_header_actions=dict(
                                type='list',
                                disposition='request_header_actions',
                                elements='dict',
                                options=dict(
                                    header_action_type=dict(
                                        type='str',
                                        disposition='header_action_type',
                                        choices=['Append',
                                                 'Delete',
                                                 'Overwrite'],
                                        required=True
                                    ),
                                    header_name=dict(
                                        type='str',
                                        disposition='header_name',
                                        required=True
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value'
                                    )
                                )
                            ),
                            response_header_actions=dict(
                                type='list',
                                disposition='response_header_actions',
                                elements='dict',
                                options=dict(
                                    header_action_type=dict(
                                        type='str',
                                        disposition='header_action_type',
                                        choices=['Append',
                                                 'Delete',
                                                 'Overwrite'],
                                        required=True
                                    ),
                                    header_name=dict(
                                        type='str',
                                        disposition='header_name',
                                        required=True
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value'
                                    )
                                )
                            ),
                            route_configuration_override=dict(
                                type='dict',
                                disposition='route_configuration_override',
                                options=dict(
                                    odata_type=dict(
                                        type='str',
                                        disposition='odata_type',
                                        required=True
                                    )
                                )
                            )
                        )
                    ),
                    match_conditions=dict(
                        type='list',
                        disposition='match_conditions',
                        elements='dict',
                        options=dict(
                            rules_engine_match_variable=dict(
                                type='str',
                                disposition='rules_engine_match_variable',
                                choices=['IsMobile',
                                         'RemoteAddr',
                                         'RequestMethod',
                                         'QueryString',
                                         'PostArgs',
                                         'RequestUri',
                                         'RequestPath',
                                         'RequestFilename',
                                         'RequestFilenameExtension',
                                         'RequestHeader',
                                         'RequestBody',
                                         'RequestScheme'],
                                required=True
                            ),
                            selector=dict(
                                type='str',
                                disposition='selector'
                            ),
                            rules_engine_operator=dict(
                                type='str',
                                disposition='rules_engine_operator',
                                choices=['Any',
                                         'IPMatch',
                                         'GeoMatch',
                                         'Equal',
                                         'Contains',
                                         'LessThan',
                                         'GreaterThan',
                                         'LessThanOrEqual',
                                         'GreaterThanOrEqual',
                                         'BeginsWith',
                                         'EndsWith'],
                                required=True
                            ),
                            negate_condition=dict(
                                type='bool',
                                disposition='negate_condition'
                            ),
                            rules_engine_match_value=dict(
                                type='list',
                                disposition='rules_engine_match_value',
                                required=True,
                                elements='str'
                            ),
                            transforms=dict(
                                type='list',
                                disposition='transforms',
                                elements='str'
                            )
                        )
                    ),
                    match_processing_behavior=dict(
                        type='str',
                        disposition='match_processing_behavior',
                        choices=['Continue',
                                 'Stop']
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
        self.front_door_name = None
        self.rules_engine_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRulesEngine, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
            response = self.mgmt_client.rules_engines.create_or_update(resource_group_name=self.resource_group_name,
                                                                       front_door_name=self.front_door_name,
                                                                       rules_engine_name=self.rules_engine_name,
                                                                       rules_engine_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RulesEngine instance.')
            self.fail('Error creating the RulesEngine instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.rules_engines.delete(resource_group_name=self.resource_group_name,
                                                             front_door_name=self.front_door_name,
                                                             rules_engine_name=self.rules_engine_name)
        except CloudError as e:
            self.log('Error attempting to delete the RulesEngine instance.')
            self.fail('Error deleting the RulesEngine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.rules_engines.get(resource_group_name=self.resource_group_name,
                                                          front_door_name=self.front_door_name,
                                                          rules_engine_name=self.rules_engine_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRulesEngine()


if __name__ == '__main__':
    main()
