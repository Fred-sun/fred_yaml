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
module: azure_rm_configurationprofilepreference
version_added: '2.9'
short_description: Manage Azure ConfigurationProfilePreference instance.
description:
  - 'Create, update and delete instance of Azure ConfigurationProfilePreference.'
options:
  configuration_profile_preference_name:
    description:
      - Name of the configuration profile preference.
      - The configuration profile preference name.
    required: true
    type: str
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  properties:
    description:
      - Properties of the configuration profile preference.
    type: dict
    suboptions:
      vm_backup:
        description:
          - The custom preferences for Azure VM Backup.
        type: dict
        suboptions:
          time_zone:
            description:
              - >-
                TimeZone optional input as string. For example: Pacific Standard
                Time
            type: str
          instant_rpretention_range_in_days:
            description:
              - Instant RP retention policy range in days
            type: integer
          retention_policy:
            description:
              - >-
                Retention policy with the details on backup copy retention
                ranges.
            type: str
          schedule_policy:
            description:
              - Backup schedule specified as part of backup policy.
            type: str
      enable_real_time_protection:
        description:
          - Enables or disables Real Time Protection
        type: str
        choices:
          - 'True'
          - 'False'
      exclusions:
        description:
          - 'Extensions, Paths and Processes that must be excluded from scan'
        type: any
      run_scheduled_scan:
        description:
          - Enables or disables a periodic scan for antimalware
        type: str
        choices:
          - 'True'
          - 'False'
      scan_type:
        description:
          - Type of scheduled scan
        type: str
        choices:
          - Quick
          - Full
      scan_day:
        description:
          - Schedule scan settings day
        type: str
      scan_time_in_minutes:
        description:
          - Schedule scan settings time
        type: str
  state:
    description:
      - Assert the state of the ConfigurationProfilePreference.
      - >-
        Use C(present) to create or update an ConfigurationProfilePreference and
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
    - name: Create or update configuration profile preference
      azure_rm_configurationprofilepreference: 
        configuration_profile_preference_name: defaultProfilePreference
        resource_group_name: myResourceGroupName
        location: East US
        properties:
          anti_malware:
            enable_real_time_protection: 'True'
          vm_backup:
            time_zone: Pacific Standard Time
        tags:
          organization: Administration
        

    - name: Delete a configuration profile preference
      azure_rm_configurationprofilepreference: 
        configuration_profile_preference_name: defaultProfilePreference
        resource_group_name: rg
        

'''

RETURN = '''
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
              TimeZone optional input as string. For example: Pacific Standard
              Time
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
            - Retention policy with the details on backup copy retention ranges.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.automanage import AutomanageClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConfigurationProfilePreference(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            configuration_profile_preference_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    vm_backup=dict(
                        type='dict',
                        disposition='vm_backup',
                        options=dict(
                            time_zone=dict(
                                type='str',
                                disposition='time_zone'
                            ),
                            instant_rpretention_range_in_days=dict(
                                type='integer',
                                disposition='instant_rpretention_range_in_days'
                            ),
                            retention_policy=dict(
                                type='str',
                                disposition='retention_policy'
                            ),
                            schedule_policy=dict(
                                type='str',
                                disposition='schedule_policy'
                            )
                        )
                    ),
                    enable_real_time_protection=dict(
                        type='str',
                        disposition='enable_real_time_protection',
                        choices=['True',
                                 'False']
                    ),
                    exclusions=dict(
                        type='any',
                        disposition='exclusions'
                    ),
                    run_scheduled_scan=dict(
                        type='str',
                        disposition='run_scheduled_scan',
                        choices=['True',
                                 'False']
                    ),
                    scan_type=dict(
                        type='str',
                        disposition='scan_type',
                        choices=['Quick',
                                 'Full']
                    ),
                    scan_day=dict(
                        type='str',
                        disposition='scan_day'
                    ),
                    scan_time_in_minutes=dict(
                        type='str',
                        disposition='scan_time_in_minutes'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.configuration_profile_preference_name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConfigurationProfilePreference, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AutomanageClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-30-preview')

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
            response = self.mgmt_client.configuration_profile_preferences.create_or_update(configuration_profile_preference_name=self.configuration_profile_preference_name,
                                                                                           resource_group_name=self.resource_group_name,
                                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ConfigurationProfilePreference instance.')
            self.fail('Error creating the ConfigurationProfilePreference instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.configuration_profile_preferences.delete(resource_group_name=self.resource_group_name,
                                                                                 configuration_profile_preference_name=self.configuration_profile_preference_name)
        except CloudError as e:
            self.log('Error attempting to delete the ConfigurationProfilePreference instance.')
            self.fail('Error deleting the ConfigurationProfilePreference instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.configuration_profile_preferences.get(configuration_profile_preference_name=self.configuration_profile_preference_name,
                                                                              resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMConfigurationProfilePreference()


if __name__ == '__main__':
    main()
