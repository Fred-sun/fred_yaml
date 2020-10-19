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
module: azure_rm_service_info
version_added: '2.9'
short_description: Get Service info.
description:
  - Get info of Service.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the Windows IoT Device
        Service.
    type: str
  device_name:
    description:
      - The name of the Windows IoT Device Service.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Services_GetProperties
      azure_rm_service_info: 
        device_name: service8596
        resource_group_name: res9407
        

    - name: Service_ListByResourceGroup
      azure_rm_service_info: 
        resource_group_name: res6117
        

    - name: Service_List
      azure_rm_service_info: 
        {}
        

'''

RETURN = '''
services:
  description: >-
    A list of dict results where the key is the name of the Service and the
    values are the facts for that Service.
  returned: always
  type: complex
  contains:
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The Azure Region where the resource lives
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          The Etag field is *not* required. If it is provided in the response
          body, it must also be provided as a header per the normal ETag
          convention.
      returned: always
      type: str
      sample: null
    notes:
      description:
        - Windows IoT Device Service notes.
      returned: always
      type: str
      sample: null
    start_date:
      description:
        - 'Windows IoT Device Service start date,'
      returned: always
      type: str
      sample: null
    quantity:
      description:
        - 'Windows IoT Device Service device allocation,'
      returned: always
      type: integer
      sample: null
    billing_domain_name:
      description:
        - Windows IoT Device Service ODM AAD domain
      returned: always
      type: str
      sample: null
    admin_domain_name:
      description:
        - Windows IoT Device Service OEM AAD domain
      returned: always
      type: str
      sample: null
    value:
      description:
        - The array of DeviceService objects.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - >-
              The Etag field is *not* required. If it is provided in the
              response body, it must also be provided as a header per the normal
              ETag convention.
          returned: always
          type: str
          sample: null
        notes:
          description:
            - Windows IoT Device Service notes.
          returned: always
          type: str
          sample: null
        start_date:
          description:
            - 'Windows IoT Device Service start date,'
          returned: always
          type: str
          sample: null
        quantity:
          description:
            - 'Windows IoT Device Service device allocation,'
          returned: always
          type: integer
          sample: null
        billing_domain_name:
          description:
            - Windows IoT Device Service ODM AAD domain
          returned: always
          type: str
          sample: null
        admin_domain_name:
          description:
            - Windows IoT Device Service OEM AAD domain
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The next link.
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
    from azure.mgmt.device import DeviceServices
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            device_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.device_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DeviceServices,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.device_name is not None):
            self.results['services'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['services'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.services.get(resource_group_name=self.resource_group_name,
                                                     device_name=self.device_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.services.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.services.list()
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
    AzureRMServiceInfo()


if __name__ == '__main__':
    main()
