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
module: azure_rm_userassignedidentity
version_added: '2.9'
short_description: Manage Azure UserAssignedIdentity instance.
description:
  - 'Create, update and delete instance of Azure UserAssignedIdentity.'
options:
  resource_group_name:
    description:
      - The name of the Resource Group to which the identity belongs.
    required: true
    type: str
  resource_name:
    description:
      - The name of the identity resource.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  state:
    description:
      - Assert the state of the UserAssignedIdentity.
      - >-
        Use C(present) to create or update an UserAssignedIdentity and C(absent)
        to delete it.
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
    - name: IdentityCreate
      azure_rm_userassignedidentity: 
        resource_group_name: rgName
        resource_name: resourceName
        location: eastus
        tags:
          key1: value1
          key2: value2
        

    - name: IdentityUpdate
      azure_rm_userassignedidentity: 
        resource_group_name: rgName
        resource_name: resourceName
        location: eastus
        tags:
          key1: value1
          key2: value2
        

    - name: IdentityDelete
      azure_rm_userassignedidentity: 
        resource_group_name: rgName
        resource_name: resourceName
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - The id of the tenant which the identity belongs to.
  returned: always
  type: uuid
  sample: null
principal_id:
  description:
    - >-
      The id of the service principal object associated with the created
      identity.
  returned: always
  type: uuid
  sample: null
client_id:
  description:
    - >-
      The id of the app associated with the identity. This is a random generated
      UUID by MSI.
  returned: always
  type: uuid
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedServiceIdentityClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMUserAssignedIdentity(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMUserAssignedIdentity, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ManagedServiceIdentityClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-30')

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
            response = self.mgmt_client.user_assigned_identities.create_or_update(resource_group_name=self.resource_group_name,
                                                                                  resource_name=self.resource_name,
                                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the UserAssignedIdentity instance.')
            self.fail('Error creating the UserAssignedIdentity instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.user_assigned_identities.delete(resource_group_name=self.resource_group_name,
                                                                        resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the UserAssignedIdentity instance.')
            self.fail('Error deleting the UserAssignedIdentity instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.user_assigned_identities.get(resource_group_name=self.resource_group_name,
                                                                     resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMUserAssignedIdentity()


if __name__ == '__main__':
    main()
