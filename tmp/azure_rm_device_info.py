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
module: azure_rm_device_info
version_added: '2.9'
short_description: Get Device info.
description:
  - Get info of Device.
options:
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
  device_name:
    description:
      - The device name
    type: str
  filter:
    description:
      - OData Filter options
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DevicesListByManager
      azure_rm_device_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DevicesGet
      azure_rm_device_info: 
        device_name: Device001ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DevicesListMetrics
      azure_rm_device_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DevicesListMetricDefinition
      azure_rm_device_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DevicesGetUpdateSummary
      azure_rm_device_info: 
        device_name: sugattdeviceforSDK
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
devices:
  description: >-
    A list of dict results where the key is the name of the Device and the
    values are the facts for that Device.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          The value.
          The list of metric definitions.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              The storage in bytes that is available on the device for tiered
              volumes.
          returned: always
          type: integer
          sample: null
        provisioned_tiered_storage_in_bytes:
          description:
            - >-
              The storage in bytes that has been provisioned on the device for
              tiered volumes.
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
            - >-
              Total capacity in bytes of tiered and locally pinned volumes on
              the device
          returned: always
          type: integer
          sample: null
        using_storage_in_bytes:
          description:
            - >-
              The storage in bytes that is currently being used on the device,
              including both local and cloud.
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
              The additional device details regarding the end point count and
              volume container count.
          returned: always
          type: dict
          sample: null
          contains:
            endpoint_count:
              description:
                - >-
                  The total number of endpoints that are currently on the device
                  ( i.e. number of volumes).
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
                  The eligibility status of device for service data encryption
                  key rollover.
              returned: always
              type: sealed-choice
              sample: null
            authorization_status:
              description:
                - >-
                  The authorization status of the device for service data
                  encryption key rollover.
              returned: always
              type: sealed-choice
              sample: null
            in_eligibility_reason:
              description:
                - >-
                  The reason for inEligibility of device, in case it's not
                  eligible for service data encryption key rollover.
              returned: always
              type: sealed-choice
              sample: null
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
        - >-
          The storage in bytes that is available on the device for tiered
          volumes.
      returned: always
      type: integer
      sample: null
    provisioned_tiered_storage_in_bytes:
      description:
        - >-
          The storage in bytes that has been provisioned on the device for
          tiered volumes.
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
        - >-
          Total capacity in bytes of tiered and locally pinned volumes on the
          device
      returned: always
      type: integer
      sample: null
    using_storage_in_bytes:
      description:
        - >-
          The storage in bytes that is currently being used on the device,
          including both local and cloud.
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
              The total number of endpoints that are currently on the device (
              i.e. number of volumes).
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
              The authorization status of the device for service data encryption
              key rollover.
          returned: always
          type: sealed-choice
          sample: null
        in_eligibility_reason:
          description:
            - >-
              The reason for inEligibility of device, in case it's not eligible
              for service data encryption key rollover.
          returned: always
          type: sealed-choice
          sample: null
    regular_updates_available:
      description:
        - Set to 'true' if regular updates are available for the device.
      returned: always
      type: bool
      sample: null
    maintenance_mode_updates_available:
      description:
        - Set to 'true' if maintenance mode update available.
      returned: always
      type: bool
      sample: null
    is_update_in_progress:
      description:
        - Indicates whether an update is in progress or not.
      returned: always
      type: bool
      sample: null
    last_updated_time:
      description:
        - The time when the last update was completed.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDeviceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
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
            device_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.manager_name = None
        self.expand = None
        self.device_name = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDeviceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None and
            self.filter is not None):
            self.results['devices'] = self.format_item(self.listmetric())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['devices'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['devices'] = self.format_item(self.listmetricdefinition())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['devices'] = self.format_item(self.getupdatesummary())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['devices'] = self.format_item(self.listbymanager())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.devices.list_metric(device_name=self.device_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name,
                                                            filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.devices.get(device_name=self.device_name,
                                                    resource_group_name=self.resource_group_name,
                                                    manager_name=self.manager_name,
                                                    expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.devices.list_metric_definition(device_name=self.device_name,
                                                                       resource_group_name=self.resource_group_name,
                                                                       manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getupdatesummary(self):
        response = None

        try:
            response = self.mgmt_client.devices.get_update_summary(device_name=self.device_name,
                                                                   resource_group_name=self.resource_group_name,
                                                                   manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanager(self):
        response = None

        try:
            response = self.mgmt_client.devices.list_by_manager(resource_group_name=self.resource_group_name,
                                                                manager_name=self.manager_name,
                                                                expand=self.expand)
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
    AzureRMDeviceInfo()


if __name__ == '__main__':
    main()
