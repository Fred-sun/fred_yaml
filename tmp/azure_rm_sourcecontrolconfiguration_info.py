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
module: azure_rm_sourcecontrolconfiguration_info
version_added: '2.9'
short_description: Get SourceControlConfiguration info.
description:
  - Get info of SourceControlConfiguration.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  cluster_rp:
    description:
      - >-
        The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
        clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
    required: true
    type: str
    choices:
      - Microsoft.ContainerService
      - Microsoft.Kubernetes
  cluster_resource_name:
    description:
      - >-
        The Kubernetes cluster resource name - either managedClusters (for AKS
        clusters) or connectedClusters (for OnPrem K8S clusters).
    required: true
    type: str
    choices:
      - managedClusters
      - connectedClusters
  cluster_name:
    description:
      - The name of the kubernetes cluster.
    required: true
    type: str
  source_control_configuration_name:
    description:
      - Name of the Source Control Configuration.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Source Control Configuration
      azure_rm_sourcecontrolconfiguration_info: 
        cluster_name: clusterName1
        cluster_resource_name: connectedClusters
        resource_group_name: rg1
        source_control_configuration_name: SRS_GitHubConfig
        

    - name: List Source Control Configuration
      azure_rm_sourcecontrolconfiguration_info: 
        cluster_name: clusterName1
        cluster_resource_name: connectedClusters
        resource_group_name: rg1
        

'''

RETURN = '''
source_control_configurations:
  description: >-
    A list of dict results where the key is the name of the
    SourceControlConfiguration and the values are the facts for that
    SourceControlConfiguration.
  returned: always
  type: complex
  contains:
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
    repository_url:
      description:
        - Url of the SourceControl Repository.
      returned: always
      type: str
      sample: null
    operator_namespace:
      description:
        - >-
          The namespace to which this operator is installed to. Maximum of 253
          lower case alphanumeric characters, hyphen and period only.
      returned: always
      type: str
      sample: null
    operator_instance_name:
      description:
        - >-
          Instance name of the operator - identifying the specific
          configuration.
      returned: always
      type: str
      sample: null
    operator_type:
      description:
        - Type of the operator
      returned: always
      type: str
      sample: null
    operator_params:
      description:
        - Any Parameters for the Operator instance in string format.
      returned: always
      type: str
      sample: null
    operator_scope:
      description:
        - Scope at which the operator will be installed.
      returned: always
      type: str
      sample: null
    repository_public_key:
      description:
        - >-
          Public Key associated with this SourceControl configuration (either
          generated within the cluster or provided by the user).
      returned: always
      type: str
      sample: null
    enable_helm_operator:
      description:
        - Option to enable Helm Operator for this git configuration.
      returned: always
      type: str
      sample: null
    helm_operator_properties:
      description:
        - Properties for Helm operator.
      returned: always
      type: dict
      sample: null
      contains:
        chart_version:
          description:
            - Version of the operator Helm chart.
          returned: always
          type: str
          sample: null
        chart_values:
          description:
            - Values override for the operator Helm chart.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource provider.
      returned: always
      type: str
      sample: null
    compliance_status:
      description:
        - Compliance Status of the Configuration
      returned: always
      type: dict
      sample: null
      contains:
        compliance_state:
          description:
            - The compliance state of the configuration.
          returned: always
          type: str
          sample: null
        last_config_applied:
          description:
            - Datetime the configuration was last applied.
          returned: always
          type: str
          sample: null
        message:
          description:
            - Message from when the configuration was applied.
          returned: always
          type: str
          sample: null
        message_level:
          description:
            - Level of the message.
          returned: always
          type: str
          sample: null
    value:
      description:
        - List of Source Control Configurations within a Kubernetes cluster.
      returned: always
      type: list
      sample: null
      contains:
        repository_url:
          description:
            - Url of the SourceControl Repository.
          returned: always
          type: str
          sample: null
        operator_namespace:
          description:
            - >-
              The namespace to which this operator is installed to. Maximum of
              253 lower case alphanumeric characters, hyphen and period only.
          returned: always
          type: str
          sample: null
        operator_instance_name:
          description:
            - >-
              Instance name of the operator - identifying the specific
              configuration.
          returned: always
          type: str
          sample: null
        operator_type:
          description:
            - Type of the operator
          returned: always
          type: str
          sample: null
        operator_params:
          description:
            - Any Parameters for the Operator instance in string format.
          returned: always
          type: str
          sample: null
        operator_scope:
          description:
            - Scope at which the operator will be installed.
          returned: always
          type: str
          sample: null
        repository_public_key:
          description:
            - >-
              Public Key associated with this SourceControl configuration
              (either generated within the cluster or provided by the user).
          returned: always
          type: str
          sample: null
        enable_helm_operator:
          description:
            - Option to enable Helm Operator for this git configuration.
          returned: always
          type: str
          sample: null
        helm_operator_properties:
          description:
            - Properties for Helm operator.
          returned: always
          type: dict
          sample: null
          contains:
            chart_version:
              description:
                - Version of the operator Helm chart.
              returned: always
              type: str
              sample: null
            chart_values:
              description:
                - Values override for the operator Helm chart.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - The provisioning state of the resource provider.
          returned: always
          type: str
          sample: null
        compliance_status:
          description:
            - Compliance Status of the Configuration
          returned: always
          type: dict
          sample: null
          contains:
            compliance_state:
              description:
                - The compliance state of the configuration.
              returned: always
              type: str
              sample: null
            last_config_applied:
              description:
                - Datetime the configuration was last applied.
              returned: always
              type: str
              sample: null
            message:
              description:
                - Message from when the configuration was applied.
              returned: always
              type: str
              sample: null
            message_level:
              description:
                - Level of the message.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - 'URL to get the next set of configuration objects, if any.'
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
    from azure.mgmt.source import SourceControlConfigurationClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSourceControlConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_rp=dict(
                type='str',
                choices=['Microsoft.ContainerService',
                         'Microsoft.Kubernetes'],
                required=True
            ),
            cluster_resource_name=dict(
                type='str',
                choices=['managedClusters',
                         'connectedClusters'],
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            source_control_configuration_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_rp = None
        self.cluster_resource_name = None
        self.cluster_name = None
        self.source_control_configuration_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-11-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSourceControlConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SourceControlConfigurationClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01-preview')

        if (self.resource_group_name is not None and
            self.cluster_rp is not None and
            self.cluster_resource_name is not None and
            self.cluster_name is not None and
            self.source_control_configuration_name is not None):
            self.results['source_control_configurations'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.cluster_rp is not None and
              self.cluster_resource_name is not None and
              self.cluster_name is not None):
            self.results['source_control_configurations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.source_control_configurations.get(resource_group_name=self.resource_group_name,
                                                                          cluster_rp=self.cluster_rp,
                                                                          cluster_resource_name=self.cluster_resource_name,
                                                                          cluster_name=self.cluster_name,
                                                                          source_control_configuration_name=self.source_control_configuration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.source_control_configurations.list(resource_group_name=self.resource_group_name,
                                                                           cluster_rp=self.cluster_rp,
                                                                           cluster_resource_name=self.cluster_resource_name,
                                                                           cluster_name=self.cluster_name)
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
    AzureRMSourceControlConfigurationInfo()


if __name__ == '__main__':
    main()
