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
module: azure_rm_startmenuitem_info
version_added: '2.9'
short_description: Get StartMenuItem info.
description:
  - Get info of StartMenuItem.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StartMenuItem_List
      azure_rm_startmenuitem_info: 
        application_group_name: applicationGroup1
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
start_menu_items:
  description: >-
    A list of dict results where the key is the name of the StartMenuItem and
    the values are the facts for that StartMenuItem.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of StartMenuItem definitions.
      returned: always
      type: list
      sample: null
      contains:
        app_alias:
          description:
            - Alias of StartMenuItem.
          returned: always
          type: str
          sample: null
        friendly_name:
          description:
            - Friendly name of StartMenuItem.
          returned: always
          type: str
          sample: null
        file_path:
          description:
            - Path to the file of StartMenuItem.
          returned: always
          type: str
          sample: null
        command_line_arguments:
          description:
            - Command line arguments for StartMenuItem.
          returned: always
          type: str
          sample: null
        icon_path:
          description:
            - Path to the icon.
          returned: always
          type: str
          sample: null
        icon_index:
          description:
            - Index of the icon.
          returned: always
          type: integer
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


class AzureRMStartMenuItemInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            application_group_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.application_group_name = None

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
        super(AzureRMStartMenuItemInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

        if (self.resource_group_name is not None and
            self.application_group_name is not None):
            self.results['start_menu_items'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.start_menu_items.list(resource_group_name=self.resource_group_name,
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
    AzureRMStartMenuItemInfo()


if __name__ == '__main__':
    main()
