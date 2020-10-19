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
module: azure_rm_disk
version_added: '2.9'
short_description: Manage Azure Disk instance.
description:
  - 'Create, update and delete instance of Azure Disk.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  user_name:
    description:
      - The name of the user profile.
    required: true
    type: str
  name:
    description:
      - The name of the disk.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=diskType)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  disk_type:
    description:
      - 'The storage type for the disk (i.e. Standard, Premium).'
    type: str
    choices:
      - Standard
      - Premium
      - StandardSSD
  disk_size_gi_b:
    description:
      - The size of the disk in GibiBytes.
    type: integer
  leased_by_lab_vm_id:
    description:
      - The resource ID of the VM to which this disk is leased.
    type: str
  disk_blob_name:
    description:
      - 'When backed by a blob, the name of the VHD blob without extension.'
    type: str
  disk_uri:
    description:
      - 'When backed by a blob, the URI of underlying blob.'
    type: str
  host_caching:
    description:
      - 'The host caching policy of the disk (i.e. None, ReadOnly, ReadWrite).'
    type: str
  managed_disk_id:
    description:
      - >-
        When backed by managed disk, this is the ID of the compute disk
        resource.
    type: str
  state:
    description:
      - Assert the state of the Disk.
      - Use C(present) to create or update an Disk and C(absent) to delete it.
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
'''

RETURN = '''
id:
  description:
    - The identifier of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
disk_type:
  description:
    - 'The storage type for the disk (i.e. Standard, Premium).'
  returned: always
  type: str
  sample: null
disk_size_gi_b:
  description:
    - The size of the disk in GibiBytes.
  returned: always
  type: integer
  sample: null
leased_by_lab_vm_id:
  description:
    - The resource ID of the VM to which this disk is leased.
  returned: always
  type: str
  sample: null
disk_blob_name:
  description:
    - 'When backed by a blob, the name of the VHD blob without extension.'
  returned: always
  type: str
  sample: null
disk_uri:
  description:
    - 'When backed by a blob, the URI of underlying blob.'
  returned: always
  type: str
  sample: null
created_date:
  description:
    - The creation date of the disk.
  returned: always
  type: str
  sample: null
host_caching:
  description:
    - 'The host caching policy of the disk (i.e. None, ReadOnly, ReadWrite).'
  returned: always
  type: str
  sample: null
managed_disk_id:
  description:
    - 'When backed by managed disk, this is the ID of the compute disk resource.'
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning status of the resource.
  returned: always
  type: str
  sample: null
unique_identifier:
  description:
    - The unique immutable identifier of a resource (Guid).
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDisk(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            user_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            disk_type=dict(
                type='str',
                disposition='/disk_type',
                choices=['Standard',
                         'Premium',
                         'StandardSSD']
            ),
            disk_size_gi_b=dict(
                type='integer',
                disposition='/disk_size_gi_b'
            ),
            leased_by_lab_vm_id=dict(
                type='str',
                disposition='/leased_by_lab_vm_id'
            ),
            disk_blob_name=dict(
                type='str',
                disposition='/disk_blob_name'
            ),
            disk_uri=dict(
                type='str',
                disposition='/disk_uri'
            ),
            host_caching=dict(
                type='str',
                disposition='/host_caching'
            ),
            managed_disk_id=dict(
                type='str',
                disposition='/managed_disk_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.user_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDisk, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.disks.create_or_update(resource_group_name=self.resource_group_name,
                                                               lab_name=self.lab_name,
                                                               user_name=self.user_name,
                                                               name=self.name,
                                                               disk=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Disk instance.')
            self.fail('Error creating the Disk instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disks.delete(resource_group_name=self.resource_group_name,
                                                     lab_name=self.lab_name,
                                                     user_name=self.user_name,
                                                     name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Disk instance.')
            self.fail('Error deleting the Disk instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.disks.get(resource_group_name=self.resource_group_name,
                                                  lab_name=self.lab_name,
                                                  user_name=self.user_name,
                                                  name=self.name,
                                                  expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDisk()


if __name__ == '__main__':
    main()
