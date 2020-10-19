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
module: azure_rm_postgresinstance_info
version_added: '2.9'
short_description: Get PostgresInstance info.
description:
  - Get info of PostgresInstance.
options:
  resource_group_name:
    description:
      - The name of the Azure resource group
    type: str
  postgres_instance_name:
    description:
      - Name of Postgres Instance
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets all Postgres Instance in a subscription.
      azure_rm_postgresinstance_info: 
        {}
        

    - name: Gets all postgres Instances in a resource group.
      azure_rm_postgresinstance_info: 
        resource_group_name: testrg
        

    - name: Gets a postgres Instances.
      azure_rm_postgresinstance_info: 
        postgres_instance_name: testpostgresInstances
        resource_group_name: testrg
        

'''

RETURN = '''
postgres_instances:
  description: >-
    A list of dict results where the key is the name of the PostgresInstance and
    the values are the facts for that PostgresInstance.
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
        hybrid_data_manager_id:
          description:
            - 'null'
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    system_data:
      description:
        - Read only system data
      returned: always
      type: dict
      sample: null
      contains:
        created_by:
          description:
            - An identifier for the identity that created the resource
          returned: always
          type: str
          sample: null
        created_by_type:
          description:
            - The type of identity that created the resource
          returned: always
          type: str
          sample: null
        created_at:
          description:
            - The timestamp of resource creation (UTC)
          returned: always
          type: str
          sample: null
        last_modified_by:
          description:
            - An identifier for the identity that last modified the resource
          returned: always
          type: str
          sample: null
        last_modified_by_type:
          description:
            - The type of identity that last modified the resource
          returned: always
          type: str
          sample: null
        last_modified_at:
          description:
            - The timestamp of resource last modification (UTC)
          returned: always
          type: str
          sample: null
    hybrid_data_manager_id:
      description:
        - 'null'
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
    from azure.mgmt.azure import AzureDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPostgresInstanceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            postgres_instance_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.postgres_instance_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-24-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPostgresInstanceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-24-preview')

        if (self.resource_group_name is not None and
            self.postgres_instance_name is not None):
            self.results['postgres_instances'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['postgres_instances'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['postgres_instances'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.postgres_instances.get(resource_group_name=self.resource_group_name,
                                                               postgres_instance_name=self.postgres_instance_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.postgres_instances.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.postgres_instances.list()
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
    AzureRMPostgresInstanceInfo()


if __name__ == '__main__':
    main()
