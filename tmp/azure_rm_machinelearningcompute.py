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
module: azure_rm_machinelearningcompute
version_added: '2.9'
short_description: Manage Azure MachineLearningCompute instance.
description:
  - 'Create, update and delete instance of Azure MachineLearningCompute.'
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
  compute_name:
    description:
      - Name of the Azure Machine Learning compute.
    required: true
    type: str
  location:
    description:
      - Specifies the location of the resource.
    type: str
  sku:
    description:
      - The sku of the workspace.
    type: dict
    suboptions:
      name:
        description:
          - Name of the sku
        type: str
      tier:
        description:
          - Tier of the sku like Basic or Enterprise
        type: str
  type:
    description:
      - The identity type.
    type: sealed-choice
  user_assigned_identities:
    description:
      - >-
        The list of user identities associated with resource. The user identity
        dictionary key references will be ARM resource ids in the form:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    type: dictionary
  properties:
    description:
      - Compute properties
    type: dict
    suboptions:
      compute_type:
        description:
          - The type of compute
        required: true
        type: str
        choices:
          - AKS
          - AmlCompute
          - ComputeInstance
          - DataFactory
          - VirtualMachine
          - HDInsight
          - Databricks
          - DataLakeAnalytics
      compute_location:
        description:
          - Location for the underlying compute
        type: str
      provisioning_state:
        description:
          - >-
            The provision state of the cluster. Valid values are Unknown,
            Updating, Provisioning, Succeeded, and Failed.
        type: str
        choices:
          - Unknown
          - Updating
          - Creating
          - Deleting
          - Succeeded
          - Failed
          - Canceled
      description:
        description:
          - The description of the Machine Learning compute.
        type: str
      created_on:
        description:
          - The date and time when the compute was created.
        type: str
      modified_on:
        description:
          - The date and time when the compute was last modified.
        type: str
      resource_id:
        description:
          - ARM resource id of the underlying compute
        type: str
      provisioning_errors:
        description:
          - Errors during provisioning
        type: list
        suboptions:
          error:
            description:
              - The error response.
            type: dict
            suboptions:
              code:
                description:
                  - Error code.
                type: str
              message:
                description:
                  - Error message.
                type: str
              details:
                description:
                  - An array of error detail objects.
                type: list
                suboptions:
                  code:
                    description:
                      - Error code.
                    required: true
                    type: str
                  message:
                    description:
                      - Error message.
                    required: true
                    type: str
      is_attached_compute:
        description:
          - >-
            Indicating whether the compute was provisioned by user and brought
            from outside if true, or machine learning service provisioned it if
            false.
        type: bool
  scale_settings:
    description:
      - Desired scale settings for the amlCompute.
    type: dict
    suboptions:
      max_node_count:
        description:
          - Max number of nodes to use
        required: true
        type: integer
      min_node_count:
        description:
          - Min number of nodes to use
        type: integer
      node_idle_time_before_scale_down:
        description:
          - Node Idle Time before scaling down amlCompute
        type: duration
  underlying_resource_action:
    description:
      - >-
        Delete the underlying compute if 'Delete', or detach the underlying
        compute from workspace if 'Detach'.
    type: str
    choices:
      - Delete
      - Detach
  state:
    description:
      - Assert the state of the MachineLearningCompute.
      - >-
        Use C(present) to create or update an MachineLearningCompute and
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
    - name: Create AKS Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        location: eastus
        properties:
          compute_type: AKS
        

    - name: Create a AML Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        identity:
          type: 'SystemAssigned,UserAssigned'
          user_assigned_identities:
            /subscriptions/00000000-0000-0000-0000-000000000000/resource_groups/my_resource_group/providers/microsoft.managed_identity/user_assigned_identities/identity-name: {}
        location: eastus
        properties:
          compute_type: AmlCompute
          properties:
            remote_login_port_public_access: NotSpecified
            scale_settings:
              max_node_count: 1
              min_node_count: 0
              node_idle_time_before_scale_down: PT5M
            vm_priority: Dedicated
            vm_size: STANDARD_NC6
        

    - name: Create a ComputeInstance Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        location: eastus
        properties:
          compute_type: ComputeInstance
          properties:
            application_sharing_policy: Personal
            ssh_settings:
              ssh_public_access: Disabled
            subnet: test-subnet-resource-id
            vm_size: STANDARD_NC6
        

    - name: Create a ComputeInstance Compute with minimal inputs
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        location: eastus
        properties:
          compute_type: ComputeInstance
          properties:
            vm_size: STANDARD_NC6
        

    - name: Create a DataFactory Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        location: eastus
        properties:
          compute_type: DataFactory
        

    - name: Update a AKS Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        location: eastus
        properties:
          description: some compute
          compute_type: AKS
          properties:
            agent_count: 4
          resource_id: >-
            /subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourcegroups/testrg123/providers/Microsoft.ContainerService/managedClusters/compute123-56826-c9b00420020b2
        

    - name: Update a AML Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        identity:
          type: 'SystemAssigned,UserAssigned'
          user_assigned_identities:
            /subscriptions/00000000-0000-0000-0000-000000000000/resource_groups/my_resource_group/providers/microsoft.managed_identity/user_assigned_identities/identity-name: {}
        location: eastus
        properties:
          compute_type: AmlCompute
          properties:
            scale_settings:
              max_node_count: 1
              min_node_count: 0
              node_idle_time_before_scale_down: PT5M
        

    - name: Update a AmlCompute Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        workspace_name: workspaces123
        properties:
          scale_settings:
            max_node_count: 4
            min_node_count: 4
            node_idle_time_before_scale_down: PT5M
        

    - name: Delete Compute
      azure_rm_machinelearningcompute: 
        compute_name: compute123
        resource_group_name: testrg123
        underlying_resource_action: Delete
        workspace_name: workspaces123
        

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
      The list of user identities associated with resource. The user identity
      dictionary key references will be ARM resource ids in the form:
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
          from outside if true, or machine learning service provisioned it if
          false.
      returned: always
      type: bool
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Machine Learning Workspaces
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMachineLearningCompute(AzureRMModuleBaseExt):
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
            compute_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    )
                )
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    compute_type=dict(
                        type='str',
                        disposition='compute_type',
                        choices=['AKS',
                                 'AmlCompute',
                                 'ComputeInstance',
                                 'DataFactory',
                                 'VirtualMachine',
                                 'HDInsight',
                                 'Databricks',
                                 'DataLakeAnalytics'],
                        required=True
                    ),
                    compute_location=dict(
                        type='str',
                        disposition='compute_location'
                    ),
                    provisioning_state=dict(
                        type='str',
                        updatable=False,
                        disposition='provisioning_state',
                        choices=['Unknown',
                                 'Updating',
                                 'Creating',
                                 'Deleting',
                                 'Succeeded',
                                 'Failed',
                                 'Canceled']
                    ),
                    description=dict(
                        type='str',
                        disposition='description'
                    ),
                    created_on=dict(
                        type='str',
                        updatable=False,
                        disposition='created_on'
                    ),
                    modified_on=dict(
                        type='str',
                        updatable=False,
                        disposition='modified_on'
                    ),
                    resource_id=dict(
                        type='str',
                        disposition='resource_id'
                    ),
                    provisioning_errors=dict(
                        type='list',
                        updatable=False,
                        disposition='provisioning_errors',
                        elements='dict',
                        options=dict(
                            error=dict(
                                type='dict',
                                updatable=False,
                                disposition='error',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='code'
                                    ),
                                    message=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='message'
                                    ),
                                    details=dict(
                                        type='list',
                                        updatable=False,
                                        disposition='details',
                                        elements='dict',
                                        options=dict(
                                            code=dict(
                                                type='str',
                                                disposition='code',
                                                required=True
                                            ),
                                            message=dict(
                                                type='str',
                                                disposition='message',
                                                required=True
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    is_attached_compute=dict(
                        type='bool',
                        updatable=False,
                        disposition='is_attached_compute'
                    )
                )
            ),
            scale_settings=dict(
                type='dict',
                disposition='/scale_settings',
                options=dict(
                    max_node_count=dict(
                        type='integer',
                        disposition='max_node_count',
                        required=True
                    ),
                    min_node_count=dict(
                        type='integer',
                        disposition='min_node_count'
                    ),
                    node_idle_time_before_scale_down=dict(
                        type='duration',
                        disposition='node_idle_time_before_scale_down'
                    )
                )
            ),
            underlying_resource_action=dict(
                type='str',
                choices=['Delete',
                         'Detach']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.compute_name = None
        self.underlying_resource_action = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMachineLearningCompute, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Machine Learning Workspaces,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.machine_learning_compute.create_or_update(resource_group_name=self.resource_group_name,
                                                                                  workspace_name=self.workspace_name,
                                                                                  compute_name=self.compute_name,
                                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MachineLearningCompute instance.')
            self.fail('Error creating the MachineLearningCompute instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.machine_learning_compute.delete(resource_group_name=self.resource_group_name,
                                                                        workspace_name=self.workspace_name,
                                                                        compute_name=self.compute_name,
                                                                        underlying_resource_action=self.underlying_resource_action)
        except CloudError as e:
            self.log('Error attempting to delete the MachineLearningCompute instance.')
            self.fail('Error deleting the MachineLearningCompute instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.machine_learning_compute.get(resource_group_name=self.resource_group_name,
                                                                     workspace_name=self.workspace_name,
                                                                     compute_name=self.compute_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMachineLearningCompute()


if __name__ == '__main__':
    main()
