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
module: azure_rm_snapshotpolicy
version_added: '2.9'
short_description: Manage Azure SnapshotPolicy instance.
description:
  - 'Create, update and delete instance of Azure SnapshotPolicy.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the NetApp account
    required: true
    type: str
  snapshot_policy_name:
    description:
      - The name of the snapshot policy target
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  hourly_schedule:
    description:
      - Schedule for hourly snapshots
    type: dict
    suboptions:
      snapshots_to_keep:
        description:
          - Hourly snapshot count to keep
        type: integer
      minute:
        description:
          - Indicates which minute snapshot should be taken
        type: integer
      used_bytes:
        description:
          - >-
            Resource size in bytes, current storage usage for the volume in
            bytes
        type: integer
  daily_schedule:
    description:
      - Schedule for daily snapshots
    type: dict
    suboptions:
      snapshots_to_keep:
        description:
          - Daily snapshot count to keep
        type: integer
      hour:
        description:
          - Indicates which hour in UTC timezone a snapshot should be taken
        type: integer
      minute:
        description:
          - Indicates which minute snapshot should be taken
        type: integer
      used_bytes:
        description:
          - >-
            Resource size in bytes, current storage usage for the volume in
            bytes
        type: integer
  weekly_schedule:
    description:
      - Schedule for weekly snapshots
    type: dict
    suboptions:
      snapshots_to_keep:
        description:
          - Weekly snapshot count to keep
        type: integer
      day:
        description:
          - >-
            Indicates which weekdays snapshot should be taken, accepts a comma
            separated list of week day names in english
        type: str
      hour:
        description:
          - Indicates which hour in UTC timezone a snapshot should be taken
        type: integer
      minute:
        description:
          - Indicates which minute snapshot should be taken
        type: integer
      used_bytes:
        description:
          - >-
            Resource size in bytes, current storage usage for the volume in
            bytes
        type: integer
  monthly_schedule:
    description:
      - Schedule for monthly snapshots
    type: dict
    suboptions:
      snapshots_to_keep:
        description:
          - Monthly snapshot count to keep
        type: integer
      days_of_month:
        description:
          - >-
            Indicates which days of the month snapshot should be taken. A comma
            delimited string.
        type: str
      hour:
        description:
          - Indicates which hour in UTC timezone a snapshot should be taken
        type: integer
      minute:
        description:
          - Indicates which minute snapshot should be taken
        type: integer
      used_bytes:
        description:
          - >-
            Resource size in bytes, current storage usage for the volume in
            bytes
        type: integer
  enabled:
    description:
      - The property to decide policy is enabled or not
    type: bool
  state:
    description:
      - Assert the state of the SnapshotPolicy.
      - >-
        Use C(present) to create or update an SnapshotPolicy and C(absent) to
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
    - name: SnapshotPolicies_Create
      azure_rm_snapshotpolicy: 
        account_name: account1
        resource_group_name: myRG
        snapshot_policy_name: snapshotPolicyName
        location: eastus
        properties:
          daily_schedule:
            hour: 14
            minute: 30
            snapshots_to_keep: 4
          hourly_schedule:
            minute: 50
            snapshots_to_keep: 2
          monthly_schedule:
            days_of_month: '10,11,12'
            hour: 14
            minute: 15
            snapshots_to_keep: 5
          weekly_schedule:
            day: Wednesday
            hour: 14
            minute: 45
            snapshots_to_keep: 3
        

    - name: SnapshotPolicies_Update
      azure_rm_snapshotpolicy: 
        account_name: account1
        resource_group_name: myRG
        snapshot_policy_name: snapshotPolicyName
        location: eastus
        properties:
          daily_schedule:
            hour: 14
            minute: 30
            snapshots_to_keep: 4
          enabled: true
          hourly_schedule:
            minute: 50
            snapshots_to_keep: 2
          monthly_schedule:
            days_of_month: '10,11,12'
            hour: 14
            minute: 15
            snapshots_to_keep: 5
          weekly_schedule:
            day: Wednesday
            hour: 14
            minute: 45
            snapshots_to_keep: 3
        

    - name: SnapshotPolicies_Delete
      azure_rm_snapshotpolicy: 
        account_name: accountName
        resource_group_name: resourceGroup
        snapshot_policy_name: snapshotPolicyName
        

'''

RETURN = '''
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
name_properties_name:
  description:
    - Snapshot policy name
  returned: always
  type: str
  sample: null
hourly_schedule:
  description:
    - Schedule for hourly snapshots
  returned: always
  type: dict
  sample: null
  contains:
    snapshots_to_keep:
      description:
        - Hourly snapshot count to keep
      returned: always
      type: integer
      sample: null
    minute:
      description:
        - Indicates which minute snapshot should be taken
      returned: always
      type: integer
      sample: null
    used_bytes:
      description:
        - 'Resource size in bytes, current storage usage for the volume in bytes'
      returned: always
      type: integer
      sample: null
daily_schedule:
  description:
    - Schedule for daily snapshots
  returned: always
  type: dict
  sample: null
  contains:
    snapshots_to_keep:
      description:
        - Daily snapshot count to keep
      returned: always
      type: integer
      sample: null
    hour:
      description:
        - Indicates which hour in UTC timezone a snapshot should be taken
      returned: always
      type: integer
      sample: null
    minute:
      description:
        - Indicates which minute snapshot should be taken
      returned: always
      type: integer
      sample: null
    used_bytes:
      description:
        - 'Resource size in bytes, current storage usage for the volume in bytes'
      returned: always
      type: integer
      sample: null
