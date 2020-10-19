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
module: azure_rm_migrationconfig
version_added: '2.9'
short_description: Manage Azure MigrationConfig instance.
description:
  - 'Create, update and delete instance of Azure MigrationConfig.'
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
    required: true
    type: str
    choices:
      - $default
  state:
    description:
      - Assert the state of the MigrationConfig.
      - >-
        Use C(present) to create or update an MigrationConfig and C(absent) to
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
    - name: MigrationConfigurationsDelete
      azure_rm_migrationconfig: 
        config_name: $default
        namespace_name: sdk-Namespace-41
        resource_group_name: ResourceGroup
        

'''

RETURN = '''
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
      Existing premium Namespace ARM Id name which has no entities, will be used
      for migration
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMigrationConfig(AzureRMModuleBaseExt):
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
                choices=['$default'],
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.config_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMigrationConfig, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.migration_configs.create()
            else:
                response = self.mgmt_client.migration_configs.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MigrationConfig instance.')
            self.fail('Error creating the MigrationConfig instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.migration_configs.delete(resource_group_name=self.resource_group_name,
                                                                 namespace_name=self.namespace_name,
                                                                 config_name=self.config_name)
        except CloudError as e:
            self.log('Error attempting to delete the MigrationConfig instance.')
            self.fail('Error deleting the MigrationConfig instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.migration_configs.get(resource_group_name=self.resource_group_name,
                                                              namespace_name=self.namespace_name,
                                                              config_name=self.config_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMigrationConfig()


if __name__ == '__main__':
    main()
