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
module: azure_rm_datamaskingpolicy
version_added: '2.9'
short_description: Manage Azure DataMaskingPolicy instance.
description:
  - 'Create, update and delete instance of Azure DataMaskingPolicy.'
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
      - The name of the database.
    required: true
    type: str
  datamaskingpolicyname:
    description:
      - The name of the database for which the data masking rule applies.
    required: true
    type: constant
  data_masking_state:
    description:
      - The state of the data masking policy.
    type: sealed-choice
  exempt_principals:
    description:
      - >-
        The list of the exempt principals. Specifies the semicolon-separated
        list of database users for which the data masking policy does not apply.
        The specified users receive data results without masking for all of the
        database queries.
    type: str
  state:
    description:
      - Assert the state of the DataMaskingPolicy.
      - >-
        Use C(present) to create or update an DataMaskingPolicy and C(absent) to
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
    - name: Create or update data masking policy max
      azure_rm_datamaskingpolicy: 
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        properties:
          data_masking_state: Enabled
          exempt_principals: testuser;
        

    - name: Create or update data masking policy min
      azure_rm_datamaskingpolicy: 
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        properties:
          data_masking_state: Enabled
        

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
    - The location of the data masking policy.
  returned: always
  type: str
  sample: null
kind:
  description:
    - 'The kind of data masking policy. Metadata, used for Azure portal.'
  returned: always
  type: str
  sample: null
data_masking_state:
  description:
    - The state of the data masking policy.
  returned: always
  type: sealed-choice
  sample: null
exempt_principals:
  description:
    - >-
      The list of the exempt principals. Specifies the semicolon-separated list
      of database users for which the data masking policy does not apply. The
      specified users receive data results without masking for all of the
      database queries.
  returned: always
  type: str
  sample: null
application_principals:
  description:
    - >-
      The list of the application principals. This is a legacy parameter and is
      no longer used.
  returned: always
  type: str
  sample: null
masking_level:
  description:
    - The masking level. This is a legacy parameter and is no longer used.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDataMaskingPolicy(AzureRMModuleBaseExt):
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
            datamaskingpolicyname=dict(
                type='constant',
                required=True
            ),
            data_masking_state=dict(
                type='sealed-choice',
                disposition='/data_masking_state'
            ),
            exempt_principals=dict(
                type='str',
                disposition='/exempt_principals'
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
        self.datamaskingpolicyname = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataMaskingPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.data_masking_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                               server_name=self.server_name,
                                                                               database_name=self.database_name,
                                                                               datamaskingpolicyname=self.datamaskingpolicyname,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DataMaskingPolicy instance.')
            self.fail('Error creating the DataMaskingPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.data_masking_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DataMaskingPolicy instance.')
            self.fail('Error deleting the DataMaskingPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.data_masking_policies.get(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  database_name=self.database_name,
                                                                  datamaskingpolicyname=self.datamaskingpolicyname)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDataMaskingPolicy()


if __name__ == '__main__':
    main()
