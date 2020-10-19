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
module: azure_rm_replica_info
version_added: '2.9'
short_description: Get Replica info.
description:
  - Get info of Replica.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ReplicasListByServer
      azure_rm_replica_info: 
        resource_group_name: TestGroup_WestCentralUS
        server_name: testserver-master
        

'''

RETURN = '''
replicas:
  description: >-
    A list of dict results where the key is the name of the Replica and the
    values are the facts for that Replica.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of servers
      returned: always
      type: list
      sample: null
      contains:
        identity:
          description:
            - The Azure Active Directory identity of the server.
          returned: always
          type: dict
          sample: null
          contains:
            principal_id:
              description:
                - The Azure Active Directory principal id.
              returned: always
              type: uuid
              sample: null
            type:
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
        sku:
          description:
            - The SKU (pricing tier) of the server.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the sku, typically, tier + family + cores, e.g.
                  B_Gen4_1, GP_Gen5_8.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - 'The tier of the particular SKU, e.g. Basic.'
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - >-
                  The scale up/out capacity, representing server's compute
                  units.
              returned: always
              type: integer
              sample: null
            size:
              description:
                - 'The size code, to be interpreted by resource as appropriate.'
              returned: always
              type: str
              sample: null
            family:
              description:
                - The family of hardware.
              returned: always
              type: str
              sample: null
        administrator_login:
          description:
            - >-
              The administrator's login name of a server. Can only be specified
              when the server is being created (and is required for creation).
          returned: always
          type: str
          sample: null
        version:
          description:
            - Server version.
          returned: always
          type: str
          sample: null
        sslenforcement:
          description:
            - Enable ssl enforcement or not when connect to server.
          returned: always
          type: sealed-choice
          sample: null
        minimal_tls_version:
          description:
            - Enforce a minimal Tls version for the server.
          returned: always
          type: str
          sample: null
        byok_enforcement:
          description:
            - >-
              Status showing whether the server data encryption is enabled with
              customer-managed keys.
          returned: always
          type: str
          sample: null
        infrastructure_encryption:
          description:
            - >-
              Status showing whether the server enabled infrastructure
              encryption.
          returned: always
          type: str
          sample: null
        user_visible_state:
          description:
            - A state of a server that is visible to user.
          returned: always
          type: str
          sample: null
        fully_qualified_domain_name:
          description:
            - The fully qualified domain name of a server.
          returned: always
          type: str
          sample: null
        earliest_restore_date:
          description:
            - Earliest restore point creation time (ISO8601 format)
          returned: always
          type: str
          sample: null
        storage_profile:
          description:
            - Storage profile of a server.
          returned: always
          type: dict
          sample: null
          contains:
            backup_retention_days:
              description:
                - Backup retention days for the server.
              returned: always
              type: integer
              sample: null
            geo_redundant_backup:
              description:
                - Enable Geo-redundant or not for server backup.
              returned: always
              type: str
              sample: null
            storage_mb:
              description:
                - Max storage allowed for a server.
              returned: always
              type: integer
              sample: null
            storage_autogrow:
              description:
                - Enable Storage Auto Grow.
              returned: always
              type: str
              sample: null
        replication_role:
          description:
            - The replication role of the server.
          returned: always
          type: str
          sample: null
        master_server_id:
          description:
            - The master server id of a replica server.
          returned: always
          type: str
          sample: null
        replica_capacity:
          description:
            - The maximum number of replicas that a master server can have.
          returned: always
          type: integer
          sample: null
        public_network_access:
          description:
            - >-
              Whether or not public network access is allowed for this server.
              Value is optional but if passed in, must be 'Enabled' or
              'Disabled'
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
                - Resource ID of the Private Endpoint Connection.
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

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.postgre import PostgreSQLManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReplicaInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
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
        self.query_parameters['api-version'] = '2017-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReplicaInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-12-01')

        if (self.resource_group_name is not None and
            self.server_name is not None):
            self.results['replicas'] = self.format_item(self.listbyserver())
        return self.results

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.replicas.list_by_server(resource_group_name=self.resource_group_name,
                                                                server_name=self.server_name)
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
    AzureRMReplicaInfo()


if __name__ == '__main__':
    main()
