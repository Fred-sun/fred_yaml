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
module: azure_rm_metricbaseline
version_added: '2.9'
short_description: Manage Azure MetricBaseline instance.
description:
  - 'Create, update and delete instance of Azure MetricBaseline.'
options:
  resource_uri:
    description:
      - >-
        The identifier of the resource. It has the following structure:
        subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}.
        For example:
        subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
    required: true
    type: str
  metric_name:
    description:
      - The name of the metric to retrieve the baseline for.
    required: true
    type: str
  timespan:
    description:
      - >-
        The timespan of the query. It is a string with the following format
        'startDateTime_ISO/endDateTime_ISO'.
    required: true
    type: str
  interval:
    description:
      - The interval (i.e. timegrain) of the query.
    required: true
    type: duration
  aggregation:
    description:
      - The aggregation type of the metric to retrieve the baseline for.
    required: true
    type: str
  sensitivities:
    description:
      - The list of sensitivities (comma separated) to retrieve.
    required: true
    type: str
  result_type:
    description:
      - >-
        Allows retrieving only metadata of the baseline. On data request all
        information is retrieved.
    required: true
    type: sealed-choice
  state:
    description:
      - Assert the state of the MetricBaseline.
      - >-
        Use C(present) to create or update an MetricBaseline and C(absent) to
        delete it.
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
    - the metric baseline Id.
  returned: always
  type: str
  sample: null
type:
  description:
    - the resource type of the baseline resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - >-
      the name and the display name of the metric, i.e. it is localizable
      string.
  returned: always
  type: dict
  sample: null
  contains:
    value:
      description:
        - the invariant value.
      returned: always
      type: str
      sample: null
    localized_value:
      description:
        - the locale specific value.
      returned: always
      type: str
      sample: null
timespan:
  description:
    - >-
      The timespan for which the data was retrieved. Its value consists of two
      datetimes concatenated, separated by '/'.  This may be adjusted in the
      future and returned back from what was originally requested.
  returned: always
  type: str
  sample: null
interval:
  description:
    - >-
      The interval (window size) for which the metric data was returned in. 
      This may be adjusted in the future and returned back from what was
      originally requested.  This is not present if a metadata request was made.
  returned: always
  type: duration
  sample: null
aggregation:
  description:
    - The aggregation type of the metric.
  returned: always
  type: str
  sample: null
timestamps:
  description:
    - the array of timestamps of the baselines.
  returned: always
  type: list
  sample: null
baseline:
  description:
    - the baseline values for each sensitivity.
  returned: always
  type: list
  sample: null
  contains:
    sensitivity:
      description:
        - the sensitivity of the baseline.
      returned: always
      type: sealed-choice
      sample: null
    low_thresholds:
      description:
        - The low thresholds of the baseline.
      returned: always
      type: list
      sample: null
    high_thresholds:
      description:
        - The high thresholds of the baseline.
      returned: always
      type: list
      sample: null
metadata:
  description:
    - the baseline metadata values.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - the name of the metadata.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - the invariant value.
          returned: always
          type: str
          sample: null
        localized_value:
          description:
            - the locale specific value.
          returned: always
          type: str
          sample: null
    value:
      description:
        - the value of the metadata.
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
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMetricBaseline(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            metric_name=dict(
                type='str',
                required=True
            ),
            timespan=dict(
                type='str',
                required=True
            ),
            interval=dict(
                type='duration',
                required=True
            ),
            aggregation=dict(
                type='str',
                required=True
            ),
            sensitivities=dict(
                type='str',
                required=True
            ),
            result_type=dict(
                type='sealed-choice',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_uri = None
        self.metric_name = None
        self.timespan = None
        self.interval = None
        self.aggregation = None
        self.sensitivities = None
        self.result_type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMetricBaseline, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-11-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.metric_baseline.create()
            else:
                response = self.mgmt_client.metric_baseline.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MetricBaseline instance.')
            self.fail('Error creating the MetricBaseline instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.metric_baseline.delete()
        except CloudError as e:
            self.log('Error attempting to delete the MetricBaseline instance.')
            self.fail('Error deleting the MetricBaseline instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.metric_baseline.get(resource_uri=self.resource_uri,
                                                            metric_name=self.metric_name,
                                                            timespan=self.timespan,
                                                            interval=self.interval,
                                                            aggregation=self.aggregation,
                                                            sensitivities=self.sensitivities,
                                                            result_type=self.result_type)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMetricBaseline()


if __name__ == '__main__':
    main()
