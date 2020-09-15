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
module: azure_rm_role
version_added: '2.9'
short_description: Manage Azure Role instance.
description:
  - 'Create, update and delete instance of Azure Role.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  name:
    description:
      - The role name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  role:
    description:
      - The role properties.
    type: dict
    suboptions:
      kind:
        description:
          - Role type.
        required: true
        type: str
        choices:
          - IOT
          - ASA
          - Functions
          - Cognitive
  state:
    description:
      - Assert the state of the Role.
      - Use C(present) to create or update an Role and C(absent) to delete it.
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
    - name: RolePut
      azure_rm_role: 
        name: IoTRole1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        role:
          kind: IOT
          properties:
            host_platform: Linux
            io_tdevice_details:
              authentication:
                symmetric_key:
                  connection_string:
                    encryption_algorithm: AES256
                    encryption_cert_thumbprint: '348586569999244'
                    value: >-
                      Encrypted<<HostName=iothub.azure-devices.net;DeviceId=iotDevice;SharedAccessKey=2C750FscEas3JmQ8Bnui5yQWZPyml0/UiRt1bQwd8=>>
              device_id: iotdevice
              io_thost_hub: iothub.azure-devices.net
            io_tedge_device_details:
              authentication:
                symmetric_key:
                  connection_string:
                    encryption_algorithm: AES256
                    encryption_cert_thumbprint: '1245475856069999244'
                    value: >-
                      Encrypted<<HostName=iothub.azure-devices.net;DeviceId=iotEdge;SharedAccessKey=2C750FscEas3JmQ8Bnui5yQWZPyml0/UiRt1bQwd8=>>
              device_id: iotEdge
              io_thost_hub: iothub.azure-devices.net
            role_status: Enabled
            share_mappings: []
        

    - name: RoleDelete
      azure_rm_role: 
        name: IoTRole1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The object name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
kind:
  description:
    - Role type.
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
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRole(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            role=dict(
                type='dict',
                disposition='/role',
                options=dict(
                    kind=dict(
                        type='str',
                        disposition='kind',
                        choices=['IOT',
                                 'ASA',
                                 'Functions',
                                 'Cognitive'],
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRole, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

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
            response = self.mgmt_client.roles.create_or_update(device_name=self.device_name,
                                                               name=self.name,
                                                               resource_group_name=self.resource_group_name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Role instance.')
            self.fail('Error creating the Role instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.roles.delete(device_name=self.device_name,
                                                     name=self.name,
                                                     resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Role instance.')
            self.fail('Error deleting the Role instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.roles.get(device_name=self.device_name,
                                                  name=self.name,
                                                  resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRole()


if __name__ == '__main__':
    main()
