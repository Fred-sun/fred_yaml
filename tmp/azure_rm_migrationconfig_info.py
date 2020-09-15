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
module: azure_rm_migrationconfig_info
version_added: '2.9'
short_description: Get MigrationConfig info.
description:
  - Get info of MigrationConfig.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
  config_name:
    description:
      - The configuration name. Should always be "$default".
    type: str
    choices:
      - $default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: MigrationConfigurationsList
      azure_rm_migrationconfig_info: 
        namespace_name: sdk-Namespace-9259
        resource_group_name: ResourceGroup
        

    - name: MigrationConfigurationsGet
      azure_rm_migrationconfig_info: 
        config_name: $default
        namespace_name: sdk-Namespace-41
        resource_group_name: ResourceGroup
        

'''

RETURN = '''
migration_configs:
  description: >-
    A list of dict results where the key is the name of the MigrationConfig and
    the values are the facts for that MigrationConfig.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Migration Configs
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - 'Provisioning state of Migration Configuration '
          returned: always
          type: str
          sample: null
        pending_replication_operations_count:
          description:
            - Number of entities pending to be replicated.
          returned: always
          type: integer
          sample: null
        target_namespace:
          description:
            - >-
              Existing premium Namespace ARM Id name which has no entities, will
              be used for migration
          returned: always
          type: str
          sample: null
        post_migration_name:
          description:
            - Name to access Standard Namespace after migration
          returned: always
          type: str
          sample: null
        migration_state:
          description:
            - >-
              State in which Standard to Premium Migration is, possible values :
              Unknown, Reverting, Completing, Initiating, Syncing, Active
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of migrationConfigurations
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - 'Provisioning state of Migration Configuration '
      returned: always
      type: str
      sample: null
    pending_replication_operations_count:
      description:
        - Number of entities pending to be replicated.
      returned: always
      type: integer
      sample: null
    target_namespace:
      description:
        - >-
          Existing premium Namespace ARM Id name which has no entities, will be
          used for migration
      returned: always
      type: str
      sample: null
    post_migration_name:
      description:
        - Name to access Standard Namespace after migration
      returned: always
      type: str
      sample: null
    migration_state:
      description:
        - >-
          State in which Standard to Premium Migration is, possible values :
          Unknown, Reverting, Completing, Initiating, Syncing, Active
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
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMigrationConfigInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            ),
            config_name=dict(
                type='str',
                choices=['$default']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.config_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMigrationConfigInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.config_name is not None):
            self.results['migration_configs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['migration_configs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.migration_configs.get(resource_group_name=self.resource_group_name,
                                                              namespace_name=self.namespace_name,
                                                              config_name=self.config_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.migration_configs.list(resource_group_name=self.resource_group_name,
                                                               namespace_name=self.namespace_name)
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
    AzureRMMigrationConfigInfo()


if __name__ == '__main__':
    main()
