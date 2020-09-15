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
module: azure_rm_storageaccountcredential
version_added: '2.9'
short_description: Manage Azure StorageAccountCredential instance.
description:
  - 'Create, update and delete instance of Azure StorageAccountCredential.'
options:
  storage_account_credential_name:
    description:
      - The name of storage account credential to be fetched.
      - The storage account credential name.
      - The name of the storage account credential.
    required: true
    type: str
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
  kind:
    description:
      - The Kind of the object. Currently only Series8000 is supported
    type: constant
  end_point:
    description:
      - The storage endpoint
    type: str
  sslstatus:
    description:
      - Signifies whether SSL needs to be enabled or not.
    type: sealed-choice
  access_key:
    description:
      - The details of the storage account password.
    type: dict
    suboptions:
      value:
        description:
          - The value of the secret.
        required: true
        type: str
      encryption_cert_thumbprint:
        description:
          - >-
            Thumbprint certificate that was used to encrypt "Value". If the
            value in unencrypted, it will be null.
        type: str
      encryption_algorithm:
        description:
          - The algorithm used to encrypt "Value".
        required: true
        type: sealed-choice
  state:
    description:
      - Assert the state of the StorageAccountCredential.
      - >-
        Use C(present) to create or update an StorageAccountCredential and
        C(absent) to delete it.
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
    - name: StorageAccountCredentialsCreateOrUpdate
      azure_rm_storageaccountcredential: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        storage_account_credential_name: SACForTest
        properties:
          access_key:
            encryption_algorithm: RSAES_PKCS1_v_1_5
            encryption_cert_thumbprint: A872A2DF196AC7682EE24791E7DE2E2A360F5926
            value: >-
              ATuJSkmrFk4h8r1jrZ4nd3nthLSddcguEO5QLO/NECUtTuB9kL4dNv3/jC4WOvFkeVr3x1UvfhlIeMmJBF1SMr6hR1JzD0xNU/TtQqUeXN7V3jk7I+2l67P9StuHWR6OMd3XOLwvznxOEQtEWpweDiobZU1ZiY03WafcGZFpV5j6tEoHeopoZ1J/GhPtkYmx+TqxzUN6qnir5rP3NSYiZciImP/qu8U9yUV/xpVRv39KvFc2Yr5SpKpMMRUj55XW10UnPer63M6KovF8X9Wi/fNnrZAs1Esl5XddZETGrW/e5B++VMJ6w0Q/uvPR+UBwrOU0804l0SzwdIe3qVVd0Q==
          end_point: blob.core.windows.net
          ssl_status: Enabled
        

    - name: StorageAccountCredentialsDelete
      azure_rm_storageaccountcredential: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        storage_account_credential_name: SACForTest
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the object.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
kind:
  description:
    - The Kind of the object. Currently only Series8000 is supported
  returned: always
  type: constant
  sample: null
end_point:
  description:
    - The storage endpoint
  returned: always
  type: str
  sample: null
sslstatus:
  description:
    - Signifies whether SSL needs to be enabled or not.
  returned: always
  type: sealed-choice
  sample: null
access_key:
  description:
    - The details of the storage account password.
  returned: always
  type: dict
  sample: null
  contains:
    value:
      description:
        - The value of the secret.
      returned: always
      type: str
      sample: null
    encryption_cert_thumbprint:
      description:
        - >-
          Thumbprint certificate that was used to encrypt "Value". If the value
          in unencrypted, it will be null.
      returned: always
      type: str
      sample: null
    encryption_algorithm:
      description:
        - The algorithm used to encrypt "Value".
      returned: always
      type: sealed-choice
      sample: null
volumes_count:
  description:
    - The count of volumes using this storage account credential.
  returned: always
  type: integer
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMStorageAccountCredential(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            storage_account_credential_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='constant',
                disposition='/kind'
            ),
            end_point=dict(
                type='str',
                disposition='/end_point'
            ),
            sslstatus=dict(
                type='sealed-choice',
                disposition='/sslstatus'
            ),
            access_key=dict(
                type='dict',
                disposition='/access_key',
                options=dict(
                    value=dict(
                        type='str',
                        disposition='value',
                        required=True
                    ),
                    encryption_cert_thumbprint=dict(
                        type='str',
                        disposition='encryption_cert_thumbprint'
                    ),
                    encryption_algorithm=dict(
                        type='sealed-choice',
                        disposition='encryption_algorithm',
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.storage_account_credential_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStorageAccountCredential, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
            response = self.mgmt_client.storage_account_credentials.create_or_update(storage_account_credential_name=self.storage_account_credential_name,
                                                                                     resource_group_name=self.resource_group_name,
                                                                                     manager_name=self.manager_name,
                                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StorageAccountCredential instance.')
            self.fail('Error creating the StorageAccountCredential instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.storage_account_credentials.delete(storage_account_credential_name=self.storage_account_credential_name,
                                                                           resource_group_name=self.resource_group_name,
                                                                           manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the StorageAccountCredential instance.')
            self.fail('Error deleting the StorageAccountCredential instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.storage_account_credentials.get(storage_account_credential_name=self.storage_account_credential_name,
                                                                        resource_group_name=self.resource_group_name,
                                                                        manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStorageAccountCredential()


if __name__ == '__main__':
    main()
