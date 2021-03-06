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
module: azure_rm_pool
version_added: '2.9'
short_description: Manage Azure Pool instance.
description:
  - 'Create, update and delete instance of Azure Pool.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the NetApp account
    required: true
    type: str
  pool_name:
    description:
      - The name of the capacity pool
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  size:
    description:
      - >-
        Provisioned size of the pool (in bytes). Allowed values are in 4TiB
        chunks (value must be multiply of 4398046511104).
    type: integer
  service_level:
    description:
      - The service level of the file system
    type: str
    choices:
      - Standard
      - Premium
      - Ultra
  qos_type:
    description:
      - The qos type of the pool
    type: str
    choices:
      - Auto
      - Manual
  state:
    description:
      - Assert the state of the Pool.
      - Use C(present) to create or update an Pool and C(absent) to delete it.
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
    - name: Pools_CreateOrUpdate
      azure_rm_pool: 
        account_name: account1
        pool_name: pool1
        resource_group_name: myRG
        location: eastus
        properties:
          qos_type: Auto
          service_level: Premium
          size: 4398046511104
        

    - name: Pools_Update
      azure_rm_pool: 
        account_name: account1
        pool_name: pool1
        resource_group_name: myRG
        

    - name: Pools_Delete
      azure_rm_pool: 
        account_name: account1
        pool_name: pool1
        resource_group_name: myRG
        

'''

RETURN = '''
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
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
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
pool_id:
  description:
    - UUID v4 used to identify the Pool
  returned: always
  type: str
  sample: null
size:
  description:
    - >-
      Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks
      (value must be multiply of 4398046511104).
  returned: always
  type: integer
  sample: null
service_level:
  description:
    - The service level of the file system
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Azure lifecycle management
  returned: always
  type: str
  sample: null
total_throughput_mibps:
  description:
    - Total throughput of pool in Mibps
  returned: always
  type: number
  sample: null
utilized_throughput_mibps:
  description:
    - Utilized throughput of pool in Mibps
  returned: always
  type: number
  sample: null
qos_type:
  description:
    - The qos type of the pool
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
    from azure.mgmt.net import NetAppManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPool(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            pool_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            size=dict(
                type='integer',
                disposition='/size'
            ),
            service_level=dict(
                type='str',
                disposition='/service_level',
                choices=['Standard',
                         'Premium',
                         'Ultra']
            ),
            qos_type=dict(
                type='str',
                disposition='/qos_type',
                choices=['Auto',
                         'Manual']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.pool_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPool, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(NetAppManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.pools.create_or_update(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               pool_name=self.pool_name,
                                                               body=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Pool instance.')
            self.fail('Error creating the Pool instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.pools.delete(resource_group_name=self.resource_group_name,
                                                     account_name=self.account_name,
                                                     pool_name=self.pool_name)
        except CloudError as e:
            self.log('Error attempting to delete the Pool instance.')
            self.fail('Error deleting the Pool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.pools.get(resource_group_name=self.resource_group_name,
                                                  account_name=self.account_name,
                                                  pool_name=self.pool_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPool()


if __name__ == '__main__':
    main()
