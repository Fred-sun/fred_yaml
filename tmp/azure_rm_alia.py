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
module: azure_rm_alia
version_added: '2.9'
short_description: Manage Azure Alia instance.
description:
  - 'Create, update and delete instance of Azure Alia.'
options:
  alias_name:
    description:
      - Alias Name
    required: true
    type: str
  properties:
    description:
      - Put alias request properties.
    type: dict
    suboptions:
      display_name:
        description:
          - The friendly name of the subscription.
        type: str
      workload:
        description:
          - >-
            The workload type of the subscription. It can be either Production
            or DevTest.
        type: str
        choices:
          - Production
          - DevTest
      billing_scope:
        description:
          - 'Determines whether subscription is fieldLed, partnerLed or LegacyEA'
        type: str
      subscription_id:
        description:
          - >-
            This parameter can be used to create alias for existing subscription
            Id
        type: str
  state:
    description:
      - Assert the state of the Alia.
      - Use C(present) to create or update an Alia and C(absent) to delete it.
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
    - name: CreateAlias
      azure_rm_alia: 
        alias_name: aliasForNewSub
        properties:
          billing_scope: >-
            /providers/Microsoft.Billing/billingAccounts/e879cf0f-2b4d-5431-109a-f72fc9868693:024cabf4-7321-4cf9-be59-df0c77ca51de_2019-05-31/billingProfiles/PE2Q-NOIT-BG7-TGB/invoiceSections/MTT4-OBS7-PJA-TGB
          display_name: Contoso MCA subscription
          workload: Production
        

    - name: DeleteAlias
      azure_rm_alia: 
        alias_name: aliasForNewSub
        

'''

RETURN = '''
id:
  description:
    - Fully qualified ID for the alias resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - Alias ID.
  returned: always
  type: str
  sample: null
type:
  description:
    - 'Resource type, Microsoft.Subscription/aliases.'
  returned: always
  type: str
  sample: null
properties:
  description:
    - Put Alias response properties.
  returned: always
  type: dict
  sample: null
  contains:
    subscription_id:
      description:
        - Newly created subscription Id.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource.
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
    from azure.mgmt.subscription import SubscriptionClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAlia(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            alias_name=dict(
                type='str',
                required=True
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    display_name=dict(
                        type='str',
                        disposition='display_name'
                    ),
                    workload=dict(
                        type='str',
                        disposition='workload',
                        choices=['Production',
                                 'DevTest']
                    ),
                    billing_scope=dict(
                        type='str',
                        disposition='billing_scope'
                    ),
                    subscription_id=dict(
                        type='str',
                        disposition='subscription_id'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.alias_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAlia, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SubscriptionClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01')

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
                response = self.mgmt_client.alias.create(alias_name=self.alias_name,
                                                         body=self.body)
            else:
                response = self.mgmt_client.alias.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Alia instance.')
            self.fail('Error creating the Alia instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.alias.delete(alias_name=self.alias_name)
        except CloudError as e:
            self.log('Error attempting to delete the Alia instance.')
            self.fail('Error deleting the Alia instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.alias.get(alias_name=self.alias_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAlia()


if __name__ == '__main__':
    main()
