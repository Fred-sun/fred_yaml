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
module: azure_rm_dedicatedhsm_info
version_added: '2.9'
short_description: Get DedicatedHsm info.
description:
  - Get info of DedicatedHsm.
options:
  resource_group_name:
    description:
      - The name of the Resource Group to which the dedicated hsm belongs.
      - The name of the Resource Group to which the dedicated HSM belongs.
    type: str
  name:
    description:
      - The name of the dedicated HSM.
    type: str
  top:
    description:
      - Maximum number of results to return.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a dedicated HSM
      azure_rm_dedicatedhsm_info: 
        name: hsm1
        resource_group_name: hsm-group
        

    - name: List dedicated HSM devices in a resource group
      azure_rm_dedicatedhsm_info: 
        resource_group_name: hsm-group
        

    - name: List dedicated HSM devices in a subscription
      azure_rm_dedicatedhsm_info: 
        {}
        

'''

RETURN = '''
dedicated_hsm:
  description: >-
    A list of dict results where the key is the name of the DedicatedHsm and the
    values are the facts for that DedicatedHsm.
  returned: always
  type: complex
  contains:
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
        - >-
          The supported Azure location where the dedicated HSM should be
          created.
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
          Specifies the list of resource Ids for the network interfaces
          associated with the dedicated HSM.
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
    value:
      description:
        - The list of dedicated HSMs.
      returned: always
      type: list
      sample: null
      contains:
        stamp_id:
          description:
            - >-
              This field will be used when RP does not support Availability
              zones.
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
              Specifies the list of resource Ids for the network interfaces
              associated with the dedicated HSM.
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
    next_link:
      description:
        - The URL to get the next set of dedicated hsms.
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
    from azure.mgmt.azure import Azure Dedicated HSM Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDedicatedHsmInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.name = None
        self.top = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-10-31-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDedicatedHsmInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Dedicated HSM Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-31-preview')

        if (self.resource_group_name is not None and
            self.name is not None):
            self.results['dedicated_hsm'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['dedicated_hsm'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['dedicated_hsm'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hsm.get(resource_group_name=self.resource_group_name,
                                                          name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hsm.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                             top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hsm.list_by_subscription(top=self.top)
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
    AzureRMDedicatedHsmInfo()


if __name__ == '__main__':
    main()
