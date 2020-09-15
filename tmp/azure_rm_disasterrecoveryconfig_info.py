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
module: azure_rm_disasterrecoveryconfig_info
version_added: '2.9'
short_description: Get DisasterRecoveryConfig info.
description:
  - Get info of DisasterRecoveryConfig.
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
    type: str
  authorization_rule_name:
    description:
      - The authorization rule name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SBAliasList
      azure_rm_disasterrecoveryconfig_info: 
        namespace_name: sdk-Namespace-8860
        resource_group_name: ardsouzatestRG
        

    - name: SBAliasGet
      azure_rm_disasterrecoveryconfig_info: 
        alias: sdk-DisasterRecovery-3814
        namespace_name: sdk-Namespace-8860
        resource_group_name: ardsouzatestRG
        

    - name: NameSpaceAuthorizationRuleListAll
      azure_rm_disasterrecoveryconfig_info: 
        alias: sdk-DisasterRecovery-4047
        namespace_name: sdk-Namespace-9080
        resource_group_name: exampleResourceGroup
        

    - name: DisasterRecoveryConfigsAuthorizationRuleGet
      azure_rm_disasterrecoveryconfig_info: 
        alias: sdk-DisasterRecovery-4879
        authorization_rule_name: sdk-Authrules-4879
        namespace_name: sdk-Namespace-9080
        resource_group_name: exampleResourceGroup
        

'''

RETURN = '''
disaster_recovery_configs:
  description: >-
    A list of dict results where the key is the name of the
    DisasterRecoveryConfig and the values are the facts for that
    DisasterRecoveryConfig.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          List of Alias(Disaster Recovery configurations)
          Result of the List Authorization Rules operation.
      returned: always
      type: list
      sample: null
      contains:
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
              ARM Id of the Primary/Secondary eventhub namespace name, which is
              part of GEO DR pairing
          returned: always
          type: str
          sample: null
        alternate_name:
          description:
            - >-
              Primary/Secondary eventhub namespace name, which is part of GEO DR
              pairing
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
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of Alias(Disaster Recovery configuration)

          Link to the next set of results. Not empty if Value contains
          incomplete list of Authorization Rules.
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
          ARM Id of the Primary/Secondary eventhub namespace name, which is part
          of GEO DR pairing
      returned: always
      type: str
      sample: null
    alternate_name:
      description:
        - >-
          Primary/Secondary eventhub namespace name, which is part of GEO DR
          pairing
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
    rights:
      description:
        - The rights associated with the rule.
      returned: always
      type: list
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


class AzureRMDisasterRecoveryConfigInfo(AzureRMModuleBase):
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
                type='str'
            ),
            authorization_rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.alias = None
        self.authorization_rule_name = None

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
        super(AzureRMDisasterRecoveryConfigInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.alias is not None and
            self.authorization_rule_name is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.alias is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.alias is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.listauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.list())
        return self.results

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.get_authorization_rule(resource_group_name=self.resource_group_name,
                                                                                         namespace_name=self.namespace_name,
                                                                                         alias=self.alias,
                                                                                         authorization_rule_name=self.authorization_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.get(resource_group_name=self.resource_group_name,
                                                                      namespace_name=self.namespace_name,
                                                                      alias=self.alias)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.list_authorization_rule(resource_group_name=self.resource_group_name,
                                                                                          namespace_name=self.namespace_name,
                                                                                          alias=self.alias)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.list(resource_group_name=self.resource_group_name,
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
    AzureRMDisasterRecoveryConfigInfo()


if __name__ == '__main__':
    main()
