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
module: azure_rm_policy_info
version_added: '2.9'
short_description: Get Policy info.
description:
  - Get info of Policy.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  policy_name:
    description:
      - The name of the Web Application Firewall Policy.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Policies in a Resource Group
      azure_rm_policy_info: 
        resource_group_name: rg1
        

    - name: Get Policy
      azure_rm_policy_info: 
        policy_name: Policy1
        resource_group_name: rg1
        

'''

RETURN = '''
policies:
  description: >-
    A list of dict results where the key is the name of the Policy and the
    values are the facts for that Policy.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of WebApplicationFirewallPolicies within a resource group.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - >-
              Gets a unique read-only string that changes whenever the resource
              is updated.
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
                  Describes if the policy is in enabled or disabled state.
                  Defaults to Enabled if not specified.
              returned: always
              type: str
              sample: null
            mode:
              description:
                - >-
                  Describes if it is in detection mode or prevention mode at
                  policy level.
              returned: always
              type: str
              sample: null
            redirect_url:
              description:
                - >-
                  If action type is redirect, this field represents redirect URL
                  for the client.
              returned: always
              type: str
              sample: null
            custom_block_response_status_code:
              description:
                - >-
                  If the action type is block, customer can override the
                  response status code.
              returned: always
              type: integer
              sample: null
            custom_block_response_body:
              description:
                - >-
                  If the action type is block, customer can override the
                  response body. The body must be specified in base64 encoding.
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
                      Describes priority of the rule. Rules with a lower value
                      will be evaluated before rules with a higher value.
                  returned: always
                  type: integer
                  sample: null
                enabled_state:
                  description:
                    - >-
                      Describes if the custom rule is in enabled or disabled
                      state. Defaults to Enabled if not specified.
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
                      Time window for resetting the rate limit count. Default is
                      1 minute.
                  returned: always
                  type: integer
                  sample: null
                rate_limit_threshold:
                  description:
                    - >-
                      Number of allowed requests per client within the time
                      window.
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
                          Match against a specific key from the QueryString,
                          PostArgs, RequestHeader or Cookies variables. Default
                          is null.
                      returned: always
                      type: str
                      sample: null
                    operator:
                      description:
                        - >-
                          Comparison type to use for matching with the variable
                          value.
                      returned: always
                      type: str
                      sample: null
                    negate_condition:
                      description:
                        - >-
                          Describes if the result of this condition should be
                          negated.
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
                    - >-
                      Describes the exclusions that are applied to all rules in
                      the set.
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
                          Describes the exclusions that are applied to all rules
                          in the group.
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
                              Selector value for which elements in the
                              collection this exclusion applies to.
                          returned: always
                          type: str
                          sample: null
                    rules:
                      description:
                        - >-
                          List of rules that will be disabled. If none
                          specified, all rules in the group will be disabled.
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
                              Describes if the managed rule is in enabled or
                              disabled state. Defaults to Disabled if not
                              specified.
                          returned: always
                          type: str
                          sample: null
                        action:
                          description:
                            - >-
                              Describes the override action to be applied when
                              rule matches.
                          returned: always
                          type: str
                          sample: null
                        exclusions:
                          description:
                            - >-
                              Describes the exclusions that are applied to this
                              specific rule.
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
                                  Comparison operator to apply to the selector
                                  when specifying which elements in the
                                  collection this exclusion applies to.
                              returned: always
                              type: str
                              sample: null
                            selector:
                              description:
                                - >-
                                  Selector value for which elements in the
                                  collection this exclusion applies to.
                              returned: always
                              type: str
                              sample: null
        frontend_endpoint_links:
          description:
            - >-
              Describes Frontend Endpoints associated with this Web Application
              Firewall policy.
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
              Describes Routing Rules associated with this Web Application
              Firewall policy.
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
    next_link:
      description:
        - >-
          URL to get the next set of WebApplicationFirewallPolicy objects if
          there are any.
      returned: always
      type: str
      sample: null
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
              Describes if the policy is in enabled or disabled state. Defaults
              to Enabled if not specified.
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
              If action type is redirect, this field represents redirect URL for
              the client.
          returned: always
          type: str
          sample: null
        custom_block_response_status_code:
          description:
            - >-
              If the action type is block, customer can override the response
              status code.
          returned: always
          type: integer
          sample: null
        custom_block_response_body:
          description:
            - >-
              If the action type is block, customer can override the response
              body. The body must be specified in base64 encoding.
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
                  Describes priority of the rule. Rules with a lower value will
                  be evaluated before rules with a higher value.
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
                      Match against a specific key from the QueryString,
                      PostArgs, RequestHeader or Cookies variables. Default is
                      null.
                  returned: always
                  type: str
                  sample: null
                operator:
                  description:
                    - >-
                      Comparison type to use for matching with the variable
                      value.
                  returned: always
                  type: str
                  sample: null
                negate_condition:
                  description:
                    - >-
                      Describes if the result of this condition should be
                      negated.
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
                - >-
                  Describes the exclusions that are applied to all rules in the
                  set.
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
                      Describes the exclusions that are applied to all rules in
                      the group.
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
                rules:
                  description:
                    - >-
                      List of rules that will be disabled. If none specified,
                      all rules in the group will be disabled.
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
                          Describes if the managed rule is in enabled or
                          disabled state. Defaults to Disabled if not specified.
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
                          Describes the exclusions that are applied to this
                          specific rule.
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
                              Selector value for which elements in the
                              collection this exclusion applies to.
                          returned: always
                          type: str
                          sample: null
    frontend_endpoint_links:
      description:
        - >-
          Describes Frontend Endpoints associated with this Web Application
          Firewall policy.
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


class AzureRMPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            policy_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.policy_name is not None):
            self.results['policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['policies'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.policies.get(resource_group_name=self.resource_group_name,
                                                     policy_name=self.policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.policies.list(resource_group_name=self.resource_group_name)
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
    AzureRMPolicyInfo()


if __name__ == '__main__':
    main()
