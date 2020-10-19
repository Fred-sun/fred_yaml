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
module: azure_rm_workspacecollection
version_added: '2.9'
short_description: Manage Azure WorkspaceCollection instance.
description:
  - 'Create, update and delete instance of Azure WorkspaceCollection.'
options:
  resource_group_name:
    description:
      - Azure resource group
    required: true
    type: str
  workspace_collection_name:
    description:
      - Power BI Embedded Workspace Collection name
    required: true
    type: str
  location:
    description:
      - Azure location
    type: str
  sku:
    description:
      - undefined
    type: dict
    suboptions:
      name:
        description:
          - SKU name
        required: true
        type: str
        choices:
          - S1
      tier:
        description:
          - SKU tier
        required: true
        type: str
        choices:
          - Standard
  state:
    description:
      - Assert the state of the WorkspaceCollection.
      - >-
        Use C(present) to create or update an WorkspaceCollection and C(absent)
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
'''

RETURN = '''
id:
  description:
    - Resource id
  returned: always
  type: str
  sample: null
name:
  description:
    - Workspace collection name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Azure location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Dictionary of <string>
  returned: always
  type: dictionary
  sample: null
sku:
  description:
    - ''
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - SKU name
      returned: always
      type: str
      sample: null
    tier:
      description:
        - SKU tier
      returned: always
      type: str
      sample: null
properties:
  description:
    - Properties
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
    from azure.mgmt.power import Power BI Embedded Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMWorkspaceCollection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_collection_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['S1'],
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier',
                        choices=['Standard'],
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.workspace_collection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMWorkspaceCollection, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Power BI Embedded Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-01-29')

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
                response = self.mgmt_client.workspace_collections.create(resource_group_name=self.resource_group_name,
                                                                         workspace_collection_name=self.workspace_collection_name,
                                                                         body=self.body)
            else:
                response = self.mgmt_client.workspace_collections.update(resource_group_name=self.resource_group_name,
                                                                         workspace_collection_name=self.workspace_collection_name,
                                                                         body=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the WorkspaceCollection instance.')
            self.fail('Error creating the WorkspaceCollection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.workspace_collections.delete(resource_group_name=self.resource_group_name,
                                                                     workspace_collection_name=self.workspace_collection_name)
        except CloudError as e:
            self.log('Error attempting to delete the WorkspaceCollection instance.')
            self.fail('Error deleting the WorkspaceCollection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.workspace_collections.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMWorkspaceCollection()


if __name__ == '__main__':
    main()
