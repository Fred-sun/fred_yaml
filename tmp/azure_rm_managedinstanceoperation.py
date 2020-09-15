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
module: azure_rm_managedinstanceoperation
version_added: '2.9'
short_description: Manage Azure ManagedInstanceOperation instance.
description:
  - 'Create, update and delete instance of Azure ManagedInstanceOperation.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  operation_id:
    description:
      - undefined
    required: true
    type: uuid
  state:
    description:
      - Assert the state of the ManagedInstanceOperation.
      - >-
        Use C(present) to create or update an ManagedInstanceOperation and
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
managed_instance_name:
  description:
    - The name of the managed instance the operation is being performed on.
  returned: always
  type: str
  sample: null
operation:
  description:
    - The name of operation.
  returned: always
  type: str
  sample: null
operation_friendly_name:
  description:
    - The friendly name of operation.
  returned: always
  type: str
  sample: null
percent_complete:
  description:
    - The percentage of the operation completed.
  returned: always
  type: integer
  sample: null
start_time:
  description:
    - The operation start time.
  returned: always
  type: str
  sample: null
state:
  description:
    - The operation state.
  returned: always
  type: str
  sample: null
error_code:
  description:
    - The operation error code.
  returned: always
  type: integer
  sample: null
error_description:
  description:
    - The operation error description.
  returned: always
  type: str
  sample: null
error_severity:
  description:
    - The operation error severity.
  returned: always
  type: integer
  sample: null
is_user_error:
  description:
    - Whether or not the error is a user error.
  returned: always
  type: bool
  sample: null
estimated_completion_time:
  description:
    - The estimated completion time of the operation.
  returned: always
  type: str
  sample: null
description:
  description:
    - The operation description.
  returned: always
  type: str
  sample: null
is_cancellable:
  description:
    - Whether the operation can be cancelled.
  returned: always
  type: bool
  sample: null
operation_parameters:
  description:
    - The operation parameters.
  returned: always
  type: dict
  sample: null
  contains:
    current_parameters:
      description:
        - The current parameters.
      returned: always
      type: dict
      sample: null
      contains:
        family:
          description:
            - ''
          returned: always
          type: str
          sample: null
        tier:
          description:
            - ''
          returned: always
          type: str
          sample: null
        v_cores:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        storage_size_in_gb:
          description:
            - ''
          returned: always
          type: integer
          sample: null
    requested_parameters:
      description:
        - The requested parameters.
      returned: always
      type: dict
      sample: null
      contains:
        family:
          description:
            - ''
          returned: always
          type: str
          sample: null
        tier:
          description:
            - ''
          returned: always
          type: str
          sample: null
        v_cores:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        storage_size_in_gb:
          description:
            - ''
          returned: always
          type: integer
          sample: null
operation_steps:
  description:
    - The operation steps.
  returned: always
  type: dict
  sample: null
  contains:
    total_steps:
      description:
        - The total number of operation steps.
      returned: always
      type: str
      sample: null
    current_step:
      description:
        - The number of current operation steps.
      returned: always
      type: integer
      sample: null
    steps_list:
      description:
        - The operation steps list.
      returned: always
      type: list
      sample: null
      contains:
        order:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        name:
          description:
            - ''
          returned: always
          type: str
          sample: null
        status:
          description:
            - ''
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagedInstanceOperation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            operation_id=dict(
                type='uuid',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.operation_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedInstanceOperation, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.managed_instance_operations.create()
            else:
                response = self.mgmt_client.managed_instance_operations.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedInstanceOperation instance.')
            self.fail('Error creating the ManagedInstanceOperation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_instance_operations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ManagedInstanceOperation instance.')
            self.fail('Error deleting the ManagedInstanceOperation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_instance_operations.get(resource_group_name=self.resource_group_name,
                                                                        managed_instance_name=self.managed_instance_name,
                                                                        operation_id=self.operation_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedInstanceOperation()


if __name__ == '__main__':
    main()
