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
module: azure_rm_request
version_added: '2.9'
short_description: Manage Azure Request instance.
description:
  - 'Create, update and delete instance of Azure Request.'
options:
  request_id:
    description:
      - The Lockbox request ID.
    required: true
    type: str
  state:
    description:
      - Assert the state of the Request.
      - >-
        Use C(present) to create or update an Request and C(absent) to delete
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
'''

RETURN = '''
id:
  description:
    - The Arm resource id of the Lockbox request.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the Lockbox request.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the Lockbox request.
  returned: always
  type: str
  sample: null
properties:
  description:
    - The properties that are associated with a lockbox request.
  returned: always
  type: dict
  sample: null
  contains:
    request_id:
      description:
        - The Lockbox request ID.
      returned: always
      type: str
      sample: null
    justification:
      description:
        - The justification of the requestor.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the request.
      returned: always
      type: str
      sample: null
    created_date_time:
      description:
        - The creation time of the request.
      returned: always
      type: str
      sample: null
    expiration_date_time:
      description:
        - The expiration time of the request.
      returned: always
      type: str
      sample: null
    duration:
      description:
        - The duration of the request in hours.
      returned: always
      type: integer
      sample: null
    requested_resource_ids:
      description:
        - >-
          A list of resource IDs associated with the Lockbox request separated
          by ','.
      returned: always
      type: list
      sample: null
    resource_type:
      description:
        - The resource type of the requested resources.
      returned: always
      type: str
      sample: null
    support_request:
      description:
        - The id of the support request associated.
      returned: always
      type: str
      sample: null
    support_case_url:
      description:
        - The url of the support case.
      returned: always
      type: str
      sample: null
    subscription_id:
      description:
        - The subscription ID.
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
    from azure.mgmt.customer import Customer Lockbox
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRequest(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            request_id=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.request_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRequest, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Customer Lockbox,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-02-28-preview')

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
                response = self.mgmt_client.requests.create()
            else:
                response = self.mgmt_client.requests.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Request instance.')
            self.fail('Error creating the Request instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.requests.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Request instance.')
            self.fail('Error deleting the Request instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.requests.get(request_id=self.request_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRequest()


if __name__ == '__main__':
    main()
