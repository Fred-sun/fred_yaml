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
module: azure_rm_enterpriseknowledgegraph_info
version_added: '2.9'
short_description: Get EnterpriseKnowledgeGraph info.
description:
  - Get info of EnterpriseKnowledgeGraph.
options:
  resource_group_name:
    description:
      - >-
        The name of the EnterpriseKnowledgeGraph resource group in the user
        subscription.
    type: str
  resource_name:
    description:
      - The name of the EnterpriseKnowledgeGraph resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get EnterpriseKnowledgeGraph
      azure_rm_enterpriseknowledgegraph_info: 
        resource_group_name: OneResourceGroupName
        resource_name: sampleekgname
        

    - name: List EnterpriseKnowledgeGraph by Resource Group
      azure_rm_enterpriseknowledgegraph_info: 
        resource_group_name: OneResourceGroupName
        

    - name: List EnterpriseKnowledgeGraph by Subscription
      azure_rm_enterpriseknowledgegraph_info: 
        {}
        

'''

RETURN = '''
enterprise_knowledge_graph:
  description: >-
    A list of dict results where the key is the name of the
    EnterpriseKnowledgeGraph and the values are the facts for that
    EnterpriseKnowledgeGraph.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Specifies the resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Specifies the name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Specifies the type of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Specifies the location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Contains resource tags defined as key/value pairs.
      returned: always
      type: dictionary
      sample: null
    name_sku_name:
      description:
        - The sku name
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the EnterpriseKnowledgeGraph
      returned: always
      type: str
      sample: null
    metadata:
      description:
        - Specifies the metadata  of the resource.
      returned: always
      type: any
      sample: null
    provisioning_state:
      description:
        - The state of EnterpriseKnowledgeGraph provisioning
      returned: always
      type: str
      sample: null
    next_link:
      description:
        - >-
          The link used to get the next page of EnterpriseKnowledgeGraph service
          resources.
      returned: always
      type: str
      sample: null
    value:
      description:
        - >-
          Gets the list of EnterpriseKnowledgeGraph service results and their
          properties.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The description of the EnterpriseKnowledgeGraph
          returned: always
          type: str
          sample: null
        metadata:
          description:
            - Specifies the metadata  of the resource.
          returned: always
          type: any
          sample: null
        provisioning_state:
          description:
            - The state of EnterpriseKnowledgeGraph provisioning
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
    from azure.mgmt.azure import Azure Enterprise Knowledge Graph Service
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEnterpriseKnowledgeGraphInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-12-03'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEnterpriseKnowledgeGraphInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Enterprise Knowledge Graph Service,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-12-03')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['enterprise_knowledge_graph'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['enterprise_knowledge_graph'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['enterprise_knowledge_graph'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.enterprise_knowledge_graph.get(resource_group_name=self.resource_group_name,
                                                                       resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.enterprise_knowledge_graph.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.enterprise_knowledge_graph.list()
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
    AzureRMEnterpriseKnowledgeGraphInfo()


if __name__ == '__main__':
    main()
