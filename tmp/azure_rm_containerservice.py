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
module: azure_rm_containerservice
version_added: '2.9'
short_description: Manage Azure ContainerService instance.
description:
  - 'Create, update and delete instance of Azure ContainerService.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  container_service_name:
    description:
      - >-
        The name of the container service in the specified subscription and
        resource group.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  orchestrator_profile:
    description:
      - Profile for the container service orchestrator.
    type: dict
    suboptions:
      orchestrator_type:
        description:
          - >-
            The orchestrator to use to manage container service cluster
            resources. Valid values are Kubernetes, Swarm, DCOS, DockerCE and
            Custom.
        required: true
        type: str
        choices:
          - Kubernetes
          - Swarm
          - DCOS
          - DockerCE
          - Custom
      orchestrator_version:
        description:
          - >-
            The version of the orchestrator to use. You can specify the
            major.minor.patch part of the actual version.For example, you can
            specify version as "1.6.11".
        type: str
  custom_profile:
    description:
      - Properties to configure a custom container service cluster.
    type: dict
    suboptions:
      orchestrator:
        description:
          - The name of the custom orchestrator to use.
        required: true
        type: str
  service_principal_profile:
    description:
      - >-
        Information about a service principal identity for the cluster to use
        for manipulating Azure APIs. Exact one of secret or keyVaultSecretRef
        need to be specified.
    type: dict
    suboptions:
      client_id:
        description:
          - The ID for the service principal.
        required: true
        type: str
      secret:
        description:
          - >-
            The secret password associated with the service principal in plain
            text.
        type: str
      key_vault_secret_ref:
        description:
          - Reference to a secret stored in Azure Key Vault.
        type: dict
        suboptions:
          vault_id:
            description:
              - Key vault identifier.
            required: true
            type: str
          secret_name:
            description:
              - The secret name.
            required: true
            type: str
          version:
            description:
              - The secret version.
            type: str
  master_profile:
    description:
      - Profile for the container service master.
    type: dict
    suboptions:
      count:
        description:
          - >-
            Number of masters (VMs) in the container service cluster. Allowed
            values are 1, 3, and 5. The default value is 1.
        type: sealed-choice
      dns_prefix:
        description:
          - DNS prefix to be used to create the FQDN for the master pool.
        required: true
        type: str
      vm_size:
        description:
          - Size of agent VMs.
        required: true
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
            OS Disk Size in GB to be used to specify the disk size for every
            machine in this master/agent pool. If you specify 0, it will apply
            the default osDisk size according to the vmSize specified.
        type: integer
      vnet_subnet_id:
        description:
          - VNet SubnetID specifies the VNet's subnet identifier.
        type: str
      first_consecutive_static_ip:
        description:
          - >-
            FirstConsecutiveStaticIP used to specify the first static ip of
            masters.
        type: str
      storage_profile:
        description:
          - >-
            Storage profile specifies what kind of storage used. Choose from
            StorageAccount and ManagedDisks. Leave it empty, we will choose for
            you based on the orchestrator choice.
        type: str
        choices:
          - StorageAccount
          - ManagedDisks
      fqdn:
        description:
          - FQDN for the master pool.
        type: str
  agent_pool_profiles:
    description:
      - Properties of the agent pool.
    type: list
    suboptions:
      name:
        description:
          - >-
            Unique name of the agent pool profile in the context of the
            subscription and resource group.
        required: true
        type: str
      count:
        description:
          - >-
            Number of agents (VMs) to host docker containers. Allowed values
            must be in the range of 1 to 100 (inclusive). The default value is
            1. 
        type: integer
      vm_size:
        description:
          - Size of agent VMs.
        required: true
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
            OS Disk Size in GB to be used to specify the disk size for every
            machine in this master/agent pool. If you specify 0, it will apply
            the default osDisk size according to the vmSize specified.
        type: integer
      dns_prefix:
        description:
          - DNS prefix to be used to create the FQDN for the agent pool.
        type: str
      fqdn:
        description:
          - FQDN for the agent pool.
        type: str
      ports:
        description:
          - >-
            Ports number array used to expose on this agent pool. The default
            opened ports are different based on your choice of orchestrator.
        type: list
      storage_profile:
        description:
          - >-
            Storage profile specifies what kind of storage used. Choose from
            StorageAccount and ManagedDisks. Leave it empty, we will choose for
            you based on the orchestrator choice.
        type: str
        choices:
          - StorageAccount
          - ManagedDisks
      vnet_subnet_id:
        description:
          - VNet SubnetID specifies the VNet's subnet identifier.
        type: str
      os_type:
        description:
          - >-
            OsType to be used to specify os type. Choose from Linux and Windows.
            Default to Linux.
        type: str
        choices:
          - Linux
          - Windows
  windows_profile:
    description:
      - Profile for Windows VMs in the container service cluster.
    type: dict
    suboptions:
      admin_username:
        description:
          - The administrator username to use for Windows VMs.
        required: true
        type: str
      admin_password:
        description:
          - The administrator password to use for Windows VMs.
        required: true
        type: str
  linux_profile:
    description:
      - Profile for Linux VMs in the container service cluster.
    type: dict
    suboptions:
      admin_username:
        description:
          - The administrator username to use for Linux VMs.
        required: true
        type: str
      ssh:
        description:
          - SSH configuration for Linux-based VMs running on Azure.
        required: true
        type: dict
        suboptions:
          public_keys:
            description:
              - >-
                The list of SSH public keys used to authenticate with
                Linux-based VMs. Only expect one key specified.
            required: true
            type: list
            suboptions:
              key_data:
                description:
                  - >-
                    Certificate public key used to authenticate with VMs through
                    SSH. The certificate must be in PEM format with or without
                    headers.
                required: true
                type: str
  diagnostics_profile:
    description:
      - Profile for diagnostics in the container service cluster.
    type: dict
    suboptions:
      vm_diagnostics:
        description:
          - Profile for diagnostics on the container service VMs.
        required: true
        type: dict
        suboptions:
          enabled:
            description:
              - Whether the VM diagnostic agent is provisioned on the VM.
            required: true
            type: bool
          storage_uri:
            description:
              - The URI of the storage account where diagnostics are stored.
            type: str
  state:
    description:
      - Assert the state of the ContainerService.
      - >-
        Use C(present) to create or update an ContainerService and C(absent) to
        delete it.
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
    - name: Create/Update Container Service
      azure_rm_containerservice: 
        container_service_name: acs1
        resource_group_name: rg1
        location: location1
        

    - name: Delete Container Service
      azure_rm_containerservice: 
        container_service_name: acs1
        resource_group_name: rg1
        

