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
module: azure_rm_trigger
version_added: '2.9'
short_description: Manage Azure Trigger instance.
description:
  - 'Create, update and delete instance of Azure Trigger.'
options:
  device_name:
    description:
      - The device name.
      - Creates or updates a trigger
    required: true
    type: str
  name:
    description:
      - The trigger name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  trigger:
    description:
      - The trigger.
    type: dict
    suboptions:
      kind:
        description:
          - Trigger Kind.
        required: true
        type: str
        choices:
          - FileEvent
          - PeriodicTimerEvent
  state:
    description:
      - Assert the state of the Trigger.
      - >-
        Use C(present) to create or update an Trigger and C(absent) to delete
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
    - name: TriggerPut
      azure_rm_trigger: 
        name: trigger1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        trigger:
          kind: FileEvent
          properties:
            custom_context_tag: CustomContextTags-1235346475
            sink_info:
              role_id: >-
                /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/GroupForEdgeAutomation/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/testedgedevice/roles/role1
            source_info:
              share_id: >-
                /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/GroupForEdgeAutomation/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/testedgedevice/shares/share1
        

    - name: TriggerDelete
      azure_rm_trigger: 
        name: trigger1
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The object name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
kind:
  description:
    - Trigger Kind.
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
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTrigger(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            trigger=dict(
                type='dict',
                disposition='/trigger',
                options=dict(
                    kind=dict(
                        type='str',
                        disposition='kind',
                        choices=['FileEvent',
                                 'PeriodicTimerEvent'],
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

        self.device_name = None
        self.name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTrigger, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

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
            response = self.mgmt_client.triggers.create_or_update(device_name=self.device_name,
                                                                  name=self.name,
                                                                  resource_group_name=self.resource_group_name,
                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Trigger instance.')
            self.fail('Error creating the Trigger instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.triggers.delete(device_name=self.device_name,
                                                        name=self.name,
                                                        resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Trigger instance.')
            self.fail('Error deleting the Trigger instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.triggers.get(device_name=self.device_name,
                                                     name=self.name,
                                                     resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTrigger()


if __name__ == '__main__':
    main()
