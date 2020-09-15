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
module: azure_rm_hybridusebenefitrevision_info
version_added: '2.9'
short_description: Get HybridUseBenefitRevision info.
description:
  - Get info of HybridUseBenefitRevision.
options:
  scope:
    description:
      - >-
        The scope at which the operation is performed. This is limited to
        Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts
        for now
    required: true
    type: str
  plan_id:
    description:
      - This is a unique identifier for a plan. Should be a guid.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: HybridUseBenefitRevisionsResponse
      azure_rm_hybridusebenefitrevision_info: 
        plan_id: 94f46eda-45f8-493a-8425-251921463a89
        scope: >-
          subscriptions/{sub-id}/resourceGroups/{rg-name}/providers/Microsoft.Compute/HostGroups/{host-group-name}/hosts/{host-name}
        

'''

RETURN = '''
hybrid_use_benefit_revision:
  description: >-
    A list of dict results where the key is the name of the
    HybridUseBenefitRevision and the values are the facts for that
    HybridUseBenefitRevision.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of hybrid use benefits
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - Indicates the revision of the hybrid use benefit
          returned: always
          type: integer
          sample: null
        provisioning_state:
          description:
            - Provisioning state
          returned: always
          type: str
          sample: null
        created_date:
          description:
            - Created date
          returned: always
          type: str
          sample: null
        last_updated_date:
          description:
            - Last updated date
          returned: always
          type: str
          sample: null
        name_sku_name:
          description:
            - Name of the SKU to be applied
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Url to get the next page of items.
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
    from azure.mgmt.software import Software Plan RP
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMHybridUseBenefitRevisionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            plan_id=dict(
                type='str',
                required=True
            )
        )

        self.scope = None
        self.plan_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMHybridUseBenefitRevisionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Software Plan RP,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.scope is not None and
            self.plan_id is not None):
            self.results['hybrid_use_benefit_revision'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.hybrid_use_benefit_revision.list(scope=self.scope,
                                                                         plan_id=self.plan_id)
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
    AzureRMHybridUseBenefitRevisionInfo()


if __name__ == '__main__':
    main()
