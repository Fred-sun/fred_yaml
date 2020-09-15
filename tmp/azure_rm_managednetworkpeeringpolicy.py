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
module: azure_rm_managednetworkpeeringpolicy
version_added: '2.9'
short_description: Manage Azure ManagedNetworkPeeringPolicy instance.
description:
  - 'Create, update and delete instance of Azure ManagedNetworkPeeringPolicy.'
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
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  type:
    description:
      - Gets or sets the connectivity type of a network structure policy
    type: str
    choices:
      - HubAndSpokeTopology
      - MeshTopology
  spokes:
    description:
      - Gets or sets the spokes group IDs
    type: list
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  mesh:
    description:
      - Gets or sets the mesh group IDs
    type: list
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  id:
    description:
      - Resource Id
    type: str
  state:
    description:
      - Assert the state of the ManagedNetworkPeeringPolicy.
      - >-
        Use C(present) to create or update an ManagedNetworkPeeringPolicy and
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
    - name: ManagedNetworkPeeringPoliciesPut
      azure_rm_managednetworkpeeringpolicy: 
        managed_network_name: myManagedNetwork
        managed_network_peering_policy_name: myHubAndSpoke
        resource_group_name: myResourceGroup
        

    - name: ManagedNetworkPeeringPoliciesDelete
      azure_rm_managednetworkpeeringpolicy: 
        managed_network_name: myManagedNetwork
        managed_network_peering_policy_name: myHubAndSpoke
        resource_group_name: myResourceGroup
        

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
    - A unique read-only string that changes whenever the resource is updated.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedNetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagedNetworkPeeringPolicy(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['HubAndSpokeTopology',
                         'MeshTopology']
            ),
            spokes=dict(
                type='list',
                disposition='/spokes',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            mesh=dict(
                type='list',
                disposition='/mesh',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.managed_network_name = None
        self.managed_network_peering_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedNetworkPeeringPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ManagedNetworkManagementClient,
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
            response = self.mgmt_client.managed_network_peering_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                                          managed_network_name=self.managed_network_name,
                                                                                          managed_network_peering_policy_name=self.managed_network_peering_policy_name,
                                                                                          managed_network_policy=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedNetworkPeeringPolicy instance.')
            self.fail('Error creating the ManagedNetworkPeeringPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_network_peering_policies.delete(resource_group_name=self.resource_group_name,
                                                                                managed_network_name=self.managed_network_name,
                                                                                managed_network_peering_policy_name=self.managed_network_peering_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagedNetworkPeeringPolicy instance.')
            self.fail('Error deleting the ManagedNetworkPeeringPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_network_peering_policies.get(resource_group_name=self.resource_group_name,
                                                                             managed_network_name=self.managed_network_name,
                                                                             managed_network_peering_policy_name=self.managed_network_peering_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedNetworkPeeringPolicy()


if __name__ == '__main__':
    main()
