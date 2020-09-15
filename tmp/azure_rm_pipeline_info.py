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
module: azure_rm_pipeline_info
version_added: '2.9'
short_description: Get Pipeline info.
description:
  - Get info of Pipeline.
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    type: str
  pipeline_name:
    description:
      - The name of the Azure Pipeline resource in ARM.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an existing Azure pipeline
      azure_rm_pipeline_info: 
        pipeline_name: myAspNetWebAppPipeline
        resource_group_name: myAspNetWebAppPipeline-rg
        

    - name: List all Azure Pipelines under the specified resource group
      azure_rm_pipeline_info: 
        resource_group_name: myAspNetWebAppPipeline-rg
        

    - name: List all Azure pipelines under the specified subscription
      azure_rm_pipeline_info: 
        {}
        

'''

RETURN = '''
pipelines:
  description: >-
    A list of dict results where the key is the name of the Pipeline and the
    values are the facts for that Pipeline.
  returned: always
  type: complex
  contains:
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
        - >-
          Unique identifier of the Azure Pipeline within the Azure DevOps
          Project.
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
    value:
      description:
        - List of pipelines.
      returned: always
      type: list
      sample: null
      contains:
        pipeline_id:
          description:
            - >-
              Unique identifier of the Azure Pipeline within the Azure DevOps
              Project.
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
              Default branch used to configure Continuous Integration (CI) in
              the pipeline.
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
    next_link:
      description:
        - 'URL to get the next set of Pipelines, if there are any.'
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
    from azure.mgmt.azure import Azure DevOps
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPipelineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            pipeline_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.pipeline_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPipelineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure DevOps,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01-preview')

        if (self.resource_group_name is not None and
            self.pipeline_name is not None):
            self.results['pipelines'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['pipelines'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['pipelines'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.pipelines.get(resource_group_name=self.resource_group_name,
                                                      pipeline_name=self.pipeline_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.pipelines.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.pipelines.list_by_subscription()
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
    AzureRMPipelineInfo()


if __name__ == '__main__':
    main()
