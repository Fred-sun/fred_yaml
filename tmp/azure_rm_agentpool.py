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
module: azure_rm_agentpool
version_added: '2.9'
short_description: Manage Azure AgentPool instance.
description:
  - 'Create, update and delete instance of Azure AgentPool.'
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
    required: true
    type: str
  count:
    description:
      - >-
        Number of agents (VMs) to host docker containers. Allowed values must be
        in the range of 0 to 100 (inclusive) for user pools and in the range of
        1 to 100 (inclusive) for system pools. The default value is 1.
    type: integer
  vm_size:
    description:
      - Size of agent VMs.
    type: str
    choices:
      - Standard_A1
      - Standard_A10
      - Standard_A11
      - Standard_A1_v2
      - Standard_A2
      - Standard_A2_v2
      - Standard_A2m_v2
      - Standard_A3
      - Standard_A4
      - Standard_A4_v2
      - Standard_A4m_v2
      - Standard_A5
      - Standard_A6
      - Standard_A7
      - Standard_A8
      - Standard_A8_v2
      - Standard_A8m_v2
      - Standard_A9
      - Standard_B2ms
      - Standard_B2s
      - Standard_B4ms
      - Standard_B8ms
      - Standard_D1
      - Standard_D11
      - Standard_D11_v2
      - Standard_D11_v2_Promo
      - Standard_D12
      - Standard_D12_v2
      - Standard_D12_v2_Promo
      - Standard_D13
      - Standard_D13_v2
      - Standard_D13_v2_Promo
      - Standard_D14
      - Standard_D14_v2
      - Standard_D14_v2_Promo
      - Standard_D15_v2
      - Standard_D16_v3
      - Standard_D16s_v3
      - Standard_D1_v2
      - Standard_D2
      - Standard_D2_v2
      - Standard_D2_v2_Promo
      - Standard_D2_v3
      - Standard_D2s_v3
      - Standard_D3
      - Standard_D32_v3
      - Standard_D32s_v3
      - Standard_D3_v2
      - Standard_D3_v2_Promo
      - Standard_D4
      - Standard_D4_v2
      - Standard_D4_v2_Promo
      - Standard_D4_v3
      - Standard_D4s_v3
      - Standard_D5_v2
      - Standard_D5_v2_Promo
      - Standard_D64_v3
      - Standard_D64s_v3
      - Standard_D8_v3
      - Standard_D8s_v3
      - Standard_DS1
      - Standard_DS11
      - Standard_DS11_v2
      - Standard_DS11_v2_Promo
      - Standard_DS12
      - Standard_DS12_v2
      - Standard_DS12_v2_Promo
      - Standard_DS13
      - Standard_DS13-2_v2
      - Standard_DS13-4_v2
      - Standard_DS13_v2
      - Standard_DS13_v2_Promo
      - Standard_DS14
      - Standard_DS14-4_v2
      - Standard_DS14-8_v2
      - Standard_DS14_v2
      - Standard_DS14_v2_Promo
      - Standard_DS15_v2
      - Standard_DS1_v2
      - Standard_DS2
      - Standard_DS2_v2
      - Standard_DS2_v2_Promo
      - Standard_DS3
      - Standard_DS3_v2
      - Standard_DS3_v2_Promo
      - Standard_DS4
      - Standard_DS4_v2
      - Standard_DS4_v2_Promo
      - Standard_DS5_v2
      - Standard_DS5_v2_Promo
      - Standard_E16_v3
      - Standard_E16s_v3
      - Standard_E2_v3
      - Standard_E2s_v3
      - Standard_E32-16s_v3
      - Standard_E32-8s_v3
      - Standard_E32_v3
      - Standard_E32s_v3
      - Standard_E4_v3
      - Standard_E4s_v3
      - Standard_E64-16s_v3
      - Standard_E64-32s_v3
      - Standard_E64_v3
      - Standard_E64s_v3
      - Standard_E8_v3
      - Standard_E8s_v3
      - Standard_F1
      - Standard_F16
      - Standard_F16s
      - Standard_F16s_v2
      - Standard_F1s
      - Standard_F2
      - Standard_F2s
      - Standard_F2s_v2
      - Standard_F32s_v2
      - Standard_F4
      - Standard_F4s
      - Standard_F4s_v2
      - Standard_F64s_v2
      - Standard_F72s_v2
      - Standard_F8
      - Standard_F8s
      - Standard_F8s_v2
      - Standard_G1
      - Standard_G2
      - Standard_G3
      - Standard_G4
      - Standard_G5
      - Standard_GS1
      - Standard_GS2
      - Standard_GS3
      - Standard_GS4
      - Standard_GS4-4
      - Standard_GS4-8
      - Standard_GS5
      - Standard_GS5-16
      - Standard_GS5-8
      - Standard_H16
      - Standard_H16m
      - Standard_H16mr
      - Standard_H16r
      - Standard_H8
      - Standard_H8m
      - Standard_L16s
      - Standard_L32s
      - Standard_L4s
      - Standard_L8s
      - Standard_M128-32ms
      - Standard_M128-64ms
      - Standard_M128ms
      - Standard_M128s
      - Standard_M64-16ms
      - Standard_M64-32ms
      - Standard_M64ms
      - Standard_M64s
      - Standard_NC12
      - Standard_NC12s_v2
      - Standard_NC12s_v3
      - Standard_NC24
      - Standard_NC24r
      - Standard_NC24rs_v2
      - Standard_NC24rs_v3
      - Standard_NC24s_v2
      - Standard_NC24s_v3
      - Standard_NC6
      - Standard_NC6s_v2
      - Standard_NC6s_v3
      - Standard_ND12s
      - Standard_ND24rs
      - Standard_ND24s
      - Standard_ND6s
      - Standard_NV12
      - Standard_NV24
      - Standard_NV6
  os_disk_size_gb:
    description:
      - >-
        OS Disk Size in GB to be used to specify the disk size for every machine
        in this master/agent pool. If you specify 0, it will apply the default
        osDisk size according to the vmSize specified.
    type: integer
  os_disk_type:
    description:
      - >-
        OS disk type to be used for machines in a given agent pool. Allowed
        values are 'Ephemeral' and 'Managed'. Defaults to 'Managed'. May not be
        changed after creation.
    type: str
    choices:
      - Managed
      - Ephemeral
  vnet_subnet_id:
    description:
      - VNet SubnetID specifies the VNet's subnet identifier.
    type: str
  max_pods:
    description:
      - Maximum number of pods that can run on a node.
    type: integer
  os_type:
    description:
      - >-
        OsType to be used to specify os type. Choose from Linux and Windows.
        Default to Linux.
    type: str
    choices:
      - Linux
      - Windows
  max_count:
    description:
      - Maximum number of nodes for auto-scaling
    type: integer
  min_count:
    description:
      - Minimum number of nodes for auto-scaling
    type: integer
  enable_auto_scaling:
    description:
      - Whether to enable auto-scaler
    type: bool
  type:
    description:
      - AgentPoolType represents types of an agent pool
    type: str
    choices:
      - VirtualMachineScaleSets
      - AvailabilitySet
  mode:
    description:
      - AgentPoolMode represents mode of an agent pool
    type: str
    choices:
      - System
      - User
  orchestrator_version:
    description:
      - Version of orchestrator specified when creating the managed cluster.
    type: str
  availability_zones:
    description:
      - >-
        Availability zones for nodes. Must use VirtualMachineScaleSets
        AgentPoolType.
    type: list
  enable_node_public_ip:
    description:
      - Enable public IP for nodes
    type: bool
  scale_set_priority:
    description:
      - >-
        ScaleSetPriority to be used to specify virtual machine scale set
        priority. Default to regular.
    type: str
    choices:
      - Spot
      - Regular
  scale_set_eviction_policy:
    description:
      - >-
        ScaleSetEvictionPolicy to be used to specify eviction policy for Spot
        virtual machine scale set. Default to Delete.
    type: str
    choices:
      - Delete
      - Deallocate
  spot_max_price:
    description:
      - >-
        SpotMaxPrice to be used to specify the maximum price you are willing to
        pay in US Dollars. Possible values are any decimal value greater than
        zero or -1 which indicates default price to be up-to on-demand.
    type: number
  node_labels:
    description:
      - Agent pool node labels to be persisted across all nodes in agent pool.
    type: dictionary
  node_taints:
    description:
      - >-
        Taints added to new nodes during node pool create and scale. For
        example, key=value:NoSchedule.
    type: list
  proximity_placement_group_id:
    description:
      - The ID for Proximity Placement Group.
    type: str
  max_surge:
    description:
      - >-
        Count or percentage of additional nodes to be added during upgrade. If
        empty uses AKS default
    type: str
  state:
    description:
      - Assert the state of the AgentPool.
      - >-
        Use C(present) to create or update an AgentPool and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create Agent Pool with Ephemeral OS Disk
      azure_rm_agentpool: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        properties:
          count: 3
          orchestrator_version: ''
          os_disk_size_gb: 64
          os_disk_type: Ephemeral
          os_type: Linux
          vm_size: Standard_DS2_v2
        

    - name: Create Agent Pool with PPG
      azure_rm_agentpool: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        properties:
          count: 3
          orchestrator_version: ''
          os_type: Linux
          proximity_placement_group_id: >-
            /subscriptions/subid1/resourcegroups/rg1/providers//Microsoft.Compute/proximityPlacementGroups/ppg1
          vm_size: Standard_DS2_v2
        

    - name: Create Spot Agent Pool
      azure_rm_agentpool: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        properties:
          count: 3
          node_labels:
            key1: val1
          node_taints:
            - 'Key1=Value1:NoSchedule'
          orchestrator_version: ''
          os_type: Linux
          scale_set_eviction_policy: Delete
          scale_set_priority: Spot
          tags:
            name1: val1
          vm_size: Standard_DS1_v2
        

    - name: Create/Update Agent Pool
      azure_rm_agentpool: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        properties:
          count: 3
          mode: User
          node_labels:
            key1: val1
          node_taints:
            - 'Key1=Value1:NoSchedule'
          orchestrator_version: ''
          os_type: Linux
          scale_set_eviction_policy: Delete
          scale_set_priority: Spot
          tags:
            name1: val1
          vm_size: Standard_DS1_v2
        

    - name: Update Agent Pool
      azure_rm_agentpool: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        properties:
          count: 3
          enable_auto_scaling: true
          max_count: 2
          min_count: 2
          node_taints:
            - 'Key1=Value1:NoSchedule'
          orchestrator_version: ''
          os_type: Linux
          scale_set_eviction_policy: Delete
          scale_set_priority: Spot
          vm_size: Standard_DS1_v2
        

    - name: Delete Agent Pool
      azure_rm_agentpool: 
        agent_pool_name: agentpool1
        resource_group_name: rg1
        resource_name: clustername1
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - >-
      The name of the resource that is unique within a resource group. This name
      can be used to access the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
