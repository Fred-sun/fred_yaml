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
module: azure_rm_providerinstance_info
version_added: '2.9'
short_description: Get ProviderInstance info.
description:
  - Get info of ProviderInstance.
options:
  resource_group_name:
    description:
      - Name of the resource group.
    required: true
    type: str
  sap_monitor_name:
    description:
      - Name of the SAP monitor resource.
    required: true
    type: str
  provider_instance_name:
    description:
      - Name of the provider instance.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all SAP Monitors in a subscription
      azure_rm_providerinstance_info: 
        resource_group_name: myResourceGroup
        sap_monitor_name: mySapMonitor
        

    - name: Get properties of a SAP monitor
      azure_rm_providerinstance_info: 
        provider_instance_name: myProviderInstance
        resource_group_name: myResourceGroup
        sap_monitor_name: mySapMonitor
        

'''

RETURN = '''
provider_instances:
  description: >-
    A list of dict results where the key is the name of the ProviderInstance and
    the values are the facts for that ProviderInstance.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of provider instances.
      returned: always
      type: list
      sample: null
      contains:
        type_properties_type:
          description:
            - The type of provider instance.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - A JSON string containing the properties of the provider instance.
          returned: always
          type: str
          sample: null
        metadata:
          description:
            - A JSON string containing metadata of the provider instance.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - State of provisioning of the provider instance
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of provider instances.
      returned: always
      type: str
      sample: null
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    type_properties_type:
      description:
        - The type of provider instance.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - A JSON string containing the properties of the provider instance.
      returned: always
      type: str
      sample: null
    metadata:
      description:
        - A JSON string containing metadata of the provider instance.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - State of provisioning of the provider instance
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
    from azure.mgmt.hana import HanaManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProviderInstanceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sap_monitor_name=dict(
                type='str',
                required=True
            ),
            provider_instance_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.sap_monitor_name = None
        self.provider_instance_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-07-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProviderInstanceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HanaManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-07-preview')

        if (self.resource_group_name is not None and
            self.sap_monitor_name is not None and
            self.provider_instance_name is not None):
            self.results['provider_instances'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.sap_monitor_name is not None):
            self.results['provider_instances'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.provider_instances.get(resource_group_name=self.resource_group_name,
                                                               sap_monitor_name=self.sap_monitor_name,
                                                               provider_instance_name=self.provider_instance_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.provider_instances.list(resource_group_name=self.resource_group_name,
                                                                sap_monitor_name=self.sap_monitor_name)
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
    AzureRMProviderInstanceInfo()


if __name__ == '__main__':
    main()
