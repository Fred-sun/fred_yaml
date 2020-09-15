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
module: azure_rm_vault_info
version_added: '2.9'
short_description: Get Vault info.
description:
  - Get info of Vault.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    type: str
  vault_name:
    description:
      - The name of the recovery services vault.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List of Recovery Services Resources in SubscriptionId
      azure_rm_vault_info: 
        {}
        

    - name: List of Recovery Services Resources in ResourceGroup
      azure_rm_vault_info: 
        resource_group_name: Default-RecoveryServices-ResourceGroup
        

    - name: Get Recovery Services Resource
      azure_rm_vault_info: 
        resource_group_name: Default-RecoveryServices-ResourceGroup
        vault_name: swaggerExample
        

'''

RETURN = '''
vaults:
  description: >-
    A list of dict results where the key is the name of the Vault and the values
    are the facts for that Vault.
  returned: always
  type: complex
  contains:
    value:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        name_sku_name:
          description:
            - The Sku name.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning State.
          returned: always
          type: str
          sample: null
        upgrade_details:
          description:
            - Details for upgrading vault.
          returned: always
          type: dict
          sample: null
          contains:
            operation_id:
              description:
                - ID of the vault upgrade operation.
              returned: always
              type: str
              sample: null
            start_time_utc:
              description:
                - UTC time at which the upgrade operation has started.
              returned: always
              type: str
              sample: null
            last_updated_time_utc:
              description:
                - >-
                  UTC time at which the upgrade operation status was last
                  updated.
              returned: always
              type: str
              sample: null
            end_time_utc:
              description:
                - UTC time at which the upgrade operation has ended.
              returned: always
              type: str
              sample: null
            status:
              description:
                - Status of the vault upgrade operation.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  Message to the user containing information about the upgrade
                  operation.
              returned: always
              type: str
              sample: null
            trigger_type:
              description:
                - The way the vault upgrade was triggered.
              returned: always
              type: str
              sample: null
            upgraded_resource_id:
              description:
                - Resource ID of the upgraded vault.
              returned: always
              type: str
              sample: null
            previous_resource_id:
              description:
                - Resource ID of the vault before the upgrade.
              returned: always
              type: str
              sample: null
        private_endpoint_connections:
          description:
            - List of private endpoint connection.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  Format of id
                  subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.[Service]/{resource}/{resourceName}/privateEndpointConnections/{connectionName}.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Private Endpoint Connection Response Properties.
              returned: always
              type: dict
              sample: null
              contains:
                provisioning_state:
                  description:
                    - >-
                      Gets or sets provisioning state of the private endpoint
                      connection.
                  returned: always
                  type: str
                  sample: null
                private_endpoint:
                  description:
                    - >-
                      The Private Endpoint network resource that is linked to
                      the Private Endpoint connection.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    id:
                      description:
                        - Gets or sets id.
                      returned: always
                      type: str
                      sample: null
                private_link_service_connection_state:
                  description:
                    - Gets or sets private link service connection state.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    status:
                      description:
                        - Gets or sets the status.
                      returned: always
                      type: str
                      sample: null
                    description:
                      description:
                        - Gets or sets description.
                      returned: always
                      type: str
                      sample: null
                    actions_required:
                      description:
                        - Gets or sets actions required.
                      returned: always
                      type: str
                      sample: null
        private_endpoint_state_for_backup:
          description:
            - Private endpoint state for backup.
          returned: always
          type: str
          sample: null
        private_endpoint_state_for_site_recovery:
          description:
            - Private endpoint state for site recovery.
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
          type: str
          sample: null
    next_link:
      description:
        - ''
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    name_sku_name:
      description:
        - The Sku name.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning State.
      returned: always
      type: str
      sample: null
    upgrade_details:
      description:
        - Details for upgrading vault.
      returned: always
      type: dict
      sample: null
      contains:
        operation_id:
          description:
            - ID of the vault upgrade operation.
          returned: always
          type: str
          sample: null
        start_time_utc:
          description:
            - UTC time at which the upgrade operation has started.
          returned: always
          type: str
          sample: null
        last_updated_time_utc:
          description:
            - UTC time at which the upgrade operation status was last updated.
          returned: always
          type: str
          sample: null
        end_time_utc:
          description:
            - UTC time at which the upgrade operation has ended.
          returned: always
          type: str
          sample: null
        status:
          description:
            - Status of the vault upgrade operation.
          returned: always
          type: str
          sample: null
        message:
          description:
            - >-
              Message to the user containing information about the upgrade
              operation.
          returned: always
          type: str
          sample: null
        trigger_type:
          description:
            - The way the vault upgrade was triggered.
          returned: always
          type: str
          sample: null
        upgraded_resource_id:
          description:
            - Resource ID of the upgraded vault.
          returned: always
          type: str
          sample: null
        previous_resource_id:
          description:
            - Resource ID of the vault before the upgrade.
          returned: always
          type: str
          sample: null
    private_endpoint_connections:
      description:
        - List of private endpoint connection.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              Format of id
              subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.[Service]/{resource}/{resourceName}/privateEndpointConnections/{connectionName}.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Private Endpoint Connection Response Properties.
          returned: always
          type: dict
          sample: null
          contains:
            provisioning_state:
              description:
                - >-
                  Gets or sets provisioning state of the private endpoint
                  connection.
              returned: always
              type: str
              sample: null
            private_endpoint:
              description:
                - >-
                  The Private Endpoint network resource that is linked to the
                  Private Endpoint connection.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Gets or sets id.
                  returned: always
                  type: str
                  sample: null
            private_link_service_connection_state:
              description:
                - Gets or sets private link service connection state.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - Gets or sets the status.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Gets or sets description.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - Gets or sets actions required.
                  returned: always
                  type: str
                  sample: null
    private_endpoint_state_for_backup:
      description:
        - Private endpoint state for backup.
      returned: always
      type: str
      sample: null
    private_endpoint_state_for_site_recovery:
      description:
        - Private endpoint state for site recovery.
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
      type: str
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.recovery import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVaultInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            vault_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vault_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVaultInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-06-01')

        if (self.resource_group_name is not None and
            self.vault_name is not None):
            self.results['vaults'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['vaults'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['vaults'] = self.format_item(self.listbysubscriptionid())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vaults.get(resource_group_name=self.resource_group_name,
                                                   vault_name=self.vault_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.vaults.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscriptionid(self):
        response = None

        try:
            response = self.mgmt_client.vaults.list_by_subscription_id()
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
    AzureRMVaultInfo()


if __name__ == '__main__':
    main()
