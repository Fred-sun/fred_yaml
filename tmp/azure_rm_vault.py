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
module: azure_rm_vault
version_added: '2.9'
short_description: Manage Azure Vault instance.
description:
  - 'Create, update and delete instance of Azure Vault.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
    type: str
  vault_name:
    description:
      - The name of the recovery services vault.
    required: true
    type: str
  e_tag:
    description:
      - Optional ETag.
    type: str
  location:
    description:
      - Resource location.
    type: str
  name:
    description:
      - The Sku name.
    type: str
    choices:
      - Standard
      - RS0
  type:
    description:
      - The identity type.
    type: str
    choices:
      - SystemAssigned
      - None
  state:
    description:
      - Assert the state of the Vault.
      - Use C(present) to create or update an Vault and C(absent) to delete it.
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
    - name: Create of Update Recovery Services vault
      azure_rm_vault: 
        resource_group_name: Default-RecoveryServices-ResourceGroup
        vault_name: swaggerExample
        identity:
          type: SystemAssigned
        location: West US
        properties: {}
        sku:
          name: Standard
        

    - name: Delete Recovery Services Vault
      azure_rm_vault: 
        resource_group_name: Default-RecoveryServices-ResourceGroup
        vault_name: swaggerExample
        

    - name: Update Resource
      azure_rm_vault: 
        resource_group_name: HelloWorld
        vault_name: swaggerExample
        tags:
          patch_key: PatchKeyUpdated
        

'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.recovery import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVault(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vault_name=dict(
                type='str',
                required=True
            ),
            e_tag=dict(
                type='str',
                disposition='/e_tag'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            name=dict(
                type='str',
                disposition='/name',
                choices=['Standard',
                         'RS0']
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['SystemAssigned',
                         'None']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vault_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVault, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-06-01')

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
            response = self.mgmt_client.vaults.create_or_update(resource_group_name=self.resource_group_name,
                                                                vault_name=self.vault_name,
                                                                vault=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Vault instance.')
            self.fail('Error creating the Vault instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vaults.delete(resource_group_name=self.resource_group_name,
                                                      vault_name=self.vault_name)
        except CloudError as e:
            self.log('Error attempting to delete the Vault instance.')
            self.fail('Error deleting the Vault instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vaults.get(resource_group_name=self.resource_group_name,
                                                   vault_name=self.vault_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVault()


if __name__ == '__main__':
    main()
