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
module: azure_rm_partner
version_added: '2.9'
short_description: Manage Azure Partner instance.
description:
  - 'Create, update and delete instance of Azure Partner.'
options:
  state:
    description:
      - Assert the state of the Partner.
      - >-
        Use C(present) to create or update an Partner and C(absent) to delete
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
etag:
  description:
    - Type of the partner
  returned: always
  type: integer
  sample: null
id:
  description:
    - Identifier of the partner
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of the partner
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of resource. "Microsoft.ManagementPartner/partners"
  returned: always
  type: str
  sample: null
partner_id:
  description:
    - This is the partner id
  returned: always
  type: str
  sample: null
partner_name:
  description:
    - This is the partner name
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - This is the tenant id.
  returned: always
  type: str
  sample: null
object_id:
  description:
    - This is the object id.
  returned: always
  type: str
  sample: null
version:
  description:
    - This is the version.
  returned: always
  type: integer
  sample: null
updated_time:
  description:
    - This is the DateTime when the partner was updated.
  returned: always
  type: str
  sample: null
created_time:
  description:
    - This is the DateTime when the partner was created.
  returned: always
  type: str
  sample: null
state:
  description:
    - This is the partner state
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
    from azure.mgmt.ace import ACE Provisioning ManagementPartner API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPartner(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            undefined,
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

        super(AzureRMPartner, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ACE Provisioning ManagementPartner API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-02-01')

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
                response = self.mgmt_client.partners.create()
            else:
                response = self.mgmt_client.partners.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Partner instance.')
            self.fail('Error creating the Partner instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.partners.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Partner instance.')
            self.fail('Error deleting the Partner instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.partners.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPartner()


if __name__ == '__main__':
    main()
