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
module: azure_rm_prediction
version_added: '2.9'
short_description: Manage Azure Prediction instance.
description:
  - 'Create, update and delete instance of Azure Prediction.'
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
    required: true
    type: str
  description:
    description:
      - Description of the prediction.
    type: dictionary
  display_name:
    description:
      - Display name of the prediction.
    type: dictionary
  involved_interaction_types:
    description:
      - Interaction types involved in the prediction.
    type: list
  involved_kpi_types:
    description:
      - KPI types involved in the prediction.
    type: list
  involved_relationships:
    description:
      - Relationships involved in the prediction.
    type: list
  negative_outcome_expression:
    description:
      - Negative outcome expression.
    type: str
  positive_outcome_expression:
    description:
      - Positive outcome expression.
    type: str
  primary_profile_type:
    description:
      - Primary profile type.
    type: str
  prediction_name1:
    description:
      - Name of the prediction.
    type: str
  scope_expression:
    description:
      - Scope expression.
    type: str
  auto_analyze:
    description:
      - Whether do auto analyze.
    type: bool
  mappings:
    description:
      - Definition of the link mapping of prediction.
    type: dict
    suboptions:
      score:
        description:
          - The score of the link mapping.
        required: true
        type: str
      grade:
        description:
          - The grade of the link mapping.
        required: true
        type: str
      reason:
        description:
          - The reason of the link mapping.
        required: true
        type: str
  score_label:
    description:
      - Score label.
    type: str
  grades:
    description:
      - The prediction grades.
    type: list
    suboptions:
      grade_name:
        description:
          - Name of the grade.
        type: str
      min_score_threshold:
        description:
          - Minimum score threshold.
        type: integer
      max_score_threshold:
        description:
          - Maximum score threshold.
        type: integer
  state:
    description:
      - Assert the state of the Prediction.
      - >-
        Use C(present) to create or update an Prediction and C(absent) to delete
        it.
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
    - name: Predictions_CreateOrUpdate
      azure_rm_prediction: 
        hub_name: sdkTestHub
        prediction_name: sdktest
        resource_group_name: TestHubRG
        properties:
          description:
            en-us: sdktest
          auto_analyze: true
          display_name:
            en-us: sdktest
          grades: []
          involved_interaction_types: []
          involved_kpi_types: []
          involved_relationships: []
          mappings:
            grade: sdktest_Grade
            reason: sdktest_Reason
            score: sdktest_Score
          negative_outcome_expression: Customers.FirstName = 'Mike'
          positive_outcome_expression: Customers.FirstName = 'David'
          prediction_name: sdktest
          primary_profile_type: Customers
          scope_expression: '*'
          score_label: score label
        

    - name: Predictions_Delete
      azure_rm_prediction: 
        hub_name: sdkTestHub
        prediction_name: sdktest
        resource_group_name: TestHubRG
        

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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPrediction(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            description=dict(
                type='dictionary',
                disposition='/description'
            ),
            display_name=dict(
                type='dictionary',
                disposition='/display_name'
            ),
            involved_interaction_types=dict(
                type='list',
                disposition='/involved_interaction_types',
                elements='str'
            ),
            involved_kpi_types=dict(
                type='list',
                disposition='/involved_kpi_types',
                elements='str'
            ),
            involved_relationships=dict(
                type='list',
                disposition='/involved_relationships',
                elements='str'
            ),
            negative_outcome_expression=dict(
                type='str',
                disposition='/negative_outcome_expression'
            ),
            positive_outcome_expression=dict(
                type='str',
                disposition='/positive_outcome_expression'
            ),
            primary_profile_type=dict(
                type='str',
                disposition='/primary_profile_type'
            ),
            prediction_name1=dict(
                type='str',
                disposition='/prediction_name1'
            ),
            scope_expression=dict(
                type='str',
                disposition='/scope_expression'
            ),
            auto_analyze=dict(
                type='bool',
                disposition='/auto_analyze'
            ),
            mappings=dict(
                type='dict',
                disposition='/mappings',
                options=dict(
                    score=dict(
                        type='str',
                        disposition='score',
                        required=True
                    ),
                    grade=dict(
                        type='str',
                        disposition='grade',
                        required=True
                    ),
                    reason=dict(
                        type='str',
                        disposition='reason',
                        required=True
                    )
                )
            ),
            score_label=dict(
                type='str',
                disposition='/score_label'
            ),
            grades=dict(
                type='list',
                disposition='/grades',
                elements='dict',
                options=dict(
                    grade_name=dict(
                        type='str',
                        disposition='grade_name'
                    ),
                    min_score_threshold=dict(
                        type='integer',
                        disposition='min_score_threshold'
                    ),
                    max_score_threshold=dict(
                        type='integer',
                        disposition='max_score_threshold'
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
        self.hub_name = None
        self.prediction_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPrediction, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

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
            response = self.mgmt_client.predictions.create_or_update(resource_group_name=self.resource_group_name,
                                                                     hub_name=self.hub_name,
                                                                     prediction_name=self.prediction_name,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Prediction instance.')
            self.fail('Error creating the Prediction instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.predictions.delete(resource_group_name=self.resource_group_name,
                                                           hub_name=self.hub_name,
                                                           prediction_name=self.prediction_name)
        except CloudError as e:
            self.log('Error attempting to delete the Prediction instance.')
            self.fail('Error deleting the Prediction instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.predictions.get(resource_group_name=self.resource_group_name,
                                                        hub_name=self.hub_name,
                                                        prediction_name=self.prediction_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPrediction()


if __name__ == '__main__':
    main()
