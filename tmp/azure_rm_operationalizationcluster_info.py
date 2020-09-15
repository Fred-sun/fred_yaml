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
module: azure_rm_operationalizationcluster_info
version_added: '2.9'
short_description: Get OperationalizationCluster info.
description:
  - Get info of OperationalizationCluster.
options:
  resource_group_name:
    description:
      - Name of the resource group in which the cluster is located.
    type: str
  cluster_name:
    description:
      - The name of the cluster.
    type: str
  skiptoken:
    description:
      - Continuation token for pagination.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GET Operationalization Cluster
      azure_rm_operationalizationcluster_info: 
        cluster_name: myCluster
        resource_group_name: myResourceGroup
        

    - name: List Operationalization Clusters by Resource Group
      azure_rm_operationalizationcluster_info: 
        resource_group_name: myResourceGroup
        

    - name: List Operationalization Clusters by Subscription
      azure_rm_operationalizationcluster_info: 
        {}
        

'''

RETURN = '''
operationalization_clusters:
  description: >-
    A list of dict results where the key is the name of the
    OperationalizationCluster and the values are the facts for that
    OperationalizationCluster.
  returned: always
  type: complex
  contains:
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
          The provision state of the cluster. Valid values are Unknown,
          Updating, Provisioning, Succeeded, and Failed.
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
              The SSL key data in PEM format. This is not returned in response
              of GET/PUT on the resource. To see this please call listKeys API.
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
              The primary auth key hash. This is not returned in response of
              GET/PUT on the resource.. To see this please call listKeys API.
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
              If auto-scale is enabled for all services. Each service can turn
              it off individually.
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
        - >-
          Type of orchestrator. It cannot be changed once the cluster is
          created.
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
          The number of agent nodes in the Container Service. This can be
          changed to scale the cluster.
      returned: always
      type: integer
      sample: null
    agent_vm_size:
      description:
        - >-
          The Azure VM size of the agent VM nodes. This cannot be changed once
          the cluster is created. This list is non exhaustive; refer to
          https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
          for the possible VM sizes.
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
          ARM resource ID of the Azure Storage Account to store CLI specific
          files. If not provided one will be created. This cannot be changed
          once the cluster is created.
      returned: always
      type: str
      sample: null
    value:
      description:
        - An array of cluster objects.
      returned: always
      type: list
      sample: null
      contains:
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
              The provision state of the cluster. Valid values are Unknown,
              Updating, Provisioning, Succeeded, and Failed.
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
                  The SSL key data in PEM format. This is not returned in
                  response of GET/PUT on the resource. To see this please call
                  listKeys API.
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
              Optional global authorization keys for all user services deployed
              in cluster. These are used if the service does not have auth keys.
          returned: always
          type: dict
          sample: null
          contains:
            primary_auth_key_hash:
              description:
                - >-
                  The primary auth key hash. This is not returned in response of
                  GET/PUT on the resource.. To see this please call listKeys
                  API.
              returned: always
              type: str
              sample: null
            secondary_auth_key_hash:
              description:
                - >-
                  The secondary auth key hash. This is not returned in response
                  of GET/PUT on the resource.. To see this please call listKeys
                  API.
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
                  If auto-scale is enabled for all services. Each service can
                  turn it off individually.
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
            - >-
              Type of orchestrator. It cannot be changed once the cluster is
              created.
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
              The number of agent nodes in the Container Service. This can be
              changed to scale the cluster.
          returned: always
          type: integer
          sample: null
        agent_vm_size:
          description:
            - >-
              The Azure VM size of the agent VM nodes. This cannot be changed
              once the cluster is created. This list is non exhaustive; refer to
              https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
              for the possible VM sizes.
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
                  The service principal secret. This is not returned in response
                  of GET/PUT on the resource. To see this please call listKeys.
              returned: always
              type: str
              sample: null
        resource_id_properties_container_registry_resource_id:
          description:
            - >-
              ARM resource ID of the Azure Container Registry used to store
              Docker images for web services in the cluster. If not provided one
              will be created. This cannot be changed once the cluster is
              created.
          returned: always
          type: str
          sample: null
        resource_id_properties_storage_account_resource_id:
          description:
            - >-
              ARM resource ID of the Azure Storage Account to store CLI specific
              files. If not provided one will be created. This cannot be changed
              once the cluster is created.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          A continuation link (absolute URI) to the next page of results in the
          list.
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
    from azure.mgmt.machine import Machine Learning Compute Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationalizationClusterInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            cluster_name=dict(
                type='str'
            ),
            skiptoken=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.skiptoken = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-08-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationalizationClusterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Machine Learning Compute Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-08-01-preview')

        if (self.resource_group_name is not None and
            self.cluster_name is not None):
            self.results['operationalization_clusters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['operationalization_clusters'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['operationalization_clusters'] = self.format_item(self.listbysubscriptionid())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.operationalization_clusters.get(resource_group_name=self.resource_group_name,
                                                                        cluster_name=self.cluster_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.operationalization_clusters.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                           skiptoken=self.skiptoken)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscriptionid(self):
        response = None

        try:
            response = self.mgmt_client.operationalization_clusters.list_by_subscription_id(skiptoken=self.skiptoken)
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
    AzureRMOperationalizationClusterInfo()


if __name__ == '__main__':
    main()
