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
module: azure_rm_containerservice_info
version_added: '2.9'
short_description: Get ContainerService info.
description:
  - Get info of ContainerService.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  container_service_name:
    description:
      - >-
        The name of the container service in the specified subscription and
        resource group.
    type: str
  location:
    description:
      - The name of a supported Azure region.
    type: str
  resource_type:
    description:
      - resource type for which the list of orchestrators needs to be returned
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Container Services
      azure_rm_containerservice_info: 
        {}
        

    - name: Get Container Service
      azure_rm_containerservice_info: 
        container_service_name: acs1
        resource_group_name: rg1
        

    - name: List Container Services by Resource Group
      azure_rm_containerservice_info: 
        resource_group_name: rg1
        

    - name: List Container Service Orchestrators
      azure_rm_containerservice_info: 
        location: location1
        

'''

RETURN = '''
container_services:
  description: >-
    A list of dict results where the key is the name of the ContainerService and
    the values are the facts for that ContainerService.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of container services.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - >-
              The current deployment or provisioning state, which only appears
              in the response.
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
                  The orchestrator to use to manage container service cluster
                  resources. Valid values are Kubernetes, Swarm, DCOS, DockerCE
                  and Custom.
              returned: always
              type: str
              sample: null
            orchestrator_version:
              description:
                - >-
                  The version of the orchestrator to use. You can specify the
                  major.minor.patch part of the actual version.For example, you
                  can specify version as "1.6.11".
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
              Information about a service principal identity for the cluster to
              use for manipulating Azure APIs. Exact one of secret or
              keyVaultSecretRef need to be specified.
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
                  The secret password associated with the service principal in
                  plain text.
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
                  Number of masters (VMs) in the container service cluster.
                  Allowed values are 1, 3, and 5. The default value is 1.
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
                  OS Disk Size in GB to be used to specify the disk size for
                  every machine in this master/agent pool. If you specify 0, it
                  will apply the default osDisk size according to the vmSize
                  specified.
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
                  FirstConsecutiveStaticIP used to specify the first static ip
                  of masters.
              returned: always
              type: str
              sample: null
            storage_profile:
              description:
                - >-
                  Storage profile specifies what kind of storage used. Choose
                  from StorageAccount and ManagedDisks. Leave it empty, we will
                  choose for you based on the orchestrator choice.
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
                  Number of agents (VMs) to host docker containers. Allowed
                  values must be in the range of 1 to 100 (inclusive). The
                  default value is 1. 
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
                  OS Disk Size in GB to be used to specify the disk size for
                  every machine in this master/agent pool. If you specify 0, it
                  will apply the default osDisk size according to the vmSize
                  specified.
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
                  Ports number array used to expose on this agent pool. The
                  default opened ports are different based on your choice of
                  orchestrator.
              returned: always
              type: list
              sample: null
            storage_profile:
              description:
                - >-
                  Storage profile specifies what kind of storage used. Choose
                  from StorageAccount and ManagedDisks. Leave it empty, we will
                  choose for you based on the orchestrator choice.
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
                  OsType to be used to specify os type. Choose from Linux and
                  Windows. Default to Linux.
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
                      The list of SSH public keys used to authenticate with
                      Linux-based VMs. Only expect one key specified.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    key_data:
                      description:
                        - >-
                          Certificate public key used to authenticate with VMs
                          through SSH. The certificate must be in PEM format
                          with or without headers.
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
                    - >-
                      The URI of the storage account where diagnostics are
                      stored.
                  returned: always
                  type: str
                  sample: null
    next_link:
      description:
        - The URL to get the next set of container service results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - |-
          Resource Id
          Id of the orchestrator version profile list result.
      returned: always
      type: str
      sample: null
    name:
      description:
        - |-
          Resource name
          Name of the orchestrator version profile list result.
      returned: always
      type: str
      sample: null
    type:
      description:
        - |-
          Resource type
          Type of the orchestrator version profile list result.
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
          The current deployment or provisioning state, which only appears in
          the response.
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
              The orchestrator to use to manage container service cluster
              resources. Valid values are Kubernetes, Swarm, DCOS, DockerCE and
              Custom.
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
          Information about a service principal identity for the cluster to use
          for manipulating Azure APIs. Exact one of secret or keyVaultSecretRef
          need to be specified.
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
              machine in this master/agent pool. If you specify 0, it will apply
              the default osDisk size according to the vmSize specified.
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
              StorageAccount and ManagedDisks. Leave it empty, we will choose
              for you based on the orchestrator choice.
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
              Number of agents (VMs) to host docker containers. Allowed values
              must be in the range of 1 to 100 (inclusive). The default value is
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
              machine in this master/agent pool. If you specify 0, it will apply
              the default osDisk size according to the vmSize specified.
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
              StorageAccount and ManagedDisks. Leave it empty, we will choose
              for you based on the orchestrator choice.
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
              OsType to be used to specify os type. Choose from Linux and
              Windows. Default to Linux.
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
                  The list of SSH public keys used to authenticate with
                  Linux-based VMs. Only expect one key specified.
              returned: always
              type: list
              sample: null
              contains:
                key_data:
                  description:
                    - >-
                      Certificate public key used to authenticate with VMs
                      through SSH. The certificate must be in PEM format with or
                      without headers.
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
    orchestrators:
      description:
        - List of orchestrator version profiles.
      returned: always
      type: list
      sample: null
      contains:
        orchestrator_type:
          description:
            - Orchestrator type.
          returned: always
          type: str
          sample: null
        orchestrator_version:
          description:
            - 'Orchestrator version (major, minor, patch).'
          returned: always
          type: str
          sample: null
        default:
          description:
            - Installed by default if version is not specified.
          returned: always
          type: bool
          sample: null
        is_preview:
          description:
            - Whether Kubernetes version is currently in preview.
          returned: always
          type: bool
          sample: null
        upgrades:
          description:
            - The list of available upgrade versions.
          returned: always
          type: list
          sample: null
          contains:
            orchestrator_type:
              description:
                - Orchestrator type.
              returned: always
              type: str
              sample: null
            orchestrator_version:
              description:
                - 'Orchestrator version (major, minor, patch).'
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


class AzureRMContainerServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            container_service_name=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            resource_type=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.container_service_name = None
        self.location = None
        self.resource_type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMContainerServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerServiceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-07-01')

        if (self.resource_group_name is not None and
            self.container_service_name is not None):
            self.results['container_services'] = self.format_item(self.get())
        elif (self.location is not None):
            self.results['container_services'] = self.format_item(self.listorchestrator())
        elif (self.resource_group_name is not None):
            self.results['container_services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['container_services'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.container_services.get(resource_group_name=self.resource_group_name,
                                                               container_service_name=self.container_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listorchestrator(self):
        response = None

        try:
            response = self.mgmt_client.container_services.list_orchestrator(location=self.location,
                                                                             resource_type=self.resource_type)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.container_services.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.container_services.list()
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
    AzureRMContainerServiceInfo()


if __name__ == '__main__':
    main()
