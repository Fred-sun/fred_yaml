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
module: azure_rm_diagnosticsettingscategory_info
version_added: '2.9'
short_description: Get DiagnosticSettingsCategory info.
description:
  - Get info of DiagnosticSettingsCategory.
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
  name:
    description:
      - The name of the diagnostic setting.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets the diagnostic setting
      azure_rm_diagnosticsettingscategory_info: 
        name: WorkflowRuntime
        resource_uri: >-
          subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourcegroups/viruela1/providers/microsoft.logic/workflows/viruela6
        

'''

RETURN = '''
diagnostic_settings_category:
  description: >-
    A list of dict results where the key is the name of the
    DiagnosticSettingsCategory and the values are the facts for that
    DiagnosticSettingsCategory.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Azure resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Azure resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Azure resource type
      returned: always
      type: str
      sample: null
    category_type:
      description:
        - The type of the diagnostic settings category.
      returned: always
      type: sealed-choice
      sample: null
    value:
      description:
        - The collection of diagnostic settings category resources.
      returned: always
      type: list
      sample: null
      contains:
        category_type:
          description:
            - The type of the diagnostic settings category.
          returned: always
          type: sealed-choice
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDiagnosticSettingsCategoryInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_uri = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDiagnosticSettingsCategoryInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-05-01-preview')

        if (self.resource_uri is not None and
            self.name is not None):
            self.results['diagnostic_settings_category'] = self.format_item(self.get())
        elif (self.resource_uri is not None):
            self.results['diagnostic_settings_category'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.diagnostic_settings_category.get(resource_uri=self.resource_uri,
                                                                         name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.diagnostic_settings_category.list(resource_uri=self.resource_uri)
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
    AzureRMDiagnosticSettingsCategoryInfo()


if __name__ == '__main__':
    main()
