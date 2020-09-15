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
module: azure_rm_cloudappliance_info
version_added: '2.9'
short_description: Get CloudAppliance info.
description:
  - Get info of CloudAppliance.
options:
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CloudAppliancesListSupportedConfigurations
      azure_rm_cloudappliance_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
cloud_appliances:
  description: >-
    A list of dict results where the key is the name of the CloudAppliance and
    the values are the facts for that CloudAppliance.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        model_number:
          description:
            - The model number.
          returned: always
          type: str
          sample: null
        cloud_platform:
          description:
            - The cloud platform.
          returned: always
          type: str
          sample: null
        acs_configuration:
          description:
            - The ACS configuration.
          returned: always
          type: dict
          sample: null
          contains:
            namespace:
              description:
                - The namespace.
              returned: always
              type: str
              sample: null
            realm:
              description:
                - The realm.
              returned: always
              type: str
              sample: null
            service_url:
              description:
                - The service URL.
              returned: always
              type: str
              sample: null
        supported_storage_account_types:
          description:
            - The supported storage account types.
          returned: always
          type: list
          sample: null
        supported_regions:
          description:
            - The supported regions.
          returned: always
          type: list
          sample: null
        supported_vm_types:
          description:
            - The supported virtual machine types.
          returned: always
          type: list
          sample: null
        supported_vm_images:
          description:
            - The supported virtual machine images.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The name.
              returned: always
              type: str
              sample: null
            version:
              description:
                - The version.
              returned: always
              type: str
              sample: null
            offer:
              description:
                - The offer.
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - The publisher.
              returned: always
              type: str
              sample: null
            sku:
              description:
                - The SKU.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCloudApplianceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.manager_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCloudApplianceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['cloud_appliances'] = self.format_item(self.listsupportedconfiguration())
        return self.results

    def listsupportedconfiguration(self):
        response = None

        try:
            response = self.mgmt_client.cloud_appliances.list_supported_configuration(resource_group_name=self.resource_group_name,
                                                                                      manager_name=self.manager_name)
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
    AzureRMCloudApplianceInfo()


if __name__ == '__main__':
    main()
