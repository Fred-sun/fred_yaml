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
module: azure_rm_virtualcluster_info
version_added: '2.9'
short_description: Get VirtualCluster info.
description:
  - Get info of VirtualCluster.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
  virtual_cluster_name:
    description:
      - The name of the virtual cluster.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List virtualClusters
      azure_rm_virtualcluster_info: 
        {}
        

    - name: List virtual clusters by resource group
      azure_rm_virtualcluster_info: 
        resource_group_name: testrg
        

    - name: Get virtual cluster
      azure_rm_virtualcluster_info: 
        resource_group_name: testrg
        virtual_cluster_name: vc-subnet1-f769ed71-b3ad-491a-a9d5-26eeceaa6be2
        

'''

RETURN = '''
virtual_clusters:
  description: >-
    A list of dict results where the key is the name of the VirtualCluster and
    the values are the facts for that VirtualCluster.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        subnet_id:
          description:
            - Subnet resource ID for the virtual cluster.
          returned: always
          type: str
          sample: null
        family:
          description:
            - >-
              If the service has different generations of hardware, for the same
              SKU, then that can be captured here.
          returned: always
          type: str
          sample: null
        child_resources:
          description:
            - List of resources in this virtual cluster.
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    subnet_id:
      description:
        - Subnet resource ID for the virtual cluster.
      returned: always
      type: str
      sample: null
    family:
      description:
        - >-
          If the service has different generations of hardware, for the same
          SKU, then that can be captured here.
      returned: always
      type: str
      sample: null
    child_resources:
      description:
        - List of resources in this virtual cluster.
      returned: always
      type: list
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualClusterInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            virtual_cluster_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.virtual_cluster_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-05-01-preview')

        if (self.resource_group_name is not None and
            self.virtual_cluster_name is not None):
            self.results['virtual_clusters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['virtual_clusters'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['virtual_clusters'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_clusters.get(resource_group_name=self.resource_group_name,
                                                             virtual_cluster_name=self.virtual_cluster_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.virtual_clusters.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_clusters.list()
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
    AzureRMVirtualClusterInfo()


if __name__ == '__main__':
    main()
