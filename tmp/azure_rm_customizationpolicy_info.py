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
module: azure_rm_customizationpolicy_info
version_added: '2.9'
short_description: Get customizationPolicy info.
description:
  - Get info of customizationPolicy.
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
  filter:
    description:
      - >-
        The filter to apply on the list operation. only type is allowed here as
        a filter e.g. $filter=type eq 'xxxx'
    type: str
  customization_policy_name:
    description:
      - customization policy name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListCustomizationPolicies
      azure_rm_customizationpolicy_info: 
        pc_name: myPrivateCloud
        region_id: myResourceGroup
        

    - name: GetCustomizationPolicy
      azure_rm_customizationpolicy_info: 
        customization_policy_name: Linux1
        pc_name: myPrivateCloud
        region_id: myResourceGroup
        

'''

RETURN = '''
customization_policies:
  description: >-
    A list of dict results where the key is the name of the customizationPolicy
    and the values are the facts for that customizationPolicy.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of the Customization policy
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of the customization policies
      returned: always
      type: list
      sample: null
      contains:
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
                - >-
                  Customization Identity. It contains data about user and
                  hostname
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMcustomizationPolicyInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            customization_policy_name=dict(
                type='str'
            )
        )

        self.region_id = None
        self.pc_name = None
        self.filter = None
        self.customization_policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMcustomizationPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.region_id is not None and
            self.pc_name is not None and
            self.customization_policy_name is not None):
            self.results['customization_policies'] = self.format_item(self.get())
        elif (self.region_id is not None and
              self.pc_name is not None):
            self.results['customization_policies'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.customization_policies.get(region_id=self.region_id,
                                                                   pc_name=self.pc_name,
                                                                   customization_policy_name=self.customization_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.customization_policies.list(region_id=self.region_id,
                                                                    pc_name=self.pc_name,
                                                                    filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
               result.append(tmp.as_dict())
            return result


def main():
    AzureRMcustomizationPolicyInfo()


if __name__ == '__main__':
    main()
