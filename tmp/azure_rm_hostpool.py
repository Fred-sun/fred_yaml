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
module: azure_rm_hostpool
version_added: '2.9'
short_description: Manage Azure HostPool instance.
description:
  - 'Create, update and delete instance of Azure HostPool.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  host_pool_name:
    description:
      - The name of the host pool within the specified resource group
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  friendly_name:
    description:
      - Friendly name of HostPool.
    type: str
  description:
    description:
      - Description of HostPool.
    type: str
  host_pool_type:
    description:
      - HostPool type for desktop.
    type: str
    choices:
      - Personal
      - Pooled
  personal_desktop_assignment_type:
    description:
      - PersonalDesktopAssignment type for HostPool.
    type: str
    choices:
      - Automatic
      - Direct
  custom_rdp_property:
    description:
      - Custom rdp property of HostPool.
    type: str
  max_session_limit:
    description:
      - The max session limit of HostPool.
    type: integer
  load_balancer_type:
    description:
      - The type of the load balancer.
    type: str
    choices:
      - BreadthFirst
      - DepthFirst
      - Persistent
  ring:
    description:
      - The ring number of HostPool.
    type: integer
  validation_environment:
    description:
      - Is validation environment.
    type: bool
  registration_info:
    description:
      - The registration info of HostPool.
    type: dict
    suboptions:
      expiration_time:
        description:
          - Expiration time of registration token.
        type: str
      token:
        description:
          - The registration token base64 encoded string.
        type: str
      registration_token_operation:
        description:
          - The type of resetting the token.
        type: str
        choices:
          - Delete
          - None
          - Update
  vm_template:
    description:
      - VM template for sessionhosts configuration within hostpool.
    type: str
  sso_context:
    description:
      - Path to keyvault containing ssoContext secret.
    type: str
  preferred_app_group_type:
    description:
      - >-
        The type of preferred application group type, default to Desktop
        Application Group
    type: str
    choices:
      - None
      - Desktop
      - RailApplications
  force:
    description:
      - Force flag to delete sessionHost.
    type: bool
  state:
    description:
      - Assert the state of the HostPool.
      - >-
        Use C(present) to create or update an HostPool and C(absent) to delete
        it.
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
    - name: HostPool_Create
      azure_rm_hostpool: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        

    - name: HostPool_Delete
      azure_rm_hostpool: 
        force: true
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        

    - name: HostPool_Update
      azure_rm_hostpool: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
friendly_name:
  description:
    - Friendly name of HostPool.
  returned: always
  type: str
  sample: null
description:
  description:
    - Description of HostPool.
  returned: always
  type: str
  sample: null
host_pool_type:
  description:
    - HostPool type for desktop.
  returned: always
  type: str
  sample: null
personal_desktop_assignment_type:
  description:
    - PersonalDesktopAssignment type for HostPool.
  returned: always
  type: str
  sample: null
custom_rdp_property:
  description:
    - Custom rdp property of HostPool.
  returned: always
  type: str
  sample: null
max_session_limit:
  description:
    - The max session limit of HostPool.
  returned: always
  type: integer
  sample: null
load_balancer_type:
  description:
    - The type of the load balancer.
  returned: always
  type: str
  sample: null
ring:
  description:
    - The ring number of HostPool.
  returned: always
  type: integer
  sample: null
validation_environment:
  description:
    - Is validation environment.
  returned: always
  type: bool
  sample: null
registration_info:
  description:
    - The registration info of HostPool.
  returned: always
  type: dict
  sample: null
  contains:
    expiration_time:
      description:
        - Expiration time of registration token.
      returned: always
      type: str
      sample: null
    token:
      description:
        - The registration token base64 encoded string.
      returned: always
      type: str
      sample: null
    registration_token_operation:
      description:
        - The type of resetting the token.
      returned: always
      type: str
      sample: null
vm_template:
  description:
    - VM template for sessionhosts configuration within hostpool.
  returned: always
  type: str
  sample: null
application_group_references:
  description:
    - List of applicationGroup links.
  returned: always
  type: list
  sample: null
sso_context:
  description:
    - Path to keyvault containing ssoContext secret.
  returned: always
  type: str
  sample: null
preferred_app_group_type:
  description:
    - >-
      The type of preferred application group type, default to Desktop
      Application Group
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
    from azure.mgmt.desktop import Desktop Virtualization API Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMHostPool(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            host_pool_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            friendly_name=dict(
                type='str',
                disposition='/friendly_name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            host_pool_type=dict(
                type='str',
                disposition='/host_pool_type',
                choices=['Personal',
                         'Pooled']
            ),
            personal_desktop_assignment_type=dict(
                type='str',
                disposition='/personal_desktop_assignment_type',
                choices=['Automatic',
                         'Direct']
            ),
            custom_rdp_property=dict(
                type='str',
                disposition='/custom_rdp_property'
            ),
            max_session_limit=dict(
                type='integer',
                disposition='/max_session_limit'
            ),
            load_balancer_type=dict(
                type='str',
                disposition='/load_balancer_type',
                choices=['BreadthFirst',
                         'DepthFirst',
                         'Persistent']
            ),
            ring=dict(
                type='integer',
                disposition='/ring'
            ),
            validation_environment=dict(
                type='bool',
                disposition='/validation_environment'
            ),
            registration_info=dict(
                type='dict',
                disposition='/registration_info',
                options=dict(
                    expiration_time=dict(
                        type='str',
                        disposition='expiration_time'
                    ),
                    token=dict(
                        type='str',
                        disposition='token'
                    ),
                    registration_token_operation=dict(
                        type='str',
                        disposition='registration_token_operation',
                        choices=['Delete',
                                 'None',
                                 'Update']
                    )
                )
            ),
            vm_template=dict(
                type='str',
                disposition='/vm_template'
            ),
            sso_context=dict(
                type='str',
                disposition='/sso_context'
            ),
            preferred_app_group_type=dict(
                type='str',
                disposition='/preferred_app_group_type',
                choices=['None',
                         'Desktop',
                         'RailApplications']
            ),
            force=dict(
                type='bool'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.host_pool_name = None
        self.force = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMHostPool, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

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
            response = self.mgmt_client.host_pools.create_or_update(resource_group_name=self.resource_group_name,
                                                                    host_pool_name=self.host_pool_name,
                                                                    host_pool=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the HostPool instance.')
            self.fail('Error creating the HostPool instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.host_pools.delete(resource_group_name=self.resource_group_name,
                                                          host_pool_name=self.host_pool_name,
                                                          force=self.force)
        except CloudError as e:
            self.log('Error attempting to delete the HostPool instance.')
            self.fail('Error deleting the HostPool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.host_pools.get(resource_group_name=self.resource_group_name,
                                                       host_pool_name=self.host_pool_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMHostPool()


if __name__ == '__main__':
    main()
