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
module: azure_rm_serverazureadadministrator
version_added: '2.9'
short_description: Manage Azure ServerAzureADAdministrator instance.
description:
  - 'Create, update and delete instance of Azure ServerAzureADAdministrator.'
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
  administrator_name:
    description:
      - The name of server active directory administrator.
    required: true
    type: str
    choices:
      - ActiveDirectory
  administrator_type:
    description:
      - Type of the sever administrator.
    type: str
    choices:
      - ActiveDirectory
  login:
    description:
      - Login name of the server administrator.
    type: str
  sid:
    description:
      - SID (object ID) of the server administrator.
    type: uuid
  tenant_id:
    description:
      - Tenant ID of the administrator.
    type: uuid
  state:
    description:
      - Assert the state of the ServerAzureADAdministrator.
      - >-
        Use C(present) to create or update an ServerAzureADAdministrator and
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
    - name: Creates or updates an existing Azure Active Directory administrator.
      azure_rm_serverazureadadministrator: 
        administrator_name: ActiveDirectory
        resource_group_name: sqlcrudtest-4799
        server_name: sqlcrudtest-6440
        properties:
          administrator_type: ActiveDirectory
          login: bob@contoso.com
          sid: c6b82b90-a647-49cb-8a62-0d2d3cb7ac7c
          tenant_id: c6b82b90-a647-49cb-8a62-0d2d3cb7ac7c
        

    - name: Delete Azure Active Directory administrator.
      azure_rm_serverazureadadministrator: 
        administrator_name: ActiveDirectory
        resource_group_name: sqlcrudtest-4799
        server_name: sqlcrudtest-6440
        

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
administrator_type:
  description:
    - Type of the sever administrator.
  returned: always
  type: str
  sample: null
login:
  description:
    - Login name of the server administrator.
  returned: always
  type: str
  sample: null
sid:
  description:
    - SID (object ID) of the server administrator.
  returned: always
  type: uuid
  sample: null
tenant_id:
  description:
    - Tenant ID of the administrator.
  returned: always
  type: uuid
  sample: null
azure_ad_only_authentication:
  description:
    - Azure Active Directory only Authentication enabled.
  returned: always
  type: bool
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


class AzureRMServerAzureADAdministrator(AzureRMModuleBaseExt):
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
            administrator_name=dict(
                type='str',
                choices=['ActiveDirectory'],
                required=True
            ),
            administrator_type=dict(
                type='str',
                disposition='/administrator_type',
                choices=['ActiveDirectory']
            ),
            login=dict(
                type='str',
                disposition='/login'
            ),
            sid=dict(
                type='uuid',
                disposition='/sid'
            ),
            tenant_id=dict(
                type='uuid',
                disposition='/tenant_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.administrator_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServerAzureADAdministrator, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-06-01-preview')

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
            response = self.mgmt_client.server_azure_adadministrators.create_or_update(resource_group_name=self.resource_group_name,
                                                                                       server_name=self.server_name,
                                                                                       administrator_name=self.administrator_name,
                                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ServerAzureADAdministrator instance.')
            self.fail('Error creating the ServerAzureADAdministrator instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.server_azure_adadministrators.delete(resource_group_name=self.resource_group_name,
                                                                             server_name=self.server_name,
                                                                             administrator_name=self.administrator_name)
        except CloudError as e:
            self.log('Error attempting to delete the ServerAzureADAdministrator instance.')
            self.fail('Error deleting the ServerAzureADAdministrator instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.server_azure_adadministrators.get(resource_group_name=self.resource_group_name,
                                                                          server_name=self.server_name,
                                                                          administrator_name=self.administrator_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServerAzureADAdministrator()


if __name__ == '__main__':
    main()
