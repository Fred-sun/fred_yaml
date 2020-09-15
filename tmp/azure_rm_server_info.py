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
module: azure_rm_server_info
version_added: '2.9'
short_description: Get Server info.
description:
  - Get info of Server.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
  server_name:
    description:
      - The name of the server.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List servers by resource group
      azure_rm_server_info: 
        resource_group_name: sqlcrudtest-7398
        

    - name: Get server
      azure_rm_server_info: 
        resource_group_name: sqlcrudtest-7398
        server_name: sqlcrudtest-4645
        

    - name: List servers
      azure_rm_server_info: 
        {}
        

'''

RETURN = '''
servers:
  description: >-
    A list of dict results where the key is the name of the Server and the
    values are the facts for that Server.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - >-
              Kind of sql server. This is metadata used for the Azure portal
              experience.
          returned: always
          type: str
          sample: null
        administrator_login:
          description:
            - >-
              Administrator username for the server. Once created it cannot be
              changed.
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
                        - >-
                          The actions required for private link service
                          connection.
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
              Whether or not public endpoint access is allowed for this server. 
              Value is optional but if passed in, must be 'Enabled' or
              'Disabled'
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
              The identity type. Set this to 'SystemAssigned' in order to
              automatically create and assign an Azure Active Directory
              principal for the resource.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The Azure Active Directory tenant id.
          returned: always
          type: uuid
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
        - >-
          Kind of sql server. This is metadata used for the Azure portal
          experience.
      returned: always
      type: str
      sample: null
    administrator_login:
      description:
        - >-
          Administrator username for the server. Once created it cannot be
          changed.
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
          Whether or not public endpoint access is allowed for this server. 
          Value is optional but if passed in, must be 'Enabled' or 'Disabled'
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
          The identity type. Set this to 'SystemAssigned' in order to
          automatically create and assign an Azure Active Directory principal
          for the resource.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMServerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            server_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMServerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None):
            self.results['servers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['servers'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['servers'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.servers.get(resource_group_name=self.resource_group_name,
                                                    server_name=self.server_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.servers.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.servers.list()
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
    AzureRMServerInfo()


if __name__ == '__main__':
    main()
