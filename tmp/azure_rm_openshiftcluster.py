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
module: azure_rm_openshiftcluster
version_added: '2.9'
short_description: Manage Azure OpenShiftCluster instance.
description:
  - 'Create, update and delete instance of Azure OpenShiftCluster.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  resource_name:
    description:
      - The name of the OpenShift cluster resource.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  provisioning_state:
    description:
      - The cluster provisioning state (immutable).
    type: str
    choices:
      - AdminUpdating
      - Creating
      - Deleting
      - Failed
      - Succeeded
      - Updating
  cluster_profile:
    description:
      - The cluster profile.
    type: dict
    suboptions:
      pull_secret:
        description:
          - The pull secret for the cluster (immutable).
        type: str
      domain:
        description:
          - The domain for the cluster (immutable).
        type: str
      version:
        description:
          - The version of the cluster (immutable).
        type: str
      resource_group_id:
        description:
          - The ID of the cluster resource group (immutable).
        type: str
  service_principal_profile:
    description:
      - The cluster service principal profile.
    type: dict
    suboptions:
      client_id:
        description:
          - The client ID used for the cluster (immutable).
        type: str
      client_secret:
        description:
          - The client secret used for the cluster (immutable).
        type: str
  network_profile:
    description:
      - The cluster network profile.
    type: dict
    suboptions:
      pod_cidr:
        description:
          - The CIDR used for OpenShift/Kubernetes Pods (immutable).
        type: str
      service_cidr:
        description:
          - The CIDR used for OpenShift/Kubernetes Services (immutable).
        type: str
  master_profile:
    description:
      - The cluster master profile.
    type: dict
    suboptions:
      vm_size:
        description:
          - The size of the master VMs (immutable).
        type: str
        choices:
          - Standard_D2s_v3
          - Standard_D4s_v3
          - Standard_D8s_v3
      subnet_id:
        description:
          - The Azure resource ID of the master subnet (immutable).
        type: str
  worker_profiles:
    description:
      - The cluster worker profiles.
    type: list
    suboptions:
      name:
        description:
          - The worker profile name.  Must be "worker" (immutable).
        type: str
      vm_size:
        description:
          - The size of the worker VMs (immutable).
        type: str
        choices:
          - Standard_D2s_v3
          - Standard_D4s_v3
          - Standard_D8s_v3
      disk_size_gb:
        description:
          - >-
            The disk size of the worker VMs.  Must be 128 or greater
            (immutable).
        type: integer
      subnet_id:
        description:
          - The Azure resource ID of the worker subnet (immutable).
        type: str
      count:
        description:
          - The number of worker VMs.  Must be between 3 and 20 (immutable).
        type: integer
  apiserver_profile:
    description:
      - The cluster API server profile.
    type: dict
    suboptions:
      visibility:
        description:
          - API server visibility (immutable).
        type: str
        choices:
          - Private
          - Public
      url:
        description:
          - The URL to access the cluster API server (immutable).
        type: str
      ip:
        description:
          - The IP of the cluster API server (immutable).
        type: str
  ingress_profiles:
    description:
      - The cluster ingress profiles.
    type: list
    suboptions:
      name:
        description:
          - The ingress profile name.  Must be "default" (immutable).
        type: str
      visibility:
        description:
          - Ingress visibility (immutable).
        type: str
        choices:
          - Private
          - Public
      ip:
        description:
          - The IP of the ingress (immutable).
        type: str
  url:
    description:
      - The URL to access the cluster console (immutable).
    type: str
  state:
    description:
      - Assert the state of the OpenShiftCluster.
      - >-
        Use C(present) to create or update an OpenShiftCluster and C(absent) to
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
    - name: Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name.
      azure_rm_openshiftcluster: 
        resource_group_name: resourceGroup
        resource_name: resourceName
        location: location
        properties:
          apiserver_profile:
            visibility: Public
          cluster_profile:
            domain: cluster.location.aroapp.io
            pull_secret: >-
              {"auths":{"registry.connect.redhat.com":{"auth":""},"registry.redhat.io":{"auth":""}}}
            resource_group_id: /subscriptions/subscriptionId/resourceGroups/clusterResourceGroup
          console_profile: {}
          ingress_profiles:
            - name: default
              visibility: Public
          master_profile:
            subnet_id: >-
              /subscriptions/subscriptionId/resourceGroups/vnetResourceGroup/providers/Microsoft.Network/virtualNetworks/vnet/subnets/master
            vm_size: Standard_D8s_v3
          network_profile:
            pod_cidr: 10.128.0.0/14
            service_cidr: 172.30.0.0/16
          service_principal_profile:
            client_id: clientId
            client_secret: clientSecret
          worker_profiles:
            - name: worker
              count: 3
              disk_size_gb: 128
              subnet_id: >-
                /subscriptions/subscriptionId/resourceGroups/vnetResourceGroup/providers/Microsoft.Network/virtualNetworks/vnet/subnets/worker
              vm_size: Standard_D2s_v3
        tags:
          key: value
        

    - name: Deletes a OpenShift cluster with the specified subscription, resource group and resource name.
      azure_rm_openshiftcluster: 
        resource_group_name: resourceGroup
        resource_name: resourceName
        

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
        - The disk size of the worker VMs.  Must be 128 or greater (immutable).
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Red Hat OpenShift 4 Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOpenShiftCluster(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state',
                choices=['AdminUpdating',
                         'Creating',
                         'Deleting',
                         'Failed',
                         'Succeeded',
                         'Updating']
            ),
            cluster_profile=dict(
                type='dict',
                disposition='/cluster_profile',
                options=dict(
                    pull_secret=dict(
                        type='str',
                        disposition='pull_secret'
                    ),
                    domain=dict(
                        type='str',
                        disposition='domain'
                    ),
                    version=dict(
                        type='str',
                        disposition='version'
                    ),
                    resource_group_id=dict(
                        type='str',
                        disposition='resource_group_id'
                    )
                )
            ),
            service_principal_profile=dict(
                type='dict',
                disposition='/service_principal_profile',
                options=dict(
                    client_id=dict(
                        type='str',
                        disposition='client_id'
                    ),
                    client_secret=dict(
                        type='str',
                        disposition='client_secret'
                    )
                )
            ),
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    pod_cidr=dict(
                        type='str',
                        disposition='pod_cidr'
                    ),
                    service_cidr=dict(
                        type='str',
                        disposition='service_cidr'
                    )
                )
            ),
            master_profile=dict(
                type='dict',
                disposition='/master_profile',
                options=dict(
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
                        choices=['Standard_D2s_v3',
                                 'Standard_D4s_v3',
                                 'Standard_D8s_v3']
                    ),
                    subnet_id=dict(
                        type='str',
                        disposition='subnet_id'
                    )
                )
            ),
            worker_profiles=dict(
                type='list',
                disposition='/worker_profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
                        choices=['Standard_D2s_v3',
                                 'Standard_D4s_v3',
                                 'Standard_D8s_v3']
                    ),
                    disk_size_gb=dict(
                        type='integer',
                        disposition='disk_size_gb'
                    ),
                    subnet_id=dict(
                        type='str',
                        disposition='subnet_id'
                    ),
                    count=dict(
                        type='integer',
                        disposition='count'
                    )
                )
            ),
            apiserver_profile=dict(
                type='dict',
                disposition='/apiserver_profile',
                options=dict(
                    visibility=dict(
                        type='str',
                        disposition='visibility',
                        choices=['Private',
                                 'Public']
                    ),
                    url=dict(
                        type='str',
                        disposition='url'
                    ),
                    ip=dict(
                        type='str',
                        disposition='ip'
                    )
                )
            ),
            ingress_profiles=dict(
                type='list',
                disposition='/ingress_profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    visibility=dict(
                        type='str',
                        disposition='visibility',
                        choices=['Private',
                                 'Public']
                    ),
                    ip=dict(
                        type='str',
                        disposition='ip'
                    )
                )
            ),
            url=dict(
                type='str',
                disposition='/url'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOpenShiftCluster, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Red Hat OpenShift 4 Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-30')

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
            response = self.mgmt_client.open_shift_clusters.create_or_update(resource_group_name=self.resource_group_name,
                                                                             resource_name=self.resource_name,
                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the OpenShiftCluster instance.')
            self.fail('Error creating the OpenShiftCluster instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.open_shift_clusters.delete(resource_group_name=self.resource_group_name,
                                                                   resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the OpenShiftCluster instance.')
            self.fail('Error deleting the OpenShiftCluster instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.open_shift_clusters.get(resource_group_name=self.resource_group_name,
                                                                resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOpenShiftCluster()


if __name__ == '__main__':
    main()
