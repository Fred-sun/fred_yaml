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
module: azure_rm_storagedomain_info
version_added: '2.9'
short_description: Get StorageDomain info.
description:
  - Get info of StorageDomain.
options:
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  storage_domain_name:
    description:
      - The storage domain name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageDomainsListByManager
      azure_rm_storagedomain_info: 
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: StorageDomainsGet
      azure_rm_storagedomain_info: 
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        storage_domain_name: sd-fs-HSDK-4XY4FI2IVG
        

'''

RETURN = '''
storage_domains:
  description: >-
    A list of dict results where the key is the name of the StorageDomain and
    the values are the facts for that StorageDomain.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        storage_account_credential_ids:
          description:
            - The storage account credentials.
          returned: always
          type: list
          sample: null
        encryption_key:
          description:
            - >-
              The encryption key used to encrypt the data. This is a user
              secret.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - >-
                  The value of the secret itself. If the secret is in plaintext
                  then EncryptionAlgorithm will be none and
                  EncryptionCertThumbprint will be null.
              returned: always
              type: str
              sample: null
            encryption_certificate_thumbprint:
              description:
                - Thumbprint certificate that was used to encrypt "Value"
              returned: always
              type: str
              sample: null
            encryption_algorithm:
              description:
                - Algorithm used to encrypt "Value"
              returned: always
              type: sealed-choice
              sample: null
        encryption_status:
          description:
            - The encryption status "Enabled | Disabled".
          returned: always
          type: sealed-choice
          sample: null
    id:
      description:
        - The identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type.
      returned: always
      type: str
      sample: null
    storage_account_credential_ids:
      description:
        - The storage account credentials.
      returned: always
      type: list
      sample: null
    encryption_key:
      description:
        - The encryption key used to encrypt the data. This is a user secret.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - >-
              The value of the secret itself. If the secret is in plaintext then
              EncryptionAlgorithm will be none and EncryptionCertThumbprint will
              be null.
          returned: always
          type: str
          sample: null
        encryption_certificate_thumbprint:
          description:
            - Thumbprint certificate that was used to encrypt "Value"
          returned: always
          type: str
          sample: null
        encryption_algorithm:
          description:
            - Algorithm used to encrypt "Value"
          returned: always
          type: sealed-choice
          sample: null
    encryption_status:
      description:
        - The encryption status "Enabled | Disabled".
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMStorageDomainInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            storage_domain_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.manager_name = None
        self.storage_domain_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-10-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMStorageDomainInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

        if (self.storage_domain_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['storage_domains'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['storage_domains'] = self.format_item(self.listbymanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.storage_domains.get(storage_domain_name=self.storage_domain_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanager(self):
        response = None

        try:
            response = self.mgmt_client.storage_domains.list_by_manager(resource_group_name=self.resource_group_name,
                                                                        manager_name=self.manager_name)
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
    AzureRMStorageDomainInfo()


if __name__ == '__main__':
    main()
