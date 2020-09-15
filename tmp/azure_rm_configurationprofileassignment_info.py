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
module: azure_rm_configurationprofileassignment_info
version_added: '2.9'
short_description: Get ConfigurationProfileAssignment info.
description:
  - Get info of ConfigurationProfileAssignment.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  configuration_profile_assignment_name:
    description:
      - The configuration profile assignment name.
    type: str
  vm_name:
    description:
      - The name of the virtual machine.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a configuration profile assignment
      azure_rm_configurationprofileassignment_info: 
        configuration_profile_assignment_name: default
        resource_group_name: myResourceGroupName
        vm_name: myVMName
        

    - name: List configuration profile assignments
      azure_rm_configurationprofileassignment_info: 
        {}
        

'''

RETURN = '''
configuration_profile_assignments:
  description: >-
    A list of dict results where the key is the name of the
    ConfigurationProfileAssignment and the values are the facts for that
    ConfigurationProfileAssignment.
  returned: always
  type: complex
  contains:
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
    value:
      description:
        - Result of the list configuration profile assignment operation.
      returned: always
      type: list
      sample: null
      contains:
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
                    - >-
                      The state of compliance, which only appears in the
                      response.
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
    from azure.mgmt.automanage import AutomanageClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConfigurationProfileAssignmentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            configuration_profile_assignment_name=dict(
                type='str'
            ),
            vm_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.configuration_profile_assignment_name = None
        self.vm_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-30-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMConfigurationProfileAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AutomanageClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-30-preview')

        if (self.resource_group_name is not None and
            self.configuration_profile_assignment_name is not None and
            self.vm_name is not None):
            self.results['configuration_profile_assignments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['configuration_profile_assignments'] = self.format_item(self.list())
        else:
            self.results['configuration_profile_assignments'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.configuration_profile_assignments.get(resource_group_name=self.resource_group_name,
                                                                              configuration_profile_assignment_name=self.configuration_profile_assignment_name,
                                                                              vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.configuration_profile_assignments.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.configuration_profile_assignments.list_by_subscription()
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
    AzureRMConfigurationProfileAssignmentInfo()


if __name__ == '__main__':
    main()
