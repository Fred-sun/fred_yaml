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
module: azure_rm_privatelinkforazuread_info
version_added: '2.9'
short_description: Get privateLinkForAzureAd info.
description:
  - Get info of privateLinkForAzureAd.
options:
  resource_group_name:
    description:
      - Name of an Azure resource group.
    type: str
  policy_name:
    description:
      - The name of the private link policy in Azure AD.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: privateLinkPolicyGet
      azure_rm_privatelinkforazuread_info: 
        policy_name: ddb1
        resource_group_name: rg1
        

    - name: privateLinkPolicyListBySubscription
      azure_rm_privatelinkforazuread_info: 
        {}
        

    - name: privateLinkPolicyGetList
      azure_rm_privatelinkforazuread_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
private_link_for_azure_ad:
  description: >-
    A list of dict results where the key is the name of the
    privateLinkForAzureAd and the values are the facts for that
    privateLinkForAzureAd.
  returned: always
  type: complex
  contains:
    id:
      description:
        - String Id used to locate any resource on Azure.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of this resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of this resource.
      returned: always
      type: str
      sample: null
    owner_tenant_id:
      description:
        - Guid of the owner tenant
      returned: always
      type: str
      sample: null
    all_tenants:
      description:
        - Flag indicating whether all tenants are allowed
      returned: always
      type: bool
      sample: null
    tenants:
      description:
        - The list of tenantIds.
      returned: always
      type: list
      sample: null
    resource_name:
      description:
        - Name of the private link policy resource
      returned: always
      type: str
      sample: null
    subscription_id:
      description:
        - Subscription Identifier
      returned: always
      type: str
      sample: null
    resource_group:
      description:
        - Name of the resource group
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - Array of private link policies
      returned: always
      type: list
      sample: null
      contains:
        owner_tenant_id:
          description:
            - Guid of the owner tenant
          returned: always
          type: str
          sample: null
        all_tenants:
          description:
            - Flag indicating whether all tenants are allowed
          returned: always
          type: bool
          sample: null
        tenants:
          description:
            - The list of tenantIds.
          returned: always
          type: list
          sample: null
        resource_name:
          description:
            - Name of the private link policy resource
          returned: always
          type: str
          sample: null
        subscription_id:
          description:
            - Subscription Identifier
          returned: always
          type: str
          sample: null
        resource_group:
          description:
            - Name of the resource group
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - The link used to get the next page of operations.
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
    from azure.mgmt.azureactivedirectory import azureactivedirectory
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMprivateLinkForAzureAdInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            policy_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMprivateLinkForAzureAdInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(azureactivedirectory,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01-preview')

        if (self.resource_group_name is not None and
            self.policy_name is not None):
            self.results['private_link_for_azure_ad'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['private_link_for_azure_ad'] = self.format_item(self.list())
        else:
            self.results['private_link_for_azure_ad'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.private_link_for_azure_ad.get(resource_group_name=self.resource_group_name,
                                                                      policy_name=self.policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.private_link_for_azure_ad.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.private_link_for_azure_ad.list_by_subscription()
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
    AzureRMprivateLinkForAzureAdInfo()


if __name__ == '__main__':
    main()
