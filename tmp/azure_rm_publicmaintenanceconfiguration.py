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
module: azure_rm_publicmaintenanceconfiguration
version_added: '2.9'
short_description: Manage Azure PublicMaintenanceConfiguration instance.
description:
  - 'Create, update and delete instance of Azure PublicMaintenanceConfiguration.'
options:
  resource_name:
    description:
      - Resource Identifier
    required: true
    type: str
  state:
    description:
      - Assert the state of the PublicMaintenanceConfiguration.
      - >-
        Use C(present) to create or update an PublicMaintenanceConfiguration and
        C(absent) to delete it.
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
    - Fully qualified identifier of the resource
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of the resource
  returned: always
  type: str
  sample: null
location:
  description:
    - Gets or sets location of the resource
  returned: always
  type: str
  sample: null
tags:
  description:
    - Gets or sets tags of the resource
  returned: always
  type: dictionary
  sample: null
namespace:
  description:
    - Gets or sets namespace of the resource
  returned: always
  type: str
  sample: null
extension_properties:
  description:
    - Gets or sets extensionProperties of the maintenanceConfiguration
  returned: always
  type: dictionary
  sample: null
maintenance_scope:
  description:
    - Gets or sets maintenanceScope of the configuration
  returned: always
  type: str
  sample: null
visibility:
  description:
    - Gets or sets the visibility of the configuration
  returned: always
  type: str
  sample: null
start_date_time:
  description:
    - >-
      Effective start date of the maintenance window in YYYY-MM-DD hh:mm format.
      The start date can be set to either the current date or future date. The
      window will be created in the time zone provided and adjusted to daylight
      savings according to that time zone.
  returned: always
  type: str
  sample: null
expiration_date_time:
  description:
    - >-
      Effective expiration date of the maintenance window in YYYY-MM-DD hh:mm
      format. The window will be created in the time zone provided and adjusted
      to daylight savings according to that time zone. Expiration date must be
      set to a future date. If not provided, it will be set to the maximum
      datetime 9999-12-31 23:59:59.
  returned: always
  type: str
  sample: null
duration:
  description:
    - >-
      Duration of the maintenance window in HH:mm format. If not provided,
      default value will be used based on maintenance scope provided. Example:
      05:00.
  returned: always
  type: str
  sample: null
time_zone:
  description:
    - >-
      Name of the timezone. List of timezones can be obtained by executing
      [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example:
      Pacific Standard Time, UTC, W. Europe Standard Time, Korea Standard Time,
      Cen. Australia Standard Time.
  returned: always
  type: str
  sample: null
recur_every:
  description:
    - >-
      Rate at which a Maintenance window is expected to recur. The rate can be
      expressed as daily, weekly, or monthly schedules. Daily schedule are
      formatted as recurEvery: [Frequency as integer]['Day(s)']. If no frequency
      is provided, the default frequency is 1. Daily schedule examples are
      recurEvery: Day, recurEvery: 3Days.  Weekly schedule are formatted as
      recurEvery: [Frequency as integer]['Week(s)'] [Optional comma separated
      list of weekdays Monday-Sunday]. Weekly schedule examples are recurEvery:
      3Weeks, recurEvery: Week Saturday,Sunday. Monthly schedules are formatted
      as [Frequency as integer]['Month(s)'] [Comma separated list of month days]
      or [Frequency as integer]['Month(s)'] [Week of Month (First, Second,
      Third, Fourth, Last)] [Weekday Monday-Sunday]. Monthly schedule examples
      are recurEvery: Month, recurEvery: 2Months, recurEvery: Month day23,day24,
      recurEvery: Month Last Sunday, recurEvery: Month Fourth Monday.
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
    from azure.mgmt.maintenance import MaintenanceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPublicMaintenanceConfiguration(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPublicMaintenanceConfiguration, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(MaintenanceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

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
                response = self.mgmt_client.public_maintenance_configurations.create()
            else:
                response = self.mgmt_client.public_maintenance_configurations.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PublicMaintenanceConfiguration instance.')
            self.fail('Error creating the PublicMaintenanceConfiguration instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.public_maintenance_configurations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the PublicMaintenanceConfiguration instance.')
            self.fail('Error deleting the PublicMaintenanceConfiguration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.public_maintenance_configurations.get(resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPublicMaintenanceConfiguration()


if __name__ == '__main__':
    main()
