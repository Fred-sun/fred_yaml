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
module: azure_rm_policy
version_added: '2.9'
short_description: Manage Azure Policy instance.
description:
  - 'Create, update and delete instance of Azure Policy.'
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  policy_name:
    description:
      - The name of the Web Application Firewall Policy.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  etag:
    description:
      - >-
        Gets a unique read-only string that changes whenever the resource is
        updated.
    type: str
  policy_settings:
    description:
      - Describes settings for the policy.
    type: dict
    suboptions:
      enabled_state:
        description:
          - >-
            Describes if the policy is in enabled or disabled state. Defaults to
            Enabled if not specified.
        type: str
        choices:
          - Disabled
          - Enabled
      mode:
        description:
          - >-
            Describes if it is in detection mode or prevention mode at policy
            level.
        type: str
        choices:
          - Prevention
          - Detection
      redirect_url:
        description:
          - >-
            If action type is redirect, this field represents redirect URL for
            the client.
        type: str
      custom_block_response_status_code:
        description:
          - >-
            If the action type is block, customer can override the response
            status code.
        type: integer
      custom_block_response_body:
        description:
          - >-
            If the action type is block, customer can override the response
            body. The body must be specified in base64 encoding.
        type: str
  custom_rules:
    description:
      - Describes custom rules inside the policy.
    type: dict
    suboptions:
      rules:
        description:
          - List of rules
        type: list
        suboptions:
          name:
            description:
              - Describes the name of the rule.
            type: str
          priority:
            description:
              - >-
                Describes priority of the rule. Rules with a lower value will be
                evaluated before rules with a higher value.
            required: true
            type: integer
          enabled_state:
            description:
              - >-
                Describes if the custom rule is in enabled or disabled state.
                Defaults to Enabled if not specified.
            type: str
            choices:
              - Disabled
              - Enabled
          rule_type:
            description:
              - Describes type of rule.
            required: true
            type: str
            choices:
              - MatchRule
              - RateLimitRule
          rate_limit_duration_in_minutes:
            description:
              - >-
                Time window for resetting the rate limit count. Default is 1
                minute.
            type: integer
          rate_limit_threshold:
            description:
              - Number of allowed requests per client within the time window.
            type: integer
          match_conditions:
            description:
              - List of match conditions.
            required: true
            type: list
            suboptions:
              match_variable:
                description:
                  - Request variable to compare with.
                required: true
                type: str
                choices:
                  - RemoteAddr
                  - RequestMethod
                  - QueryString
                  - PostArgs
                  - RequestUri
                  - RequestHeader
                  - RequestBody
                  - Cookies
                  - SocketAddr
              selector:
                description:
                  - >-
                    Match against a specific key from the QueryString, PostArgs,
                    RequestHeader or Cookies variables. Default is null.
                type: str
              operator:
                description:
                  - Comparison type to use for matching with the variable value.
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
                  - RegEx
              negate_condition:
                description:
                  - Describes if the result of this condition should be negated.
                type: bool
              match_value:
                description:
                  - List of possible match values.
                required: true
                type: list
              transforms:
                description:
                  - List of transforms.
                type: list
          action:
            description:
              - Describes what action to be applied when rule matches.
            required: true
            type: str
            choices:
              - Allow
              - Block
              - Log
              - Redirect
  managed_rules:
    description:
      - Describes managed rules inside the policy.
    type: dict
    suboptions:
      managed_rule_sets:
        description:
          - List of rule sets.
        type: list
        suboptions:
          rule_set_type:
            description:
              - Defines the rule set type to use.
            required: true
            type: str
          rule_set_version:
            description:
              - Defines the version of the rule set to use.
            required: true
            type: str
          exclusions:
            description:
              - >-
                Describes the exclusions that are applied to all rules in the
                set.
            type: list
            suboptions:
              match_variable:
                description:
                  - The variable type to be excluded.
                required: true
                type: str
                choices:
                  - RequestHeaderNames
                  - RequestCookieNames
                  - QueryStringArgNames
                  - RequestBodyPostArgNames
              selector_match_operator:
                description:
                  - >-
                    Comparison operator to apply to the selector when specifying
                    which elements in the collection this exclusion applies to.
                required: true
                type: str
                choices:
                  - Equals
                  - Contains
                  - StartsWith
                  - EndsWith
                  - EqualsAny
              selector:
                description:
                  - >-
                    Selector value for which elements in the collection this
                    exclusion applies to.
                required: true
                type: str
          rule_group_overrides:
            description:
              - Defines the rule group overrides to apply to the rule set.
            type: list
            suboptions:
              rule_group_name:
                description:
                  - Describes the managed rule group to override.
                required: true
                type: str
              exclusions:
                description:
                  - >-
                    Describes the exclusions that are applied to all rules in
                    the group.
                type: list
                suboptions:
                  match_variable:
                    description:
                      - The variable type to be excluded.
                    required: true
                    type: str
                    choices:
                      - RequestHeaderNames
                      - RequestCookieNames
                      - QueryStringArgNames
                      - RequestBodyPostArgNames
                  selector_match_operator:
                    description:
                      - >-
                        Comparison operator to apply to the selector when
                        specifying which elements in the collection this
                        exclusion applies to.
                    required: true
                    type: str
                    choices:
                      - Equals
                      - Contains
                      - StartsWith
                      - EndsWith
                      - EqualsAny
                  selector:
                    description:
                      - >-
                        Selector value for which elements in the collection this
                        exclusion applies to.
                    required: true
                    type: str
              rules:
                description:
                  - >-
                    List of rules that will be disabled. If none specified, all
                    rules in the group will be disabled.
                type: list
                suboptions:
                  rule_id:
                    description:
                      - Identifier for the managed rule.
                    required: true
                    type: str
                  enabled_state:
                    description:
                      - >-
                        Describes if the managed rule is in enabled or disabled
                        state. Defaults to Disabled if not specified.
                    type: str
                    choices:
                      - Disabled
                      - Enabled
                  action:
                    description:
                      - >-
                        Describes the override action to be applied when rule
                        matches.
                    type: str
                    choices:
                      - Allow
                      - Block
                      - Log
                      - Redirect
                  exclusions:
                    description:
                      - >-
                        Describes the exclusions that are applied to this
                        specific rule.
                    type: list
                    suboptions:
                      match_variable:
                        description:
                          - The variable type to be excluded.
                        required: true
                        type: str
                        choices:
                          - RequestHeaderNames
                          - RequestCookieNames
                          - QueryStringArgNames
                          - RequestBodyPostArgNames
                      selector_match_operator:
                        description:
                          - >-
                            Comparison operator to apply to the selector when
                            specifying which elements in the collection this
                            exclusion applies to.
                        required: true
                        type: str
                        choices:
                          - Equals
                          - Contains
                          - StartsWith
                          - EndsWith
                          - EqualsAny
                      selector:
                        description:
                          - >-
                            Selector value for which elements in the collection
                            this exclusion applies to.
                        required: true
                        type: str
  state:
    description:
      - Assert the state of the Policy.
      - Use C(present) to create or update an Policy and C(absent) to delete it.
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
    - name: Creates specific policy
      azure_rm_policy: 
        policy_name: Policy1
        resource_group_name: rg1
        properties:
          custom_rules:
            rules:
              - name: Rule1
                action: Block
                match_conditions:
                  - match_value:
                      - 192.168.1.0/24
                      - 10.0.0.0/24
                    match_variable: RemoteAddr
                    operator: IPMatch
                priority: 1
                rate_limit_threshold: 1000
                rule_type: RateLimitRule
              - name: Rule2
                action: Block
                match_conditions:
                  - match_value:
                      - CH
                    match_variable: RemoteAddr
                    operator: GeoMatch
                  - match_value:
                      - windows
                    match_variable: RequestHeader
                    operator: Contains
                    selector: UserAgent
                    transforms:
                      - Lowercase
                priority: 2
                rule_type: MatchRule
          managed_rules:
            managed_rule_sets:
              - exclusions:
                  - match_variable: RequestHeaderNames
                    selector: User-Agent
                    selector_match_operator: Equals
                rule_group_overrides:
                  - exclusions:
                      - match_variable: RequestCookieNames
                        selector: token
                        selector_match_operator: StartsWith
                    rule_group_name: SQLI
                    rules:
                      - action: Redirect
                        enabled_state: Enabled
                        exclusions:
                          - match_variable: QueryStringArgNames
                            selector: query
                            selector_match_operator: Equals
                        rule_id: '942100'
                      - enabled_state: Disabled
                        rule_id: '942110'
                rule_set_type: DefaultRuleSet
                rule_set_version: '1.0'
          policy_settings:
            custom_block_response_body: >-
              PGh0bWw+CjxoZWFkZXI+PHRpdGxlPkhlbGxvPC90aXRsZT48L2hlYWRlcj4KPGJvZHk+CkhlbGxvIHdvcmxkCjwvYm9keT4KPC9odG1sPg==
            custom_block_response_status_code: 499
            redirect_url: 'http://www.bing.com'
        

    - name: Delete protection policy
      azure_rm_policy: 
        policy_name: Policy1
        resource_group_name: rg1
        

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
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
etag:
  description:
    - >-
      Gets a unique read-only string that changes whenever the resource is
      updated.
  returned: always
  type: str
  sample: null
