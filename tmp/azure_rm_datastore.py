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
module: azure_rm_datastore
version_added: '2.9'
short_description: Manage Azure DataStore instance.
description:
  - 'Create, update and delete instance of Azure DataStore.'
options:
  data_store_name:
    description:
      - The data store/repository name queried.
      - The data store/repository name to be created or updated.
      - The data store/repository name to be deleted.
    required: true
    type: str
  resource_group_name:
    description:
      - The Resource Group Name
    required: true
    type: str
  data_manager_name:
    description:
      - >-
        The name of the DataManager Resource within the specified resource
        group. DataManager names must be between 3 and 24 characters in length
        and use any alphanumeric and underscore only
    required: true
    type: str
  repository_id:
    description:
      - >-
        Arm Id for the manager resource to which the data source is associated.
        This is optional.
    type: str
  state:
    description:
      - Assert the state of the DataStore.
      - >-
        Use C(present) to create or update an DataStore and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
  extended_properties:
    description:
      - A generic json used differently by each data source type.
    type: any
  data_store_type_id:
    description:
      - The arm id of the data store type.
    type: str
  customer_secrets:
    description:
      - >-
        List of customer secrets containing a key identifier and key value. The
        key identifier is a way for the specific data source to understand the
        key. Value contains customer secret encrypted by the encryptionKeys.
    type: list
    suboptions:
      key_identifier:
        description:
          - >-
            The identifier to the data service input object which this secret
            corresponds to.
        required: true
        type: str
      key_value:
        description:
          - It contains the encrypted customer secret.
        required: true
        type: str
      algorithm:
        description:
          - The encryption algorithm used to encrypt data.
        required: true
        type: sealed-choice
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DataStores_CreateOrUpdate_DataSinkPUT162
      azure_rm_datastore: 
        data_manager_name: TestAzureSDKOperations
        data_store_name: TestAzureStorage1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataStores_CreateOrUpdate_DataSourcePUT162
      azure_rm_datastore: 
        data_manager_name: TestAzureSDKOperations
        data_store_name: TestStorSimpleSource1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataStores_Delete_DataSinkDELETE161
      azure_rm_datastore: 
        data_manager_name: TestAzureSDKOperations
        data_store_name: TestAzureStorage1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataStores_Delete_DataSourceDELETE161
      azure_rm_datastore: 
        data_manager_name: TestAzureSDKOperations
        data_store_name: TestStorSimpleSource1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
name:
  description:
    - Name of the object.
  returned: always
  type: str
  sample: null
id:
  description:
    - Id of the object.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of the object.
  returned: always
  type: str
  sample: null
repository_id:
  description:
    - >-
      Arm Id for the manager resource to which the data source is associated.
      This is optional.
  returned: always
  type: str
  sample: null
state:
  description:
    - State of the data source.
  returned: always
  type: sealed-choice
  sample: null
extended_properties:
  description:
    - A generic json used differently by each data source type.
  returned: always
  type: any
  sample: null
data_store_type_id:
  description:
    - The arm id of the data store type.
  returned: always
  type: str
  sample: null
customer_secrets:
  description:
    - >-
      List of customer secrets containing a key identifier and key value. The
      key identifier is a way for the specific data source to understand the
      key. Value contains customer secret encrypted by the encryptionKeys.
  returned: always
  type: list
  sample: null
  contains:
    key_identifier:
      description:
        - >-
          The identifier to the data service input object which this secret
          corresponds to.
      returned: always
      type: str
      sample: null
    key_value:
      description:
        - It contains the encrypted customer secret.
      returned: always
      type: str
      sample: null
    algorithm:
      description:
        - The encryption algorithm used to encrypt data.
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDataStore(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            data_store_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            repository_id=dict(
                type='str',
                disposition='/repository_id'
            ),
            state=dict(
                type='sealed-choice',
                disposition='/state'
            ),
            extended_properties=dict(
                type='any',
                disposition='/extended_properties'
            ),
            data_store_type_id=dict(
                type='str',
                disposition='/data_store_type_id'
            ),
            customer_secrets=dict(
                type='list',
                disposition='/customer_secrets',
                elements='dict',
                options=dict(
                    key_identifier=dict(
                        type='str',
                        disposition='key_identifier',
                        required=True
                    ),
                    key_value=dict(
                        type='str',
                        disposition='key_value',
                        required=True
                    ),
                    algorithm=dict(
                        type='sealed-choice',
                        disposition='algorithm',
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

        self.data_store_name = None
        self.resource_group_name = None
        self.data_manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataStore, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

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
            response = self.mgmt_client.data_stores.create_or_update(data_store_name=self.data_store_name,
                                                                     resource_group_name=self.resource_group_name,
                                                                     data_manager_name=self.data_manager_name,
                                                                     data_store=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DataStore instance.')
            self.fail('Error creating the DataStore instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.data_stores.delete(data_store_name=self.data_store_name,
                                                           resource_group_name=self.resource_group_name,
                                                           data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the DataStore instance.')
            self.fail('Error deleting the DataStore instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.data_stores.get(data_store_name=self.data_store_name,
                                                        resource_group_name=self.resource_group_name,
                                                        data_manager_name=self.data_manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDataStore()


if __name__ == '__main__':
    main()
