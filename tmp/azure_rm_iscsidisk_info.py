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
module: azure_rm_iscsidisk_info
version_added: '2.9'
short_description: Get IscsiDisk info.
description:
  - Get info of IscsiDisk.
options:
  device_name:
    description:
      - The device name.
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
  iscsi_server_name:
    description:
      - The iSCSI server name.
    type: str
  disk_name:
    description:
      - The disk name.
      - The iSCSI disk name.
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
    - name: IscsiDisksListByDevice
      azure_rm_iscsidisk_info: 
        device_name: HSDK-0NZI14MDTF
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiDisksListByIscsiServer
      azure_rm_iscsidisk_info: 
        device_name: HSDK-0NZI14MDTF
        iscsi_server_name: HSDK-0NZI14MDTF
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiDisksGet
      azure_rm_iscsidisk_info: 
        device_name: HSDK-0NZI14MDTF
        disk_name: Auto-TestIscsiDisk1
        iscsi_server_name: HSDK-0NZI14MDTF
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiDisksListMetrics
      azure_rm_iscsidisk_info: 
        device_name: HSDK-WSJQERQW3F
        disk_name: TieredIscsiDiskForSDKTest
        iscsi_server_name: HSDK-WSJQERQW3F
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiDisksListMetricDefinition
      azure_rm_iscsidisk_info: 
        device_name: HSDK-WSJQERQW3F
        disk_name: TieredIscsiDiskForSDKTest
        iscsi_server_name: HSDK-WSJQERQW3F
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
iscsi_disks:
  description: >-
    A list of dict results where the key is the name of the IscsiDisk and the
    values are the facts for that IscsiDisk.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          The value.
          The list of metric definition
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The description.
          returned: always
          type: str
          sample: null
        disk_status:
          description:
            - The disk status.
          returned: always
          type: sealed-choice
          sample: null
        access_control_records:
          description:
            - The access control records.
          returned: always
          type: list
          sample: null
        data_policy:
          description:
            - The data policy.
          returned: always
          type: sealed-choice
          sample: null
        provisioned_capacity_in_bytes:
          description:
            - The provisioned capacity in bytes.
          returned: always
          type: integer
          sample: null
        used_capacity_in_bytes:
          description:
            - The used capacity in bytes.
          returned: always
          type: integer
          sample: null
        local_used_capacity_in_bytes:
          description:
            - The local used capacity in bytes.
          returned: always
          type: integer
          sample: null
        monitoring_status:
          description:
            - The monitoring.
          returned: always
          type: sealed-choice
          sample: null
    id:
      description:
        - The identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description.
      returned: always
      type: str
      sample: null
    disk_status:
      description:
        - The disk status.
      returned: always
      type: sealed-choice
      sample: null
    access_control_records:
      description:
        - The access control records.
      returned: always
      type: list
      sample: null
    data_policy:
      description:
        - The data policy.
      returned: always
      type: sealed-choice
      sample: null
    provisioned_capacity_in_bytes:
      description:
        - The provisioned capacity in bytes.
      returned: always
      type: integer
      sample: null
    used_capacity_in_bytes:
      description:
        - The used capacity in bytes.
      returned: always
      type: integer
      sample: null
    local_used_capacity_in_bytes:
      description:
        - The local used capacity in bytes.
      returned: always
      type: integer
      sample: null
    monitoring_status:
      description:
        - The monitoring.
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMIscsiDiskInfo(AzureRMModuleBase):
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
            iscsi_server_name=dict(
                type='str'
            ),
            disk_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.iscsi_server_name = None
        self.disk_name = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-10-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMIscsiDiskInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

        if (self.device_name is not None and
            self.iscsi_server_name is not None and
            self.disk_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['iscsi_disks'] = self.format_item(self.listmetric())
        elif (self.device_name is not None and
              self.iscsi_server_name is not None and
              self.disk_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_disks'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.iscsi_server_name is not None and
              self.disk_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_disks'] = self.format_item(self.listmetricdefinition())
        elif (self.device_name is not None and
              self.iscsi_server_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_disks'] = self.format_item(self.listbyiscsiserver())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_disks'] = self.format_item(self.listbydevice())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_disks.list_metric(device_name=self.device_name,
                                                                iscsi_server_name=self.iscsi_server_name,
                                                                disk_name=self.disk_name,
                                                                resource_group_name=self.resource_group_name,
                                                                manager_name=self.manager_name,
                                                                filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_disks.get(device_name=self.device_name,
                                                        iscsi_server_name=self.iscsi_server_name,
                                                        disk_name=self.disk_name,
                                                        resource_group_name=self.resource_group_name,
                                                        manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_disks.list_metric_definition(device_name=self.device_name,
                                                                           iscsi_server_name=self.iscsi_server_name,
                                                                           disk_name=self.disk_name,
                                                                           resource_group_name=self.resource_group_name,
                                                                           manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyiscsiserver(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_disks.list_by_iscsi_server(device_name=self.device_name,
                                                                         iscsi_server_name=self.iscsi_server_name,
                                                                         resource_group_name=self.resource_group_name,
                                                                         manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_disks.list_by_device(device_name=self.device_name,
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
    AzureRMIscsiDiskInfo()


if __name__ == '__main__':
    main()
