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
module: azure_rm_replicationlink
version_added: '2.9'
short_description: Manage Azure ReplicationLink instance.
description:
  - 'Create, update and delete instance of Azure ReplicationLink.'
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
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - The name of the database that has the replication link to be dropped.
      - The name of the database to get the link for.
    required: true
    type: str
  link_id:
    description:
      - The ID of the replication link to be deleted.
      - The replication link ID to be retrieved.
    required: true
    type: str
  state:
    description:
      - Assert the state of the ReplicationLink.
      - >-
        Use C(present) to create or update an ReplicationLink and C(absent) to
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
    - name: Delete a replication link
      azure_rm_replicationlink: 
        database_name: testdb
        link_id: 5b301b68-03f6-4b26-b0f4-73ebb8634238
        resource_group_name: sqlcrudtest-4799
        server_name: sqlcrudtest-6440
        

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
    - Location of the server that contains this firewall rule.
  returned: always
  type: str
  sample: null
is_termination_allowed:
  description:
    - >-
      Legacy value indicating whether termination is allowed.  Currently always
      returns true.
  returned: always
  type: bool
  sample: null
replication_mode:
  description:
    - Replication mode of this replication link.
  returned: always
  type: str
  sample: null
partner_server:
  description:
    - The name of the server hosting the partner database.
  returned: always
  type: str
  sample: null
partner_database:
  description:
    - The name of the partner database.
  returned: always
  type: str
  sample: null
partner_location:
  description:
    - The Azure Region of the partner database.
  returned: always
  type: str
  sample: null
role:
  description:
    - The role of the database in the replication link.
  returned: always
  type: sealed-choice
  sample: null
partner_role:
  description:
    - The role of the partner database in the replication link.
  returned: always
  type: sealed-choice
  sample: null
start_time:
  description:
    - The start time for the replication link.
  returned: always
  type: str
  sample: null
percent_complete:
  description:
    - The percentage of seeding complete for the replication link.
  returned: always
  type: integer
  sample: null
replication_state:
  description:
    - The replication state for the replication link.
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


class AzureRMReplicationLink(AzureRMModuleBaseExt):
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
            database_name=dict(
                type='str',
                required=True
            ),
            link_id=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.link_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMReplicationLink, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2014-04-01')

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
                response = self.mgmt_client.replication_links.create()
            else:
                response = self.mgmt_client.replication_links.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ReplicationLink instance.')
            self.fail('Error creating the ReplicationLink instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.replication_links.delete(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 database_name=self.database_name,
                                                                 link_id=self.link_id)
        except CloudError as e:
            self.log('Error attempting to delete the ReplicationLink instance.')
            self.fail('Error deleting the ReplicationLink instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.replication_links.get(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              database_name=self.database_name,
                                                              link_id=self.link_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMReplicationLink()


if __name__ == '__main__':
    main()
