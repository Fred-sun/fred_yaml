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
module: azure_rm_configurationstore
version_added: '2.9'
short_description: Manage Azure ConfigurationStore instance.
description:
  - 'Create, update and delete instance of Azure ConfigurationStore.'
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  config_store_name:
    description:
      - The name of the configuration store.
    required: true
    type: str
  location:
    description:
      - >-
        The location of the resource. This cannot be changed after the resource
        is created.
    type: str
  name:
    description:
      - The SKU name of the configuration store.
    type: str
  encryption:
    description:
      - The encryption settings of the configuration store.
    type: dict
    suboptions:
      key_vault_properties:
        description:
          - Key vault properties.
        type: dict
        suboptions:
          key_identifier:
            description:
              - The URI of the key vault key used to encrypt data.
            type: str
          identity_client_id:
            description:
              - >-
                The client id of the identity which will be used to access key
                vault.
            type: str
  public_network_access:
    description:
      - >-
        Control permission for data plane traffic coming from public networks
        while private endpoint is enabled.
    type: str
    choices:
      - Enabled
      - Disabled
  type:
    description:
      - >-
        The type of managed identity used. The type 'SystemAssigned,
        UserAssigned' includes both an implicitly created identity and a set of
        user-assigned identities. The type 'None' will remove any identities.
    type: str
    choices:
      - None
      - SystemAssigned
      - UserAssigned
      - 'SystemAssigned, UserAssigned'
  user_assigned_identities:
    description:
      - >-
        The list of user-assigned identities associated with the resource. The
        user-assigned identity dictionary keys will be ARM resource ids in the
        form:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    type: dictionary
  state:
    description:
      - Assert the state of the ConfigurationStore.
      - >-
        Use C(present) to create or update an ConfigurationStore and C(absent)
        to delete it.
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
    - name: ConfigurationStores_Create
      azure_rm_configurationstore: 
        config_store_name: contoso
        resource_group_name: myResourceGroup
        

    - name: ConfigurationStores_Create_WithIdentity
      azure_rm_configurationstore: 
        config_store_name: contoso
        resource_group_name: myResourceGroup
        

    - name: ConfigurationStores_Delete
      azure_rm_configurationstore: 
        config_store_name: contoso
        resource_group_name: myResourceGroup
        

    - name: ConfigurationStores_Update
      azure_rm_configurationstore: 
        config_store_name: contoso
        resource_group_name: myResourceGroup
        

    - name: ConfigurationStores_Update_WithIdentity
      azure_rm_configurationstore: 
        config_store_name: contoso
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
name_sku_name:
  description:
    - The SKU name of the configuration store.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the configuration store.
  returned: always
  type: str
  sample: null
creation_date:
  description:
    - The creation date of configuration store.
  returned: always
  type: str
  sample: null
endpoint:
  description:
    - The DNS endpoint where the configuration store API will be available.
  returned: always
  type: str
  sample: null
encryption:
  description:
    - The encryption settings of the configuration store.
  returned: always
  type: dict
  sample: null
  contains:
    key_vault_properties:
      description:
        - Key vault properties.
      returned: always
      type: dict
      sample: null
      contains:
        key_identifier:
          description:
            - The URI of the key vault key used to encrypt data.
          returned: always
          type: str
          sample: null
        identity_client_id:
          description:
            - >-
              The client id of the identity which will be used to access key
              vault.
          returned: always
          type: str
          sample: null
private_endpoint_connections:
  description:
    - >-
      The list of private endpoint connections that are set up for this
      resource.
  returned: always
  type: list
  sample: null
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
    provisioning_state:
      description:
        - The provisioning status of the private endpoint connection.
      returned: always
      type: str
      sample: null
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
            - The private link service connection description.
          returned: always
          type: str
          sample: null
        actions_required:
          description:
            - >-
              Any action that is required beyond basic workflow (approve/
              reject/ disconnect)
          returned: always
          type: str
          sample: null
    id_properties_private_endpoint_id:
      description:
        - The resource Id for private endpoint
      returned: always
      type: str
      sample: null
public_network_access:
  description:
    - >-
      Control permission for data plane traffic coming from public networks
      while private endpoint is enabled.
  returned: always
  type: str
  sample: null
type_identity_type:
  description:
    - >-
      The type of managed identity used. The type 'SystemAssigned, UserAssigned'
      includes both an implicitly created identity and a set of user-assigned
      identities. The type 'None' will remove any identities.
  returned: always
  type: str
  sample: null
user_assigned_identities:
  description:
    - >-
      The list of user-assigned identities associated with the resource. The
      user-assigned identity dictionary keys will be ARM resource ids in the
      form:
      '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
  returned: always
  type: dictionary
  sample: null
principal_id:
  description:
    - >-
      The principal id of the identity. This property will only be provided for
      a system-assigned identity.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - >-
      The tenant id associated with the resource's identity. This property will
      only be provided for a system-assigned identity.
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
    from azure.mgmt.app import AppConfigurationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConfigurationStore(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            config_store_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    key_vault_properties=dict(
                        type='dict',
                        disposition='key_vault_properties',
                        options=dict(
                            key_identifier=dict(
                                type='str',
                                disposition='key_identifier'
                            ),
                            identity_client_id=dict(
                                type='str',
                                disposition='identity_client_id'
                            )
                        )
                    )
                )
            ),
            public_network_access=dict(
                type='str',
                disposition='/public_network_access',
                choices=['Enabled',
                         'Disabled']
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['None',
                         'SystemAssigned',
                         'UserAssigned',
                         'SystemAssigned, UserAssigned']
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.config_store_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConfigurationStore, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AppConfigurationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
                response = self.mgmt_client.configuration_stores.create(resource_group_name=self.resource_group_name,
                                                                        config_store_name=self.config_store_name,
                                                                        config_store_creation_parameters=self.body)
            else:
                response = self.mgmt_client.configuration_stores.update(resource_group_name=self.resource_group_name,
                                                                        config_store_name=self.config_store_name,
                                                                        config_store_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ConfigurationStore instance.')
            self.fail('Error creating the ConfigurationStore instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.configuration_stores.delete(resource_group_name=self.resource_group_name,
                                                                    config_store_name=self.config_store_name)
        except CloudError as e:
            self.log('Error attempting to delete the ConfigurationStore instance.')
            self.fail('Error deleting the ConfigurationStore instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.configuration_stores.get(resource_group_name=self.resource_group_name,
                                                                 config_store_name=self.config_store_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMConfigurationStore()


if __name__ == '__main__':
    main()
