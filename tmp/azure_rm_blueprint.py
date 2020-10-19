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
module: azure_rm_blueprint
version_added: '2.9'
short_description: Manage Azure Blueprint instance.
description:
  - 'Create, update and delete instance of Azure Blueprint.'
options:
  resource_scope:
    description:
      - >-
        The scope of the resource. Valid scopes are: management group (format:
        '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
        subscription (format: '/subscriptions/{subscriptionId}').
    required: true
    type: str
  blueprint_name:
    description:
      - Name of the blueprint definition.
    required: true
    type: str
  display_name:
    description:
      - One-liner string explain this resource.
    type: str
  description:
    description:
      - Multi-line explain this resource.
    type: str
  target_scope:
    description:
      - The scope where this blueprint definition can be assigned.
    type: str
    choices:
      - subscription
      - managementGroup
  parameters:
    description:
      - Parameters required by this blueprint definition.
    type: dictionary
  resource_groups:
    description:
      - Resource group placeholders defined by this blueprint definition.
    type: dictionary
  versions:
    description:
      - Published versions of this blueprint definition.
    type: any
  layout:
    description:
      - Layout view of the blueprint definition for UI reference.
    type: any
  state:
    description:
      - Assert the state of the Blueprint.
      - >-
        Use C(present) to create or update an Blueprint and C(absent) to delete
        it.
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
    - name: ManagementGroupBlueprint
      azure_rm_blueprint: 
        blueprint_name: simpleBlueprint
        resource_scope: providers/Microsoft.Management/managementGroups/ContosoOnlineGroup
        properties:
          description: 'blueprint contains all artifact kinds {''template'', ''rbac'', ''policy''}'
          parameters:
            cost_center:
              type: string
              metadata:
                display_name: force cost center tag for all resources under given subscription.
            owners:
              type: array
              metadata:
                display_name: assign owners to subscription along with blueprint assignment.
            storage_account_type:
              type: string
              metadata:
                display_name: storage account type.
          resource_groups:
            storage_rg:
              metadata:
                description: Contains storageAccounts that collect all shoebox logs.
                display_name: storage resource group
          target_scope: subscription
        

    - name: ResourceGroupWithTags
      azure_rm_blueprint: 
        blueprint_name: simpleBlueprint
        resource_scope: 'providers/Microsoft.Management/managementGroups/{ManagementGroupId}'
        properties:
          description: An example blueprint containing an RG with two tags.
          resource_groups:
            my_rgname:
              name: myRGName
              location: westus
              metadata:
                display_name: My Resource Group
              tags:
                costcenter: '123456'
                name_only_tag: ''
          target_scope: subscription
        

    - name: SubscriptionBlueprint
      azure_rm_blueprint: 
        blueprint_name: simpleBlueprint
        resource_scope: subscriptions/00000000-0000-0000-0000-000000000000
        properties:
          description: 'blueprint contains all artifact kinds {''template'', ''rbac'', ''policy''}'
          parameters:
            cost_center:
              type: string
              metadata:
                display_name: force cost center tag for all resources under given subscription.
            owners:
              type: array
              metadata:
                display_name: assign owners to subscription along with blueprint assignment.
            storage_account_type:
              type: string
              metadata:
                display_name: storage account type.
          resource_groups:
            storage_rg:
              metadata:
                description: Contains storageAccounts that collect all shoebox logs.
                display_name: storage resource group
          target_scope: subscription
        

'''

RETURN = '''
id:
  description:
    - String Id used to locate any resource on Azure.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of this resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of this resource.
  returned: always
  type: str
  sample: null
display_name:
  description:
    - One-liner string explain this resource.
  returned: always
  type: str
  sample: null
description:
  description:
    - Multi-line explain this resource.
  returned: always
  type: str
  sample: null
status:
  description:
    - Status of the blueprint. This field is readonly.
  returned: always
  type: dict
  sample: null
  contains:
    time_created:
      description:
        - Creation time of this blueprint definition.
      returned: always
      type: str
      sample: null
    last_modified:
      description:
        - Last modified time of this blueprint definition.
      returned: always
      type: str
      sample: null
target_scope:
  description:
    - The scope where this blueprint definition can be assigned.
  returned: always
  type: str
  sample: null
parameters:
  description:
    - Parameters required by this blueprint definition.
  returned: always
  type: dictionary
  sample: null
resource_groups:
  description:
    - Resource group placeholders defined by this blueprint definition.
  returned: always
  type: dictionary
  sample: null
versions:
  description:
    - Published versions of this blueprint definition.
  returned: always
  type: any
  sample: null
layout:
  description:
    - Layout view of the blueprint definition for UI reference.
  returned: always
  type: any
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.blueprint import BlueprintManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBlueprint(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_scope=dict(
                type='str',
                required=True
            ),
            blueprint_name=dict(
                type='str',
                required=True
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            target_scope=dict(
                type='str',
                disposition='/target_scope',
                choices=['subscription',
                         'managementGroup']
            ),
            parameters=dict(
                type='dictionary',
                disposition='/parameters'
            ),
            resource_groups=dict(
                type='dictionary',
                disposition='/resource_groups'
            ),
            versions=dict(
                type='any',
                disposition='/versions'
            ),
            layout=dict(
                type='any',
                disposition='/layout'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_scope = None
        self.blueprint_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBlueprint, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(BlueprintManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-01-preview')

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
            response = self.mgmt_client.blueprints.create_or_update(resource_scope=self.resource_scope,
                                                                    blueprint_name=self.blueprint_name,
                                                                    blueprint=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Blueprint instance.')
            self.fail('Error creating the Blueprint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.blueprints.delete(resource_scope=self.resource_scope,
                                                          blueprint_name=self.blueprint_name)
        except CloudError as e:
            self.log('Error attempting to delete the Blueprint instance.')
            self.fail('Error deleting the Blueprint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.blueprints.get(resource_scope=self.resource_scope,
                                                       blueprint_name=self.blueprint_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBlueprint()


if __name__ == '__main__':
    main()
