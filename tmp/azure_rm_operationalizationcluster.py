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
module: azure_rm_operationalizationcluster
version_added: '2.9'
short_description: Manage Azure OperationalizationCluster instance.
description:
  - 'Create, update and delete instance of Azure OperationalizationCluster.'
options:
  resource_group_name:
    description:
      - Name of the resource group in which the cluster is located.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the cluster.
    required: true
    type: str
  location:
    description:
      - Specifies the location of the resource.
    type: str
  description:
    description:
      - The description of the cluster.
    type: str
  cluster_type:
    description:
      - The cluster type.
    type: str
    choices:
      - ACS
      - Local
  etag:
    description:
      - The configuration ETag for updates.
    type: str
  ssl:
    description:
      - The SSL configuration properties
    type: dict
    suboptions:
      status:
        description:
          - SSL status. Allowed values are Enabled and Disabled.
        type: str
        choices:
          - Enabled
          - Disabled
      cert:
        description:
          - The SSL cert data in PEM format.
        type: str
      key:
        description:
          - >-
            The SSL key data in PEM format. This is not returned in response of
            GET/PUT on the resource. To see this please call listKeys API.
        type: str
      cname:
        description:
          - The CName of the certificate.
        type: str
  service_auth:
    description:
      - >-
        Optional global authorization keys for all user services deployed in
        cluster. These are used if the service does not have auth keys.
    type: dict
    suboptions:
      primary_auth_key_hash:
        description:
          - >-
            The primary auth key hash. This is not returned in response of
            GET/PUT on the resource.. To see this please call listKeys API.
        required: true
        type: str
      secondary_auth_key_hash:
        description:
          - >-
            The secondary auth key hash. This is not returned in response of
            GET/PUT on the resource.. To see this please call listKeys API.
        required: true
        type: str
  auto_scale:
    description:
      - The auto-scale configuration
    type: dict
    suboptions:
      status:
        description:
          - >-
            If auto-scale is enabled for all services. Each service can turn it
            off individually.
        type: str
        choices:
          - Enabled
          - Disabled
      min_replicas:
        description:
          - The minimum number of replicas for each service.
        type: integer
      max_replicas:
        description:
          - The maximum number of replicas for each service.
        type: integer
      target_utilization:
        description:
          - The target utilization.
        type: number
      refresh_period_in_seconds:
        description:
          - Refresh period in seconds.
        type: integer
  resource_id:
    description:
      - ARM resource ID of the App Insights.
    type: str
  orchestrator_type:
    description:
      - Type of orchestrator. It cannot be changed once the cluster is created.
    type: str
    choices:
      - Kubernetes
      - None
  system_services:
    description:
      - The system services deployed to the cluster
    type: list
    suboptions:
      system_service_type:
        description:
          - The system service type
        required: true
        type: str
        choices:
          - None
          - ScoringFrontEnd
          - BatchFrontEnd
      public_ip_address:
        description:
          - The public IP address of the system service
        type: str
      version:
        description:
          - The state of the system service
        type: str
  master_count:
    description:
      - The number of master nodes in the container service.
    type: integer
  agent_count:
    description:
      - >-
        The number of agent nodes in the Container Service. This can be changed
        to scale the cluster.
    type: integer
  agent_vm_size:
    description:
      - >-
        The Azure VM size of the agent VM nodes. This cannot be changed once the
        cluster is created. This list is non exhaustive; refer to
        https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
        for the possible VM sizes.
    type: str
    choices:
      - Standard_A0
      - Standard_A1
      - Standard_A2
      - Standard_A3
      - Standard_A4
      - Standard_A5
      - Standard_A6
      - Standard_A7
      - Standard_A8
      - Standard_A9
      - Standard_A10
      - Standard_A11
      - Standard_D1
      - Standard_D2
      - Standard_D3
      - Standard_D4
      - Standard_D11
      - Standard_D12
      - Standard_D13
      - Standard_D14
      - Standard_D1_v2
      - Standard_D2_v2
      - Standard_D3_v2
      - Standard_D4_v2
      - Standard_D5_v2
      - Standard_D11_v2
      - Standard_D12_v2
      - Standard_D13_v2
      - Standard_D14_v2
      - Standard_G1
      - Standard_G2
      - Standard_G3
      - Standard_G4
      - Standard_G5
      - Standard_DS1
      - Standard_DS2
      - Standard_DS3
      - Standard_DS4
      - Standard_DS11
      - Standard_DS12
      - Standard_DS13
      - Standard_DS14
      - Standard_GS1
      - Standard_GS2
      - Standard_GS3
      - Standard_GS4
      - Standard_GS5
  service_principal:
    description:
      - The Azure Service Principal used by Kubernetes
    type: dict
    suboptions:
      client_id:
        description:
          - The service principal client ID
        required: true
        type: str
      secret:
        description:
          - >-
            The service principal secret. This is not returned in response of
            GET/PUT on the resource. To see this please call listKeys.
        required: true
        type: str
  container_registry_properties_resource_id:
    description:
      - >-
        ARM resource ID of the Azure Container Registry used to store Docker
        images for web services in the cluster. If not provided one will be
        created. This cannot be changed once the cluster is created.
    type: str
  storage_account_properties_resource_id:
    description:
      - >-
        ARM resource ID of the Azure Storage Account to store CLI specific
        files. If not provided one will be created. This cannot be changed once
        the cluster is created.
    type: str
  delete_all:
    description:
      - 'If true, deletes all resources associated with this cluster.'
    type: bool
  state:
    description:
      - Assert the state of the OperationalizationCluster.
      - >-
        Use C(present) to create or update an OperationalizationCluster and
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
    - name: PUT Operationalization Cluster
      azure_rm_operationalizationcluster: 
        cluster_name: myCluster
        resource_group_name: myResourceGroup
        location: West US
        properties:
          description: My Operationalization Cluster
          cluster_type: ACS
          container_service:
            orchestrator_properties:
              service_principal:
                client_id: abcdefghijklmnopqrt
                secret: uiuiwueiwuewiue
            orchestrator_type: Kubernetes
          global_service_configuration:
            ssl:
              cert: afjdklq2131casfakld=
              cname: foo.bar.com
              key: flksdafkldsajf=
              status: Enabled
        tags:
          key1: alpha
          key2: beta
        

    - name: PATCH Operationalization Cluster
      azure_rm_operationalizationcluster: 
        cluster_name: myCluster
        resource_group_name: myResourceGroup
        tags:
          key1: value1
        

    - name: DELETE Operationalization Cluster
      azure_rm_operationalizationcluster: 
        cluster_name: myCluster
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
id:
  description:
    - Specifies the resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Specifies the name of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - Specifies the location of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - Specifies the type of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Contains resource tags defined as key/value pairs.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - The description of the cluster.
  returned: always
  type: str
  sample: null
