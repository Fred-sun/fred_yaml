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
module: azure_rm_elasticpooloperation_info
version_added: '2.9'
short_description: Get ElasticPoolOperation info.
description:
  - Get info of ElasticPoolOperation.
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
  elastic_pool_name:
    description:
      - undefined
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List the elastic pool management operations
      azure_rm_elasticpooloperation_info: 
        elastic_pool_name: testpool
        resource_group_name: sqlcrudtestgroup
        server_name: sqlcrudtestserver
        

'''

RETURN = '''
elastic_pool_operations:
  description: >-
    A list of dict results where the key is the name of the ElasticPoolOperation
    and the values are the facts for that ElasticPoolOperation.
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
        elastic_pool_name:
          description:
            - The name of the elastic pool the operation is being performed on.
          returned: always
          type: str
          sample: null
        operation:
          description:
            - The name of operation.
          returned: always
          type: str
          sample: null
        operation_friendly_name:
          description:
            - The friendly name of operation.
          returned: always
          type: str
          sample: null
        percent_complete:
          description:
            - The percentage of the operation completed.
          returned: always
          type: integer
          sample: null
        server_name:
          description:
            - The name of the server.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - The operation start time.
          returned: always
          type: str
          sample: null
        state:
          description:
            - The operation state.
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - The operation error code.
          returned: always
          type: integer
          sample: null
        error_description:
          description:
            - The operation error description.
          returned: always
          type: str
          sample: null
        error_severity:
          description:
            - The operation error severity.
          returned: always
          type: integer
          sample: null
        is_user_error:
          description:
            - Whether or not the error is a user error.
          returned: always
          type: bool
          sample: null
        estimated_completion_time:
          description:
            - The estimated completion time of the operation.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The operation description.
          returned: always
          type: str
          sample: null
        is_cancellable:
          description:
            - Whether the operation can be cancelled.
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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


class AzureRMElasticPoolOperationInfo(AzureRMModuleBase):
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
            elastic_pool_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.elastic_pool_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-10-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMElasticPoolOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.elastic_pool_name is not None):
            self.results['elastic_pool_operations'] = self.format_item(self.listbyelasticpool())
        return self.results

    def listbyelasticpool(self):
        response = None

        try:
            response = self.mgmt_client.elastic_pool_operations.list_by_elastic_pool(resource_group_name=self.resource_group_name,
                                                                                     server_name=self.server_name,
                                                                                     elastic_pool_name=self.elastic_pool_name)
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
    AzureRMElasticPoolOperationInfo()


if __name__ == '__main__':
    main()
