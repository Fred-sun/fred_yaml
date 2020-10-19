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
module: azure_rm_hostpool_info
version_added: '2.9'
short_description: Get HostPool info.
description:
  - Get info of HostPool.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  host_pool_name:
    description:
      - The name of the host pool within the specified resource group
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: HostPool_Get
      azure_rm_hostpool_info: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        

    - name: HostPool_ListByResourceGroup
      azure_rm_hostpool_info: 
        resource_group_name: resourceGroup1
        

    - name: HostPool_List
      azure_rm_hostpool_info: 
        {}
        

'''

RETURN = '''
host_pools:
  description: >-
    A list of dict results where the key is the name of the HostPool and the
    values are the facts for that HostPool.
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
    friendly_name:
      description:
        - Friendly name of HostPool.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description of HostPool.
      returned: always
      type: str
      sample: null
    host_pool_type:
      description:
        - HostPool type for desktop.
      returned: always
      type: str
      sample: null
    personal_desktop_assignment_type:
      description:
        - PersonalDesktopAssignment type for HostPool.
      returned: always
      type: str
      sample: null
    custom_rdp_property:
      description:
        - Custom rdp property of HostPool.
      returned: always
      type: str
      sample: null
    max_session_limit:
      description:
        - The max session limit of HostPool.
      returned: always
      type: integer
      sample: null
    load_balancer_type:
      description:
        - The type of the load balancer.
      returned: always
      type: str
      sample: null
    ring:
      description:
        - The ring number of HostPool.
      returned: always
      type: integer
      sample: null
    validation_environment:
      description:
        - Is validation environment.
      returned: always
      type: bool
      sample: null
    registration_info:
      description:
        - The registration info of HostPool.
      returned: always
      type: dict
      sample: null
      contains:
        expiration_time:
          description:
            - Expiration time of registration token.
          returned: always
          type: str
          sample: null
        token:
          description:
            - The registration token base64 encoded string.
          returned: always
          type: str
          sample: null
        registration_token_operation:
          description:
            - The type of resetting the token.
          returned: always
          type: str
          sample: null
    vm_template:
      description:
        - VM template for sessionhosts configuration within hostpool.
      returned: always
      type: str
      sample: null
    application_group_references:
      description:
        - List of applicationGroup links.
      returned: always
      type: list
      sample: null
    sso_context:
      description:
        - Path to keyvault containing ssoContext secret.
      returned: always
      type: str
      sample: null
    preferred_app_group_type:
      description:
        - >-
          The type of preferred application group type, default to Desktop
          Application Group
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of HostPool definitions.
      returned: always
      type: list
      sample: null
      contains:
        friendly_name:
          description:
            - Friendly name of HostPool.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Description of HostPool.
          returned: always
          type: str
          sample: null
        host_pool_type:
          description:
            - HostPool type for desktop.
          returned: always
          type: str
          sample: null
        personal_desktop_assignment_type:
          description:
            - PersonalDesktopAssignment type for HostPool.
          returned: always
          type: str
          sample: null
        custom_rdp_property:
          description:
            - Custom rdp property of HostPool.
          returned: always
          type: str
          sample: null
        max_session_limit:
          description:
            - The max session limit of HostPool.
          returned: always
          type: integer
          sample: null
        load_balancer_type:
          description:
            - The type of the load balancer.
          returned: always
          type: str
          sample: null
        ring:
          description:
            - The ring number of HostPool.
          returned: always
          type: integer
          sample: null
        validation_environment:
          description:
            - Is validation environment.
          returned: always
          type: bool
          sample: null
        registration_info:
          description:
            - The registration info of HostPool.
          returned: always
          type: dict
          sample: null
          contains:
            expiration_time:
              description:
                - Expiration time of registration token.
              returned: always
              type: str
              sample: null
            token:
              description:
                - The registration token base64 encoded string.
              returned: always
              type: str
              sample: null
            registration_token_operation:
              description:
                - The type of resetting the token.
              returned: always
              type: str
              sample: null
        vm_template:
          description:
            - VM template for sessionhosts configuration within hostpool.
          returned: always
          type: str
          sample: null
        application_group_references:
          description:
            - List of applicationGroup links.
          returned: always
          type: list
          sample: null
        sso_context:
          description:
            - Path to keyvault containing ssoContext secret.
          returned: always
          type: str
          sample: null
        preferred_app_group_type:
          description:
            - >-
              The type of preferred application group type, default to Desktop
              Application Group
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


class AzureRMHostPoolInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            host_pool_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.host_pool_name = None

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
        super(AzureRMHostPoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

        if (self.resource_group_name is not None and
            self.host_pool_name is not None):
            self.results['host_pools'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['host_pools'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['host_pools'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.host_pools.get(resource_group_name=self.resource_group_name,
                                                       host_pool_name=self.host_pool_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.host_pools.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.host_pools.list()
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
    AzureRMHostPoolInfo()


if __name__ == '__main__':
    main()
