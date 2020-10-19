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
module: azure_rm_managedruleset_info
version_added: '2.9'
short_description: Get ManagedRuleSet info.
description:
  - Get info of ManagedRuleSet.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Policies in a Resource Group
      azure_rm_managedruleset_info: 
        {}
        

'''

RETURN = '''
managed_rule_sets:
  description: >-
    A list of dict results where the key is the name of the ManagedRuleSet and
    the values are the facts for that ManagedRuleSet.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of managed rule set definitions.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - Provisioning state of the managed rule set.
          returned: always
          type: str
          sample: null
        rule_set_id:
          description:
            - Id of the managed rule set.
          returned: always
          type: str
          sample: null
        rule_set_type:
          description:
            - Type of the managed rule set.
          returned: always
          type: str
          sample: null
        rule_set_version:
          description:
            - Version of the managed rule set type.
          returned: always
          type: str
          sample: null
        rule_groups:
          description:
            - Rule groups of the managed rule set.
          returned: always
          type: list
          sample: null
          contains:
            rule_group_name:
              description:
                - Name of the managed rule group.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Description of the managed rule group.
              returned: always
              type: str
              sample: null
            rules:
              description:
                - List of rules within the managed rule group.
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
                default_state:
                  description:
                    - Describes the default state for the managed rule.
                  returned: always
                  type: str
                  sample: null
                default_action:
                  description:
                    - >-
                      Describes the default action to be applied when the
                      managed rule matches.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Describes the functionality of the managed rule.
                  returned: always
                  type: str
                  sample: null
    next_link:
      description:
        - URL to retrieve next set of managed rule set definitions.
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


class AzureRMManagedRuleSetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


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
        super(AzureRMManagedRuleSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        else:
            self.results['managed_rule_sets'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.managed_rule_sets.list()
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
    AzureRMManagedRuleSetInfo()


if __name__ == '__main__':
    main()
