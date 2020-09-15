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
module: azure_rm_recommendedaction_info
version_added: '2.9'
short_description: Get RecommendedAction info.
description:
  - Get info of RecommendedAction.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  advisor_name:
    description:
      - The advisor name for recommendation action.
    required: true
    type: str
  recommended_action_name:
    description:
      - The recommended action name.
    type: str
  session_id:
    description:
      - The recommendation action session identifier.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RecommendedActionsGet
      azure_rm_recommendedaction_info: 
        advisor_name: Index
        recommended_action_name: Index-1
        resource_group_name: testResourceGroupName
        server_name: testServerName
        

    - name: RecommendedActionsListByServer
      azure_rm_recommendedaction_info: 
        advisor_name: Index
        resource_group_name: testResourceGroupName
        server_name: testServerName
        

'''

RETURN = '''
recommended_actions:
  description: >-
    A list of dict results where the key is the name of the RecommendedAction
    and the values are the facts for that RecommendedAction.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    advisor_name:
      description:
        - Advisor name.
      returned: always
      type: str
      sample: null
    session_id:
      description:
        - Recommendation action session identifier.
      returned: always
      type: str
      sample: null
    action_id:
      description:
        - Recommendation action identifier.
      returned: always
      type: integer
      sample: null
    created_time:
      description:
        - Recommendation action creation time.
      returned: always
      type: str
      sample: null
    expiration_time:
      description:
        - Recommendation action expiration time.
      returned: always
      type: str
      sample: null
    reason:
      description:
        - Recommendation action reason.
      returned: always
      type: str
      sample: null
    recommendation_type:
      description:
        - Recommendation action type.
      returned: always
      type: str
      sample: null
    details:
      description:
        - Recommendation action details.
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - The list of recommendation action advisors.
      returned: always
      type: list
      sample: null
      contains:
        advisor_name:
          description:
            - Advisor name.
          returned: always
          type: str
          sample: null
        session_id:
          description:
            - Recommendation action session identifier.
          returned: always
          type: str
          sample: null
        action_id:
          description:
            - Recommendation action identifier.
          returned: always
          type: integer
          sample: null
        created_time:
          description:
            - Recommendation action creation time.
          returned: always
          type: str
          sample: null
        expiration_time:
          description:
            - Recommendation action expiration time.
          returned: always
          type: str
          sample: null
        reason:
          description:
            - Recommendation action reason.
          returned: always
          type: str
          sample: null
        recommendation_type:
          description:
            - Recommendation action type.
          returned: always
          type: str
          sample: null
        details:
          description:
            - Recommendation action details.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.my import MySQLManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRecommendedActionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            advisor_name=dict(
                type='str',
                required=True
            ),
            recommended_action_name=dict(
                type='str'
            ),
            session_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.advisor_name = None
        self.recommended_action_name = None
        self.session_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRecommendedActionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.advisor_name is not None and
            self.recommended_action_name is not None):
            self.results['recommended_actions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.advisor_name is not None):
            self.results['recommended_actions'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.recommended_actions.get(resource_group_name=self.resource_group_name,
                                                                server_name=self.server_name,
                                                                advisor_name=self.advisor_name,
                                                                recommended_action_name=self.recommended_action_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.recommended_actions.list_by_server(resource_group_name=self.resource_group_name,
                                                                           server_name=self.server_name,
                                                                           advisor_name=self.advisor_name,
                                                                           session_id=self.session_id)
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
    AzureRMRecommendedActionInfo()


if __name__ == '__main__':
    main()
