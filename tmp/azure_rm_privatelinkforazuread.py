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
module: azure_rm_privatelinkforazuread
version_added: '2.9'
short_description: Manage Azure privateLinkForAzureAd instance.
description:
  - 'Create, update and delete instance of Azure privateLinkForAzureAd.'
options:
  resource_group_name:
    description:
      - Name of an Azure resource group.
    required: true
    type: str
  policy_name:
    description:
      - The name of the private link policy in Azure AD.
    required: true
    type: str
  name:
    description:
      - Name of this resource.
    type: str
  owner_tenant_id:
    description:
      - Guid of the owner tenant
    type: str
  all_tenants:
    description:
      - Flag indicating whether all tenants are allowed
    type: bool
  tenants:
    description:
      - The list of tenantIds.
    type: list
  resource_name:
    description:
      - Name of the private link policy resource
    type: str
  resource_group:
    description:
      - Name of the resource group
    type: str
  state:
    description:
      - Assert the state of the privateLinkForAzureAd.
      - >-
        Use C(present) to create or update an privateLinkForAzureAd and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: privateLinkPolicyCreate
      azure_rm_privatelinkforazuread: 
        policy_name: ddb1
        resource_group_name: rg1
        

    - name: privateLinkPolicyMinCreate
      azure_rm_privatelinkforazuread: 
        policy_name: ddb1
        resource_group_name: rg1
        

    - name: privateLinkPolicyUpdate
      azure_rm_privatelinkforazuread: 
        policy_name: ddb1
        resource_group_name: rg1
        

    - name: privateLinkPolicyDelete
      azure_rm_privatelinkforazuread: 
        policy_name: ddb1
        resource_group_name: rg1
        

'''

RETURN = '''
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azureactivedirectory import azureactivedirectory
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMprivateLinkForAzureAd(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            policy_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            owner_tenant_id=dict(
                type='str',
                disposition='/owner_tenant_id'
            ),
            all_tenants=dict(
                type='bool',
                disposition='/all_tenants'
            ),
            tenants=dict(
                type='list',
                disposition='/tenants',
                elements='str'
            ),
            resource_name=dict(
                type='str',
                disposition='/resource_name'
            ),
            resource_group=dict(
                type='str',
                disposition='/resource_group'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMprivateLinkForAzureAd, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                           supports_check_mode=True,
                                                           supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(azureactivedirectory,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01-preview')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.private_link_for_azure_ad.create(resource_group_name=self.resource_group_name,
                                                                             policy_name=self.policy_name,
                                                                             private_link_policy=self.body)
            else:
                response = self.mgmt_client.private_link_for_azure_ad.update(resource_group_name=self.resource_group_name,
                                                                             policy_name=self.policy_name,
                                                                             private_link_policy=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the privateLinkForAzureAd instance.')
            self.fail('Error creating the privateLinkForAzureAd instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.private_link_for_azure_ad.delete(resource_group_name=self.resource_group_name,
                                                                         policy_name=self.policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the privateLinkForAzureAd instance.')
            self.fail('Error deleting the privateLinkForAzureAd instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.private_link_for_azure_ad.get(resource_group_name=self.resource_group_name,
                                                                      policy_name=self.policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMprivateLinkForAzureAd()


if __name__ == '__main__':
    main()
