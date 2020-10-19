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
module: azure_rm_zone
version_added: '2.9'
short_description: Manage Azure Zone instance.
description:
  - 'Create, update and delete instance of Azure Zone.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  zone_name:
    description:
      - The name of the DNS zone (without a terminating dot).
    required: true
    type: str
  if_match:
    description:
      - >-
        The etag of the DNS zone. Omit this value to always overwrite the
        current zone. Specify the last-seen etag value to prevent accidentally
        overwriting any concurrent changes.
      - >-
        The etag of the DNS zone. Omit this value to always delete the current
        zone. Specify the last-seen etag value to prevent accidentally deleting
        any concurrent changes.
    type: str
  if_none_match:
    description:
      - >-
        Set to '*' to allow a new DNS zone to be created, but to prevent
        updating an existing zone. Other values will be ignored.
    type: str
  location:
    description:
      - Resource location.
    type: str
  etag:
    description:
      - The etag of the zone.
    type: str
  zone_type:
    description:
      - The type of this DNS zone (Public or Private).
    type: sealed-choice
  registration_virtual_networks:
    description:
      - >-
        A list of references to virtual networks that register hostnames in this
        DNS zone. This is a only when ZoneType is Private.
    type: list
    suboptions:
      id:
        description:
          - Resource Id.
        type: str
  resolution_virtual_networks:
    description:
      - >-
        A list of references to virtual networks that resolve records in this
        DNS zone. This is a only when ZoneType is Private.
    type: list
    suboptions:
      id:
        description:
          - Resource Id.
        type: str
  state:
    description:
      - Assert the state of the Zone.
      - Use C(present) to create or update an Zone and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create zone
      azure_rm_zone: 
        resource_group_name: rg1
        zone_name: zone1
        location: Global
        tags:
          key1: value1
        

    - name: Delete zone
      azure_rm_zone: 
        resource_group_name: rg1
        zone_name: zone1
        

    - name: Patch zone
      azure_rm_zone: 
        resource_group_name: rg1
        zone_name: zone1
        tags:
          key2: value2
        

'''

RETURN = '''
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
      The maximum number of record sets that can be created in this DNS zone. 
      This is a read-only property and any attempt to set this value will be
      ignored.
  returned: always
  type: integer
  sample: null
number_of_record_sets:
  description:
    - >-
      The current number of record sets in this DNS zone.  This is a read-only
      property and any attempt to set this value will be ignored.
  returned: always
  type: integer
  sample: null
name_servers:
  description:
    - >-
      The name servers for this DNS zone. This is a read-only property and any
      attempt to set this value will be ignored.
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
      A list of references to virtual networks that register hostnames in this
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
resolution_virtual_networks:
  description:
    - >-
      A list of references to virtual networks that resolve records in this DNS
      zone. This is a only when ZoneType is Private.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dns import DnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMZone(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            zone_name=dict(
                type='str',
                required=True
            ),
            if_match=dict(
                type='str'
            ),
            if_none_match=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            zone_type=dict(
                type='sealed-choice',
                disposition='/zone_type'
            ),
            registration_virtual_networks=dict(
                type='list',
                disposition='/registration_virtual_networks',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            resolution_virtual_networks=dict(
                type='list',
                disposition='/resolution_virtual_networks',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.zone_name = None
        self.if_match = None
        self.if_none_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMZone, self).__init__(derived_arg_spec=self.module_arg_spec,
                                          supports_check_mode=True,
                                          supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(DnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-05-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.zones.create_or_update(resource_group_name=self.resource_group_name,
                                                               zone_name=self.zone_name,
                                                               if_match=self.if_match,
                                                               if_none_match=self.if_none_match,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Zone instance.')
            self.fail('Error creating the Zone instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.zones.delete(resource_group_name=self.resource_group_name,
                                                     zone_name=self.zone_name,
                                                     if_match=self.if_match)
        except CloudError as e:
            self.log('Error attempting to delete the Zone instance.')
            self.fail('Error deleting the Zone instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.zones.get(resource_group_name=self.resource_group_name,
                                                  zone_name=self.zone_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMZone()


if __name__ == '__main__':
    main()
