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
module: azure_rm_cluster
version_added: '2.9'
short_description: Manage Azure Cluster instance.
description:
  - 'Create, update and delete instance of Azure Cluster.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  private_cloud_name:
    description:
      - Name of the private cloud
      - The name of the private cloud.
    required: true
    type: str
  cluster_name:
    description:
      - Name of the cluster in the private cloud
    required: true
    type: str
  cluster_size:
    description:
      - The cluster size
    type: integer
  name:
    description:
      - The name of the SKU.
    type: str
  state:
    description:
      - Assert the state of the Cluster.
      - >-
        Use C(present) to create or update an Cluster and C(absent) to delete
        it.
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
    - name: Clusters_CreateOrUpdate
      azure_rm_cluster: 
        cluster_name: cluster1
        private_cloud_name: cloud1
        resource_group_name: group1
        properties:
          cluster_size: 3
        sku:
          name: AV20
        

    - name: Clusters_Update
      azure_rm_cluster: 
        cluster_name: cluster1
        private_cloud_name: cloud1
        resource_group_name: group1
        

    - name: Clusters_Delete
      azure_rm_cluster: 
        cluster_name: cluster1
        private_cloud_name: cloud1
        resource_group_name: group1
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
cluster_size:
  description:
    - The cluster size
  returned: always
  type: integer
  sample: null
cluster_id:
  description:
    - The identity
  returned: always
  type: integer
  sample: null
hosts:
  description:
    - The hosts
  returned: always
  type: list
  sample: null
provisioning_state:
  description:
    - The state of the cluster provisioning
  returned: always
  type: str
  sample: null
name_sku_name:
  description:
    - The name of the SKU.
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
    from azure.mgmt.azure import Azure VMware Solution API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCluster(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            private_cloud_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            cluster_size=dict(
                type='integer',
                disposition='/cluster_size'
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
        self.private_cloud_name = None
        self.cluster_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCluster, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure VMware Solution API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-20')

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
            response = self.mgmt_client.clusters.create_or_update(resource_group_name=self.resource_group_name,
                                                                  private_cloud_name=self.private_cloud_name,
                                                                  cluster_name=self.cluster_name,
                                                                  cluster=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Cluster instance.')
            self.fail('Error creating the Cluster instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.clusters.delete(resource_group_name=self.resource_group_name,
                                                        private_cloud_name=self.private_cloud_name,
                                                        cluster_name=self.cluster_name)
        except CloudError as e:
            self.log('Error attempting to delete the Cluster instance.')
            self.fail('Error deleting the Cluster instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.clusters.get(resource_group_name=self.resource_group_name,
                                                     private_cloud_name=self.private_cloud_name,
                                                     cluster_name=self.cluster_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCluster()


if __name__ == '__main__':
    main()