policy_settings:
  description:
    - Describes settings for the policy.
  returned: always
  type: dict
  sample: null
  contains:
    enabled_state:
      description:
        - >-
          Describes if the policy is in enabled or disabled state. Defaults to
          Enabled if not specified.
      returned: always
      type: str
      sample: null
    mode:
      description:
        - >-
          Describes if it is in detection mode or prevention mode at policy
          level.
      returned: always
      type: str
      sample: null
    redirect_url:
      description:
        - >-
          If action type is redirect, this field represents redirect URL for the
          client.
      returned: always
      type: str
      sample: null
    custom_block_response_status_code:
      description:
        - >-
          If the action type is block, customer can override the response status
          code.
      returned: always
      type: integer
      sample: null
    custom_block_response_body:
      description:
        - >-
          If the action type is block, customer can override the response body.
          The body must be specified in base64 encoding.
      returned: always
      type: str
      sample: null
custom_rules:
  description:
    - Describes custom rules inside the policy.
  returned: always
  type: dict
  sample: null
  contains:
    rules:
      description:
        - List of rules
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Describes the name of the rule.
          returned: always
          type: str
          sample: null
        priority:
          description:
            - >-
              Describes priority of the rule. Rules with a lower value will be
              evaluated before rules with a higher value.
          returned: always
          type: integer
          sample: null
        enabled_state:
          description:
            - >-
              Describes if the custom rule is in enabled or disabled state.
              Defaults to Enabled if not specified.
          returned: always
          type: str
          sample: null
        rule_type:
          description:
            - Describes type of rule.
          returned: always
          type: str
          sample: null
        rate_limit_duration_in_minutes:
          description:
            - >-
              Time window for resetting the rate limit count. Default is 1
              minute.
          returned: always
          type: integer
          sample: null
        rate_limit_threshold:
          description:
            - Number of allowed requests per client within the time window.
          returned: always
          type: integer
          sample: null
        match_conditions:
          description:
            - List of match conditions.
          returned: always
          type: list
          sample: null
          contains:
            match_variable:
              description:
                - Request variable to compare with.
              returned: always
              type: str
              sample: null
            selector:
              description:
                - >-
                  Match against a specific key from the QueryString, PostArgs,
                  RequestHeader or Cookies variables. Default is null.
              returned: always
              type: str
              sample: null
            operator:
              description:
                - Comparison type to use for matching with the variable value.
              returned: always
              type: str
              sample: null
            negate_condition:
              description:
                - Describes if the result of this condition should be negated.
              returned: always
              type: bool
              sample: null
            match_value:
              description:
                - List of possible match values.
              returned: always
              type: list
              sample: null
            transforms:
              description:
                - List of transforms.
              returned: always
              type: list
              sample: null
        action:
          description:
            - Describes what action to be applied when rule matches.
          returned: always
          type: str
          sample: null
