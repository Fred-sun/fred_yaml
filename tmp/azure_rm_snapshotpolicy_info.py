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
module: azure_rm_snapshotpolicy_info
version_added: '2.9'
short_description: Get SnapshotPolicy info.
description:
  - Get info of SnapshotPolicy.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SnapshotPolicies_List
      azure_rm_snapshotpolicy_info: 
        account_name: account1
        resource_group_name: myRG
        

    - name: SnapshotPolicies_Get
      azure_rm_snapshotpolicy_info: 
        account_name: account1
        resource_group_name: myRG
        snapshot_policy_name: snapshotPolicyName
        

    - name: SnapshotPolicies_ListVolumes
      azure_rm_snapshotpolicy_info: 
        account_name: account1
        resource_group_name: myRG
        snapshot_policy_name: snapshotPolicyName
        

'''

RETURN = '''
snapshot_policies:
  description: >-
    A list of dict results where the key is the name of the SnapshotPolicy and
    the values are the facts for that SnapshotPolicy.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          A list of snapshot policies
          List of volumes
      returned: always
      type: list
      sample: null
      contains:
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
                - >-
                  Resource size in bytes, current storage usage for the volume
                  in bytes
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
                - >-
                  Indicates which hour in UTC timezone a snapshot should be
                  taken
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
                - >-
                  Resource size in bytes, current storage usage for the volume
                  in bytes
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
                  Indicates which weekdays snapshot should be taken, accepts a
                  comma separated list of week day names in english
              returned: always
              type: str
              sample: null
            hour:
              description:
                - >-
                  Indicates which hour in UTC timezone a snapshot should be
                  taken
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
                - >-
                  Resource size in bytes, current storage usage for the volume
                  in bytes
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
                  Indicates which days of the month snapshot should be taken. A
                  comma delimited string.
              returned: always
              type: str
              sample: null
            hour:
              description:
                - >-
                  Indicates which hour in UTC timezone a snapshot should be
                  taken
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
                - >-
                  Resource size in bytes, current storage usage for the volume
                  in bytes
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
            - >-
              Resource size in bytes, current storage usage for the volume in
              bytes
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
            - >-
              Resource size in bytes, current storage usage for the volume in
              bytes
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
            - >-
              Resource size in bytes, current storage usage for the volume in
              bytes
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
              Indicates which days of the month snapshot should be taken. A
              comma delimited string.
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
            - >-
              Resource size in bytes, current storage usage for the volume in
              bytes
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.net import NetAppManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSnapshotPolicyInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.snapshot_policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSnapshotPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetAppManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.snapshot_policy_name is not None):
            self.results['snapshot_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.snapshot_policy_name is not None):
            self.results['snapshot_policies'] = self.format_item(self.listvolume())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['snapshot_policies'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.snapshot_policies.get(resource_group_name=self.resource_group_name,
                                                              account_name=self.account_name,
                                                              snapshot_policy_name=self.snapshot_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listvolume(self):
        response = None

        try:
            response = self.mgmt_client.snapshot_policies.list_volume(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      snapshot_policy_name=self.snapshot_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.snapshot_policies.list(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name)
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
    AzureRMSnapshotPolicyInfo()


if __name__ == '__main__':
    main()
