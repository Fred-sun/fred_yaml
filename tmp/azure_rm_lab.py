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
module: azure_rm_lab
version_added: '2.9'
short_description: Manage Azure Lab instance.
description:
  - 'Create, update and delete instance of Azure Lab.'
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
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=maxUsersInLab)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  max_users_in_lab:
    description:
      - Maximum number of users allowed in the lab.
    type: integer
  usage_quota:
    description:
      - Maximum duration a user can use an environment for in the lab.
    type: duration
  user_access_mode:
    description:
      - >-
        Lab user access mode (open to all vs. restricted to those listed on the
        lab).
    type: str
    choices:
      - Restricted
      - Open
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
      - Assert the state of the Lab.
      - Use C(present) to create or update an Lab and C(absent) to delete it.
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
max_users_in_lab:
  description:
    - Maximum number of users allowed in the lab.
  returned: always
  type: integer
  sample: null
user_quota:
  description:
    - 'Maximum value MaxUsersInLab can be set to, as specified by the service'
  returned: always
  type: integer
  sample: null
invitation_code:
  description:
    - Invitation code that users can use to join a lab.
  returned: always
  type: str
  sample: null
created_by_object_id:
  description:
    - Object id of the user that created the lab.
  returned: always
  type: str
  sample: null
usage_quota:
  description:
    - Maximum duration a user can use an environment for in the lab.
  returned: always
  type: duration
  sample: null
user_access_mode:
  description:
    - >-
      Lab user access mode (open to all vs. restricted to those listed on the
      lab).
  returned: always
  type: str
  sample: null
created_by_user_principal_name:
  description:
    - Lab creator name
  returned: always
  type: str
  sample: null
created_date:
  description:
    - Creation date for the lab
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


class AzureRMLab(AzureRMModuleBaseExt):
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
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            max_users_in_lab=dict(
                type='integer',
                disposition='/max_users_in_lab'
            ),
            usage_quota=dict(
                type='duration',
                disposition='/usage_quota'
            ),
            user_access_mode=dict(
                type='str',
                disposition='/user_access_mode',
                choices=['Restricted',
                         'Open']
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
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLab, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.labs.create_or_update(resource_group_name=self.resource_group_name,
                                                              lab_account_name=self.lab_account_name,
                                                              lab_name=self.lab_name,
                                                              lab=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Lab instance.')
            self.fail('Error creating the Lab instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.labs.delete(resource_group_name=self.resource_group_name,
                                                    lab_account_name=self.lab_account_name,
                                                    lab_name=self.lab_name)
        except CloudError as e:
            self.log('Error attempting to delete the Lab instance.')
            self.fail('Error deleting the Lab instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.labs.get(resource_group_name=self.resource_group_name,
                                                 lab_account_name=self.lab_account_name,
                                                 lab_name=self.lab_name,
                                                 expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLab()


if __name__ == '__main__':
    main()
