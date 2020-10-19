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
module: azure_rm_capacity
version_added: '2.9'
short_description: Manage Azure Capacity instance.
description:
  - 'Create, update and delete instance of Azure Capacity.'
options:
  resource_group_name:
    description:
      - >-
        The name of the Azure Resource group of which a given PowerBIDedicated
        capacity is part. This name must be at least 1 character in length, and
        no more than 90.
    required: true
    type: str
  dedicated_capacity_name:
    description:
      - >-
        The name of the Dedicated capacity. It must be a minimum of 3
        characters, and a maximum of 63.
      - >-
        The name of the Dedicated capacity. It must be at least 3 characters in
        length, and no more than 63.
    required: true
    type: str
  location:
    description:
      - Location of the PowerBI Dedicated resource.
    type: str
  sku:
    description:
      - The SKU of the PowerBI Dedicated resource.
      - The SKU of the Dedicated capacity resource.
    type: dict
    suboptions:
      name:
        description:
          - Name of the SKU level.
        required: true
        type: str
      tier:
        description:
          - The name of the Azure pricing tier to which the SKU applies.
        type: str
        choices:
          - PBIE_Azure
  administration:
    description:
      - A collection of Dedicated capacity administrators
    type: dict
    suboptions:
      members:
        description:
          - An array of administrator user identities.
        type: list
  state:
    description:
      - Assert the state of the Capacity.
      - >-
        Use C(present) to create or update an Capacity and C(absent) to delete
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
    - name: Create capacity
      azure_rm_capacity: 
        dedicated_capacity_name: azsdktest
        resource_group_name: TestRG
        

    - name: Get details of a capacity
      azure_rm_capacity: 
        dedicated_capacity_name: azsdktest
        resource_group_name: TestRG
        

    - name: Update capacity parameters
      azure_rm_capacity: 
        dedicated_capacity_name: azsdktest
        resource_group_name: TestRG
        

'''

RETURN = '''
id:
  description:
    - An identifier that represents the PowerBI Dedicated resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the PowerBI Dedicated resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the PowerBI Dedicated resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - Location of the PowerBI Dedicated resource.
  returned: always
  type: str
  sample: null
sku:
  description:
    - The SKU of the PowerBI Dedicated resource.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of the SKU level.
      returned: always
      type: str
      sample: null
    tier:
      description:
        - The name of the Azure pricing tier to which the SKU applies.
      returned: always
      type: str
      sample: null
tags:
  description:
    - Key-value pairs of additional resource provisioning properties.
  returned: always
  type: dictionary
  sample: null
administration:
  description:
    - A collection of Dedicated capacity administrators
  returned: always
  type: dict
  sample: null
  contains:
    members:
      description:
        - An array of administrator user identities.
      returned: always
      type: list
      sample: null
state:
  description:
    - >-
      The current state of PowerBI Dedicated resource. The state is to indicate
      more states outside of resource provisioning.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - >-
      The current deployment state of PowerBI Dedicated resource. The
      provisioningState is to indicate states for resource provisioning.
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
    from azure.mgmt.power import PowerBIDedicated
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCapacity(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            dedicated_capacity_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier',
                        choices=['PBIE_Azure']
                    )
                )
            ),
            administration=dict(
                type='dict',
                disposition='/administration',
                options=dict(
                    members=dict(
                        type='list',
                        disposition='members',
                        elements='str'
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
        self.dedicated_capacity_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCapacity, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(PowerBIDedicated,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01')

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
                response = self.mgmt_client.capacities.create(resource_group_name=self.resource_group_name,
                                                              dedicated_capacity_name=self.dedicated_capacity_name,
                                                              capacity_parameters=self.body)
            else:
                response = self.mgmt_client.capacities.update(resource_group_name=self.resource_group_name,
                                                              dedicated_capacity_name=self.dedicated_capacity_name,
                                                              capacity_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Capacity instance.')
            self.fail('Error creating the Capacity instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.capacities.delete(resource_group_name=self.resource_group_name,
                                                          dedicated_capacity_name=self.dedicated_capacity_name)
        except CloudError as e:
            self.log('Error attempting to delete the Capacity instance.')
            self.fail('Error deleting the Capacity instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.capacities.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCapacity()


if __name__ == '__main__':
    main()
