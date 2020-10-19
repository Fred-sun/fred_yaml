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
module: azure_rm_workspaceconnection
version_added: '2.9'
short_description: Manage Azure WorkspaceConnection instance.
description:
  - 'Create, update and delete instance of Azure WorkspaceConnection.'
options:
  resource_group_name:
    description:
      - Name of the resource group in which workspace is located.
    required: true
    type: str
  workspace_name:
    description:
      - Name of Azure Machine Learning workspace.
    required: true
    type: str
  connection_name:
    description:
      - Friendly name of the workspace connection
    required: true
    type: str
  name:
    description:
      - Friendly name of the workspace connection
    type: str
  category:
    description:
      - Category of the workspace connection.
    type: str
  target:
    description:
      - Target of the workspace connection.
    type: str
  auth_type:
    description:
      - Authorization type of the workspace connection.
    type: str
  value:
    description:
      - Value details of the workspace connection.
    type: str
  state:
    description:
      - Assert the state of the WorkspaceConnection.
      - >-
        Use C(present) to create or update an WorkspaceConnection and C(absent)
        to delete it.
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
    - name: CreateWorkspaceConnection
      azure_rm_workspaceconnection: 
        connection_name: connection-1
        resource_group_name: resourceGroup-1
        workspace_name: workspace-1
        name: connection-1
        properties:
          auth_type: PAT
          category: ACR
          target: www.facebook.com
          value: secrets
        

    - name: DeleteWorkspaceConnection
      azure_rm_workspaceconnection: 
        connection_name: connection-1
        resource_group_name: resourceGroup-1
        workspace_name: workspace-1
        

'''

RETURN = '''
id:
  description:
    - ResourceId of the workspace connection.
  returned: always
  type: str
  sample: null
name:
  description:
    - Friendly name of the workspace connection.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type of workspace connection.
  returned: always
  type: str
  sample: null
category:
  description:
    - Category of the workspace connection.
  returned: always
  type: str
  sample: null
target:
  description:
    - Target of the workspace connection.
  returned: always
  type: str
  sample: null
auth_type:
  description:
    - Authorization type of the workspace connection.
  returned: always
  type: str
  sample: null
value:
  description:
    - Value details of the workspace connection.
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
    from azure.mgmt.azure import Azure Machine Learning Workspaces
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMWorkspaceConnection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            ),
            connection_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            category=dict(
                type='str',
                disposition='/category'
            ),
            target=dict(
                type='str',
                disposition='/target'
            ),
            auth_type=dict(
                type='str',
                disposition='/auth_type'
            ),
            value=dict(
                type='str',
                disposition='/value'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.connection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMWorkspaceConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Machine Learning Workspaces,
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
                response = self.mgmt_client.workspace_connections.create(resource_group_name=self.resource_group_name,
                                                                         workspace_name=self.workspace_name,
                                                                         connection_name=self.connection_name,
                                                                         parameters=self.body)
            else:
                response = self.mgmt_client.workspace_connections.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the WorkspaceConnection instance.')
            self.fail('Error creating the WorkspaceConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.workspace_connections.delete(resource_group_name=self.resource_group_name,
                                                                     workspace_name=self.workspace_name,
                                                                     connection_name=self.connection_name)
        except CloudError as e:
            self.log('Error attempting to delete the WorkspaceConnection instance.')
            self.fail('Error deleting the WorkspaceConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.workspace_connections.get(resource_group_name=self.resource_group_name,
                                                                  workspace_name=self.workspace_name,
                                                                  connection_name=self.connection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMWorkspaceConnection()


if __name__ == '__main__':
    main()
