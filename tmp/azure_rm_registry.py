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
module: azure_rm_registry
version_added: '2.9'
short_description: Manage Azure Registry instance.
description:
  - 'Create, update and delete instance of Azure Registry.'
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  registry_name:
    description:
      - The name of the container registry.
    required: true
    type: str
  location:
    description:
      - >-
        The location of the resource. This cannot be changed after the resource
        is created.
    type: str
  admin_user_enabled:
    description:
      - The value that indicates whether the admin user is enabled.
    type: bool
  storage_account:
    description:
      - >-
        The properties of the storage account for the container registry. Only
        applicable to Classic SKU.
    type: dict
    suboptions:
      id:
        description:
          - The resource ID of the storage account.
        required: true
        type: str
  network_rule_set:
    description:
      - The network rule set for a container registry.
    type: dict
    suboptions:
      default_action:
        description:
          - The default action of allow or deny when no other rules match.
        required: true
        type: str
        choices:
          - Allow
          - Deny
      virtual_network_rules:
        description:
          - The virtual network rules.
        type: list
        suboptions:
          action:
            description:
              - The action of virtual network rule.
            type: str
            choices:
              - Allow
          virtual_network_resource_id:
            description:
              - >-
                Resource ID of a subnet, for example:
                /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
            required: true
            type: str
      ip_rules:
        description:
          - The IP ACL rules.
        type: list
        suboptions:
          action:
            description:
              - The action of IP ACL rule.
            type: str
            choices:
              - Allow
          ip_address_or_range:
            description:
              - >-
                Specifies the IP or IP range in CIDR format. Only IPV4 address
                is allowed.
            required: true
            type: str
  policies:
    description:
      - The policies for a container registry.
    type: dict
    suboptions:
      quarantine_policy:
        description:
          - The quarantine policy for a container registry.
        type: dict
        suboptions:
          status:
            description:
              - The value that indicates whether the policy is enabled or not.
            type: str
            choices:
              - enabled
              - disabled
      trust_policy:
        description:
          - The content trust policy for a container registry.
        type: dict
        suboptions:
          type:
            description:
              - The type of trust policy.
            type: str
            choices:
              - Notary
          status:
            description:
              - The value that indicates whether the policy is enabled or not.
            type: str
            choices:
              - enabled
              - disabled
      retention_policy:
        description:
          - The retention policy for a container registry.
        type: dict
        suboptions:
          days:
            description:
              - >-
                The number of days to retain an untagged manifest after which it
                gets purged.
            type: integer
          last_updated_time:
            description:
              - The timestamp when the policy was last updated.
            type: str
          status:
            description:
              - The value that indicates whether the policy is enabled or not.
            type: str
            choices:
              - enabled
              - disabled
  encryption:
    description:
      - The encryption settings of container registry.
    type: dict
    suboptions:
      status:
        description:
          - >-
            Indicates whether or not the encryption is enabled for container
            registry.
        type: str
        choices:
          - enabled
          - disabled
      key_vault_properties:
        description:
          - Key vault properties.
        type: dict
        suboptions:
          key_identifier:
            description:
              - Key vault uri to access the encryption key.
            type: str
          versioned_key_identifier:
            description:
              - >-
                The fully qualified key identifier that includes the version of
                the key that is actually used for encryption.
            type: str
          identity:
            description:
              - >-
                The client id of the identity which will be used to access key
                vault.
            type: str
  data_endpoint_enabled:
    description:
      - Enable a single data endpoint per region for serving data.
    type: bool
  public_network_access:
    description:
      - >-
        Whether or not public network access is allowed for the container
        registry.
    type: str
    choices:
      - Enabled
      - Disabled
  principal_id:
    description:
      - The principal ID of resource identity.
    type: str
  tenant_id:
    description:
      - The tenant ID of resource.
    type: str
  type:
    description:
      - The identity type.
    type: sealed-choice
  user_assigned_identities:
    description:
      - "The list of user identities associated with the resource. The user identity \r"
      - "dictionary key references will be ARM resource ids in the form: \r"
      - "'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/\r"
      - '    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}''.'
    type: dictionary
  name:
    description:
      - The SKU name of the container registry. Required for registry creation.
    type: str
    choices:
      - Classic
      - Basic
      - Standard
      - Premium
  state:
    description:
      - Assert the state of the Registry.
      - >-
        Use C(present) to create or update an Registry and C(absent) to delete
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
    - name: RegistryCreate
      azure_rm_registry: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        location: westus
        properties:
          admin_user_enabled: true
        sku:
          name: Standard
        tags:
          key: value
        

    - name: RegistryDelete
      azure_rm_registry: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

    - name: RegistryUpdate
      azure_rm_registry: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
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
      The location of the resource. This cannot be changed after the resource is
      created.
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
      The provisioning state of the container registry at the time the operation
      was called.
  returned: always
  type: str
  sample: null
