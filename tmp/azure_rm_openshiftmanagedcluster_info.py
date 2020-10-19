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
module: azure_rm_openshiftmanagedcluster_info
version_added: '2.9'
short_description: Get OpenShiftManagedCluster info.
description:
  - Get info of OpenShiftManagedCluster.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  resource_name:
    description:
      - The name of the OpenShift managed cluster resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Managed Clusters
      azure_rm_openshiftmanagedcluster_info: 
        {}
        

    - name: Get Managed Clusters by Resource Group
      azure_rm_openshiftmanagedcluster_info: 
        resource_group_name: rg1
        

    - name: Get OpenShift Managed Cluster
      azure_rm_openshiftmanagedcluster_info: 
        resource_group_name: rg1
        resource_name: clustername1
        

'''

RETURN = '''
open_shift_managed_clusters:
  description: >-
    A list of dict results where the key is the name of the
    OpenShiftManagedCluster and the values are the facts for that
    OpenShiftManagedCluster.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of OpenShift managed clusters.
      returned: always
      type: list
      sample: null
      contains:
        plan:
          description:
            - Define the resource plan as required by ARM for billing purposes
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The plan ID.
              returned: always
              type: str
              sample: null
            product:
              description:
                - >-
                  Specifies the product of the image from the marketplace. This
                  is the same value as Offer under the imageReference element.
              returned: always
              type: str
              sample: null
            promotion_code:
              description:
                - The promotion code.
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - The plan ID.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - >-
              The current deployment or provisioning state, which only appears
              in the response.
          returned: always
          type: str
          sample: null
        open_shift_version:
          description:
            - Version of OpenShift specified when creating the cluster.
          returned: always
          type: str
          sample: null
        cluster_version:
          description:
            - Version of OpenShift specified when creating the cluster.
          returned: always
          type: str
          sample: null
        public_hostname:
          description:
            - Service generated FQDN for OpenShift API server.
          returned: always
          type: str
          sample: null
        fqdn:
          description:
            - >-
              Service generated FQDN for OpenShift API server loadbalancer
              internal hostname.
          returned: always
          type: str
          sample: null
        network_profile:
          description:
            - Configuration for OpenShift networking.
          returned: always
          type: dict
          sample: null
          contains:
            vnet_cidr:
              description:
                - CIDR for the OpenShift Vnet.
              returned: always
              type: str
              sample: null
            peer_vnet_id:
              description:
                - CIDR of the Vnet to peer.
              returned: always
              type: str
              sample: null
            vnet_id:
              description:
                - ID of the Vnet created for OSA cluster.
              returned: always
              type: str
              sample: null
        router_profiles:
          description:
            - Configuration for OpenShift router(s).
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the router profile.
              returned: always
              type: str
              sample: null
            public_subdomain:
              description:
                - DNS subdomain for OpenShift router.
              returned: always
              type: str
              sample: null
            fqdn:
              description:
                - Auto-allocated FQDN for the OpenShift router.
              returned: always
              type: str
              sample: null
        master_pool_profile:
          description:
            - Configuration for OpenShift master VMs.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  Unique name of the master pool profile in the context of the
                  subscription and resource group.
              returned: always
              type: str
              sample: null
            count:
              description:
                - >-
                  Number of masters (VMs) to host docker containers. The default
                  value is 3.
              returned: always
              type: integer
              sample: null
            vm_size:
              description:
                - Size of agent VMs.
              returned: always
              type: str
              sample: null
            subnet_cidr:
              description:
                - Subnet CIDR for the peering.
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
        agent_pool_profiles:
          description:
            - Configuration of OpenShift cluster VMs.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  Unique name of the pool profile in the context of the
                  subscription and resource group.
              returned: always
              type: str
              sample: null
            count:
              description:
                - Number of agents (VMs) to host docker containers.
              returned: always
              type: integer
              sample: null
            vm_size:
              description:
                - Size of agent VMs.
              returned: always
              type: str
              sample: null
            subnet_cidr:
              description:
                - Subnet CIDR for the peering.
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
            role:
              description:
                - Define the role of the AgentPoolProfile.
              returned: always
              type: str
              sample: null
        identity_providers:
          description:
            - Type of authentication profile to use.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the provider.
              returned: always
              type: str
              sample: null
            provider:
              description:
                - Configuration of the provider.
              returned: always
              type: dict
              sample: null
              contains:
                kind:
                  description:
                    - The kind of the provider.
                  returned: always
                  type: str
                  sample: null
    next_link:
      description:
        - The URL to get the next set of OpenShift managed cluster results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
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
    plan:
      description:
        - Define the resource plan as required by ARM for billing purposes
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - The plan ID.
          returned: always
          type: str
          sample: null
        product:
          description:
            - >-
              Specifies the product of the image from the marketplace. This is
              the same value as Offer under the imageReference element.
          returned: always
          type: str
          sample: null
        promotion_code:
          description:
            - The promotion code.
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - The plan ID.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - >-
          The current deployment or provisioning state, which only appears in
          the response.
      returned: always
      type: str
      sample: null
    open_shift_version:
      description:
        - Version of OpenShift specified when creating the cluster.
      returned: always
      type: str
      sample: null
    cluster_version:
      description:
        - Version of OpenShift specified when creating the cluster.
      returned: always
      type: str
      sample: null
    public_hostname:
      description:
        - Service generated FQDN for OpenShift API server.
      returned: always
      type: str
      sample: null
    fqdn:
      description:
        - >-
          Service generated FQDN for OpenShift API server loadbalancer internal
          hostname.
      returned: always
      type: str
      sample: null
    network_profile:
      description:
        - Configuration for OpenShift networking.
      returned: always
      type: dict
      sample: null
      contains:
        vnet_cidr:
          description:
            - CIDR for the OpenShift Vnet.
          returned: always
          type: str
          sample: null
        peer_vnet_id:
          description:
            - CIDR of the Vnet to peer.
          returned: always
          type: str
          sample: null
        vnet_id:
          description:
            - ID of the Vnet created for OSA cluster.
          returned: always
          type: str
          sample: null
    router_profiles:
      description:
        - Configuration for OpenShift router(s).
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the router profile.
          returned: always
          type: str
          sample: null
        public_subdomain:
          description:
            - DNS subdomain for OpenShift router.
          returned: always
          type: str
          sample: null
        fqdn:
          description:
            - Auto-allocated FQDN for the OpenShift router.
          returned: always
          type: str
          sample: null
    master_pool_profile:
      description:
        - Configuration for OpenShift master VMs.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              Unique name of the master pool profile in the context of the
              subscription and resource group.
          returned: always
          type: str
          sample: null
        count:
          description:
            - >-
              Number of masters (VMs) to host docker containers. The default
              value is 3.
          returned: always
          type: integer
          sample: null
        vm_size:
          description:
            - Size of agent VMs.
          returned: always
          type: str
          sample: null
        subnet_cidr:
          description:
            - Subnet CIDR for the peering.
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
    agent_pool_profiles:
      description:
        - Configuration of OpenShift cluster VMs.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              Unique name of the pool profile in the context of the subscription
              and resource group.
          returned: always
          type: str
          sample: null
        count:
          description:
            - Number of agents (VMs) to host docker containers.
          returned: always
          type: integer
          sample: null
        vm_size:
          description:
            - Size of agent VMs.
          returned: always
          type: str
          sample: null
        subnet_cidr:
          description:
            - Subnet CIDR for the peering.
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
        role:
          description:
            - Define the role of the AgentPoolProfile.
          returned: always
          type: str
          sample: null
    identity_providers:
      description:
        - Type of authentication profile to use.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the provider.
          returned: always
          type: str
          sample: null
        provider:
          description:
            - Configuration of the provider.
          returned: always
          type: dict
          sample: null
          contains:
            kind:
              description:
                - The kind of the provider.
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


class AzureRMOpenShiftManagedClusterInfo(AzureRMModuleBase):
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
        self.query_parameters['api-version'] = '2019-04-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOpenShiftManagedClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerServiceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-30')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['open_shift_managed_clusters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['open_shift_managed_clusters'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['open_shift_managed_clusters'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.open_shift_managed_clusters.get(resource_group_name=self.resource_group_name,
                                                                        resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.open_shift_managed_clusters.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.open_shift_managed_clusters.list()
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
    AzureRMOpenShiftManagedClusterInfo()


if __name__ == '__main__':
    main()
