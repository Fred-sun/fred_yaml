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
module: azure_rm_environment_info
version_added: '2.9'
short_description: Get Environment info.
description:
  - Get info of Environment.
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
        'properties($expand=networkInterface)'
    required: true
    type: str
  filter:
    description:
      - The filter to apply to the operation.
    type: str
  top:
    description:
      - The maximum number of resources to return from the operation.
    type: integer
  orderby:
    description:
      - 'The ordering expression for the results, using OData notation.'
    type: str
  environment_name:
    description:
      - The name of the environment.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
environments:
  description: >-
    A list of dict results where the key is the name of the Environment and the
    values are the facts for that Environment.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              The name or email address of the user who has claimed the
              environment
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
    next_link:
      description:
        - Link for next set of results.
      returned: always
      type: str
      sample: null
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEnvironmentInfo(AzureRMModuleBase):
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
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            ),
            environment_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.lab_account_name = None
        self.lab_name = None
        self.environment_setting_name = None
        self.expand = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.environment_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-10-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEnvironmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-15')

        if (self.resource_group_name is not None and
            self.lab_account_name is not None and
            self.lab_name is not None and
            self.environment_setting_name is not None and
            self.environment_name is not None):
            self.results['environments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_account_name is not None and
              self.lab_name is not None and
              self.environment_setting_name is not None):
            self.results['environments'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.environments.get(resource_group_name=self.resource_group_name,
                                                         lab_account_name=self.lab_account_name,
                                                         lab_name=self.lab_name,
                                                         environment_setting_name=self.environment_setting_name,
                                                         environment_name=self.environment_name,
                                                         expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.environments.list(resource_group_name=self.resource_group_name,
                                                          lab_account_name=self.lab_account_name,
                                                          lab_name=self.lab_name,
                                                          environment_setting_name=self.environment_setting_name,
                                                          expand=self.expand,
                                                          filter=self.filter,
                                                          top=self.top,
                                                          orderby=self.orderby)
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
    AzureRMEnvironmentInfo()


if __name__ == '__main__':
    main()
