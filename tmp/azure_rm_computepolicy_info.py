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
module: azure_rm_computepolicy_info
version_added: '2.9'
short_description: Get ComputePolicy info.
description:
  - Get info of ComputePolicy.
options:
  resource_group_name:
    description:
      - The name of the Azure resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the Data Lake Analytics account.
    required: true
    type: str
  compute_policy_name:
    description:
      - The name of the compute policy to retrieve.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists the compute policies within the adla account
      azure_rm_computepolicy_info: 
        account_name: contosoadla
        resource_group_name: contosorg
        

    - name: Gets the specified compute policy
      azure_rm_computepolicy_info: 
        account_name: contosoadla
        compute_policy_name: test_policy
        resource_group_name: contosorg
        

'''

RETURN = '''
compute_policies:
  description: >-
    A list of dict results where the key is the name of the ComputePolicy and
    the values are the facts for that ComputePolicy.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        object_id:
          description:
            - The AAD object identifier for the entity to create a policy for.
          returned: always
          type: uuid
          sample: null
        object_type:
          description:
            - The type of AAD object the object identifier refers to.
          returned: always
          type: str
          sample: null
        max_degree_of_parallelism_per_job:
          description:
            - >-
              The maximum degree of parallelism per job this user can use to
              submit jobs.
          returned: always
          type: integer
          sample: null
        min_priority_per_job:
          description:
            - The minimum priority per job this user can use to submit jobs.
          returned: always
          type: integer
          sample: null
    next_link:
      description:
        - The link (url) to the next page of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The resource identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The resource type.
      returned: always
      type: str
      sample: null
    object_id:
      description:
        - The AAD object identifier for the entity to create a policy for.
      returned: always
      type: uuid
      sample: null
    object_type:
      description:
        - The type of AAD object the object identifier refers to.
      returned: always
      type: str
      sample: null
    max_degree_of_parallelism_per_job:
      description:
        - >-
          The maximum degree of parallelism per job this user can use to submit
          jobs.
      returned: always
      type: integer
      sample: null
    min_priority_per_job:
      description:
        - The minimum priority per job this user can use to submit jobs.
      returned: always
      type: integer
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataLakeAnalyticsAccountManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMComputePolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            compute_policy_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.compute_policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMComputePolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataLakeAnalyticsAccountManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-11-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.compute_policy_name is not None):
            self.results['compute_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['compute_policies'] = self.format_item(self.listbyaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.compute_policies.get(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name,
                                                             compute_policy_name=self.compute_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyaccount(self):
        response = None

        try:
            response = self.mgmt_client.compute_policies.list_by_account(resource_group_name=self.resource_group_name,
                                                                         account_name=self.account_name)
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
    AzureRMComputePolicyInfo()


if __name__ == '__main__':
    main()
