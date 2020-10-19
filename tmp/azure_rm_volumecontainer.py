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
module: azure_rm_volumecontainer
version_added: '2.9'
short_description: Manage Azure VolumeContainer instance.
description:
  - 'Create, update and delete instance of Azure VolumeContainer.'
options:
  device_name:
    description:
      - The device name
    required: true
    type: str
  volume_container_name:
    description:
      - The name of the volume container.
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
  kind:
    description:
      - The Kind of the object. Currently only Series8000 is supported
    type: constant
  encryption_key:
    description:
      - >-
        The key used to encrypt data in the volume container. It is required
        when property 'EncryptionStatus' is "Enabled".
    type: dict
    suboptions:
      value:
        description:
          - The value of the secret.
        required: true
        type: str
      encryption_cert_thumbprint:
        description:
          - >-
            Thumbprint certificate that was used to encrypt "Value". If the
            value in unencrypted, it will be null.
        type: str
      encryption_algorithm:
        description:
          - The algorithm used to encrypt "Value".
        required: true
        type: sealed-choice
  storage_account_credential_id:
    description:
      - The path ID of storage account associated with the volume container.
    type: str
  band_width_rate_in_mbps:
    description:
      - The bandwidth-rate set on the volume container.
    type: integer
  bandwidth_setting_id:
    description:
      - The ID of the bandwidth setting associated with the volume container.
    type: str
  state:
    description:
      - Assert the state of the VolumeContainer.
      - >-
        Use C(present) to create or update an VolumeContainer and C(absent) to
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
    - name: VolumeContainersCreateOrUpdate
      azure_rm_volumecontainer: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: VolumeContainerForSDKTest
        properties:
          bandwidth_setting_id: >-
            /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/ResourceGroupForSDKTest/providers/Microsoft.StorSimple/managers/ManagerForSDKTest1/bandwidthSettings/bandwidthSetting1
          encryption_key:
            encryption_algorithm: RSAES_PKCS1_v_1_5
            encryption_cert_thumbprint: A872A2DF196AC7682EE24791E7DE2E2A360F5926
            value: >-
              R//pyVLx/fn58ia098JiLgZB5RY7fVT+6o8a4fmsvjy+ls2UgJphMf25XVqEQCZnsp/5uxteN1M/9ArPIICdhM7M1+b/Ur7kJ0FH0ktxfk7CrPWWJLI4q20LZoduJGI56lREav1VpuLdqw5F9fRcq7zbfgPQ3B/SD0mfumNRiV+AnwbC6msfavIuWrhVDl9iSzEPE+zU06/kpsexnrS81yYT2QlVVUbvpY4F3zfH8TQPpAROTbv2pld6JO4eGOrZ5O1iOr6XCg2TY2W/jf+Ev4z5tqC9VWXE5kh65gjBfpWN0bDWXKekqEhor2crHAxZi4dybdY8Ok1MDWd1CSU8kw==
          storage_account_credential_id: >-
            /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/ResourceGroupForSDKTest/providers/Microsoft.StorSimple/managers/ManagerForSDKTest1/storageAccountCredentials/safortestrecording
        

    - name: VolumeContainersDelete
      azure_rm_volumecontainer: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        volume_container_name: VolumeContainerForSDKTest
        

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
encryption_key:
  description:
    - >-
      The key used to encrypt data in the volume container. It is required when
      property 'EncryptionStatus' is "Enabled".
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
          Thumbprint certificate that was used to encrypt "Value". If the value
          in unencrypted, it will be null.
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


class AzureRMVolumeContainer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            volume_container_name=dict(
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
            kind=dict(
                type='constant',
                disposition='/kind'
            ),
            encryption_key=dict(
                type='dict',
                disposition='/encryption_key',
                options=dict(
                    value=dict(
                        type='str',
                        disposition='value',
                        required=True
                    ),
                    encryption_cert_thumbprint=dict(
                        type='str',
                        disposition='encryption_cert_thumbprint'
                    ),
                    encryption_algorithm=dict(
                        type='sealed-choice',
                        disposition='encryption_algorithm',
                        required=True
                    )
                )
            ),
            storage_account_credential_id=dict(
                type='str',
                disposition='/storage_account_credential_id'
            ),
            band_width_rate_in_mbps=dict(
                type='integer',
                disposition='/band_width_rate_in_mbps'
            ),
            bandwidth_setting_id=dict(
                type='str',
                disposition='/bandwidth_setting_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.volume_container_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVolumeContainer, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.volume_containers.create_or_update(device_name=self.device_name,
                                                                           volume_container_name=self.volume_container_name,
                                                                           resource_group_name=self.resource_group_name,
                                                                           manager_name=self.manager_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VolumeContainer instance.')
            self.fail('Error creating the VolumeContainer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.volume_containers.delete(device_name=self.device_name,
                                                                 volume_container_name=self.volume_container_name,
                                                                 resource_group_name=self.resource_group_name,
                                                                 manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the VolumeContainer instance.')
            self.fail('Error deleting the VolumeContainer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.volume_containers.get(device_name=self.device_name,
                                                              volume_container_name=self.volume_container_name,
                                                              resource_group_name=self.resource_group_name,
                                                              manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVolumeContainer()


if __name__ == '__main__':
    main()
