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
module: azure_rm_dedicatedcloudnode_info
version_added: '2.9'
short_description: Get DedicatedCloudNode info.
description:
  - Get info of DedicatedCloudNode.
options:
  filter:
    description:
      - The filter to apply on the list operation
    type: str
  top:
    description:
      - The maximum number of record sets to return
    type: integer
  skip_token:
    description:
      - to be used by nextLink implementation
    type: str
  resource_group_name:
    description:
      - The name of the resource group
    type: str
  dedicated_cloud_node_name:
    description:
      - dedicated cloud node name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListDedicatedCloudNodes
      azure_rm_dedicatedcloudnode_info: 
        {}
        

    - name: ListRGDedicatedCloudNodes
      azure_rm_dedicatedcloudnode_info: 
        resource_group_name: myResourceGroup
        

    - name: GetDedicatedCloudNode
      azure_rm_dedicatedcloudnode_info: 
        dedicated_cloud_node_name: myNode
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
dedicated_cloud_nodes:
  description: >-
    A list of dict results where the key is the name of the DedicatedCloudNode
    and the values are the facts for that DedicatedCloudNode.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of DedicatedCloudNode
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the DedicatedCloudNode list
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName}
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure region
          returned: always
          type: str
          sample: null
        name:
          description:
            - '{dedicatedCloudNodeName}'
          returned: always
          type: str
          sample: null
        sku:
          description:
            - Dedicated Cloud Nodes SKU
          returned: always
          type: dict
          sample: null
          contains:
            capacity:
              description:
                - The capacity of the SKU
              returned: always
              type: str
              sample: null
            description:
              description:
                - >-
                  dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon®
                  Processor E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB
                  PC4-19200 2400MHz DDR4 ECC Registered DIMM, ...
              returned: always
              type: str
              sample: null
            family:
              description:
                - >-
                  If the service has different generations of hardware, for the
                  same SKU, then that can be captured here
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the SKU for VMWare CloudSimple Node
              returned: always
              type: str
              sample: null
            tier:
              description:
                - The tier of the SKU
              returned: always
              type: str
              sample: null
        tags:
          description:
            - Dedicated Cloud Nodes tags
          returned: always
          type: dictionary
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
          returned: always
          type: str
          sample: null
        availability_zone_id:
          description:
            - 'Availability Zone id, e.g. "az1"'
          returned: always
          type: str
          sample: null
        availability_zone_name:
          description:
            - 'Availability Zone name, e.g. "Availability Zone 1"'
          returned: always
          type: str
          sample: null
        cloud_rack_name:
          description:
            - VMWare Cloud Rack Name
          returned: always
          type: str
          sample: null
        created:
          description:
            - date time the resource was created
          returned: always
          type: any
          sample: null
        nodes_count:
          description:
            - count of nodes to create
          returned: always
          type: integer
          sample: null
        placement_group_id:
          description:
            - 'Placement Group id, e.g. "n1"'
          returned: always
          type: str
          sample: null
        placement_group_name:
          description:
            - 'Placement Name, e.g. "Placement Group 1"'
          returned: always
          type: str
          sample: null
        private_cloud_id:
          description:
            - Private Cloud Id
          returned: always
          type: str
          sample: null
        private_cloud_name:
          description:
            - Resource Pool Name
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning status of the resource
          returned: always
          type: str
          sample: null
        purchase_id:
          description:
            - purchase id
          returned: always
          type: uuid
          sample: null
        status:
          description:
            - 'Node status, indicates is private cloud set up on this node or not'
          returned: always
          type: sealed-choice
          sample: null
        vmware_cluster_name:
          description:
            - VMWare Cluster Name
          returned: always
          type: str
          sample: null
        id_properties_sku_description_id:
          description:
            - SKU's id
          returned: always
          type: str
          sample: null
        name_properties_sku_description_name:
          description:
            - SKU's name
          returned: always
          type: str
          sample: null
    id:
      description:
        - >-
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName}
      returned: always
      type: str
      sample: null
    location:
      description:
        - Azure region
      returned: always
      type: str
      sample: null
    name:
      description:
        - '{dedicatedCloudNodeName}'
      returned: always
      type: str
      sample: null
    sku:
      description:
        - Dedicated Cloud Nodes SKU
      returned: always
      type: dict
      sample: null
      contains:
        capacity:
          description:
            - The capacity of the SKU
          returned: always
          type: str
          sample: null
        description:
          description:
            - >-
              dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon® Processor
              E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz
              DDR4 ECC Registered DIMM, ...
          returned: always
          type: str
          sample: null
        family:
          description:
            - >-
              If the service has different generations of hardware, for the same
              SKU, then that can be captured here
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the SKU for VMWare CloudSimple Node
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The tier of the SKU
          returned: always
          type: str
          sample: null
    tags:
      description:
        - Dedicated Cloud Nodes tags
      returned: always
      type: dictionary
      sample: null
    type:
      description:
        - '{resourceProviderNamespace}/{resourceType}'
      returned: always
      type: str
      sample: null
    availability_zone_id:
      description:
        - 'Availability Zone id, e.g. "az1"'
      returned: always
      type: str
      sample: null
    availability_zone_name:
      description:
        - 'Availability Zone name, e.g. "Availability Zone 1"'
      returned: always
      type: str
      sample: null
    cloud_rack_name:
      description:
        - VMWare Cloud Rack Name
      returned: always
      type: str
      sample: null
    created:
      description:
        - date time the resource was created
      returned: always
      type: any
      sample: null
    nodes_count:
      description:
        - count of nodes to create
      returned: always
      type: integer
      sample: null
    placement_group_id:
      description:
        - 'Placement Group id, e.g. "n1"'
      returned: always
      type: str
      sample: null
    placement_group_name:
      description:
        - 'Placement Name, e.g. "Placement Group 1"'
      returned: always
      type: str
      sample: null
    private_cloud_id:
      description:
        - Private Cloud Id
      returned: always
      type: str
      sample: null
    private_cloud_name:
      description:
        - Resource Pool Name
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning status of the resource
      returned: always
      type: str
      sample: null
    purchase_id:
      description:
        - purchase id
      returned: always
      type: uuid
      sample: null
    status:
      description:
        - 'Node status, indicates is private cloud set up on this node or not'
      returned: always
      type: sealed-choice
      sample: null
    vmware_cluster_name:
      description:
        - VMWare Cluster Name
      returned: always
      type: str
      sample: null
    id_properties_sku_description_id:
      description:
        - SKU's id
      returned: always
      type: str
      sample: null
    name_properties_sku_description_name:
      description:
        - SKU's name
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
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDedicatedCloudNodeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip_token=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            dedicated_cloud_node_name=dict(
                type='str'
            )
        )

        self.filter = None
        self.top = None
        self.skip_token = None
        self.resource_group_name = None
        self.dedicated_cloud_node_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDedicatedCloudNodeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.resource_group_name is not None and
            self.dedicated_cloud_node_name is not None):
            self.results['dedicated_cloud_nodes'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['dedicated_cloud_nodes'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['dedicated_cloud_nodes'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_nodes.get(resource_group_name=self.resource_group_name,
                                                                  dedicated_cloud_node_name=self.dedicated_cloud_node_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_nodes.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                     filter=self.filter,
                                                                                     top=self.top,
                                                                                     skip_token=self.skip_token)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_nodes.list_by_subscription(filter=self.filter,
                                                                                   top=self.top,
                                                                                   skip_token=self.skip_token)
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
    AzureRMDedicatedCloudNodeInfo()


if __name__ == '__main__':
    main()
