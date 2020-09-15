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
module: azure_rm_openshiftmanagedcluster
version_added: '2.9'
short_description: Manage Azure OpenShiftManagedCluster instance.
description:
  - 'Create, update and delete instance of Azure OpenShiftManagedCluster.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  resource_name:
    description:
      - The name of the OpenShift managed cluster resource.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  plan:
    description:
      - Define the resource plan as required by ARM for billing purposes
    type: dict
    suboptions:
      name:
        description:
          - The plan ID.
        type: str
      product:
        description:
          - >-
            Specifies the product of the image from the marketplace. This is the
            same value as Offer under the imageReference element.
        type: str
      promotion_code:
        description:
          - The promotion code.
        type: str
      publisher:
        description:
          - The plan ID.
        type: str
  open_shift_version:
    description:
      - Version of OpenShift specified when creating the cluster.
    type: str
  network_profile:
    description:
      - Configuration for OpenShift networking.
    type: dict
    suboptions:
      vnet_cidr:
        description:
          - CIDR for the OpenShift Vnet.
        type: str
      peer_vnet_id:
        description:
          - CIDR of the Vnet to peer.
        type: str
      vnet_id:
        description:
          - ID of the Vnet created for OSA cluster.
        type: str
  router_profiles:
    description:
      - Configuration for OpenShift router(s).
    type: list
    suboptions:
      name:
        description:
          - Name of the router profile.
        type: str
      public_subdomain:
        description:
          - DNS subdomain for OpenShift router.
        type: str
      fqdn:
        description:
          - Auto-allocated FQDN for the OpenShift router.
        type: str
  master_pool_profile:
    description:
      - Configuration for OpenShift master VMs.
    type: dict
    suboptions:
      name:
        description:
          - >-
            Unique name of the master pool profile in the context of the
            subscription and resource group.
        type: str
      count:
        description:
          - >-
            Number of masters (VMs) to host docker containers. The default value
            is 3.
        required: true
        type: integer
      vm_size:
        description:
          - Size of agent VMs.
        required: true
        type: str
        choices:
          - Standard_D2s_v3
          - Standard_D4s_v3
          - Standard_D8s_v3
          - Standard_D16s_v3
          - Standard_D32s_v3
          - Standard_D64s_v3
          - Standard_DS4_v2
          - Standard_DS5_v2
          - Standard_F8s_v2
          - Standard_F16s_v2
          - Standard_F32s_v2
          - Standard_F64s_v2
          - Standard_F72s_v2
          - Standard_F8s
          - Standard_F16s
          - Standard_E4s_v3
          - Standard_E8s_v3
          - Standard_E16s_v3
          - Standard_E20s_v3
          - Standard_E32s_v3
          - Standard_E64s_v3
          - Standard_GS2
          - Standard_GS3
          - Standard_GS4
          - Standard_GS5
          - Standard_DS12_v2
          - Standard_DS13_v2
          - Standard_DS14_v2
          - Standard_DS15_v2
          - Standard_L4s
          - Standard_L8s
          - Standard_L16s
          - Standard_L32s
      subnet_cidr:
        description:
          - Subnet CIDR for the peering.
        type: str
      os_type:
        description:
          - >-
            OsType to be used to specify os type. Choose from Linux and Windows.
            Default to Linux.
        type: str
        choices:
          - Linux
          - Windows
  agent_pool_profiles:
    description:
      - Configuration of OpenShift cluster VMs.
    type: list
    suboptions:
      name:
        description:
          - >-
            Unique name of the pool profile in the context of the subscription
            and resource group.
        required: true
        type: str
      count:
        description:
          - Number of agents (VMs) to host docker containers.
        required: true
        type: integer
      vm_size:
        description:
          - Size of agent VMs.
        required: true
        type: str
        choices:
          - Standard_D2s_v3
          - Standard_D4s_v3
          - Standard_D8s_v3
          - Standard_D16s_v3
          - Standard_D32s_v3
          - Standard_D64s_v3
          - Standard_DS4_v2
          - Standard_DS5_v2
          - Standard_F8s_v2
          - Standard_F16s_v2
          - Standard_F32s_v2
          - Standard_F64s_v2
          - Standard_F72s_v2
          - Standard_F8s
          - Standard_F16s
          - Standard_E4s_v3
          - Standard_E8s_v3
          - Standard_E16s_v3
          - Standard_E20s_v3
          - Standard_E32s_v3
          - Standard_E64s_v3
          - Standard_GS2
          - Standard_GS3
          - Standard_GS4
          - Standard_GS5
          - Standard_DS12_v2
          - Standard_DS13_v2
          - Standard_DS14_v2
          - Standard_DS15_v2
          - Standard_L4s
          - Standard_L8s
          - Standard_L16s
          - Standard_L32s
      subnet_cidr:
        description:
          - Subnet CIDR for the peering.
        type: str
      os_type:
        description:
          - >-
            OsType to be used to specify os type. Choose from Linux and Windows.
            Default to Linux.
        type: str
        choices:
          - Linux
          - Windows
      role:
        description:
          - Define the role of the AgentPoolProfile.
        type: str
        choices:
          - compute
          - infra
  identity_providers:
    description:
      - Type of authentication profile to use.
    type: list
    suboptions:
      name:
        description:
          - Name of the provider.
        type: str
      provider:
        description:
          - Configuration of the provider.
        type: dict
        suboptions:
          kind:
            description:
              - The kind of the provider.
            required: true
            type: str
  state:
    description:
      - Assert the state of the OpenShiftManagedCluster.
      - >-
        Use C(present) to create or update an OpenShiftManagedCluster and
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
    - name: Create/Update OpenShift Managed Cluster
      azure_rm_openshiftmanagedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        location: location1
        properties:
          agent_pool_profiles:
            - name: infra
              count: 2
              os_type: Linux
              role: infra
              subnet_cidr: 10.0.0.0/24
              vm_size: Standard_D4s_v3
            - name: compute
              count: 4
              os_type: Linux
              role: compute
              subnet_cidr: 10.0.0.0/24
              vm_size: Standard_D4s_v3
          auth_profile:
            identity_providers:
              - name: Azure AD
                provider:
                  client_id: clientId
                  customer_admin_group_id: customerAdminGroupId
                  kind: AADIdentityProvider
                  secret: secret
                  tenant_id: tenantId
          master_pool_profile:
            name: master
            count: 3
            os_type: Linux
            subnet_cidr: 10.0.0.0/24
            vm_size: Standard_D4s_v3
          network_profile:
            vnet_cidr: 10.0.0.0/8
          open_shift_version: v3.11
          router_profiles:
            - name: default
        tags:
          archv2: ''
          tier: production
        

    - name: Delete OpenShift Managed Cluster
      azure_rm_openshiftmanagedcluster: 
        resource_group_name: rg1
        resource_name: clustername1
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
plan:
  description:
    - Define the resource plan as required by ARM for billing purposes
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - The plan ID.
      returned: always
      type: str
      sample: null
    product:
      description:
        - >-
          Specifies the product of the image from the marketplace. This is the
          same value as Offer under the imageReference element.
      returned: always
      type: str
      sample: null
    promotion_code:
      description:
        - The promotion code.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - The plan ID.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - >-
      The current deployment or provisioning state, which only appears in the
      response.
  returned: always
  type: str
  sample: null
