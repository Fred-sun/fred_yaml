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
module: azure_rm_dedicatedcloudservice_info
version_added: '2.9'
short_description: Get DedicatedCloudService info.
description:
  - Get info of DedicatedCloudService.
options:
  filter:
    description:
      - The filter to apply on the list operation
    type: str
  top:
    description:
      - The maximum number of record sets to return
    type: integer
  skip_token:
    description:
      - to be used by nextLink implementation
    type: str
  resource_group_name:
    description:
      - The name of the resource group
    type: str
  dedicated_cloud_service_name:
    description:
      - dedicated cloud Service name
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListDedicatedCloudServices
      azure_rm_dedicatedcloudservice_info: 
        {}
        

    - name: ListRGDedicatedCloudServices
      azure_rm_dedicatedcloudservice_info: 
        resource_group_name: myResourceGroup
        

    - name: GetDedicatedCloudService
      azure_rm_dedicatedcloudservice_info: 
        dedicated_cloud_service_name: myService
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
dedicated_cloud_services:
  description: >-
    A list of dict results where the key is the name of the
    DedicatedCloudService and the values are the facts for that
    DedicatedCloudService.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - Link for next list of DedicatedCloudNode
      returned: always
      type: str
      sample: null
    value:
      description:
        - Results of the DedicatedCloudService list
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
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
            - '{dedicatedCloudServiceName}'
          returned: always
          type: str
          sample: null
        tags:
          description:
            - The list of tags
          returned: always
          type: dictionary
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
          returned: always
          type: str
          sample: null
        gateway_subnet:
          description:
            - >-
              gateway Subnet for the account. It will collect the subnet address
              and always treat it as /28
          returned: always
          type: str
          sample: null
        is_account_onboarded:
          description:
            - indicates whether account onboarded or not in a given region
          returned: always
          type: sealed-choice
          sample: null
        nodes:
          description:
            - total nodes purchased
          returned: always
          type: integer
          sample: null
        service_url:
          description:
            - link to a service management web portal
          returned: always
          type: str
          sample: null
    id:
      description:
        - >-
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
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
        - '{dedicatedCloudServiceName}'
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The list of tags
      returned: always
      type: dictionary
      sample: null
    type:
      description:
        - '{resourceProviderNamespace}/{resourceType}'
      returned: always
      type: str
      sample: null
    gateway_subnet:
      description:
        - >-
          gateway Subnet for the account. It will collect the subnet address and
          always treat it as /28
      returned: always
      type: str
      sample: null
    is_account_onboarded:
      description:
        - indicates whether account onboarded or not in a given region
      returned: always
      type: sealed-choice
      sample: null
    nodes:
      description:
        - total nodes purchased
      returned: always
      type: integer
      sample: null
    service_url:
      description:
        - link to a service management web portal
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


class AzureRMDedicatedCloudServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip_token=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            dedicated_cloud_service_name=dict(
                type='str'
            )
        )

        self.filter = None
        self.top = None
        self.skip_token = None
        self.resource_group_name = None
        self.dedicated_cloud_service_name = None

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
        super(AzureRMDedicatedCloudServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.resource_group_name is not None and
            self.dedicated_cloud_service_name is not None):
            self.results['dedicated_cloud_services'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['dedicated_cloud_services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['dedicated_cloud_services'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_services.get(resource_group_name=self.resource_group_name,
                                                                     dedicated_cloud_service_name=self.dedicated_cloud_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_services.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                        filter=self.filter,
                                                                                        top=self.top,
                                                                                        skip_token=self.skip_token)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_services.list_by_subscription(filter=self.filter,
                                                                                      top=self.top,
                                                                                      skip_token=self.skip_token)
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
    AzureRMDedicatedCloudServiceInfo()


if __name__ == '__main__':
    main()
