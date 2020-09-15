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
module: azure_rm_publicmaintenanceconfiguration_info
version_added: '2.9'
short_description: Get PublicMaintenanceConfiguration info.
description:
  - Get info of PublicMaintenanceConfiguration.
options:
  resource_name:
    description:
      - Resource Identifier
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: PublicMaintenanceConfigurations_List
      azure_rm_publicmaintenanceconfiguration_info: 
        {}
        

    - name: PublicMaintenanceConfigurations_GetForResource
      azure_rm_publicmaintenanceconfiguration_info: 
        resource_name: configuration1
        

'''

RETURN = '''
public_maintenance_configurations:
  description: >-
    A list of dict results where the key is the name of the
    PublicMaintenanceConfiguration and the values are the facts for that
    PublicMaintenanceConfiguration.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of maintenance Configurations
      returned: always
      type: list
      sample: null
      contains:
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
              Effective start date of the maintenance window in YYYY-MM-DD hh:mm
              format. The start date can be set to either the current date or
              future date. The window will be created in the time zone provided
              and adjusted to daylight savings according to that time zone.
          returned: always
          type: str
          sample: null
        expiration_date_time:
          description:
            - >-
              Effective expiration date of the maintenance window in YYYY-MM-DD
              hh:mm format. The window will be created in the time zone provided
              and adjusted to daylight savings according to that time zone.
              Expiration date must be set to a future date. If not provided, it
              will be set to the maximum datetime 9999-12-31 23:59:59.
          returned: always
          type: str
          sample: null
        duration:
          description:
            - >-
              Duration of the maintenance window in HH:mm format. If not
              provided, default value will be used based on maintenance scope
              provided. Example: 05:00.
          returned: always
          type: str
          sample: null
        time_zone:
          description:
            - >-
              Name of the timezone. List of timezones can be obtained by
              executing [System.TimeZoneInfo]::GetSystemTimeZones() in
              PowerShell. Example: Pacific Standard Time, UTC, W. Europe
              Standard Time, Korea Standard Time, Cen. Australia Standard Time.
          returned: always
          type: str
          sample: null
        recur_every:
          description:
            - >-
              Rate at which a Maintenance window is expected to recur. The rate
              can be expressed as daily, weekly, or monthly schedules. Daily
              schedule are formatted as recurEvery: [Frequency as
              integer]['Day(s)']. If no frequency is provided, the default
              frequency is 1. Daily schedule examples are recurEvery: Day,
              recurEvery: 3Days.  Weekly schedule are formatted as recurEvery:
              [Frequency as integer]['Week(s)'] [Optional comma separated list
              of weekdays Monday-Sunday]. Weekly schedule examples are
              recurEvery: 3Weeks, recurEvery: Week Saturday,Sunday. Monthly
              schedules are formatted as [Frequency as integer]['Month(s)']
              [Comma separated list of month days] or [Frequency as
              integer]['Month(s)'] [Week of Month (First, Second, Third, Fourth,
              Last)] [Weekday Monday-Sunday]. Monthly schedule examples are
              recurEvery: Month, recurEvery: 2Months, recurEvery: Month
              day23,day24, recurEvery: Month Last Sunday, recurEvery: Month
              Fourth Monday.
          returned: always
          type: str
          sample: null
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
          Effective start date of the maintenance window in YYYY-MM-DD hh:mm
          format. The start date can be set to either the current date or future
          date. The window will be created in the time zone provided and
          adjusted to daylight savings according to that time zone.
      returned: always
      type: str
      sample: null
    expiration_date_time:
      description:
        - >-
          Effective expiration date of the maintenance window in YYYY-MM-DD
          hh:mm format. The window will be created in the time zone provided and
          adjusted to daylight savings according to that time zone. Expiration
          date must be set to a future date. If not provided, it will be set to
          the maximum datetime 9999-12-31 23:59:59.
      returned: always
      type: str
      sample: null
    duration:
      description:
        - >-
          Duration of the maintenance window in HH:mm format. If not provided,
          default value will be used based on maintenance scope provided.
          Example: 05:00.
      returned: always
      type: str
      sample: null
    time_zone:
      description:
        - >-
          Name of the timezone. List of timezones can be obtained by executing
          [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example:
          Pacific Standard Time, UTC, W. Europe Standard Time, Korea Standard
          Time, Cen. Australia Standard Time.
      returned: always
      type: str
      sample: null
    recur_every:
      description:
        - >-
          Rate at which a Maintenance window is expected to recur. The rate can
          be expressed as daily, weekly, or monthly schedules. Daily schedule
          are formatted as recurEvery: [Frequency as integer]['Day(s)']. If no
          frequency is provided, the default frequency is 1. Daily schedule
          examples are recurEvery: Day, recurEvery: 3Days.  Weekly schedule are
          formatted as recurEvery: [Frequency as integer]['Week(s)'] [Optional
          comma separated list of weekdays Monday-Sunday]. Weekly schedule
          examples are recurEvery: 3Weeks, recurEvery: Week Saturday,Sunday.
          Monthly schedules are formatted as [Frequency as integer]['Month(s)']
          [Comma separated list of month days] or [Frequency as
          integer]['Month(s)'] [Week of Month (First, Second, Third, Fourth,
          Last)] [Weekday Monday-Sunday]. Monthly schedule examples are
          recurEvery: Month, recurEvery: 2Months, recurEvery: Month day23,day24,
          recurEvery: Month Last Sunday, recurEvery: Month Fourth Monday.
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
    from azure.mgmt.maintenance import MaintenanceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPublicMaintenanceConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str'
            )
        )

        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPublicMaintenanceConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MaintenanceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

        if (self.resource_name is not None):
            self.results['public_maintenance_configurations'] = self.format_item(self.get())
        else:
            self.results['public_maintenance_configurations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.public_maintenance_configurations.get(resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.public_maintenance_configurations.list()
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
    AzureRMPublicMaintenanceConfigurationInfo()


if __name__ == '__main__':
    main()
