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
module: azure_rm_scopemap
version_added: '2.9'
short_description: Manage Azure ScopeMap instance.
description:
  - 'Create, update and delete instance of Azure ScopeMap.'
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  registry_name:
    description:
      - The name of the container registry.
    required: true
    type: str
  scope_map_name:
    description:
      - The name of the scope map.
    required: true
    type: str
  description:
    description:
      - The user friendly description of the scope map.
    type: str
  actions:
    description:
      - "The list of scoped permissions for registry artifacts.\r"
      - "E.g. repositories/repository-name/content/read,\r"
      - repositories/repository-name/metadata/write
      - "The list of scope permissions for registry artifacts.\r"
      - "E.g. repositories/repository-name/pull, \r"
      - repositories/repository-name/delete
    type: list
  state:
    description:
      - Assert the state of the ScopeMap.
      - >-
        Use C(present) to create or update an ScopeMap and C(absent) to delete
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
    - name: ScopeMapCreate
      azure_rm_scopemap: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        scope_map_name: myScopeMap
        

    - name: ScopeMapDelete
      azure_rm_scopemap: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        scope_map_name: myScopeMap
        

    - name: ScopeMapUpdate
      azure_rm_scopemap: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        scope_map_name: myScopeMap
        

'''

RETURN = '''
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
description:
  description:
    - The user friendly description of the scope map.
  returned: always
  type: str
  sample: null
type_properties_type:
  description:
    - The type of the scope map. E.g. BuildIn scope map.
  returned: always
  type: str
  sample: null
creation_date:
  description:
    - The creation date of scope map.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state of the resource.
  returned: always
  type: str
  sample: null
actions:
  description:
    - "The list of scoped permissions for registry artifacts.\r\nE.g. repositories/repository-name/content/read,\r\nrepositories/repository-name/metadata/write"
  returned: always
  type: list
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMScopeMap(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            scope_map_name=dict(
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            actions=dict(
                type='list',
                disposition='/actions',
                elements='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.scope_map_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMScopeMap, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-05-01-preview')

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
                response = self.mgmt_client.scope_maps.create(resource_group_name=self.resource_group_name,
                                                              registry_name=self.registry_name,
                                                              scope_map_name=self.scope_map_name,
                                                              scope_map_create_parameters=self.body)
            else:
                response = self.mgmt_client.scope_maps.update(resource_group_name=self.resource_group_name,
                                                              registry_name=self.registry_name,
                                                              scope_map_name=self.scope_map_name,
                                                              scope_map_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ScopeMap instance.')
            self.fail('Error creating the ScopeMap instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.scope_maps.delete(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name,
                                                          scope_map_name=self.scope_map_name)
        except CloudError as e:
            self.log('Error attempting to delete the ScopeMap instance.')
            self.fail('Error deleting the ScopeMap instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.scope_maps.get(resource_group_name=self.resource_group_name,
                                                       registry_name=self.registry_name,
                                                       scope_map_name=self.scope_map_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMScopeMap()


if __name__ == '__main__':
    main()
