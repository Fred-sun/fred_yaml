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
module: azure_rm_managednetwork_info
version_added: '2.9'
short_description: Get ManagedNetwork info.
description:
  - Get info of ManagedNetwork.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  managed_network_name:
    description:
      - The name of the Managed Network.
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
    - name: ManagedNetworksGet
      azure_rm_managednetwork_info: 
        managed_network_name: myManagedNetwork
        resource_group_name: myResourceGroup
        

    - name: ManagedNetworksListByResourceGroup
      azure_rm_managednetwork_info: 
        resource_group_name: myResourceGroup
        

    - name: ManagedNetworksListBySubscription
      azure_rm_managednetwork_info: 
        {}
        

'''

RETURN = '''
managed_networks:
  description: >-
    A list of dict results where the key is the name of the ManagedNetwork and
    the values are the facts for that ManagedNetwork.
  returned: always
  type: complex
  contains:
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
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
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
              The collection of connectivity related Managed Network Groups
              within the Managed Network
          returned: always
          type: list
          sample: null
          contains:
            kind:
              description:
                - >-
                  Responsibility role under which this Managed Network Group
                  will be created
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
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            management_groups:
              description:
                - >-
                  The collection of management groups covered by the Managed
                  Network
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
              The collection of Managed Network Peering Policies within the
              Managed Network
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
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type_properties_type:
              description:
                - >-
                  Gets or sets the connectivity type of a network structure
                  policy
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
    value:
      description:
        - Gets a page of ManagedNetworks
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
                  The collection of connectivity related Managed Network Groups
                  within the Managed Network
              returned: always
              type: list
              sample: null
              contains:
                kind:
                  description:
                    - >-
                      Responsibility role under which this Managed Network Group
                      will be created
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
                      A unique read-only string that changes whenever the
                      resource is updated.
                  returned: always
                  type: str
                  sample: null
                management_groups:
                  description:
                    - >-
                      The collection of management groups covered by the Managed
                      Network
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
                    - >-
                      The collection of subscriptions covered by the Managed
                      Network
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
                    - >-
                      The collection of virtual nets covered by the Managed
                      Network
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
                  The collection of Managed Network Peering Policies within the
                  Managed Network
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
                      A unique read-only string that changes whenever the
                      resource is updated.
                  returned: always
                  type: str
                  sample: null
                type_properties_type:
                  description:
                    - >-
                      Gets or sets the connectivity type of a network structure
                      policy
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


class AzureRMManagedNetworkInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            managed_network_name=dict(
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
        super(AzureRMManagedNetworkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedNetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.managed_network_name is not None):
            self.results['managed_networks'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['managed_networks'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['managed_networks'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_networks.get(resource_group_name=self.resource_group_name,
                                                             managed_network_name=self.managed_network_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.managed_networks.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                top=self.top,
                                                                                skiptoken=self.skiptoken)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.managed_networks.list_by_subscription(top=self.top,
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
    AzureRMManagedNetworkInfo()


if __name__ == '__main__':
    main()
