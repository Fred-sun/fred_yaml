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
module: azure_rm_configuration_info
version_added: '2.9'
short_description: Get Configuration info.
description:
  - Get info of Configuration.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  configuration_name:
    description:
      - The name of the server configuration.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ConfigurationGet
      azure_rm_configuration_info: 
        configuration_name: array_nulls
        resource_group_name: TestGroup
        server_name: testserver
        

    - name: ConfigurationList
      azure_rm_configuration_info: 
        resource_group_name: TestGroup
        server_name: testserver
        

'''

RETURN = '''
configurations:
  description: >-
    A list of dict results where the key is the name of the Configuration and
    the values are the facts for that Configuration.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    value:
      description:
        - |-
          Value of the configuration.
          The list of server configurations.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description of the configuration.
      returned: always
      type: str
      sample: null
    default_value:
      description:
        - Default value of the configuration.
      returned: always
      type: str
      sample: null
    data_type:
      description:
        - Data type of the configuration.
      returned: always
      type: str
      sample: null
    allowed_values:
      description:
        - Allowed values of the configuration.
      returned: always
      type: str
      sample: null
    source:
      description:
        - Source of the configuration.
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
    from azure.mgmt.postgre import PostgreSQLManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConfigurationInfo(AzureRMModuleBase):
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
            configuration_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.configuration_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-12-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.configuration_name is not None):
            self.results['configurations'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['configurations'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.configurations.get(resource_group_name=self.resource_group_name,
                                                           server_name=self.server_name,
                                                           configuration_name=self.configuration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.configurations.list_by_server(resource_group_name=self.resource_group_name,
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
    AzureRMConfigurationInfo()


if __name__ == '__main__':
    main()
