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
module: azure_rm_customizationpolicy
version_added: '2.9'
short_description: Manage Azure customizationPolicy instance.
description:
  - 'Create, update and delete instance of Azure customizationPolicy.'
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  customization_policy_name:
    description:
      - customization policy name
    required: true
    type: str
  state:
    description:
      - Assert the state of the customizationPolicy.
      - >-
        Use C(present) to create or update an customizationPolicy and C(absent)
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
    - Customization policy azure id
  returned: always
  type: str
  sample: null
location:
  description:
    - Azure region
  returned: always
  type: str
  sample: null
name:
  description:
    - Customization policy name
  returned: always
  type: str
  sample: null
type:
  description:
    - ''
  returned: always
  type: str
  sample: null
description:
  description:
    - Policy description
  returned: always
  type: str
  sample: null
private_cloud_id:
  description:
    - The Private cloud id
  returned: always
  type: str
  sample: null
specification:
  description:
    - Detailed customization policy specification
  returned: always
  type: dict
  sample: null
  contains:
    identity:
      description:
        - Customization Identity. It contains data about user and hostname
      returned: always
      type: dict
      sample: null
      contains:
        data:
          description:
            - Windows Text Identity. Prepared data
          returned: always
          type: str
          sample: null
        host_name:
          description:
            - Virtual machine host name settings
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Hostname
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of host name
              returned: always
              type: str
              sample: null
        type:
          description:
            - Identity type
          returned: always
          type: str
          sample: null
        user_data:
          description:
            - Windows Identity. User data customization
          returned: always
          type: dict
          sample: null
          contains:
            is_password_predefined:
              description:
                - Is password predefined in customization policy
              returned: always
              type: bool
              sample: null
    nic_settings:
      description:
        - Network interface settings
      returned: always
      type: list
      sample: null
      contains:
        adapter:
          description:
            - The list of adapters' settings
          returned: always
          type: dict
          sample: null
          contains:
            gateway:
              description:
                - The list of gateways
              returned: always
              type: list
              sample: null
            ip:
              description:
                - Ip address customization settings
              returned: always
              type: dict
              sample: null
              contains:
                argument:
                  description:
                    - Argument when Custom ip type is selected
                  returned: always
                  type: str
                  sample: null
                ip_address:
                  description:
                    - Defined Ip Address when Fixed ip type is selected
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - Customization Specification ip type
                  returned: always
                  type: str
                  sample: null
            subnet_mask:
              description:
                - Adapter subnet mask
              returned: always
              type: str
              sample: null
        mac_address:
          description:
            - NIC mac address
          returned: always
          type: str
          sample: null
type_properties_type:
  description:
    - The type of customization (Linux or Windows)
  returned: always
  type: str
  sample: null
version:
  description:
    - Policy version
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
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMcustomizationPolicy(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=True
            ),
            pc_name=dict(
                type='str',
                required=True
            ),
            customization_policy_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.region_id = None
        self.pc_name = None
        self.customization_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMcustomizationPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

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
                response = self.mgmt_client.customization_policies.create()
            else:
                response = self.mgmt_client.customization_policies.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the customizationPolicy instance.')
            self.fail('Error creating the customizationPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.customization_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the customizationPolicy instance.')
            self.fail('Error deleting the customizationPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.customization_policies.get(region_id=self.region_id,
                                                                   pc_name=self.pc_name,
                                                                   customization_policy_name=self.customization_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMcustomizationPolicy()


if __name__ == '__main__':
    main()
