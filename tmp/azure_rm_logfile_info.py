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
module: azure_rm_logfile_info
version_added: '2.9'
short_description: Get LogFile info.
description:
  - Get info of LogFile.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: LogFileList
      azure_rm_logfile_info: 
        resource_group_name: TestGroup
        server_name: testserver
        

'''

RETURN = '''
log_files:
  description: >-
    A list of dict results where the key is the name of the LogFile and the
    values are the facts for that LogFile.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of log files.
      returned: always
      type: list
      sample: null
      contains:
        size_in_kb:
          description:
            - Size of the log file.
          returned: always
          type: integer
          sample: null
        created_time:
          description:
            - Creation timestamp of the log file.
          returned: always
          type: str
          sample: null
        last_modified_time:
          description:
            - Last modified timestamp of the log file.
          returned: always
          type: str
          sample: null
        type_properties_type:
          description:
            - Type of the log file.
          returned: always
          type: str
          sample: null
        url:
          description:
            - The url to download the log file from.
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


class AzureRMLogFileInfo(AzureRMModuleBase):
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
        self.query_parameters['api-version'] = '2017-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLogFileInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-12-01')

        if (self.resource_group_name is not None and
            self.server_name is not None):
            self.results['log_files'] = self.format_item(self.listbyserver())
        return self.results

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.log_files.list_by_server(resource_group_name=self.resource_group_name,
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
    AzureRMLogFileInfo()


if __name__ == '__main__':
    main()
