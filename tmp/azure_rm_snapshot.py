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
module: azure_rm_snapshot
version_added: '2.9'
short_description: Manage Azure Snapshot instance.
description:
  - 'Create, update and delete instance of Azure Snapshot.'
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
  volume_name:
    description:
      - The name of the volume
    required: true
    type: str
  snapshot_name:
    description:
      - The name of the mount target
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  body:
    description:
      - Snapshot object supplied in the body of the operation.
    type: any
  state:
    description:
      - Assert the state of the Snapshot.
      - >-
        Use C(present) to create or update an Snapshot and C(absent) to delete
        it.
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
    - name: Snapshots_Create
      azure_rm_snapshot: 
        account_name: account1
        pool_name: pool1
        resource_group_name: myRG
        snapshot_name: snapshot1
        volume_name: volume1
        location: eastus
        

    - name: Snapshots_Update
      azure_rm_snapshot: 
        account_name: account1
        body: {}
        pool_name: pool1
        resource_group_name: myRG
        snapshot_name: snapshot1
        volume_name: volume1
        

    - name: Snapshots_Delete
      azure_rm_snapshot: 
        account_name: account1
        pool_name: pool1
        resource_group_name: myRG
        snapshot_name: snapshot1
        volume_name: volume1
        

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
snapshot_id:
  description:
    - UUID v4 used to identify the Snapshot
  returned: always
  type: str
  sample: null
created:
  description:
    - The creation date of the snapshot
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Azure lifecycle management
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


class AzureRMSnapshot(AzureRMModuleBaseExt):
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
            volume_name=dict(
                type='str',
                required=True
            ),
            snapshot_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            body=dict(
                type='any',
                disposition='/body'
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
        self.volume_name = None
        self.snapshot_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSnapshot, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.snapshots.create(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name,
                                                             pool_name=self.pool_name,
                                                             volume_name=self.volume_name,
                                                             snapshot_name=self.snapshot_name,
                                                             body=self.body)
            else:
                response = self.mgmt_client.snapshots.update(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name,
                                                             pool_name=self.pool_name,
                                                             volume_name=self.volume_name,
                                                             snapshot_name=self.snapshot_name,
                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Snapshot instance.')
            self.fail('Error creating the Snapshot instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.snapshots.delete(resource_group_name=self.resource_group_name,
                                                         account_name=self.account_name,
                                                         pool_name=self.pool_name,
                                                         volume_name=self.volume_name,
                                                         snapshot_name=self.snapshot_name)
        except CloudError as e:
            self.log('Error attempting to delete the Snapshot instance.')
            self.fail('Error deleting the Snapshot instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.snapshots.get(resource_group_name=self.resource_group_name,
                                                      account_name=self.account_name,
                                                      pool_name=self.pool_name,
                                                      volume_name=self.volume_name,
                                                      snapshot_name=self.snapshot_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSnapshot()


if __name__ == '__main__':
    main()
