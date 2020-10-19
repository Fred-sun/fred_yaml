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
module: azure_rm_desktop_info
version_added: '2.9'
short_description: Get Desktop info.
description:
  - Get info of Desktop.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  application_group_name:
    description:
      - The name of the application group
    required: true
    type: str
  desktop_name:
    description:
      - The name of the desktop within the specified desktop group
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Desktop_Get
      azure_rm_desktop_info: 
        application_group_name: applicationGroup1
        desktop_name: SessionDesktop
        resource_group_name: resourceGroup1
        

    - name: Desktop_List
      azure_rm_desktop_info: 
        application_group_name: applicationGroup1
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
desktops:
  description: >-
    A list of dict results where the key is the name of the Desktop and the
    values are the facts for that Desktop.
  returned: always
  type: complex
  contains:
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
    description:
      description:
        - Description of Desktop.
      returned: always
      type: str
      sample: null
    friendly_name:
      description:
        - Friendly name of Desktop.
      returned: always
      type: str
      sample: null
    icon_hash:
      description:
        - Hash of the icon.
      returned: always
      type: str
      sample: null
    icon_content:
      description:
        - The icon a 64 bit string as a byte array.
      returned: always
      type: byte-array
      sample: null
    value:
      description:
        - List of Desktop definitions.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - Description of Desktop.
          returned: always
          type: str
          sample: null
        friendly_name:
          description:
            - Friendly name of Desktop.
          returned: always
          type: str
          sample: null
        icon_hash:
          description:
            - Hash of the icon.
          returned: always
          type: str
          sample: null
        icon_content:
          description:
            - The icon a 64 bit string as a byte array.
          returned: always
          type: byte-array
          sample: null
    next_link:
      description:
        - Link to the next page of results.
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
    from azure.mgmt.desktop import Desktop Virtualization API Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDesktopInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            application_group_name=dict(
                type='str',
                required=True
            ),
            desktop_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.application_group_name = None
        self.desktop_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-10-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDesktopInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

        if (self.resource_group_name is not None and
            self.application_group_name is not None and
            self.desktop_name is not None):
            self.results['desktops'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.application_group_name is not None):
            self.results['desktops'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.desktops.get(resource_group_name=self.resource_group_name,
                                                     application_group_name=self.application_group_name,
                                                     desktop_name=self.desktop_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.desktops.list(resource_group_name=self.resource_group_name,
                                                      application_group_name=self.application_group_name)
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
    AzureRMDesktopInfo()


if __name__ == '__main__':
    main()
