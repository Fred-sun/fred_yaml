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
module: azure_rm_virtualnetworklink_info
version_added: '2.9'
short_description: Get VirtualNetworkLink info.
description:
  - Get info of VirtualNetworkLink.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  private_zone_name:
    description:
      - The name of the Private DNS zone (without a terminating dot).
    required: true
    type: str
  virtual_network_link_name:
    description:
      - The name of the virtual network link.
    type: str
  top:
    description:
      - >-
        The maximum number of virtual network links to return. If not specified,
        returns up to 100 virtual network links.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GET Private DNS Zone Virtual Network Link
      azure_rm_virtualnetworklink_info: 
        private_zone_name: privatezone1.com
        resource_group_name: resourceGroup1
        virtual_network_link_name: virtualNetworkLink1
        

    - name: Get Private DNS Zone Virtual Network Links
      azure_rm_virtualnetworklink_info: 
        private_zone_name: privatezone1.com
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
virtual_network_links:
  description: >-
    A list of dict results where the key is the name of the VirtualNetworkLink
    and the values are the facts for that VirtualNetworkLink.
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
        - The ETag of the virtual network link.
      returned: always
      type: str
      sample: null
    registration_enabled:
      description:
        - >-
          Is auto-registration of virtual machine records in the virtual network
          in the Private DNS zone enabled?
      returned: always
      type: bool
      sample: null
    virtual_network_link_state:
      description:
        - >-
          The status of the virtual network link to the Private DNS zone.
          Possible values are 'InProgress' and 'Done'. This is a read-only
          property and any attempt to set this value will be ignored.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The provisioning state of the resource. This is a read-only property
          and any attempt to set this value will be ignored.
      returned: always
      type: str
      sample: null
    id_properties_virtual_network_id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Information about the virtual network links to the Private DNS zones.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - The ETag of the virtual network link.
          returned: always
          type: str
          sample: null
        registration_enabled:
          description:
            - >-
              Is auto-registration of virtual machine records in the virtual
              network in the Private DNS zone enabled?
          returned: always
          type: bool
          sample: null
        virtual_network_link_state:
          description:
            - >-
              The status of the virtual network link to the Private DNS zone.
              Possible values are 'InProgress' and 'Done'. This is a read-only
              property and any attempt to set this value will be ignored.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the resource. This is a read-only
              property and any attempt to set this value will be ignored.
          returned: always
          type: str
          sample: null
        id_properties_virtual_network_id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The continuation token for the next page of results.
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
    from azure.mgmt.private import PrivateDnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualNetworkLinkInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            private_zone_name=dict(
                type='str',
                required=True
            ),
            virtual_network_link_name=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.private_zone_name = None
        self.virtual_network_link_name = None
        self.top = None

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
        super(AzureRMVirtualNetworkLinkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PrivateDnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01')

        if (self.resource_group_name is not None and
            self.private_zone_name is not None and
            self.virtual_network_link_name is not None):
            self.results['virtual_network_links'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.private_zone_name is not None):
            self.results['virtual_network_links'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_links.get(resource_group_name=self.resource_group_name,
                                                                  private_zone_name=self.private_zone_name,
                                                                  virtual_network_link_name=self.virtual_network_link_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_links.list(resource_group_name=self.resource_group_name,
                                                                   private_zone_name=self.private_zone_name,
                                                                   top=self.top)
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
    AzureRMVirtualNetworkLinkInfo()


if __name__ == '__main__':
    main()
