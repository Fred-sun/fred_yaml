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
module: azure_rm_applicationgroup
version_added: '2.9'
short_description: Manage Azure ApplicationGroup instance.
description:
  - 'Create, update and delete instance of Azure ApplicationGroup.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  application_group_name:
    description:
      - The name of the application group
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  description:
    description:
      - Description of ApplicationGroup.
    type: str
  friendly_name:
    description:
      - Friendly name of ApplicationGroup.
    type: str
  host_pool_arm_path:
    description:
      - HostPool arm path of ApplicationGroup.
    type: str
  application_group_type:
    description:
      - Resource Type of ApplicationGroup.
    type: str
    choices:
      - RemoteApp
      - Desktop
  state:
    description:
      - Assert the state of the ApplicationGroup.
      - >-
        Use C(present) to create or update an ApplicationGroup and C(absent) to
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
    - name: ApplicationGroup_Create
      azure_rm_applicationgroup: 
        application_group_name: applicationGroup1
        resource_group_name: resourceGroup1
        

    - name: ApplicationGroup_Delete
      azure_rm_applicationgroup: 
        application_group_name: applicationGroup1
        resource_group_name: resourceGroup1
        

    - name: ApplicationGroups_Update
      azure_rm_applicationgroup: 
        application_group_name: applicationGroup1
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
description:
  description:
    - Description of ApplicationGroup.
  returned: always
  type: str
  sample: null
friendly_name:
  description:
    - Friendly name of ApplicationGroup.
  returned: always
  type: str
  sample: null
host_pool_arm_path:
  description:
    - HostPool arm path of ApplicationGroup.
  returned: always
  type: str
  sample: null
workspace_arm_path:
  description:
    - Workspace arm path of ApplicationGroup.
  returned: always
  type: str
  sample: null
application_group_type:
  description:
    - Resource Type of ApplicationGroup.
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


class AzureRMApplicationGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            application_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            friendly_name=dict(
                type='str',
                disposition='/friendly_name'
            ),
            host_pool_arm_path=dict(
                type='str',
                disposition='/host_pool_arm_path'
            ),
            application_group_type=dict(
                type='str',
                disposition='/application_group_type',
                choices=['RemoteApp',
                         'Desktop']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.application_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplicationGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.application_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                            application_group_name=self.application_group_name,
                                                                            application_group=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ApplicationGroup instance.')
            self.fail('Error creating the ApplicationGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.application_groups.delete(resource_group_name=self.resource_group_name,
                                                                  application_group_name=self.application_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the ApplicationGroup instance.')
            self.fail('Error deleting the ApplicationGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.application_groups.get(resource_group_name=self.resource_group_name,
                                                               application_group_name=self.application_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApplicationGroup()


if __name__ == '__main__':
    main()
