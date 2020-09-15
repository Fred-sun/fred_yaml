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
module: azure_rm_kpi_info
version_added: '2.9'
short_description: Get Kpi info.
description:
  - Get info of Kpi.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Kpi_Get
      azure_rm_kpi_info: 
        hub_name: sdkTestHub
        kpi_name: kpiTest45453647
        resource_group_name: TestHubRG
        

    - name: Kpi_ListByHub
      azure_rm_kpi_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
kpi:
  description: >-
    A list of dict results where the key is the name of the Kpi and the values
    are the facts for that Kpi.
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
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
    next_link:
      description:
        - Link to the next set of results.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMKpiInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.kpi_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-26'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMKpiInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.kpi_name is not None):
            self.results['kpi'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['kpi'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.kpi.get(resource_group_name=self.resource_group_name,
                                                hub_name=self.hub_name,
                                                kpi_name=self.kpi_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.kpi.list_by_hub(resource_group_name=self.resource_group_name,
                                                        hub_name=self.hub_name)
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
    AzureRMKpiInfo()


if __name__ == '__main__':
    main()
