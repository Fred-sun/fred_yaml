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
module: azure_rm_notebookworkspace_info
version_added: '2.9'
short_description: Get NotebookWorkspace info.
description:
  - Get info of NotebookWorkspace.
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
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CosmosDBNotebookWorkspaceList
      azure_rm_notebookworkspace_info: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBNotebookWorkspaceGet
      azure_rm_notebookworkspace_info: 
        account_name: ddb1
        notebook_workspace_name: default
        resource_group_name: rg1
        

'''

RETURN = '''
notebook_workspaces:
  description: >-
    A list of dict results where the key is the name of the NotebookWorkspace
    and the values are the facts for that NotebookWorkspace.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of notebook workspace resources
      returned: always
      type: list
      sample: null
      contains:
        notebook_server_endpoint:
          description:
            - Specifies the endpoint of Notebook server.
          returned: always
          type: str
          sample: null
        status:
          description:
            - >-
              Status of the notebook workspace. Possible values are: Creating,
              Online, Deleting, Failed, Updating.
          returned: always
          type: str
          sample: null
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
          Status of the notebook workspace. Possible values are: Creating,
          Online, Deleting, Failed, Updating.
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
    from azure.mgmt.cosmos import CosmosDBManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNotebookWorkspaceInfo(AzureRMModuleBase):
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
                choices=['default']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.notebook_workspace_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMNotebookWorkspaceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.notebook_workspace_name is not None):
            self.results['notebook_workspaces'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['notebook_workspaces'] = self.format_item(self.listbydatabaseaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.notebook_workspaces.get(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                notebook_workspace_name=self.notebook_workspace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabaseaccount(self):
        response = None

        try:
            response = self.mgmt_client.notebook_workspaces.list_by_database_account(resource_group_name=self.resource_group_name,
                                                                                     account_name=self.account_name)
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
    AzureRMNotebookWorkspaceInfo()


if __name__ == '__main__':
    main()
