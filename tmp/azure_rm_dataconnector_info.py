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
module: azure_rm_dataconnector_info
version_added: '2.9'
short_description: Get DataConnector info.
description:
  - Get info of DataConnector.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  workspace_name:
    description:
      - The name of the workspace.
    required: true
    type: str
  data_connector_id:
    description:
      - Connector ID
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all data connectors.
      azure_rm_dataconnector_info: 
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get a ASC data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: 763f9fa1-c2d3-4fa2-93e9-bccd4899aa12
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get a MCAS data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: b96d014d-b5c2-4a01-9aba-a8058f629d42
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get a MDATP data connector
      azure_rm_dataconnector_info: 
        data_connector_id: 06b3ccb8-1384-4bcc-aec7-852f6d57161b
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get a TI data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: c345bf40-8509-4ed2-b947-50cb773aaf04
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get an AAD data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: f0cd27d2-5f03-4c06-ba31-d2dc82dcb51d
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get an AATP data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: 07e42cb3-e658-4e90-801c-efa0f29d3d44
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get an AwsCloudTrail data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: c345bf40-8509-4ed2-b947-50cb773aaf04
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get an Office365 data connector.
      azure_rm_dataconnector_info: 
        data_connector_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

'''

RETURN = '''
data_connectors:
  description: >-
    A list of dict results where the key is the name of the DataConnector and
    the values are the facts for that DataConnector.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URL to fetch the next set of data connectors.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of data connectors.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - The data connector kind
          returned: always
          type: str
          sample: null
    id:
      description:
        - Azure resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Azure resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Azure resource type
      returned: always
      type: str
      sample: null
    etag:
      description:
        - Etag of the azure resource
      returned: always
      type: str
      sample: null
    kind:
      description:
        - The data connector kind
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
    from azure.mgmt.security import Security Insights
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataConnectorInfo(AzureRMModuleBase):
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
            data_connector_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.data_connector_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDataConnectorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.data_connector_id is not None):
            self.results['data_connectors'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['data_connectors'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_connectors.get(resource_group_name=self.resource_group_name,
                                                            workspace_name=self.workspace_name,
                                                            data_connector_id=self.data_connector_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.data_connectors.list(resource_group_name=self.resource_group_name,
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
    AzureRMDataConnectorInfo()


if __name__ == '__main__':
    main()
