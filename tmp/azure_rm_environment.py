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
module: azure_rm_environment
version_added: '2.9'
short_description: Manage Azure Environment instance.
description:
  - 'Create, update and delete instance of Azure Environment.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_account_name:
    description:
      - The name of the lab Account.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  environment_setting_name:
    description:
      - The name of the environment Setting.
    required: true
    type: str
  environment_name:
    description:
      - The name of the environment.
    required: true
    type: str
  expand:
    description:
      - >-
        Specify the $expand query. Example:
        'properties($expand=networkInterface)'
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  resource_sets:
    description:
      - The set of a VM and the setting id it was created for
    type: dict
    suboptions:
      vm_resource_id:
        description:
          - VM resource Id for the environment
        type: str
      resource_setting_id:
        description:
          - resourceSettingId for the environment
        type: str
  provisioning_state:
    description:
      - The provisioning status of the resource.
    type: str
  unique_identifier:
    description:
      - The unique immutable identifier of a resource (Guid).
    type: str
  state:
    description:
      - Assert the state of the Environment.
      - >-
        Use C(present) to create or update an Environment and C(absent) to
        delete it.
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
'''

RETURN = '''
id:
  description:
    - The identifier of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
resource_sets:
  description:
    - The set of a VM and the setting id it was created for
  returned: always
  type: dict
  sample: null
  contains:
    vm_resource_id:
      description:
        - VM resource Id for the environment
      returned: always
      type: str
      sample: null
    resource_setting_id:
      description:
        - resourceSettingId for the environment
      returned: always
      type: str
      sample: null
claimed_by_user_object_id:
  description:
    - The AAD object Id of the user who has claimed the environment
  returned: always
  type: str
  sample: null
claimed_by_user_principal_id:
  description:
    - The user principal Id of the user who has claimed the environment
  returned: always
  type: str
  sample: null
claimed_by_user_name:
  description:
    - The name or email address of the user who has claimed the environment
  returned: always
  type: str
  sample: null
is_claimed:
  description:
    - Is the environment claimed or not
  returned: always
  type: bool
  sample: null
last_known_power_state:
  description:
    - Last known power state of the environment
  returned: always
  type: str
  sample: null
network_interface:
  description:
    - Network details of the environment
  returned: always
  type: dict
  sample: null
  contains:
    private_ip_address:
      description:
        - PrivateIp address of the Compute VM
      returned: always
      type: str
      sample: null
    ssh_authority:
      description:
        - Connection information for Linux
      returned: always
      type: str
      sample: null
    rdp_authority:
      description:
        - Connection information for Windows
      returned: always
      type: str
      sample: null
    username:
      description:
        - Username of the VM
      returned: always
      type: str
      sample: null
total_usage:
  description:
    - How long the environment has been used by a lab user
  returned: always
  type: duration
  sample: null
password_last_reset:
  description:
    - When the password was last reset on the environment.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning status of the resource.
  returned: always
  type: str
  sample: null
unique_identifier:
  description:
    - The unique immutable identifier of a resource (Guid).
  returned: always
  type: str
  sample: null
latest_operation_result:
  description:
    - 'The details of the latest operation. ex: status, error'
  returned: always
  type: dict
  sample: null
  contains:
    status:
      description:
        - The current status of the operation.
      returned: always
      type: str
      sample: null
    error_code:
      description:
        - Error code on failure.
      returned: always
      type: str
      sample: null
    error_message:
      description:
        - The error message.
      returned: always
      type: str
      sample: null
    request_uri:
      description:
        - Request URI of the operation.
      returned: always
      type: str
      sample: null
    http_method:
      description:
        - The HttpMethod - PUT/POST/DELETE for the operation.
      returned: always
      type: str
      sample: null
    operation_url:
      description:
        - The URL to use to check long-running operation status
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
    from azure.mgmt.managed import ManagedLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMEnvironment(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_account_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            environment_setting_name=dict(
                type='str',
                required=True
            ),
            environment_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            resource_sets=dict(
                type='dict',
                disposition='/resource_sets',
                options=dict(
                    vm_resource_id=dict(
                        type='str',
                        disposition='vm_resource_id'
                    ),
                    resource_setting_id=dict(
                        type='str',
                        disposition='resource_setting_id'
                    )
                )
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state'
            ),
            unique_identifier=dict(
                type='str',
                disposition='/unique_identifier'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_account_name = None
        self.lab_name = None
        self.environment_setting_name = None
        self.environment_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEnvironment, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ManagedLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-15')

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
            response = self.mgmt_client.environments.create_or_update(resource_group_name=self.resource_group_name,
                                                                      lab_account_name=self.lab_account_name,
                                                                      lab_name=self.lab_name,
                                                                      environment_setting_name=self.environment_setting_name,
                                                                      environment_name=self.environment_name,
                                                                      environment=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Environment instance.')
            self.fail('Error creating the Environment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.environments.delete(resource_group_name=self.resource_group_name,
                                                            lab_account_name=self.lab_account_name,
                                                            lab_name=self.lab_name,
                                                            environment_setting_name=self.environment_setting_name,
                                                            environment_name=self.environment_name)
        except CloudError as e:
            self.log('Error attempting to delete the Environment instance.')
            self.fail('Error deleting the Environment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.environments.get(resource_group_name=self.resource_group_name,
                                                         lab_account_name=self.lab_account_name,
                                                         lab_name=self.lab_name,
                                                         environment_setting_name=self.environment_setting_name,
                                                         environment_name=self.environment_name,
                                                         expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEnvironment()


if __name__ == '__main__':
    main()