open_shift_version:
  description:
    - Version of OpenShift specified when creating the cluster.
  returned: always
  type: str
  sample: null
cluster_version:
  description:
    - Version of OpenShift specified when creating the cluster.
  returned: always
  type: str
  sample: null
public_hostname:
  description:
    - Service generated FQDN for OpenShift API server.
  returned: always
  type: str
  sample: null
fqdn:
  description:
    - >-
      Service generated FQDN for OpenShift API server loadbalancer internal
      hostname.
  returned: always
  type: str
  sample: null
network_profile:
  description:
    - Configuration for OpenShift networking.
  returned: always
  type: dict
  sample: null
  contains:
    vnet_cidr:
      description:
        - CIDR for the OpenShift Vnet.
      returned: always
      type: str
      sample: null
    peer_vnet_id:
      description:
        - CIDR of the Vnet to peer.
      returned: always
      type: str
      sample: null
    vnet_id:
      description:
        - ID of the Vnet created for OSA cluster.
      returned: always
      type: str
      sample: null
router_profiles:
  description:
    - Configuration for OpenShift router(s).
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - Name of the router profile.
      returned: always
      type: str
      sample: null
    public_subdomain:
      description:
        - DNS subdomain for OpenShift router.
      returned: always
      type: str
      sample: null
    fqdn:
      description:
        - Auto-allocated FQDN for the OpenShift router.
      returned: always
      type: str
      sample: null
