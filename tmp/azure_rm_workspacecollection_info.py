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
module: azure_rm_workspacecollection_info
version_added: '2.9'
short_description: Get WorkspaceCollection info.
description:
  - Get info of WorkspaceCollection.
options:
  resource_group_name:
    description:
      - Azure resource group
    type: str
  workspace_collection_name:
    description:
      - Power BI Embedded Workspace Collection name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
workspace_collections:
  description: >-
    A list of dict results where the key is the name of the WorkspaceCollection
    and the values are the facts for that WorkspaceCollection.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Workspace collection name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Azure location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Dictionary of <string>
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - SKU name
          returned: always
          type: str
          sample: null
        tier:
          description:
            - SKU tier
          returned: always
          type: str
          sample: null
    properties:
      description:
        - Properties
      returned: always
      type: any
      sample: null
    value:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Workspace collection name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure location
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Dictionary of <string>
          returned: always
          type: dictionary
          sample: null
        sku:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - SKU name
              returned: always
              type: str
              sample: null
            tier:
              description:
                - SKU tier
              returned: always
              type: str
              sample: null
        properties:
          description:
            - Properties
          returned: always
          type: any
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.power import Power BI Embedded Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWorkspaceCollectionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            workspace_collection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_collection_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-01-29'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWorkspaceCollectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Power BI Embedded Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-01-29')

        if (self.resource_group_name is not None and
            self.workspace_collection_name is not None):
            self.results['workspace_collections'] = self.format_item(self.getbyname())
        elif (self.resource_group_name is not None):
            self.results['workspace_collections'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['workspace_collections'] = self.format_item(self.listbysubscription())
        return self.results

    def getbyname(self):
        response = None

        try:
            response = self.mgmt_client.workspace_collections.get_by_name(resource_group_name=self.resource_group_name,
                                                                          workspace_collection_name=self.workspace_collection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.workspace_collections.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.workspace_collections.list_by_subscription()
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
    AzureRMWorkspaceCollectionInfo()


if __name__ == '__main__':
    main()
