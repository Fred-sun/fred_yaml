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
module: azure_rm_cost
version_added: '2.9'
short_description: Manage Azure Cost instance.
description:
  - 'Create, update and delete instance of Azure Cost.'
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
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  currency_code:
    description:
      - The currency code of the cost.
    type: str
  start_date_time:
    description:
      - The start time of the cost data.
    type: str
  end_date_time:
    description:
      - The end time of the cost data.
    type: str
  created_date:
    description:
      - The creation date of the cost.
    type: str
  status:
    description:
      - Target cost status
    type: str
    choices:
      - Enabled
      - Disabled
  target:
    description:
      - Lab target cost
    type: integer
  cost_thresholds:
    description:
      - Cost thresholds.
    type: list
    suboptions:
      threshold_id:
        description:
          - The ID of the cost threshold item.
        type: str
      percentage_threshold:
        description:
          - The value of the percentage cost threshold.
        type: dict
        suboptions:
          threshold_value:
            description:
              - The cost threshold value.
            type: number
      display_on_chart:
        description:
          - Indicates whether this threshold will be displayed on cost charts.
        type: str
        choices:
          - Enabled
          - Disabled
      send_notification_when_exceeded:
        description:
          - >-
            Indicates whether notifications will be sent when this threshold is
            exceeded.
        type: str
        choices:
          - Enabled
          - Disabled
      notification_sent:
        description:
          - >-
            Indicates the datetime when notifications were last sent for this
            threshold.
        type: str
  cycle_start_date_time:
    description:
      - Reporting cycle start date.
    type: str
  cycle_end_date_time:
    description:
      - Reporting cycle end date.
    type: str
  cycle_type:
    description:
      - Reporting cycle type.
    type: str
    choices:
      - CalendarMonth
      - Custom
  state:
    description:
      - Assert the state of the Cost.
      - Use C(present) to create or update an Cost and C(absent) to delete it.
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
'''

RETURN = '''
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
          Indicates whether notifications will be sent when this threshold is
          exceeded.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCost(AzureRMModuleBaseExt):
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
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            currency_code=dict(
                type='str',
                disposition='/currency_code'
            ),
            start_date_time=dict(
                type='str',
                disposition='/start_date_time'
            ),
            end_date_time=dict(
                type='str',
                disposition='/end_date_time'
            ),
            created_date=dict(
                type='str',
                disposition='/created_date'
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['Enabled',
                         'Disabled']
            ),
            target=dict(
                type='integer',
                disposition='/target'
            ),
            cost_thresholds=dict(
                type='list',
                disposition='/cost_thresholds',
                elements='dict',
                options=dict(
                    threshold_id=dict(
                        type='str',
                        disposition='threshold_id'
                    ),
                    percentage_threshold=dict(
                        type='dict',
                        disposition='percentage_threshold',
                        options=dict(
                            threshold_value=dict(
                                type='number',
                                disposition='threshold_value'
                            )
                        )
                    ),
                    display_on_chart=dict(
                        type='str',
                        disposition='display_on_chart',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    send_notification_when_exceeded=dict(
                        type='str',
                        disposition='send_notification_when_exceeded',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    notification_sent=dict(
                        type='str',
                        disposition='notification_sent'
                    )
                )
            ),
            cycle_start_date_time=dict(
                type='str',
                disposition='/cycle_start_date_time'
            ),
            cycle_end_date_time=dict(
                type='str',
                disposition='/cycle_end_date_time'
            ),
            cycle_type=dict(
                type='str',
                disposition='/cycle_type',
                choices=['CalendarMonth',
                         'Custom']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCost, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.costs.create_or_update(resource_group_name=self.resource_group_name,
                                                               lab_name=self.lab_name,
                                                               name=self.name,
                                                               lab_cost=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Cost instance.')
            self.fail('Error creating the Cost instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.costs.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Cost instance.')
            self.fail('Error deleting the Cost instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.costs.get(resource_group_name=self.resource_group_name,
                                                  lab_name=self.lab_name,
                                                  name=self.name,
                                                  expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCost()


if __name__ == '__main__':
    main()
