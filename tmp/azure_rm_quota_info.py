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
module: azure_rm_quota_info
version_added: '2.9'
short_description: Get Quota info.
description:
  - Get info of Quota.
options:
  provider_id:
    description:
      - Azure resource provider id.
    required: true
    type: str
  location:
    description:
      - Azure region.
    required: true
    type: str
  resource_name:
    description:
      - >-
        The resource name for a resource provider, such as SKU name for
        Microsoft.Compute, Sku or TotalLowPriorityCores for
        Microsoft.MachineLearningServices
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Quotas_Request_ForCompute
      azure_rm_quota_info: 
        location: eastus
        provider_id: Microsoft.Compute
        resource_name: standardNDSFamily
        

    - name: Quotas_listUsagesForCompute
      azure_rm_quota_info: 
        location: eastus
        provider_id: Microsoft.Compute
        

    - name: Quotas_listUsagesForMsSql
      azure_rm_quota_info: 
        location: westus
        provider_id: Microsoft.Sql
        

    - name: Quotas_listUsagesMachineLearningServices
      azure_rm_quota_info: 
        location: eastus
        provider_id: Microsoft.MachineLearningServices
        

'''

RETURN = '''
quota:
  description: >-
    A list of dict results where the key is the name of the Quota and the values
    are the facts for that Quota.
  returned: always
  type: complex
  contains:
    limit:
      description:
        - The quota limit.
      returned: always
      type: integer
      sample: null
    current_value:
      description:
        - The current resource usages information.
      returned: always
      type: integer
      sample: null
    unit:
      description:
        - ' The units of the limit, such as - Count, Bytes, etc. Use the unit field provided in the Get quota response.'
      returned: always
      type: str
      sample: null
    resource_type:
      description:
        - The Resource Type Name.
      returned: always
      type: str
      sample: null
    quota_period:
      description:
        - >-
          The quota period over which the usage values are summarized, such as -
          P1D (Per one day), PT1M (Per one minute), PT1S (Per one second). This
          parameter is optional because, for some resources like compute, the
          period doesn’t matter.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Additional properties for the specific resource provider.
      returned: always
      type: any
      sample: null
    value:
      description:
        - |-
          Resource name.
          List of Quota limits.
      returned: always
      type: str
      sample: null
    localized_value:
      description:
        - Resource display name.
      returned: always
      type: str
      sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of quota limits. When there are no more
          pages, this is null.
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
    from azure.mgmt.azure import Azure Reservation API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMQuotaInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            provider_id=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.provider_id = None
        self.location = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-19-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMQuotaInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Reservation API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-19-preview')

        if (self.provider_id is not None and
            self.location is not None and
            self.resource_name is not None):
            self.results['quota'] = self.format_item(self.get())
        elif (self.provider_id is not None and
              self.location is not None):
            self.results['quota'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.quota.get(provider_id=self.provider_id,
                                                  location=self.location,
                                                  resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.quota.list(provider_id=self.provider_id,
                                                   location=self.location)
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
    AzureRMQuotaInfo()


if __name__ == '__main__':
    main()
