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
module: azure_rm_sessionhost
version_added: '2.9'
short_description: Manage Azure SessionHost instance.
description:
  - 'Create, update and delete instance of Azure SessionHost.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  host_pool_name:
    description:
      - The name of the host pool within the specified resource group
    required: true
    type: str
  session_host_name:
    description:
      - The name of the session host within the specified host pool
    required: true
    type: str
  force:
    description:
      - Force flag to force sessionHost deletion even when userSession exists.
    type: bool
  allow_new_session:
    description:
      - Allow a new session.
    type: bool
  assigned_user:
    description:
      - User assigned to SessionHost.
    type: str
  state:
    description:
      - Assert the state of the SessionHost.
      - >-
        Use C(present) to create or update an SessionHost and C(absent) to
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
    - name: SessionHost_Delete
      azure_rm_sessionhost: 
        force: true
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        session_host_name: sessionHost1.microsoft.com
        

    - name: SessionHost_Update
      azure_rm_sessionhost: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        session_host_name: sessionHost1.microsoft.com
        

'''

RETURN = '''
id:
  description:
    - >-
      Fully qualified resource Id for the resource. Ex -
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource. Ex- Microsoft.Compute/virtualMachines or
      Microsoft.Storage/storageAccounts.
  returned: always
  type: str
  sample: null
last_heart_beat:
  description:
    - Last heart beat from SessionHost.
  returned: always
  type: str
  sample: null
sessions:
  description:
    - Number of sessions on SessionHost.
  returned: always
  type: integer
  sample: null
agent_version:
  description:
    - Version of agent on SessionHost.
  returned: always
  type: str
  sample: null
allow_new_session:
  description:
    - Allow a new session.
  returned: always
  type: bool
  sample: null
virtual_machine_id:
  description:
    - Virtual Machine Id of SessionHost's underlying virtual machine.
  returned: always
  type: str
  sample: null
resource_id:
  description:
    - Resource Id of SessionHost's underlying virtual machine.
  returned: always
  type: str
  sample: null
assigned_user:
  description:
    - User assigned to SessionHost.
  returned: always
  type: str
  sample: null
status:
  description:
    - Status for a SessionHost.
  returned: always
  type: str
  sample: null
status_timestamp:
  description:
    - The timestamp of the status.
  returned: always
  type: str
  sample: null
os_version:
  description:
    - The version of the OS on the session host.
  returned: always
  type: str
  sample: null
sx_sstack_version:
  description:
    - The version of the side by side stack on the session host.
  returned: always
  type: str
  sample: null
update_state:
  description:
    - Update state of a SessionHost.
  returned: always
  type: str
  sample: null
last_update_time:
  description:
    - The timestamp of the last update.
  returned: always
  type: str
  sample: null
update_error_message:
  description:
    - The error message.
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
    from azure.mgmt.desktop import Desktop Virtualization API Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSessionHost(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            host_pool_name=dict(
                type='str',
                required=True
            ),
            session_host_name=dict(
                type='str',
                required=True
            ),
            force=dict(
                type='bool'
            ),
            allow_new_session=dict(
                type='bool',
                disposition='/allow_new_session'
            ),
            assigned_user=dict(
                type='str',
                disposition='/assigned_user'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.host_pool_name = None
        self.session_host_name = None
        self.force = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSessionHost, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

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
                response = self.mgmt_client.session_hosts.create()
            else:
                response = self.mgmt_client.session_hosts.update(resource_group_name=self.resource_group_name,
                                                                 host_pool_name=self.host_pool_name,
                                                                 session_host_name=self.session_host_name,
                                                                 session_host=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SessionHost instance.')
            self.fail('Error creating the SessionHost instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.session_hosts.delete(resource_group_name=self.resource_group_name,
                                                             host_pool_name=self.host_pool_name,
                                                             session_host_name=self.session_host_name,
                                                             force=self.force)
        except CloudError as e:
            self.log('Error attempting to delete the SessionHost instance.')
            self.fail('Error deleting the SessionHost instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.session_hosts.get(resource_group_name=self.resource_group_name,
                                                          host_pool_name=self.host_pool_name,
                                                          session_host_name=self.session_host_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSessionHost()


if __name__ == '__main__':
    main()
