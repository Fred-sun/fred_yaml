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
module: azure_rm_mediaservice_info
version_added: '2.9'
short_description: Get Mediaservice info.
description:
  - Get info of Mediaservice.
options:
  resource_group_name:
    description:
      - The name of the resource group within the Azure subscription.
    type: str
  account_name:
    description:
      - The Media Services account name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all Media Services accounts
      azure_rm_mediaservice_info: 
        resource_group_name: contoso
        

    - name: Get a Media Services account by name
      azure_rm_mediaservice_info: 
        account_name: contosotv
        resource_group_name: contoso
        

'''

RETURN = '''
mediaservices:
  description: >-
    A list of dict results where the key is the name of the Mediaservice and the
    values are the facts for that Mediaservice.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A collection of MediaService items.
      returned: always
      type: list
      sample: null
      contains:
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
                  The ID of the storage account resource. Media Services relies
                  on tables and queues as well as blobs, so the primary storage
                  account must be a Standard Storage account (either
                  Microsoft.ClassicStorage or Microsoft.Storage). Blob only
                  storage accounts can be added as secondary storage accounts.
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
                      The URL of the Key Vault key used to encrypt the account.
                      The key may either be versioned (for example
                      https://vault/keys/mykey/version1) or reference a key
                      without a version (for example https://vault/keys/mykey).
                  returned: always
                  type: str
                  sample: null
                current_key_identifier:
                  description:
                    - >-
                      The current key used to encrypt the Media Services
                      account, including the key version.
                  returned: always
                  type: str
                  sample: null
    odata_next_link:
      description:
        - >-
          A link to the next page of the collection (when the collection
          contains too many results to return in one response).
      returned: always
      type: str
      sample: null
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
              must be a Standard Storage account (either
              Microsoft.ClassicStorage or Microsoft.Storage). Blob only storage
              accounts can be added as secondary storage accounts.
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
                  The URL of the Key Vault key used to encrypt the account. The
                  key may either be versioned (for example
                  https://vault/keys/mykey/version1) or reference a key without
                  a version (for example https://vault/keys/mykey).
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMediaserviceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            account_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMediaserviceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None):
            self.results['mediaservices'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['mediaservices'] = self.format_item(self.list())
        elif (self.account_name is not None):
            self.results['mediaservices'] = self.format_item(self.getbysubscription())
        else:
            self.results['mediaservices'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.mediaservices.get(resource_group_name=self.resource_group_name,
                                                          account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.mediaservices.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.mediaservices.get_by_subscription(account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.mediaservices.list_by_subscription()
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
    AzureRMMediaserviceInfo()


if __name__ == '__main__':
    main()