'''

RETURN = '''
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
provisioning_state:
  description:
    - >-
      The current deployment or provisioning state, which only appears in the
      response.
  returned: always
  type: str
  sample: null
orchestrator_profile:
  description:
    - Profile for the container service orchestrator.
  returned: always
  type: dict
  sample: null
  contains:
    orchestrator_type:
      description:
        - >-
          The orchestrator to use to manage container service cluster resources.
          Valid values are Kubernetes, Swarm, DCOS, DockerCE and Custom.
      returned: always
      type: str
      sample: null
    orchestrator_version:
      description:
        - >-
          The version of the orchestrator to use. You can specify the
          major.minor.patch part of the actual version.For example, you can
          specify version as "1.6.11".
      returned: always
      type: str
      sample: null
custom_profile:
  description:
    - Properties to configure a custom container service cluster.
  returned: always
  type: dict
  sample: null
  contains:
    orchestrator:
      description:
        - The name of the custom orchestrator to use.
      returned: always
      type: str
      sample: null
service_principal_profile:
  description:
    - >-
      Information about a service principal identity for the cluster to use for
      manipulating Azure APIs. Exact one of secret or keyVaultSecretRef need to
      be specified.
  returned: always
  type: dict
  sample: null
  contains:
    client_id:
      description:
        - The ID for the service principal.
      returned: always
      type: str
      sample: null
    secret:
      description:
        - >-
          The secret password associated with the service principal in plain
          text.
      returned: always
      type: str
      sample: null
    key_vault_secret_ref:
      description:
        - Reference to a secret stored in Azure Key Vault.
      returned: always
      type: dict
      sample: null
      contains:
        vault_id:
          description:
            - Key vault identifier.
          returned: always
          type: str
          sample: null
        secret_name:
          description:
            - The secret name.
          returned: always
          type: str
          sample: null
        version:
          description:
            - The secret version.
          returned: always
          type: str
          sample: null
