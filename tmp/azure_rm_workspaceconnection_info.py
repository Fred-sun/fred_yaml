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
module: azure_rm_workspaceconnection_info
version_added: '2.9'
short_description: Get WorkspaceConnection info.
description:
  - Get info of WorkspaceConnection.
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
  target:
    description:
      - Target of the workspace connection.
    type: str
  category:
    description:
      - Category of the workspace connection.
    type: str
  connection_name:
    description:
      - Friendly name of the workspace connection
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListWorkspaceConnections
      azure_rm_workspaceconnection_info: 
        category: ACR
        resource_group_name: resourceGroup-1
        target: www.facebook.com
        workspace_name: workspace-1
        

    - name: GetWorkspaceConnection
      azure_rm_workspaceconnection_info: 
        connection_name: connection-1
        resource_group_name: resourceGroup-1
        workspace_name: workspace-1
        

'''

RETURN = '''
workspace_connections:
  description: >-
    A list of dict results where the key is the name of the WorkspaceConnection
    and the values are the facts for that WorkspaceConnection.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          An array of Workspace connection objects.
          Value details of the workspace connection.
      returned: always
      type: list
      sample: null
      contains:
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
    next_link:
      description:
        - >-
          A continuation link (absolute URI) to the next page of results in the
          list.
      returned: always
      type: str
      sample: null
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

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Machine Learning Workspaces
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWorkspaceConnectionInfo(AzureRMModuleBase):
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
            target=dict(
                type='str'
            ),
            category=dict(
                type='str'
            ),
            connection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.target = None
        self.category = None
        self.connection_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWorkspaceConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Machine Learning Workspaces,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.connection_name is not None):
            self.results['workspace_connections'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['workspace_connections'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.workspace_connections.get(resource_group_name=self.resource_group_name,
                                                                  workspace_name=self.workspace_name,
                                                                  connection_name=self.connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.workspace_connections.list(resource_group_name=self.resource_group_name,
                                                                   workspace_name=self.workspace_name,
                                                                   target=self.target,
                                                                   category=self.category)
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
    AzureRMWorkspaceConnectionInfo()


if __name__ == '__main__':
    main()
