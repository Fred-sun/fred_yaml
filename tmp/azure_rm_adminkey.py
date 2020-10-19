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
module: azure_rm_adminkey
version_added: '2.9'
short_description: Manage Azure AdminKey instance.
description:
  - 'Create, update and delete instance of Azure AdminKey.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the current subscription. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  search_service_name:
    description:
      - >-
        The name of the Azure Cognitive Search service associated with the
        specified resource group.
    required: true
    type: str
  clientrequestid:
    description:
      - >-
        A client-generated GUID value that identifies this request. If
        specified, this will be included in response information as a way to
        track the request.
    required: true
    type: uuid
  search_management_request_options:
    description:
      - Parameter group
    required: true
    type: group
    suboptions:
      client_request_id:
        description:
          - >-
            A client-generated GUID value that identifies this request. If
            specified, this will be included in response information as a way to
            track the request.
        type: uuid
  state:
    description:
      - Assert the state of the AdminKey.
      - >-
        Use C(present) to create or update an AdminKey and C(absent) to delete
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
'''

RETURN = '''
primary_key:
  description:
    - The primary admin API key of the search service.
  returned: always
  type: str
  sample: null
secondary_key:
  description:
    - The secondary admin API key of the search service.
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
    from azure.mgmt.search import SearchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAdminKey(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            search_service_name=dict(
                type='str',
                required=True
            ),
            clientrequestid=dict(
                type='uuid',
                required=True
            ),
            search_management_request_options=dict(
                type='group',
                disposition='/search_management_request_options',
                required=True,
                options=dict(
                    client_request_id=dict(
                        type='uuid',
                        disposition='client_request_id'
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
        self.search_service_name = None
        self.clientrequestid = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAdminKey, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SearchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

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
                response = self.mgmt_client.admin_keys.create()
            else:
                response = self.mgmt_client.admin_keys.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AdminKey instance.')
            self.fail('Error creating the AdminKey instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.admin_keys.delete()
        except CloudError as e:
            self.log('Error attempting to delete the AdminKey instance.')
            self.fail('Error deleting the AdminKey instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.admin_keys.get(resource_group_name=self.resource_group_name,
                                                       search_service_name=self.search_service_name,
                                                       clientrequestid=self.clientrequestid,
                                                       parameters=self.body)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAdminKey()


if __name__ == '__main__':
    main()
