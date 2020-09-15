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
module: azure_rm_volume_info
version_added: '2.9'
short_description: Get Volume info.
description:
  - Get info of Volume.
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  volume_container_name:
    description:
      - The volume container name.
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
  volume_name:
    description:
      - The volume name.
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
    - name: VolumesListByVolumeContainer
      azure_rm_volume_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: volumeContainerForSDKTest
        

    - name: VolumesGet
      azure_rm_volume_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: VolumeContainerForSDKTest
        volume_name: Volume1ForSDKTest
        

    - name: VolumesListMetrics
      azure_rm_volume_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: vcForOdataFilterTest
        volume_name: CloneVolForSDKTest890836587
        

    - name: VolumesListMetricDefinition
      azure_rm_volume_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: vcForOdataFilterTest
        volume_name: CloneVolForSDKTest890836587
        

    - name: VolumesListByDevice
      azure_rm_volume_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
volumes:
  description: >-
    A list of dict results where the key is the name of the Volume and the
    values are the facts for that Volume.
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
        size_in_bytes:
          description:
            - The size of the volume in bytes.
          returned: always
          type: integer
          sample: null
        volume_type:
          description:
            - The type of the volume.
          returned: always
          type: sealed-choice
          sample: null
        volume_container_id:
          description:
            - 'The ID of the volume container, in which this volume is created.'
          returned: always
          type: str
          sample: null
        access_control_record_ids:
          description:
            - 'The IDs of the access control records, associated with the volume.'
          returned: always
          type: list
          sample: null
        volume_status:
          description:
            - The volume status.
          returned: always
          type: sealed-choice
          sample: null
        operation_status:
          description:
            - The operation status on the volume.
          returned: always
          type: sealed-choice
          sample: null
        backup_status:
          description:
            - The backup status of the volume.
          returned: always
          type: sealed-choice
          sample: null
        monitoring_status:
          description:
            - The monitoring status of the volume.
          returned: always
          type: sealed-choice
          sample: null
        backup_policy_ids:
          description:
            - 'The IDs of the backup policies, in which this volume is part of.'
          returned: always
          type: list
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
    size_in_bytes:
      description:
        - The size of the volume in bytes.
      returned: always
      type: integer
      sample: null
    volume_type:
      description:
        - The type of the volume.
      returned: always
      type: sealed-choice
      sample: null
    volume_container_id:
      description:
        - 'The ID of the volume container, in which this volume is created.'
      returned: always
      type: str
      sample: null
    access_control_record_ids:
      description:
        - 'The IDs of the access control records, associated with the volume.'
      returned: always
      type: list
      sample: null
    volume_status:
      description:
        - The volume status.
      returned: always
      type: sealed-choice
      sample: null
    operation_status:
      description:
        - The operation status on the volume.
      returned: always
      type: sealed-choice
      sample: null
    backup_status:
      description:
        - The backup status of the volume.
      returned: always
      type: sealed-choice
      sample: null
    monitoring_status:
      description:
        - The monitoring status of the volume.
      returned: always
      type: sealed-choice
      sample: null
    backup_policy_ids:
      description:
        - 'The IDs of the backup policies, in which this volume is part of.'
      returned: always
      type: list
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


class AzureRMVolumeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            volume_container_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            volume_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.device_name = None
        self.volume_container_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.volume_name = None
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
        super(AzureRMVolumeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.volume_container_name is not None and
            self.volume_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None and
            self.filter is not None):
            self.results['volumes'] = self.format_item(self.listmetric())
        elif (self.device_name is not None and
              self.volume_container_name is not None and
              self.volume_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volumes'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.volume_container_name is not None and
              self.volume_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volumes'] = self.format_item(self.listmetricdefinition())
        elif (self.device_name is not None and
              self.volume_container_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volumes'] = self.format_item(self.listbyvolumecontainer())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volumes'] = self.format_item(self.listbydevice())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.volumes.list_metric(device_name=self.device_name,
                                                            volume_container_name=self.volume_container_name,
                                                            volume_name=self.volume_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name,
                                                            filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.volumes.get(device_name=self.device_name,
                                                    volume_container_name=self.volume_container_name,
                                                    volume_name=self.volume_name,
                                                    resource_group_name=self.resource_group_name,
                                                    manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.volumes.list_metric_definition(device_name=self.device_name,
                                                                       volume_container_name=self.volume_container_name,
                                                                       volume_name=self.volume_name,
                                                                       resource_group_name=self.resource_group_name,
                                                                       manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyvolumecontainer(self):
        response = None

        try:
            response = self.mgmt_client.volumes.list_by_volume_container(device_name=self.device_name,
                                                                         volume_container_name=self.volume_container_name,
                                                                         resource_group_name=self.resource_group_name,
                                                                         manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.volumes.list_by_device(device_name=self.device_name,
                                                               resource_group_name=self.resource_group_name,
                                                               manager_name=self.manager_name)
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
    AzureRMVolumeInfo()


if __name__ == '__main__':
    main()
