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
module: azure_rm_customimage_info
version_added: '2.9'
short_description: Get CustomImage info.
description:
  - Get info of CustomImage.
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
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=vm)'''
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
      - The name of the custom image.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
custom_images:
  description: >-
    A list of dict results where the key is the name of the CustomImage and the
    values are the facts for that CustomImage.
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
        vhd:
          description:
            - The VHD from which the image is to be created.
          returned: always
          type: dict
          sample: null
          contains:
            image_name:
              description:
                - The image name.
              returned: always
              type: str
              sample: null
            sys_prep:
              description:
                - Indicates whether sysprep has been run on the VHD.
              returned: always
              type: bool
              sample: null
            os_type:
              description:
                - 'The OS type of the custom image (i.e. Windows, Linux)'
              returned: always
              type: str
              sample: null
        description:
          description:
            - The description of the custom image.
          returned: always
          type: str
          sample: null
        author:
          description:
            - The author of the custom image.
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of the custom image.
          returned: always
          type: str
          sample: null
        managed_image_id:
          description:
            - The Managed Image Id backing the custom image.
          returned: always
          type: str
          sample: null
        managed_snapshot_id:
          description:
            - The Managed Snapshot Id backing the custom image.
          returned: always
          type: str
          sample: null
        data_disk_storage_info:
          description:
            - >-
              Storage information about the data disks present in the custom
              image
          returned: always
          type: list
          sample: null
          contains:
            lun:
              description:
                - Disk Lun
              returned: always
              type: str
              sample: null
            storage_type:
              description:
                - Disk Storage Type
              returned: always
              type: str
              sample: null
        custom_image_plan:
          description:
            - Storage information about the plan related to this custom image
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - 'The id of the plan, equivalent to name of the plan'
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - >-
                  The publisher for the plan from the marketplace image the
                  custom image is derived from
              returned: always
              type: str
              sample: null
            offer:
              description:
                - >-
                  The offer for the plan from the marketplace image the custom
                  image is derived from
              returned: always
              type: str
              sample: null
        is_plan_authorized:
          description:
            - >-
              Whether or not the custom images underlying offer/plan has been
              enabled for programmatic deployment
          returned: always
          type: bool
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
        source_vm_id:
          description:
            - The source vm identifier.
          returned: always
          type: str
          sample: null
        windows_os_info:
          description:
            - The Windows OS information of the VM.
          returned: always
          type: dict
          sample: null
          contains:
            windows_os_state:
              description:
                - >-
                  The state of the Windows OS (i.e. NonSysprepped,
                  SysprepRequested, SysprepApplied).
              returned: always
              type: str
              sample: null
        linux_os_info:
          description:
            - The Linux OS information of the VM.
          returned: always
          type: dict
          sample: null
          contains:
            linux_os_state:
              description:
                - >-
                  The state of the Linux OS (i.e. NonDeprovisioned,
                  DeprovisionRequested, DeprovisionApplied).
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
    vhd:
      description:
        - The VHD from which the image is to be created.
      returned: always
      type: dict
      sample: null
      contains:
        image_name:
          description:
            - The image name.
          returned: always
          type: str
          sample: null
        sys_prep:
          description:
            - Indicates whether sysprep has been run on the VHD.
          returned: always
          type: bool
          sample: null
        os_type:
          description:
            - 'The OS type of the custom image (i.e. Windows, Linux)'
          returned: always
          type: str
          sample: null
    description:
      description:
        - The description of the custom image.
      returned: always
      type: str
      sample: null
    author:
      description:
        - The author of the custom image.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of the custom image.
      returned: always
      type: str
      sample: null
    managed_image_id:
      description:
        - The Managed Image Id backing the custom image.
      returned: always
      type: str
      sample: null
    managed_snapshot_id:
      description:
        - The Managed Snapshot Id backing the custom image.
      returned: always
      type: str
      sample: null
    data_disk_storage_info:
      description:
        - Storage information about the data disks present in the custom image
      returned: always
      type: list
      sample: null
      contains:
        lun:
          description:
            - Disk Lun
          returned: always
          type: str
          sample: null
        storage_type:
          description:
            - Disk Storage Type
          returned: always
          type: str
          sample: null
    custom_image_plan:
      description:
        - Storage information about the plan related to this custom image
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - 'The id of the plan, equivalent to name of the plan'
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - >-
              The publisher for the plan from the marketplace image the custom
              image is derived from
          returned: always
          type: str
          sample: null
        offer:
          description:
            - >-
              The offer for the plan from the marketplace image the custom image
              is derived from
          returned: always
          type: str
          sample: null
    is_plan_authorized:
      description:
        - >-
          Whether or not the custom images underlying offer/plan has been
          enabled for programmatic deployment
      returned: always
      type: bool
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
    source_vm_id:
      description:
        - The source vm identifier.
      returned: always
      type: str
      sample: null
    windows_os_info:
      description:
        - The Windows OS information of the VM.
      returned: always
      type: dict
      sample: null
      contains:
        windows_os_state:
          description:
            - >-
              The state of the Windows OS (i.e. NonSysprepped, SysprepRequested,
              SysprepApplied).
          returned: always
          type: str
          sample: null
    linux_os_info:
      description:
        - The Linux OS information of the VM.
      returned: always
      type: dict
      sample: null
      contains:
        linux_os_state:
          description:
            - >-
              The state of the Linux OS (i.e. NonDeprovisioned,
              DeprovisionRequested, DeprovisionApplied).
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


class AzureRMCustomImageInfo(AzureRMModuleBase):
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
        super(AzureRMCustomImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

        if (self.resource_group_name is not None and
            self.lab_name is not None and
            self.name is not None):
            self.results['custom_images'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_name is not None):
            self.results['custom_images'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.custom_images.get(resource_group_name=self.resource_group_name,
                                                          lab_name=self.lab_name,
                                                          name=self.name,
                                                          expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.custom_images.list(resource_group_name=self.resource_group_name,
                                                           lab_name=self.lab_name,
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
    AzureRMCustomImageInfo()


if __name__ == '__main__':
    main()
