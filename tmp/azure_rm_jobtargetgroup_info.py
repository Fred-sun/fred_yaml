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
module: azure_rm_jobtargetgroup_info
version_added: '2.9'
short_description: Get JobTargetGroup info.
description:
  - Get info of JobTargetGroup.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  job_agent_name:
    description:
      - The name of the job agent.
    required: true
    type: str
  target_group_name:
    description:
      - The name of the target group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all target groups in an agent.
      azure_rm_jobtargetgroup_info: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        

    - name: Get a target group.
      azure_rm_jobtargetgroup_info: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        target_group_name: targetGroup1
        

'''

RETURN = '''
job_target_groups:
  description: >-
    A list of dict results where the key is the name of the JobTargetGroup and
    the values are the facts for that JobTargetGroup.
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
        members:
          description:
            - Members of the target group.
          returned: always
          type: list
          sample: null
          contains:
            membership_type:
              description:
                - Whether the target is included or excluded from the group.
              returned: always
              type: sealed-choice
              sample: null
            type:
              description:
                - The target type.
              returned: always
              type: str
              sample: null
            server_name:
              description:
                - The target server name.
              returned: always
              type: str
              sample: null
            database_name:
              description:
                - The target database name.
              returned: always
              type: str
              sample: null
            elastic_pool_name:
              description:
                - The target elastic pool name.
              returned: always
              type: str
              sample: null
            shard_map_name:
              description:
                - The target shard map.
              returned: always
              type: str
              sample: null
            refresh_credential:
              description:
                - >-
                  The resource ID of the credential that is used during job
                  execution to connect to the target and determine the list of
                  databases inside the target.
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
    members:
      description:
        - Members of the target group.
      returned: always
      type: list
      sample: null
      contains:
        membership_type:
          description:
            - Whether the target is included or excluded from the group.
          returned: always
          type: sealed-choice
          sample: null
        type:
          description:
            - The target type.
          returned: always
          type: str
          sample: null
        server_name:
          description:
            - The target server name.
          returned: always
          type: str
          sample: null
        database_name:
          description:
            - The target database name.
          returned: always
          type: str
          sample: null
        elastic_pool_name:
          description:
            - The target elastic pool name.
          returned: always
          type: str
          sample: null
        shard_map_name:
          description:
            - The target shard map.
          returned: always
          type: str
          sample: null
        refresh_credential:
          description:
            - >-
              The resource ID of the credential that is used during job
              execution to connect to the target and determine the list of
              databases inside the target.
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


class AzureRMJobTargetGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            job_agent_name=dict(
                type='str',
                required=True
            ),
            target_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.job_agent_name = None
        self.target_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMJobTargetGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.job_agent_name is not None and
            self.target_group_name is not None):
            self.results['job_target_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.job_agent_name is not None):
            self.results['job_target_groups'] = self.format_item(self.listbyagent())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_target_groups.get(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              job_agent_name=self.job_agent_name,
                                                              target_group_name=self.target_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyagent(self):
        response = None

        try:
            response = self.mgmt_client.job_target_groups.list_by_agent(resource_group_name=self.resource_group_name,
                                                                        server_name=self.server_name,
                                                                        job_agent_name=self.job_agent_name)
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
    AzureRMJobTargetGroupInfo()


if __name__ == '__main__':
    main()
