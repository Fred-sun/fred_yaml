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
module: azure_rm_environmentsetting
version_added: '2.9'
short_description: Manage Azure EnvironmentSetting instance.
description:
  - 'Create, update and delete instance of Azure EnvironmentSetting.'
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
  expand:
    description:
      - >-
        Specify the $expand query. Example:
        'properties($select=publishingState)'
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  configuration_state:
    description:
      - Describes the user's progress in configuring their environment setting
    type: str
    choices:
      - NotApplicable
      - Completed
  description:
    description:
      - Describes the environment and its resource settings
    type: str
  title:
    description:
      - Brief title describing the environment and its resource settings
    type: str
  provisioning_state:
    description:
      - The provisioning status of the resource.
    type: str
  unique_identifier:
    description:
      - The unique immutable identifier of a resource (Guid).
    type: str
  gallery_image_resource_id:
    description:
      - >-
        The resource id of the gallery image used for creating the virtual
        machine
    type: str
  size:
    description:
      - The size of the virtual machine
    type: str
    choices:
      - Basic
      - Standard
      - Performance
  reference_vm:
    description:
      - Details specific to Reference Vm
    type: dict
    suboptions:
      user_name:
        description:
          - The username of the virtual machine
        required: true
        type: str
      password:
        description:
          - >-
            The password of the virtual machine. This will be set to null in GET
            resource API
        type: str
      vm_state_details:
        description:
          - The state details for the reference virtual machine.
        type: dict
        suboptions:
          rdp_authority:
            description:
              - >-
                The RdpAuthority property is a server DNS host name or IP
                address followed by the service port number for RDP (Remote
                Desktop Protocol).
            type: str
          ssh_authority:
            description:
              - >-
                The SshAuthority property is a server DNS host name or IP
                address followed by the service port number for SSH.
            type: str
          power_state:
            description:
              - The power state of the reference virtual machine.
            type: str
          last_known_power_state:
            description:
              - Last known compute power state captured in DTL
            type: str
      vm_resource_id:
        description:
          - VM resource Id for the environment
        type: str
  state:
    description:
      - Assert the state of the EnvironmentSetting.
      - >-
        Use C(present) to create or update an EnvironmentSetting and C(absent)
        to delete it.
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
publishing_state:
  description:
    - Describes the readiness of this environment setting
  returned: always
  type: str
  sample: null
configuration_state:
  description:
    - Describes the user's progress in configuring their environment setting
  returned: always
  type: str
  sample: null
description:
  description:
    - Describes the environment and its resource settings
  returned: always
  type: str
  sample: null
title:
  description:
    - Brief title describing the environment and its resource settings
  returned: always
  type: str
  sample: null
last_changed:
  description:
    - Time when the template VM was last changed.
  returned: always
  type: str
  sample: null
last_published:
  description:
    - Time when the template VM was last sent for publishing.
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
id_properties_resource_settings_id:
  description:
    - The unique id of the resource setting
  returned: always
  type: str
  sample: null
gallery_image_resource_id:
  description:
    - The resource id of the gallery image used for creating the virtual machine
  returned: always
  type: str
  sample: null
image_name:
  description:
    - The name of the image used to created the environment setting
  returned: always
  type: str
  sample: null
size:
  description:
    - The size of the virtual machine
  returned: always
  type: str
  sample: null
cores:
  description:
    - The translated compute cores of the virtual machine
  returned: always
  type: integer
  sample: null
reference_vm:
  description:
    - Details specific to Reference Vm
  returned: always
  type: dict
  sample: null
  contains:
    user_name:
      description:
        - The username of the virtual machine
      returned: always
      type: str
      sample: null
    password:
      description:
        - >-
          The password of the virtual machine. This will be set to null in GET
          resource API
      returned: always
      type: str
      sample: null
    vm_state_details:
      description:
        - The state details for the reference virtual machine.
      returned: always
      type: dict
      sample: null
      contains:
        rdp_authority:
          description:
            - >-
              The RdpAuthority property is a server DNS host name or IP address
              followed by the service port number for RDP (Remote Desktop
              Protocol).
          returned: always
          type: str
          sample: null
        ssh_authority:
          description:
            - >-
              The SshAuthority property is a server DNS host name or IP address
              followed by the service port number for SSH.
          returned: always
          type: str
          sample: null
        power_state:
          description:
            - The power state of the reference virtual machine.
          returned: always
          type: str
          sample: null
        last_known_power_state:
          description:
            - Last known compute power state captured in DTL
          returned: always
          type: str
          sample: null
    vm_resource_id:
      description:
        - VM resource Id for the environment
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


class AzureRMEnvironmentSetting(AzureRMModuleBaseExt):
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
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            configuration_state=dict(
                type='str',
                disposition='/configuration_state',
                choices=['NotApplicable',
                         'Completed']
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            title=dict(
                type='str',
                disposition='/title'
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state'
            ),
            unique_identifier=dict(
                type='str',
                disposition='/unique_identifier'
            ),
            gallery_image_resource_id=dict(
                type='str',
                disposition='/gallery_image_resource_id'
            ),
            size=dict(
                type='str',
                disposition='/size',
                choices=['Basic',
                         'Standard',
                         'Performance']
            ),
            reference_vm=dict(
                type='dict',
                disposition='/reference_vm',
                options=dict(
                    user_name=dict(
                        type='str',
                        disposition='user_name',
                        required=True
                    ),
                    password=dict(
                        type='str',
                        disposition='password'
                    ),
                    vm_state_details=dict(
                        type='dict',
                        updatable=False,
                        disposition='vm_state_details',
                        options=dict(
                            rdp_authority=dict(
                                type='str',
                                updatable=False,
                                disposition='rdp_authority'
                            ),
                            ssh_authority=dict(
                                type='str',
                                updatable=False,
                                disposition='ssh_authority'
                            ),
                            power_state=dict(
                                type='str',
                                updatable=False,
                                disposition='power_state'
                            ),
                            last_known_power_state=dict(
                                type='str',
                                updatable=False,
                                disposition='last_known_power_state'
                            )
                        )
                    ),
                    vm_resource_id=dict(
                        type='str',
                        updatable=False,
                        disposition='vm_resource_id'
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
        self.lab_account_name = None
        self.lab_name = None
        self.environment_setting_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEnvironmentSetting, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.environment_settings.create_or_update(resource_group_name=self.resource_group_name,
                                                                              lab_account_name=self.lab_account_name,
                                                                              lab_name=self.lab_name,
                                                                              environment_setting_name=self.environment_setting_name,
                                                                              environment_setting=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the EnvironmentSetting instance.')
            self.fail('Error creating the EnvironmentSetting instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.environment_settings.delete(resource_group_name=self.resource_group_name,
                                                                    lab_account_name=self.lab_account_name,
                                                                    lab_name=self.lab_name,
                                                                    environment_setting_name=self.environment_setting_name)
        except CloudError as e:
            self.log('Error attempting to delete the EnvironmentSetting instance.')
            self.fail('Error deleting the EnvironmentSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.environment_settings.get(resource_group_name=self.resource_group_name,
                                                                 lab_account_name=self.lab_account_name,
                                                                 lab_name=self.lab_name,
                                                                 environment_setting_name=self.environment_setting_name,
                                                                 expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEnvironmentSetting()


if __name__ == '__main__':
    main()
