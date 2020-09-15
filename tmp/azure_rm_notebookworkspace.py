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
module: azure_rm_notebookworkspace
version_added: '2.9'
short_description: Manage Azure NotebookWorkspace instance.
description:
  - 'Create, update and delete instance of Azure NotebookWorkspace.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    required: true
    type: str
  notebook_workspace_name:
    description:
      - The name of the notebook workspace resource.
    required: true
    type: str
    choices:
      - default
  state:
    description:
      - Assert the state of the NotebookWorkspace.
      - >-
        Use C(present) to create or update an NotebookWorkspace and C(absent) to
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
    - name: CosmosDBNotebookWorkspaceCreate
      azure_rm_notebookworkspace: 
        account_name: ddb1
        notebook_workspace_name: default
        resource_group_name: rg1
        

    - name: CosmosDBNotebookWorkspaceDelete
      azure_rm_notebookworkspace: 
        account_name: ddb1
        notebook_workspace_name: default
        resource_group_name: rg1
        

'''

RETURN = '''
id:
  description:
    - The unique resource identifier of the database account.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the database account.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of Azure resource.
  returned: always
  type: str
  sample: null
notebook_server_endpoint:
  description:
    - Specifies the endpoint of Notebook server.
  returned: always
  type: str
  sample: null
status:
  description:
    - >-
      Status of the notebook workspace. Possible values are: Creating, Online,
      Deleting, Failed, Updating.
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
    from azure.mgmt.cosmos import CosmosDBManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNotebookWorkspace(AzureRMModuleBaseExt):
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
            notebook_workspace_name=dict(
                type='str',
                choices=['default'],
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.notebook_workspace_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNotebookWorkspace, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

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
            response = self.mgmt_client.notebook_workspaces.create_or_update(resource_group_name=self.resource_group_name,
                                                                             account_name=self.account_name,
                                                                             notebook_workspace_name=self.notebook_workspace_name,
                                                                             notebook_create_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the NotebookWorkspace instance.')
            self.fail('Error creating the NotebookWorkspace instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.notebook_workspaces.delete(resource_group_name=self.resource_group_name,
                                                                   account_name=self.account_name,
                                                                   notebook_workspace_name=self.notebook_workspace_name)
        except CloudError as e:
            self.log('Error attempting to delete the NotebookWorkspace instance.')
            self.fail('Error deleting the NotebookWorkspace instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.notebook_workspaces.get(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                notebook_workspace_name=self.notebook_workspace_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNotebookWorkspace()


if __name__ == '__main__':
    main()
