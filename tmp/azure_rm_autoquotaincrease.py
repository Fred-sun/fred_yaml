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
module: azure_rm_autoquotaincrease
version_added: '2.9'
short_description: Manage Azure AutoQuotaIncrease instance.
description:
  - 'Create, update and delete instance of Azure AutoQuotaIncrease.'
options:
  support_ticket_action:
    description:
      - The support ticket action.
    required: true
    type: dict
    suboptions:
      severity:
        description:
          - The support request severity.
        type: str
        choices:
          - Critical
          - Moderate
          - Minimal
      first_name:
        description:
          - The first name of the recipient.
        type: str
      last_name:
        description:
          - The last name of the recipient.
        type: str
      country:
        description:
          - The country of the recipient.
        type: str
      phone_number:
        description:
          - The phone number of the recipient.
        type: str
      primary_email_address:
        description:
          - The primary email addresses of the recipients.
        type: str
      support_language:
        description:
          - The support language.
        type: str
      preferred_contact_method:
        description:
          - The preferred communication channel.
        type: str
        choices:
          - Email
          - Phone
      alternate_email_addresses:
        description:
          - The alternate email address of the recipient.
        type: list
  email_actions:
    description:
      - The email actions for auto quota increase.
    required: true
    type: dict
    suboptions:
      email_addresses:
        description:
          - The list of email actions.
        type: list
        suboptions:
          email_address:
            description:
              - The email address for the action.
            type: str
  email_actions1:
    description:
      - The email actions for auto quota increase.
    required: true
    type: dict
    suboptions:
      email_addresses:
        description:
          - The list of email actions.
        type: list
        suboptions:
          email_address:
            description:
              - The email address for the action.
            type: str
  auto_quota_increase_state:
    description:
      - If the subscription has enabled automatic quota increase.
    required: true
    type: str
    choices:
      - enabled
      - disabled
  state:
    description:
      - Assert the state of the AutoQuotaIncrease.
      - >-
        Use C(present) to create or update an AutoQuotaIncrease and C(absent) to
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
    - name: SetAutoQuotaIncreaseSettings
      azure_rm_autoquotaincrease: 
        {}
        

    - name: TurnOffAutoQuotaIncrease
      azure_rm_autoquotaincrease: 
        {}
        

'''

RETURN = '''
id:
  description:
    - The subscription Id.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the auto quota increase.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource
  returned: always
  type: str
  sample: null
support_ticket_action:
  description:
    - The support ticket action.
  returned: always
  type: dict
  sample: null
  contains:
    severity:
      description:
        - The support request severity.
      returned: always
      type: str
      sample: null
    first_name:
      description:
        - The first name of the recipient.
      returned: always
      type: str
      sample: null
    last_name:
      description:
        - The last name of the recipient.
      returned: always
      type: str
      sample: null
    country:
      description:
        - The country of the recipient.
      returned: always
      type: str
      sample: null
    phone_number:
      description:
        - The phone number of the recipient.
      returned: always
      type: str
      sample: null
    primary_email_address:
      description:
        - The primary email addresses of the recipients.
      returned: always
      type: str
      sample: null
    support_language:
      description:
        - The support language.
      returned: always
      type: str
      sample: null
    preferred_contact_method:
      description:
        - The preferred communication channel.
      returned: always
      type: str
      sample: null
    alternate_email_addresses:
      description:
        - The alternate email address of the recipient.
      returned: always
      type: list
      sample: null
email_actions_properties_on_success_email_actions:
  description:
    - The email actions for auto quota increase.
  returned: always
  type: dict
  sample: null
  contains:
    email_addresses:
      description:
        - The list of email actions.
      returned: always
      type: list
      sample: null
      contains:
        email_address:
          description:
            - The email address for the action.
          returned: always
          type: str
          sample: null
email_actions_properties_on_failure_email_actions:
  description:
    - The email actions for auto quota increase.
  returned: always
  type: dict
  sample: null
  contains:
    email_addresses:
      description:
        - The list of email actions.
      returned: always
      type: list
      sample: null
      contains:
        email_address:
          description:
            - The email address for the action.
          returned: always
          type: str
          sample: null
auto_quota_increase_state:
  description:
    - If the subscription has enabled automatic quota increase.
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
    from azure.mgmt.azure import Azure Reservation API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAutoQuotaIncrease(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            support_ticket_action=dict(
                type='dict',
                disposition='/support_ticket_action',
                required=True,
                options=dict(
                    severity=dict(
                        type='str',
                        disposition='severity',
                        choices=['Critical',
                                 'Moderate',
                                 'Minimal']
                    ),
                    first_name=dict(
                        type='str',
                        disposition='first_name'
                    ),
                    last_name=dict(
                        type='str',
                        disposition='last_name'
                    ),
                    country=dict(
                        type='str',
                        disposition='country'
                    ),
                    phone_number=dict(
                        type='str',
                        disposition='phone_number'
                    ),
                    primary_email_address=dict(
                        type='str',
                        disposition='primary_email_address'
                    ),
                    support_language=dict(
                        type='str',
                        disposition='support_language'
                    ),
                    preferred_contact_method=dict(
                        type='str',
                        disposition='preferred_contact_method',
                        choices=['Email',
                                 'Phone']
                    ),
                    alternate_email_addresses=dict(
                        type='list',
                        disposition='alternate_email_addresses',
                        elements='str'
                    )
                )
            ),
            email_actions=dict(
                type='dict',
                disposition='/email_actions',
                required=True,
                options=dict(
                    email_addresses=dict(
                        type='list',
                        disposition='email_addresses',
                        elements='dict',
                        options=dict(
                            email_address=dict(
                                type='str',
                                disposition='email_address'
                            )
                        )
                    )
                )
            ),
            email_actions1=dict(
                type='dict',
                disposition='/email_actions1',
                required=True,
                options=dict(
                    email_addresses=dict(
                        type='list',
                        disposition='email_addresses',
                        elements='dict',
                        options=dict(
                            email_address=dict(
                                type='str',
                                disposition='email_address'
                            )
                        )
                    )
                )
            ),
            auto_quota_increase_state=dict(
                type='str',
                disposition='/auto_quota_increase_state',
                choices=['enabled',
                         'disabled'],
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAutoQuotaIncrease, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Reservation API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-19-preview')

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
                response = self.mgmt_client.auto_quota_increase.create(,
                                                                       auto_quota_increase_request=self.body)
            else:
                response = self.mgmt_client.auto_quota_increase.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AutoQuotaIncrease instance.')
            self.fail('Error creating the AutoQuotaIncrease instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.auto_quota_increase.delete()
        except CloudError as e:
            self.log('Error attempting to delete the AutoQuotaIncrease instance.')
            self.fail('Error deleting the AutoQuotaIncrease instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.auto_quota_increase.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAutoQuotaIncrease()


if __name__ == '__main__':
    main()
