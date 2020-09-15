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
module: azure_rm_locationbasedrecommendedactionsessionsresult_info
version_added: '2.9'
short_description: Get LocationBasedRecommendedActionSessionsResult info.
description:
  - Get info of LocationBasedRecommendedActionSessionsResult.
options:
  location_name:
    description:
      - The name of the location.
    required: true
    type: str
  operation_id:
    description:
      - The operation identifier.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RecommendedActionSessionResult
      azure_rm_locationbasedrecommendedactionsessionsresult_info: 
        operation_id: aaaabbbb-cccc-dddd-0000-111122223333
        location_name: WestUS
        

'''

RETURN = '''
location_based_recommended_action_sessions_result:
  description: >-
    A list of dict results where the key is the name of the
    LocationBasedRecommendedActionSessionsResult and the values are the facts
    for that LocationBasedRecommendedActionSessionsResult.
  returned: always
  type: complex
  contains:
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


class AzureRMLocationBasedRecommendedActionSessionsResultInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            operation_id=dict(
                type='str',
                required=True
            )
        )

        self.location_name = None
        self.operation_id = None

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
        super(AzureRMLocationBasedRecommendedActionSessionsResultInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01')

        if (self.location_name is not None and
            self.operation_id is not None):
            self.results['location_based_recommended_action_sessions_result'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.location_based_recommended_action_sessions_result.list(location_name=self.location_name,
                                                                                               operation_id=self.operation_id)
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
    AzureRMLocationBasedRecommendedActionSessionsResultInfo()


if __name__ == '__main__':
    main()
