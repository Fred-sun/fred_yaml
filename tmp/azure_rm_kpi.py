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
module: azure_rm_kpi
version_added: '2.9'
short_description: Manage Azure Kpi instance.
description:
  - 'Create, update and delete instance of Azure Kpi.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  hub_name:
    description:
      - The name of the hub.
    required: true
    type: str
  kpi_name:
    description:
      - The name of the KPI.
    required: true
    type: str
  entity_type:
    description:
      - The mapping entity type.
    type: sealed-choice
  entity_type_name:
    description:
      - The mapping entity name.
    type: str
  display_name:
    description:
      - Localized display name for the KPI.
    type: dictionary
  description:
    description:
      - Localized description for the KPI.
    type: dictionary
  calculation_window:
    description:
      - The calculation window.
    type: sealed-choice
  calculation_window_field_name:
    description:
      - Name of calculation window field.
    type: str
  function:
    description:
      - The computation function for the KPI.
    type: sealed-choice
  expression:
    description:
      - The computation expression for the KPI.
    type: str
  unit:
    description:
      - The unit of measurement for the KPI.
    type: str
  filter:
    description:
      - The filter expression for the KPI.
    type: str
  group_by:
    description:
      - the group by properties for the KPI.
    type: list
  thres_holds:
    description:
      - The KPI thresholds.
    type: dict
    suboptions:
      lower_limit:
        description:
          - The lower threshold limit.
        required: true
        type: number
      upper_limit:
        description:
          - The upper threshold limit.
        required: true
        type: number
      increasing_kpi:
        description:
          - Whether or not the KPI is an increasing KPI.
        required: true
        type: bool
  aliases:
    description:
      - The aliases.
    type: list
    suboptions:
      alias_name:
        description:
          - KPI alias name.
        required: true
        type: str
      expression:
        description:
          - The expression.
        required: true
        type: str
  extracts:
    description:
      - The KPI extracts.
    type: list
    suboptions:
      extract_name:
        description:
          - KPI extract name.
        required: true
        type: str
      expression:
        description:
          - The expression.
        required: true
        type: str
  state:
    description:
      - Assert the state of the Kpi.
      - Use C(present) to create or update an Kpi and C(absent) to delete it.
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
    - name: Kpi_CreateOrUpdate
      azure_rm_kpi: 
        hub_name: sdkTestHub
        kpi_name: kpiTest45453647
        resource_group_name: TestHubRG
        properties:
          description:
            en-us: Kpi Description
          aliases:
            - alias_name: alias
              expression: Id+4
          calculation_window: Day
          display_name:
            en-us: Kpi DisplayName
          entity_type: Profile
          entity_type_name: testProfile2327128
          expression: SavingAccountBalance
          function: Sum
          group_by:
            - SavingAccountBalance
          thres_holds:
            increasing_kpi: true
            lower_limit: 5
            upper_limit: 50
          unit: unit
        

    - name: Kpi_Delete
      azure_rm_kpi: 
        hub_name: sdkTestHub
        kpi_name: kpiTest45453647
        resource_group_name: TestHubRG
        

'''

RETURN = '''
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
entity_type:
  description:
    - The mapping entity type.
  returned: always
  type: sealed-choice
  sample: null
entity_type_name:
  description:
    - The mapping entity name.
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The hub name.
  returned: always
  type: str
  sample: null
kpi_name:
  description:
    - The KPI name.
  returned: always
  type: str
  sample: null
display_name:
  description:
    - Localized display name for the KPI.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - Localized description for the KPI.
  returned: always
  type: dictionary
  sample: null
calculation_window:
  description:
    - The calculation window.
  returned: always
  type: sealed-choice
  sample: null
calculation_window_field_name:
  description:
    - Name of calculation window field.
  returned: always
  type: str
  sample: null
function:
  description:
    - The computation function for the KPI.
  returned: always
  type: sealed-choice
  sample: null
expression:
  description:
    - The computation expression for the KPI.
  returned: always
  type: str
  sample: null
unit:
  description:
    - The unit of measurement for the KPI.
  returned: always
  type: str
  sample: null
filter:
  description:
    - The filter expression for the KPI.
  returned: always
  type: str
  sample: null
group_by:
  description:
    - the group by properties for the KPI.
  returned: always
  type: list
  sample: null
