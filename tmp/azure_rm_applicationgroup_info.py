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
module: azure_rm_applicationgroup_info
version_added: '2.9'
short_description: Get ApplicationGroup info.
description:
  - Get info of ApplicationGroup.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  application_group_name:
    description:
      - The name of the application group
    type: str
  filter:
    description:
      - >-
        OData filter expression. Valid properties for filtering are
        applicationGroupType.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ApplicationGroup_Get
      azure_rm_applicationgroup_info: 
        application_group_name: applicationGroup1
        resource_group_name: resourceGroup1
        

    - name: ApplicationGroup_ListByResourceGroup
      azure_rm_applicationgroup_info: 
        resource_group_name: resourceGroup1
        

    - name: ApplicationGroup_List
      azure_rm_applicationgroup_info: 
        {}
        

'''

RETURN = '''
application_groups:
  description: >-
    A list of dict results where the key is the name of the ApplicationGroup and
    the values are the facts for that ApplicationGroup.
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
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description of ApplicationGroup.
      returned: always
      type: str
      sample: null
    friendly_name:
      description:
        - Friendly name of ApplicationGroup.
      returned: always
      type: str
      sample: null
    host_pool_arm_path:
      description:
        - HostPool arm path of ApplicationGroup.
      returned: always
      type: str
      sample: null
    workspace_arm_path:
      description:
        - Workspace arm path of ApplicationGroup.
      returned: always
      type: str
      sample: null
    application_group_type:
      description:
        - Resource Type of ApplicationGroup.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of ApplicationGroup definitions.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - Description of ApplicationGroup.
          returned: always
          type: str
          sample: null
        friendly_name:
          description:
            - Friendly name of ApplicationGroup.
          returned: always
          type: str
          sample: null
        host_pool_arm_path:
          description:
            - HostPool arm path of ApplicationGroup.
          returned: always
          type: str
          sample: null
        workspace_arm_path:
          description:
            - Workspace arm path of ApplicationGroup.
          returned: always
          type: str
          sample: null
        application_group_type:
          description:
            - Resource Type of ApplicationGroup.
          returned: always
          type: str
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


class AzureRMApplicationGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            application_group_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.application_group_name = None
        self.filter = None

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
        super(AzureRMApplicationGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

        if (self.resource_group_name is not None and
            self.application_group_name is not None):
            self.results['application_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['application_groups'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['application_groups'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.application_groups.get(resource_group_name=self.resource_group_name,
                                                               application_group_name=self.application_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.application_groups.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                  filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.application_groups.list_by_subscription(filter=self.filter)
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
    AzureRMApplicationGroupInfo()


if __name__ == '__main__':
    main()
