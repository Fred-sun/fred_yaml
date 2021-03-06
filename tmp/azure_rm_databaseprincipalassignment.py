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
module: azure_rm_databaseprincipalassignment
version_added: '2.9'
short_description: Manage Azure DatabasePrincipalAssignment instance.
description:
  - 'Create, update and delete instance of Azure DatabasePrincipalAssignment.'
options:
  resource_group_name:
    description:
      - The name of the resource group containing the Kusto cluster.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the Kusto cluster.
    required: true
    type: str
  database_name:
    description:
      - The name of the database in the Kusto cluster.
    required: true
    type: str
  principal_assignment_name:
    description:
      - The name of the Kusto principalAssignment.
    required: true
    type: str
  principal_id:
    description:
      - >-
        The principal ID assigned to the database principal. It can be a user
        email, application ID, or security group name.
    type: str
  role:
    description:
      - Database principal role.
    type: str
    choices:
      - Admin
      - Ingestor
      - Monitor
      - User
      - UnrestrictedViewers
      - Viewer
  tenant_id:
    description:
      - The tenant id of the principal
    type: str
  principal_type:
    description:
      - Principal type.
    type: str
    choices:
      - App
      - Group
      - User
  state:
    description:
      - Assert the state of the DatabasePrincipalAssignment.
      - >-
        Use C(present) to create or update an DatabasePrincipalAssignment and
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
    - name: KustoDatabasePrincipalAssignmentsCreateOrUpdate
      azure_rm_databaseprincipalassignment: 
        cluster_name: kustoclusterrptest4
        database_name: Kustodatabase8
        principal_assignment_name: kustoprincipal1
        resource_group_name: kustorptest
        properties:
          principal_id: 87654321-1234-1234-1234-123456789123
          principal_type: App
          role: Admin
          tenant_id: 12345678-1234-1234-1234-123456789123
        

    - name: KustoDatabasePrincipalAssignmentsDelete
      azure_rm_databaseprincipalassignment: 
        cluster_name: kustoclusterrptest4
        database_name: Kustodatabase8
        principal_assignment_name: kustoprincipal1
        resource_group_name: kustorptest
        

'''

RETURN = '''
id:
  description:
    - >-
      Fully qualified resource Id for the resource. Ex -
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource. Ex- Microsoft.Compute/virtualMachines or
      Microsoft.Storage/storageAccounts.
  returned: always
  type: str
  sample: null
principal_id:
  description:
    - >-
      The principal ID assigned to the database principal. It can be a user
      email, application ID, or security group name.
  returned: always
  type: str
  sample: null
role:
  description:
    - Database principal role.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The tenant id of the principal
  returned: always
  type: str
  sample: null
principal_type:
  description:
    - Principal type.
  returned: always
  type: str
  sample: null
tenant_name:
  description:
    - The tenant name of the principal
  returned: always
  type: str
  sample: null
principal_name:
  description:
    - The principal name
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioned state of the resource.
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
    from azure.mgmt.kusto import KustoManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDatabasePrincipalAssignment(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            principal_assignment_name=dict(
                type='str',
                required=True
            ),
            principal_id=dict(
                type='str',
                disposition='/principal_id'
            ),
            role=dict(
                type='str',
                disposition='/role',
                choices=['Admin',
                         'Ingestor',
                         'Monitor',
                         'User',
                         'UnrestrictedViewers',
                         'Viewer']
            ),
            tenant_id=dict(
                type='str',
                disposition='/tenant_id'
            ),
            principal_type=dict(
                type='str',
                disposition='/principal_type',
                choices=['App',
                         'Group',
                         'User']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.database_name = None
        self.principal_assignment_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDatabasePrincipalAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(KustoManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-14')

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
            response = self.mgmt_client.database_principal_assignments.create_or_update(resource_group_name=self.resource_group_name,
                                                                                        cluster_name=self.cluster_name,
                                                                                        database_name=self.database_name,
                                                                                        principal_assignment_name=self.principal_assignment_name,
                                                                                        parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DatabasePrincipalAssignment instance.')
            self.fail('Error creating the DatabasePrincipalAssignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.database_principal_assignments.delete(resource_group_name=self.resource_group_name,
                                                                              cluster_name=self.cluster_name,
                                                                              database_name=self.database_name,
                                                                              principal_assignment_name=self.principal_assignment_name)
        except CloudError as e:
            self.log('Error attempting to delete the DatabasePrincipalAssignment instance.')
            self.fail('Error deleting the DatabasePrincipalAssignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.database_principal_assignments.get(resource_group_name=self.resource_group_name,
                                                                           cluster_name=self.cluster_name,
                                                                           database_name=self.database_name,
                                                                           principal_assignment_name=self.principal_assignment_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDatabasePrincipalAssignment()


if __name__ == '__main__':
    main()
