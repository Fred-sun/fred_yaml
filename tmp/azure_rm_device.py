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
module: azure_rm_device
version_added: '2.9'
short_description: Manage Azure Device instance.
description:
  - 'Create, update and delete instance of Azure Device.'
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  expand:
    description:
      - >-
        Specify $expand=details to populate additional fields related to the
        device or $expand=rolloverdetails to populate additional fields related
        to the service data encryption key rollover on device
    type: str
  device_description:
    description:
      - Short description given for the device
    type: str
  state:
    description:
      - Assert the state of the Device.
      - Use C(present) to create or update an Device and C(absent) to delete it.
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
    - name: DevicesDelete
      azure_rm_device: 
        device_name: Device001ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DevicesUpdate
      azure_rm_device: 
        device_name: Device001ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        properties:
          device_description: updated device description
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the object.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
kind:
  description:
    - The Kind of the object. Currently only Series8000 is supported
  returned: always
  type: constant
  sample: null
friendly_name:
  description:
    - The friendly name of the device.
  returned: always
  type: str
  sample: null
activation_time:
  description:
    - The UTC time at which the device was activated
  returned: always
  type: str
  sample: null
culture:
  description:
    - 'The language culture setting on the device. For eg: "en-US"'
  returned: always
  type: str
  sample: null
device_description:
  description:
    - The device description.
  returned: always
  type: str
  sample: null
device_software_version:
  description:
    - The version number of the software running on the device.
  returned: always
  type: str
  sample: null
friendly_software_name:
  description:
    - The friendly name of the software running on the device.
  returned: always
  type: str
  sample: null
device_configuration_status:
  description:
    - The current configuration status of the device.
  returned: always
  type: sealed-choice
  sample: null
target_iqn:
  description:
    - The target IQN.
  returned: always
  type: str
  sample: null
model_description:
  description:
    - The device model.
  returned: always
  type: str
  sample: null
status:
  description:
    - The current status of the device.
  returned: always
  type: sealed-choice
  sample: null
serial_number:
  description:
    - The serial number.
  returned: always
  type: str
  sample: null
device_type:
  description:
    - The type of the device.
  returned: always
  type: sealed-choice
  sample: null
active_controller:
  description:
    - The identifier of the active controller of the device.
  returned: always
  type: sealed-choice
  sample: null
friendly_software_version:
  description:
    - The device friendly software version.
  returned: always
  type: str
  sample: null
available_local_storage_in_bytes:
  description:
    - The storage in bytes that is available locally on the device.
  returned: always
  type: integer
  sample: null
available_tiered_storage_in_bytes:
  description:
    - The storage in bytes that is available on the device for tiered volumes.
  returned: always
  type: integer
  sample: null
provisioned_tiered_storage_in_bytes:
  description:
    - >-
      The storage in bytes that has been provisioned on the device for tiered
      volumes.
  returned: always
  type: integer
  sample: null
provisioned_local_storage_in_bytes:
  description:
    - >-
      The storage in bytes used for locally pinned volumes on the device
      (including additional local reservation).
  returned: always
  type: integer
  sample: null
provisioned_volume_size_in_bytes:
  description:
    - Total capacity in bytes of tiered and locally pinned volumes on the device
  returned: always
  type: integer
  sample: null
using_storage_in_bytes:
  description:
    - >-
      The storage in bytes that is currently being used on the device, including
      both local and cloud.
  returned: always
  type: integer
  sample: null
total_tiered_storage_in_bytes:
  description:
    - The total tiered storage available on the device in bytes.
  returned: always
  type: integer
  sample: null
agent_group_version:
  description:
    - The device agent group version.
  returned: always
  type: integer
  sample: null
network_interface_card_count:
  description:
    - The number of network interface cards
  returned: always
  type: integer
  sample: null
device_location:
  description:
    - The location of the virtual appliance.
  returned: always
  type: str
  sample: null
virtual_machine_api_type:
  description:
    - The virtual machine API type.
  returned: always
  type: sealed-choice
  sample: null
details:
  description:
    - >-
      The additional device details regarding the end point count and volume
      container count.
  returned: always
  type: dict
  sample: null
  contains:
    endpoint_count:
      description:
        - >-
          The total number of endpoints that are currently on the device ( i.e.
          number of volumes).
      returned: always
      type: integer
      sample: null
    volume_container_count:
      description:
        - The total number of volume containers on the device.
      returned: always
      type: integer
      sample: null
rollover_details:
  description:
    - >-
      The additional device details for the service data encryption key
      rollover.
  returned: always
  type: dict
  sample: null
  contains:
    authorization_eligibility:
      description:
        - >-
          The eligibility status of device for service data encryption key
          rollover.
      returned: always
      type: sealed-choice
      sample: null
    authorization_status:
      description:
        - >-
          The authorization status of the device for service data encryption key
          rollover.
      returned: always
      type: sealed-choice
      sample: null
    in_eligibility_reason:
      description:
        - >-
          The reason for inEligibility of device, in case it's not eligible for
          service data encryption key rollover.
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDevice(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            device_description=dict(
                type='str',
                disposition='/device_description'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDevice, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
                response = self.mgmt_client.devices.create()
            else:
                response = self.mgmt_client.devices.update(device_name=self.device_name,
                                                           resource_group_name=self.resource_group_name,
                                                           manager_name=self.manager_name,
                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Device instance.')
            self.fail('Error creating the Device instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.devices.delete(device_name=self.device_name,
                                                       resource_group_name=self.resource_group_name,
                                                       manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the Device instance.')
            self.fail('Error deleting the Device instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.devices.get(device_name=self.device_name,
                                                    resource_group_name=self.resource_group_name,
                                                    manager_name=self.manager_name,
                                                    expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDevice()


if __name__ == '__main__':
    main()