managed_rules:
  description:
    - Describes managed rules inside the policy.
  returned: always
  type: dict
  sample: null
  contains:
    managed_rule_sets:
      description:
        - List of rule sets.
      returned: always
      type: list
      sample: null
      contains:
        rule_set_type:
          description:
            - Defines the rule set type to use.
          returned: always
          type: str
          sample: null
        rule_set_version:
          description:
            - Defines the version of the rule set to use.
          returned: always
          type: str
          sample: null
        exclusions:
          description:
            - Describes the exclusions that are applied to all rules in the set.
          returned: always
          type: list
          sample: null
          contains:
            match_variable:
              description:
                - The variable type to be excluded.
              returned: always
              type: str
              sample: null
            selector_match_operator:
              description:
                - >-
                  Comparison operator to apply to the selector when specifying
                  which elements in the collection this exclusion applies to.
              returned: always
              type: str
              sample: null
            selector:
              description:
                - >-
                  Selector value for which elements in the collection this
                  exclusion applies to.
              returned: always
              type: str
              sample: null
        rule_group_overrides:
          description:
            - Defines the rule group overrides to apply to the rule set.
          returned: always
          type: list
          sample: null
          contains:
            rule_group_name:
              description:
                - Describes the managed rule group to override.
              returned: always
              type: str
              sample: null
            exclusions:
              description:
                - >-
                  Describes the exclusions that are applied to all rules in the
                  group.
              returned: always
              type: list
              sample: null
              contains:
                match_variable:
                  description:
                    - The variable type to be excluded.
                  returned: always
                  type: str
                  sample: null
                selector_match_operator:
                  description:
                    - >-
                      Comparison operator to apply to the selector when
                      specifying which elements in the collection this exclusion
                      applies to.
                  returned: always
                  type: str
                  sample: null
                selector:
                  description:
                    - >-
                      Selector value for which elements in the collection this
                      exclusion applies to.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - >-
                  List of rules that will be disabled. If none specified, all
                  rules in the group will be disabled.
              returned: always
              type: list
              sample: null
              contains:
                rule_id:
                  description:
                    - Identifier for the managed rule.
                  returned: always
                  type: str
                  sample: null
                enabled_state:
                  description:
                    - >-
                      Describes if the managed rule is in enabled or disabled
                      state. Defaults to Disabled if not specified.
                  returned: always
                  type: str
                  sample: null
                action:
                  description:
                    - >-
                      Describes the override action to be applied when rule
                      matches.
                  returned: always
                  type: str
                  sample: null
                exclusions:
                  description:
                    - >-
                      Describes the exclusions that are applied to this specific
                      rule.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    match_variable:
                      description:
                        - The variable type to be excluded.
                      returned: always
                      type: str
                      sample: null
                    selector_match_operator:
                      description:
                        - >-
                          Comparison operator to apply to the selector when
                          specifying which elements in the collection this
                          exclusion applies to.
                      returned: always
                      type: str
                      sample: null
                    selector:
                      description:
                        - >-
                          Selector value for which elements in the collection
                          this exclusion applies to.
                      returned: always
                      type: str
                      sample: null
