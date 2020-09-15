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
module: azure_rm_dashboard_info
version_added: '2.9'
short_description: Get Dashboard info.
description:
  - Get info of Dashboard.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  dashboard_name:
    description:
      - The name of the dashboard.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a Dashboard
      azure_rm_dashboard_info: 
        dashboard_name: testDashboard
        resource_group_name: testRG
        

    - name: List all custom resource providers on the resourceGroup
      azure_rm_dashboard_info: 
        resource_group_name: testRG
        

    - name: List all custom resource providers on the subscription
      azure_rm_dashboard_info: 
        {}
        

'''

RETURN = '''
dashboards:
  description: >-
    A list of dict results where the key is the name of the Dashboard and the
    values are the facts for that Dashboard.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    lenses:
      description:
        - The dashboard lenses.
      returned: always
      type: list
      sample: null
    metadata:
      description:
        - The dashboard metadata.
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - The array of custom resource provider manifests.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags
          returned: always
          type: dictionary
          sample: null
        lenses:
          description:
            - The dashboard lenses.
          returned: always
          type: list
          sample: null
        metadata:
          description:
            - The dashboard metadata.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
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
    from azure.mgmt.portal import portal
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDashboardInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            dashboard_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.dashboard_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDashboardInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(portal,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

        if (self.resource_group_name is not None and
            self.dashboard_name is not None):
            self.results['dashboards'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['dashboards'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['dashboards'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dashboards.get(resource_group_name=self.resource_group_name,
                                                       dashboard_name=self.dashboard_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.dashboards.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.dashboards.list_by_subscription()
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
    AzureRMDashboardInfo()


if __name__ == '__main__':
    main()
