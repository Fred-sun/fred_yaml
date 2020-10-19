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
module: azure_rm_server
version_added: '2.9'
short_description: Manage Azure Server instance.
description:
  - 'Create, update and delete instance of Azure Server.'
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
  location:
    description:
      - Resource location.
    type: str
  administrator_login:
    description:
      - >-
        Administrator username for the server. Once created it cannot be
        changed.
    type: str
  administrator_login_password:
    description:
      - The administrator login password (required for server creation).
    type: str
  version:
    description:
      - The version of the server.
    type: str
  minimal_tls_version:
    description:
      - 'Minimal TLS version. Allowed values: ''1.0'', ''1.1'', ''1.2'''
    type: str
  public_network_access:
    description:
      - >-
        Whether or not public endpoint access is allowed for this server.  Value
        is optional but if passed in, must be 'Enabled' or 'Disabled'
    type: str
    choices:
      - Enabled
      - Disabled
  type:
    description:
      - >-
        The identity type. Set this to 'SystemAssigned' in order to
        automatically create and assign an Azure Active Directory principal for
        the resource.
    type: str
    choices:
      - SystemAssigned
  state:
    description:
      - Assert the state of the Server.
      - Use C(present) to create or update an Server and C(absent) to delete it.
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
    - name: Create server
      azure_rm_server: 
        resource_group_name: sqlcrudtest-7398
        server_name: sqlcrudtest-4645
        location: Japan East
        properties:
          administrator_login: dummylogin
          administrator_login_password: Un53cuRE!
        

    - name: Delete server
      azure_rm_server: 
        resource_group_name: sqlcrudtest-7398
        server_name: sqlcrudtest-6661
        

    - name: Update a server
      azure_rm_server: 
        resource_group_name: sqlcrudtest-7398
        server_name: sqlcrudtest-4645
        properties:
          administrator_login: dummylogin
          administrator_login_password: Un53cuRE!
        

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
kind:
  description:
    - Kind of sql server. This is metadata used for the Azure portal experience.
  returned: always
  type: str
  sample: null
administrator_login:
  description:
    - Administrator username for the server. Once created it cannot be changed.
  returned: always
  type: str
  sample: null
administrator_login_password:
  description:
    - The administrator login password (required for server creation).
  returned: always
  type: str
  sample: null
version:
  description:
    - The version of the server.
  returned: always
  type: str
  sample: null
state:
  description:
    - The state of the server.
  returned: always
  type: str
  sample: null
fully_qualified_domain_name:
  description:
    - The fully qualified domain name of the server.
  returned: always
  type: str
  sample: null
private_endpoint_connections:
  description:
    - List of private endpoint connections on a server
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Private endpoint connection properties
      returned: always
      type: dict
      sample: null
      contains:
        private_endpoint:
          description:
            - Private endpoint which the connection belongs to.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource id of the private endpoint.
              returned: always
              type: str
              sample: null
        private_link_service_connection_state:
          description:
            - Connection state of the private endpoint connection.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - The private link service connection status.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The private link service connection description.
              returned: always
              type: str
              sample: null
            actions_required:
              description:
                - The actions required for private link service connection.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - State of the private endpoint connection.
          returned: always
          type: str
          sample: null
minimal_tls_version:
  description:
    - 'Minimal TLS version. Allowed values: ''1.0'', ''1.1'', ''1.2'''
  returned: always
  type: str
  sample: null
public_network_access:
  description:
    - >-
      Whether or not public endpoint access is allowed for this server.  Value
      is optional but if passed in, must be 'Enabled' or 'Disabled'
  returned: always
  type: str
  sample: null
principal_id:
  description:
    - The Azure Active Directory principal id.
  returned: always
  type: uuid
  sample: null
type_identity_type:
  description:
    - >-
      The identity type. Set this to 'SystemAssigned' in order to automatically
      create and assign an Azure Active Directory principal for the resource.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The Azure Active Directory tenant id.
  returned: always
  type: uuid
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


class AzureRMServer(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            administrator_login=dict(
                type='str',
                disposition='/administrator_login'
            ),
            administrator_login_password=dict(
                type='str',
                disposition='/administrator_login_password'
            ),
            version=dict(
                type='str',
                disposition='/version'
            ),
            minimal_tls_version=dict(
                type='str',
                disposition='/minimal_tls_version'
            ),
            public_network_access=dict(
                type='str',
                disposition='/public_network_access',
                choices=['Enabled',
                         'Disabled']
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['SystemAssigned']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.servers.create_or_update(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Server instance.')
            self.fail('Error creating the Server instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.servers.delete(resource_group_name=self.resource_group_name,
                                                       server_name=self.server_name)
        except CloudError as e:
            self.log('Error attempting to delete the Server instance.')
            self.fail('Error deleting the Server instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.servers.get(resource_group_name=self.resource_group_name,
                                                    server_name=self.server_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMServer()


if __name__ == '__main__':
    main()