master_profile:
  description:
    - Profile for the container service master.
  returned: always
  type: dict
  sample: null
  contains:
    count:
      description:
        - >-
          Number of masters (VMs) in the container service cluster. Allowed
          values are 1, 3, and 5. The default value is 1.
      returned: always
      type: sealed-choice
      sample: null
    dns_prefix:
      description:
        - DNS prefix to be used to create the FQDN for the master pool.
      returned: always
      type: str
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
    vnet_subnet_id:
      description:
        - VNet SubnetID specifies the VNet's subnet identifier.
      returned: always
      type: str
      sample: null
    first_consecutive_static_ip:
      description:
        - >-
          FirstConsecutiveStaticIP used to specify the first static ip of
          masters.
      returned: always
      type: str
      sample: null
    storage_profile:
      description:
        - >-
          Storage profile specifies what kind of storage used. Choose from
          StorageAccount and ManagedDisks. Leave it empty, we will choose for
          you based on the orchestrator choice.
      returned: always
      type: str
      sample: null
    fqdn:
      description:
        - FQDN for the master pool.
      returned: always
      type: str
      sample: null
agent_pool_profiles:
  description:
    - Properties of the agent pool.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - >-
          Unique name of the agent pool profile in the context of the
          subscription and resource group.
      returned: always
      type: str
      sample: null
    count:
      description:
        - >-
          Number of agents (VMs) to host docker containers. Allowed values must
          be in the range of 1 to 100 (inclusive). The default value is 1. 
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
    dns_prefix:
      description:
        - DNS prefix to be used to create the FQDN for the agent pool.
      returned: always
      type: str
      sample: null
    fqdn:
      description:
        - FQDN for the agent pool.
      returned: always
      type: str
      sample: null
    ports:
      description:
        - >-
          Ports number array used to expose on this agent pool. The default
          opened ports are different based on your choice of orchestrator.
      returned: always
      type: list
      sample: null
    storage_profile:
      description:
        - >-
          Storage profile specifies what kind of storage used. Choose from
          StorageAccount and ManagedDisks. Leave it empty, we will choose for
          you based on the orchestrator choice.
      returned: always
      type: str
      sample: null
    vnet_subnet_id:
      description:
        - VNet SubnetID specifies the VNet's subnet identifier.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - >-
          OsType to be used to specify os type. Choose from Linux and Windows.
          Default to Linux.
      returned: always
      type: str
      sample: null
windows_profile:
  description:
    - Profile for Windows VMs in the container service cluster.
  returned: always
  type: dict
  sample: null
  contains:
    admin_username:
      description:
        - The administrator username to use for Windows VMs.
      returned: always
      type: str
      sample: null
    admin_password:
      description:
        - The administrator password to use for Windows VMs.
      returned: always
      type: str
      sample: null
linux_profile:
  description:
    - Profile for Linux VMs in the container service cluster.
  returned: always
  type: dict
  sample: null
  contains:
    admin_username:
      description:
        - The administrator username to use for Linux VMs.
      returned: always
      type: str
      sample: null
    ssh:
      description:
        - SSH configuration for Linux-based VMs running on Azure.
      returned: always
      type: dict
      sample: null
      contains:
        public_keys:
          description:
            - >-
              The list of SSH public keys used to authenticate with Linux-based
              VMs. Only expect one key specified.
          returned: always
          type: list
          sample: null
          contains:
            key_data:
              description:
                - >-
                  Certificate public key used to authenticate with VMs through
                  SSH. The certificate must be in PEM format with or without
                  headers.
              returned: always
              type: str
              sample: null
diagnostics_profile:
  description:
    - Profile for diagnostics in the container service cluster.
  returned: always
  type: dict
  sample: null
  contains:
    vm_diagnostics:
      description:
        - Profile for diagnostics on the container service VMs.
      returned: always
      type: dict
      sample: null
      contains:
        enabled:
          description:
            - Whether the VM diagnostic agent is provisioned on the VM.
          returned: always
          type: bool
          sample: null
        storage_uri:
          description:
            - The URI of the storage account where diagnostics are stored.
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


