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
module: azure_rm_serviceobjective_info
version_added: '2.9'
short_description: Get ServiceObjective info.
description:
  - Get info of ServiceObjective.
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
  service_objective_name:
    description:
      - The name of the service objective to retrieve.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a service objective
      azure_rm_serviceobjective_info: 
        resource_group_name: group1
        server_name: sqlcrudtest
        service_objective_name: 29dd7459-4a7c-4e56-be22-f0adda49440d
        

    - name: List service objectives
      azure_rm_serviceobjective_info: 
        resource_group_name: group1
        server_name: sqlcrudtest
        

'''

RETURN = '''
service_objectives:
  description: >-
    A list of dict results where the key is the name of the ServiceObjective and
    the values are the facts for that ServiceObjective.
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
    service_objective_name:
      description:
        - The name for the service objective.
      returned: always
      type: str
      sample: null
    is_default:
      description:
        - >-
          Gets whether the service level objective is the default service
          objective.
      returned: always
      type: bool
      sample: null
    is_system:
      description:
        - >-
          Gets whether the service level objective is a system service
          objective.
      returned: always
      type: bool
      sample: null
    description:
      description:
        - The description for the service level objective.
      returned: always
      type: str
      sample: null
    enabled:
      description:
        - Gets whether the service level objective is enabled.
      returned: always
      type: bool
      sample: null
    value:
      description:
        - The list of database service objectives.
      returned: always
      type: list
      sample: null
      contains:
        service_objective_name:
          description:
            - The name for the service objective.
          returned: always
          type: str
          sample: null
        is_default:
          description:
            - >-
              Gets whether the service level objective is the default service
              objective.
          returned: always
          type: bool
          sample: null
        is_system:
          description:
            - >-
              Gets whether the service level objective is a system service
              objective.
          returned: always
          type: bool
          sample: null
        description:
          description:
            - The description for the service level objective.
          returned: always
          type: str
          sample: null
        enabled:
          description:
            - Gets whether the service level objective is enabled.
          returned: always
          type: bool
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


class AzureRMServiceObjectiveInfo(AzureRMModuleBase):
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
            service_objective_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.service_objective_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMServiceObjectiveInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.service_objective_name is not None):
            self.results['service_objectives'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['service_objectives'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.service_objectives.get(resource_group_name=self.resource_group_name,
                                                               server_name=self.server_name,
                                                               service_objective_name=self.service_objective_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.service_objectives.list_by_server(resource_group_name=self.resource_group_name,
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
    AzureRMServiceObjectiveInfo()


if __name__ == '__main__':
    main()
