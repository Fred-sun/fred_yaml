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
module: azure_rm_servicetieradvisor_info
version_added: '2.9'
short_description: Get ServiceTierAdvisor info.
description:
  - Get info of ServiceTierAdvisor.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - The name of database.
    required: true
    type: str
  service_tier_advisor_name:
    description:
      - The name of service tier advisor.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a service tier advisor
      azure_rm_servicetieradvisor_info: 
        database_name: sqlcrudtest-9187
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        service_tier_advisor_name: Current
        

    - name: Get a list of a service tier advisors
      azure_rm_servicetieradvisor_info: 
        database_name: sqlcrudtest-9187
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        

'''

RETURN = '''
service_tier_advisors:
  description: >-
    A list of dict results where the key is the name of the ServiceTierAdvisor
    and the values are the facts for that ServiceTierAdvisor.
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
    observation_period_start:
      description:
        - The observation period start (ISO8601 format).
      returned: always
      type: str
      sample: null
    observation_period_end:
      description:
        - The observation period start (ISO8601 format).
      returned: always
      type: str
      sample: null
    active_time_ratio:
      description:
        - The activeTimeRatio for service tier advisor.
      returned: always
      type: number
      sample: null
    min_dtu:
      description:
        - Gets or sets minDtu for service tier advisor.
      returned: always
      type: number
      sample: null
    avg_dtu:
      description:
        - Gets or sets avgDtu for service tier advisor.
      returned: always
      type: number
      sample: null
    max_dtu:
      description:
        - Gets or sets maxDtu for service tier advisor.
      returned: always
      type: number
      sample: null
    max_size_in_gb:
      description:
        - Gets or sets maxSizeInGB for service tier advisor.
      returned: always
      type: number
      sample: null
    service_level_objective_usage_metrics:
      description:
        - >-
          Gets or sets serviceLevelObjectiveUsageMetrics for the service tier
          advisor.
      returned: always
      type: list
      sample: null
      contains:
        service_level_objective:
          description:
            - The serviceLevelObjective for SLO usage metric.
          returned: always
          type: str
          sample: null
        service_level_objective_id:
          description:
            - The serviceLevelObjectiveId for SLO usage metric.
          returned: always
          type: uuid
          sample: null
        in_range_time_ratio:
          description:
            - Gets or sets inRangeTimeRatio for SLO usage metric.
          returned: always
          type: number
          sample: null
    current_service_level_objective:
      description:
        - Gets or sets currentServiceLevelObjective for service tier advisor.
      returned: always
      type: str
      sample: null
    current_service_level_objective_id:
      description:
        - Gets or sets currentServiceLevelObjectiveId for service tier advisor.
      returned: always
      type: uuid
      sample: null
    usage_based_recommendation_service_level_objective:
      description:
        - >-
          Gets or sets usageBasedRecommendationServiceLevelObjective for service
          tier advisor.
      returned: always
      type: str
      sample: null
    usage_based_recommendation_service_level_objective_id:
      description:
        - >-
          Gets or sets usageBasedRecommendationServiceLevelObjectiveId for
          service tier advisor.
      returned: always
      type: uuid
      sample: null
    database_size_based_recommendation_service_level_objective:
      description:
        - >-
          Gets or sets databaseSizeBasedRecommendationServiceLevelObjective for
          service tier advisor.
      returned: always
      type: str
      sample: null
    database_size_based_recommendation_service_level_objective_id:
      description:
        - >-
          Gets or sets databaseSizeBasedRecommendationServiceLevelObjectiveId
          for service tier advisor.
      returned: always
      type: uuid
      sample: null
    disaster_plan_based_recommendation_service_level_objective:
      description:
        - >-
          Gets or sets disasterPlanBasedRecommendationServiceLevelObjective for
          service tier advisor.
      returned: always
      type: str
      sample: null
    disaster_plan_based_recommendation_service_level_objective_id:
      description:
        - >-
          Gets or sets disasterPlanBasedRecommendationServiceLevelObjectiveId
          for service tier advisor.
      returned: always
      type: uuid
      sample: null
    overall_recommendation_service_level_objective:
      description:
        - >-
          Gets or sets overallRecommendationServiceLevelObjective for service
          tier advisor.
      returned: always
      type: str
      sample: null
    overall_recommendation_service_level_objective_id:
      description:
        - >-
          Gets or sets overallRecommendationServiceLevelObjectiveId for service
          tier advisor.
      returned: always
      type: uuid
      sample: null
    confidence:
      description:
        - Gets or sets confidence for service tier advisor.
      returned: always
      type: number
      sample: null
    value:
      description:
        - The list of service tier advisors for specified database.
      returned: always
      type: list
      sample: null
      contains:
        observation_period_start:
          description:
            - The observation period start (ISO8601 format).
          returned: always
          type: str
          sample: null
        observation_period_end:
          description:
            - The observation period start (ISO8601 format).
          returned: always
          type: str
          sample: null
        active_time_ratio:
          description:
            - The activeTimeRatio for service tier advisor.
          returned: always
          type: number
          sample: null
        min_dtu:
          description:
            - Gets or sets minDtu for service tier advisor.
          returned: always
          type: number
          sample: null
        avg_dtu:
          description:
            - Gets or sets avgDtu for service tier advisor.
          returned: always
          type: number
          sample: null
        max_dtu:
          description:
            - Gets or sets maxDtu for service tier advisor.
          returned: always
          type: number
          sample: null
        max_size_in_gb:
          description:
            - Gets or sets maxSizeInGB for service tier advisor.
          returned: always
          type: number
          sample: null
        service_level_objective_usage_metrics:
          description:
            - >-
              Gets or sets serviceLevelObjectiveUsageMetrics for the service
              tier advisor.
          returned: always
          type: list
          sample: null
          contains:
            service_level_objective:
              description:
                - The serviceLevelObjective for SLO usage metric.
              returned: always
              type: str
              sample: null
            service_level_objective_id:
              description:
                - The serviceLevelObjectiveId for SLO usage metric.
              returned: always
              type: uuid
              sample: null
            in_range_time_ratio:
              description:
                - Gets or sets inRangeTimeRatio for SLO usage metric.
              returned: always
              type: number
              sample: null
        current_service_level_objective:
          description:
            - >-
              Gets or sets currentServiceLevelObjective for service tier
              advisor.
          returned: always
          type: str
          sample: null
        current_service_level_objective_id:
          description:
            - >-
              Gets or sets currentServiceLevelObjectiveId for service tier
              advisor.
          returned: always
          type: uuid
          sample: null
        usage_based_recommendation_service_level_objective:
          description:
            - >-
              Gets or sets usageBasedRecommendationServiceLevelObjective for
              service tier advisor.
          returned: always
          type: str
          sample: null
        usage_based_recommendation_service_level_objective_id:
          description:
            - >-
              Gets or sets usageBasedRecommendationServiceLevelObjectiveId for
              service tier advisor.
          returned: always
          type: uuid
          sample: null
        database_size_based_recommendation_service_level_objective:
          description:
            - >-
              Gets or sets databaseSizeBasedRecommendationServiceLevelObjective
              for service tier advisor.
          returned: always
          type: str
          sample: null
        database_size_based_recommendation_service_level_objective_id:
          description:
            - >-
              Gets or sets
              databaseSizeBasedRecommendationServiceLevelObjectiveId for service
              tier advisor.
          returned: always
          type: uuid
          sample: null
        disaster_plan_based_recommendation_service_level_objective:
          description:
            - >-
              Gets or sets disasterPlanBasedRecommendationServiceLevelObjective
              for service tier advisor.
          returned: always
          type: str
          sample: null
        disaster_plan_based_recommendation_service_level_objective_id:
          description:
            - >-
              Gets or sets
              disasterPlanBasedRecommendationServiceLevelObjectiveId for service
              tier advisor.
          returned: always
          type: uuid
          sample: null
        overall_recommendation_service_level_objective:
          description:
            - >-
              Gets or sets overallRecommendationServiceLevelObjective for
              service tier advisor.
          returned: always
          type: str
          sample: null
        overall_recommendation_service_level_objective_id:
          description:
            - >-
              Gets or sets overallRecommendationServiceLevelObjectiveId for
              service tier advisor.
          returned: always
          type: uuid
          sample: null
        confidence:
          description:
            - Gets or sets confidence for service tier advisor.
          returned: always
          type: number
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMServiceTierAdvisorInfo(AzureRMModuleBase):
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
            database_name=dict(
                type='str',
                required=True
            ),
            service_tier_advisor_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.service_tier_advisor_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMServiceTierAdvisorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.service_tier_advisor_name is not None):
            self.results['service_tier_advisors'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['service_tier_advisors'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.service_tier_advisors.get(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  database_name=self.database_name,
                                                                  service_tier_advisor_name=self.service_tier_advisor_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.service_tier_advisors.list_by_database(resource_group_name=self.resource_group_name,
                                                                               server_name=self.server_name,
                                                                               database_name=self.database_name)
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
    AzureRMServiceTierAdvisorInfo()


if __name__ == '__main__':
    main()
