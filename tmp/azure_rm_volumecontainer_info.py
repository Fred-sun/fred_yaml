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
module: azure_rm_volumecontainer_info
version_added: '2.9'
short_description: Get VolumeContainer info.
description:
  - Get info of VolumeContainer.
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
  volume_container_name:
    description:
      - The name of the volume container.
      - The volume container name.
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
    - name: VolumeContainersListByDevice
      azure_rm_volumecontainer_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: VolumeContainersGet
      azure_rm_volumecontainer_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: VolumeContainerForSDKTest
        

    - name: VolumeContainersListMetrics
      azure_rm_volumecontainer_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: vcForOdataFilterTest
        

    - name: VolumeContainersListMetricDefinition
      azure_rm_volumecontainer_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: vcForOdataFilterTest
        

'''

RETURN = '''
volume_containers:
  description: >-
    A list of dict results where the key is the name of the VolumeContainer and
    the values are the facts for that VolumeContainer.
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
        encryption_key:
          description:
            - >-
              The key used to encrypt data in the volume container. It is
              required when property 'EncryptionStatus' is "Enabled".
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - The value of the secret.
              returned: always
              type: str
              sample: null
            encryption_cert_thumbprint:
              description:
                - >-
                  Thumbprint certificate that was used to encrypt "Value". If
                  the value in unencrypted, it will be null.
              returned: always
              type: str
              sample: null
            encryption_algorithm:
              description:
                - The algorithm used to encrypt "Value".
              returned: always
              type: sealed-choice
              sample: null
        encryption_status:
          description:
            - The flag to denote whether encryption is enabled or not.
          returned: always
          type: sealed-choice
          sample: null
        volume_count:
          description:
            - The number of volumes in the volume Container.
          returned: always
          type: integer
          sample: null
        storage_account_credential_id:
          description:
            - >-
              The path ID of storage account associated with the volume
              container.
          returned: always
          type: str
          sample: null
        owner_ship_status:
          description:
            - >-
              The owner ship status of the volume container. Only when the
              status is "NotOwned", the delete operation on the volume container
              is permitted.
          returned: always
          type: sealed-choice
          sample: null
        band_width_rate_in_mbps:
          description:
            - The bandwidth-rate set on the volume container.
          returned: always
          type: integer
          sample: null
        bandwidth_setting_id:
          description:
            - >-
              The ID of the bandwidth setting associated with the volume
              container.
          returned: always
          type: str
          sample: null
        total_cloud_storage_usage_in_bytes:
          description:
            - The total cloud storage for the volume container.
          returned: always
          type: integer
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
    encryption_key:
      description:
        - >-
          The key used to encrypt data in the volume container. It is required
          when property 'EncryptionStatus' is "Enabled".
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - The value of the secret.
          returned: always
          type: str
          sample: null
        encryption_cert_thumbprint:
          description:
            - >-
              Thumbprint certificate that was used to encrypt "Value". If the
              value in unencrypted, it will be null.
          returned: always
          type: str
          sample: null
        encryption_algorithm:
          description:
            - The algorithm used to encrypt "Value".
          returned: always
          type: sealed-choice
          sample: null
    encryption_status:
      description:
        - The flag to denote whether encryption is enabled or not.
      returned: always
      type: sealed-choice
      sample: null
    volume_count:
      description:
        - The number of volumes in the volume Container.
      returned: always
      type: integer
      sample: null
    storage_account_credential_id:
      description:
        - The path ID of storage account associated with the volume container.
      returned: always
      type: str
      sample: null
    owner_ship_status:
      description:
        - >-
          The owner ship status of the volume container. Only when the status is
          "NotOwned", the delete operation on the volume container is permitted.
      returned: always
      type: sealed-choice
      sample: null
    band_width_rate_in_mbps:
      description:
        - The bandwidth-rate set on the volume container.
      returned: always
      type: integer
      sample: null
    bandwidth_setting_id:
      description:
        - The ID of the bandwidth setting associated with the volume container.
      returned: always
      type: str
      sample: null
    total_cloud_storage_usage_in_bytes:
      description:
        - The total cloud storage for the volume container.
      returned: always
      type: integer
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


class AzureRMVolumeContainerInfo(AzureRMModuleBase):
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
            volume_container_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.volume_container_name = None
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
        super(AzureRMVolumeContainerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.volume_container_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None and
            self.filter is not None):
            self.results['volume_containers'] = self.format_item(self.listmetric())
        elif (self.device_name is not None and
              self.volume_container_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volume_containers'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.volume_container_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volume_containers'] = self.format_item(self.listmetricdefinition())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['volume_containers'] = self.format_item(self.listbydevice())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.volume_containers.list_metric(device_name=self.device_name,
                                                                      volume_container_name=self.volume_container_name,
                                                                      resource_group_name=self.resource_group_name,
                                                                      manager_name=self.manager_name,
                                                                      filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.volume_containers.get(device_name=self.device_name,
                                                              volume_container_name=self.volume_container_name,
                                                              resource_group_name=self.resource_group_name,
                                                              manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.volume_containers.list_metric_definition(device_name=self.device_name,
                                                                                 volume_container_name=self.volume_container_name,
                                                                                 resource_group_name=self.resource_group_name,
                                                                                 manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.volume_containers.list_by_device(device_name=self.device_name,
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
    AzureRMVolumeContainerInfo()


if __name__ == '__main__':
    main()