class AzureRMContainerService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            container_service_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            orchestrator_profile=dict(
                type='dict',
                disposition='/orchestrator_profile',
                options=dict(
                    orchestrator_type=dict(
                        type='str',
                        disposition='orchestrator_type',
                        choices=['Kubernetes',
                                 'Swarm',
                                 'DCOS',
                                 'DockerCE',
                                 'Custom'],
                        required=True
                    ),
                    orchestrator_version=dict(
                        type='str',
                        disposition='orchestrator_version'
                    )
                )
            ),
            custom_profile=dict(
                type='dict',
                disposition='/custom_profile',
                options=dict(
                    orchestrator=dict(
                        type='str',
                        disposition='orchestrator',
                        required=True
                    )
                )
            ),
            service_principal_profile=dict(
                type='dict',
                disposition='/service_principal_profile',
                options=dict(
                    client_id=dict(
                        type='str',
                        disposition='client_id',
                        required=True
                    ),
                    secret=dict(
                        type='str',
                        disposition='secret'
                    ),
                    key_vault_secret_ref=dict(
                        type='dict',
                        disposition='key_vault_secret_ref',
                        options=dict(
                            vault_id=dict(
                                type='str',
                                disposition='vault_id',
                                required=True
                            ),
                            secret_name=dict(
                                type='str',
                                disposition='secret_name',
                                required=True
                            ),
                            version=dict(
                                type='str',
                                disposition='version'
                            )
                        )
                    )
                )
            ),
            master_profile=dict(
                type='dict',
                disposition='/master_profile',
                options=dict(
                    count=dict(
                        type='sealed-choice',
                        disposition='count'
                    ),
                    dns_prefix=dict(
                        type='str',
                        disposition='dns_prefix',
                        required=True
                    ),
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
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
                                 'Standard_NV6'],
                        required=True
                    ),
                    os_disk_size_gb=dict(
                        type='integer',
                        disposition='os_disk_size_gb'
                    ),
                    vnet_subnet_id=dict(
                        type='str',
                        disposition='vnet_subnet_id'
                    ),
                    first_consecutive_static_ip=dict(
                        type='str',
                        disposition='first_consecutive_static_ip'
                    ),
                    storage_profile=dict(
                        type='str',
                        disposition='storage_profile',
                        choices=['StorageAccount',
                                 'ManagedDisks']
                    ),
                    fqdn=dict(
                        type='str',
                        updatable=False,
                        disposition='fqdn'
                    )
                )
            ),
            agent_pool_profiles=dict(
                type='list',
                disposition='/agent_pool_profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    count=dict(
                        type='integer',
                        disposition='count'
                    ),
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
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
                                 'Standard_NV6'],
                        required=True
                    ),
                    os_disk_size_gb=dict(
                        type='integer',
                        disposition='os_disk_size_gb'
                    ),
                    dns_prefix=dict(
                        type='str',
                        disposition='dns_prefix'
                    ),
                    fqdn=dict(
                        type='str',
                        updatable=False,
                        disposition='fqdn'
                    ),
                    ports=dict(
                        type='list',
                        disposition='ports',
                        elements='integer'
                    ),
                    storage_profile=dict(
                        type='str',
                        disposition='storage_profile',
                        choices=['StorageAccount',
                                 'ManagedDisks']
                    ),
                    vnet_subnet_id=dict(
                        type='str',
                        disposition='vnet_subnet_id'
                    ),
                    os_type=dict(
                        type='str',
                        disposition='os_type',
                        choices=['Linux',
                                 'Windows']
                    )
                )
            ),
            windows_profile=dict(
                type='dict',
                disposition='/windows_profile',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='admin_username',
                        required=True
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='admin_password',
                        required=True
                    )
                )
            ),
            linux_profile=dict(
                type='dict',
                disposition='/linux_profile',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='admin_username',
                        required=True
                    ),
                    ssh=dict(
                        type='dict',
                        disposition='ssh',
                        required=True,
                        options=dict(
                            public_keys=dict(
                                type='list',
                                disposition='public_keys',
                                required=True,
                                elements='dict',
                                options=dict(
                                    key_data=dict(
                                        type='str',
                                        disposition='key_data',
                                        required=True
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/diagnostics_profile',
                options=dict(
                    vm_diagnostics=dict(
                        type='dict',
                        disposition='vm_diagnostics',
                        required=True,
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled',
                                required=True
                            ),
                            storage_uri=dict(
                                type='str',
                                updatable=False,
                                disposition='storage_uri'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.container_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContainerService, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-07-01')

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
            response = self.mgmt_client.container_services.create_or_update(resource_group_name=self.resource_group_name,
                                                                            container_service_name=self.container_service_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ContainerService instance.')
            self.fail('Error creating the ContainerService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.container_services.delete(resource_group_name=self.resource_group_name,
                                                                  container_service_name=self.container_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the ContainerService instance.')
            self.fail('Error deleting the ContainerService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.container_services.get(resource_group_name=self.resource_group_name,
                                                               container_service_name=self.container_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContainerService()


if __name__ == '__main__':
    main()
