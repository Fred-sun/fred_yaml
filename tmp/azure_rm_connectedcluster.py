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
module: azure_rm_connectedcluster
version_added: '2.9'
short_description: Manage Azure ConnectedCluster instance.
description:
  - 'Create, update and delete instance of Azure ConnectedCluster.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the Kubernetes cluster on which get is called.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  agent_public_key_certificate:
    description:
      - >-
        Base64 encoded public certificate used by the agent to do the initial
        handshake to the backend services in Azure.
    type: str
  aadprofile:
    description:
      - undefined
    type: dict
    suboptions:
      tenant_id:
        description:
          - The aad tenant id which is configured on target K8s cluster
        required: true
        type: str
      client_app_id:
        description:
          - 'The client app id configured on target K8 cluster '
        required: true
        type: str
      server_app_id:
        description:
          - The server app id to access AD server
        required: true
        type: str
  provisioning_state:
    description:
      - The current deployment state of connectedClusters.
    type: str
    choices:
      - Succeeded
      - Failed
      - Canceled
      - Provisioning
      - Updating
      - Deleting
      - Accepted
  type:
    description:
      - >-
        The type of identity used for the connected cluster. The type
        'SystemAssigned, includes a system created identity. The type 'None'
        means no identity is assigned to the connected cluster.
    type: sealed-choice
  state:
    description:
      - Assert the state of the ConnectedCluster.
      - >-
        Use C(present) to create or update an ConnectedCluster and C(absent) to
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
    - name: CreateClusterExample
      azure_rm_connectedcluster: 
        cluster_name: testCluster
        resource_group_name: k8sc-rg
        

    - name: UpdateClusterExample
      azure_rm_connectedcluster: 
        cluster_name: testCluster
        resource_group_name: k8sc-rg
        

    - name: DeleteClusterExample
      azure_rm_connectedcluster: 
        cluster_name: testCluster
        resource_group_name: k8sc-rg
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
agent_public_key_certificate:
  description:
    - >-
      Base64 encoded public certificate used by the agent to do the initial
      handshake to the backend services in Azure.
  returned: always
  type: str
  sample: null
aadprofile:
  description:
    - ''
  returned: always
  type: dict
  sample: null
  contains:
    tenant_id:
      description:
        - The aad tenant id which is configured on target K8s cluster
      returned: always
      type: str
      sample: null
    client_app_id:
      description:
        - 'The client app id configured on target K8 cluster '
      returned: always
      type: str
      sample: null
    server_app_id:
      description:
        - The server app id to access AD server
      returned: always
      type: str
      sample: null
kubernetes_version:
  description:
    - The Kubernetes version of the connected cluster resource
  returned: always
  type: str
  sample: null
total_node_count:
  description:
    - Number of nodes present in the connected cluster resource
  returned: always
  type: integer
  sample: null
agent_version:
  description:
    - Version of the agent running on the connected cluster resource
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The current deployment state of connectedClusters.
  returned: always
  type: str
  sample: null
principal_id:
  description:
    - >-
      The principal id of connected cluster identity. This property will only be
      provided for a system assigned identity.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - >-
      The tenant id associated with the connected cluster. This property will
      only be provided for a system assigned identity.
  returned: always
  type: str
  sample: null
type_identity_type:
  description:
    - >-
      The type of identity used for the connected cluster. The type
      'SystemAssigned, includes a system created identity. The type 'None' means
      no identity is assigned to the connected cluster.
  returned: always
  type: sealed-choice
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.connected import ConnectedKubernetesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConnectedCluster(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                disposition='/location'
            ),
            agent_public_key_certificate=dict(
                type='str',
                disposition='/agent_public_key_certificate'
            ),
            aadprofile=dict(
                type='dict',
                disposition='/aadprofile',
                options=dict(
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id',
                        required=True
                    ),
                    client_app_id=dict(
                        type='str',
                        disposition='client_app_id',
                        required=True
                    ),
                    server_app_id=dict(
                        type='str',
                        disposition='server_app_id',
                        required=True
                    )
                )
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state',
                choices=['Succeeded',
                         'Failed',
                         'Canceled',
                         'Provisioning',
                         'Updating',
                         'Deleting',
                         'Accepted']
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConnectedCluster, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ConnectedKubernetesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.connected_cluster.create(resource_group_name=self.resource_group_name,
                                                                     cluster_name=self.cluster_name,
                                                                     connected_cluster=self.body)
            else:
                response = self.mgmt_client.connected_cluster.update(resource_group_name=self.resource_group_name,
                                                                     cluster_name=self.cluster_name,
                                                                     connected_cluster_patch=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ConnectedCluster instance.')
            self.fail('Error creating the ConnectedCluster instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.connected_cluster.delete(resource_group_name=self.resource_group_name,
                                                                 cluster_name=self.cluster_name)
        except CloudError as e:
            self.log('Error attempting to delete the ConnectedCluster instance.')
            self.fail('Error deleting the ConnectedCluster instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.connected_cluster.get(resource_group_name=self.resource_group_name,
                                                              cluster_name=self.cluster_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMConnectedCluster()


if __name__ == '__main__':
    main()
