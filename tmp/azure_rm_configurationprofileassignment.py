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
module: azure_rm_configurationprofileassignment
version_added: '2.9'
short_description: Manage Azure ConfigurationProfileAssignment instance.
description:
  - 'Create, update and delete instance of Azure ConfigurationProfileAssignment.'
options:
  configuration_profile_assignment_name:
    description:
      - Name of the configuration profile assignment. Only default is supported.
      - The configuration profile assignment name.
    required: true
    type: str
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  vm_name:
    description:
      - The name of the virtual machine.
    required: true
    type: str
  properties:
    description:
      - Properties of the configuration profile assignment.
    type: dict
    suboptions:
      configuration_profile:
        description:
          - A value indicating configuration profile.
        type: str
        choices:
          - Azure virtual machine best practices – Dev/Test
          - Azure virtual machine best practices – Production
      target_id:
        description:
          - The target VM resource URI
        type: str
      account_id:
        description:
          - The Automanage account ARM Resource URI
        type: str
      configuration_profile_preference_id:
        description:
          - The configuration profile custom preferences ARM resource URI
        type: str
      provisioning_status:
        description:
          - 'The state of onboarding, which only appears in the response.'
        type: str
        choices:
          - Succeeded
          - Failed
          - Created
      compliance:
        description:
          - The configuration setting for the configuration profile.
        type: dict
        suboptions:
          update_status:
            description:
              - 'The state of compliance, which only appears in the response.'
            type: str
            choices:
              - Succeeded
              - Failed
              - Created
  state:
    description:
      - Assert the state of the ConfigurationProfileAssignment.
      - >-
        Use C(present) to create or update an ConfigurationProfileAssignment and
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
    - name: Create or update configuration profile assignment
      azure_rm_configurationprofileassignment: 
        configuration_profile_assignment_name: default
        resource_group_name: myResourceGroupName
        vm_name: myVMName
        properties:
          account_id: >-
            /subscriptions/subid/resourceGroups/rg/providers/Microsoft.Automanage/accounts/AutomanageAccount
          configuration_profile: Azure Best Practices - Prod
          configuration_profile_preference_id: >-
            /subscriptions/subscriptionId/resourceGroups/myResourceGroupName/providers/Microsoft.Automanage/configurationProfilePreferences/defaultProfilePreference
        

    - name: Delete an configuration profile assignment
      azure_rm_configurationprofileassignment: 
        configuration_profile_assignment_name: default
        resource_group_name: myResourceGroupName
        vm_name: myVMName
        

'''

RETURN = '''
id:
  description:
    - >-
      Fully qualified resource Id for the resource. Ex -
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource. Ex- Microsoft.Compute/virtualMachines or
      Microsoft.Storage/storageAccounts.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties of the configuration profile assignment.
  returned: always
  type: dict
  sample: null
  contains:
    configuration_profile:
      description:
        - A value indicating configuration profile.
      returned: always
      type: str
      sample: null
    target_id:
      description:
        - The target VM resource URI
      returned: always
      type: str
      sample: null
    account_id:
      description:
        - The Automanage account ARM Resource URI
      returned: always
      type: str
      sample: null
    configuration_profile_preference_id:
      description:
        - The configuration profile custom preferences ARM resource URI
      returned: always
      type: str
      sample: null
    provisioning_status:
      description:
        - 'The state of onboarding, which only appears in the response.'
      returned: always
      type: str
      sample: null
    compliance:
      description:
        - The configuration setting for the configuration profile.
      returned: always
      type: dict
      sample: null
      contains:
        update_status:
          description:
            - 'The state of compliance, which only appears in the response.'
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
    from azure.mgmt.automanage import AutomanageClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConfigurationProfileAssignment(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            configuration_profile_assignment_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vm_name=dict(
                type='str',
                required=True
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    configuration_profile=dict(
                        type='str',
                        disposition='configuration_profile',
                        choices=['Azure virtual machine best practices – Dev/Test',
                                 'Azure virtual machine best practices – Production']
                    ),
                    target_id=dict(
                        type='str',
                        disposition='target_id'
                    ),
                    account_id=dict(
                        type='str',
                        disposition='account_id'
                    ),
                    configuration_profile_preference_id=dict(
                        type='str',
                        disposition='configuration_profile_preference_id'
                    ),
                    provisioning_status=dict(
                        type='str',
                        updatable=False,
                        disposition='provisioning_status',
                        choices=['Succeeded',
                                 'Failed',
                                 'Created']
                    ),
                    compliance=dict(
                        type='dict',
                        disposition='compliance',
                        options=dict(
                            update_status=dict(
                                type='str',
                                updatable=False,
                                disposition='update_status',
                                choices=['Succeeded',
                                         'Failed',
                                         'Created']
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

        self.configuration_profile_assignment_name = None
        self.resource_group_name = None
        self.vm_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConfigurationProfileAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AutomanageClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-30-preview')

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
            response = self.mgmt_client.configuration_profile_assignments.create_or_update(configuration_profile_assignment_name=self.configuration_profile_assignment_name,
                                                                                           resource_group_name=self.resource_group_name,
                                                                                           vm_name=self.vm_name,
                                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ConfigurationProfileAssignment instance.')
            self.fail('Error creating the ConfigurationProfileAssignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.configuration_profile_assignments.delete(resource_group_name=self.resource_group_name,
                                                                                 configuration_profile_assignment_name=self.configuration_profile_assignment_name,
                                                                                 vm_name=self.vm_name)
        except CloudError as e:
            self.log('Error attempting to delete the ConfigurationProfileAssignment instance.')
            self.fail('Error deleting the ConfigurationProfileAssignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.configuration_profile_assignments.get(resource_group_name=self.resource_group_name,
                                                                              configuration_profile_assignment_name=self.configuration_profile_assignment_name,
                                                                              vm_name=self.vm_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMConfigurationProfileAssignment()


if __name__ == '__main__':
    main()
