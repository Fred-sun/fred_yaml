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
module: azure_rm_instancefailovergroup_info
version_added: '2.9'
short_description: Get InstanceFailoverGroup info.
description:
  - Get info of InstanceFailoverGroup.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  location_name:
    description:
      - The name of the region where the resource is located.
    required: true
    type: str
  failover_group_name:
    description:
      - The name of the failover group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get failover group
      azure_rm_instancefailovergroup_info: 
        failover_group_name: failover-group-test
        location_name: Japan East
        resource_group_name: Default
        

    - name: List failover group
      azure_rm_instancefailovergroup_info: 
        location_name: Japan East
        resource_group_name: Default
        

'''

RETURN = '''
instance_failover_groups:
  description: >-
    A list of dict results where the key is the name of the
    InstanceFailoverGroup and the values are the facts for that
    InstanceFailoverGroup.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    read_write_endpoint:
      description:
        - Read-write endpoint of the failover group instance.
      returned: always
      type: dict
      sample: null
      contains:
        failover_policy:
          description:
            - >-
              Failover policy of the read-write endpoint for the failover group.
              If failoverPolicy is Automatic then
              failoverWithDataLossGracePeriodMinutes is required.
          returned: always
          type: str
          sample: null
        failover_with_data_loss_grace_period_minutes:
          description:
            - >-
              Grace period before failover with data loss is attempted for the
              read-write endpoint. If failoverPolicy is Automatic then
              failoverWithDataLossGracePeriodMinutes is required.
          returned: always
          type: integer
          sample: null
    replication_role:
      description:
        - Local replication role of the failover group instance.
      returned: always
      type: str
      sample: null
    replication_state:
      description:
        - Replication state of the failover group instance.
      returned: always
      type: str
      sample: null
    partner_regions:
      description:
        - Partner region information for the failover group.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Geo location of the partner managed instances.
          returned: always
          type: str
          sample: null
        replication_role:
          description:
            - Replication role of the partner managed instances.
          returned: always
          type: str
          sample: null
    managed_instance_pairs:
      description:
        - List of managed instance pairs in the failover group.
      returned: always
      type: list
      sample: null
      contains:
        primary_managed_instance_id:
          description:
            - Id of Primary Managed Instance in pair.
          returned: always
          type: str
          sample: null
        partner_managed_instance_id:
          description:
            - Id of Partner Managed Instance in pair.
          returned: always
          type: str
          sample: null
    failover_policy:
      description:
        - Failover policy of the read-only endpoint for the failover group.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        read_write_endpoint:
          description:
            - Read-write endpoint of the failover group instance.
          returned: always
          type: dict
          sample: null
          contains:
            failover_policy:
              description:
                - >-
                  Failover policy of the read-write endpoint for the failover
                  group. If failoverPolicy is Automatic then
                  failoverWithDataLossGracePeriodMinutes is required.
              returned: always
              type: str
              sample: null
            failover_with_data_loss_grace_period_minutes:
              description:
                - >-
                  Grace period before failover with data loss is attempted for
                  the read-write endpoint. If failoverPolicy is Automatic then
                  failoverWithDataLossGracePeriodMinutes is required.
              returned: always
              type: integer
              sample: null
        replication_role:
          description:
            - Local replication role of the failover group instance.
          returned: always
          type: str
          sample: null
        replication_state:
          description:
            - Replication state of the failover group instance.
          returned: always
          type: str
          sample: null
        partner_regions:
          description:
            - Partner region information for the failover group.
          returned: always
          type: list
          sample: null
          contains:
            location:
              description:
                - Geo location of the partner managed instances.
              returned: always
              type: str
              sample: null
            replication_role:
              description:
                - Replication role of the partner managed instances.
              returned: always
              type: str
              sample: null
        managed_instance_pairs:
          description:
            - List of managed instance pairs in the failover group.
          returned: always
          type: list
          sample: null
          contains:
            primary_managed_instance_id:
              description:
                - Id of Primary Managed Instance in pair.
              returned: always
              type: str
              sample: null
            partner_managed_instance_id:
              description:
                - Id of Partner Managed Instance in pair.
              returned: always
              type: str
              sample: null
        failover_policy:
          description:
            - Failover policy of the read-only endpoint for the failover group.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMInstanceFailoverGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            location_name=dict(
                type='str',
                required=True
            ),
            failover_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.location_name = None
        self.failover_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-10-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMInstanceFailoverGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01-preview')

        if (self.resource_group_name is not None and
            self.location_name is not None and
            self.failover_group_name is not None):
            self.results['instance_failover_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.location_name is not None):
            self.results['instance_failover_groups'] = self.format_item(self.listbylocation())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.instance_failover_groups.get(resource_group_name=self.resource_group_name,
                                                                     location_name=self.location_name,
                                                                     failover_group_name=self.failover_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.instance_failover_groups.list_by_location(resource_group_name=self.resource_group_name,
                                                                                  location_name=self.location_name)
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
    AzureRMInstanceFailoverGroupInfo()


if __name__ == '__main__':
    main()
