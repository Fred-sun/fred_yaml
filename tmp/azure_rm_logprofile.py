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
module: azure_rm_logprofile
version_added: '2.9'
short_description: Manage Azure LogProfile instance.
description:
  - 'Create, update and delete instance of Azure LogProfile.'
options:
  log_profile_name:
    description:
      - The name of the log profile.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  storage_account_id:
    description:
      - >-
        the resource id of the storage account to which you would like to send
        the Activity Log.
    type: str
  service_bus_rule_id:
    description:
      - >-
        The service bus rule ID of the service bus namespace in which you would
        like to have Event Hubs created for streaming the Activity Log. The rule
        ID is of the format: '{service bus resource ID}/authorizationrules/{key
        name}'.
    type: str
  locations:
    description:
      - >-
        List of regions for which Activity Log events should be stored or
        streamed. It is a comma separated list of valid ARM locations including
        the 'global' location.
    type: list
  categories:
    description:
      - >-
        the categories of the logs. These categories are created as is
        convenient to the user. Some values are: 'Write', 'Delete', and/or
        'Action.'
    type: list
  retention_policy:
    description:
      - the retention policy for the events in the log.
    type: dict
    suboptions:
      enabled:
        description:
          - a value indicating whether the retention policy is enabled.
        required: true
        type: bool
      days:
        description:
          - >-
            the number of days for the retention in days. A value of 0 will
            retain the events indefinitely.
        required: true
        type: integer
  state:
    description:
      - Assert the state of the LogProfile.
      - >-
        Use C(present) to create or update an LogProfile and C(absent) to delete
        it.
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
    - name: Delete log profile
      azure_rm_logprofile: 
        log_profile_name: Rac46PostSwapRG
        

    - name: Create or update a log profile
      azure_rm_logprofile: 
        log_profile_name: Rac46PostSwapRG
        location: ''
        properties:
          categories:
            - Write
            - Delete
            - Action
          locations:
            - global
          retention_policy:
            days: 3
            enabled: true
          service_bus_rule_id: ''
          storage_account_id: >-
            /subscriptions/df602c9c-7aa0-407d-a6fb-eb20c8bd1192/resourceGroups/JohnKemTest/providers/Microsoft.Storage/storageAccounts/johnkemtest8162
        tags: {}
        

    - name: Patch a log profile
      azure_rm_logprofile: 
        log_profile_name: Rac46PostSwapRG
        

'''

RETURN = '''
id:
  description:
    - Azure resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Azure resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Azure resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
storage_account_id:
  description:
    - >-
      the resource id of the storage account to which you would like to send the
      Activity Log.
  returned: always
  type: str
  sample: null
service_bus_rule_id:
  description:
    - >-
      The service bus rule ID of the service bus namespace in which you would
      like to have Event Hubs created for streaming the Activity Log. The rule
      ID is of the format: '{service bus resource ID}/authorizationrules/{key
      name}'.
  returned: always
  type: str
  sample: null
locations:
  description:
    - >-
      List of regions for which Activity Log events should be stored or
      streamed. It is a comma separated list of valid ARM locations including
      the 'global' location.
  returned: always
  type: list
  sample: null
categories:
  description:
    - >-
      the categories of the logs. These categories are created as is convenient
      to the user. Some values are: 'Write', 'Delete', and/or 'Action.'
  returned: always
  type: list
  sample: null
retention_policy:
  description:
    - the retention policy for the events in the log.
  returned: always
  type: dict
  sample: null
  contains:
    enabled:
      description:
        - a value indicating whether the retention policy is enabled.
      returned: always
      type: bool
      sample: null
    days:
      description:
        - >-
          the number of days for the retention in days. A value of 0 will retain
          the events indefinitely.
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
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLogProfile(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            log_profile_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            storage_account_id=dict(
                type='str',
                disposition='/storage_account_id'
            ),
            service_bus_rule_id=dict(
                type='str',
                disposition='/service_bus_rule_id'
            ),
            locations=dict(
                type='list',
                disposition='/locations',
                elements='str'
            ),
            categories=dict(
                type='list',
                disposition='/categories',
                elements='str'
            ),
            retention_policy=dict(
                type='dict',
                disposition='/retention_policy',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='enabled',
                        required=True
                    ),
                    days=dict(
                        type='integer',
                        disposition='days',
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.log_profile_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLogProfile, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2016-03-01')

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
            response = self.mgmt_client.log_profiles.create_or_update(log_profile_name=self.log_profile_name,
                                                                      parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LogProfile instance.')
            self.fail('Error creating the LogProfile instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.log_profiles.delete(log_profile_name=self.log_profile_name)
        except CloudError as e:
            self.log('Error attempting to delete the LogProfile instance.')
            self.fail('Error deleting the LogProfile instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.log_profiles.get(log_profile_name=self.log_profile_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLogProfile()


if __name__ == '__main__':
    main()
