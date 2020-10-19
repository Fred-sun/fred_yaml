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
module: azure_rm_managedcluster_info
version_added: '2.9'
short_description: Get ManagedCluster info.
description:
  - Get info of ManagedCluster.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  resource_name:
    description:
      - The name of the managed cluster resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Managed Clusters
      azure_rm_managedcluster_info: 
        {}
        

    - name: Get Managed Clusters by Resource Group
      azure_rm_managedcluster_info: 
        resource_group_name: rg1
        

    - name: Get Upgrade Profile for Managed Cluster
      azure_rm_managedcluster_info: 
        resource_group_name: rg1
        resource_name: clustername1
        

    - name: Get Managed Cluster
      azure_rm_managedcluster_info: 
        resource_group_name: rg1
        resource_name: clustername1
        

'''

RETURN = '''
managed_clusters:
  description: >-
    A list of dict results where the key is the name of the ManagedCluster and
    the values are the facts for that ManagedCluster.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of managed clusters.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - The managed cluster SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of a managed cluster SKU.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - Tier of a managed cluster SKU.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - The URL to get the next set of managed cluster results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - |-
          Id of upgrade profile.
          Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - |-
          Name of upgrade profile.
          Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - |-
          Type of upgrade profile.
          Resource type
      returned: always
      type: str
      sample: null
    control_plane_profile:
      description:
        - The list of available upgrade versions for the control plane.
      returned: always
      type: dict
      sample: null
      contains:
        kubernetes_version:
          description:
            - 'Kubernetes version (major, minor, patch).'
          returned: always
          type: str
          sample: null
        name:
          description:
            - Pool name.
          returned: always
          type: str
          sample: null
        os_type:
          description:
            - >-
              OsType to be used to specify os type. Choose from Linux and
              Windows. Default to Linux.
          returned: always
          type: str
          sample: null
        upgrades:
          description:
            - List of orchestrator types and versions available for upgrade.
          returned: always
          type: list
          sample: null
          contains:
            kubernetes_version:
              description:
                - 'Kubernetes version (major, minor, patch).'
              returned: always
              type: str
              sample: null
            is_preview:
              description:
                - Whether Kubernetes version is currently in preview.
              returned: always
              type: bool
              sample: null
    agent_pool_profiles:
      description:
        - The list of available upgrade versions for agent pools.
      returned: always
      type: list
      sample: null
      contains:
        kubernetes_version:
          description:
            - 'Kubernetes version (major, minor, patch).'
          returned: always
          type: str
          sample: null
        name:
          description:
            - Pool name.
          returned: always
          type: str
          sample: null
        os_type:
          description:
            - >-
              OsType to be used to specify os type. Choose from Linux and
              Windows. Default to Linux.
          returned: always
          type: str
          sample: null
        upgrades:
          description:
            - List of orchestrator types and versions available for upgrade.
          returned: always
          type: list
          sample: null
          contains:
            kubernetes_version:
              description:
                - 'Kubernetes version (major, minor, patch).'
              returned: always
              type: str
              sample: null
            is_preview:
              description:
                - Whether Kubernetes version is currently in preview.
              returned: always
              type: bool
              sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - The managed cluster SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of a managed cluster SKU.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - Tier of a managed cluster SKU.
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
    from azure.mgmt.container import ContainerServiceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagedClusterInfo(AzureRMModuleBase):
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
        self.query_parameters['api-version'] = '2020-09-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerServiceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['managed_clusters'] = self.format_item(self.getupgradeprofile())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['managed_clusters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['managed_clusters'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['managed_clusters'] = self.format_item(self.list())
        return self.results

    def getupgradeprofile(self):
        response = None

        try:
            response = self.mgmt_client.managed_clusters.get_upgrade_profile(resource_group_name=self.resource_group_name,
                                                                             resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_clusters.get(resource_group_name=self.resource_group_name,
                                                             resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.managed_clusters.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.managed_clusters.list()
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
    AzureRMManagedClusterInfo()


if __name__ == '__main__':
    main()
