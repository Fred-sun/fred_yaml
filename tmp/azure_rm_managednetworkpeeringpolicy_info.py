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
module: azure_rm_managednetworkpeeringpolicy_info
version_added: '2.9'
short_description: Get ManagedNetworkPeeringPolicy info.
description:
  - Get info of ManagedNetworkPeeringPolicy.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  managed_network_name:
    description:
      - The name of the Managed Network.
    required: true
    type: str
  managed_network_peering_policy_name:
    description:
      - The name of the Managed Network Peering Policy.
    type: str
  top:
    description:
      - May be used to limit the number of results in a page for list queries.
    type: integer
  skiptoken:
    description:
      - >-
        Skiptoken is only used if a previous operation returned a partial
        result. If a previous response contains a nextLink element, the value of
        the nextLink element will include a skiptoken parameter that specifies a
        starting point to use for subsequent calls.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ManagedNetworkPeeringPoliciesGet
      azure_rm_managednetworkpeeringpolicy_info: 
        managed_network_name: myManagedNetwork
        managed_network_peering_policy_name: myHubAndSpoke
        resource_group_name: myResourceGroup
        

    - name: ManagedNetworkPeeringPoliciesListByManagedNetwork
      azure_rm_managednetworkpeeringpolicy_info: 
        managed_network_name: myManagedNetwork
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
managed_network_peering_policies:
  description: >-
    A list of dict results where the key is the name of the
    ManagedNetworkPeeringPolicy and the values are the facts for that
    ManagedNetworkPeeringPolicy.
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
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the ManagedNetwork resource.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    type_properties_type:
      description:
        - Gets or sets the connectivity type of a network structure policy
      returned: always
      type: str
      sample: null
    spokes:
      description:
        - Gets or sets the spokes group IDs
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
    mesh:
      description:
        - Gets or sets the mesh group IDs
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
    id_properties_hub_id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    value:
      description:
        - Gets a page of Peering Policies
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - Provisioning state of the ManagedNetwork resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              A unique read-only string that changes whenever the resource is
              updated.
          returned: always
          type: str
          sample: null
        type_properties_type:
          description:
            - Gets or sets the connectivity type of a network structure policy
          returned: always
          type: str
          sample: null
        spokes:
          description:
            - Gets or sets the spokes group IDs
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource Id
              returned: always
              type: str
              sample: null
        mesh:
          description:
            - Gets or sets the mesh group IDs
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource Id
              returned: always
              type: str
              sample: null
        id_properties_hub_id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Gets the URL to get the next page of results.
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
    from azure.mgmt.managed import ManagedNetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagedNetworkPeeringPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_network_name=dict(
                type='str',
                required=True
            ),
            managed_network_peering_policy_name=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skiptoken=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.managed_network_name = None
        self.managed_network_peering_policy_name = None
        self.top = None
        self.skiptoken = None

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
        super(AzureRMManagedNetworkPeeringPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.managed_network_name is not None and
            self.managed_network_peering_policy_name is not None):
            self.results['managed_network_peering_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_network_name is not None):
            self.results['managed_network_peering_policies'] = self.format_item(self.listbymanagednetwork())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_network_peering_policies.get(resource_group_name=self.resource_group_name,
                                                                             managed_network_name=self.managed_network_name,
                                                                             managed_network_peering_policy_name=self.managed_network_peering_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanagednetwork(self):
        response = None

        try:
            response = self.mgmt_client.managed_network_peering_policies.list_by_managed_network(resource_group_name=self.resource_group_name,
                                                                                                 managed_network_name=self.managed_network_name,
                                                                                                 top=self.top,
                                                                                                 skiptoken=self.skiptoken)
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
    AzureRMManagedNetworkPeeringPolicyInfo()


if __name__ == '__main__':
    main()
