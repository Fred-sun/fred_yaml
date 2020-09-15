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
module: azure_rm_elasticpooldatabaseactivity_info
version_added: '2.9'
short_description: Get ElasticPoolDatabaseActivity info.
description:
  - Get info of ElasticPoolDatabaseActivity.
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
      - The name of the elastic pool.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List elastic pool database activity
      azure_rm_elasticpooldatabaseactivity_info: 
        elastic_pool_name: '7537'
        resource_group_name: sqlcrudtest-4673
        server_name: sqlcrudtest-603
        

'''

RETURN = '''
elastic_pool_database_activities:
  description: >-
    A list of dict results where the key is the name of the
    ElasticPoolDatabaseActivity and the values are the facts for that
    ElasticPoolDatabaseActivity.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of elastic pool database activities.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - The geo-location where the resource lives
          returned: always
          type: str
          sample: null
        database_name:
          description:
            - The database name.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The time the operation finished (ISO8601 format).
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - The error code if available.
          returned: always
          type: integer
          sample: null
        error_message:
          description:
            - The error message if available.
          returned: always
          type: str
          sample: null
        error_severity:
          description:
            - The error severity if available.
          returned: always
          type: integer
          sample: null
        operation:
          description:
            - The operation name.
          returned: always
          type: str
          sample: null
        operation_id:
          description:
            - The unique operation ID.
          returned: always
          type: uuid
          sample: null
        percent_complete:
          description:
            - The percentage complete if available.
          returned: always
          type: integer
          sample: null
        requested_elastic_pool_name:
          description:
            - >-
              The name for the elastic pool the database is moving into if
              available.
          returned: always
          type: str
          sample: null
        current_elastic_pool_name:
          description:
            - >-
              The name of the current elastic pool the database is in if
              available.
          returned: always
          type: str
          sample: null
        current_service_objective:
          description:
            - The name of the current service objective if available.
          returned: always
          type: str
          sample: null
        requested_service_objective:
          description:
            - The name of the requested service objective if available.
          returned: always
          type: str
          sample: null
        server_name:
          description:
            - The name of the server the elastic pool is in.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - The time the operation started (ISO8601 format).
          returned: always
          type: str
          sample: null
        state:
          description:
            - The current state of the operation.
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


class AzureRMElasticPoolDatabaseActivityInfo(AzureRMModuleBase):
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
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMElasticPoolDatabaseActivityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.elastic_pool_name is not None):
            self.results['elastic_pool_database_activities'] = self.format_item(self.listbyelasticpool())
        return self.results

    def listbyelasticpool(self):
        response = None

        try:
            response = self.mgmt_client.elastic_pool_database_activities.list_by_elastic_pool(resource_group_name=self.resource_group_name,
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
    AzureRMElasticPoolDatabaseActivityInfo()


if __name__ == '__main__':
    main()
