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
module: azure_rm_geobackuppolicy_info
version_added: '2.9'
short_description: Get GeoBackupPolicy info.
description:
  - Get info of GeoBackupPolicy.
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
  database_name:
    description:
      - The name of the database.
    required: true
    type: str
  geo_backup_policy_name:
    description:
      - The name of the geo backup policy.
    type: str
    choices:
      - Default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get geo backup policy
      azure_rm_geobackuppolicy_info: 
        database_name: testdw
        geo_backup_policy_name: Default
        resource_group_name: sqlcrudtest-4799
        server_name: sqlcrudtest-5961
        

    - name: List geo backup policies
      azure_rm_geobackuppolicy_info: 
        database_name: testdw
        resource_group_name: sqlcrudtest-4799
        server_name: sqlcrudtest-5961
        

'''

RETURN = '''
geo_backup_policies:
  description: >-
    A list of dict results where the key is the name of the GeoBackupPolicy and
    the values are the facts for that GeoBackupPolicy.
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
    kind:
      description:
        - >-
          Kind of geo backup policy.  This is metadata used for the Azure portal
          experience.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Backup policy location.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The state of the geo backup policy.
      returned: always
      type: sealed-choice
      sample: null
    storage_type:
      description:
        - The storage type of the geo backup policy.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of geo backup policies.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - >-
              Kind of geo backup policy.  This is metadata used for the Azure
              portal experience.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Backup policy location.
          returned: always
          type: str
          sample: null
        state:
          description:
            - The state of the geo backup policy.
          returned: always
          type: sealed-choice
          sample: null
        storage_type:
          description:
            - The storage type of the geo backup policy.
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


class AzureRMGeoBackupPolicyInfo(AzureRMModuleBase):
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
            database_name=dict(
                type='str',
                required=True
            ),
            geo_backup_policy_name=dict(
                type='str',
                choices=['Default']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.geo_backup_policy_name = None

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
        super(AzureRMGeoBackupPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.geo_backup_policy_name is not None):
            self.results['geo_backup_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['geo_backup_policies'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.geo_backup_policies.get(resource_group_name=self.resource_group_name,
                                                                server_name=self.server_name,
                                                                database_name=self.database_name,
                                                                geo_backup_policy_name=self.geo_backup_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.geo_backup_policies.list_by_database(resource_group_name=self.resource_group_name,
                                                                             server_name=self.server_name,
                                                                             database_name=self.database_name)
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
    AzureRMGeoBackupPolicyInfo()


if __name__ == '__main__':
    main()
