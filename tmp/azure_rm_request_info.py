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
module: azure_rm_request_info
version_added: '2.9'
short_description: Get Request info.
description:
  - Get info of Request.
options:
  request_id:
    description:
      - The Lockbox request ID.
    type: str
  filter:
    description:
      - >-
        The $filter OData query parameter. Only filter by request status is
        supported, e.g $filter=properties/status eq 'Pending'
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a lockbox request in subscription scope
      azure_rm_request_info: 
        request_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        

    - name: List lockbox requests in a subscription with filter by request status (eg. $filter=properties/status eq 'Pending')
      azure_rm_request_info: 
        {}
        

    - name: List lockbox requests with no filters
      azure_rm_request_info: 
        {}
        

'''

RETURN = '''
requests:
  description: >-
    A list of dict results where the key is the name of the Request and the
    values are the facts for that Request.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The Arm resource id of the Lockbox request.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the Lockbox request.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the Lockbox request.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - The properties that are associated with a lockbox request.
      returned: always
      type: dict
      sample: null
      contains:
        request_id:
          description:
            - The Lockbox request ID.
          returned: always
          type: str
          sample: null
        justification:
          description:
            - The justification of the requestor.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The status of the request.
          returned: always
          type: str
          sample: null
        created_date_time:
          description:
            - The creation time of the request.
          returned: always
          type: str
          sample: null
        expiration_date_time:
          description:
            - The expiration time of the request.
          returned: always
          type: str
          sample: null
        duration:
          description:
            - The duration of the request in hours.
          returned: always
          type: integer
          sample: null
        requested_resource_ids:
          description:
            - >-
              A list of resource IDs associated with the Lockbox request
              separated by ','.
          returned: always
          type: list
          sample: null
        resource_type:
          description:
            - The resource type of the requested resources.
          returned: always
          type: str
          sample: null
        support_request:
          description:
            - The id of the support request associated.
          returned: always
          type: str
          sample: null
        support_case_url:
          description:
            - The url of the support case.
          returned: always
          type: str
          sample: null
        subscription_id:
          description:
            - The subscription ID.
          returned: always
          type: str
          sample: null
    value:
      description:
        - A list of Lockbox requests. Populated by a 'List' operation.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The Arm resource id of the Lockbox request.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the Lockbox request.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the Lockbox request.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The properties that are associated with a lockbox request.
          returned: always
          type: dict
          sample: null
          contains:
            request_id:
              description:
                - The Lockbox request ID.
              returned: always
              type: str
              sample: null
            justification:
              description:
                - The justification of the requestor.
              returned: always
              type: str
              sample: null
            status:
              description:
                - The status of the request.
              returned: always
              type: str
              sample: null
            created_date_time:
              description:
                - The creation time of the request.
              returned: always
              type: str
              sample: null
            expiration_date_time:
              description:
                - The expiration time of the request.
              returned: always
              type: str
              sample: null
            duration:
              description:
                - The duration of the request in hours.
              returned: always
              type: integer
              sample: null
            requested_resource_ids:
              description:
                - >-
                  A list of resource IDs associated with the Lockbox request
                  separated by ','.
              returned: always
              type: list
              sample: null
            resource_type:
              description:
                - The resource type of the requested resources.
              returned: always
              type: str
              sample: null
            support_request:
              description:
                - The id of the support request associated.
              returned: always
              type: str
              sample: null
            support_case_url:
              description:
                - The url of the support case.
              returned: always
              type: str
              sample: null
            subscription_id:
              description:
                - The subscription ID.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - URL to get the next set of operation list results if there are any.
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
    from azure.mgmt.customer import Customer Lockbox
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRequestInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            request_id=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.request_id = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-02-28-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRequestInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Customer Lockbox,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-02-28-preview')

        if (self.request_id is not None):
            self.results['requests'] = self.format_item(self.get())
        else:
            self.results['requests'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.requests.get(request_id=self.request_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.requests.list(filter=self.filter)
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
    AzureRMRequestInfo()


if __name__ == '__main__':
    main()
