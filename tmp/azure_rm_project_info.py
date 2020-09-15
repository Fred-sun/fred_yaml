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
module: azure_rm_project_info
version_added: '2.9'
short_description: Get Project info.
description:
  - Get info of Project.
options:
  resource_group_name:
    description:
      - Name of the resource group within the Azure subscription.
    required: true
    type: str
  root_resource_name:
    description:
      - Name of the Team Services account.
    required: true
    type: str
  resource_name:
    description:
      - Name of the Team Services project.
    type: str
  sub_container_name:
    description:
      - This parameter should be set to the resourceName.
    type: str
  operation:
    description:
      - The operation type. The only supported value is 'put'.
    type: str
  job_id:
    description:
      - The job identifier.
    type: uuid
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a list of project resources in the Team Services account
      azure_rm_project_info: 
        resource_group_name: VS-Example-Group
        root_resource_name: ExampleAccount
        

    - name: Get a project resource
      azure_rm_project_info: 
        resource_group_name: VS-Example-Group
        resource_name: ExampleProject
        root_resource_name: ExampleAccount
        

    - name: Get the status of the project creation job
      azure_rm_project_info: 
        job_id: 126167d2-d710-4b5d-80a8-a1d58717142d
        operation: put
        resource_group_name: VS-Example-Group
        resource_name: ExampleProject
        root_resource_name: ExampleAccount
        sub_container_name: ExampleProject
        

'''

RETURN = '''
projects:
  description: >-
    A list of dict results where the key is the name of the Project and the
    values are the facts for that Project.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of project resource details.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - Key/value pair of resource properties.
          returned: always
          type: dictionary
          sample: null
    id:
      description:
        - Unique identifier of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Key/value pair of resource properties.
      returned: always
      type: dictionary
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.visual import Visual Studio Resource Provider Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProjectInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            root_resource_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str'
            ),
            sub_container_name=dict(
                type='str'
            ),
            operation=dict(
                type='str'
            ),
            job_id=dict(
                type='uuid'
            )
        )

        self.resource_group_name = None
        self.root_resource_name = None
        self.resource_name = None
        self.sub_container_name = None
        self.operation = None
        self.job_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProjectInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Visual Studio Resource Provider Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01-preview')

        if (self.resource_group_name is not None and
            self.root_resource_name is not None and
            self.resource_name is not None and
            self.sub_container_name is not None and
            self.operation is not None):
            self.results['projects'] = self.format_item(self.getjobstatus())
        elif (self.resource_group_name is not None and
              self.root_resource_name is not None and
              self.resource_name is not None):
            self.results['projects'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.root_resource_name is not None):
            self.results['projects'] = self.format_item(self.listbyresourcegroup())
        return self.results

    def getjobstatus(self):
        response = None

        try:
            response = self.mgmt_client.projects.get_job_status(resource_group_name=self.resource_group_name,
                                                                root_resource_name=self.root_resource_name,
                                                                resource_name=self.resource_name,
                                                                sub_container_name=self.sub_container_name,
                                                                operation=self.operation,
                                                                job_id=self.job_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.projects.get(resource_group_name=self.resource_group_name,
                                                     root_resource_name=self.root_resource_name,
                                                     resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.projects.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                        root_resource_name=self.root_resource_name)
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
    AzureRMProjectInfo()


if __name__ == '__main__':
    main()
