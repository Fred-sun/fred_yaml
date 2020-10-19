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
module: azure_rm_prediction_info
version_added: '2.9'
short_description: Get Prediction info.
description:
  - Get info of Prediction.
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
  prediction_name:
    description:
      - The name of the Prediction.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Predictions_Get
      azure_rm_prediction_info: 
        hub_name: sdkTestHub
        prediction_name: sdktest
        resource_group_name: TestHubRG
        

    - name: Predictions_ListByHub
      azure_rm_prediction_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
predictions:
  description: >-
    A list of dict results where the key is the name of the Prediction and the
    values are the facts for that Prediction.
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
    description:
      description:
        - Description of the prediction.
      returned: always
      type: dictionary
      sample: null
    display_name:
      description:
        - Display name of the prediction.
      returned: always
      type: dictionary
      sample: null
    involved_interaction_types:
      description:
        - Interaction types involved in the prediction.
      returned: always
      type: list
      sample: null
    involved_kpi_types:
      description:
        - KPI types involved in the prediction.
      returned: always
      type: list
      sample: null
    involved_relationships:
      description:
        - Relationships involved in the prediction.
      returned: always
      type: list
      sample: null
    negative_outcome_expression:
      description:
        - Negative outcome expression.
      returned: always
      type: str
      sample: null
    positive_outcome_expression:
      description:
        - Positive outcome expression.
      returned: always
      type: str
      sample: null
    primary_profile_type:
      description:
        - Primary profile type.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state.
      returned: always
      type: str
      sample: null
    prediction_name:
      description:
        - Name of the prediction.
      returned: always
      type: str
      sample: null
    scope_expression:
      description:
        - Scope expression.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The hub name.
      returned: always
      type: str
      sample: null
    auto_analyze:
      description:
        - Whether do auto analyze.
      returned: always
      type: bool
      sample: null
    mappings:
      description:
        - Definition of the link mapping of prediction.
      returned: always
      type: dict
      sample: null
      contains:
        score:
          description:
            - The score of the link mapping.
          returned: always
          type: str
          sample: null
        grade:
          description:
            - The grade of the link mapping.
          returned: always
          type: str
          sample: null
        reason:
          description:
            - The reason of the link mapping.
          returned: always
          type: str
          sample: null
    score_label:
      description:
        - Score label.
      returned: always
      type: str
      sample: null
    grades:
      description:
        - The prediction grades.
      returned: always
      type: list
      sample: null
      contains:
        grade_name:
          description:
            - Name of the grade.
          returned: always
          type: str
          sample: null
        min_score_threshold:
          description:
            - Minimum score threshold.
          returned: always
          type: integer
          sample: null
        max_score_threshold:
          description:
            - Maximum score threshold.
          returned: always
          type: integer
          sample: null
    system_generated_entities:
      description:
        - System generated entities.
      returned: always
      type: dict
      sample: null
      contains:
        generated_interaction_types:
          description:
            - Generated interaction types.
          returned: always
          type: list
          sample: null
        generated_links:
          description:
            - Generated links.
          returned: always
          type: list
          sample: null
        generated_kpis:
          description:
            - Generated KPIs.
          returned: always
          type: dictionary
          sample: null
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - Description of the prediction.
          returned: always
          type: dictionary
          sample: null
        display_name:
          description:
            - Display name of the prediction.
          returned: always
          type: dictionary
          sample: null
        involved_interaction_types:
          description:
            - Interaction types involved in the prediction.
          returned: always
          type: list
          sample: null
        involved_kpi_types:
          description:
            - KPI types involved in the prediction.
          returned: always
          type: list
          sample: null
        involved_relationships:
          description:
            - Relationships involved in the prediction.
          returned: always
          type: list
          sample: null
        negative_outcome_expression:
          description:
            - Negative outcome expression.
          returned: always
          type: str
          sample: null
        positive_outcome_expression:
          description:
            - Positive outcome expression.
          returned: always
          type: str
          sample: null
        primary_profile_type:
          description:
            - Primary profile type.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state.
          returned: always
          type: str
          sample: null
        prediction_name:
          description:
            - Name of the prediction.
          returned: always
          type: str
          sample: null
        scope_expression:
          description:
            - Scope expression.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The hub name.
          returned: always
          type: str
          sample: null
        auto_analyze:
          description:
            - Whether do auto analyze.
          returned: always
          type: bool
          sample: null
        mappings:
          description:
            - Definition of the link mapping of prediction.
          returned: always
          type: dict
          sample: null
          contains:
            score:
              description:
                - The score of the link mapping.
              returned: always
              type: str
              sample: null
            grade:
              description:
                - The grade of the link mapping.
              returned: always
              type: str
              sample: null
            reason:
              description:
                - The reason of the link mapping.
              returned: always
              type: str
              sample: null
        score_label:
          description:
            - Score label.
          returned: always
          type: str
          sample: null
        grades:
          description:
            - The prediction grades.
          returned: always
          type: list
          sample: null
          contains:
            grade_name:
              description:
                - Name of the grade.
              returned: always
              type: str
              sample: null
            min_score_threshold:
              description:
                - Minimum score threshold.
              returned: always
              type: integer
              sample: null
            max_score_threshold:
              description:
                - Maximum score threshold.
              returned: always
              type: integer
              sample: null
        system_generated_entities:
          description:
            - System generated entities.
          returned: always
          type: dict
          sample: null
          contains:
            generated_interaction_types:
              description:
                - Generated interaction types.
              returned: always
              type: list
              sample: null
            generated_links:
              description:
                - Generated links.
              returned: always
              type: list
              sample: null
            generated_kpis:
              description:
                - Generated KPIs.
              returned: always
              type: dictionary
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


class AzureRMPredictionInfo(AzureRMModuleBase):
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
            prediction_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.prediction_name = None

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
        super(AzureRMPredictionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.prediction_name is not None):
            self.results['predictions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['predictions'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.predictions.get(resource_group_name=self.resource_group_name,
                                                        hub_name=self.hub_name,
                                                        prediction_name=self.prediction_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.predictions.list_by_hub(resource_group_name=self.resource_group_name,
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
    AzureRMPredictionInfo()


if __name__ == '__main__':
    main()
