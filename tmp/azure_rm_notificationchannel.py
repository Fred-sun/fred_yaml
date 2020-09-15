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
module: azure_rm_notificationchannel
version_added: '2.9'
short_description: Manage Azure NotificationChannel instance.
description:
  - 'Create, update and delete instance of Azure NotificationChannel.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  name:
    description:
      - The name of the notification channel.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=webHookUrl)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  web_hook_url:
    description:
      - The webhook URL to send notifications to.
    type: str
  email_recipient:
    description:
      - >-
        The email recipient to send notifications to (can be a list of
        semi-colon separated email addresses).
    type: str
  notification_locale:
    description:
      - >-
        The locale to use when sending a notification (fallback for unsupported
        languages is EN).
    type: str
  description:
    description:
      - Description of notification.
    type: str
  events:
    description:
      - The list of event for which this notification is enabled.
    type: list
    suboptions:
      event_name:
        description:
          - >-
            The event type for which this notification is enabled (i.e.
            AutoShutdown, Cost)
        type: str
        choices:
          - AutoShutdown
          - Cost
  state:
    description:
      - Assert the state of the NotificationChannel.
      - >-
        Use C(present) to create or update an NotificationChannel and C(absent)
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
    - The identifier of the resource.
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
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
web_hook_url:
  description:
    - The webhook URL to send notifications to.
  returned: always
  type: str
  sample: null
email_recipient:
  description:
    - >-
      The email recipient to send notifications to (can be a list of semi-colon
      separated email addresses).
  returned: always
  type: str
  sample: null
notification_locale:
  description:
    - >-
      The locale to use when sending a notification (fallback for unsupported
      languages is EN).
  returned: always
  type: str
  sample: null
description:
  description:
    - Description of notification.
  returned: always
  type: str
  sample: null
events:
  description:
    - The list of event for which this notification is enabled.
  returned: always
  type: list
  sample: null
  contains:
    event_name:
      description:
        - >-
          The event type for which this notification is enabled (i.e.
          AutoShutdown, Cost)
      returned: always
      type: str
      sample: null
created_date:
  description:
    - The creation date of the notification channel.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning status of the resource.
  returned: always
  type: str
  sample: null
unique_identifier:
  description:
    - The unique immutable identifier of a resource (Guid).
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNotificationChannel(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            web_hook_url=dict(
                type='str',
                disposition='/web_hook_url'
            ),
            email_recipient=dict(
                type='str',
                disposition='/email_recipient'
            ),
            notification_locale=dict(
                type='str',
                disposition='/notification_locale'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            events=dict(
                type='list',
                disposition='/events',
                elements='dict',
                options=dict(
                    event_name=dict(
                        type='str',
                        disposition='event_name',
                        choices=['AutoShutdown',
                                 'Cost']
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
        self.lab_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNotificationChannel, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.notification_channels.create_or_update(resource_group_name=self.resource_group_name,
                                                                               lab_name=self.lab_name,
                                                                               name=self.name,
                                                                               notification_channel=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the NotificationChannel instance.')
            self.fail('Error creating the NotificationChannel instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.notification_channels.delete(resource_group_name=self.resource_group_name,
                                                                     lab_name=self.lab_name,
                                                                     name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the NotificationChannel instance.')
            self.fail('Error deleting the NotificationChannel instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.notification_channels.get(resource_group_name=self.resource_group_name,
                                                                  lab_name=self.lab_name,
                                                                  name=self.name,
                                                                  expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNotificationChannel()


if __name__ == '__main__':
    main()
