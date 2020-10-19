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
module: azure_rm_bandwidthsetting
version_added: '2.9'
short_description: Manage Azure BandwidthSetting instance.
description:
  - 'Create, update and delete instance of Azure BandwidthSetting.'
options:
  bandwidth_setting_name:
    description:
      - The name of bandwidth setting to be fetched.
      - The bandwidth setting name.
      - The name of the bandwidth setting.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  kind:
    description:
      - The Kind of the object. Currently only Series8000 is supported
    type: constant
  schedules:
    description:
      - The schedules.
    type: list
    suboptions:
      start:
        description:
          - The start time of the schedule.
        required: true
        type: dict
        suboptions:
          hours:
            description:
              - The hour.
            required: true
            type: integer
          minutes:
            description:
              - The minute.
            required: true
            type: integer
          seconds:
            description:
              - The second.
            required: true
            type: integer
      stop:
        description:
          - The stop time of the schedule.
        required: true
        type: dict
        suboptions:
          hours:
            description:
              - The hour.
            required: true
            type: integer
          minutes:
            description:
              - The minute.
            required: true
            type: integer
          seconds:
            description:
              - The second.
            required: true
            type: integer
      rate_in_mbps:
        description:
          - The rate in Mbps.
        required: true
        type: integer
      days:
        description:
          - The days of the week when this schedule is applicable.
        required: true
        type: list
  state:
    description:
      - Assert the state of the BandwidthSetting.
      - >-
        Use C(present) to create or update an BandwidthSetting and C(absent) to
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
    - name: BandwidthSettingsCreateOrUpdate
      azure_rm_bandwidthsetting: 
        bandwidth_setting_name: BWSForTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        properties:
          schedules:
            - days:
                - Saturday
                - Sunday
              rate_in_mbps: 10
              start:
                hours: 10
                minutes: 0
                seconds: 0
              stop:
                hours: 20
                minutes: 0
                seconds: 0
        

    - name: BandwidthSettingsDelete
      azure_rm_bandwidthsetting: 
        bandwidth_setting_name: BWSForTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the object.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
kind:
  description:
    - The Kind of the object. Currently only Series8000 is supported
  returned: always
  type: constant
  sample: null
schedules:
  description:
    - The schedules.
  returned: always
  type: list
  sample: null
  contains:
    start:
      description:
        - The start time of the schedule.
      returned: always
      type: dict
      sample: null
      contains:
        hours:
          description:
            - The hour.
          returned: always
          type: integer
          sample: null
        minutes:
          description:
            - The minute.
          returned: always
          type: integer
          sample: null
        seconds:
          description:
            - The second.
          returned: always
          type: integer
          sample: null
    stop:
      description:
        - The stop time of the schedule.
      returned: always
      type: dict
      sample: null
      contains:
        hours:
          description:
            - The hour.
          returned: always
          type: integer
          sample: null
        minutes:
          description:
            - The minute.
          returned: always
          type: integer
          sample: null
        seconds:
          description:
            - The second.
          returned: always
          type: integer
          sample: null
    rate_in_mbps:
      description:
        - The rate in Mbps.
      returned: always
      type: integer
      sample: null
    days:
      description:
        - The days of the week when this schedule is applicable.
      returned: always
      type: list
      sample: null
volume_count:
  description:
    - The number of volumes that uses the bandwidth setting.
  returned: always
  type: integer
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBandwidthSetting(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            bandwidth_setting_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='constant',
                disposition='/kind'
            ),
            schedules=dict(
                type='list',
                disposition='/schedules',
                elements='dict',
                options=dict(
                    start=dict(
                        type='dict',
                        disposition='start',
                        required=True,
                        options=dict(
                            hours=dict(
                                type='integer',
                                disposition='hours',
                                required=True
                            ),
                            minutes=dict(
                                type='integer',
                                disposition='minutes',
                                required=True
                            ),
                            seconds=dict(
                                type='integer',
                                disposition='seconds',
                                required=True
                            )
                        )
                    ),
                    stop=dict(
                        type='dict',
                        disposition='stop',
                        required=True,
                        options=dict(
                            hours=dict(
                                type='integer',
                                disposition='hours',
                                required=True
                            ),
                            minutes=dict(
                                type='integer',
                                disposition='minutes',
                                required=True
                            ),
                            seconds=dict(
                                type='integer',
                                disposition='seconds',
                                required=True
                            )
                        )
                    ),
                    rate_in_mbps=dict(
                        type='integer',
                        disposition='rate_in_mbps',
                        required=True
                    ),
                    days=dict(
                        type='list',
                        disposition='days',
                        required=True,
                        elements='sealed-choice'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.bandwidth_setting_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBandwidthSetting, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
            response = self.mgmt_client.bandwidth_settings.create_or_update(bandwidth_setting_name=self.bandwidth_setting_name,
                                                                            resource_group_name=self.resource_group_name,
                                                                            manager_name=self.manager_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BandwidthSetting instance.')
            self.fail('Error creating the BandwidthSetting instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.bandwidth_settings.delete(bandwidth_setting_name=self.bandwidth_setting_name,
                                                                  resource_group_name=self.resource_group_name,
                                                                  manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the BandwidthSetting instance.')
            self.fail('Error deleting the BandwidthSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.bandwidth_settings.get(bandwidth_setting_name=self.bandwidth_setting_name,
                                                               resource_group_name=self.resource_group_name,
                                                               manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBandwidthSetting()


if __name__ == '__main__':
    main()
