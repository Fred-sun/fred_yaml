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
module: azure_rm_recommendedelasticpool_info
version_added: '2.9'
short_description: Get RecommendedElasticPool info.
description:
  - Get info of RecommendedElasticPool.
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
  recommended_elastic_pool_name:
    description:
      - The name of the recommended elastic pool to be retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a recommended elastic pool
      azure_rm_recommendedelasticpool_info: 
        recommended_elastic_pool_name: ElasticPool1
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        

    - name: List recommended elastic pools
      azure_rm_recommendedelasticpool_info: 
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        

    - name: Get recommended elastic pool metrics
      azure_rm_recommendedelasticpool_info: 
        recommended_elastic_pool_name: sqlcrudtest-2080_pool1
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        

'''

RETURN = '''
recommended_elastic_pools:
  description: >-
    A list of dict results where the key is the name of the
    RecommendedElasticPool and the values are the facts for that
    RecommendedElasticPool.
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
    database_edition:
      description:
        - >-
          The edition of the recommended elastic pool. The ElasticPoolEdition
          enumeration contains all the valid editions.
      returned: always
      type: str
      sample: null
    dtu:
      description:
        - The DTU for the recommended elastic pool.
      returned: always
      type: number
      sample: null
    database_dtu_min:
      description:
        - The minimum DTU for the database.
      returned: always
      type: number
      sample: null
    database_dtu_max:
      description:
        - The maximum DTU for the database.
      returned: always
      type: number
      sample: null
    storage_mb:
      description:
        - Gets storage size in megabytes.
      returned: always
      type: number
      sample: null
    observation_period_start:
      description:
        - The observation period start (ISO8601 format).
      returned: always
      type: str
      sample: null
    observation_period_end:
      description:
        - The observation period start (ISO8601 format).
      returned: always
      type: str
      sample: null
    max_observed_dtu:
      description:
        - Gets maximum observed DTU.
      returned: always
      type: number
      sample: null
    max_observed_storage_mb:
      description:
        - Gets maximum observed storage in megabytes.
      returned: always
      type: number
      sample: null
    databases:
      description:
        - The list of databases in this pool. Expanded property
      returned: always
      type: list
      sample: null
      contains:
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
    metrics:
      description:
        - The list of databases housed in the server. Expanded property
      returned: always
      type: list
      sample: null
      contains:
        date_time:
          description:
            - The time of metric (ISO8601 format).
          returned: always
          type: str
          sample: null
        dtu:
          description:
            - >-
              Gets or sets the DTUs (Database Transaction Units). See
              https://azure.microsoft.com/documentation/articles/sql-database-what-is-a-dtu/
          returned: always
          type: number
          sample: null
        size_gb:
          description:
            - Gets or sets size in gigabytes.
          returned: always
          type: number
          sample: null
    value:
      description:
        - |-
          The list of recommended elastic pools hosted in the server.
          The list of recommended elastic pools metrics.
      returned: always
      type: list
      sample: null
      contains:
        database_edition:
          description:
            - >-
              The edition of the recommended elastic pool. The
              ElasticPoolEdition enumeration contains all the valid editions.
          returned: always
          type: str
          sample: null
        dtu:
          description:
            - The DTU for the recommended elastic pool.
          returned: always
          type: number
          sample: null
        database_dtu_min:
          description:
            - The minimum DTU for the database.
          returned: always
          type: number
          sample: null
        database_dtu_max:
          description:
            - The maximum DTU for the database.
          returned: always
          type: number
          sample: null
        storage_mb:
          description:
            - Gets storage size in megabytes.
          returned: always
          type: number
          sample: null
        observation_period_start:
          description:
            - The observation period start (ISO8601 format).
          returned: always
          type: str
          sample: null
        observation_period_end:
          description:
            - The observation period start (ISO8601 format).
          returned: always
          type: str
          sample: null
        max_observed_dtu:
          description:
            - Gets maximum observed DTU.
          returned: always
          type: number
          sample: null
        max_observed_storage_mb:
          description:
            - Gets maximum observed storage in megabytes.
          returned: always
          type: number
          sample: null
        databases:
          description:
            - The list of databases in this pool. Expanded property
          returned: always
          type: list
          sample: null
          contains:
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
        metrics:
          description:
            - The list of databases housed in the server. Expanded property
          returned: always
          type: list
          sample: null
          contains:
            date_time:
              description:
                - The time of metric (ISO8601 format).
              returned: always
              type: str
              sample: null
            dtu:
              description:
                - >-
                  Gets or sets the DTUs (Database Transaction Units). See
                  https://azure.microsoft.com/documentation/articles/sql-database-what-is-a-dtu/
              returned: always
              type: number
              sample: null
            size_gb:
              description:
                - Gets or sets size in gigabytes.
              returned: always
              type: number
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


class AzureRMRecommendedElasticPoolInfo(AzureRMModuleBase):
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
            recommended_elastic_pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.recommended_elastic_pool_name = None

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
        super(AzureRMRecommendedElasticPoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.recommended_elastic_pool_name is not None):
            self.results['recommended_elastic_pools'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.recommended_elastic_pool_name is not None):
            self.results['recommended_elastic_pools'] = self.format_item(self.listmetric())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['recommended_elastic_pools'] = self.format_item(self.listbyserver())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.recommended_elastic_pools.get(resource_group_name=self.resource_group_name,
                                                                      server_name=self.server_name,
                                                                      recommended_elastic_pool_name=self.recommended_elastic_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.recommended_elastic_pools.list_metric(resource_group_name=self.resource_group_name,
                                                                              server_name=self.server_name,
                                                                              recommended_elastic_pool_name=self.recommended_elastic_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.recommended_elastic_pools.list_by_server(resource_group_name=self.resource_group_name,
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
    AzureRMRecommendedElasticPoolInfo()


if __name__ == '__main__':
    main()
