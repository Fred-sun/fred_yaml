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
module: azure_rm_jobagent_info
version_added: '2.9'
short_description: Get JobAgent info.
description:
  - Get info of JobAgent.
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
      - The name of the job agent to be retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List job agents in a server
      azure_rm_jobagent_info: 
        resource_group_name: group1
        server_name: server1
        

    - name: Get a job agent
      azure_rm_jobagent_info: 
        job_agent_name: agent1
        resource_group_name: group1
        server_name: server1
        

'''

RETURN = '''
job_agents:
  description: >-
    A list of dict results where the key is the name of the JobAgent and the
    values are the facts for that JobAgent.
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
        sku:
          description:
            - The name and tier of the SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the SKU, typically, a letter + Number code, e.g.
                  P3.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - >-
                  The tier or edition of the particular SKU, e.g. Basic,
                  Premium.
              returned: always
              type: str
              sample: null
            size:
              description:
                - Size of the particular SKU
              returned: always
              type: str
              sample: null
            family:
              description:
                - >-
                  If the service has different generations of hardware, for the
                  same SKU, then that can be captured here.
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - Capacity of the particular SKU.
              returned: always
              type: integer
              sample: null
        database_id:
          description:
            - Resource ID of the database to store job metadata in.
          returned: always
          type: str
          sample: null
        state:
          description:
            - The state of the job agent.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - The name and tier of the SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
          returned: always
          type: str
          sample: null
        tier:
          description:
            - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
          returned: always
          type: str
          sample: null
        size:
          description:
            - Size of the particular SKU
          returned: always
          type: str
          sample: null
        family:
          description:
            - >-
              If the service has different generations of hardware, for the same
              SKU, then that can be captured here.
          returned: always
          type: str
          sample: null
        capacity:
          description:
            - Capacity of the particular SKU.
          returned: always
          type: integer
          sample: null
    database_id:
      description:
        - Resource ID of the database to store job metadata in.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The state of the job agent.
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


class AzureRMJobAgentInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.job_agent_name = None

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
        super(AzureRMJobAgentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.job_agent_name is not None):
            self.results['job_agents'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['job_agents'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_agents.get(resource_group_name=self.resource_group_name,
                                                       server_name=self.server_name,
                                                       job_agent_name=self.job_agent_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.job_agents.list_by_server(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name)
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
    AzureRMJobAgentInfo()


if __name__ == '__main__':
    main()