status:
  description:
    - The status of the container registry at the time the operation was called.
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
              Specifies the IP or IP range in CIDR format. Only IPV4 address is
              allowed.
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
              The number of days to retain an untagged manifest after which it
              gets purged.
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
              The fully qualified key identifier that includes the version of
              the key that is actually used for encryption.
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
    - List of host names that will serve data when dataEndpointEnabled is true.
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
          A collection of information about the state of the connection between
          service consumer and provider.
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
              The description for connection status. For example if connection
              is rejected it can indicate reason for rejection.
          returned: always
          type: str
          sample: null
        actions_required:
          description:
            - >-
              A message indicating if changes on the service provider require
              any updates on the consumer.
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
    - The SKU name of the container registry. Required for registry creation.
  returned: always
  type: str
  sample: null
tier:
  description:
    - The SKU tier based on the SKU name.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRegistry(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            admin_user_enabled=dict(
                type='bool',
                disposition='/admin_user_enabled'
            ),
            storage_account=dict(
                type='dict',
                disposition='/storage_account',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id',
                        required=True
                    )
                )
            ),
            network_rule_set=dict(
                type='dict',
                disposition='/network_rule_set',
                options=dict(
                    default_action=dict(
                        type='str',
                        disposition='default_action',
                        choices=['Allow',
                                 'Deny'],
                        required=True
                    ),
                    virtual_network_rules=dict(
                        type='list',
                        disposition='virtual_network_rules',
                        elements='dict',
                        options=dict(
                            action=dict(
                                type='str',
                                disposition='action',
                                choices=['Allow']
                            ),
                            virtual_network_resource_id=dict(
                                type='str',
                                disposition='virtual_network_resource_id',
                                required=True
                            )
                        )
                    ),
                    ip_rules=dict(
                        type='list',
                        disposition='ip_rules',
                        elements='dict',
                        options=dict(
                            action=dict(
                                type='str',
                                disposition='action',
                                choices=['Allow']
                            ),
                            ip_address_or_range=dict(
                                type='str',
                                disposition='ip_address_or_range',
                                required=True
                            )
                        )
                    )
                )
            ),
            policies=dict(
                type='dict',
                disposition='/policies',
                options=dict(
                    quarantine_policy=dict(
                        type='dict',
                        disposition='quarantine_policy',
                        options=dict(
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['enabled',
                                         'disabled']
                            )
                        )
                    ),
                    trust_policy=dict(
                        type='dict',
                        disposition='trust_policy',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                choices=['Notary']
                            ),
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['enabled',
                                         'disabled']
                            )
                        )
                    ),
                    retention_policy=dict(
                        type='dict',
                        disposition='retention_policy',
                        options=dict(
                            days=dict(
                                type='integer',
                                disposition='days'
                            ),
                            last_updated_time=dict(
                                type='str',
                                updatable=False,
                                disposition='last_updated_time'
                            ),
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['enabled',
                                         'disabled']
                            )
                        )
                    )
                )
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    status=dict(
                        type='str',
                        disposition='status',
                        choices=['enabled',
                                 'disabled']
                    ),
                    key_vault_properties=dict(
                        type='dict',
                        disposition='key_vault_properties',
                        options=dict(
                            key_identifier=dict(
                                type='str',
                                disposition='key_identifier'
                            ),
                            versioned_key_identifier=dict(
                                type='str',
                                updatable=False,
                                disposition='versioned_key_identifier'
                            ),
                            identity=dict(
                                type='str',
                                disposition='identity'
                            )
                        )
                    )
                )
            ),
            data_endpoint_enabled=dict(
                type='bool',
                disposition='/data_endpoint_enabled'
            ),
            public_network_access=dict(
                type='str',
                disposition='/public_network_access',
                choices=['Enabled',
                         'Disabled']
            ),
            principal_id=dict(
                type='str',
                disposition='/principal_id'
            ),
            tenant_id=dict(
                type='str',
                disposition='/tenant_id'
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            name=dict(
                type='str',
                disposition='/name',
                choices=['Classic',
                         'Basic',
                         'Standard',
                         'Premium']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRegistry, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.registries.create(resource_group_name=self.resource_group_name,
                                                              registry_name=self.registry_name,
                                                              registry=self.body)
            else:
                response = self.mgmt_client.registries.update(resource_group_name=self.resource_group_name,
                                                              registry_name=self.registry_name,
                                                              registry_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Registry instance.')
            self.fail('Error creating the Registry instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.registries.delete(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name)
        except CloudError as e:
            self.log('Error attempting to delete the Registry instance.')
            self.fail('Error deleting the Registry instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.registries.get(resource_group_name=self.resource_group_name,
                                                       registry_name=self.registry_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRegistry()


if __name__ == '__main__':
    main()
