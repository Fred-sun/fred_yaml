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
module: azure_rm_privatezone
version_added: '2.9'
short_description: Manage Azure PrivateZone instance.
description:
  - 'Create, update and delete instance of Azure PrivateZone.'
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
  if_match:
    description:
      - >-
        The ETag of the Private DNS zone. Omit this value to always overwrite
        the current zone. Specify the last-seen ETag value to prevent
        accidentally overwriting any concurrent changes.
      - >-
        The ETag of the Private DNS zone. Omit this value to always delete the
        current zone. Specify the last-seen ETag value to prevent accidentally
        deleting any concurrent changes.
    type: str
  if_none_match:
    description:
      - >-
        Set to '*' to allow a new Private DNS zone to be created, but to prevent
        updating an existing zone. Other values will be ignored.
    type: str
  location:
    description:
      - The Azure Region where the resource lives
    type: str
  etag:
    description:
      - The ETag of the zone.
    type: str
  state:
    description:
      - Assert the state of the PrivateZone.
      - >-
        Use C(present) to create or update an PrivateZone and C(absent) to
        delete it.
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
    - name: PUT Private DNS Zone
      azure_rm_privatezone: 
        private_zone_name: privatezone1.com
        resource_group_name: resourceGroup1
        location: Global
        tags:
          key1: value1
        

    - name: PATCH Private DNS Zone
      azure_rm_privatezone: 
        private_zone_name: privatezone1.com
        resource_group_name: resourceGroup1
        tags:
          key2: value2
        

    - name: DELETE Private DNS Zone
      azure_rm_privatezone: 
        private_zone_name: privatezone1.com
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
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
    - The ETag of the zone.
  returned: always
  type: str
  sample: null
max_number_of_record_sets:
  description:
    - >-
      The maximum number of record sets that can be created in this Private DNS
      zone. This is a read-only property and any attempt to set this value will
      be ignored.
  returned: always
  type: integer
  sample: null
number_of_record_sets:
  description:
    - >-
      The current number of record sets in this Private DNS zone. This is a
      read-only property and any attempt to set this value will be ignored.
  returned: always
  type: integer
  sample: null
max_number_of_virtual_network_links:
  description:
    - >-
      The maximum number of virtual networks that can be linked to this Private
      DNS zone. This is a read-only property and any attempt to set this value
      will be ignored.
  returned: always
  type: integer
  sample: null
number_of_virtual_network_links:
  description:
    - >-
      The current number of virtual networks that are linked to this Private DNS
      zone. This is a read-only property and any attempt to set this value will
      be ignored.
  returned: always
  type: integer
  sample: null
max_number_of_virtual_network_links_with_registration:
  description:
    - >-
      The maximum number of virtual networks that can be linked to this Private
      DNS zone with registration enabled. This is a read-only property and any
      attempt to set this value will be ignored.
  returned: always
  type: integer
  sample: null
number_of_virtual_network_links_with_registration:
  description:
    - >-
      The current number of virtual networks that are linked to this Private DNS
      zone with registration enabled. This is a read-only property and any
      attempt to set this value will be ignored.
  returned: always
  type: integer
  sample: null
provisioning_state:
  description:
    - >-
      The provisioning state of the resource. This is a read-only property and
      any attempt to set this value will be ignored.
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
    from azure.mgmt.private import PrivateDnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPrivateZone(AzureRMModuleBaseExt):
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
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.private_zone_name = None
        self.if_match = None
        self.if_none_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPrivateZone, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(PrivateDnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01')

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
            response = self.mgmt_client.private_zones.create_or_update(resource_group_name=self.resource_group_name,
                                                                       private_zone_name=self.private_zone_name,
                                                                       if_match=self.if_match,
                                                                       if_none_match=self.if_none_match,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PrivateZone instance.')
            self.fail('Error creating the PrivateZone instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.private_zones.delete(resource_group_name=self.resource_group_name,
                                                             private_zone_name=self.private_zone_name,
                                                             if_match=self.if_match)
        except CloudError as e:
            self.log('Error attempting to delete the PrivateZone instance.')
            self.fail('Error deleting the PrivateZone instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.private_zones.get(resource_group_name=self.resource_group_name,
                                                          private_zone_name=self.private_zone_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPrivateZone()


if __name__ == '__main__':
    main()
