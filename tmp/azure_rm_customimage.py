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
module: azure_rm_customimage
version_added: '2.9'
short_description: Manage Azure CustomImage instance.
description:
  - 'Create, update and delete instance of Azure CustomImage.'
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
  name:
    description:
      - The name of the custom image.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=vm)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  vhd:
    description:
      - The VHD from which the image is to be created.
    type: dict
    suboptions:
      image_name:
        description:
          - The image name.
        type: str
      sys_prep:
        description:
          - Indicates whether sysprep has been run on the VHD.
        type: bool
      os_type:
        description:
          - 'The OS type of the custom image (i.e. Windows, Linux)'
        required: true
        type: str
        choices:
          - Windows
          - Linux
          - None
  description:
    description:
      - The description of the custom image.
    type: str
  author:
    description:
      - The author of the custom image.
    type: str
  managed_image_id:
    description:
      - The Managed Image Id backing the custom image.
    type: str
  managed_snapshot_id:
    description:
      - The Managed Snapshot Id backing the custom image.
    type: str
  data_disk_storage_info:
    description:
      - Storage information about the data disks present in the custom image
    type: list
    suboptions:
      lun:
        description:
          - Disk Lun
        type: str
      storage_type:
        description:
          - Disk Storage Type
        type: str
        choices:
          - Standard
          - Premium
          - StandardSSD
  custom_image_plan:
    description:
      - Storage information about the plan related to this custom image
    type: dict
    suboptions:
      id:
        description:
          - 'The id of the plan, equivalent to name of the plan'
        type: str
      publisher:
        description:
          - >-
            The publisher for the plan from the marketplace image the custom
            image is derived from
        type: str
      offer:
        description:
          - >-
            The offer for the plan from the marketplace image the custom image
            is derived from
        type: str
  is_plan_authorized:
    description:
      - >-
        Whether or not the custom images underlying offer/plan has been enabled
        for programmatic deployment
    type: bool
  source_vm_id:
    description:
      - The source vm identifier.
    type: str
  windows_os_info:
    description:
      - The Windows OS information of the VM.
    type: dict
    suboptions:
      windows_os_state:
        description:
          - >-
            The state of the Windows OS (i.e. NonSysprepped, SysprepRequested,
            SysprepApplied).
        type: str
        choices:
          - NonSysprepped
          - SysprepRequested
          - SysprepApplied
  linux_os_info:
    description:
      - The Linux OS information of the VM.
    type: dict
    suboptions:
      linux_os_state:
        description:
          - >-
            The state of the Linux OS (i.e. NonDeprovisioned,
            DeprovisionRequested, DeprovisionApplied).
        type: str
        choices:
          - NonDeprovisioned
          - DeprovisionRequested
          - DeprovisionApplied
  state:
    description:
      - Assert the state of the CustomImage.
      - >-
        Use C(present) to create or update an CustomImage and C(absent) to
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
          The publisher for the plan from the marketplace image the custom image
          is derived from
      returned: always
      type: str
      sample: null
    offer:
      description:
        - >-
          The offer for the plan from the marketplace image the custom image is
          derived from
      returned: always
      type: str
      sample: null
is_plan_authorized:
  description:
    - >-
      Whether or not the custom images underlying offer/plan has been enabled
      for programmatic deployment
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


class AzureRMCustomImage(AzureRMModuleBaseExt):
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
            vhd=dict(
                type='dict',
                disposition='/vhd',
                options=dict(
                    image_name=dict(
                        type='str',
                        disposition='image_name'
                    ),
                    sys_prep=dict(
                        type='bool',
                        disposition='sys_prep'
                    ),
                    os_type=dict(
                        type='str',
                        disposition='os_type',
                        choices=['Windows',
                                 'Linux',
                                 'None'],
                        required=True
                    )
                )
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            author=dict(
                type='str',
                disposition='/author'
            ),
            managed_image_id=dict(
                type='str',
                disposition='/managed_image_id'
            ),
            managed_snapshot_id=dict(
                type='str',
                disposition='/managed_snapshot_id'
            ),
            data_disk_storage_info=dict(
                type='list',
                disposition='/data_disk_storage_info',
                elements='dict',
                options=dict(
                    lun=dict(
                        type='str',
                        disposition='lun'
                    ),
                    storage_type=dict(
                        type='str',
                        disposition='storage_type',
                        choices=['Standard',
                                 'Premium',
                                 'StandardSSD']
                    )
                )
            ),
            custom_image_plan=dict(
                type='dict',
                disposition='/custom_image_plan',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    offer=dict(
                        type='str',
                        disposition='offer'
                    )
                )
            ),
            is_plan_authorized=dict(
                type='bool',
                disposition='/is_plan_authorized'
            ),
            source_vm_id=dict(
                type='str',
                disposition='/source_vm_id'
            ),
            windows_os_info=dict(
                type='dict',
                disposition='/windows_os_info',
                options=dict(
                    windows_os_state=dict(
                        type='str',
                        disposition='windows_os_state',
                        choices=['NonSysprepped',
                                 'SysprepRequested',
                                 'SysprepApplied']
                    )
                )
            ),
            linux_os_info=dict(
                type='dict',
                disposition='/linux_os_info',
                options=dict(
                    linux_os_state=dict(
                        type='str',
                        disposition='linux_os_state',
                        choices=['NonDeprovisioned',
                                 'DeprovisionRequested',
                                 'DeprovisionApplied']
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
        self.lab_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCustomImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.custom_images.create_or_update(resource_group_name=self.resource_group_name,
                                                                       lab_name=self.lab_name,
                                                                       name=self.name,
                                                                       custom_image=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the CustomImage instance.')
            self.fail('Error creating the CustomImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.custom_images.delete(resource_group_name=self.resource_group_name,
                                                             lab_name=self.lab_name,
                                                             name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the CustomImage instance.')
            self.fail('Error deleting the CustomImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.custom_images.get(resource_group_name=self.resource_group_name,
                                                          lab_name=self.lab_name,
                                                          name=self.name,
                                                          expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCustomImage()


if __name__ == '__main__':
    main()
