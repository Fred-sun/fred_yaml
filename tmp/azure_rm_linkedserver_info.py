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
module: azure_rm_linkedserver_info
version_added: '2.9'
short_description: Get LinkedServer info.
description:
  - Get info of LinkedServer.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The name of the redis cache.
    required: true
    type: str
  linked_server_name:
    description:
      - The name of the linked server.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: LinkedServer_Get
      azure_rm_linkedserver_info: 
        name: cache1
        linked_server_name: cache2
        resource_group_name: rg1
        

    - name: LinkedServer_List
      azure_rm_linkedserver_info: 
        name: cache1
        resource_group_name: rg1
        

'''

RETURN = '''
linked_server:
  description: >-
    A list of dict results where the key is the name of the LinkedServer and the
    values are the facts for that LinkedServer.
  returned: always
  type: complex
  contains:
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
    value:
      description:
        - List of linked servers (with properties) of a Redis cache.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              Terminal state of the link between primary and secondary redis
              cache.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link for next set.
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
    from azure.mgmt.redis import RedisManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLinkedServerInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.name = None
        self.linked_server_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLinkedServerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RedisManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01')

        if (self.resource_group_name is not None and
            self.name is not None and
            self.linked_server_name is not None):
            self.results['linked_server'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['linked_server'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.linked_server.get(resource_group_name=self.resource_group_name,
                                                          name=self.name,
                                                          linked_server_name=self.linked_server_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.linked_server.list(resource_group_name=self.resource_group_name,
                                                           name=self.name)
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
    AzureRMLinkedServerInfo()


if __name__ == '__main__':
    main()
