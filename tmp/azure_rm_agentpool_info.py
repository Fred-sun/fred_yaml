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
module: azure_rm_agentpool_info
version_added: '2.9'
short_description: Get AgentPool info.
description:
  - Get info of AgentPool.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  resource_name:
    description:
      - The name of the managed cluster resource.
    required: true
    type: str
  agent_pool_name:
    description:
      - The name of the agent pool.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Agent Pools by Managed Cluster
      azure_rm_agentpool_info: 
        resource_group_name: rg1
        resource_name: clustername1
        

    - name: Get Agent Pool
      azure_rm_agentpool_info: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        

    - name: Get Upgrade Profile for Agent Pool
      azure_rm_agentpool_info: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        

    - name: Get available versions for agent pool
      azure_rm_agentpool_info: 
        resource_group_name: rg1
        resource_name: clustername1
        

'''

RETURN = '''
agent_pools:
  description: >-
    A list of dict results where the key is the name of the AgentPool and the
    values are the facts for that AgentPool.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of agent pools.
      returned: always
      type: list
      sample: null
      contains:
        count:
          description:
            - >-
              Number of agents (VMs) to host docker containers. Allowed values
              must be in the range of 0 to 100 (inclusive) for user pools and in
              the range of 1 to 100 (inclusive) for system pools. The default
              value is 1.
          returned: always
          type: integer
          sample: null
        vm_size:
          description:
            - Size of agent VMs.
          returned: always
          type: str
          sample: null
        os_disk_size_gb:
          description:
            - >-
              OS Disk Size in GB to be used to specify the disk size for every
              machine in this master/agent pool. If you specify 0, it will apply
              the default osDisk size according to the vmSize specified.
          returned: always
          type: integer
          sample: null
        os_disk_type:
          description:
            - >-
              OS disk type to be used for machines in a given agent pool.
              Allowed values are 'Ephemeral' and 'Managed'. Defaults to
              'Managed'. May not be changed after creation.
          returned: always
          type: str
          sample: null
        vnet_subnet_id:
          description:
            - VNet SubnetID specifies the VNet's subnet identifier.
          returned: always
          type: str
          sample: null
        max_pods:
          description:
            - Maximum number of pods that can run on a node.
          returned: always
          type: integer
          sample: null
        os_type:
          description:
            - >-
              OsType to be used to specify os type. Choose from Linux and
              Windows. Default to Linux.
          returned: always
          type: str
          sample: null
        max_count:
          description:
            - Maximum number of nodes for auto-scaling
          returned: always
          type: integer
          sample: null
        min_count:
          description:
            - Minimum number of nodes for auto-scaling
          returned: always
          type: integer
          sample: null
        enable_auto_scaling:
          description:
            - Whether to enable auto-scaler
          returned: always
          type: bool
          sample: null
        type_properties_type:
          description:
            - AgentPoolType represents types of an agent pool
          returned: always
          type: str
          sample: null
        mode:
          description:
            - AgentPoolMode represents mode of an agent pool
          returned: always
          type: str
          sample: null
        orchestrator_version:
          description:
            - >-
              Version of orchestrator specified when creating the managed
              cluster.
          returned: always
          type: str
          sample: null
        node_image_version:
          description:
            - Version of node image
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
        power_state:
          description:
            - Describes whether the Agent Pool is Running or Stopped
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - Tells whether the cluster is Running or Stopped
              returned: always
              type: str
              sample: null
        availability_zones:
          description:
            - >-
              Availability zones for nodes. Must use VirtualMachineScaleSets
              AgentPoolType.
          returned: always
          type: list
          sample: null
        enable_node_public_ip:
          description:
            - Enable public IP for nodes
          returned: always
          type: bool
          sample: null
        scale_set_priority:
          description:
            - >-
              ScaleSetPriority to be used to specify virtual machine scale set
              priority. Default to regular.
          returned: always
          type: str
          sample: null
        scale_set_eviction_policy:
          description:
            - >-
              ScaleSetEvictionPolicy to be used to specify eviction policy for
              Spot virtual machine scale set. Default to Delete.
          returned: always
          type: str
          sample: null
        spot_max_price:
          description:
            - >-
              SpotMaxPrice to be used to specify the maximum price you are
              willing to pay in US Dollars. Possible values are any decimal
              value greater than zero or -1 which indicates default price to be
              up-to on-demand.
          returned: always
          type: number
          sample: null
        tags:
          description:
            - >-
              Agent pool tags to be persisted on the agent pool virtual machine
              scale set.
          returned: always
          type: dictionary
          sample: null
        node_labels:
          description:
            - >-
              Agent pool node labels to be persisted across all nodes in agent
              pool.
          returned: always
          type: dictionary
          sample: null
        node_taints:
          description:
            - >-
              Taints added to new nodes during node pool create and scale. For
              example, key=value:NoSchedule.
          returned: always
          type: list
          sample: null
        proximity_placement_group_id:
          description:
            - The ID for Proximity Placement Group.
          returned: always
          type: str
          sample: null
        max_surge:
          description:
            - >-
              Count or percentage of additional nodes to be added during
              upgrade. If empty uses AKS default
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of agent pool results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - |-
          Resource ID.
          Id of the agent pool upgrade profile.
          Id of the agent pool available versions.
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.

          Name of the agent pool upgrade profile.

          Name of the agent pool available versions.
      returned: always
      type: str
      sample: null
    type:
      description:
        - |-
          Resource type
          Type of the agent pool upgrade profile.
          Type of the agent pool  available versions.
      returned: always
      type: str
      sample: null
    count:
      description:
        - >-
          Number of agents (VMs) to host docker containers. Allowed values must
          be in the range of 0 to 100 (inclusive) for user pools and in the
          range of 1 to 100 (inclusive) for system pools. The default value is
          1.
      returned: always
      type: integer
      sample: null
    vm_size:
      description:
        - Size of agent VMs.
      returned: always
      type: str
      sample: null
    os_disk_size_gb:
      description:
        - >-
          OS Disk Size in GB to be used to specify the disk size for every
          machine in this master/agent pool. If you specify 0, it will apply the
          default osDisk size according to the vmSize specified.
      returned: always
      type: integer
      sample: null
    os_disk_type:
      description:
        - >-
          OS disk type to be used for machines in a given agent pool. Allowed
          values are 'Ephemeral' and 'Managed'. Defaults to 'Managed'. May not
          be changed after creation.
      returned: always
      type: str
      sample: null
    vnet_subnet_id:
      description:
        - VNet SubnetID specifies the VNet's subnet identifier.
      returned: always
      type: str
      sample: null
    max_pods:
      description:
        - Maximum number of pods that can run on a node.
      returned: always
      type: integer
      sample: null
    os_type:
      description:
        - >-
          OsType to be used to specify os type. Choose from Linux and Windows.
          Default to Linux.
      returned: always
      type: str
      sample: null
    max_count:
      description:
        - Maximum number of nodes for auto-scaling
      returned: always
      type: integer
      sample: null
    min_count:
      description:
        - Minimum number of nodes for auto-scaling
      returned: always
      type: integer
      sample: null
    enable_auto_scaling:
      description:
        - Whether to enable auto-scaler
      returned: always
      type: bool
      sample: null
    type_properties_type:
      description:
        - AgentPoolType represents types of an agent pool
      returned: always
      type: str
      sample: null
    mode:
      description:
        - AgentPoolMode represents mode of an agent pool
      returned: always
      type: str
      sample: null
    orchestrator_version:
      description:
        - Version of orchestrator specified when creating the managed cluster.
      returned: always
      type: str
      sample: null
    node_image_version:
      description:
        - Version of node image
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
    power_state:
      description:
        - Describes whether the Agent Pool is Running or Stopped
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - Tells whether the cluster is Running or Stopped
          returned: always
          type: str
          sample: null
    availability_zones:
      description:
        - >-
          Availability zones for nodes. Must use VirtualMachineScaleSets
          AgentPoolType.
      returned: always
      type: list
      sample: null
    enable_node_public_ip:
      description:
        - Enable public IP for nodes
      returned: always
      type: bool
      sample: null
    scale_set_priority:
      description:
        - >-
          ScaleSetPriority to be used to specify virtual machine scale set
          priority. Default to regular.
      returned: always
      type: str
      sample: null
    scale_set_eviction_policy:
      description:
        - >-
          ScaleSetEvictionPolicy to be used to specify eviction policy for Spot
          virtual machine scale set. Default to Delete.
      returned: always
      type: str
      sample: null
    spot_max_price:
      description:
        - >-
          SpotMaxPrice to be used to specify the maximum price you are willing
          to pay in US Dollars. Possible values are any decimal value greater
          than zero or -1 which indicates default price to be up-to on-demand.
      returned: always
      type: number
      sample: null
    tags:
      description:
        - >-
          Agent pool tags to be persisted on the agent pool virtual machine
          scale set.
      returned: always
      type: dictionary
      sample: null
    node_labels:
      description:
        - Agent pool node labels to be persisted across all nodes in agent pool.
      returned: always
      type: dictionary
      sample: null
    node_taints:
      description:
        - >-
          Taints added to new nodes during node pool create and scale. For
          example, key=value:NoSchedule.
      returned: always
      type: list
      sample: null
    proximity_placement_group_id:
      description:
        - The ID for Proximity Placement Group.
      returned: always
      type: str
      sample: null
    max_surge:
      description:
        - >-
          Count or percentage of additional nodes to be added during upgrade. If
          empty uses AKS default
      returned: always
      type: str
      sample: null
    kubernetes_version:
      description:
        - 'Kubernetes version (major, minor, patch).'
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
    latest_node_image_version:
      description:
        - LatestNodeImageVersion is the latest AKS supported node image version.
      returned: always
      type: str
      sample: null
    agent_pool_versions:
      description:
        - List of versions available for agent pool.
      returned: always
      type: list
      sample: null
      contains:
        default:
          description:
            - Whether this version is the default agent pool version.
          returned: always
          type: bool
          sample: null
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


class AzureRMAgentPoolInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            agent_pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.agent_pool_name = None

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
        super(AzureRMAgentPoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerServiceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01')

        if (self.resource_group_name is not None and
            self.resource_name is not None and
            self.agent_pool_name is not None):
            self.results['agent_pools'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.resource_name is not None and
              self.agent_pool_name is not None):
            self.results['agent_pools'] = self.format_item(self.getupgradeprofile())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['agent_pools'] = self.format_item(self.list())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['agent_pools'] = self.format_item(self.getavailableagentpoolversion())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.agent_pools.get(resource_group_name=self.resource_group_name,
                                                        resource_name=self.resource_name,
                                                        agent_pool_name=self.agent_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getupgradeprofile(self):
        response = None

        try:
            response = self.mgmt_client.agent_pools.get_upgrade_profile(resource_group_name=self.resource_group_name,
                                                                        resource_name=self.resource_name,
                                                                        agent_pool_name=self.agent_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.agent_pools.list(resource_group_name=self.resource_group_name,
                                                         resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getavailableagentpoolversion(self):
        response = None

        try:
            response = self.mgmt_client.agent_pools.get_available_agent_pool_version(resource_group_name=self.resource_group_name,
                                                                                     resource_name=self.resource_name)
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
    AzureRMAgentPoolInfo()


if __name__ == '__main__':
    main()
