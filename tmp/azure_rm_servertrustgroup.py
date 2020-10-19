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
module: azure_rm_servertrustgroup
version_added: '2.9'
short_description: Manage Azure ServerTrustGroup instance.
description:
  - 'Create, update and delete instance of Azure ServerTrustGroup.'
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
  server_trust_group_name:
    description:
      - The name of the server trust group.
    required: true
    type: str
  group_members:
    description:
      - Group members information for the server trust group.
    type: list
    suboptions:
      server_id:
        description:
          - Server Id.
        required: true
        type: str
  trust_scopes:
    description:
      - Trust scope of the server trust group.
    type: list
  state:
    description:
      - Assert the state of the ServerTrustGroup.
      - >-
        Use C(present) to create or update an ServerTrustGroup and C(absent) to
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
    - name: Create server trust group
      azure_rm_servertrustgroup: 
        location_name: Japan East
        resource_group_name: Default
        server_trust_group_name: server-trust-group-test
        properties:
          group_members:
            - server_id: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/managedInstances/managedInstance-1
            - server_id: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/managedInstances/managedInstance-2
          trust_scopes:
            - GlobalTransactions
        

    - name: Drop server trust group
      azure_rm_servertrustgroup: 
        location_name: Japan East
        resource_group_name: Default
        server_trust_group_name: server-trust-group-test
        

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
group_members:
  description:
    - Group members information for the server trust group.
  returned: always
  type: list
  sample: null
  contains:
    server_id:
      description:
        - Server Id.
      returned: always
      type: str
      sample: null
trust_scopes:
  description:
    - Trust scope of the server trust group.
  returned: always
  type: list
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


class AzureRMServerTrustGroup(AzureRMModuleBaseExt):
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
            server_trust_group_name=dict(
                type='str',
                required=True
            ),
            group_members=dict(
                type='list',
                disposition='/group_members',
                elements='dict',
                options=dict(
                    server_id=dict(
                        type='str',
                        disposition='server_id',
                        required=True
                    )
                )
            ),
            trust_scopes=dict(
                type='list',
                disposition='/trust_scopes',
                elements='constant'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.location_name = None
        self.server_trust_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServerTrustGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-02-02-preview')

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
            response = self.mgmt_client.server_trust_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                             location_name=self.location_name,
                                                                             server_trust_group_name=self.server_trust_group_name,
                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ServerTrustGroup instance.')
            self.fail('Error creating the ServerTrustGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.server_trust_groups.delete(resource_group_name=self.resource_group_name,
                                                                   location_name=self.location_name,
                                                                   server_trust_group_name=self.server_trust_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the ServerTrustGroup instance.')
            self.fail('Error deleting the ServerTrustGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.server_trust_groups.get(resource_group_name=self.resource_group_name,
                                                                location_name=self.location_name,
                                                                server_trust_group_name=self.server_trust_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServerTrustGroup()


if __name__ == '__main__':
    main()
