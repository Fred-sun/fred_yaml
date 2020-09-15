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
module: azure_rm_cluster_info
version_added: '2.9'
short_description: Get Cluster info.
description:
  - Get info of Cluster.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  private_cloud_name:
    description:
      - Name of the private cloud
    required: true
    type: str
  cluster_name:
    description:
      - Name of the cluster in the private cloud
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Clusters_List
      azure_rm_cluster_info: 
        private_cloud_name: cloud1
        resource_group_name: group1
        

    - name: Clusters_Get
      azure_rm_cluster_info: 
        cluster_name: cluster1
        private_cloud_name: cloud1
        resource_group_name: group1
        

'''

RETURN = '''
clusters:
  description: >-
    A list of dict results where the key is the name of the Cluster and the
    values are the facts for that Cluster.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The items on a page
      returned: always
      type: list
      sample: null
      contains:
        cluster_size:
          description:
            - The cluster size
          returned: always
          type: integer
          sample: null
        cluster_id:
          description:
            - The identity
          returned: always
          type: integer
          sample: null
        hosts:
          description:
            - The hosts
          returned: always
          type: list
          sample: null
        provisioning_state:
          description:
            - The state of the cluster provisioning
          returned: always
          type: str
          sample: null
        name_sku_name:
          description:
            - The name of the SKU.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next page if any
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    cluster_size:
      description:
        - The cluster size
      returned: always
      type: integer
      sample: null
    cluster_id:
      description:
        - The identity
      returned: always
      type: integer
      sample: null
    hosts:
      description:
        - The hosts
      returned: always
      type: list
      sample: null
    provisioning_state:
      description:
        - The state of the cluster provisioning
      returned: always
      type: str
      sample: null
    name_sku_name:
      description:
        - The name of the SKU.
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
    from azure.mgmt.azure import Azure VMware Solution API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMClusterInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            private_cloud_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.private_cloud_name = None
        self.cluster_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-20'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure VMware Solution API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-20')

        if (self.resource_group_name is not None and
            self.private_cloud_name is not None and
            self.cluster_name is not None):
            self.results['clusters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.private_cloud_name is not None):
            self.results['clusters'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.clusters.get(resource_group_name=self.resource_group_name,
                                                     private_cloud_name=self.private_cloud_name,
                                                     cluster_name=self.cluster_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.clusters.list(resource_group_name=self.resource_group_name,
                                                      private_cloud_name=self.private_cloud_name)
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
    AzureRMClusterInfo()


if __name__ == '__main__':
    main()