created_on:
  description:
    - The date and time when the cluster was created.
  returned: always
  type: str
  sample: null
modified_on:
  description:
    - The date and time when the cluster was last modified.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - >-
      The provision state of the cluster. Valid values are Unknown, Updating,
      Provisioning, Succeeded, and Failed.
  returned: always
  type: str
  sample: null
provisioning_errors:
  description:
    - List of provisioning errors reported by the resource provider.
  returned: always
  type: list
  sample: null
  contains:
    error:
      description:
        - The error response.
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - Error code.
          returned: always
          type: str
          sample: null
        message:
          description:
            - Error message.
          returned: always
          type: str
          sample: null
        details:
          description:
            - An array of error detail objects.
          returned: always
          type: list
          sample: null
          contains:
            code:
              description:
                - Error code.
              returned: always
              type: str
              sample: null
            message:
              description:
                - Error message.
              returned: always
              type: str
              sample: null
cluster_type:
  description:
    - The cluster type.
  returned: always
  type: str
  sample: null
etag:
  description:
    - The configuration ETag for updates.
  returned: always
  type: str
  sample: null
ssl:
  description:
    - The SSL configuration properties
  returned: always
  type: dict
  sample: null
  contains:
    status:
      description:
        - SSL status. Allowed values are Enabled and Disabled.
      returned: always
      type: str
      sample: null
    cert:
      description:
        - The SSL cert data in PEM format.
      returned: always
      type: str
      sample: null
    key:
      description:
        - >-
          The SSL key data in PEM format. This is not returned in response of
          GET/PUT on the resource. To see this please call listKeys API.
      returned: always
      type: str
      sample: null
    cname:
      description:
        - The CName of the certificate.
      returned: always
      type: str
      sample: null
