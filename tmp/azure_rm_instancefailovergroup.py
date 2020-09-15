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
module: azure_rm_instancefailovergroup
version_added: '2.9'
short_description: Manage Azure InstanceFailoverGroup instance.
description:
  - 'Create, update and delete instance of Azure InstanceFailoverGroup.'
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
  partner_regions:
    description:
      - Partner region information for the failover group.
    type: list
    suboptions:
      location:
        description:
          - Geo location of the partner managed instances.
        type: str
      replication_role:
        description:
          - Replication role of the partner managed instances.
        type: str
        choices:
          - Primary
          - Secondary
  managed_instance_pairs:
    description:
      - List of managed instance pairs in the failover group.
    type: list
    suboptions:
      primary_managed_instance_id:
        description:
          - Id of Primary Managed Instance in pair.
        type: str
      partner_managed_instance_id:
        description:
          - Id of Partner Managed Instance in pair.
        type: str
  failover_policy:
    description:
      - Failover policy of the read-only endpoint for the failover group.
    type: str
    choices:
      - Disabled
      - Enabled
  state:
    description:
      - Assert the state of the InstanceFailoverGroup.
      - >-
        Use C(present) to create or update an InstanceFailoverGroup and
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
    - name: Create failover group
      azure_rm_instancefailovergroup: 
        failover_group_name: failover-group-test-3
        location_name: Japan East
        resource_group_name: Default
        properties:
          managed_instance_pairs:
            - partner_managed_instance_id: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/managedInstances/failover-group-secondary-mngdInstance
              primary_managed_instance_id: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/managedInstances/failover-group-primary-mngdInstance
          partner_regions:
            - location: Japan West
          read_only_endpoint:
            failover_policy: Disabled
          read_write_endpoint:
            failover_policy: Automatic
            failover_with_data_loss_grace_period_minutes: 480
        

    - name: Delete failover group
      azure_rm_instancefailovergroup: 
        failover_group_name: failover-group-test-1
        location_name: Japan East
        resource_group_name: Default
        

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


class AzureRMInstanceFailoverGroup(AzureRMModuleBaseExt):
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
            partner_regions=dict(
                type='list',
                disposition='/partner_regions',
                elements='dict',
                options=dict(
                    location=dict(
                        type='str',
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
            managed_instance_pairs=dict(
                type='list',
                disposition='/managed_instance_pairs',
                elements='dict',
                options=dict(
                    primary_managed_instance_id=dict(
                        type='str',
                        disposition='primary_managed_instance_id'
                    ),
                    partner_managed_instance_id=dict(
                        type='str',
                        disposition='partner_managed_instance_id'
                    )
                )
            ),
            failover_policy=dict(
                type='str',
                disposition='/failover_policy',
                choices=['Disabled',
                         'Enabled']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.location_name = None
        self.failover_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMInstanceFailoverGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-10-01-preview')

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
            response = self.mgmt_client.instance_failover_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                                  location_name=self.location_name,
                                                                                  failover_group_name=self.failover_group_name,
                                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the InstanceFailoverGroup instance.')
            self.fail('Error creating the InstanceFailoverGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.instance_failover_groups.delete(resource_group_name=self.resource_group_name,
                                                                        location_name=self.location_name,
                                                                        failover_group_name=self.failover_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the InstanceFailoverGroup instance.')
            self.fail('Error deleting the InstanceFailoverGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.instance_failover_groups.get(resource_group_name=self.resource_group_name,
                                                                     location_name=self.location_name,
                                                                     failover_group_name=self.failover_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMInstanceFailoverGroup()


if __name__ == '__main__':
    main()
