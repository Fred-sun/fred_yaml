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
module: azure_rm_failovergroup
version_added: '2.9'
short_description: Manage Azure FailoverGroup instance.
description:
  - 'Create, update and delete instance of Azure FailoverGroup.'
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
    required: true
    type: str
  read_write_endpoint:
    description:
      - Read-write endpoint of the failover group instance.
    type: dict
    suboptions:
      failover_policy:
        description:
          - >-
            Failover policy of the read-write endpoint for the failover group.
            If failoverPolicy is Automatic then
            failoverWithDataLossGracePeriodMinutes is required.
        required: true
        type: str
        choices:
          - Manual
          - Automatic
      failover_with_data_loss_grace_period_minutes:
        description:
          - >-
            Grace period before failover with data loss is attempted for the
            read-write endpoint. If failoverPolicy is Automatic then
            failoverWithDataLossGracePeriodMinutes is required.
        type: integer
  partner_servers:
    description:
      - List of partner server information for the failover group.
    type: list
    suboptions:
      id:
        description:
          - Resource identifier of the partner server.
        required: true
        type: str
      location:
        description:
          - Geo location of the partner server.
        type: str
      replication_role:
        description:
          - Replication role of the partner server.
        type: str
        choices:
          - Primary
          - Secondary
  databases:
    description:
      - List of databases in the failover group.
    type: list
  failover_policy:
    description:
      - Failover policy of the read-only endpoint for the failover group.
    type: str
    choices:
      - Disabled
      - Enabled
  read_only_endpoint:
    description:
      - Read-only endpoint of the failover group instance.
    type: dict
    suboptions:
      failover_policy:
        description:
          - Failover policy of the read-only endpoint for the failover group.
        type: str
        choices:
          - Disabled
          - Enabled
  state:
    description:
      - Assert the state of the FailoverGroup.
      - >-
        Use C(present) to create or update an FailoverGroup and C(absent) to
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
    - name: Create failover group
      azure_rm_failovergroup: 
        failover_group_name: failover-group-test-3
        resource_group_name: Default
        server_name: failover-group-primary-server
        properties:
          databases:
            - >-
              /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/failover-group-primary-server/databases/testdb-1
            - >-
              /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/failover-group-primary-server/databases/testdb-2
          partner_servers:
            - id: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/failover-group-secondary-server
          read_only_endpoint:
            failover_policy: Disabled
          read_write_endpoint:
            failover_policy: Automatic
            failover_with_data_loss_grace_period_minutes: 480
        

    - name: Delete failover group
      azure_rm_failovergroup: 
        failover_group_name: failover-group-test-1
        resource_group_name: Default
        server_name: failover-group-primary-server
        

    - name: Update failover group
      azure_rm_failovergroup: 
        failover_group_name: failover-group-test-1
        resource_group_name: Default
        server_name: failover-group-primary-server
        properties:
          databases:
            - >-
              /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/failover-group-primary-server/databases/testdb-1
          read_write_endpoint:
            failover_policy: Automatic
            failover_with_data_loss_grace_period_minutes: 120
        

'''

RETURN = '''
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
          Failover policy of the read-write endpoint for the failover group. If
          failoverPolicy is Automatic then
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFailoverGroup(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            read_write_endpoint=dict(
                type='dict',
                disposition='/read_write_endpoint',
                options=dict(
                    failover_policy=dict(
                        type='str',
                        disposition='failover_policy',
                        choices=['Manual',
                                 'Automatic'],
                        required=True
                    ),
                    failover_with_data_loss_grace_period_minutes=dict(
                        type='integer',
                        disposition='failover_with_data_loss_grace_period_minutes'
                    )
                )
            ),
            partner_servers=dict(
                type='list',
                disposition='/partner_servers',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id',
                        required=True
                    ),
                    location=dict(
                        type='str',
                        updatable=False,
                        disposition='location'
                    ),
                    replication_role=dict(
                        type='str',
                        updatable=False,
                        disposition='replication_role',
                        choices=['Primary',
                                 'Secondary']
                    )
                )
            ),
            databases=dict(
                type='list',
                disposition='/databases',
                elements='str'
            ),
            failover_policy=dict(
                type='str',
                disposition='/failover_policy',
                choices=['Disabled',
                         'Enabled']
            ),
            read_only_endpoint=dict(
                type='dict',
                disposition='/read_only_endpoint',
                options=dict(
                    failover_policy=dict(
                        type='str',
                        disposition='failover_policy',
                        choices=['Disabled',
                                 'Enabled']
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.failover_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFailoverGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

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
            response = self.mgmt_client.failover_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         failover_group_name=self.failover_group_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FailoverGroup instance.')
            self.fail('Error creating the FailoverGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.failover_groups.delete(resource_group_name=self.resource_group_name,
                                                               server_name=self.server_name,
                                                               failover_group_name=self.failover_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the FailoverGroup instance.')
            self.fail('Error deleting the FailoverGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.failover_groups.get(resource_group_name=self.resource_group_name,
                                                            server_name=self.server_name,
                                                            failover_group_name=self.failover_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFailoverGroup()


if __name__ == '__main__':
    main()
