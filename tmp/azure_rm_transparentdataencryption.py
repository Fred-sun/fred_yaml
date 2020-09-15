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
module: azure_rm_transparentdataencryption
version_added: '2.9'
short_description: Manage Azure TransparentDataEncryption instance.
description:
  - 'Create, update and delete instance of Azure TransparentDataEncryption.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - >-
        The name of the database for which setting the transparent data
        encryption applies.
      - >-
        The name of the database for which the transparent data encryption
        applies.
    required: true
    type: str
  transparent_data_encryption_name:
    description:
      - The name of the transparent data encryption configuration.
    required: true
    type: str
    choices:
      - current
  status:
    description:
      - The status of the database transparent data encryption.
    type: sealed-choice
  state:
    description:
      - Assert the state of the TransparentDataEncryption.
      - >-
        Use C(present) to create or update an TransparentDataEncryption and
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
    - name: Create or update a database's transparent data encryption configuration
      azure_rm_transparentdataencryption: 
        database_name: sqlcrudtest-9187
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        transparent_data_encryption_name: current
        properties:
          status: Enabled
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
status:
  description:
    - The status of the database transparent data encryption.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTransparentDataEncryption(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            transparent_data_encryption_name=dict(
                type='str',
                choices=['current'],
                required=True
            ),
            status=dict(
                type='sealed-choice',
                disposition='/status'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.transparent_data_encryption_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTransparentDataEncryption, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

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
            response = self.mgmt_client.transparent_data_encryptions.create_or_update(resource_group_name=self.resource_group_name,
                                                                                      server_name=self.server_name,
                                                                                      database_name=self.database_name,
                                                                                      transparent_data_encryption_name=self.transparent_data_encryption_name,
                                                                                      parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the TransparentDataEncryption instance.')
            self.fail('Error creating the TransparentDataEncryption instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.transparent_data_encryptions.delete()
        except CloudError as e:
            self.log('Error attempting to delete the TransparentDataEncryption instance.')
            self.fail('Error deleting the TransparentDataEncryption instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.transparent_data_encryptions.get(resource_group_name=self.resource_group_name,
                                                                         server_name=self.server_name,
                                                                         database_name=self.database_name,
                                                                         transparent_data_encryption_name=self.transparent_data_encryption_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTransparentDataEncryption()


if __name__ == '__main__':
    main()