count:
  description:
    - >-
      Number of agents (VMs) to host docker containers. Allowed values must be
      in the range of 0 to 100 (inclusive) for user pools and in the range of 1
      to 100 (inclusive) for system pools. The default value is 1.
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
      OS Disk Size in GB to be used to specify the disk size for every machine
      in this master/agent pool. If you specify 0, it will apply the default
      osDisk size according to the vmSize specified.
  returned: always
  type: integer
  sample: null
os_disk_type:
  description:
    - >-
      OS disk type to be used for machines in a given agent pool. Allowed values
      are 'Ephemeral' and 'Managed'. Defaults to 'Managed'. May not be changed
      after creation.
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
      The current deployment or provisioning state, which only appears in the
      response.
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
      ScaleSetPriority to be used to specify virtual machine scale set priority.
      Default to regular.
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
      SpotMaxPrice to be used to specify the maximum price you are willing to
      pay in US Dollars. Possible values are any decimal value greater than zero
      or -1 which indicates default price to be up-to on-demand.
  returned: always
  type: number
  sample: null
tags:
  description:
    - >-
      Agent pool tags to be persisted on the agent pool virtual machine scale
      set.
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
      Taints added to new nodes during node pool create and scale. For example,
      key=value:NoSchedule.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.container import ContainerServiceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAgentPool(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            count=dict(
                type='integer',
                disposition='/count'
            ),
            vm_size=dict(
                type='str',
                disposition='/vm_size',
                choices=['Standard_A1',
                         'Standard_A10',
                         'Standard_A11',
                         'Standard_A1_v2',
                         'Standard_A2',
                         'Standard_A2_v2',
                         'Standard_A2m_v2',
                         'Standard_A3',
                         'Standard_A4',
                         'Standard_A4_v2',
                         'Standard_A4m_v2',
                         'Standard_A5',
                         'Standard_A6',
                         'Standard_A7',
                         'Standard_A8',
                         'Standard_A8_v2',
                         'Standard_A8m_v2',
                         'Standard_A9',
                         'Standard_B2ms',
                         'Standard_B2s',
                         'Standard_B4ms',
                         'Standard_B8ms',
                         'Standard_D1',
                         'Standard_D11',
                         'Standard_D11_v2',
                         'Standard_D11_v2_Promo',
                         'Standard_D12',
                         'Standard_D12_v2',
                         'Standard_D12_v2_Promo',
                         'Standard_D13',
                         'Standard_D13_v2',
                         'Standard_D13_v2_Promo',
                         'Standard_D14',
                         'Standard_D14_v2',
                         'Standard_D14_v2_Promo',
                         'Standard_D15_v2',
                         'Standard_D16_v3',
                         'Standard_D16s_v3',
                         'Standard_D1_v2',
                         'Standard_D2',
                         'Standard_D2_v2',
                         'Standard_D2_v2_Promo',
                         'Standard_D2_v3',
                         'Standard_D2s_v3',
                         'Standard_D3',
                         'Standard_D32_v3',
                         'Standard_D32s_v3',
                         'Standard_D3_v2',
                         'Standard_D3_v2_Promo',
                         'Standard_D4',
                         'Standard_D4_v2',
                         'Standard_D4_v2_Promo',
                         'Standard_D4_v3',
                         'Standard_D4s_v3',
                         'Standard_D5_v2',
                         'Standard_D5_v2_Promo',
                         'Standard_D64_v3',
                         'Standard_D64s_v3',
                         'Standard_D8_v3',
                         'Standard_D8s_v3',
                         'Standard_DS1',
                         'Standard_DS11',
                         'Standard_DS11_v2',
                         'Standard_DS11_v2_Promo',
                         'Standard_DS12',
                         'Standard_DS12_v2',
                         'Standard_DS12_v2_Promo',
                         'Standard_DS13',
                         'Standard_DS13-2_v2',
                         'Standard_DS13-4_v2',
                         'Standard_DS13_v2',
                         'Standard_DS13_v2_Promo',
                         'Standard_DS14',
                         'Standard_DS14-4_v2',
                         'Standard_DS14-8_v2',
                         'Standard_DS14_v2',
                         'Standard_DS14_v2_Promo',
                         'Standard_DS15_v2',
                         'Standard_DS1_v2',
                         'Standard_DS2',
                         'Standard_DS2_v2',
                         'Standard_DS2_v2_Promo',
                         'Standard_DS3',
                         'Standard_DS3_v2',
                         'Standard_DS3_v2_Promo',
                         'Standard_DS4',
                         'Standard_DS4_v2',
                         'Standard_DS4_v2_Promo',
                         'Standard_DS5_v2',
                         'Standard_DS5_v2_Promo',
                         'Standard_E16_v3',
                         'Standard_E16s_v3',
                         'Standard_E2_v3',
                         'Standard_E2s_v3',
                         'Standard_E32-16s_v3',
                         'Standard_E32-8s_v3',
                         'Standard_E32_v3',
                         'Standard_E32s_v3',
                         'Standard_E4_v3',
                         'Standard_E4s_v3',
                         'Standard_E64-16s_v3',
                         'Standard_E64-32s_v3',
                         'Standard_E64_v3',
                         'Standard_E64s_v3',
                         'Standard_E8_v3',
                         'Standard_E8s_v3',
                         'Standard_F1',
                         'Standard_F16',
                         'Standard_F16s',
                         'Standard_F16s_v2',
                         'Standard_F1s',
                         'Standard_F2',
                         'Standard_F2s',
                         'Standard_F2s_v2',
                         'Standard_F32s_v2',
                         'Standard_F4',
                         'Standard_F4s',
                         'Standard_F4s_v2',
                         'Standard_F64s_v2',
                         'Standard_F72s_v2',
                         'Standard_F8',
                         'Standard_F8s',
                         'Standard_F8s_v2',
                         'Standard_G1',
                         'Standard_G2',
                         'Standard_G3',
                         'Standard_G4',
                         'Standard_G5',
                         'Standard_GS1',
                         'Standard_GS2',
                         'Standard_GS3',
                         'Standard_GS4',
                         'Standard_GS4-4',
                         'Standard_GS4-8',
                         'Standard_GS5',
                         'Standard_GS5-16',
                         'Standard_GS5-8',
                         'Standard_H16',
                         'Standard_H16m',
                         'Standard_H16mr',
                         'Standard_H16r',
                         'Standard_H8',
                         'Standard_H8m',
                         'Standard_L16s',
                         'Standard_L32s',
                         'Standard_L4s',
                         'Standard_L8s',
                         'Standard_M128-32ms',
                         'Standard_M128-64ms',
                         'Standard_M128ms',
                         'Standard_M128s',
                         'Standard_M64-16ms',
                         'Standard_M64-32ms',
                         'Standard_M64ms',
                         'Standard_M64s',
                         'Standard_NC12',
                         'Standard_NC12s_v2',
                         'Standard_NC12s_v3',
                         'Standard_NC24',
                         'Standard_NC24r',
                         'Standard_NC24rs_v2',
                         'Standard_NC24rs_v3',
                         'Standard_NC24s_v2',
                         'Standard_NC24s_v3',
                         'Standard_NC6',
                         'Standard_NC6s_v2',
                         'Standard_NC6s_v3',
                         'Standard_ND12s',
                         'Standard_ND24rs',
                         'Standard_ND24s',
                         'Standard_ND6s',
                         'Standard_NV12',
                         'Standard_NV24',
                         'Standard_NV6']
            ),
            os_disk_size_gb=dict(
                type='integer',
                disposition='/os_disk_size_gb'
            ),
            os_disk_type=dict(
                type='str',
                disposition='/os_disk_type',
                choices=['Managed',
                         'Ephemeral']
            ),
            vnet_subnet_id=dict(
                type='str',
                disposition='/vnet_subnet_id'
            ),
            max_pods=dict(
                type='integer',
                disposition='/max_pods'
            ),
            os_type=dict(
                type='str',
                disposition='/os_type',
                choices=['Linux',
                         'Windows']
            ),
            max_count=dict(
                type='integer',
                disposition='/max_count'
            ),
            min_count=dict(
                type='integer',
                disposition='/min_count'
            ),
            enable_auto_scaling=dict(
                type='bool',
                disposition='/enable_auto_scaling'
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['VirtualMachineScaleSets',
                         'AvailabilitySet']
            ),
            mode=dict(
                type='str',
                disposition='/mode',
                choices=['System',
                         'User']
            ),
            orchestrator_version=dict(
                type='str',
                disposition='/orchestrator_version'
            ),
            availability_zones=dict(
                type='list',
                disposition='/availability_zones',
                elements='str'
            ),
            enable_node_public_ip=dict(
                type='bool',
                disposition='/enable_node_public_ip'
            ),
            scale_set_priority=dict(
                type='str',
                disposition='/scale_set_priority',
                choices=['Spot',
                         'Regular']
            ),
            scale_set_eviction_policy=dict(
                type='str',
                disposition='/scale_set_eviction_policy',
                choices=['Delete',
                         'Deallocate']
            ),
            spot_max_price=dict(
                type='number',
                disposition='/spot_max_price'
            ),
            node_labels=dict(
                type='dictionary',
                disposition='/node_labels'
            ),
            node_taints=dict(
                type='list',
                disposition='/node_taints',
                elements='str'
            ),
            proximity_placement_group_id=dict(
                type='str',
                disposition='/proximity_placement_group_id'
            ),
            max_surge=dict(
                type='str',
                disposition='/max_surge'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.agent_pool_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAgentPool, self).__init__(derived_arg_spec=self.module_arg_spec,
                                               supports_check_mode=True,
                                               supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(ContainerServiceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.agent_pools.create_or_update(resource_group_name=self.resource_group_name,
                                                                     resource_name=self.resource_name,
                                                                     agent_pool_name=self.agent_pool_name,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AgentPool instance.')
            self.fail('Error creating the AgentPool instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.agent_pools.delete(resource_group_name=self.resource_group_name,
                                                           resource_name=self.resource_name,
                                                           agent_pool_name=self.agent_pool_name)
        except CloudError as e:
            self.log('Error attempting to delete the AgentPool instance.')
            self.fail('Error deleting the AgentPool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.agent_pools.get(resource_group_name=self.resource_group_name,
                                                        resource_name=self.resource_name,
                                                        agent_pool_name=self.agent_pool_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAgentPool()


if __name__ == '__main__':
    main()
