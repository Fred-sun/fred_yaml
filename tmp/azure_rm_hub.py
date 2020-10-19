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
module: azure_rm_hub
version_added: '2.9'
short_description: Manage Azure Hub instance.
description:
  - 'Create, update and delete instance of Azure Hub.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  hub_name:
    description:
      - The name of the Hub.
      - The name of the hub.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  tenant_features:
    description:
      - >-
        The bit flags for enabled hub features. Bit 0 is set to 1 indicates
        graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates
        the hub is disabled, or enabled if set to 0.
    type: integer
  hub_billing_info:
    description:
      - Billing settings of the hub.
    type: dict
    suboptions:
      sku_name:
        description:
          - The sku name.
        type: str
      min_units:
        description:
          - >-
            The minimum number of units will be billed. One unit is 10,000
            Profiles and 100,000 Interactions.
        type: integer
      max_units:
        description:
          - >-
            The maximum number of units can be used.  One unit is 10,000
            Profiles and 100,000 Interactions.
        type: integer
  state:
    description:
      - Assert the state of the Hub.
      - Use C(present) to create or update an Hub and C(absent) to delete it.
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
    - name: Hubs_CreateOrUpdate
      azure_rm_hub: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        location: West US
        properties:
          hub_billing_info:
            max_units: 5
            min_units: 1
            sku_name: B0
        

    - name: Hubs_Update
      azure_rm_hub: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        location: West US
        properties:
          hub_billing_info:
            max_units: 5
            min_units: 1
            sku_name: B0
        

    - name: Hubs_Delete
      azure_rm_hub: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
api_endpoint:
  description:
    - API endpoint URL of the hub.
  returned: always
  type: str
  sample: null
web_endpoint:
  description:
    - Web endpoint URL of the hub.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state of the hub.
  returned: always
  type: str
  sample: null
tenant_features:
  description:
    - >-
      The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph
      is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub
      is disabled, or enabled if set to 0.
  returned: always
  type: integer
  sample: null
hub_billing_info:
  description:
    - Billing settings of the hub.
  returned: always
  type: dict
  sample: null
  contains:
    sku_name:
      description:
        - The sku name.
      returned: always
      type: str
      sample: null
    min_units:
      description:
        - >-
          The minimum number of units will be billed. One unit is 10,000
          Profiles and 100,000 Interactions.
      returned: always
      type: integer
      sample: null
    max_units:
      description:
        - >-
          The maximum number of units can be used.  One unit is 10,000 Profiles
          and 100,000 Interactions.
      returned: always
      type: integer
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMHub(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            hub_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            tenant_features=dict(
                type='integer',
                disposition='/tenant_features'
            ),
            hub_billing_info=dict(
                type='dict',
                disposition='/hub_billing_info',
                options=dict(
                    sku_name=dict(
                        type='str',
                        disposition='sku_name'
                    ),
                    min_units=dict(
                        type='integer',
                        disposition='min_units'
                    ),
                    max_units=dict(
                        type='integer',
                        disposition='max_units'
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
        self.hub_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMHub, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

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
            response = self.mgmt_client.hubs.create_or_update(resource_group_name=self.resource_group_name,
                                                              hub_name=self.hub_name,
                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Hub instance.')
            self.fail('Error creating the Hub instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.hubs.delete(resource_group_name=self.resource_group_name,
                                                    hub_name=self.hub_name)
        except CloudError as e:
            self.log('Error attempting to delete the Hub instance.')
            self.fail('Error deleting the Hub instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.hubs.get(resource_group_name=self.resource_group_name,
                                                 hub_name=self.hub_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMHub()


if __name__ == '__main__':
    main()
