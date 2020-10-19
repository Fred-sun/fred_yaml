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
module: azure_rm_dedicatedhsm
version_added: '2.9'
short_description: Manage Azure DedicatedHsm instance.
description:
  - 'Create, update and delete instance of Azure DedicatedHsm.'
options:
  resource_group_name:
    description:
      - The name of the Resource Group to which the resource belongs.
      - The name of the Resource Group to which the server belongs.
      - The name of the Resource Group to which the dedicated HSM belongs.
      - The name of the Resource Group to which the dedicated hsm belongs.
    required: true
    type: str
  name:
    description:
      - Name of the dedicated Hsm
      - Name of the dedicated HSM
      - The name of the dedicated HSM to delete
      - The name of the dedicated HSM.
    required: true
    type: str
  location:
    description:
      - The supported Azure location where the dedicated HSM should be created.
    type: str
  sku:
    description:
      - SKU details
    type: dict
    suboptions:
      name:
        description:
          - SKU of the dedicated HSM
        type: constant
  zones:
    description:
      - The Dedicated Hsm zones.
    type: list
  stamp_id:
    description:
      - This field will be used when RP does not support Availability zones.
    type: str
  subnet:
    description:
      - Specifies the identifier of the subnet.
    type: dict
    suboptions:
      id:
        description:
          - >-
            The ARM resource id in the form of
            /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        type: str
  network_interfaces:
    description:
      - >-
        Specifies the list of resource Ids for the network interfaces associated
        with the dedicated HSM.
    type: list
    suboptions:
      id:
        description:
          - >-
            The ARM resource id in the form of
            /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        type: str
      private_ip_address:
        description:
          - Private Ip address of the interface
        type: str
  state:
    description:
      - Assert the state of the DedicatedHsm.
      - >-
        Use C(present) to create or update an DedicatedHsm and C(absent) to
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
    - name: Create a new or update an existing dedicated HSM
      azure_rm_dedicatedhsm: 
        name: hsm1
        resource_group_name: hsm-group
        location: westus
        properties:
          network_profile:
            network_interfaces:
              - private_ip_address: 1.0.0.1
            subnet:
              id: >-
                /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/hsm-group/providers/Microsoft.Network/virtualNetworks/stamp01/subnets/stamp01
          stamp_id: stamp01
        sku:
          name: SafeNet Luna Network HSM A790
        tags:
          dept: hsm
          environment: dogfood
        

    - name: Update an existing dedicated HSM
      azure_rm_dedicatedhsm: 
        name: hsm1
        resource_group_name: hsm-group
        tags:
          dept: hsm
          environment: dogfood
          slice: A
        

    - name: Delete a dedicated HSM
      azure_rm_dedicatedhsm: 
        name: hsm1
        resource_group_name: hsm-group
        

'''

RETURN = '''
id:
  description:
    - The Azure Resource Manager resource ID for the dedicated HSM.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the dedicated HSM.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type of the dedicated HSM.
  returned: always
  type: str
  sample: null
location:
  description:
    - The supported Azure location where the dedicated HSM should be created.
  returned: always
  type: str
  sample: null
sku:
  description:
    - SKU details
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - SKU of the dedicated HSM
      returned: always
      type: constant
      sample: null
zones:
  description:
    - The Dedicated Hsm zones.
  returned: always
  type: list
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
stamp_id:
  description:
    - This field will be used when RP does not support Availability zones.
  returned: always
  type: str
  sample: null
status_message:
  description:
    - Resource Status Message.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state.
  returned: always
  type: str
  sample: null
subnet:
  description:
    - Specifies the identifier of the subnet.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - >-
          The ARM resource id in the form of
          /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
      returned: always
      type: str
      sample: null
network_interfaces:
  description:
    - >-
      Specifies the list of resource Ids for the network interfaces associated
      with the dedicated HSM.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - >-
          The ARM resource id in the form of
          /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
      returned: always
      type: str
      sample: null
    private_ip_address:
      description:
        - Private Ip address of the interface
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
    from azure.mgmt.azure import Azure Dedicated HSM Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedHsm(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            name=dict(
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
                        type='constant',
                        disposition='name'
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
            ),
            stamp_id=dict(
                type='str',
                disposition='/stamp_id'
            ),
            subnet=dict(
                type='dict',
                disposition='/subnet',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            network_interfaces=dict(
                type='list',
                disposition='/network_interfaces',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        updatable=False,
                        disposition='id'
                    ),
                    private_ip_address=dict(
                        type='str',
                        disposition='private_ip_address'
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
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedHsm, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Dedicated HSM Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-31-preview')

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
            response = self.mgmt_client.dedicated_hsm.create_or_update(resource_group_name=self.resource_group_name,
                                                                       name=self.name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedHsm instance.')
            self.fail('Error creating the DedicatedHsm instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_hsm.delete(resource_group_name=self.resource_group_name,
                                                             name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedHsm instance.')
            self.fail('Error deleting the DedicatedHsm instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dedicated_hsm.get(resource_group_name=self.resource_group_name,
                                                          name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedHsm()


if __name__ == '__main__':
    main()
