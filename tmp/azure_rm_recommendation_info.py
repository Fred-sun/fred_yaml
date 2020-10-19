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
module: azure_rm_recommendation_info
version_added: '2.9'
short_description: Get Recommendation info.
description:
  - Get info of Recommendation.
options:
  operation_id:
    description:
      - >-
        The operation ID, which can be found from the Location field in the
        generate recommendation response header.
    type: uuid
  filter:
    description:
      - >-
        The filter to apply to the recommendations.<br>Filter can be applied to
        properties ['ResourceId', 'ResourceGroup', 'RecommendationTypeGuid',
        '[Category](#category)'] with operators ['eq', 'and',
        'or'].<br>Example:<br>- $filter=Category eq 'Cost' and ResourceGroup eq
        'MyResourceGroup'
    type: str
  top:
    description:
      - >-
        The number of recommendations per page if a paged version of this API is
        being used.
    type: integer
  skip_token:
    description:
      - The page-continuation token to use with a paged version of this API.
    type: str
  resource_uri:
    description:
      - >-
        The fully qualified Azure Resource Manager identifier of the resource to
        which the recommendation applies.
    type: str
  recommendation_id:
    description:
      - The recommendation ID.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetGenerateStatus
      azure_rm_recommendation_info: 
        operation_id: operationGUID
        

    - name: ListRecommendations
      azure_rm_recommendation_info: 
        {}
        

    - name: GetRecommendationDetail
      azure_rm_recommendation_info: 
        recommendation_id: recommendationId
        resource_uri: resourceUri
        

'''

RETURN = '''
recommendations:
  description: >-
    A list of dict results where the key is the name of the Recommendation and
    the values are the facts for that Recommendation.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - The link used to get the next page of recommendations.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of recommendations.
      returned: always
      type: list
      sample: null
      contains:
        category:
          description:
            - The category of the recommendation.
          returned: always
          type: str
          sample: null
        impact:
          description:
            - The business impact of the recommendation.
          returned: always
          type: str
          sample: null
        impacted_field:
          description:
            - The resource type identified by Advisor.
          returned: always
          type: str
          sample: null
        impacted_value:
          description:
            - The resource identified by Advisor.
          returned: always
          type: str
          sample: null
        last_updated:
          description:
            - >-
              The most recent time that Advisor checked the validity of the
              recommendation.
          returned: always
          type: str
          sample: null
        metadata:
          description:
            - The recommendation metadata.
          returned: always
          type: dictionary
          sample: null
        recommendation_type_id:
          description:
            - The recommendation-type GUID.
          returned: always
          type: str
          sample: null
        risk:
          description:
            - The potential risk of not implementing the recommendation.
          returned: always
          type: str
          sample: null
        short_description:
          description:
            - A summary of the recommendation.
          returned: always
          type: dict
          sample: null
          contains:
            problem:
              description:
                - The issue or opportunity identified by the recommendation.
              returned: always
              type: str
              sample: null
            solution:
              description:
                - The remediation action suggested by the recommendation.
              returned: always
              type: str
              sample: null
        suppression_ids:
          description:
            - The list of snoozed and dismissed rules for the recommendation.
          returned: always
          type: list
          sample: null
        extended_properties:
          description:
            - Extended properties
          returned: always
          type: dictionary
          sample: null
        resource_metadata:
          description:
            - Metadata of resource that was assessed
          returned: always
          type: dict
          sample: null
          contains:
            resource_id:
              description:
                - Azure resource Id of the assessed resource
              returned: always
              type: str
              sample: null
            source:
              description:
                - Source from which recommendation is generated
              returned: always
              type: str
              sample: null
    id:
      description:
        - The resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    category:
      description:
        - The category of the recommendation.
      returned: always
      type: str
      sample: null
    impact:
      description:
        - The business impact of the recommendation.
      returned: always
      type: str
      sample: null
    impacted_field:
      description:
        - The resource type identified by Advisor.
      returned: always
      type: str
      sample: null
    impacted_value:
      description:
        - The resource identified by Advisor.
      returned: always
      type: str
      sample: null
    last_updated:
      description:
        - >-
          The most recent time that Advisor checked the validity of the
          recommendation.
      returned: always
      type: str
      sample: null
    metadata:
      description:
        - The recommendation metadata.
      returned: always
      type: dictionary
      sample: null
    recommendation_type_id:
      description:
        - The recommendation-type GUID.
      returned: always
      type: str
      sample: null
    risk:
      description:
        - The potential risk of not implementing the recommendation.
      returned: always
      type: str
      sample: null
    short_description:
      description:
        - A summary of the recommendation.
      returned: always
      type: dict
      sample: null
      contains:
        problem:
          description:
            - The issue or opportunity identified by the recommendation.
          returned: always
          type: str
          sample: null
        solution:
          description:
            - The remediation action suggested by the recommendation.
          returned: always
          type: str
          sample: null
    suppression_ids:
      description:
        - The list of snoozed and dismissed rules for the recommendation.
      returned: always
      type: list
      sample: null
    extended_properties:
      description:
        - Extended properties
      returned: always
      type: dictionary
      sample: null
    resource_metadata:
      description:
        - Metadata of resource that was assessed
      returned: always
      type: dict
      sample: null
      contains:
        resource_id:
          description:
            - Azure resource Id of the assessed resource
          returned: always
          type: str
          sample: null
        source:
          description:
            - Source from which recommendation is generated
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
    from azure.mgmt.advisor import AdvisorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRecommendationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            operation_id=dict(
                type='uuid'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip_token=dict(
                type='str'
            ),
            resource_uri=dict(
                type='str'
            ),
            recommendation_id=dict(
                type='str'
            )
        )

        self.operation_id = None
        self.filter = None
        self.top = None
        self.skip_token = None
        self.resource_uri = None
        self.recommendation_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRecommendationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AdvisorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_uri is not None and
            self.recommendation_id is not None):
            self.results['recommendations'] = self.format_item(self.get())
        elif (self.operation_id is not None):
            self.results['recommendations'] = self.format_item(self.getgeneratestatus())
        else:
            self.results['recommendations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.recommendations.get(resource_uri=self.resource_uri,
                                                            recommendation_id=self.recommendation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getgeneratestatus(self):
        response = None

        try:
            response = self.mgmt_client.recommendations.get_generate_status(operation_id=self.operation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.recommendations.list(filter=self.filter,
                                                             top=self.top,
                                                             skip_token=self.skip_token)
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
    AzureRMRecommendationInfo()


if __name__ == '__main__':
    main()
