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
module: azure_rm_jobversion_info
version_added: '2.9'
short_description: Get JobVersion info.
description:
  - Get info of JobVersion.
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
  job_name:
    description:
      - The name of the job to get.
      - The name of the job.
    required: true
    type: str
  job_version:
    description:
      - The version of the job to get.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all versions of a job.
      azure_rm_jobversion_info: 
        job_agent_name: agent1
        job_name: job1
        resource_group_name: group1
        server_name: server1
        

    - name: Get a version of a job.
      azure_rm_jobversion_info: 
        job_agent_name: agent1
        job_name: job1
        job_version: '1'
        resource_group_name: group1
        server_name: server1
        

'''

RETURN = '''
job_versions:
  description: >-
    A list of dict results where the key is the name of the JobVersion and the
    values are the facts for that JobVersion.
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


class AzureRMJobVersionInfo(AzureRMModuleBase):
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
            job_name=dict(
                type='str',
                required=True
            ),
            job_version=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.job_agent_name = None
        self.job_name = None
        self.job_version = None

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
        super(AzureRMJobVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.job_agent_name is not None and
            self.job_name is not None and
            self.job_version is not None):
            self.results['job_versions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.job_agent_name is not None and
              self.job_name is not None):
            self.results['job_versions'] = self.format_item(self.listbyjob())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_versions.get(resource_group_name=self.resource_group_name,
                                                         server_name=self.server_name,
                                                         job_agent_name=self.job_agent_name,
                                                         job_name=self.job_name,
                                                         job_version=self.job_version)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyjob(self):
        response = None

        try:
            response = self.mgmt_client.job_versions.list_by_job(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 job_agent_name=self.job_agent_name,
                                                                 job_name=self.job_name)
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
    AzureRMJobVersionInfo()


if __name__ == '__main__':
    main()