group_by_metadata:
  description:
    - The KPI GroupByMetadata.
  returned: always
  type: list
  sample: null
  contains:
    display_name:
      description:
        - The display name.
      returned: always
      type: dictionary
      sample: null
    field_name:
      description:
        - The name of the field.
      returned: always
      type: str
      sample: null
    field_type:
      description:
        - The type of the field.
      returned: always
      type: str
      sample: null
participant_profiles_metadata:
  description:
    - The participant profiles.
  returned: always
  type: list
  sample: null
  contains:
    type_name:
      description:
        - Name of the type.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - Provisioning state.
  returned: always
  type: str
  sample: null
thres_holds:
  description:
    - The KPI thresholds.
  returned: always
  type: dict
  sample: null
  contains:
    lower_limit:
      description:
        - The lower threshold limit.
      returned: always
      type: number
      sample: null
    upper_limit:
      description:
        - The upper threshold limit.
      returned: always
      type: number
      sample: null
    increasing_kpi:
      description:
        - Whether or not the KPI is an increasing KPI.
      returned: always
      type: bool
      sample: null
aliases:
  description:
    - The aliases.
  returned: always
  type: list
  sample: null
  contains:
    alias_name:
      description:
        - KPI alias name.
      returned: always
      type: str
      sample: null
    expression:
      description:
        - The expression.
      returned: always
      type: str
      sample: null
extracts:
  description:
    - The KPI extracts.
  returned: always
  type: list
  sample: null
  contains:
    extract_name:
      description:
        - KPI extract name.
      returned: always
      type: str
      sample: null
    expression:
      description:
        - The expression.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMKpi(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            hub_name=dict(
                type='str',
                required=True
            ),
            kpi_name=dict(
                type='str',
                required=True
            ),
            entity_type=dict(
                type='sealed-choice',
                disposition='/entity_type'
            ),
            entity_type_name=dict(
                type='str',
                disposition='/entity_type_name'
            ),
            display_name=dict(
                type='dictionary',
                disposition='/display_name'
            ),
            description=dict(
                type='dictionary',
                disposition='/description'
            ),
            calculation_window=dict(
                type='sealed-choice',
                disposition='/calculation_window'
            ),
            calculation_window_field_name=dict(
                type='str',
                disposition='/calculation_window_field_name'
            ),
            function=dict(
                type='sealed-choice',
                disposition='/function'
            ),
            expression=dict(
                type='str',
                disposition='/expression'
            ),
            unit=dict(
                type='str',
                disposition='/unit'
            ),
            filter=dict(
                type='str',
                disposition='/filter'
            ),
            group_by=dict(
                type='list',
                disposition='/group_by',
                elements='str'
            ),
            thres_holds=dict(
                type='dict',
                disposition='/thres_holds',
                options=dict(
                    lower_limit=dict(
                        type='number',
                        disposition='lower_limit',
                        required=True
                    ),
                    upper_limit=dict(
                        type='number',
                        disposition='upper_limit',
                        required=True
                    ),
                    increasing_kpi=dict(
                        type='bool',
                        disposition='increasing_kpi',
                        required=True
                    )
                )
            ),
            aliases=dict(
                type='list',
                disposition='/aliases',
                elements='dict',
                options=dict(
                    alias_name=dict(
                        type='str',
                        disposition='alias_name',
                        required=True
                    ),
                    expression=dict(
                        type='str',
                        disposition='expression',
                        required=True
                    )
                )
            ),
            extracts=dict(
                type='list',
                disposition='/extracts',
                elements='dict',
                options=dict(
                    extract_name=dict(
                        type='str',
                        disposition='extract_name',
                        required=True
                    ),
                    expression=dict(
                        type='str',
                        disposition='expression',
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.kpi_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMKpi, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

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
            response = self.mgmt_client.kpi.create_or_update(resource_group_name=self.resource_group_name,
                                                             hub_name=self.hub_name,
                                                             kpi_name=self.kpi_name,
                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Kpi instance.')
            self.fail('Error creating the Kpi instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.kpi.delete(resource_group_name=self.resource_group_name,
                                                   hub_name=self.hub_name,
                                                   kpi_name=self.kpi_name)
        except CloudError as e:
            self.log('Error attempting to delete the Kpi instance.')
            self.fail('Error deleting the Kpi instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.kpi.get(resource_group_name=self.resource_group_name,
                                                hub_name=self.hub_name,
                                                kpi_name=self.kpi_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMKpi()


if __name__ == '__main__':
    main()
