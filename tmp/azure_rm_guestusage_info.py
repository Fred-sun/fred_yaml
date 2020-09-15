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
module: azure_rm_guestusage_info
version_added: '2.9'
short_description: Get GuestUsage info.
description:
  - Get info of GuestUsage.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  resource_name:
    description:
      - The initial domain name of the AAD tenant.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GuestUsages_Get
      azure_rm_guestusage_info: 
        resource_group_name: contosoResourceGroup
        resource_name: contoso.onmicrosoft.com
        

    - name: GuestUsagesSubscription_List
      azure_rm_guestusage_info: 
        {}
        

    - name: GuestUsagesResourceGroup_List
      azure_rm_guestusage_info: 
        resource_group_name: contosoResourceGroup
        

'''

RETURN = '''
guest_usages:
  description: >-
    A list of dict results where the key is the name of the GuestUsage and the
    values are the facts for that GuestUsage.
  returned: always
  type: complex
  contains:
    id:
      description:
        - An identifier that represents the Guest Usages resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the Guest Usages resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the Guest Usages resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Location of the Guest Usages resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Key-value pairs of additional resource provisioning properties.
      returned: always
      type: dictionary
      sample: null
    tenant_id:
      description:
        - An identifier for the tenant for which the resource is being created
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of guest usages resources
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - An identifier that represents the Guest Usages resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the Guest Usages resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the Guest Usages resource.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Location of the Guest Usages resource.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Key-value pairs of additional resource provisioning properties.
          returned: always
          type: dictionary
          sample: null
        tenant_id:
          description:
            - >-
              An identifier for the tenant for which the resource is being
              created
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
    from azure.mgmt.cpim import cpim
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGuestUsageInfo(AzureRMModuleBase):
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
        self.query_parameters['api-version'] = '2020-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGuestUsageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(cpim,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01-preview')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['guest_usages'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['guest_usages'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['guest_usages'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.guest_usages.get(resource_group_name=self.resource_group_name,
                                                         resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.guest_usages.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.guest_usages.list_by_subscription()
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
    AzureRMGuestUsageInfo()


if __name__ == '__main__':
    main()
