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
module: azure_rm_linkedserver
version_added: '2.9'
short_description: Manage Azure LinkedServer instance.
description:
  - 'Create, update and delete instance of Azure LinkedServer.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The name of the Redis cache.
      - The name of the redis cache.
    required: true
    type: str
  linked_server_name:
    description:
      - The name of the linked server that is being added to the Redis cache.
      - The name of the linked server.
    required: true
    type: str
  linked_redis_cache_id:
    description:
      - Fully qualified resourceId of the linked redis cache.
    type: str
  linked_redis_cache_location:
    description:
      - Location of the linked redis cache.
    type: str
  server_role:
    description:
      - Role of the linked server.
    type: sealed-choice
  state:
    description:
      - Assert the state of the LinkedServer.
      - >-
        Use C(present) to create or update an LinkedServer and C(absent) to
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
    - name: LinkedServer_Create
      azure_rm_linkedserver: 
        name: cache1
        linked_server_name: cache2
        resource_group_name: rg1
        properties:
          linked_redis_cache_id: >-
            /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Cache/Redis/cache2
          linked_redis_cache_location: West US
          server_role: Secondary
        

    - name: LinkedServerDelete
      azure_rm_linkedserver: 
        name: cache1
        linked_server_name: cache2
        resource_group_name: rg1
        

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
linked_redis_cache_id:
  description:
    - Fully qualified resourceId of the linked redis cache.
  returned: always
  type: str
  sample: null
linked_redis_cache_location:
  description:
    - Location of the linked redis cache.
  returned: always
  type: str
  sample: null
server_role:
  description:
    - Role of the linked server.
  returned: always
  type: sealed-choice
  sample: null
provisioning_state:
  description:
    - Terminal state of the link between primary and secondary redis cache.
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
    from azure.mgmt.redis import RedisManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLinkedServer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            linked_server_name=dict(
                type='str',
                required=True
            ),
            linked_redis_cache_id=dict(
                type='str',
                disposition='/linked_redis_cache_id'
            ),
            linked_redis_cache_location=dict(
                type='str',
                disposition='/linked_redis_cache_location'
            ),
            server_role=dict(
                type='sealed-choice',
                disposition='/server_role'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.name = None
        self.linked_server_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLinkedServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(RedisManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01')

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
                response = self.mgmt_client.linked_server.create(resource_group_name=self.resource_group_name,
                                                                 name=self.name,
                                                                 linked_server_name=self.linked_server_name,
                                                                 parameters=self.body)
            else:
                response = self.mgmt_client.linked_server.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LinkedServer instance.')
            self.fail('Error creating the LinkedServer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.linked_server.delete(resource_group_name=self.resource_group_name,
                                                             name=self.name,
                                                             linked_server_name=self.linked_server_name)
        except CloudError as e:
            self.log('Error attempting to delete the LinkedServer instance.')
            self.fail('Error deleting the LinkedServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.linked_server.get(resource_group_name=self.resource_group_name,
                                                          name=self.name,
                                                          linked_server_name=self.linked_server_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLinkedServer()


if __name__ == '__main__':
    main()
