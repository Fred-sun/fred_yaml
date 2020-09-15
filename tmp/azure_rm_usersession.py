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
module: azure_rm_usersession
version_added: '2.9'
short_description: Manage Azure UserSession instance.
description:
  - 'Create, update and delete instance of Azure UserSession.'
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
  user_session_id:
    description:
      - The name of the user session within the specified session host
    required: true
    type: str
  force:
    description:
      - Force flag to login off userSession.
    type: bool
  state:
    description:
      - Assert the state of the UserSession.
      - >-
        Use C(present) to create or update an UserSession and C(absent) to
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
    - name: UserSession_Delete
      azure_rm_usersession: 
        force: true
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        session_host_name: sessionHost1.microsoft.com
        user_session_id: '1'
        

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
user_principal_name:
  description:
    - The user principal name.
  returned: always
  type: str
  sample: null
application_type:
  description:
    - Application type of application.
  returned: always
  type: str
  sample: null
session_state:
  description:
    - State of user session.
  returned: always
  type: str
  sample: null
active_directory_user_name:
  description:
    - The active directory user name.
  returned: always
  type: str
  sample: null
create_time:
  description:
    - The timestamp of the user session create.
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


class AzureRMUserSession(AzureRMModuleBaseExt):
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
            user_session_id=dict(
                type='str',
                required=True
            ),
            force=dict(
                type='bool'
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
        self.user_session_id = None
        self.force = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMUserSession, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.user_sessions.create()
            else:
                response = self.mgmt_client.user_sessions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the UserSession instance.')
            self.fail('Error creating the UserSession instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.user_sessions.delete(resource_group_name=self.resource_group_name,
                                                             host_pool_name=self.host_pool_name,
                                                             session_host_name=self.session_host_name,
                                                             user_session_id=self.user_session_id,
                                                             force=self.force)
        except CloudError as e:
            self.log('Error attempting to delete the UserSession instance.')
            self.fail('Error deleting the UserSession instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.user_sessions.get(resource_group_name=self.resource_group_name,
                                                          host_pool_name=self.host_pool_name,
                                                          session_host_name=self.session_host_name,
                                                          user_session_id=self.user_session_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMUserSession()


if __name__ == '__main__':
    main()
