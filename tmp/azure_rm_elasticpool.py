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
module: azure_rm_elasticpool
version_added: '2.9'
short_description: Manage Azure ElasticPool instance.
description:
  - 'Create, update and delete instance of Azure ElasticPool.'
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
  location:
    description:
      - Resource location.
    type: str
  sku:
    description:
      - "The elastic pool SKU.\r"
      - "\r"
      - "The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or the following command:\r"
      - "\r"
      - "```azurecli\r"
      - "az sql elastic-pool list-editions -l <location> -o table\r"
      - "````\r"
      - ''
      - An ARM Resource SKU.
    type: dict
    suboptions:
      name:
        description:
          - 'The name of the SKU, typically, a letter + Number code, e.g. P3.'
        required: true
        type: str
      tier:
        description:
          - 'The tier or edition of the particular SKU, e.g. Basic, Premium.'
        type: str
      size:
        description:
          - Size of the particular SKU
        type: str
      family:
        description:
          - >-
            If the service has different generations of hardware, for the same
            SKU, then that can be captured here.
        type: str
      capacity:
        description:
          - Capacity of the particular SKU.
        type: integer
  max_size_bytes:
    description:
      - The storage limit for the database elastic pool in bytes.
    type: integer
  per_database_settings:
    description:
      - The per database settings for the elastic pool.
    type: dict
    suboptions:
      min_capacity:
        description:
          - The minimum capacity all databases are guaranteed.
        type: number
      max_capacity:
        description:
          - The maximum capacity any one database can consume.
        type: number
  zone_redundant:
    description:
      - >-
        Whether or not this elastic pool is zone redundant, which means the
        replicas of this elastic pool will be spread across multiple
        availability zones.
    type: bool
  license_type:
    description:
      - The license type to apply for this elastic pool.
    type: str
    choices:
      - LicenseIncluded
      - BasePrice
  state:
    description:
      - Assert the state of the ElasticPool.
      - >-
        Use C(present) to create or update an ElasticPool and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create or update elastic pool with all parameter
      azure_rm_elasticpool: 
        elastic_pool_name: sqlcrudtest-8102
        resource_group_name: sqlcrudtest-2369
        server_name: sqlcrudtest-8069
        location: Japan East
        properties:
          per_database_settings:
            max_capacity: 2
            min_capacity: 0.25
        sku:
          name: GP_Gen4_2
          capacity: 2
          tier: GeneralPurpose
        

    - name: Create or update elastic pool with minimum parameters
      azure_rm_elasticpool: 
        elastic_pool_name: sqlcrudtest-8102
        resource_group_name: sqlcrudtest-2369
        server_name: sqlcrudtest-8069
        location: Japan East
        

    - name: Delete an elastic pool
      azure_rm_elasticpool: 
        elastic_pool_name: sqlcrudtest-3851
        resource_group_name: sqlcrudtest-3129
        server_name: sqlcrudtest-228
        

    - name: Update an elastic pool with all parameter
      azure_rm_elasticpool: 
        elastic_pool_name: sqlcrudtest-8102
        resource_group_name: sqlcrudtest-2369
        server_name: sqlcrudtest-8069
        properties:
          license_type: LicenseIncluded
          per_database_settings:
            max_capacity: 1
            min_capacity: 0.25
          zone_redundant: true
        sku:
          name: BC_Gen4_2
          capacity: 2
          tier: BusinessCritical
        

    - name: Update an elastic pool with minimum parameters
      azure_rm_elasticpool: 
        elastic_pool_name: sqlcrudtest-8102
        resource_group_name: sqlcrudtest-2369
        server_name: sqlcrudtest-8069
        

'''

RETURN = '''
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
      replicas of this elastic pool will be spread across multiple availability
      zones.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMElasticPool(AzureRMModuleBaseExt):
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
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    size=dict(
                        type='str',
                        disposition='size'
                    ),
                    family=dict(
                        type='str',
                        disposition='family'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            max_size_bytes=dict(
                type='integer',
                disposition='/max_size_bytes'
            ),
            per_database_settings=dict(
                type='dict',
                disposition='/per_database_settings',
                options=dict(
                    min_capacity=dict(
                        type='number',
                        disposition='min_capacity'
                    ),
                    max_capacity=dict(
                        type='number',
                        disposition='max_capacity'
                    )
                )
            ),
            zone_redundant=dict(
                type='bool',
                disposition='/zone_redundant'
            ),
            license_type=dict(
                type='str',
                disposition='/license_type',
                choices=['LicenseIncluded',
                         'BasePrice']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.elastic_pool_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMElasticPool, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                 supports_check_mode=True,
                                                 supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.elastic_pools.create_or_update(resource_group_name=self.resource_group_name,
                                                                       server_name=self.server_name,
                                                                       elastic_pool_name=self.elastic_pool_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ElasticPool instance.')
            self.fail('Error creating the ElasticPool instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.elastic_pools.delete(resource_group_name=self.resource_group_name,
                                                             server_name=self.server_name,
                                                             elastic_pool_name=self.elastic_pool_name)
        except CloudError as e:
            self.log('Error attempting to delete the ElasticPool instance.')
            self.fail('Error deleting the ElasticPool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.elastic_pools.get(resource_group_name=self.resource_group_name,
                                                          server_name=self.server_name,
                                                          elastic_pool_name=self.elastic_pool_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMElasticPool()


if __name__ == '__main__':
    main()
