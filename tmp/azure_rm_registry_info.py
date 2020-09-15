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
module: azure_rm_registry_info
version_added: '2.9'
short_description: Get Registry info.
description:
  - Get info of Registry.
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    type: str
  registry_name:
    description:
      - The name of the container registry.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RegistryGet
      azure_rm_registry_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: RegistryListByResourceGroup
      azure_rm_registry_info: 
        resource_group_name: myResourceGroup
        

    - name: RegistryList
      azure_rm_registry_info: 
        {}
        

    - name: RegistryListUsages
      azure_rm_registry_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: RegistryListPrivateLinkResources
      azure_rm_registry_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
registries:
  description: >-
    A list of dict results where the key is the name of the Registry and the
    values are the facts for that Registry.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - >-
          The location of the resource. This cannot be changed after the
          resource is created.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    login_server:
      description:
        - The URL that can be used to log into the container registry.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of the container registry in ISO8601 format.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The provisioning state of the container registry at the time the
          operation was called.
      returned: always
      type: str
      sample: null
    status:
      description:
        - >-
          The status of the container registry at the time the operation was
          called.
      returned: always
      type: dict
      sample: null
      contains:
        display_status:
          description:
            - The short label for the status.
          returned: always
          type: str
          sample: null
        message:
          description:
            - >-
              The detailed message for the status, including alerts and error
              messages.
          returned: always
          type: str
          sample: null
        timestamp:
          description:
            - The timestamp when the status was changed to the current value.
          returned: always
          type: str
          sample: null
    admin_user_enabled:
      description:
        - The value that indicates whether the admin user is enabled.
      returned: always
      type: bool
      sample: null
    storage_account:
      description:
        - >-
          The properties of the storage account for the container registry. Only
          applicable to Classic SKU.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The resource ID of the storage account.
          returned: always
          type: str
          sample: null
    network_rule_set:
      description:
        - The network rule set for a container registry.
      returned: always
      type: dict
      sample: null
      contains:
        default_action:
          description:
            - The default action of allow or deny when no other rules match.
          returned: always
          type: str
          sample: null
        virtual_network_rules:
          description:
            - The virtual network rules.
          returned: always
          type: list
          sample: null
          contains:
            action:
              description:
                - The action of virtual network rule.
              returned: always
              type: str
              sample: null
            virtual_network_resource_id:
              description:
                - >-
                  Resource ID of a subnet, for example:
                  /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
              returned: always
              type: str
              sample: null
        ip_rules:
          description:
            - The IP ACL rules.
          returned: always
          type: list
          sample: null
          contains:
            action:
              description:
                - The action of IP ACL rule.
              returned: always
              type: str
              sample: null
            ip_address_or_range:
              description:
                - >-
                  Specifies the IP or IP range in CIDR format. Only IPV4 address
                  is allowed.
              returned: always
              type: str
              sample: null
    policies:
      description:
        - The policies for a container registry.
      returned: always
      type: dict
      sample: null
      contains:
        quarantine_policy:
          description:
            - The quarantine policy for a container registry.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - The value that indicates whether the policy is enabled or not.
              returned: always
              type: str
              sample: null
        trust_policy:
          description:
            - The content trust policy for a container registry.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of trust policy.
              returned: always
              type: str
              sample: null
            status:
              description:
                - The value that indicates whether the policy is enabled or not.
              returned: always
              type: str
              sample: null
        retention_policy:
          description:
            - The retention policy for a container registry.
          returned: always
          type: dict
          sample: null
          contains:
            days:
              description:
                - >-
                  The number of days to retain an untagged manifest after which
                  it gets purged.
              returned: always
              type: integer
              sample: null
            last_updated_time:
              description:
                - The timestamp when the policy was last updated.
              returned: always
              type: str
              sample: null
            status:
              description:
                - The value that indicates whether the policy is enabled or not.
              returned: always
              type: str
              sample: null
    encryption:
      description:
        - The encryption settings of container registry.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - >-
              Indicates whether or not the encryption is enabled for container
              registry.
          returned: always
          type: str
          sample: null
        key_vault_properties:
          description:
            - Key vault properties.
          returned: always
          type: dict
          sample: null
          contains:
            key_identifier:
              description:
                - Key vault uri to access the encryption key.
              returned: always
              type: str
              sample: null
            versioned_key_identifier:
              description:
                - >-
                  The fully qualified key identifier that includes the version
                  of the key that is actually used for encryption.
              returned: always
              type: str
              sample: null
            identity:
              description:
                - >-
                  The client id of the identity which will be used to access key
                  vault.
              returned: always
              type: str
              sample: null
    data_endpoint_enabled:
      description:
        - Enable a single data endpoint per region for serving data.
      returned: always
      type: bool
      sample: null
    data_endpoint_host_names:
      description:
        - >-
          List of host names that will serve data when dataEndpointEnabled is
          true.
      returned: always
      type: list
      sample: null
    private_endpoint_connections:
      description:
        - List of private endpoint connections for a container registry.
      returned: always
      type: list
      sample: null
      contains:
        private_link_service_connection_state:
          description:
            - >-
              A collection of information about the state of the connection
              between service consumer and provider.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - The private link service connection status.
              returned: always
              type: str
              sample: null
            description:
              description:
                - >-
                  The description for connection status. For example if
                  connection is rejected it can indicate reason for rejection.
              returned: always
              type: str
              sample: null
            actions_required:
              description:
                - >-
                  A message indicating if changes on the service provider
                  require any updates on the consumer.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - The provisioning state of private endpoint connection resource.
          returned: always
          type: str
          sample: null
        id_properties_private_endpoint_id:
          description:
            - >-
              This is private endpoint resource created with Microsoft.Network
              resource provider.
          returned: always
          type: str
          sample: null
    public_network_access:
      description:
        - >-
          Whether or not public network access is allowed for the container
          registry.
      returned: always
      type: str
      sample: null
    principal_id:
      description:
        - The principal ID of resource identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The tenant ID of resource.
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - The identity type.
      returned: always
      type: sealed-choice
      sample: null
    user_assigned_identities:
      description:
        - "The list of user identities associated with the resource. The user identity \r\ndictionary key references will be ARM resource ids in the form: \r\n'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/\r\n    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'."
      returned: always
      type: dictionary
      sample: null
    name_sku_name:
      description:
        - >-
          The SKU name of the container registry. Required for registry
          creation.
      returned: always
      type: str
      sample: null
    tier:
      description:
        - The SKU tier based on the SKU name.
      returned: always
      type: str
      sample: null
    value:
      description:
        - >-
          The list of container registries. Since this list may be incomplete,
          the nextLink field should be used to request the next list of
          container registries.

          The list of container registry quota usages.

          The list of private link resources. Since this list may be incomplete,
          the nextLink field should be used to request the next list of private
          link resources.
      returned: always
      type: list
      sample: null
      contains:
        login_server:
          description:
            - The URL that can be used to log into the container registry.
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of the container registry in ISO8601 format.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the container registry at the time the
              operation was called.
          returned: always
          type: str
          sample: null
        status:
          description:
            - >-
              The status of the container registry at the time the operation was
              called.
          returned: always
          type: dict
          sample: null
          contains:
            display_status:
              description:
                - The short label for the status.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The detailed message for the status, including alerts and
                  error messages.
              returned: always
              type: str
              sample: null
            timestamp:
              description:
                - >-
                  The timestamp when the status was changed to the current
                  value.
              returned: always
              type: str
              sample: null
        admin_user_enabled:
          description:
            - The value that indicates whether the admin user is enabled.
          returned: always
          type: bool
          sample: null
        storage_account:
          description:
            - >-
              The properties of the storage account for the container registry.
              Only applicable to Classic SKU.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - The resource ID of the storage account.
              returned: always
              type: str
              sample: null
        network_rule_set:
          description:
            - The network rule set for a container registry.
          returned: always
          type: dict
          sample: null
          contains:
            default_action:
              description:
                - The default action of allow or deny when no other rules match.
              returned: always
              type: str
              sample: null
            virtual_network_rules:
              description:
                - The virtual network rules.
              returned: always
              type: list
              sample: null
              contains:
                action:
                  description:
                    - The action of virtual network rule.
                  returned: always
                  type: str
                  sample: null
                virtual_network_resource_id:
                  description:
                    - >-
                      Resource ID of a subnet, for example:
                      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
                  returned: always
                  type: str
                  sample: null
            ip_rules:
              description:
                - The IP ACL rules.
              returned: always
              type: list
              sample: null
              contains:
                action:
                  description:
                    - The action of IP ACL rule.
                  returned: always
                  type: str
                  sample: null
                ip_address_or_range:
                  description:
                    - >-
                      Specifies the IP or IP range in CIDR format. Only IPV4
                      address is allowed.
                  returned: always
                  type: str
                  sample: null
        policies:
          description:
            - The policies for a container registry.
          returned: always
          type: dict
          sample: null
          contains:
            quarantine_policy:
              description:
                - The quarantine policy for a container registry.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - >-
                      The value that indicates whether the policy is enabled or
                      not.
                  returned: always
                  type: str
                  sample: null
            trust_policy:
              description:
                - The content trust policy for a container registry.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of trust policy.
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - >-
                      The value that indicates whether the policy is enabled or
                      not.
                  returned: always
                  type: str
                  sample: null
            retention_policy:
              description:
                - The retention policy for a container registry.
              returned: always
              type: dict
              sample: null
              contains:
                days:
                  description:
                    - >-
                      The number of days to retain an untagged manifest after
                      which it gets purged.
                  returned: always
                  type: integer
                  sample: null
                last_updated_time:
                  description:
                    - The timestamp when the policy was last updated.
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - >-
                      The value that indicates whether the policy is enabled or
                      not.
                  returned: always
                  type: str
                  sample: null
        encryption:
          description:
            - The encryption settings of container registry.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  Indicates whether or not the encryption is enabled for
                  container registry.
              returned: always
              type: str
              sample: null
            key_vault_properties:
              description:
                - Key vault properties.
              returned: always
              type: dict
              sample: null
              contains:
                key_identifier:
                  description:
                    - Key vault uri to access the encryption key.
                  returned: always
                  type: str
                  sample: null
                versioned_key_identifier:
                  description:
                    - >-
                      The fully qualified key identifier that includes the
                      version of the key that is actually used for encryption.
                  returned: always
                  type: str
                  sample: null
                identity:
                  description:
                    - >-
                      The client id of the identity which will be used to access
                      key vault.
                  returned: always
                  type: str
                  sample: null
        data_endpoint_enabled:
          description:
            - Enable a single data endpoint per region for serving data.
          returned: always
          type: bool
          sample: null
        data_endpoint_host_names:
          description:
            - >-
              List of host names that will serve data when dataEndpointEnabled
              is true.
          returned: always
          type: list
          sample: null
        private_endpoint_connections:
          description:
            - List of private endpoint connections for a container registry.
          returned: always
          type: list
          sample: null
          contains:
            private_link_service_connection_state:
              description:
                - >-
                  A collection of information about the state of the connection
                  between service consumer and provider.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - The private link service connection status.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - >-
                      The description for connection status. For example if
                      connection is rejected it can indicate reason for
                      rejection.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - >-
                      A message indicating if changes on the service provider
                      require any updates on the consumer.
                  returned: always
                  type: str
                  sample: null
            provisioning_state:
              description:
                - >-
                  The provisioning state of private endpoint connection
                  resource.
              returned: always
              type: str
              sample: null
            id_properties_private_endpoint_id:
              description:
                - >-
                  This is private endpoint resource created with
                  Microsoft.Network resource provider.
              returned: always
              type: str
              sample: null
        public_network_access:
          description:
            - >-
              Whether or not public network access is allowed for the container
              registry.
          returned: always
          type: str
          sample: null
        principal_id:
          description:
            - The principal ID of resource identity.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The tenant ID of resource.
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - The identity type.
          returned: always
          type: sealed-choice
          sample: null
        user_assigned_identities:
          description:
            - "The list of user identities associated with the resource. The user identity \r\ndictionary key references will be ARM resource ids in the form: \r\n'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/\r\n    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'."
          returned: always
          type: dictionary
          sample: null
        name_sku_name:
          description:
            - >-
              The SKU name of the container registry. Required for registry
              creation.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The SKU tier based on the SKU name.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          The URI that can be used to request the next list of container
          registries.

          The URI that can be used to request the next list of private link
          resources.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRegistryInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            registry_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRegistryInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None):
            self.results['registries'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['registries'] = self.format_item(self.listusage())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['registries'] = self.format_item(self.listprivatelinkresource())
        elif (self.resource_group_name is not None):
            self.results['registries'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['registries'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.registries.get(resource_group_name=self.resource_group_name,
                                                       registry_name=self.registry_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listusage(self):
        response = None

        try:
            response = self.mgmt_client.registries.list_usage(resource_group_name=self.resource_group_name,
                                                              registry_name=self.registry_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listprivatelinkresource(self):
        response = None

        try:
            response = self.mgmt_client.registries.list_private_link_resource(resource_group_name=self.resource_group_name,
                                                                              registry_name=self.registry_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.registries.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.registries.list()
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
    AzureRMRegistryInfo()


if __name__ == '__main__':
    main()
