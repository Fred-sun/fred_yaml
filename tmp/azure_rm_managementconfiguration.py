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
module: azure_rm_managementconfiguration
version_added: '2.9'
short_description: Manage Azure ManagementConfiguration instance.
description:
  - 'Create, update and delete instance of Azure ManagementConfiguration.'
options:
  resource_group_name:
    description:
      - The name of the resource group to get. The name is case insensitive.
    required: true
    type: str
  management_configuration_name:
    description:
      - User Management Configuration Name.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  application_id:
    description:
      - The applicationId of the appliance for this Management.
    type: str
  parent_resource_type:
    description:
      - The type of the parent resource.
    type: str
  parameters:
    description:
      - Parameters to run the ARM template
    type: list
    suboptions:
      name:
        description:
          - name of the parameter.
        type: str
      value:
        description:
          - 'value for the parameter. In Jtoken '
        type: str
  template:
    description:
      - The Json object containing the ARM template to deploy
    type: any
  state:
    description:
      - Assert the state of the ManagementConfiguration.
      - >-
        Use C(present) to create or update an ManagementConfiguration and
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
    - name: ManagementConfigurationCreate
      azure_rm_managementconfiguration: 
        management_configuration_name: managementConfiguration1
        parameters:
          location: East US
        resource_group_name: rg1
        location: East US
        

    - name: ManagementConfigurationDelete
      azure_rm_managementconfiguration: 
        management_configuration_name: managementConfigurationName
        resource_group_name: rg1
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
application_id:
  description:
    - The applicationId of the appliance for this Management.
  returned: always
  type: str
  sample: null
parent_resource_type:
  description:
    - The type of the parent resource.
  returned: always
  type: str
  sample: null
parameters:
  description:
    - Parameters to run the ARM template
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - name of the parameter.
      returned: always
      type: str
      sample: null
    value:
      description:
        - 'value for the parameter. In Jtoken '
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - The provisioning state for the ManagementConfiguration.
  returned: always
  type: str
  sample: null
template:
  description:
    - The Json object containing the ARM template to deploy
  returned: always
  type: any
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.operations import OperationsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagementConfiguration(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            management_configuration_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            application_id=dict(
                type='str',
                disposition='/application_id'
            ),
            parent_resource_type=dict(
                type='str',
                disposition='/parent_resource_type'
            ),
            parameters=dict(
                type='list',
                disposition='/parameters',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    value=dict(
                        type='str',
                        disposition='value'
                    )
                )
            ),
            template=dict(
                type='any',
                disposition='/template'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.management_configuration_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagementConfiguration, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(OperationsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-11-01-preview')

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
            response = self.mgmt_client.management_configurations.create_or_update(resource_group_name=self.resource_group_name,
                                                                                   management_configuration_name=self.management_configuration_name,
                                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagementConfiguration instance.')
            self.fail('Error creating the ManagementConfiguration instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.management_configurations.delete(resource_group_name=self.resource_group_name,
                                                                         management_configuration_name=self.management_configuration_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagementConfiguration instance.')
            self.fail('Error deleting the ManagementConfiguration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.management_configurations.get(resource_group_name=self.resource_group_name,
                                                                      management_configuration_name=self.management_configuration_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagementConfiguration()


if __name__ == '__main__':
    main()
