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
module: azure_rm_authorizationpolicy_info
version_added: '2.9'
short_description: Get AuthorizationPolicy info.
description:
  - Get info of AuthorizationPolicy.
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
  authorization_policy_name:
    description:
      - The name of the policy.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: AuthorizationPolicies_Get
      azure_rm_authorizationpolicy_info: 
        authorization_policy_name: testPolicy4222
        hub_name: azSdkTestHub
        resource_group_name: TestHubRG
        

    - name: AuthorizationPolicies_ListByHub
      azure_rm_authorizationpolicy_info: 
        hub_name: azSdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
authorization_policies:
  description: >-
    A list of dict results where the key is the name of the AuthorizationPolicy
    and the values are the facts for that AuthorizationPolicy.
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
    policy_name:
      description:
        - Name of the policy.
      returned: always
      type: str
      sample: null
    permissions:
      description:
        - The permissions associated with the policy.
      returned: always
      type: list
      sample: null
    primary_key:
      description:
        - Primary key associated with the policy.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - Secondary key associated with the policy.
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
        policy_name:
          description:
            - Name of the policy.
          returned: always
          type: str
          sample: null
        permissions:
          description:
            - The permissions associated with the policy.
          returned: always
          type: list
          sample: null
        primary_key:
          description:
            - Primary key associated with the policy.
          returned: always
          type: str
          sample: null
        secondary_key:
          description:
            - Secondary key associated with the policy.
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


class AzureRMAuthorizationPolicyInfo(AzureRMModuleBase):
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
            authorization_policy_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.authorization_policy_name = None

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
        super(AzureRMAuthorizationPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.authorization_policy_name is not None):
            self.results['authorization_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['authorization_policies'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.authorization_policies.get(resource_group_name=self.resource_group_name,
                                                                   hub_name=self.hub_name,
                                                                   authorization_policy_name=self.authorization_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.authorization_policies.list_by_hub(resource_group_name=self.resource_group_name,
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
    AzureRMAuthorizationPolicyInfo()


if __name__ == '__main__':
    main()
