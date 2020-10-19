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
module: azure_rm_disk_info
version_added: '2.9'
short_description: Get Disk info.
description:
  - Get info of Disk.
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
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=diskType)'''
    required: true
    type: str
  filter:
    description:
      - >-
        The filter to apply to the operation. Example:
        '$filter=contains(name,'myName')
    type: str
  top:
    description:
      - >-
        The maximum number of resources to return from the operation. Example:
        '$top=10'
    type: integer
  orderby:
    description:
      - >-
        The ordering expression for the results, using OData notation. Example:
        '$orderby=name desc'
    type: str
  name:
    description:
      - The name of the disk.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
disks:
  description: >-
    A list of dict results where the key is the name of the Disk and the values
    are the facts for that Disk.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              The host caching policy of the disk (i.e. None, ReadOnly,
              ReadWrite).
          returned: always
          type: str
          sample: null
        managed_disk_id:
          description:
            - >-
              When backed by managed disk, this is the ID of the compute disk
              resource.
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
    next_link:
      description:
        - Link for next set of results.
      returned: always
      type: str
      sample: null
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
        - >-
          When backed by managed disk, this is the ID of the compute disk
          resource.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDiskInfo(AzureRMModuleBase):
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
            expand=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.user_name = None
        self.expand = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDiskInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

        if (self.resource_group_name is not None and
            self.lab_name is not None and
            self.user_name is not None and
            self.name is not None):
            self.results['disks'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_name is not None and
              self.user_name is not None):
            self.results['disks'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.disks.get(resource_group_name=self.resource_group_name,
                                                  lab_name=self.lab_name,
                                                  user_name=self.user_name,
                                                  name=self.name,
                                                  expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.disks.list(resource_group_name=self.resource_group_name,
                                                   lab_name=self.lab_name,
                                                   user_name=self.user_name,
                                                   expand=self.expand,
                                                   filter=self.filter,
                                                   top=self.top,
                                                   orderby=self.orderby)
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
    AzureRMDiskInfo()


if __name__ == '__main__':
    main()
