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
module: azure_rm_zone_info
version_added: '2.9'
short_description: Get Zone info.
description:
  - Get info of Zone.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  zone_name:
    description:
      - The name of the DNS zone (without a terminating dot).
    type: str
  top:
    description:
      - >-
        The maximum number of record sets to return. If not specified, returns
        up to 100 record sets.
      - >-
        The maximum number of DNS zones to return. If not specified, returns up
        to 100 zones.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get zone
      azure_rm_zone_info: 
        resource_group_name: rg1
        zone_name: zone1
        

    - name: List zones by resource group
      azure_rm_zone_info: 
        resource_group_name: rg1
        

    - name: List zones by subscription
      azure_rm_zone_info: 
        {}
        

'''

RETURN = '''
zones:
  description: >-
    A list of dict results where the key is the name of the Zone and the values
    are the facts for that Zone.
  returned: always
  type: complex
  contains:
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
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - The etag of the zone.
      returned: always
      type: str
      sample: null
    max_number_of_record_sets:
      description:
        - >-
          The maximum number of record sets that can be created in this DNS
          zone.  This is a read-only property and any attempt to set this value
          will be ignored.
      returned: always
      type: integer
      sample: null
    number_of_record_sets:
      description:
        - >-
          The current number of record sets in this DNS zone.  This is a
          read-only property and any attempt to set this value will be ignored.
      returned: always
      type: integer
      sample: null
    name_servers:
      description:
        - >-
          The name servers for this DNS zone. This is a read-only property and
          any attempt to set this value will be ignored.
      returned: always
      type: list
      sample: null
    zone_type:
      description:
        - The type of this DNS zone (Public or Private).
      returned: always
      type: sealed-choice
      sample: null
    registration_virtual_networks:
      description:
        - >-
          A list of references to virtual networks that register hostnames in
          this DNS zone. This is a only when ZoneType is Private.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource Id.
          returned: always
          type: str
          sample: null
    resolution_virtual_networks:
      description:
        - >-
          A list of references to virtual networks that resolve records in this
          DNS zone. This is a only when ZoneType is Private.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource Id.
          returned: always
          type: str
          sample: null
    value:
      description:
        - Information about the DNS zones.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - The etag of the zone.
          returned: always
          type: str
          sample: null
        max_number_of_record_sets:
          description:
            - >-
              The maximum number of record sets that can be created in this DNS
              zone.  This is a read-only property and any attempt to set this
              value will be ignored.
          returned: always
          type: integer
          sample: null
        number_of_record_sets:
          description:
            - >-
              The current number of record sets in this DNS zone.  This is a
              read-only property and any attempt to set this value will be
              ignored.
          returned: always
          type: integer
          sample: null
        name_servers:
          description:
            - >-
              The name servers for this DNS zone. This is a read-only property
              and any attempt to set this value will be ignored.
          returned: always
          type: list
          sample: null
        zone_type:
          description:
            - The type of this DNS zone (Public or Private).
          returned: always
          type: sealed-choice
          sample: null
        registration_virtual_networks:
          description:
            - >-
              A list of references to virtual networks that register hostnames
              in this DNS zone. This is a only when ZoneType is Private.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource Id.
              returned: always
              type: str
              sample: null
        resolution_virtual_networks:
          description:
            - >-
              A list of references to virtual networks that resolve records in
              this DNS zone. This is a only when ZoneType is Private.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource Id.
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
    from azure.mgmt.dns import DnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMZoneInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            zone_name=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.zone_name = None
        self.top = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMZoneInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-05-01')

        if (self.resource_group_name is not None and
            self.zone_name is not None):
            self.results['zones'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['zones'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['zones'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.zones.get(resource_group_name=self.resource_group_name,
                                                  zone_name=self.zone_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.zones.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                     top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.zones.list(top=self.top)
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
    AzureRMZoneInfo()


if __name__ == '__main__':
    main()
