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
module: azure_rm_managedcluster
version_added: '2.9'
short_description: Manage Azure ManagedCluster instance.
description:
  - 'Create, update and delete instance of Azure ManagedCluster.'
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
  location:
    description:
      - Resource location
    type: str
  type:
    description:
      - >-
        The type of identity used for the managed cluster. Type 'SystemAssigned'
        will use an implicitly created identity in master components and an
        auto-created user assigned identity in MC_ resource group in agent
        nodes. Type 'None' will not use MSI for the managed cluster, service
        principal will be used instead.
    type: sealed-choice
  user_assigned_identities:
    description:
      - >-
        The user identity associated with the managed cluster. This identity
        will be used in control plane and only one user assigned identity is
        allowed. The user identity dictionary key references will be ARM
        resource ids in the form:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    type: dictionary
  kubernetes_version:
    description:
      - Version of Kubernetes specified when creating the managed cluster.
    type: str
  dns_prefix:
    description:
      - DNS prefix specified when creating the managed cluster.
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
        type: str
      license_type:
        description:
          - >-
            The licenseType to use for Windows VMs. Windows_Server is used to
            enable Azure Hybrid User Benefits for Windows VMs.
        type: str
        choices:
          - None
          - Windows_Server
  service_principal_profile:
    description:
      - >-
        Information about a service principal identity for the cluster to use
        for manipulating Azure APIs.
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
  addon_profiles:
    description:
      - Profile of managed cluster add-on.
    type: dictionary
  node_resource_group:
    description:
      - Name of the resource group containing agent pool nodes.
    type: str
  enable_rbac:
    description:
      - Whether to enable Kubernetes Role-Based Access Control.
    type: bool
  enable_pod_security_policy:
    description:
      - >-
        (DEPRECATING) Whether to enable Kubernetes pod security policy
        (preview). This feature is set for removal on October 15th, 2020. Learn
        more at aka.ms/aks/azpodpolicy.
    type: bool
  network_profile:
    description:
      - Profile of network configuration.
    type: dict
    suboptions:
      network_plugin:
        description:
          - Network plugin used for building Kubernetes network.
        type: str
        choices:
          - azure
          - kubenet
      network_policy:
        description:
          - Network policy used for building Kubernetes network.
        type: str
        choices:
          - calico
          - azure
      network_mode:
        description:
          - Network mode used for building Kubernetes network.
        type: str
        choices:
          - transparent
          - bridge
      pod_cidr:
        description:
          - >-
            A CIDR notation IP range from which to assign pod IPs when kubenet
            is used.
        type: str
      service_cidr:
        description:
          - >-
            A CIDR notation IP range from which to assign service cluster IPs.
            It must not overlap with any Subnet IP ranges.
        type: str
      dns_service_ip:
        description:
          - >-
            An IP address assigned to the Kubernetes DNS service. It must be
            within the Kubernetes service address range specified in
            serviceCidr.
        type: str
      docker_bridge_cidr:
        description:
          - >-
            A CIDR notation IP range assigned to the Docker bridge network. It
            must not overlap with any Subnet IP ranges or the Kubernetes service
            address range.
        type: str
      outbound_type:
        description:
          - The outbound (egress) routing method.
        type: str
        choices:
          - loadBalancer
          - userDefinedRouting
      load_balancer_sku:
        description:
          - The load balancer sku for the managed cluster.
        type: str
        choices:
          - standard
          - basic
      load_balancer_profile:
        description:
          - Profile of the cluster load balancer.
        type: dict
        suboptions:
          managed_outbound_ips:
            description:
              - Desired managed outbound IPs for the cluster load balancer.
            type: dict
            suboptions:
              count:
                description:
                  - >-
                    Desired number of outbound IP created/managed by Azure for
                    the cluster load balancer. Allowed values must be in the
                    range of 1 to 100 (inclusive). The default value is 1. 
                type: integer
          outbound_ip_prefixes:
            description:
              - >-
                Desired outbound IP Prefix resources for the cluster load
                balancer.
            type: dict
            suboptions:
              public_ip_prefixes:
                description:
                  - A list of public IP prefix resources.
                type: list
                suboptions:
                  id:
                    description:
                      - The fully qualified Azure resource id.
                    type: str
          outbound_ips:
            description:
              - Desired outbound IP resources for the cluster load balancer.
            type: dict
            suboptions:
              public_ips:
                description:
                  - A list of public IP resources.
                type: list
                suboptions:
                  id:
                    description:
                      - The fully qualified Azure resource id.
                    type: str
          effective_outbound_ips:
            description:
              - >-
                The effective outbound IP resources of the cluster load
                balancer.
            type: list
            suboptions:
              id:
                description:
                  - The fully qualified Azure resource id.
                type: str
          allocated_outbound_ports:
            description:
              - >-
                Desired number of allocated SNAT ports per VM. Allowed values
                must be in the range of 0 to 64000 (inclusive). The default
                value is 0 which results in Azure dynamically allocating ports.
            type: integer
          idle_timeout_in_minutes:
            description:
              - >-
                Desired outbound flow idle timeout in minutes. Allowed values
                must be in the range of 4 to 120 (inclusive). The default value
                is 30 minutes.
            type: integer
  aadprofile:
    description:
      - Profile of Azure Active Directory configuration.
    type: dict
    suboptions:
      managed:
        description:
          - Whether to enable managed AAD.
        type: bool
      enable_azure_rbac:
        description:
          - Whether to enable Azure RBAC for Kubernetes authorization.
        type: bool
      admin_group_object_ids:
        description:
          - AAD group object IDs that will have admin role of the cluster.
        type: list
      client_app_id:
        description:
          - The client AAD application ID.
        type: str
      server_app_id:
        description:
          - The server AAD application ID.
        type: str
      server_app_secret:
        description:
          - The server AAD application secret.
        type: str
      tenant_id:
        description:
          - >-
            The AAD tenant ID to use for authentication. If not specified, will
            use the tenant of the deployment subscription.
        type: str
  auto_scaler_profile:
    description:
      - Parameters to be applied to the cluster-autoscaler when enabled
    type: dict
    suboptions:
      balance_similar_node_groups:
        description:
          - undefined
        type: str
      expander:
        description:
          - undefined
        type: str
        choices:
          - least-waste
          - most-pods
          - random
      max_empty_bulk_delete:
        description:
          - undefined
        type: str
      max_graceful_termination_sec:
        description:
          - undefined
        type: str
      max_total_unready_percentage:
        description:
          - undefined
        type: str
      new_pod_scale_up_delay:
        description:
          - undefined
        type: str
      ok_total_unready_count:
        description:
          - undefined
        type: str
      scan_interval:
        description:
          - undefined
        type: str
      scale_down_delay_after_add:
        description:
          - undefined
        type: str
      scale_down_delay_after_delete:
        description:
          - undefined
        type: str
      scale_down_delay_after_failure:
        description:
          - undefined
        type: str
      scale_down_unneeded_time:
        description:
          - undefined
        type: str
      scale_down_unready_time:
        description:
          - undefined
        type: str
      scale_down_utilization_threshold:
        description:
          - undefined
        type: str
      skip_nodes_with_local_storage:
        description:
          - undefined
        type: str
      skip_nodes_with_system_pods:
        description:
          - undefined
        type: str
  api_server_access_profile:
    description:
      - Access profile for managed cluster API server.
    type: dict
    suboptions:
      authorized_ip_ranges:
        description:
          - Authorized IP Ranges to kubernetes API server.
        type: list
      enable_private_cluster:
        description:
          - Whether to create the cluster as a private cluster or not.
        type: bool
  disk_encryption_set_id:
    description:
      - >-
        ResourceId of the disk encryption set to use for enabling encryption at
        rest.
    type: str
  identity_profile:
    description:
      - Identities associated with the cluster.
    type: dictionary
  sku:
    description:
      - The managed cluster SKU.
    type: dict
    suboptions:
      name:
        description:
          - Name of a managed cluster SKU.
        type: str
        choices:
          - Basic
      tier:
        description:
          - Tier of a managed cluster SKU.
        type: str
        choices:
          - Paid
          - Free
  state:
    description:
      - Assert the state of the ManagedCluster.
      - >-
        Use C(present) to create or update an ManagedCluster and C(absent) to
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
    - name: Create Managed Cluster with PPG
      azure_rm_managedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        location: location1
        properties:
          addon_profiles: {}
          agent_pool_profiles:
            - name: nodepool1
              type: VirtualMachineScaleSets
              count: 3
              enable_node_public_ip: true
              mode: System
              os_type: Linux
              proximity_placement_group_id: >-
                /subscriptions/subid1/resourcegroups/rg1/providers//Microsoft.Compute/proximityPlacementGroups/ppg1
              vm_size: Standard_DS2_v2
          auto_scaler_profile:
            scale-down-delay-after-add: 15m
            scan-interval: 20s
          disk_encryption_set_id: >-
            /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute/diskEncryptionSets/des
          dns_prefix: dnsprefix1
          enable_pod_security_policy: true
          enable_rbac: true
          kubernetes_version: ''
          linux_profile:
            admin_username: azureuser
            ssh:
              public_keys:
                - key_data: keydata
          network_profile:
            load_balancer_profile:
              managed_outbound_ips:
                count: 2
            load_balancer_sku: standard
            outbound_type: loadBalancer
          service_principal_profile:
            client_id: clientid
            secret: secret
          windows_profile:
            admin_password: replacePassword1234$
            admin_username: azureuser
        sku:
          name: Basic
          tier: Free
        tags:
          archv2: ''
          tier: production
        

    - name: Create/Update AAD Managed Cluster with EnableAzureRBAC
      azure_rm_managedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        location: location1
        properties:
          aad_profile:
            enable_azure_rbac: true
            managed: true
          addon_profiles: {}
          agent_pool_profiles:
            - name: nodepool1
              type: VirtualMachineScaleSets
              availability_zones:
                - '1'
                - '2'
                - '3'
              count: 3
              enable_node_public_ip: true
              mode: System
              os_type: Linux
              vm_size: Standard_DS1_v2
          auto_scaler_profile:
            scale-down-delay-after-add: 15m
            scan-interval: 20s
          disk_encryption_set_id: >-
            /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute/diskEncryptionSets/des
          dns_prefix: dnsprefix1
          enable_pod_security_policy: true
          enable_rbac: true
          kubernetes_version: ''
          linux_profile:
            admin_username: azureuser
            ssh:
              public_keys:
                - key_data: keydata
          network_profile:
            load_balancer_profile:
              managed_outbound_ips:
                count: 2
            load_balancer_sku: standard
            outbound_type: loadBalancer
          service_principal_profile:
            client_id: clientid
            secret: secret
          windows_profile:
            admin_password: replacePassword1234$
            admin_username: azureuser
        sku:
          name: Basic
          tier: Free
        tags:
          archv2: ''
          tier: production
        

    - name: Create/Update Managed Cluster
      azure_rm_managedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        identity:
          type: UserAssigned
          user_assigned_identities:
            /subscriptions/subid1/resource_groups/rg_name1/providers/microsoft.managed_identity/user_assigned_identities/identity1: {}
        location: location1
        properties:
          addon_profiles: {}
          agent_pool_profiles:
            - name: nodepool1
              type: VirtualMachineScaleSets
              availability_zones:
                - '1'
                - '2'
                - '3'
              count: 3
              enable_node_public_ip: true
              mode: System
              os_type: Linux
              vm_size: Standard_DS1_v2
          auto_scaler_profile:
            balance-similar-node-groups: 'true'
            expander: most-pods
            new-pod-scale-up-delay: 1m
            scale-down-delay-after-add: 15m
            scan-interval: 20s
            skip-nodes-with-system-pods: 'false'
          disk_encryption_set_id: >-
            /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute/diskEncryptionSets/des
          dns_prefix: dnsprefix1
          enable_pod_security_policy: true
          enable_rbac: true
          kubernetes_version: ''
          linux_profile:
            admin_username: azureuser
            ssh:
              public_keys:
                - key_data: keydata
          network_profile:
            load_balancer_profile:
              managed_outbound_ips:
                count: 2
            load_balancer_sku: standard
            outbound_type: loadBalancer
          service_principal_profile:
            client_id: clientid
            secret: secret
          windows_profile:
            admin_password: replacePassword1234$
            admin_username: azureuser
        sku:
          name: Basic
          tier: Free
        tags:
          archv2: ''
          tier: production
        

    - name: Create/Update Managed Cluster with EnableAHUB
      azure_rm_managedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        identity:
          type: UserAssigned
          user_assigned_identities:
            /subscriptions/subid1/resource_groups/rg_name1/providers/microsoft.managed_identity/user_assigned_identities/identity1: {}
        location: location1
        properties:
          addon_profiles: {}
          agent_pool_profiles:
            - name: nodepool1
              type: VirtualMachineScaleSets
              availability_zones:
                - '1'
                - '2'
                - '3'
              count: 3
              enable_node_public_ip: true
              mode: System
              os_type: Linux
              vm_size: Standard_DS1_v2
          auto_scaler_profile:
            scale-down-delay-after-add: 15m
            scan-interval: 20s
          disk_encryption_set_id: >-
            /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute/diskEncryptionSets/des
          dns_prefix: dnsprefix1
          enable_pod_security_policy: true
          enable_rbac: true
          kubernetes_version: ''
          linux_profile:
            admin_username: azureuser
            ssh:
              public_keys:
                - key_data: keydata
          network_profile:
            load_balancer_profile:
              managed_outbound_ips:
                count: 2
            load_balancer_sku: standard
            outbound_type: loadBalancer
          service_principal_profile:
            client_id: clientid
            secret: secret
          windows_profile:
            admin_password: replacePassword1234$
            admin_username: azureuser
            license_type: Windows_Server
        sku:
          name: Basic
          tier: Free
        tags:
          archv2: ''
          tier: production
        

    - name: Delete Managed Cluster
      azure_rm_managedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        

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