weekly_schedule:
  description:
    - Schedule for weekly snapshots
  returned: always
  type: dict
  sample: null
  contains:
    snapshots_to_keep:
      description:
        - Weekly snapshot count to keep
      returned: always
      type: integer
      sample: null
    day:
      description:
        - >-
          Indicates which weekdays snapshot should be taken, accepts a comma
          separated list of week day names in english
      returned: always
      type: str
      sample: null
    hour:
      description:
        - Indicates which hour in UTC timezone a snapshot should be taken
      returned: always
      type: integer
      sample: null
    minute:
      description:
        - Indicates which minute snapshot should be taken
      returned: always
      type: integer
      sample: null
    used_bytes:
      description:
        - 'Resource size in bytes, current storage usage for the volume in bytes'
      returned: always
      type: integer
      sample: null
monthly_schedule:
  description:
    - Schedule for monthly snapshots
  returned: always
  type: dict
  sample: null
  contains:
    snapshots_to_keep:
      description:
        - Monthly snapshot count to keep
      returned: always
      type: integer
      sample: null
    days_of_month:
      description:
        - >-
          Indicates which days of the month snapshot should be taken. A comma
          delimited string.
      returned: always
      type: str
      sample: null
    hour:
      description:
        - Indicates which hour in UTC timezone a snapshot should be taken
      returned: always
      type: integer
      sample: null
    minute:
      description:
        - Indicates which minute snapshot should be taken
      returned: always
      type: integer
      sample: null
    used_bytes:
      description:
        - 'Resource size in bytes, current storage usage for the volume in bytes'
      returned: always
      type: integer
      sample: null
enabled:
  description:
    - The property to decide policy is enabled or not
  returned: always
  type: bool
  sample: null
provisioning_state:
  description:
    - Azure lifecycle management
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
    from azure.mgmt.net import NetAppManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSnapshotPolicy(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            snapshot_policy_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            hourly_schedule=dict(
                type='dict',
                disposition='/hourly_schedule',
                options=dict(
                    snapshots_to_keep=dict(
                        type='integer',
                        disposition='snapshots_to_keep'
                    ),
                    minute=dict(
                        type='integer',
                        disposition='minute'
                    ),
                    used_bytes=dict(
                        type='integer',
                        disposition='used_bytes'
                    )
                )
            ),
            daily_schedule=dict(
                type='dict',
                disposition='/daily_schedule',
                options=dict(
                    snapshots_to_keep=dict(
                        type='integer',
                        disposition='snapshots_to_keep'
                    ),
                    hour=dict(
                        type='integer',
                        disposition='hour'
                    ),
                    minute=dict(
                        type='integer',
                        disposition='minute'
                    ),
                    used_bytes=dict(
                        type='integer',
                        disposition='used_bytes'
                    )
                )
            ),
            weekly_schedule=dict(
                type='dict',
                disposition='/weekly_schedule',
                options=dict(
                    snapshots_to_keep=dict(
                        type='integer',
                        disposition='snapshots_to_keep'
                    ),
                    day=dict(
                        type='str',
                        disposition='day'
                    ),
                    hour=dict(
                        type='integer',
                        disposition='hour'
                    ),
                    minute=dict(
                        type='integer',
                        disposition='minute'
                    ),
                    used_bytes=dict(
                        type='integer',
                        disposition='used_bytes'
                    )
                )
            ),
            monthly_schedule=dict(
                type='dict',
                disposition='/monthly_schedule',
                options=dict(
                    snapshots_to_keep=dict(
                        type='integer',
                        disposition='snapshots_to_keep'
                    ),
                    days_of_month=dict(
                        type='str',
                        disposition='days_of_month'
                    ),
                    hour=dict(
                        type='integer',
                        disposition='hour'
                    ),
                    minute=dict(
                        type='integer',
                        disposition='minute'
                    ),
                    used_bytes=dict(
                        type='integer',
                        disposition='used_bytes'
                    )
                )
            ),
            enabled=dict(
                type='bool',
                disposition='/enabled'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.snapshot_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSnapshotPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(NetAppManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
                response = self.mgmt_client.snapshot_policies.create(resource_group_name=self.resource_group_name,
                                                                     account_name=self.account_name,
                                                                     snapshot_policy_name=self.snapshot_policy_name,
                                                                     body=self.body)
            else:
                response = self.mgmt_client.snapshot_policies.update(resource_group_name=self.resource_group_name,
                                                                     account_name=self.account_name,
                                                                     snapshot_policy_name=self.snapshot_policy_name,
                                                                     body=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SnapshotPolicy instance.')
            self.fail('Error creating the SnapshotPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.snapshot_policies.delete(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name,
                                                                 snapshot_policy_name=self.snapshot_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the SnapshotPolicy instance.')
            self.fail('Error deleting the SnapshotPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.snapshot_policies.get(resource_group_name=self.resource_group_name,
                                                              account_name=self.account_name,
                                                              snapshot_policy_name=self.snapshot_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSnapshotPolicy()


if __name__ == '__main__':
    main()
