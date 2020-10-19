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
module: azure_rm_app_info
version_added: '2.9'
short_description: Get App info.
description:
  - Get info of App.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the IoT Central
        application.
    type: str
  resource_name:
    description:
      - The ARM resource name of the IoT Central application.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Apps_Get
      azure_rm_app_info: 
        resource_group_name: resRg
        resource_name: myIoTCentralApp
        

    - name: Apps_ListBySubscription
      azure_rm_app_info: 
        {}
        

    - name: Apps_ListByResourceGroup
      azure_rm_app_info: 
        resource_group_name: resRg
        

'''

RETURN = '''
apps:
  description: >-
    A list of dict results where the key is the name of the App and the values
    are the facts for that App.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The ARM resource identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The ARM resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The resource tags.
      returned: always
      type: dictionary
      sample: null
    name_sku_name:
      description:
        - The name of the SKU.
      returned: always
      type: str
      sample: null
    application_id:
      description:
        - The ID of the application.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - The display name of the application.
      returned: always
      type: str
      sample: null
    subdomain:
      description:
        - The subdomain of the application.
      returned: always
      type: str
      sample: null
    template:
      description:
        - >-
          The ID of the application template, which is a blueprint that defines
          the characteristics and behaviors of an application. Optional; if not
          specified, defaults to a blank blueprint and allows the application to
          be defined from scratch.
      returned: always
      type: str
      sample: null
    next_link:
      description:
        - The link used to get the next page of IoT Central Applications.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of IoT Central Applications.
      returned: always
      type: list
      sample: null
      contains:
        name_sku_name:
          description:
            - The name of the SKU.
          returned: always
          type: str
          sample: null
        application_id:
          description:
            - The ID of the application.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The display name of the application.
          returned: always
          type: str
          sample: null
        subdomain:
          description:
            - The subdomain of the application.
          returned: always
          type: str
          sample: null
        template:
          description:
            - >-
              The ID of the application template, which is a blueprint that
              defines the characteristics and behaviors of an application.
              Optional; if not specified, defaults to a blank blueprint and
              allows the application to be defined from scratch.
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
    from azure.mgmt.iot import IotCentralClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAppInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAppInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(IotCentralClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['apps'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['apps'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['apps'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.apps.get(resource_group_name=self.resource_group_name,
                                                 resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.apps.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.apps.list_by_subscription()
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
    AzureRMAppInfo()


if __name__ == '__main__':
    main()
