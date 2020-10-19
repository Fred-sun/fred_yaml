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
module: azure_rm_patchschedule_info
version_added: '2.9'
short_description: Get PatchSchedule info.
description:
  - Get info of PatchSchedule.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  cache_name:
    description:
      - The name of the Redis cache.
    type: str
  name:
    description:
      - The name of the redis cache.
    type: str
  default:
    description:
      - >-
        Default string modeled as parameter for auto generation to work
        correctly.
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RedisCachePatchSchedulesList
      azure_rm_patchschedule_info: 
        cache_name: cache1
        resource_group_name: rg1
        

    - name: RedisCachePatchSchedulesGet
      azure_rm_patchschedule_info: 
        name: cache1
        default: default
        resource_group_name: rg1
        

'''

RETURN = '''
patch_schedules:
  description: >-
    A list of dict results where the key is the name of the PatchSchedule and
    the values are the facts for that PatchSchedule.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list patch schedules operation.
      returned: always
      type: list
      sample: null
      contains:
        schedule_entries:
          description:
            - List of patch schedules for a Redis cache.
          returned: always
          type: list
          sample: null
          contains:
            day_of_week:
              description:
                - Day of the week when a cache can be patched.
              returned: always
              type: sealed-choice
              sample: null
            start_hour_utc:
              description:
                - Start hour after which cache patching can start.
              returned: always
              type: integer
              sample: null
            maintenance_window:
              description:
                - >-
                  ISO8601 timespan specifying how much time cache patching can
                  take. 
              returned: always
              type: duration
              sample: null
    next_link:
      description:
        - Link for next page of results.
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
    schedule_entries:
      description:
        - List of patch schedules for a Redis cache.
      returned: always
      type: list
      sample: null
      contains:
        day_of_week:
          description:
            - Day of the week when a cache can be patched.
          returned: always
          type: sealed-choice
          sample: null
        start_hour_utc:
          description:
            - Start hour after which cache patching can start.
          returned: always
          type: integer
          sample: null
        maintenance_window:
          description:
            - >-
              ISO8601 timespan specifying how much time cache patching can
              take. 
          returned: always
          type: duration
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


class AzureRMPatchScheduleInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cache_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            default=dict(
                type='str',
                choices=['default']
            )
        )

        self.resource_group_name = None
        self.cache_name = None
        self.name = None
        self.default = None

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
        super(AzureRMPatchScheduleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RedisManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01')

        if (self.resource_group_name is not None and
            self.name is not None and
            self.default is not None):
            self.results['patch_schedules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.cache_name is not None):
            self.results['patch_schedules'] = self.format_item(self.listbyredisresource())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.patch_schedules.get(resource_group_name=self.resource_group_name,
                                                            name=self.name,
                                                            default=self.default)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyredisresource(self):
        response = None

        try:
            response = self.mgmt_client.patch_schedules.list_by_redis_resource(resource_group_name=self.resource_group_name,
                                                                               cache_name=self.cache_name)
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
    AzureRMPatchScheduleInfo()


if __name__ == '__main__':
    main()
