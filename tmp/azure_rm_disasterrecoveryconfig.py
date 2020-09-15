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
module: azure_rm_disasterrecoveryconfig
version_added: '2.9'
short_description: Manage Azure DisasterRecoveryConfig instance.
description:
  - 'Create, update and delete instance of Azure DisasterRecoveryConfig.'
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
  alias:
    description:
      - The Disaster Recovery configuration name
    required: true
    type: str
  partner_namespace:
    description:
      - >-
        ARM Id of the Primary/Secondary eventhub namespace name, which is part
        of GEO DR pairing
    type: str
  alternate_name:
    description:
      - >-
        Primary/Secondary eventhub namespace name, which is part of GEO DR
        pairing
    type: str
  state:
    description:
      - Assert the state of the DisasterRecoveryConfig.
      - >-
        Use C(present) to create or update an DisasterRecoveryConfig and
        C(absent) to delete it.
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
    - name: SBAliasCreate
      azure_rm_disasterrecoveryconfig: 
        alias: sdk-Namespace-8860
        namespace_name: sdk-Namespace-8860
        resource_group_name: ardsouzatestRG
        properties:
          alternate_name: alternameforAlias-Namespace-8860
          partner_namespace: sdk-Namespace-37
        

    - name: SBAliasDelete
      azure_rm_disasterrecoveryconfig: 
        alias: sdk-DisasterRecovery-3814
        namespace_name: sdk-Namespace-8860
        resource_group_name: SouthCentralUS
        

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
    - >-
      Provisioning state of the Alias(Disaster Recovery configuration) -
      possible values 'Accepted' or 'Succeeded' or 'Failed'
  returned: always
  type: sealed-choice
  sample: null
pending_replication_operations_count:
  description:
    - Number of entities pending to be replicated.
  returned: always
  type: integer
  sample: null
partner_namespace:
  description:
    - >-
      ARM Id of the Primary/Secondary eventhub namespace name, which is part of
      GEO DR pairing
  returned: always
  type: str
  sample: null
alternate_name:
  description:
    - 'Primary/Secondary eventhub namespace name, which is part of GEO DR pairing'
  returned: always
  type: str
  sample: null
role:
  description:
    - >-
      role of namespace in GEO DR - possible values 'Primary' or
      'PrimaryNotReplicating' or 'Secondary'
  returned: always
  type: sealed-choice
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


class AzureRMDisasterRecoveryConfig(AzureRMModuleBaseExt):
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
            alias=dict(
                type='str',
                required=True
            ),
            partner_namespace=dict(
                type='str',
                disposition='/partner_namespace'
            ),
            alternate_name=dict(
                type='str',
                disposition='/alternate_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.alias = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDisasterRecoveryConfig, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.disaster_recovery_configs.create_or_update(resource_group_name=self.resource_group_name,
                                                                                   namespace_name=self.namespace_name,
                                                                                   alias=self.alias,
                                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DisasterRecoveryConfig instance.')
            self.fail('Error creating the DisasterRecoveryConfig instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disaster_recovery_configs.delete(resource_group_name=self.resource_group_name,
                                                                         namespace_name=self.namespace_name,
                                                                         alias=self.alias)
        except CloudError as e:
            self.log('Error attempting to delete the DisasterRecoveryConfig instance.')
            self.fail('Error deleting the DisasterRecoveryConfig instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.disaster_recovery_configs.get(resource_group_name=self.resource_group_name,
                                                                      namespace_name=self.namespace_name,
                                                                      alias=self.alias)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDisasterRecoveryConfig()


if __name__ == '__main__':
    main()
