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
module: azure_rm_configurationprofilepreference_info
version_added: '2.9'
short_description: Get ConfigurationProfilePreference info.
description:
  - Get info of ConfigurationProfilePreference.
options:
  configuration_profile_preference_name:
    description:
      - The configuration profile preference name.
    type: str
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a configuration profile
      azure_rm_configurationprofilepreference_info: 
        configuration_profile_preference_name: defaultProfilePreference
        resource_group_name: myResourceGroupName
        

    - name: List configuration profile preferences by resource group
      azure_rm_configurationprofilepreference_info: 
        resource_group_name: myResourceGroupName
        

    - name: List configuration profile preferences by subscription
      azure_rm_configurationprofilepreference_info: 
        {}
        

'''

RETURN = '''
configuration_profile_preferences:
  description: >-
    A list of dict results where the key is the name of the
    ConfigurationProfilePreference and the values are the facts for that
    ConfigurationProfilePreference.
  returned: always
  type: complex
  contains:
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Properties of the configuration profile preference.
      returned: always
      type: dict
      sample: null
      contains:
        vm_backup:
          description:
            - The custom preferences for Azure VM Backup.
          returned: always
          type: dict
          sample: null
          contains:
            time_zone:
              description:
                - >-
                  TimeZone optional input as string. For example: Pacific
                  Standard Time
              returned: always
              type: str
              sample: null
            instant_rpretention_range_in_days:
              description:
                - Instant RP retention policy range in days
              returned: always
              type: integer
              sample: null
            retention_policy:
              description:
                - >-
                  Retention policy with the details on backup copy retention
                  ranges.
              returned: always
              type: str
              sample: null
            schedule_policy:
              description:
                - Backup schedule specified as part of backup policy.
              returned: always
              type: str
              sample: null
        enable_real_time_protection:
          description:
            - Enables or disables Real Time Protection
          returned: always
          type: str
          sample: null
        exclusions:
          description:
            - 'Extensions, Paths and Processes that must be excluded from scan'
          returned: always
          type: any
          sample: null
        run_scheduled_scan:
          description:
            - Enables or disables a periodic scan for antimalware
          returned: always
          type: str
          sample: null
        scan_type:
          description:
            - Type of scheduled scan
          returned: always
          type: str
          sample: null
        scan_day:
          description:
            - Schedule scan settings day
          returned: always
          type: str
          sample: null
        scan_time_in_minutes:
          description:
            - Schedule scan settings time
          returned: always
          type: str
          sample: null
    value:
      description:
        - Result of the list ConfigurationProfilePreference operation.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - Properties of the configuration profile preference.
          returned: always
          type: dict
          sample: null
          contains:
            vm_backup:
              description:
                - The custom preferences for Azure VM Backup.
              returned: always
              type: dict
              sample: null
              contains:
                time_zone:
                  description:
                    - >-
                      TimeZone optional input as string. For example: Pacific
                      Standard Time
                  returned: always
                  type: str
                  sample: null
                instant_rpretention_range_in_days:
                  description:
                    - Instant RP retention policy range in days
                  returned: always
                  type: integer
                  sample: null
                retention_policy:
                  description:
                    - >-
                      Retention policy with the details on backup copy retention
                      ranges.
                  returned: always
                  type: str
                  sample: null
                schedule_policy:
                  description:
                    - Backup schedule specified as part of backup policy.
                  returned: always
                  type: str
                  sample: null
            enable_real_time_protection:
              description:
                - Enables or disables Real Time Protection
              returned: always
              type: str
              sample: null
            exclusions:
              description:
                - >-
                  Extensions, Paths and Processes that must be excluded from
                  scan
              returned: always
              type: any
              sample: null
            run_scheduled_scan:
              description:
                - Enables or disables a periodic scan for antimalware
              returned: always
              type: str
              sample: null
            scan_type:
              description:
                - Type of scheduled scan
              returned: always
              type: str
              sample: null
            scan_day:
              description:
                - Schedule scan settings day
              returned: always
              type: str
              sample: null
            scan_time_in_minutes:
              description:
                - Schedule scan settings time
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
    from azure.mgmt.automanage import AutomanageClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConfigurationProfilePreferenceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            configuration_profile_preference_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            )
        )

        self.configuration_profile_preference_name = None
        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-30-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMConfigurationProfilePreferenceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AutomanageClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-30-preview')

        if (self.configuration_profile_preference_name is not None and
            self.resource_group_name is not None):
            self.results['configuration_profile_preferences'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['configuration_profile_preferences'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['configuration_profile_preferences'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.configuration_profile_preferences.get(configuration_profile_preference_name=self.configuration_profile_preference_name,
                                                                              resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.configuration_profile_preferences.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.configuration_profile_preferences.list_by_subscription()
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
    AzureRMConfigurationProfilePreferenceInfo()


if __name__ == '__main__':
    main()