service_auth:
  description:
    - >-
      Optional global authorization keys for all user services deployed in
      cluster. These are used if the service does not have auth keys.
  returned: always
  type: dict
  sample: null
  contains:
    primary_auth_key_hash:
      description:
        - >-
          The primary auth key hash. This is not returned in response of GET/PUT
          on the resource.. To see this please call listKeys API.
      returned: always
      type: str
      sample: null
    secondary_auth_key_hash:
      description:
        - >-
          The secondary auth key hash. This is not returned in response of
          GET/PUT on the resource.. To see this please call listKeys API.
      returned: always
      type: str
      sample: null
auto_scale:
  description:
    - The auto-scale configuration
  returned: always
  type: dict
  sample: null
  contains:
    status:
      description:
        - >-
          If auto-scale is enabled for all services. Each service can turn it
          off individually.
      returned: always
      type: str
      sample: null
    min_replicas:
      description:
        - The minimum number of replicas for each service.
      returned: always
      type: integer
      sample: null
    max_replicas:
      description:
        - The maximum number of replicas for each service.
      returned: always
      type: integer
      sample: null
    target_utilization:
      description:
        - The target utilization.
      returned: always
      type: number
      sample: null
    refresh_period_in_seconds:
      description:
        - Refresh period in seconds.
      returned: always
      type: integer
      sample: null
resource_id_properties_app_insights_resource_id:
  description:
    - ARM resource ID of the App Insights.
  returned: always
  type: str
  sample: null
cluster_fqdn:
  description:
    - 'The FQDN of the cluster. '
  returned: always
  type: str
  sample: null
orchestrator_type:
  description:
    - Type of orchestrator. It cannot be changed once the cluster is created.
  returned: always
  type: str
  sample: null
system_services:
  description:
    - The system services deployed to the cluster
  returned: always
  type: list
  sample: null
  contains:
    system_service_type:
      description:
        - The system service type
      returned: always
      type: str
      sample: null
    public_ip_address:
      description:
        - The public IP address of the system service
      returned: always
      type: str
      sample: null
    version:
      description:
        - The state of the system service
      returned: always
      type: str
      sample: null
master_count:
  description:
    - The number of master nodes in the container service.
  returned: always
  type: integer
  sample: null
agent_count:
  description:
    - >-
      The number of agent nodes in the Container Service. This can be changed to
      scale the cluster.
  returned: always
  type: integer
  sample: null
agent_vm_size:
  description:
    - >-
      The Azure VM size of the agent VM nodes. This cannot be changed once the
      cluster is created. This list is non exhaustive; refer to
      https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes for
      the possible VM sizes.
  returned: always
  type: str
  sample: null
service_principal:
  description:
    - The Azure Service Principal used by Kubernetes
  returned: always
  type: dict
  sample: null
  contains:
    client_id:
      description:
        - The service principal client ID
      returned: always
      type: str
      sample: null
    secret:
      description:
        - >-
          The service principal secret. This is not returned in response of
          GET/PUT on the resource. To see this please call listKeys.
      returned: always
      type: str
      sample: null
resource_id_properties_container_registry_resource_id:
  description:
    - >-
      ARM resource ID of the Azure Container Registry used to store Docker
      images for web services in the cluster. If not provided one will be
      created. This cannot be changed once the cluster is created.
  returned: always
  type: str
  sample: null
