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
module: azure_rm_pipeline
version_added: '2.9'
short_description: Manage Azure Pipeline instance.
description:
  - 'Create, update and delete instance of Azure Pipeline.'
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    required: true
    type: str
  pipeline_name:
    description:
      - The name of the Azure Pipeline resource in ARM.
      - The name of the Azure Pipeline resource.
    required: true
    type: str
  location:
    description:
      - Resource Location
    type: str
  id:
    description:
      - Unique identifier of the pipeline template.
    type: str
  parameters:
    description:
      - Dictionary of input parameters used in the pipeline template.
    type: dictionary
  repository_type:
    description:
      - Type of code repository.
    type: str
    choices:
      - gitHub
      - vstsGit
  code_repository_id:
    description:
      - Unique immutable identifier of the code repository.
    type: str
  default_branch:
    description:
      - >-
        Default branch used to configure Continuous Integration (CI) in the
        pipeline.
    type: str
  properties:
    description:
      - Repository-specific properties.
    type: dictionary
  authorization_type:
    description:
      - Type of authorization.
    type: str
    choices:
      - personalAccessToken
  authorization_parameters:
    description:
      - Authorization parameters corresponding to the authorization type.
    type: dictionary
  name:
    description:
      - Name of the Azure DevOps Project.
    type: str
  organization_reference_name:
    description:
      - Name of the Azure DevOps Organization.
    type: str
  state:
    description:
      - Assert the state of the Pipeline.
      - >-
        Use C(present) to create or update an Pipeline and C(absent) to delete
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
    - name: Create an Azure pipeline to deploy a sample ASP.Net application to Azure web-app
      azure_rm_pipeline: 
        pipeline_name: myAspNetWebAppPipeline
        resource_group_name: myAspNetWebAppPipeline-rg
        

    - name: Get an existing Azure pipeline
      azure_rm_pipeline: 
        pipeline_name: myAspNetWebAppPipeline
        resource_group_name: myAspNetWebAppPipeline-rg
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource Type
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource Tags
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - Resource Location
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource Name
  returned: always
  type: str
  sample: null
pipeline_id:
  description:
    - Unique identifier of the Azure Pipeline within the Azure DevOps Project.
  returned: always
  type: integer
  sample: null
id_properties_bootstrap_configuration_template_id:
  description:
    - Unique identifier of the pipeline template.
  returned: always
  type: str
  sample: null
parameters_properties_bootstrap_configuration_template_parameters:
  description:
    - Dictionary of input parameters used in the pipeline template.
  returned: always
  type: dictionary
  sample: null
repository_type:
  description:
    - Type of code repository.
  returned: always
  type: str
  sample: null
id_properties_bootstrap_configuration_repository_id:
  description:
    - Unique immutable identifier of the code repository.
  returned: always
  type: str
  sample: null
default_branch:
  description:
    - >-
      Default branch used to configure Continuous Integration (CI) in the
      pipeline.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Repository-specific properties.
  returned: always
  type: dictionary
  sample: null
authorization_type:
  description:
    - Type of authorization.
  returned: always
  type: str
  sample: null
parameters_properties_bootstrap_configuration_repository_authorization_parameters:
  description:
    - Authorization parameters corresponding to the authorization type.
  returned: always
  type: dictionary
  sample: null
id_properties_project_id:
  description:
    - Unique immutable identifier of the Azure DevOps Project.
  returned: always
  type: str
  sample: null
name_properties_project_name:
  description:
    - Name of the Azure DevOps Project.
  returned: always
  type: str
  sample: null
id_properties_organization_id:
  description:
    - Unique immutable identifier for the Azure DevOps Organization.
  returned: always
  type: str
  sample: null
name_properties_organization_name:
  description:
    - Name of the Azure DevOps Organization.
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
    from azure.mgmt.azure import Azure DevOps
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPipeline(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            pipeline_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            parameters=dict(
                type='dictionary',
                disposition='/parameters'
            ),
            repository_type=dict(
                type='str',
                disposition='/repository_type',
                choices=['gitHub',
                         'vstsGit']
            ),
            code_repository_id=dict(
                type='str',
                disposition='/code_repository_id'
            ),
            default_branch=dict(
                type='str',
                disposition='/default_branch'
            ),
            properties=dict(
                type='dictionary',
                disposition='/properties'
            ),
            authorization_type=dict(
                type='str',
                disposition='/authorization_type',
                choices=['personalAccessToken']
            ),
            authorization_parameters=dict(
                type='dictionary',
                disposition='/authorization_parameters'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            organization_reference_name=dict(
                type='str',
                disposition='/organization_reference_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.pipeline_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPipeline, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure DevOps,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01-preview')

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
            response = self.mgmt_client.pipelines.create_or_update(resource_group_name=self.resource_group_name,
                                                                   pipeline_name=self.pipeline_name,
                                                                   create_operation_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Pipeline instance.')
            self.fail('Error creating the Pipeline instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.pipelines.delete(resource_group_name=self.resource_group_name,
                                                         pipeline_name=self.pipeline_name)
        except CloudError as e:
            self.log('Error attempting to delete the Pipeline instance.')
            self.fail('Error deleting the Pipeline instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.pipelines.get(resource_group_name=self.resource_group_name,
                                                      pipeline_name=self.pipeline_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPipeline()


if __name__ == '__main__':
    main()