class AzureRMManagedCluster(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            kubernetes_version=dict(
                type='str',
                disposition='/kubernetes_version'
            ),
            dns_prefix=dict(
                type='str',
                disposition='/dns_prefix'
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
                        disposition='admin_password'
                    ),
                    license_type=dict(
                        type='str',
                        disposition='license_type',
                        choices=['None',
                                 'Windows_Server']
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
                    )
                )
            ),
            addon_profiles=dict(
                type='dictionary',
                disposition='/addon_profiles'
            ),
            node_resource_group=dict(
                type='str',
                disposition='/node_resource_group'
            ),
            enable_rbac=dict(
                type='bool',
                disposition='/enable_rbac'
            ),
            enable_pod_security_policy=dict(
                type='bool',
                disposition='/enable_pod_security_policy'
            ),
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    network_plugin=dict(
                        type='str',
                        disposition='network_plugin',
                        choices=['azure',
                                 'kubenet']
                    ),
                    network_policy=dict(
                        type='str',
                        disposition='network_policy',
                        choices=['calico',
                                 'azure']
                    ),
                    network_mode=dict(
                        type='str',
                        disposition='network_mode',
                        choices=['transparent',
                                 'bridge']
                    ),
                    pod_cidr=dict(
                        type='str',
                        disposition='pod_cidr'
                    ),
                    service_cidr=dict(
                        type='str',
                        disposition='service_cidr'
                    ),
                    dns_service_ip=dict(
                        type='str',
                        disposition='dns_service_ip'
                    ),
                    docker_bridge_cidr=dict(
                        type='str',
                        disposition='docker_bridge_cidr'
                    ),
                    outbound_type=dict(
                        type='str',
                        disposition='outbound_type',
                        choices=['loadBalancer',
                                 'userDefinedRouting']
                    ),
                    load_balancer_sku=dict(
                        type='str',
                        disposition='load_balancer_sku',
                        choices=['standard',
                                 'basic']
                    ),
                    load_balancer_profile=dict(
                        type='dict',
                        disposition='load_balancer_profile',
                        options=dict(
                            managed_outbound_ips=dict(
                                type='dict',
                                disposition='managed_outbound_ips',
                                options=dict(
                                    count=dict(
                                        type='integer',
                                        disposition='count'
                                    )
                                )
                            ),
                            outbound_ip_prefixes=dict(
                                type='dict',
                                disposition='outbound_ip_prefixes',
                                options=dict(
                                    public_ip_prefixes=dict(
                                        type='list',
                                        disposition='public_ip_prefixes',
                                        elements='dict',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
                            ),
                            outbound_ips=dict(
                                type='dict',
                                disposition='outbound_ips',
                                options=dict(
                                    public_ips=dict(
                                        type='list',
                                        disposition='public_ips',
                                        elements='dict',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
                            ),
                            effective_outbound_ips=dict(
                                type='list',
                                disposition='effective_outbound_ips',
                                elements='dict',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            allocated_outbound_ports=dict(
                                type='integer',
                                disposition='allocated_outbound_ports'
                            ),
                            idle_timeout_in_minutes=dict(
                                type='integer',
                                disposition='idle_timeout_in_minutes'
                            )
                        )
                    )
                )
            ),
            aadprofile=dict(
                type='dict',
                disposition='/aadprofile',
                options=dict(
                    managed=dict(
                        type='bool',
                        disposition='managed'
                    ),
                    enable_azure_rbac=dict(
                        type='bool',
                        disposition='enable_azure_rbac'
                    ),
                    admin_group_object_ids=dict(
                        type='list',
                        disposition='admin_group_object_ids',
                        elements='str'
                    ),
                    client_app_id=dict(
                        type='str',
                        disposition='client_app_id'
                    ),
                    server_app_id=dict(
                        type='str',
                        disposition='server_app_id'
                    ),
                    server_app_secret=dict(
                        type='str',
                        disposition='server_app_secret'
                    ),
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id'
                    )
                )
            ),
            auto_scaler_profile=dict(
                type='dict',
                disposition='/auto_scaler_profile',
                options=dict(
                    balance_similar_node_groups=dict(
                        type='str',
                        disposition='balance_similar_node_groups'
                    ),
                    expander=dict(
                        type='str',
                        disposition='expander',
                        choices=['least-waste',
                                 'most-pods',
                                 'random']
                    ),
                    max_empty_bulk_delete=dict(
                        type='str',
                        disposition='max_empty_bulk_delete'
                    ),
                    max_graceful_termination_sec=dict(
                        type='str',
                        disposition='max_graceful_termination_sec'
                    ),
                    max_total_unready_percentage=dict(
                        type='str',
                        disposition='max_total_unready_percentage'
                    ),
                    new_pod_scale_up_delay=dict(
                        type='str',
                        disposition='new_pod_scale_up_delay'
                    ),
                    ok_total_unready_count=dict(
                        type='str',
                        disposition='ok_total_unready_count'
                    ),
                    scan_interval=dict(
                        type='str',
                        disposition='scan_interval'
                    ),
                    scale_down_delay_after_add=dict(
                        type='str',
                        disposition='scale_down_delay_after_add'
                    ),
                    scale_down_delay_after_delete=dict(
                        type='str',
                        disposition='scale_down_delay_after_delete'
                    ),
                    scale_down_delay_after_failure=dict(
                        type='str',
                        disposition='scale_down_delay_after_failure'
                    ),
                    scale_down_unneeded_time=dict(
                        type='str',
                        disposition='scale_down_unneeded_time'
                    ),
                    scale_down_unready_time=dict(
                        type='str',
                        disposition='scale_down_unready_time'
                    ),
                    scale_down_utilization_threshold=dict(
                        type='str',
                        disposition='scale_down_utilization_threshold'
                    ),
                    skip_nodes_with_local_storage=dict(
                        type='str',
                        disposition='skip_nodes_with_local_storage'
                    ),
                    skip_nodes_with_system_pods=dict(
                        type='str',
                        disposition='skip_nodes_with_system_pods'
                    )
                )
            ),
            api_server_access_profile=dict(
                type='dict',
                disposition='/api_server_access_profile',
                options=dict(
                    authorized_ip_ranges=dict(
                        type='list',
                        disposition='authorized_ip_ranges',
                        elements='str'
                    ),
                    enable_private_cluster=dict(
                        type='bool',
                        disposition='enable_private_cluster'
                    )
                )
            ),
            disk_encryption_set_id=dict(
                type='str',
                disposition='/disk_encryption_set_id'
            ),
            identity_profile=dict(
                type='dictionary',
                disposition='/identity_profile'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['Basic']
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier',
                        choices=['Paid',
                                 'Free']
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
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedCluster, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.managed_clusters.create_or_update(resource_group_name=self.resource_group_name,
                                                                          resource_name=self.resource_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedCluster instance.')
            self.fail('Error creating the ManagedCluster instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_clusters.delete(resource_group_name=self.resource_group_name,
                                                                resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagedCluster instance.')
            self.fail('Error deleting the ManagedCluster instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_clusters.get(resource_group_name=self.resource_group_name,
                                                             resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedCluster()


if __name__ == '__main__':
    main()
