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
module: azure_rm_bandwidthschedule
version_added: '2.9'
short_description: Manage Azure BandwidthSchedule instance.
description:
  - 'Create, update and delete instance of Azure BandwidthSchedule.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  name:
    description:
      - The bandwidth schedule name.
      - The bandwidth schedule name which needs to be added/updated.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  start:
    description:
      - The start time of the schedule in UTC.
    type: str
  stop:
    description:
      - The stop time of the schedule in UTC.
    type: str
  rate_in_mbps:
    description:
      - The bandwidth rate in Mbps.
    type: integer
  days:
    description:
      - The days of the week when this schedule is applicable.
    type: list
  state:
    description:
      - Assert the state of the BandwidthSchedule.
      - >-
        Use C(present) to create or update an BandwidthSchedule and C(absent) to
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
    - name: BandwidthSchedulePut
      azure_rm_bandwidthschedule: 
        name: bandwidth-1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        properties:
          days:
            - Sunday
            - Monday
          rate_in_mbps: 100
          start: '0:0:0'
          stop: '13:59:0'
        

    - name: BandwidthScheduleDelete
      azure_rm_bandwidthschedule: 
        name: bandwidth-1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

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
    - The object name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
start:
  description:
    - The start time of the schedule in UTC.
  returned: always
  type: str
  sample: null
stop:
  description:
    - The stop time of the schedule in UTC.
  returned: always
  type: str
  sample: null
rate_in_mbps:
  description:
    - The bandwidth rate in Mbps.
  returned: always
  type: integer
  sample: null
days:
  description:
    - The days of the week when this schedule is applicable.
  returned: always
  type: list
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBandwidthSchedule(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            start=dict(
                type='str',
                disposition='/start'
            ),
            stop=dict(
                type='str',
                disposition='/stop'
            ),
            rate_in_mbps=dict(
                type='integer',
                disposition='/rate_in_mbps'
            ),
            days=dict(
                type='list',
                disposition='/days',
                elements='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBandwidthSchedule, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

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
            response = self.mgmt_client.bandwidth_schedules.create_or_update(device_name=self.device_name,
                                                                             name=self.name,
                                                                             resource_group_name=self.resource_group_name,
                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BandwidthSchedule instance.')
            self.fail('Error creating the BandwidthSchedule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.bandwidth_schedules.delete(device_name=self.device_name,
                                                                   name=self.name,
                                                                   resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the BandwidthSchedule instance.')
            self.fail('Error deleting the BandwidthSchedule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.bandwidth_schedules.get(device_name=self.device_name,
                                                                name=self.name,
                                                                resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBandwidthSchedule()


if __name__ == '__main__':
    main()
