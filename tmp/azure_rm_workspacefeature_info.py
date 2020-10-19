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
module: azure_rm_workspacefeature_info
version_added: '2.9'
short_description: Get WorkspaceFeature info.
description:
  - Get info of WorkspaceFeature.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Workspace features
      azure_rm_workspacefeature_info: 
        resource_group_name: myResourceGroup
        workspace_name: testworkspace
        

'''

RETURN = '''
workspace_features:
  description: >-
    A list of dict results where the key is the name of the WorkspaceFeature and
    the values are the facts for that WorkspaceFeature.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of AML user facing features.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Specifies the feature ID
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - 'Specifies the feature name '
          returned: always
          type: str
          sample: null
        description:
          description:
            - Describes the feature for user experience
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          The URI to fetch the next page of AML user features information. Call
          ListNext() with this to fetch the next page of AML user features
          information.
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


class AzureRMWorkspaceFeatureInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.workspace_name = None

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
        super(AzureRMWorkspaceFeatureInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Machine Learning Workspaces,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None):
            self.results['workspace_features'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.workspace_features.list(resource_group_name=self.resource_group_name,
                                                                workspace_name=self.workspace_name)
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
    AzureRMWorkspaceFeatureInfo()


if __name__ == '__main__':
    main()
