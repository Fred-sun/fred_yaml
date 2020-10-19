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
module: azure_rm_supportplantype_info
version_added: '2.9'
short_description: Get SupportPlanType info.
description:
  - Get info of SupportPlanType.
options:
  provider_name:
    description:
      - The support plan type. For now the only valid type is "canonical".
    required: true
    type: str
  plan_type_name:
    description:
      - The Canonical support plan type.
    required: true
    type: str
    choices:
      - Essential
      - Standard
      - Advanced
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SupportPlanTypes_Get
      azure_rm_supportplantype_info: 
        plan_type_name: Standard
        provider_name: Canonical
        

'''

RETURN = '''
support_plan_types:
  description: >-
    A list of dict results where the key is the name of the SupportPlanType and
    the values are the facts for that SupportPlanType.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          The id of the ARM resource, e.g.
          "/subscriptions/{id}/providers/Microsoft.Addons/supportProvider/{supportProviderName}/supportPlanTypes/{planTypeName}".
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          The name of the Canonical support plan, i.e. "essential", "standard"
          or "advanced".
      returned: always
      type: str
      sample: null
    type:
      description:
        - Microsoft.Addons/supportProvider
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource.
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
    from azure.mgmt.azure import Azure Addons Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSupportPlanTypeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            provider_name=dict(
                type='str',
                required=True
            ),
            plan_type_name=dict(
                type='str',
                choices=['Essential',
                         'Standard',
                         'Advanced'],
                required=True
            )
        )

        self.provider_name = None
        self.plan_type_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSupportPlanTypeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Addons Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-03-01')

        if (self.provider_name is not None and
            self.plan_type_name is not None):
            self.results['support_plan_types'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.support_plan_types.get(provider_name=self.provider_name,
                                                               plan_type_name=self.plan_type_name)
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
    AzureRMSupportPlanTypeInfo()


if __name__ == '__main__':
    main()
