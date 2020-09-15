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
module: azure_rm_clusterprincipalassignment_info
version_added: '2.9'
short_description: Get ClusterPrincipalAssignment info.
description:
  - Get info of ClusterPrincipalAssignment.
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
  principal_assignment_name:
    description:
      - The name of the Kusto principalAssignment.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: KustoClusterPrincipalAssignmentsGet
      azure_rm_clusterprincipalassignment_info: 
        cluster_name: kustoclusterrptest4
        principal_assignment_name: kustoprincipal1
        resource_group_name: kustorptest
        

    - name: KustoPrincipalAssignmentsList
      azure_rm_clusterprincipalassignment_info: 
        cluster_name: kustoclusterrptest4
        resource_group_name: kustorptest
        

'''

RETURN = '''
cluster_principal_assignments:
  description: >-
    A list of dict results where the key is the name of the
    ClusterPrincipalAssignment and the values are the facts for that
    ClusterPrincipalAssignment.
  returned: always
  type: complex
  contains:
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
          The principal ID assigned to the cluster principal. It can be a user
          email, application ID, or security group name.
      returned: always
      type: str
      sample: null
    role:
      description:
        - Cluster principal role.
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
    value:
      description:
        - The list of Kusto cluster principal assignments.
      returned: always
      type: list
      sample: null
      contains:
        principal_id:
          description:
            - >-
              The principal ID assigned to the cluster principal. It can be a
              user email, application ID, or security group name.
          returned: always
          type: str
          sample: null
        role:
          description:
            - Cluster principal role.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.kusto import KustoManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMClusterPrincipalAssignmentInfo(AzureRMModuleBase):
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
            principal_assignment_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.principal_assignment_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-14'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMClusterPrincipalAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(KustoManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-14')

        if (self.resource_group_name is not None and
            self.cluster_name is not None and
            self.principal_assignment_name is not None):
            self.results['cluster_principal_assignments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.cluster_name is not None):
            self.results['cluster_principal_assignments'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.cluster_principal_assignments.get(resource_group_name=self.resource_group_name,
                                                                          cluster_name=self.cluster_name,
                                                                          principal_assignment_name=self.principal_assignment_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.cluster_principal_assignments.list(resource_group_name=self.resource_group_name,
                                                                           cluster_name=self.cluster_name)
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
    AzureRMClusterPrincipalAssignmentInfo()


if __name__ == '__main__':
    main()
