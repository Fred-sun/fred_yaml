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
module: azure_rm_widgettype_info
version_added: '2.9'
short_description: Get WidgetType info.
description:
  - Get info of WidgetType.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  hub_name:
    description:
      - The name of the hub.
    required: true
    type: str
  widget_type_name:
    description:
      - The name of the widget type.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: WidgetTypes_ListByHub
      azure_rm_widgettype_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

    - name: WidgetTypes_Get
      azure_rm_widgettype_info: 
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        widget_type_name: ActivityGauge
        

'''

RETURN = '''
widget_types:
  description: >-
    A list of dict results where the key is the name of the WidgetType and the
    values are the facts for that WidgetType.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        widget_type_name:
          description:
            - Name of the widget type.
          returned: always
          type: str
          sample: null
        definition:
          description:
            - Definition for widget type.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Description for widget type.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - Localized display name for the widget type.
          returned: always
          type: dictionary
          sample: null
        image_url:
          description:
            - The image URL.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The hub name.
          returned: always
          type: str
          sample: null
        widget_version:
          description:
            - The widget version.
          returned: always
          type: str
          sample: null
        changed:
          description:
            - Date time when widget type was last modified.
          returned: always
          type: str
          sample: null
        created:
          description:
            - Date time when widget type was created.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    widget_type_name:
      description:
        - Name of the widget type.
      returned: always
      type: str
      sample: null
    definition:
      description:
        - Definition for widget type.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description for widget type.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Localized display name for the widget type.
      returned: always
      type: dictionary
      sample: null
    image_url:
      description:
        - The image URL.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - The hub name.
      returned: always
      type: str
      sample: null
    widget_version:
      description:
        - The widget version.
      returned: always
      type: str
      sample: null
    changed:
      description:
        - Date time when widget type was last modified.
      returned: always
      type: str
      sample: null
    created:
      description:
        - Date time when widget type was created.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWidgetTypeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            hub_name=dict(
                type='str',
                required=True
            ),
            widget_type_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.widget_type_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-26'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWidgetTypeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.widget_type_name is not None):
            self.results['widget_types'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None):
            self.results['widget_types'] = self.format_item(self.listbyhub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.widget_types.get(resource_group_name=self.resource_group_name,
                                                         hub_name=self.hub_name,
                                                         widget_type_name=self.widget_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhub(self):
        response = None

        try:
            response = self.mgmt_client.widget_types.list_by_hub(resource_group_name=self.resource_group_name,
                                                                 hub_name=self.hub_name)
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
    AzureRMWidgetTypeInfo()


if __name__ == '__main__':
    main()