frontend_endpoint_links:
  description:
    - >-
      Describes Frontend Endpoints associated with this Web Application Firewall
      policy.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
routing_rule_links:
  description:
    - >-
      Describes Routing Rules associated with this Web Application Firewall
      policy.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - Provisioning state of the policy.
  returned: always
  type: str
  sample: null
resource_state:
  description:
    - Resource status of the policy.
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


class AzureRMPolicy(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            policy_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            policy_settings=dict(
                type='dict',
                disposition='/policy_settings',
                options=dict(
                    enabled_state=dict(
                        type='str',
                        disposition='enabled_state',
                        choices=['Disabled',
                                 'Enabled']
                    ),
                    mode=dict(
                        type='str',
                        disposition='mode',
                        choices=['Prevention',
                                 'Detection']
                    ),
                    redirect_url=dict(
                        type='str',
                        disposition='redirect_url'
                    ),
                    custom_block_response_status_code=dict(
                        type='integer',
                        disposition='custom_block_response_status_code'
                    ),
                    custom_block_response_body=dict(
                        type='str',
                        disposition='custom_block_response_body'
                    )
                )
            ),
            custom_rules=dict(
                type='dict',
                disposition='/custom_rules',
                options=dict(
                    rules=dict(
                        type='list',
                        disposition='rules',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            priority=dict(
                                type='integer',
                                disposition='priority',
                                required=True
                            ),
                            enabled_state=dict(
                                type='str',
                                disposition='enabled_state',
                                choices=['Disabled',
                                         'Enabled']
                            ),
                            rule_type=dict(
                                type='str',
                                disposition='rule_type',
                                choices=['MatchRule',
                                         'RateLimitRule'],
                                required=True
                            ),
                            rate_limit_duration_in_minutes=dict(
                                type='integer',
                                disposition='rate_limit_duration_in_minutes'
                            ),
                            rate_limit_threshold=dict(
                                type='integer',
                                disposition='rate_limit_threshold'
                            ),
                            match_conditions=dict(
                                type='list',
                                disposition='match_conditions',
                                required=True,
                                elements='dict',
                                options=dict(
                                    match_variable=dict(
                                        type='str',
                                        disposition='match_variable',
                                        choices=['RemoteAddr',
                                                 'RequestMethod',
                                                 'QueryString',
                                                 'PostArgs',
                                                 'RequestUri',
                                                 'RequestHeader',
                                                 'RequestBody',
                                                 'Cookies',
                                                 'SocketAddr'],
                                        required=True
                                    ),
                                    selector=dict(
                                        type='str',
                                        disposition='selector'
                                    ),
                                    operator=dict(
                                        type='str',
                                        disposition='operator',
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
                                                 'EndsWith',
                                                 'RegEx'],
                                        required=True
                                    ),
                                    negate_condition=dict(
                                        type='bool',
                                        disposition='negate_condition'
                                    ),
                                    match_value=dict(
                                        type='list',
                                        disposition='match_value',
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
                            action=dict(
                                type='str',
                                disposition='action',
                                choices=['Allow',
                                         'Block',
                                         'Log',
                                         'Redirect'],
                                required=True
                            )
                        )
                    )
                )
            ),
            managed_rules=dict(
                type='dict',
                disposition='/managed_rules',
                options=dict(
                    managed_rule_sets=dict(
                        type='list',
                        disposition='managed_rule_sets',
                        elements='dict',
                        options=dict(
                            rule_set_type=dict(
                                type='str',
                                disposition='rule_set_type',
                                required=True
                            ),
                            rule_set_version=dict(
                                type='str',
                                disposition='rule_set_version',
                                required=True
                            ),
                            exclusions=dict(
                                type='list',
                                disposition='exclusions',
                                elements='dict',
                                options=dict(
                                    match_variable=dict(
                                        type='str',
                                        disposition='match_variable',
                                        choices=['RequestHeaderNames',
                                                 'RequestCookieNames',
                                                 'QueryStringArgNames',
                                                 'RequestBodyPostArgNames'],
                                        required=True
                                    ),
                                    selector_match_operator=dict(
                                        type='str',
                                        disposition='selector_match_operator',
                                        choices=['Equals',
                                                 'Contains',
                                                 'StartsWith',
                                                 'EndsWith',
                                                 'EqualsAny'],
                                        required=True
                                    ),
                                    selector=dict(
                                        type='str',
                                        disposition='selector',
                                        required=True
                                    )
                                )
                            ),
                            rule_group_overrides=dict(
                                type='list',
                                disposition='rule_group_overrides',
                                elements='dict',
                                options=dict(
                                    rule_group_name=dict(
                                        type='str',
                                        disposition='rule_group_name',
                                        required=True
                                    ),
                                    exclusions=dict(
                                        type='list',
                                        disposition='exclusions',
                                        elements='dict',
                                        options=dict(
                                            match_variable=dict(
                                                type='str',
                                                disposition='match_variable',
                                                choices=['RequestHeaderNames',
                                                         'RequestCookieNames',
                                                         'QueryStringArgNames',
                                                         'RequestBodyPostArgNames'],
                                                required=True
                                            ),
                                            selector_match_operator=dict(
                                                type='str',
                                                disposition='selector_match_operator',
                                                choices=['Equals',
                                                         'Contains',
                                                         'StartsWith',
                                                         'EndsWith',
                                                         'EqualsAny'],
                                                required=True
                                            ),
                                            selector=dict(
                                                type='str',
                                                disposition='selector',
                                                required=True
                                            )
                                        )
                                    ),
                                    rules=dict(
                                        type='list',
                                        disposition='rules',
                                        elements='dict',
                                        options=dict(
                                            rule_id=dict(
                                                type='str',
                                                disposition='rule_id',
                                                required=True
                                            ),
                                            enabled_state=dict(
                                                type='str',
                                                disposition='enabled_state',
                                                choices=['Disabled',
                                                         'Enabled']
                                            ),
                                            action=dict(
                                                type='str',
                                                disposition='action',
                                                choices=['Allow',
                                                         'Block',
                                                         'Log',
                                                         'Redirect']
                                            ),
                                            exclusions=dict(
                                                type='list',
                                                disposition='exclusions',
                                                elements='dict',
                                                options=dict(
                                                    match_variable=dict(
                                                        type='str',
                                                        disposition='match_variable',
                                                        choices=['RequestHeaderNames',
                                                                 'RequestCookieNames',
                                                                 'QueryStringArgNames',
                                                                 'RequestBodyPostArgNames'],
                                                        required=True
                                                    ),
                                                    selector_match_operator=dict(
                                                        type='str',
                                                        disposition='selector_match_operator',
                                                        choices=['Equals',
                                                                 'Contains',
                                                                 'StartsWith',
                                                                 'EndsWith',
                                                                 'EqualsAny'],
                                                        required=True
                                                    ),
                                                    selector=dict(
                                                        type='str',
                                                        disposition='selector',
                                                        required=True
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
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
        self.policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-04-01')

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
            response = self.mgmt_client.policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                  policy_name=self.policy_name,
                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Policy instance.')
            self.fail('Error creating the Policy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.policies.delete(resource_group_name=self.resource_group_name,
                                                        policy_name=self.policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the Policy instance.')
            self.fail('Error deleting the Policy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.policies.get(resource_group_name=self.resource_group_name,
                                                     policy_name=self.policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPolicy()


if __name__ == '__main__':
    main()
