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
module: azure_rm_configurationstore_info
version_added: '2.9'
short_description: Get ConfigurationStore info.
description:
  - Get info of ConfigurationStore.
options:
  skip_token:
    description:
      - >-
        A skip token is used to continue retrieving items after an operation
        returns a partial result. If a previous response contains a nextLink
        element, the value of the nextLink element will include a skipToken
        parameter that specifies a starting point to use for subsequent calls.
    type: str
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    type: str
  config_store_name:
    description:
      - The name of the configuration store.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ConfigurationStores_List
      azure_rm_configurationstore_info: 
        {}
        

    - name: ConfigurationStores_ListByResourceGroup
      azure_rm_configurationstore_info: 
        resource_group_name: myResourceGroup
        

    - name: ConfigurationStores_Get
      azure_rm_configurationstore_info: 
        config_store_name: contoso
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
configuration_stores:
  description: >-
    A list of dict results where the key is the name of the ConfigurationStore
    and the values are the facts for that ConfigurationStore.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The collection value.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              The DNS endpoint where the configuration store API will be
              available.
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
                      The client id of the identity which will be used to access
                      key vault.
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
                    - The private link service connection description.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - >-
                      Any action that is required beyond basic workflow
                      (approve/ reject/ disconnect)
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
              Control permission for data plane traffic coming from public
              networks while private endpoint is enabled.
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - >-
              The type of managed identity used. The type 'SystemAssigned,
              UserAssigned' includes both an implicitly created identity and a
              set of user-assigned identities. The type 'None' will remove any
              identities.
          returned: always
          type: str
          sample: null
        user_assigned_identities:
          description:
            - >-
              The list of user-assigned identities associated with the resource.
              The user-assigned identity dictionary keys will be ARM resource
              ids in the form:
              '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
          returned: always
          type: dictionary
          sample: null
        principal_id:
          description:
            - >-
              The principal id of the identity. This property will only be
              provided for a system-assigned identity.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              The tenant id associated with the resource's identity. This
              property will only be provided for a system-assigned identity.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URI that can be used to request the next set of paged results.
      returned: always
      type: str
      sample: null
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
          The type of managed identity used. The type 'SystemAssigned,
          UserAssigned' includes both an implicitly created identity and a set
          of user-assigned identities. The type 'None' will remove any
          identities.
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
          The principal id of the identity. This property will only be provided
          for a system-assigned identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - >-
          The tenant id associated with the resource's identity. This property
          will only be provided for a system-assigned identity.
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
    from azure.mgmt.app import AppConfigurationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConfigurationStoreInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            skip_token=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            config_store_name=dict(
                type='str'
            )
        )

        self.skip_token = None
        self.resource_group_name = None
        self.config_store_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMConfigurationStoreInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AppConfigurationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.config_store_name is not None):
            self.results['configuration_stores'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['configuration_stores'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['configuration_stores'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.configuration_stores.get(resource_group_name=self.resource_group_name,
                                                                 config_store_name=self.config_store_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.configuration_stores.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                    skip_token=self.skip_token)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.configuration_stores.list(skip_token=self.skip_token)
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
    AzureRMConfigurationStoreInfo()


if __name__ == '__main__':
    main()
