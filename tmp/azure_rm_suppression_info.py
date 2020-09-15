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
module: azure_rm_suppression_info
version_added: '2.9'
short_description: Get Suppression info.
description:
  - Get info of Suppression.
options:
  resource_uri:
    description:
      - >-
        The fully qualified Azure Resource Manager identifier of the resource to
        which the recommendation applies.
    type: str
  recommendation_id:
    description:
      - The recommendation ID.
    type: str
  name:
    description:
      - The name of the suppression.
    type: str
  top:
    description:
      - >-
        The number of suppressions per page if a paged version of this API is
        being used.
    type: integer
  skip_token:
    description:
      - The page-continuation token to use with a paged version of this API.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetSuppressionDetail
      azure_rm_suppression_info: 
        name: suppressionName1
        recommendation_id: recommendationId
        resource_uri: resourceUri
        

    - name: ListSuppressions
      azure_rm_suppression_info: 
        {}
        

'''

RETURN = '''
suppressions:
  description: >-
    A list of dict results where the key is the name of the Suppression and the
    values are the facts for that Suppression.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    suppression_id:
      description:
        - The GUID of the suppression.
      returned: always
      type: str
      sample: null
    ttl:
      description:
        - The duration for which the suppression is valid.
      returned: always
      type: str
      sample: null
    next_link:
      description:
        - The link used to get the next page of suppressions.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of suppressions.
      returned: always
      type: list
      sample: null
      contains:
        suppression_id:
          description:
            - The GUID of the suppression.
          returned: always
          type: str
          sample: null
        ttl:
          description:
            - The duration for which the suppression is valid.
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
    from azure.mgmt.advisor import AdvisorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSuppressionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str'
            ),
            recommendation_id=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip_token=dict(
                type='str'
            )
        )

        self.resource_uri = None
        self.recommendation_id = None
        self.name = None
        self.top = None
        self.skip_token = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSuppressionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AdvisorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_uri is not None and
            self.recommendation_id is not None and
            self.name is not None):
            self.results['suppressions'] = self.format_item(self.get())
        else:
            self.results['suppressions'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.suppressions.get(resource_uri=self.resource_uri,
                                                         recommendation_id=self.recommendation_id,
                                                         name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.suppressions.list(top=self.top,
                                                          skip_token=self.skip_token)
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
    AzureRMSuppressionInfo()


if __name__ == '__main__':
    main()
