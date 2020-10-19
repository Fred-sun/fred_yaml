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
module: azure_rm_quotarequeststatu_info
version_added: '2.9'
short_description: Get QuotaRequestStatu info.
description:
  - Get info of QuotaRequestStatu.
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
  id:
    description:
      - Quota Request id.
    type: str
  filter:
    description:
      - '| Field                    | Supported operators  '
      - '|---------------------|------------------------'
      - "\r"
      - '|requestSubmitTime | ge, le, eq, gt, lt'
      - ''
    type: str
  top:
    description:
      - Number of records to return.
    type: integer
  skiptoken:
    description:
      - >-
        Skiptoken is only used if a previous operation returned a partial
        result. If a previous response contains a nextLink element, the value of
        the nextLink element will include a skiptoken parameter that specifies a
        starting point to use for subsequent calls
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: QuotaRequestFailed
      azure_rm_quotarequeststatu_info: 
        id: 2B5C8515-37D8-4B6A-879B-CD641A2CF605
        location: eastus
        provider_id: Microsoft.Compute
        

    - name: QuotaRequestInProgress
      azure_rm_quotarequeststatu_info: 
        id: 2B5C8515-37D8-4B6A-879B-CD641A2CF605
        location: eastus
        provider_id: Microsoft.Compute
        

    - name: QuotaRequestStatus
      azure_rm_quotarequeststatu_info: 
        id: 2B5C8515-37D8-4B6A-879B-CD641A2CF605
        location: eastus
        provider_id: Microsoft.Compute
        

    - name: QuotaRequestHistory
      azure_rm_quotarequeststatu_info: 
        location: eastus
        provider_id: Microsoft.Compute
        

'''

RETURN = '''
quota_request_status:
  description: >-
    A list of dict results where the key is the name of the QuotaRequestStatu
    and the values are the facts for that QuotaRequestStatu.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The quota request Id.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the quota request.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of resource. "Microsoft.Capacity/ServiceLimits"
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The quota request status.
      returned: always
      type: str
      sample: null
    message:
      description:
        - User friendly status message.
      returned: always
      type: str
      sample: null
    request_submit_time:
      description:
        - >-
          The quota request submit time. The date conforms to the following
          format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard.
      returned: always
      type: str
      sample: null
    value:
      description:
        - |-
          The quotaRequests.
          The quota Requests.
      returned: always
      type: list
      sample: null
      contains:
        limit:
          description:
            - The Resource limit.
          returned: always
          type: integer
          sample: null
        name:
          description:
            - The Resource name.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - Resource name.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - Resource display name.
              returned: always
              type: str
              sample: null
        resource_type:
          description:
            - Resource type for which the quota check was made.
          returned: always
          type: str
          sample: null
        unit:
          description:
            - ' The units of the limit, such as - Count, Bytes, etc. Use the unit field provided in the Get quota response.'
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The quota request status.
          returned: always
          type: str
          sample: null
        message:
          description:
            - User friendly status message.
          returned: always
          type: str
          sample: null
        sub_request_id:
          description:
            - Sub request id for individual request.
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


class AzureRMQuotaRequestStatuInfo(AzureRMModuleBase):
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
            id=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skiptoken=dict(
                type='str'
            )
        )

        self.provider_id = None
        self.location = None
        self.id = None
        self.filter = None
        self.top = None
        self.skiptoken = None

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
        super(AzureRMQuotaRequestStatuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Reservation API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-19-preview')

        if (self.provider_id is not None and
            self.location is not None and
            self.id is not None):
            self.results['quota_request_status'] = self.format_item(self.get())
        elif (self.provider_id is not None and
              self.location is not None):
            self.results['quota_request_status'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.quota_request_status.get(provider_id=self.provider_id,
                                                                 location=self.location,
                                                                 id=self.id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.quota_request_status.list(provider_id=self.provider_id,
                                                                  location=self.location,
                                                                  filter=self.filter,
                                                                  top=self.top,
                                                                  skiptoken=self.skiptoken)
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
    AzureRMQuotaRequestStatuInfo()


if __name__ == '__main__':
    main()
