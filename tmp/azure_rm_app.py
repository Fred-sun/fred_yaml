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
module: azure_rm_app
version_added: '2.9'
short_description: Manage Azure App instance.
description:
  - 'Create, update and delete instance of Azure App.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the IoT Central
        application.
    required: true
    type: str
  resource_name:
    description:
      - The ARM resource name of the IoT Central application.
    required: true
    type: str
  location:
    description:
      - The resource location.
    type: str
  name:
    description:
      - The name of the SKU.
    type: str
    choices:
      - F1
      - S1
      - ST0
      - ST1
      - ST2
  display_name:
    description:
      - The display name of the application.
    type: str
  subdomain:
    description:
      - The subdomain of the application.
    type: str
  template:
    description:
      - >-
        The ID of the application template, which is a blueprint that defines
        the characteristics and behaviors of an application. Optional; if not
        specified, defaults to a blank blueprint and allows the application to
        be defined from scratch.
    type: str
  state:
    description:
      - Assert the state of the App.
      - Use C(present) to create or update an App and C(absent) to delete it.
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
    - name: Apps_CreateOrUpdate
      azure_rm_app: 
        resource_group_name: resRg
        resource_name: myIoTCentralApp
        

    - name: Apps_Update
      azure_rm_app: 
        resource_group_name: resRg
        resource_name: myIoTCentralApp
        

    - name: Apps_Delete
      azure_rm_app: 
        resource_group_name: resRg
        resource_name: myIoTCentralApp
        

'''

RETURN = '''
id:
  description:
    - The ARM resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The ARM resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - The resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: dictionary
  sample: null
name_sku_name:
  description:
    - The name of the SKU.
  returned: always
  type: str
  sample: null
application_id:
  description:
    - The ID of the application.
  returned: always
  type: str
  sample: null
display_name:
  description:
    - The display name of the application.
  returned: always
  type: str
  sample: null
subdomain:
  description:
    - The subdomain of the application.
  returned: always
  type: str
  sample: null
template:
  description:
    - >-
      The ID of the application template, which is a blueprint that defines the
      characteristics and behaviors of an application. Optional; if not
      specified, defaults to a blank blueprint and allows the application to be
      defined from scratch.
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
    from azure.mgmt.iot import IotCentralClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApp(AzureRMModuleBaseExt):
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
            name=dict(
                type='str',
                disposition='/name',
                choices=['F1',
                         'S1',
                         'ST0',
                         'ST1',
                         'ST2']
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            subdomain=dict(
                type='str',
                disposition='/subdomain'
            ),
            template=dict(
                type='str',
                disposition='/template'
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

        super(AzureRMApp, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(IotCentralClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01')

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
            response = self.mgmt_client.apps.create_or_update(resource_group_name=self.resource_group_name,
                                                              resource_name=self.resource_name,
                                                              app=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the App instance.')
            self.fail('Error creating the App instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.apps.delete(resource_group_name=self.resource_group_name,
                                                    resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the App instance.')
            self.fail('Error deleting the App instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.apps.get(resource_group_name=self.resource_group_name,
                                                 resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApp()


if __name__ == '__main__':
    main()
