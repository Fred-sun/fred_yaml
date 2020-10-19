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
module: azure_rm_connectedcluster_info
version_added: '2.9'
short_description: Get ConnectedCluster info.
description:
  - Get info of ConnectedCluster.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  cluster_name:
    description:
      - The name of the Kubernetes cluster on which get is called.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetClusterExample
      azure_rm_connectedcluster_info: 
        cluster_name: testCluster
        resource_group_name: k8sc-rg
        

    - name: GetClustersExample
      azure_rm_connectedcluster_info: 
        resource_group_name: k8sc-rg
        

'''

RETURN = '''
connected_cluster:
  description: >-
    A list of dict results where the key is the name of the ConnectedCluster and
    the values are the facts for that ConnectedCluster.
  returned: always
  type: complex
  contains:
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
          The principal id of connected cluster identity. This property will
          only be provided for a system assigned identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - >-
          The tenant id associated with the connected cluster. This property
          will only be provided for a system assigned identity.
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - >-
          The type of identity used for the connected cluster. The type
          'SystemAssigned, includes a system created identity. The type 'None'
          means no identity is assigned to the connected cluster.
      returned: always
      type: sealed-choice
      sample: null
    value:
      description:
        - The list of connected clusters
      returned: always
      type: list
      sample: null
      contains:
        agent_public_key_certificate:
          description:
            - >-
              Base64 encoded public certificate used by the agent to do the
              initial handshake to the backend services in Azure.
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
              The principal id of connected cluster identity. This property will
              only be provided for a system assigned identity.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              The tenant id associated with the connected cluster. This property
              will only be provided for a system assigned identity.
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - >-
              The type of identity used for the connected cluster. The type
              'SystemAssigned, includes a system created identity. The type
              'None' means no identity is assigned to the connected cluster.
          returned: always
          type: sealed-choice
          sample: null
    next_link:
      description:
        - The link to fetch the next page of connected cluster
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
    from azure.mgmt.connected import ConnectedKubernetesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConnectedClusterInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            cluster_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMConnectedClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ConnectedKubernetesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01-preview')

        if (self.resource_group_name is not None and
            self.cluster_name is not None):
            self.results['connected_cluster'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['connected_cluster'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['connected_cluster'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.connected_cluster.get(resource_group_name=self.resource_group_name,
                                                              cluster_name=self.cluster_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.connected_cluster.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.connected_cluster.list_by_subscription()
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
    AzureRMConnectedClusterInfo()


if __name__ == '__main__':
    main()
