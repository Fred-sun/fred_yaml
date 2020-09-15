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
module: azure_rm_elasticpool_info
version_added: '2.9'
short_description: Get ElasticPool info.
description:
  - Get info of ElasticPool.
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
    type: str
  filter:
    description:
      - An OData filter expression that describes a subset of metrics to return.
    type: str
  skip:
    description:
      - The number of elements in the collection to skip.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List database usage metrics
      azure_rm_elasticpool_info: 
        elastic_pool_name: '3481'
        resource_group_name: sqlcrudtest-6730
        server_name: sqlcrudtest-9007
        

    - name: Get all elastic pools in a server
      azure_rm_elasticpool_info: 
        resource_group_name: sqlcrudtest-2369
        server_name: sqlcrudtest-8069
        

    - name: Get an elastic pool
      azure_rm_elasticpool_info: 
        elastic_pool_name: sqlcrudtest-8102
        resource_group_name: sqlcrudtest-2369
        server_name: sqlcrudtest-8069
        

'''

RETURN = '''
elastic_pools:
  description: >-
    A list of dict results where the key is the name of the ElasticPool and the
    values are the facts for that ElasticPool.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          The list of metrics for the database.
          The list of metric definitions for the database.
          Array of results.
      returned: always
      type: list
      sample: null
      contains:
        start_time:
          description:
            - The start time for the metric (ISO-8601 format).
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The end time for the metric (ISO-8601 format).
          returned: always
          type: str
          sample: null
        time_grain:
          description:
            - The time step to be used to summarize the metric values.
          returned: always
          type: str
          sample: null
        unit:
          description:
            - The unit of the metric.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name information for the metric.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - The name of the database metric.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - The friendly name of the database metric.
              returned: always
              type: str
              sample: null
        metric_values:
          description:
            - The metric values for the specified time window and timestep.
          returned: always
          type: list
          sample: null
          contains:
            count:
              description:
                - The number of values for the metric.
              returned: always
              type: integer
              sample: null
            average:
              description:
                - The average value of the metric.
              returned: always
              type: number
              sample: null
            maximum:
              description:
                - The max value of the metric.
              returned: always
              type: number
              sample: null
            minimum:
              description:
                - The min value of the metric.
              returned: always
              type: number
              sample: null
            timestamp:
              description:
                - The metric timestamp (ISO-8601 format).
              returned: always
              type: str
              sample: null
            total:
              description:
                - The total value of the metric.
              returned: always
              type: number
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
        - "The elastic pool SKU.\r\n\r\nThe list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or the following command:\r\n\r\n```azurecli\r\naz sql elastic-pool list-editions -l <location> -o table\r\n````\r\n"
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
    kind:
      description:
        - >-
          Kind of elastic pool. This is metadata used for the Azure portal
          experience.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The state of the elastic pool.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of the elastic pool (ISO8601 format).
      returned: always
      type: str
      sample: null
    max_size_bytes:
      description:
        - The storage limit for the database elastic pool in bytes.
      returned: always
      type: integer
      sample: null
    per_database_settings:
      description:
        - The per database settings for the elastic pool.
      returned: always
      type: dict
      sample: null
      contains:
        min_capacity:
          description:
            - The minimum capacity all databases are guaranteed.
          returned: always
          type: number
          sample: null
        max_capacity:
          description:
            - The maximum capacity any one database can consume.
          returned: always
          type: number
          sample: null
    zone_redundant:
      description:
        - >-
          Whether or not this elastic pool is zone redundant, which means the
          replicas of this elastic pool will be spread across multiple
          availability zones.
      returned: always
      type: bool
      sample: null
    license_type:
      description:
        - The license type to apply for this elastic pool.
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


class AzureRMElasticPoolInfo(AzureRMModuleBase):
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
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            skip=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.elastic_pool_name = None
        self.filter = None
        self.skip = None

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
        super(AzureRMElasticPoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.elastic_pool_name is not None and
            self.filter is not None):
            self.results['elastic_pools'] = self.format_item(self.listmetric())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.elastic_pool_name is not None):
            self.results['elastic_pools'] = self.format_item(self.listmetricdefinition())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.elastic_pool_name is not None):
            self.results['elastic_pools'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None):
            self.results['elastic_pools'] = self.format_item(self.listbyserver())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.elastic_pools.list_metric(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  elastic_pool_name=self.elastic_pool_name,
                                                                  filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.elastic_pools.list_metric_definition(resource_group_name=self.resource_group_name,
                                                                             server_name=self.server_name,
                                                                             elastic_pool_name=self.elastic_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.elastic_pools.get(resource_group_name=self.resource_group_name,
                                                          server_name=self.server_name,
                                                          elastic_pool_name=self.elastic_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyserver(self):
        response = None

        try:
            response = self.mgmt_client.elastic_pools.list_by_server(resource_group_name=self.resource_group_name,
                                                                     server_name=self.server_name,
                                                                     skip=self.skip)
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
    AzureRMElasticPoolInfo()


if __name__ == '__main__':
    main()
