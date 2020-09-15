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
module: azure_rm_serverusage_info
version_added: '2.9'
short_description: Get ServerUsage info.
description:
  - Get info of ServerUsage.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List servers usages
      azure_rm_serverusage_info: 
        resource_group_name: sqlcrudtest-6730
        server_name: sqlcrudtest-9007
        

'''

RETURN = '''
server_usages:
  description: >-
    A list of dict results where the key is the name of the ServerUsage and the
    values are the facts for that ServerUsage.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of server metrics for the server.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the server usage metric.
          returned: always
          type: str
          sample: null
        resource_name:
          description:
            - The name of the resource.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The metric display name.
          returned: always
          type: str
          sample: null
        current_value:
          description:
            - The current value of the metric.
          returned: always
          type: number
          sample: null
        limit:
          description:
            - The current limit of the metric.
          returned: always
          type: number
          sample: null
        unit:
          description:
            - The units of the metric.
          returned: always
          type: str
          sample: null
        next_reset_time:
          description:
            - The next reset time for the metric (ISO8601 format).
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


class AzureRMServerUsageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.server_name = None

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
        super(AzureRMServerUsageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None):
            self.results['server_usages'] = self.format_item(self.listbyserver())
        return self.results

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.server_usages.list_by_server(resource_group_name=self.resource_group_name,
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
    AzureRMServerUsageInfo()


if __name__ == '__main__':
    main()