resource_id_properties_storage_account_resource_id:
  description:
    - >-
      ARM resource ID of the Azure Storage Account to store CLI specific files.
      If not provided one will be created. This cannot be changed once the
      cluster is created.
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
    from azure.mgmt.machine import Machine Learning Compute Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOperationalizationCluster(AzureRMModuleBaseExt):
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
            description=dict(
                type='str',
                disposition='/description'
            ),
            cluster_type=dict(
                type='str',
                disposition='/cluster_type',
                choices=['ACS',
                         'Local']
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            ssl=dict(
                type='dict',
                disposition='/ssl',
                options=dict(
                    status=dict(
                        type='str',
                        disposition='status',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    cert=dict(
                        type='str',
                        disposition='cert'
                    ),
                    key=dict(
                        type='str',
                        disposition='key'
                    ),
                    cname=dict(
                        type='str',
                        disposition='cname'
                    )
                )
            ),
            service_auth=dict(
                type='dict',
                disposition='/service_auth',
                options=dict(
                    primary_auth_key_hash=dict(
                        type='str',
                        disposition='primary_auth_key_hash',
                        required=True
                    ),
                    secondary_auth_key_hash=dict(
                        type='str',
                        disposition='secondary_auth_key_hash',
                        required=True
                    )
                )
            ),
            auto_scale=dict(
                type='dict',
                disposition='/auto_scale',
                options=dict(
                    status=dict(
                        type='str',
                        disposition='status',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    min_replicas=dict(
                        type='integer',
                        disposition='min_replicas'
                    ),
                    max_replicas=dict(
                        type='integer',
                        disposition='max_replicas'
                    ),
                    target_utilization=dict(
                        type='number',
                        disposition='target_utilization'
                    ),
                    refresh_period_in_seconds=dict(
                        type='integer',
                        disposition='refresh_period_in_seconds'
                    )
                )
            ),
            resource_id=dict(
                type='str',
                disposition='/resource_id'
            ),
            orchestrator_type=dict(
                type='str',
                disposition='/orchestrator_type',
                choices=['Kubernetes',
                         'None']
            ),
            system_services=dict(
                type='list',
                disposition='/system_services',
                elements='dict',
                options=dict(
                    system_service_type=dict(
                        type='str',
                        disposition='system_service_type',
                        choices=['None',
                                 'ScoringFrontEnd',
                                 'BatchFrontEnd'],
                        required=True
                    ),
                    public_ip_address=dict(
                        type='str',
                        updatable=False,
                        disposition='public_ip_address'
                    ),
                    version=dict(
                        type='str',
                        updatable=False,
                        disposition='version'
                    )
                )
            ),
            master_count=dict(
                type='integer',
                disposition='/master_count'
            ),
            agent_count=dict(
                type='integer',
                disposition='/agent_count'
            ),
            agent_vm_size=dict(
                type='str',
                disposition='/agent_vm_size',
                choices=['Standard_A0',
                         'Standard_A1',
                         'Standard_A2',
                         'Standard_A3',
                         'Standard_A4',
                         'Standard_A5',
                         'Standard_A6',
                         'Standard_A7',
                         'Standard_A8',
                         'Standard_A9',
                         'Standard_A10',
                         'Standard_A11',
                         'Standard_D1',
                         'Standard_D2',
                         'Standard_D3',
                         'Standard_D4',
                         'Standard_D11',
                         'Standard_D12',
                         'Standard_D13',
                         'Standard_D14',
                         'Standard_D1_v2',
                         'Standard_D2_v2',
                         'Standard_D3_v2',
                         'Standard_D4_v2',
                         'Standard_D5_v2',
                         'Standard_D11_v2',
                         'Standard_D12_v2',
                         'Standard_D13_v2',
                         'Standard_D14_v2',
                         'Standard_G1',
                         'Standard_G2',
                         'Standard_G3',
                         'Standard_G4',
                         'Standard_G5',
                         'Standard_DS1',
                         'Standard_DS2',
                         'Standard_DS3',
                         'Standard_DS4',
                         'Standard_DS11',
                         'Standard_DS12',
                         'Standard_DS13',
                         'Standard_DS14',
                         'Standard_GS1',
                         'Standard_GS2',
                         'Standard_GS3',
                         'Standard_GS4',
                         'Standard_GS5']
            ),
            service_principal=dict(
                type='dict',
                disposition='/service_principal',
                options=dict(
                    client_id=dict(
                        type='str',
                        disposition='client_id',
                        required=True
                    ),
                    secret=dict(
                        type='str',
                        disposition='secret',
                        required=True
                    )
                )
            ),
            container_registry_properties_resource_id=dict(
                type='str',
                disposition='/container_registry_properties_resource_id'
            ),
            storage_account_properties_resource_id=dict(
                type='str',
                disposition='/storage_account_properties_resource_id'
            ),
            delete_all=dict(
                type='bool'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.delete_all = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOperationalizationCluster, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Machine Learning Compute Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-08-01-preview')

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
            response = self.mgmt_client.operationalization_clusters.create_or_update(resource_group_name=self.resource_group_name,
                                                                                     cluster_name=self.cluster_name,
                                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the OperationalizationCluster instance.')
            self.fail('Error creating the OperationalizationCluster instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.operationalization_clusters.delete(resource_group_name=self.resource_group_name,
                                                                           cluster_name=self.cluster_name,
                                                                           delete_all=self.delete_all)
        except CloudError as e:
            self.log('Error attempting to delete the OperationalizationCluster instance.')
            self.fail('Error deleting the OperationalizationCluster instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.operationalization_clusters.get(resource_group_name=self.resource_group_name,
                                                                        cluster_name=self.cluster_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOperationalizationCluster()


if __name__ == '__main__':
    main()
