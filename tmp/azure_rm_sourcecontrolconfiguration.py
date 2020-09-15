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
module: azure_rm_sourcecontrolconfiguration
version_added: '2.9'
short_description: Manage Azure SourceControlConfiguration instance.
description:
  - 'Create, update and delete instance of Azure SourceControlConfiguration.'
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
    required: true
    type: str
  repository_url:
    description:
      - Url of the SourceControl Repository.
    type: str
  operator_namespace:
    description:
      - >-
        The namespace to which this operator is installed to. Maximum of 253
        lower case alphanumeric characters, hyphen and period only.
    type: str
  operator_instance_name:
    description:
      - Instance name of the operator - identifying the specific configuration.
    type: str
  operator_type:
    description:
      - Type of the operator
    type: str
    choices:
      - Flux
  operator_params:
    description:
      - Any Parameters for the Operator instance in string format.
    type: str
  operator_scope:
    description:
      - Scope at which the operator will be installed.
    type: str
    choices:
      - cluster
      - namespace
  enable_helm_operator:
    description:
      - Option to enable Helm Operator for this git configuration.
    type: str
    choices:
      - 'true'
      - 'false'
  helm_operator_properties:
    description:
      - Properties for Helm operator.
    type: dict
    suboptions:
      chart_version:
        description:
          - Version of the operator Helm chart.
        type: str
      chart_values:
        description:
          - Values override for the operator Helm chart.
        type: str
  state:
    description:
      - Assert the state of the SourceControlConfiguration.
      - >-
        Use C(present) to create or update an SourceControlConfiguration and
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
    - name: Create Source Control Configuration
      azure_rm_sourcecontrolconfiguration: 
        cluster_name: clusterName1
        cluster_resource_name: connectedClusters
        resource_group_name: rg1
        source_control_configuration_name: SRS_GitHubConfig
        

    - name: Delete Source Control Configuration
      azure_rm_sourcecontrolconfiguration: 
        cluster_name: clusterName1
        cluster_resource_name: connectedClusters
        resource_group_name: rg1
        source_control_configuration_name: SRS_GitHubConfig
        

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
repository_url:
  description:
    - Url of the SourceControl Repository.
  returned: always
  type: str
  sample: null
operator_namespace:
  description:
    - >-
      The namespace to which this operator is installed to. Maximum of 253 lower
      case alphanumeric characters, hyphen and period only.
  returned: always
  type: str
  sample: null
operator_instance_name:
  description:
    - Instance name of the operator - identifying the specific configuration.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.source import SourceControlConfigurationClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSourceControlConfiguration(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            repository_url=dict(
                type='str',
                disposition='/repository_url'
            ),
            operator_namespace=dict(
                type='str',
                disposition='/operator_namespace'
            ),
            operator_instance_name=dict(
                type='str',
                disposition='/operator_instance_name'
            ),
            operator_type=dict(
                type='str',
                disposition='/operator_type',
                choices=['Flux']
            ),
            operator_params=dict(
                type='str',
                disposition='/operator_params'
            ),
            operator_scope=dict(
                type='str',
                disposition='/operator_scope',
                choices=['cluster',
                         'namespace']
            ),
            enable_helm_operator=dict(
                type='str',
                disposition='/enable_helm_operator',
                choices=['true',
                         'false']
            ),
            helm_operator_properties=dict(
                type='dict',
                disposition='/helm_operator_properties',
                options=dict(
                    chart_version=dict(
                        type='str',
                        disposition='chart_version'
                    ),
                    chart_values=dict(
                        type='str',
                        disposition='chart_values'
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
        self.cluster_rp = None
        self.cluster_resource_name = None
        self.cluster_name = None
        self.source_control_configuration_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSourceControlConfiguration, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SourceControlConfigurationClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01-preview')

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
            response = self.mgmt_client.source_control_configurations.create_or_update(resource_group_name=self.resource_group_name,
                                                                                       cluster_rp=self.cluster_rp,
                                                                                       cluster_resource_name=self.cluster_resource_name,
                                                                                       cluster_name=self.cluster_name,
                                                                                       source_control_configuration_name=self.source_control_configuration_name,
                                                                                       source_control_configuration=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SourceControlConfiguration instance.')
            self.fail('Error creating the SourceControlConfiguration instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.source_control_configurations.delete(resource_group_name=self.resource_group_name,
                                                                             cluster_rp=self.cluster_rp,
                                                                             cluster_resource_name=self.cluster_resource_name,
                                                                             cluster_name=self.cluster_name,
                                                                             source_control_configuration_name=self.source_control_configuration_name)
        except CloudError as e:
            self.log('Error attempting to delete the SourceControlConfiguration instance.')
            self.fail('Error deleting the SourceControlConfiguration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.source_control_configurations.get(resource_group_name=self.resource_group_name,
                                                                          cluster_rp=self.cluster_rp,
                                                                          cluster_resource_name=self.cluster_resource_name,
                                                                          cluster_name=self.cluster_name,
                                                                          source_control_configuration_name=self.source_control_configuration_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSourceControlConfiguration()


if __name__ == '__main__':
    main()
