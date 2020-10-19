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
module: azure_rm_managednetwork
version_added: '2.9'
short_description: Manage Azure ManagedNetwork instance.
description:
  - 'Create, update and delete instance of Azure ManagedNetwork.'
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
  location:
    description:
      - The geo-location where the resource lives
    type: str
  management_groups:
    description:
      - The collection of management groups covered by the Managed Network
    type: list
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  subscriptions:
    description:
      - The collection of subscriptions covered by the Managed Network
    type: list
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  virtual_networks:
    description:
      - The collection of virtual nets covered by the Managed Network
    type: list
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  subnets:
    description:
      - The collection of  subnets covered by the Managed Network
    type: list
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  state:
    description:
      - Assert the state of the ManagedNetwork.
      - >-
        Use C(present) to create or update an ManagedNetwork and C(absent) to
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
    - name: ManagedNetworksPut
      azure_rm_managednetwork: 
        managed_network_name: myManagedNetwork
        resource_group_name: myResourceGroup
        

    - name: ManagedNetworksDelete
      azure_rm_managednetwork: 
        managed_network_name: myManagedNetwork
        resource_group_name: myResourceGroup
        

    - name: ManagedNetworksPatch
      azure_rm_managednetwork: 
        managed_network_name: myManagedNetwork
        resource_group_name: myResourceGroup
        tags: {}
        

'''

RETURN = '''
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
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
connectivity:
  description:
    - The collection of groups and policies concerned with connectivity
  returned: always
  type: dict
  sample: null
  contains:
    groups:
      description:
        - >-
          The collection of connectivity related Managed Network Groups within
          the Managed Network
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - >-
              Responsibility role under which this Managed Network Group will be
              created
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
        management_groups:
          description:
            - The collection of management groups covered by the Managed Network
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
        subscriptions:
          description:
            - The collection of subscriptions covered by the Managed Network
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
        virtual_networks:
          description:
            - The collection of virtual nets covered by the Managed Network
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
        subnets:
          description:
            - The collection of  subnets covered by the Managed Network
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
    peerings:
      description:
        - >-
          The collection of Managed Network Peering Policies within the Managed
          Network
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
management_groups:
  description:
    - The collection of management groups covered by the Managed Network
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
subscriptions:
  description:
    - The collection of subscriptions covered by the Managed Network
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
virtual_networks:
  description:
    - The collection of virtual nets covered by the Managed Network
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
subnets:
  description:
    - The collection of  subnets covered by the Managed Network
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


class AzureRMManagedNetwork(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            management_groups=dict(
                type='list',
                disposition='/management_groups',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            subscriptions=dict(
                type='list',
                disposition='/subscriptions',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            virtual_networks=dict(
                type='list',
                disposition='/virtual_networks',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            subnets=dict(
                type='list',
                disposition='/subnets',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.managed_network_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedNetwork, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.managed_networks.create_or_update(resource_group_name=self.resource_group_name,
                                                                          managed_network_name=self.managed_network_name,
                                                                          managed_network=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedNetwork instance.')
            self.fail('Error creating the ManagedNetwork instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_networks.delete(resource_group_name=self.resource_group_name,
                                                                managed_network_name=self.managed_network_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagedNetwork instance.')
            self.fail('Error deleting the ManagedNetwork instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_networks.get(resource_group_name=self.resource_group_name,
                                                             managed_network_name=self.managed_network_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedNetwork()


if __name__ == '__main__':
    main()
