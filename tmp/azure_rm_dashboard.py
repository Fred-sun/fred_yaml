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
module: azure_rm_dashboard
version_added: '2.9'
short_description: Manage Azure Dashboard instance.
description:
  - 'Create, update and delete instance of Azure Dashboard.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  dashboard_name:
    description:
      - The name of the dashboard.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  lenses:
    description:
      - The dashboard lenses.
    type: list
  metadata:
    description:
      - The dashboard metadata.
    type: dictionary
  state:
    description:
      - Assert the state of the Dashboard.
      - >-
        Use C(present) to create or update an Dashboard and C(absent) to delete
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
    - name: Create or update a Dashboard
      azure_rm_dashboard: 
        dashboard_name: testDashboard
        resource_group_name: testRG
        location: eastus
        properties:
          lenses:
            - order: 1
              parts:
                - position:
                    col_span: 3
                    row_span: 4
                    x: 1
                    'y': 2
                - position:
                    col_span: 6
                    row_span: 6
                    x: 5
                    'y': 5
            - order: 2
              parts: []
          metadata:
            metadata:
              col_span: 2
              row_span: 1
              x: 4
              'y': 3
        tags:
          a_key: aValue
          another_key: anotherValue
        

    - name: Delete a Dashboard
      azure_rm_dashboard: 
        dashboard_name: testDashboard
        resource_group_name: testRG
        

    - name: Update a Dashboard
      azure_rm_dashboard: 
        dashboard_name: testDashboard
        resource_group_name: testRG
        tags:
          a_key: bValue
          another_key: anotherValue2
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
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
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
lenses:
  description:
    - The dashboard lenses.
  returned: always
  type: list
  sample: null
metadata:
  description:
    - The dashboard metadata.
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
    from azure.mgmt.portal import portal
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDashboard(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            dashboard_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            lenses=dict(
                type='list',
                disposition='/lenses',
                elements='any'
            ),
            metadata=dict(
                type='dictionary',
                disposition='/metadata'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.dashboard_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDashboard, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(portal,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

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
            response = self.mgmt_client.dashboards.create_or_update(resource_group_name=self.resource_group_name,
                                                                    dashboard_name=self.dashboard_name,
                                                                    dashboard=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Dashboard instance.')
            self.fail('Error creating the Dashboard instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dashboards.delete(resource_group_name=self.resource_group_name,
                                                          dashboard_name=self.dashboard_name)
        except CloudError as e:
            self.log('Error attempting to delete the Dashboard instance.')
            self.fail('Error deleting the Dashboard instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dashboards.get(resource_group_name=self.resource_group_name,
                                                       dashboard_name=self.dashboard_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDashboard()


if __name__ == '__main__':
    main()
