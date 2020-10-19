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
module: azure_rm_controller
version_added: '2.9'
short_description: Manage Azure Controller instance.
description:
  - 'Create, update and delete instance of Azure Controller.'
options:
  resource_group_name:
    description:
      - >-
        The name of the Azure Resource group of which a given DelegatedNetwork
        resource is part. This name must be at least 1 character in length, and
        no more than 90.
    required: true
    type: str
  resource_name:
    description:
      - >-
        The name of the resource. It must be a minimum of 3 characters, and a
        maximum of 63.
    required: true
    type: str
  controller_type:
    description:
      - Type of Delegated controller.
    type: str
  kubernetes_properties:
    description:
      - properties of kubernetes clusters
    type: list
    suboptions:
      server_app_id:
        description:
          - AAD ID used with apiserver
        type: str
      server_tenant_id:
        description:
          - TenantID of server App ID
        type: str
      cluster_root_ca:
        description:
          - RootCA certificate of kubernetes cluster
        type: str
      api_server_endpoint:
        description:
          - APIServer url
        type: str
  state:
    description:
      - Assert the state of the Controller.
      - >-
        Use C(present) to create or update an Controller and C(absent) to delete
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
    - name: Create controller
      azure_rm_controller: 
        resource_group_name: TestRG
        resource_name: dnctestcontroller
        

    - name: Delete controller
      azure_rm_controller: 
        resource_group_name: TestRG
        resource_name: dnctestcontroller
        

'''

RETURN = '''
id:
  description:
    - An identifier that represents the DNC controller resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the DNC controller resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the DNC controller 
      resource.(Microsoft.DelegatedNetwork/controller)
  returned: always
  type: str
  sample: null
location:
  description:
    - Location of the DNC controller resource.
  returned: always
  type: str
  sample: null
state:
  description:
    - The current state of dnc controller resource.
  returned: always
  type: str
  sample: null
type_properties_type:
  description:
    - Type of dnc controller.
  returned: always
  type: str
  sample: null
resource_guid:
  description:
    - Gets or sets resource GUID property of the controller resource.
  returned: always
  type: str
  sample: null
dnc_app_id:
  description:
    - Get controller AAD ID.
  returned: always
  type: str
  sample: null
dnc_endpoint:
  description:
    - Dnc Endpoint url.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dnc import DNC
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMController(AzureRMModuleBaseExt):
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
            controller_type=dict(
                type='str',
                disposition='/controller_type'
            ),
            kubernetes_properties=dict(
                type='list',
                disposition='/kubernetes_properties',
                elements='dict',
                options=dict(
                    server_app_id=dict(
                        type='str',
                        disposition='server_app_id'
                    ),
                    server_tenant_id=dict(
                        type='str',
                        disposition='server_tenant_id'
                    ),
                    cluster_root_ca=dict(
                        type='str',
                        disposition='cluster_root_ca'
                    ),
                    api_server_endpoint=dict(
                        type='str',
                        disposition='api_server_endpoint'
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
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMController, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DNC,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-08-preview')

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
                response = self.mgmt_client.controller.create(resource_group_name=self.resource_group_name,
                                                              resource_name=self.resource_name,
                                                              controller_parameters=self.body)
            else:
                response = self.mgmt_client.controller.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Controller instance.')
            self.fail('Error creating the Controller instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.controller.delete(resource_group_name=self.resource_group_name,
                                                          resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Controller instance.')
            self.fail('Error deleting the Controller instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.controller.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMController()


if __name__ == '__main__':
    main()
