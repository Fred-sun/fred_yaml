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
module: azure_rm_failovergroup_info
version_added: '2.9'
short_description: Get FailoverGroup info.
description:
  - Get info of FailoverGroup.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server containing the failover group.
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
      azure_rm_failovergroup_info: 
        failover_group_name: failover-group-test
        resource_group_name: Default
        server_name: failover-group-primary-server
        

    - name: List failover group
      azure_rm_failovergroup_info: 
        resource_group_name: Default
        server_name: failover-group-primary-server
        

'''

RETURN = '''
failover_groups:
  description: >-
    A list of dict results where the key is the name of the FailoverGroup and
    the values are the facts for that FailoverGroup.
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
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
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
    partner_servers:
      description:
        - List of partner server information for the failover group.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource identifier of the partner server.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Geo location of the partner server.
          returned: always
          type: str
          sample: null
        replication_role:
          description:
            - Replication role of the partner server.
          returned: always
          type: str
          sample: null
    databases:
      description:
        - List of databases in the failover group.
      returned: always
      type: list
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
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags.
          returned: always
          type: dictionary
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
        partner_servers:
          description:
            - List of partner server information for the failover group.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource identifier of the partner server.
              returned: always
              type: str
              sample: null
            location:
              description:
                - Geo location of the partner server.
              returned: always
              type: str
              sample: null
            replication_role:
              description:
                - Replication role of the partner server.
              returned: always
              type: str
              sample: null
        databases:
          description:
            - List of databases in the failover group.
          returned: always
          type: list
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


class AzureRMFailoverGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            failover_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.failover_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMFailoverGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.failover_group_name is not None):
            self.results['failover_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['failover_groups'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.failover_groups.get(resource_group_name=self.resource_group_name,
                                                            server_name=self.server_name,
                                                            failover_group_name=self.failover_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.failover_groups.list_by_server(resource_group_name=self.resource_group_name,
                                                                       server_name=self.server_name)
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
    AzureRMFailoverGroupInfo()


if __name__ == '__main__':
    main()
