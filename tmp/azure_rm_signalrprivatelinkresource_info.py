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
module: azure_rm_signalrprivatelinkresource_info
version_added: '2.9'
short_description: Get SignalRPrivateLinkResource info.
description:
  - Get info of SignalRPrivateLinkResource.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  resource_name:
    description:
      - The name of the SignalR resource.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SignalRPrivateLinkResources_List
      azure_rm_signalrprivatelinkresource_info: 
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        

'''

RETURN = '''
signal_rprivate_link_resources:
  description: >-
    A list of dict results where the key is the name of the
    SignalRPrivateLinkResource and the values are the facts for that
    SignalRPrivateLinkResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of PrivateLinkResource
      returned: always
      type: list
      sample: null
      contains:
        group_id:
          description:
            - Group Id of the private link resource
          returned: always
          type: str
          sample: null
        required_members:
          description:
            - Required members of the private link resource
          returned: always
          type: list
          sample: null
        required_zone_names:
          description:
            - Required private DNS zone names
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - "The URL the client should use to fetch the next page (per server side paging).\r\nIt's null for now, added for future use."
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
    from azure.mgmt.signal import SignalRManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSignalRPrivateLinkResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
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
        self.query_parameters['api-version'] = '2020-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSignalRPrivateLinkResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SignalRManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['signal_rprivate_link_resources'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.signal_rprivate_link_resources.list(resource_group_name=self.resource_group_name,
                                                                            resource_name=self.resource_name)
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
    AzureRMSignalRPrivateLinkResourceInfo()


if __name__ == '__main__':
    main()
