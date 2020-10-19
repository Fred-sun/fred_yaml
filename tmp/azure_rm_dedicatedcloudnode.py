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
module: azure_rm_dedicatedcloudnode
version_added: '2.9'
short_description: Manage Azure DedicatedCloudNode instance.
description:
  - 'Create, update and delete instance of Azure DedicatedCloudNode.'
options:
  resource_group_name:
    description:
      - The name of the resource group
    required: true
    type: str
  dedicated_cloud_node_name:
    description:
      - dedicated cloud node name
    required: true
    type: str
  referer:
    description:
      - referer url
    type: str
  location:
    description:
      - Azure region
    type: str
  sku:
    description:
      - Dedicated Cloud Nodes SKU
    type: dict
    suboptions:
      capacity:
        description:
          - The capacity of the SKU
        type: str
      description:
        description:
          - >-
            dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon® Processor
            E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz
            DDR4 ECC Registered DIMM, ...
        type: str
      family:
        description:
          - >-
            If the service has different generations of hardware, for the same
            SKU, then that can be captured here
        type: str
      name:
        description:
          - The name of the SKU for VMWare CloudSimple Node
        required: true
        type: str
      tier:
        description:
          - The tier of the SKU
        type: str
  availability_zone_id:
    description:
      - 'Availability Zone id, e.g. "az1"'
    type: str
  nodes_count:
    description:
      - count of nodes to create
    type: integer
  placement_group_id:
    description:
      - 'Placement Group id, e.g. "n1"'
    type: str
  purchase_id:
    description:
      - purchase id
    type: uuid
  id:
    description:
      - SKU's id
    type: str
  name:
    description:
      - SKU's name
    type: str
  state:
    description:
      - Assert the state of the DedicatedCloudNode.
      - >-
        Use C(present) to create or update an DedicatedCloudNode and C(absent)
        to delete it.
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
    - name: CreateDedicatedCloudNode
      azure_rm_dedicatedcloudnode: 
        dedicated_cloud_node_name: myNode
        resource_group_name: myResourceGroup
        

    - name: DeleteDedicatedCloudNode
      azure_rm_dedicatedcloudnode: 
        dedicated_cloud_node_name: myNode
        resource_group_name: myResourceGroup
        

    - name: PatchDedicatedCloudNode
      azure_rm_dedicatedcloudnode: 
        dedicated_cloud_node_name: myNode
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
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
          E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz DDR4
          ECC Registered DIMM, ...
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedCloudNode(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            dedicated_cloud_node_name=dict(
                type='str',
                required=True
            ),
            referer=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    capacity=dict(
                        type='str',
                        disposition='capacity'
                    ),
                    description=dict(
                        type='str',
                        disposition='description'
                    ),
                    family=dict(
                        type='str',
                        disposition='family'
                    ),
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    )
                )
            ),
            availability_zone_id=dict(
                type='str',
                disposition='/availability_zone_id'
            ),
            nodes_count=dict(
                type='integer',
                disposition='/nodes_count'
            ),
            placement_group_id=dict(
                type='str',
                disposition='/placement_group_id'
            ),
            purchase_id=dict(
                type='uuid',
                disposition='/purchase_id'
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.dedicated_cloud_node_name = None
        self.referer = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedCloudNode, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

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
            response = self.mgmt_client.dedicated_cloud_nodes.create_or_update(resource_group_name=self.resource_group_name,
                                                                               referer=self.referer,
                                                                               dedicated_cloud_node_name=self.dedicated_cloud_node_name,
                                                                               dedicated_cloud_node_request=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedCloudNode instance.')
            self.fail('Error creating the DedicatedCloudNode instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_cloud_nodes.delete(resource_group_name=self.resource_group_name,
                                                                     dedicated_cloud_node_name=self.dedicated_cloud_node_name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedCloudNode instance.')
            self.fail('Error deleting the DedicatedCloudNode instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dedicated_cloud_nodes.get(resource_group_name=self.resource_group_name,
                                                                  dedicated_cloud_node_name=self.dedicated_cloud_node_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedCloudNode()


if __name__ == '__main__':
    main()
