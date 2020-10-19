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
module: azure_rm_mediaservice
version_added: '2.9'
short_description: Manage Azure Mediaservice instance.
description:
  - 'Create, update and delete instance of Azure Mediaservice.'
options:
  resource_group_name:
    description:
      - The name of the resource group within the Azure subscription.
    required: true
    type: str
  account_name:
    description:
      - The Media Services account name.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  type:
    description:
      - The identity type.
    type: str
    choices:
      - SystemAssigned
      - None
  storage_accounts:
    description:
      - The storage accounts for this resource.
    type: list
    suboptions:
      id:
        description:
          - >-
            The ID of the storage account resource. Media Services relies on
            tables and queues as well as blobs, so the primary storage account
            must be a Standard Storage account (either Microsoft.ClassicStorage
            or Microsoft.Storage). Blob only storage accounts can be added as
            secondary storage accounts.
        type: str
      type:
        description:
          - The type of the storage account.
        required: true
        type: str
        choices:
          - Primary
          - Secondary
  storage_authentication:
    description:
      - undefined
    type: str
    choices:
      - System
      - ManagedIdentity
  encryption:
    description:
      - The account encryption properties.
    type: dict
    suboptions:
      type:
        description:
          - The type of key used to encrypt the Account Key.
        required: true
        type: str
        choices:
          - SystemKey
          - CustomerKey
      key_vault_properties:
        description:
          - The properties of the key used to encrypt the account.
        type: dict
        suboptions:
          key_identifier:
            description:
              - >-
                The URL of the Key Vault key used to encrypt the account. The
                key may either be versioned (for example
                https://vault/keys/mykey/version1) or reference a key without a
                version (for example https://vault/keys/mykey).
            type: str
          current_key_identifier:
            description:
              - >-
                The current key used to encrypt the Media Services account,
                including the key version.
            type: str
  state:
    description:
      - Assert the state of the Mediaservice.
      - >-
        Use C(present) to create or update an Mediaservice and C(absent) to
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
    - name: Create a Media Services account
      azure_rm_mediaservice: 
        account_name: contososports
        resource_group_name: contoso
        location: South Central US
        properties:
          storage_accounts:
            - type: Primary
              id: >-
                /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contoso/providers/Microsoft.Storage/storageAccounts/contososportsstore
        tags:
          key1: value1
          key2: value2
        

    - name: Delete a Media Services account
      azure_rm_mediaservice: 
        account_name: contososports
        resource_group_name: contoso
        

    - name: Update a Media Services accounts
      azure_rm_mediaservice: 
        account_name: contososports
        resource_group_name: contoso
        location: South Central US
        tags:
          key1: value3
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
type_identity_type:
  description:
    - The identity type.
  returned: always
  type: str
  sample: null
principal_id:
  description:
    - The Principal ID of the identity.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The Tenant ID of the identity.
  returned: always
  type: str
  sample: null
media_service_id:
  description:
    - The Media Services account ID.
  returned: always
  type: uuid
  sample: null
storage_accounts:
  description:
    - The storage accounts for this resource.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - >-
          The ID of the storage account resource. Media Services relies on
          tables and queues as well as blobs, so the primary storage account
          must be a Standard Storage account (either Microsoft.ClassicStorage or
          Microsoft.Storage). Blob only storage accounts can be added as
          secondary storage accounts.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the storage account.
      returned: always
      type: str
      sample: null
storage_authentication:
  description:
    - ''
  returned: always
  type: str
  sample: null
encryption:
  description:
    - The account encryption properties.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - The type of key used to encrypt the Account Key.
      returned: always
      type: str
      sample: null
    key_vault_properties:
      description:
        - The properties of the key used to encrypt the account.
      returned: always
      type: dict
      sample: null
      contains:
        key_identifier:
          description:
            - >-
              The URL of the Key Vault key used to encrypt the account. The key
              may either be versioned (for example
              https://vault/keys/mykey/version1) or reference a key without a
              version (for example https://vault/keys/mykey).
          returned: always
          type: str
          sample: null
        current_key_identifier:
          description:
            - >-
              The current key used to encrypt the Media Services account,
              including the key version.
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
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMediaservice(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['SystemAssigned',
                         'None']
            ),
            storage_accounts=dict(
                type='list',
                disposition='/storage_accounts',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    ),
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['Primary',
                                 'Secondary'],
                        required=True
                    )
                )
            ),
            storage_authentication=dict(
                type='str',
                disposition='/storage_authentication',
                choices=['System',
                         'ManagedIdentity']
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['SystemKey',
                                 'CustomerKey'],
                        required=True
                    ),
                    key_vault_properties=dict(
                        type='dict',
                        disposition='key_vault_properties',
                        options=dict(
                            key_identifier=dict(
                                type='str',
                                disposition='key_identifier'
                            ),
                            current_key_identifier=dict(
                                type='str',
                                updatable=False,
                                disposition='current_key_identifier'
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
        self.account_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMediaservice, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
            response = self.mgmt_client.mediaservices.create_or_update(resource_group_name=self.resource_group_name,
                                                                       account_name=self.account_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Mediaservice instance.')
            self.fail('Error creating the Mediaservice instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.mediaservices.delete(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name)
        except CloudError as e:
            self.log('Error attempting to delete the Mediaservice instance.')
            self.fail('Error deleting the Mediaservice instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.mediaservices.get(resource_group_name=self.resource_group_name,
                                                          account_name=self.account_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMediaservice()


if __name__ == '__main__':
    main()
