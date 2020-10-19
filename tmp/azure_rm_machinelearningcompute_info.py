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
module: azure_rm_machinelearningcompute_info
version_added: '2.9'
short_description: Get MachineLearningCompute info.
description:
  - Get info of MachineLearningCompute.
options:
  resource_group_name:
    description:
      - Name of the resource group in which workspace is located.
    required: true
    type: str
  workspace_name:
    description:
      - Name of Azure Machine Learning workspace.
    required: true
    type: str
  skiptoken:
    description:
      - Continuation token for pagination.
    type: str
  compute_name:
    description:
      - Name of the Azure Machine Learning compute.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Computes
      azure_rm_machinelearningcompute_info: 
        resource_group_name: testrg123
        workspace_name: workspaces123
        

    - name: Get a AKS Compute
      azure_rm_machinelearningcompute_info: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        

    - name: Get a AML Compute
      azure_rm_machinelearningcompute_info: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        

    - name: Get a ComputeInstance
      azure_rm_machinelearningcompute_info: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        

'''

RETURN = '''
machine_learning_compute:
  description: >-
    A list of dict results where the key is the name of the
    MachineLearningCompute and the values are the facts for that
    MachineLearningCompute.
  returned: always
  type: complex
  contains:
    value:
      description:
        - >-
          An array of Machine Learning compute objects wrapped in ARM resource
          envelope.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - Compute properties
          returned: always
          type: dict
          sample: null
          contains:
            compute_type:
              description:
                - The type of compute
              returned: always
              type: str
              sample: null
            compute_location:
              description:
                - Location for the underlying compute
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
            description:
              description:
                - The description of the Machine Learning compute.
              returned: always
              type: str
              sample: null
            created_on:
              description:
                - The date and time when the compute was created.
              returned: always
              type: str
              sample: null
            modified_on:
              description:
                - The date and time when the compute was last modified.
              returned: always
              type: str
              sample: null
            resource_id:
              description:
                - ARM resource id of the underlying compute
              returned: always
              type: str
              sample: null
            provisioning_errors:
              description:
                - Errors during provisioning
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
            is_attached_compute:
              description:
                - >-
                  Indicating whether the compute was provisioned by user and
                  brought from outside if true, or machine learning service
                  provisioned it if false.
              returned: always
              type: bool
              sample: null
    next_link:
      description:
        - >-
          A continuation link (absolute URI) to the next page of results in the
          list.
      returned: always
      type: str
      sample: null
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
    sku:
      description:
        - The sku of the workspace.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of the sku
          returned: always
          type: str
          sample: null
        tier:
          description:
            - Tier of the sku like Basic or Enterprise
          returned: always
          type: str
          sample: null
    principal_id:
      description:
        - The principal ID of resource identity.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The tenant ID of resource.
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - The identity type.
      returned: always
      type: sealed-choice
      sample: null
    user_assigned_identities:
      description:
        - >-
          The list of user identities associated with resource. The user
          identity dictionary key references will be ARM resource ids in the
          form:
          '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
      returned: always
      type: dictionary
      sample: null
    properties:
      description:
        - Compute properties
      returned: always
      type: dict
      sample: null
      contains:
        compute_type:
          description:
            - The type of compute
          returned: always
          type: str
          sample: null
        compute_location:
          description:
            - Location for the underlying compute
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
        description:
          description:
            - The description of the Machine Learning compute.
          returned: always
          type: str
          sample: null
        created_on:
          description:
            - The date and time when the compute was created.
          returned: always
          type: str
          sample: null
        modified_on:
          description:
            - The date and time when the compute was last modified.
          returned: always
          type: str
          sample: null
        resource_id:
          description:
            - ARM resource id of the underlying compute
          returned: always
          type: str
          sample: null
        provisioning_errors:
          description:
            - Errors during provisioning
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
        is_attached_compute:
          description:
            - >-
              Indicating whether the compute was provisioned by user and brought
              from outside if true, or machine learning service provisioned it
              if false.
          returned: always
          type: bool
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Machine Learning Workspaces
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMachineLearningComputeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            ),
            skiptoken=dict(
                type='str'
            ),
            compute_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.skiptoken = None
        self.compute_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMachineLearningComputeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Machine Learning Workspaces,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.compute_name is not None):
            self.results['machine_learning_compute'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['machine_learning_compute'] = self.format_item(self.listbyworkspace())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.machine_learning_compute.get(resource_group_name=self.resource_group_name,
                                                                     workspace_name=self.workspace_name,
                                                                     compute_name=self.compute_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyworkspace(self):
        response = None

        try:
            response = self.mgmt_client.machine_learning_compute.list_by_workspace(resource_group_name=self.resource_group_name,
                                                                                   workspace_name=self.workspace_name,
                                                                                   skiptoken=self.skiptoken)
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
    AzureRMMachineLearningComputeInfo()


if __name__ == '__main__':
    main()
