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
module: azure_rm_cost_info
version_added: '2.9'
short_description: Get Cost info.
description:
  - Get info of Cost.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  name:
    description:
      - The name of the cost.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($expand=labCostDetails)'''
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
costs:
  description: >-
    A list of dict results where the key is the name of the Cost and the values
    are the facts for that Cost.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The identifier of the resource.
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
    location:
      description:
        - The location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    lab_cost_summary:
      description:
        - The lab cost summary component of the cost data.
      returned: always
      type: dict
      sample: null
      contains:
        estimated_lab_cost:
          description:
            - The cost component of the cost item.
          returned: always
          type: number
          sample: null
    lab_cost_details:
      description:
        - The lab cost details component of the cost data.
      returned: always
      type: list
      sample: null
      contains:
        date:
          description:
            - The date of the cost item.
          returned: always
          type: str
          sample: null
        cost:
          description:
            - The cost component of the cost item.
          returned: always
          type: number
          sample: null
        cost_type:
          description:
            - The type of the cost.
          returned: always
          type: str
          sample: null
    resource_costs:
      description:
        - The resource cost component of the cost data.
      returned: always
      type: list
      sample: null
      contains:
        resourcename:
          description:
            - The name of the resource.
          returned: always
          type: str
          sample: null
        resource_uid:
          description:
            - The unique identifier of the resource.
          returned: always
          type: str
          sample: null
        resource_cost:
          description:
            - The cost component of the resource cost item.
          returned: always
          type: number
          sample: null
        resource_type:
          description:
            - 'The logical resource type (ex. virtualmachine, storageaccount)'
          returned: always
          type: str
          sample: null
        resource_owner:
          description:
            - The owner of the resource (ex. janedoe@microsoft.com)
          returned: always
          type: str
          sample: null
        resource_pricing_tier:
          description:
            - 'The category of the resource (ex. Premium_LRS, Standard_DS1)'
          returned: always
          type: str
          sample: null
        resource_status:
          description:
            - The status of the resource (ex. Active)
          returned: always
          type: str
          sample: null
        resource_id:
          description:
            - The ID of the resource
          returned: always
          type: str
          sample: null
        external_resource_id:
          description:
            - The ID of the external resource
          returned: always
          type: str
          sample: null
    currency_code:
      description:
        - The currency code of the cost.
      returned: always
      type: str
      sample: null
    start_date_time:
      description:
        - The start time of the cost data.
      returned: always
      type: str
      sample: null
    end_date_time:
      description:
        - The end time of the cost data.
      returned: always
      type: str
      sample: null
    created_date:
      description:
        - The creation date of the cost.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning status of the resource.
      returned: always
      type: str
      sample: null
    unique_identifier:
      description:
        - The unique immutable identifier of a resource (Guid).
      returned: always
      type: str
      sample: null
    status:
      description:
        - Target cost status
      returned: always
      type: str
      sample: null
    target:
      description:
        - Lab target cost
      returned: always
      type: integer
      sample: null
    cost_thresholds:
      description:
        - Cost thresholds.
      returned: always
      type: list
      sample: null
      contains:
        threshold_id:
          description:
            - The ID of the cost threshold item.
          returned: always
          type: str
          sample: null
        percentage_threshold:
          description:
            - The value of the percentage cost threshold.
          returned: always
          type: dict
          sample: null
          contains:
            threshold_value:
              description:
                - The cost threshold value.
              returned: always
              type: number
              sample: null
        display_on_chart:
          description:
            - Indicates whether this threshold will be displayed on cost charts.
          returned: always
          type: str
          sample: null
        send_notification_when_exceeded:
          description:
            - >-
              Indicates whether notifications will be sent when this threshold
              is exceeded.
          returned: always
          type: str
          sample: null
        notification_sent:
          description:
            - >-
              Indicates the datetime when notifications were last sent for this
              threshold.
          returned: always
          type: str
          sample: null
    cycle_start_date_time:
      description:
        - Reporting cycle start date.
      returned: always
      type: str
      sample: null
    cycle_end_date_time:
      description:
        - Reporting cycle end date.
      returned: always
      type: str
      sample: null
    cycle_type:
      description:
        - Reporting cycle type.
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCostInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCostInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

        if (self.resource_group_name is not None and
            self.lab_name is not None and
            self.name is not None):
            self.results['costs'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.costs.get(resource_group_name=self.resource_group_name,
                                                  lab_name=self.lab_name,
                                                  name=self.name,
                                                  expand=self.expand)
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
    AzureRMCostInfo()


if __name__ == '__main__':
    main()
