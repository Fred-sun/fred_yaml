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
module: azure_rm_managedinstanceoperation_info
version_added: '2.9'
short_description: Get ManagedInstanceOperation info.
description:
  - Get info of ManagedInstanceOperation.
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
    type: uuid
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List the managed instance management operations
      azure_rm_managedinstanceoperation_info: 
        managed_instance_name: sqlcrudtest-4645
        resource_group_name: sqlcrudtest-7398
        

    - name: Gets the managed instance management operation
      azure_rm_managedinstanceoperation_info: 
        operation_id: 00000000-1111-2222-3333-444444444444
        managed_instance_name: sqlcrudtest-4645
        resource_group_name: sqlcrudtest-7398
        

'''

RETURN = '''
managed_instance_operations:
  description: >-
    A list of dict results where the key is the name of the
    ManagedInstanceOperation and the values are the facts for that
    ManagedInstanceOperation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        managed_instance_name:
          description:
            - >-
              The name of the managed instance the operation is being performed
              on.
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
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagedInstanceOperationInfo(AzureRMModuleBase):
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
                type='uuid'
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.operation_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedInstanceOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.operation_id is not None):
            self.results['managed_instance_operations'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['managed_instance_operations'] = self.format_item(self.listbymanagedinstance())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_operations.get(resource_group_name=self.resource_group_name,
                                                                        managed_instance_name=self.managed_instance_name,
                                                                        operation_id=self.operation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanagedinstance(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_operations.list_by_managed_instance(resource_group_name=self.resource_group_name,
                                                                                             managed_instance_name=self.managed_instance_name)
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
    AzureRMManagedInstanceOperationInfo()


if __name__ == '__main__':
    main()
