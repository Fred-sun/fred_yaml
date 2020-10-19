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
module: azure_rm_openshiftcluster_info
version_added: '2.9'
short_description: Get OpenShiftCluster info.
description:
  - Get info of OpenShiftCluster.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  resource_name:
    description:
      - The name of the OpenShift cluster resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists OpenShift clusters in the specified subscription.
      azure_rm_openshiftcluster_info: 
        {}
        

    - name: Lists OpenShift clusters in the specified subscription and resource group.
      azure_rm_openshiftcluster_info: 
        resource_group_name: resourceGroup
        

    - name: Gets a OpenShift cluster with the specified subscription, resource group and resource name.
      azure_rm_openshiftcluster_info: 
        resource_group_name: resourceGroup
        resource_name: resourceName
        

'''

RETURN = '''
open_shift_clusters:
  description: >-
    A list of dict results where the key is the name of the OpenShiftCluster and
    the values are the facts for that OpenShiftCluster.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of OpenShift clusters.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - The cluster provisioning state (immutable).
          returned: always
          type: str
          sample: null
        cluster_profile:
          description:
            - The cluster profile.
          returned: always
          type: dict
          sample: null
          contains:
            pull_secret:
              description:
                - The pull secret for the cluster (immutable).
              returned: always
              type: str
              sample: null
            domain:
              description:
                - The domain for the cluster (immutable).
              returned: always
              type: str
              sample: null
            version:
              description:
                - The version of the cluster (immutable).
              returned: always
              type: str
              sample: null
            resource_group_id:
              description:
                - The ID of the cluster resource group (immutable).
              returned: always
              type: str
              sample: null
        service_principal_profile:
          description:
            - The cluster service principal profile.
          returned: always
          type: dict
          sample: null
          contains:
            client_id:
              description:
                - The client ID used for the cluster (immutable).
              returned: always
              type: str
              sample: null
            client_secret:
              description:
                - The client secret used for the cluster (immutable).
              returned: always
              type: str
              sample: null
        network_profile:
          description:
            - The cluster network profile.
          returned: always
          type: dict
          sample: null
          contains:
            pod_cidr:
              description:
                - The CIDR used for OpenShift/Kubernetes Pods (immutable).
              returned: always
              type: str
              sample: null
            service_cidr:
              description:
                - The CIDR used for OpenShift/Kubernetes Services (immutable).
              returned: always
              type: str
              sample: null
        master_profile:
          description:
            - The cluster master profile.
          returned: always
          type: dict
          sample: null
          contains:
            vm_size:
              description:
                - The size of the master VMs (immutable).
              returned: always
              type: str
              sample: null
            subnet_id:
              description:
                - The Azure resource ID of the master subnet (immutable).
              returned: always
              type: str
              sample: null
        worker_profiles:
          description:
            - The cluster worker profiles.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The worker profile name.  Must be "worker" (immutable).
              returned: always
              type: str
              sample: null
            vm_size:
              description:
                - The size of the worker VMs (immutable).
              returned: always
              type: str
              sample: null
            disk_size_gb:
              description:
                - >-
                  The disk size of the worker VMs.  Must be 128 or greater
                  (immutable).
              returned: always
              type: integer
              sample: null
            subnet_id:
              description:
                - The Azure resource ID of the worker subnet (immutable).
              returned: always
              type: str
              sample: null
            count:
              description:
                - >-
                  The number of worker VMs.  Must be between 3 and 20
                  (immutable).
              returned: always
              type: integer
              sample: null
        apiserver_profile:
          description:
            - The cluster API server profile.
          returned: always
          type: dict
          sample: null
          contains:
            visibility:
              description:
                - API server visibility (immutable).
              returned: always
              type: str
              sample: null
            url:
              description:
                - The URL to access the cluster API server (immutable).
              returned: always
              type: str
              sample: null
            ip:
              description:
                - The IP of the cluster API server (immutable).
              returned: always
              type: str
              sample: null
        ingress_profiles:
          description:
            - The cluster ingress profiles.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The ingress profile name.  Must be "default" (immutable).
              returned: always
              type: str
              sample: null
            visibility:
              description:
                - Ingress visibility (immutable).
              returned: always
              type: str
              sample: null
            ip:
              description:
                - The IP of the ingress (immutable).
              returned: always
              type: str
              sample: null
        url:
          description:
            - The URL to access the cluster console (immutable).
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link used to get the next page of operations.
      returned: always
      type: str
      sample: null
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
    provisioning_state:
      description:
        - The cluster provisioning state (immutable).
      returned: always
      type: str
      sample: null
    cluster_profile:
      description:
        - The cluster profile.
      returned: always
      type: dict
      sample: null
      contains:
        pull_secret:
          description:
            - The pull secret for the cluster (immutable).
          returned: always
          type: str
          sample: null
        domain:
          description:
            - The domain for the cluster (immutable).
          returned: always
          type: str
          sample: null
        version:
          description:
            - The version of the cluster (immutable).
          returned: always
          type: str
          sample: null
        resource_group_id:
          description:
            - The ID of the cluster resource group (immutable).
          returned: always
          type: str
          sample: null
    service_principal_profile:
      description:
        - The cluster service principal profile.
      returned: always
      type: dict
      sample: null
      contains:
        client_id:
          description:
            - The client ID used for the cluster (immutable).
          returned: always
          type: str
          sample: null
        client_secret:
          description:
            - The client secret used for the cluster (immutable).
          returned: always
          type: str
          sample: null
    network_profile:
      description:
        - The cluster network profile.
      returned: always
      type: dict
      sample: null
      contains:
        pod_cidr:
          description:
            - The CIDR used for OpenShift/Kubernetes Pods (immutable).
          returned: always
          type: str
          sample: null
        service_cidr:
          description:
            - The CIDR used for OpenShift/Kubernetes Services (immutable).
          returned: always
          type: str
          sample: null
    master_profile:
      description:
        - The cluster master profile.
      returned: always
      type: dict
      sample: null
      contains:
        vm_size:
          description:
            - The size of the master VMs (immutable).
          returned: always
          type: str
          sample: null
        subnet_id:
          description:
            - The Azure resource ID of the master subnet (immutable).
          returned: always
          type: str
          sample: null
    worker_profiles:
      description:
        - The cluster worker profiles.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The worker profile name.  Must be "worker" (immutable).
          returned: always
          type: str
          sample: null
        vm_size:
          description:
            - The size of the worker VMs (immutable).
          returned: always
          type: str
          sample: null
        disk_size_gb:
          description:
            - >-
              The disk size of the worker VMs.  Must be 128 or greater
              (immutable).
          returned: always
          type: integer
          sample: null
        subnet_id:
          description:
            - The Azure resource ID of the worker subnet (immutable).
          returned: always
          type: str
          sample: null
        count:
          description:
            - The number of worker VMs.  Must be between 3 and 20 (immutable).
          returned: always
          type: integer
          sample: null
    apiserver_profile:
      description:
        - The cluster API server profile.
      returned: always
      type: dict
      sample: null
      contains:
        visibility:
          description:
            - API server visibility (immutable).
          returned: always
          type: str
          sample: null
        url:
          description:
            - The URL to access the cluster API server (immutable).
          returned: always
          type: str
          sample: null
        ip:
          description:
            - The IP of the cluster API server (immutable).
          returned: always
          type: str
          sample: null
    ingress_profiles:
      description:
        - The cluster ingress profiles.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The ingress profile name.  Must be "default" (immutable).
          returned: always
          type: str
          sample: null
        visibility:
          description:
            - Ingress visibility (immutable).
          returned: always
          type: str
          sample: null
        ip:
          description:
            - The IP of the ingress (immutable).
          returned: always
          type: str
          sample: null
    url:
      description:
        - The URL to access the cluster console (immutable).
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
    from azure.mgmt.azure import Azure Red Hat OpenShift 4 Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOpenShiftClusterInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOpenShiftClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Red Hat OpenShift 4 Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-30')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['open_shift_clusters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['open_shift_clusters'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['open_shift_clusters'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.open_shift_clusters.get(resource_group_name=self.resource_group_name,
                                                                resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.open_shift_clusters.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.open_shift_clusters.list()
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
    AzureRMOpenShiftClusterInfo()


if __name__ == '__main__':
    main()