master_pool_profile:
  description:
    - Configuration for OpenShift master VMs.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - >-
          Unique name of the master pool profile in the context of the
          subscription and resource group.
      returned: always
      type: str
      sample: null
    count:
      description:
        - >-
          Number of masters (VMs) to host docker containers. The default value
          is 3.
      returned: always
      type: integer
      sample: null
    vm_size:
      description:
        - Size of agent VMs.
      returned: always
      type: str
      sample: null
    subnet_cidr:
      description:
        - Subnet CIDR for the peering.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - >-
          OsType to be used to specify os type. Choose from Linux and Windows.
          Default to Linux.
      returned: always
      type: str
      sample: null
agent_pool_profiles:
  description:
    - Configuration of OpenShift cluster VMs.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - >-
          Unique name of the pool profile in the context of the subscription and
          resource group.
      returned: always
      type: str
      sample: null
    count:
      description:
        - Number of agents (VMs) to host docker containers.
      returned: always
      type: integer
      sample: null
    vm_size:
      description:
        - Size of agent VMs.
      returned: always
      type: str
      sample: null
    subnet_cidr:
      description:
        - Subnet CIDR for the peering.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - >-
          OsType to be used to specify os type. Choose from Linux and Windows.
          Default to Linux.
      returned: always
      type: str
      sample: null
    role:
      description:
        - Define the role of the AgentPoolProfile.
      returned: always
      type: str
      sample: null
