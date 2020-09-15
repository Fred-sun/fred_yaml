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
module: azure_rm_communication
version_added: '2.9'
short_description: Manage Azure Communication instance.
description:
  - 'Create, update and delete instance of Azure Communication.'
options:
  support_ticket_name:
    description:
      - Support ticket name.
    required: true
    type: str
  communication_name:
    description:
      - Communication name.
    required: true
    type: str
  sender:
    description:
      - >-
        Email address of the sender. This property is required if called by a
        service principal.
    type: str
  subject:
    description:
      - Subject of the communication.
    type: str
  body:
    description:
      - Body of the communication.
    type: str
  state:
    description:
      - Assert the state of the Communication.
      - >-
        Use C(present) to create or update an Communication and C(absent) to
        delete it.
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
    - name: AddCommunicationToSubscriptionTicket
      azure_rm_communication: 
        communication_name: testcommunication
        support_ticket_name: testticket
        

'''

RETURN = '''
id:
  description:
    - Id of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of the resource 'Microsoft.Support/communications'.
  returned: always
  type: str
  sample: null
communication_type:
  description:
    - Communication type.
  returned: always
  type: str
  sample: null
communication_direction:
  description:
    - Direction of communication.
  returned: always
  type: str
  sample: null
sender:
  description:
    - >-
      Email address of the sender. This property is required if called by a
      service principal.
  returned: always
  type: str
  sample: null
subject:
  description:
    - Subject of the communication.
  returned: always
  type: str
  sample: null
body:
  description:
    - Body of the communication.
  returned: always
  type: str
  sample: null
created_date:
  description:
    - Time in UTC (ISO 8601 format) when the communication was created.
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
    from azure.mgmt.microsoft.support import Microsoft.Support
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCommunication(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            support_ticket_name=dict(
                type='str',
                required=True
            ),
            communication_name=dict(
                type='str',
                required=True
            ),
            sender=dict(
                type='str',
                disposition='/sender'
            ),
            subject=dict(
                type='str',
                disposition='/subject'
            ),
            body=dict(
                type='str',
                disposition='/body'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.support_ticket_name = None
        self.communication_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCommunication, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.Support,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

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
                response = self.mgmt_client.communications.create(support_ticket_name=self.support_ticket_name,
                                                                  communication_name=self.communication_name,
                                                                  create_communication_parameters=self.body)
            else:
                response = self.mgmt_client.communications.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Communication instance.')
            self.fail('Error creating the Communication instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.communications.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Communication instance.')
            self.fail('Error deleting the Communication instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.communications.get(support_ticket_name=self.support_ticket_name,
                                                           communication_name=self.communication_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCommunication()


if __name__ == '__main__':
    main()