identity_providers:
  description:
    - Type of authentication profile to use.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - Name of the provider.
      returned: always
      type: str
      sample: null
    provider:
      description:
        - Configuration of the provider.
      returned: always
      type: dict
      sample: null
      contains:
        kind:
          description:
            - The kind of the provider.
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
    from azure.mgmt.container import ContainerServiceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOpenShiftManagedCluster(AzureRMModuleBaseExt):
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
            plan=dict(
                type='dict',
                disposition='/plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    product=dict(
                        type='str',
                        disposition='product'
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='promotion_code'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    )
                )
            ),
            open_shift_version=dict(
                type='str',
                disposition='/open_shift_version'
            ),
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    vnet_cidr=dict(
                        type='str',
                        disposition='vnet_cidr'
                    ),
                    peer_vnet_id=dict(
                        type='str',
                        disposition='peer_vnet_id'
                    ),
                    vnet_id=dict(
                        type='str',
                        disposition='vnet_id'
                    )
                )
            ),
            router_profiles=dict(
                type='list',
                disposition='/router_profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    public_subdomain=dict(
                        type='str',
                        updatable=False,
                        disposition='public_subdomain'
                    ),
                    fqdn=dict(
                        type='str',
                        updatable=False,
                        disposition='fqdn'
                    )
                )
            ),
            master_pool_profile=dict(
                type='dict',
                disposition='/master_pool_profile',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    count=dict(
                        type='integer',
                        disposition='count',
                        required=True
                    ),
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
                        choices=['Standard_D2s_v3',
                                 'Standard_D4s_v3',
                                 'Standard_D8s_v3',
                                 'Standard_D16s_v3',
                                 'Standard_D32s_v3',
                                 'Standard_D64s_v3',
                                 'Standard_DS4_v2',
                                 'Standard_DS5_v2',
                                 'Standard_F8s_v2',
                                 'Standard_F16s_v2',
                                 'Standard_F32s_v2',
                                 'Standard_F64s_v2',
                                 'Standard_F72s_v2',
                                 'Standard_F8s',
                                 'Standard_F16s',
                                 'Standard_E4s_v3',
                                 'Standard_E8s_v3',
                                 'Standard_E16s_v3',
                                 'Standard_E20s_v3',
                                 'Standard_E32s_v3',
                                 'Standard_E64s_v3',
                                 'Standard_GS2',
                                 'Standard_GS3',
                                 'Standard_GS4',
                                 'Standard_GS5',
                                 'Standard_DS12_v2',
                                 'Standard_DS13_v2',
                                 'Standard_DS14_v2',
                                 'Standard_DS15_v2',
                                 'Standard_L4s',
                                 'Standard_L8s',
                                 'Standard_L16s',
                                 'Standard_L32s'],
                        required=True
                    ),
                    subnet_cidr=dict(
                        type='str',
                        disposition='subnet_cidr'
                    ),
                    os_type=dict(
                        type='str',
                        disposition='os_type',
                        choices=['Linux',
                                 'Windows']
                    )
                )
            ),
            agent_pool_profiles=dict(
                type='list',
                disposition='/agent_pool_profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    count=dict(
                        type='integer',
                        disposition='count',
                        required=True
                    ),
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
                        choices=['Standard_D2s_v3',
                                 'Standard_D4s_v3',
                                 'Standard_D8s_v3',
                                 'Standard_D16s_v3',
                                 'Standard_D32s_v3',
                                 'Standard_D64s_v3',
                                 'Standard_DS4_v2',
                                 'Standard_DS5_v2',
                                 'Standard_F8s_v2',
                                 'Standard_F16s_v2',
                                 'Standard_F32s_v2',
                                 'Standard_F64s_v2',
                                 'Standard_F72s_v2',
                                 'Standard_F8s',
                                 'Standard_F16s',
                                 'Standard_E4s_v3',
                                 'Standard_E8s_v3',
                                 'Standard_E16s_v3',
                                 'Standard_E20s_v3',
                                 'Standard_E32s_v3',
                                 'Standard_E64s_v3',
                                 'Standard_GS2',
                                 'Standard_GS3',
                                 'Standard_GS4',
                                 'Standard_GS5',
                                 'Standard_DS12_v2',
                                 'Standard_DS13_v2',
                                 'Standard_DS14_v2',
                                 'Standard_DS15_v2',
                                 'Standard_L4s',
                                 'Standard_L8s',
                                 'Standard_L16s',
                                 'Standard_L32s'],
                        required=True
                    ),
                    subnet_cidr=dict(
                        type='str',
                        disposition='subnet_cidr'
                    ),
                    os_type=dict(
                        type='str',
                        disposition='os_type',
                        choices=['Linux',
                                 'Windows']
                    ),
                    role=dict(
                        type='str',
                        disposition='role',
                        choices=['compute',
                                 'infra']
                    )
                )
            ),
            identity_providers=dict(
                type='list',
                disposition='/identity_providers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    provider=dict(
                        type='dict',
                        disposition='provider',
                        options=dict(
                            kind=dict(
                                type='str',
                                disposition='kind',
                                required=True
                            )
                        )
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
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOpenShiftManagedCluster, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ContainerServiceClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-30')

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
            response = self.mgmt_client.open_shift_managed_clusters.create_or_update(resource_group_name=self.resource_group_name,
                                                                                     resource_name=self.resource_name,
                                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the OpenShiftManagedCluster instance.')
            self.fail('Error creating the OpenShiftManagedCluster instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.open_shift_managed_clusters.delete(resource_group_name=self.resource_group_name,
                                                                           resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the OpenShiftManagedCluster instance.')
            self.fail('Error deleting the OpenShiftManagedCluster instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.open_shift_managed_clusters.get(resource_group_name=self.resource_group_name,
                                                                        resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOpenShiftManagedCluster()


if __name__ == '__main__':
    main()
