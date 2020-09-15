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
module: azure_rm_devicesetting_info
version_added: '2.9'
short_description: Get DeviceSetting info.
description:
  - Get info of DeviceSetting.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DeviceSettingsGetAlertSettings
      azure_rm_devicesetting_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DeviceSettingsGetNetworkSettings
      azure_rm_devicesetting_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DeviceSettingsGetSecuritySettings
      azure_rm_devicesetting_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DeviceSettingsGetTimeSettings
      azure_rm_devicesetting_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
device_settings:
  description: >-
    A list of dict results where the key is the name of the DeviceSetting and
    the values are the facts for that DeviceSetting.
  returned: always
  type: complex
  contains:
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
    email_notification:
      description:
        - Indicates whether email notification enabled or not.
      returned: always
      type: sealed-choice
      sample: null
    alert_notification_culture:
      description:
        - The alert notification culture.
      returned: always
      type: str
      sample: null
    notification_to_service_owners:
      description:
        - >-
          The value indicating whether alert notification enabled for admin or
          not.
      returned: always
      type: sealed-choice
      sample: null
    additional_recipient_email_list:
      description:
        - The alert notification email list.
      returned: always
      type: list
      sample: null
    dns_settings:
      description:
        - The DNS (Domain Name System) settings of device.
      returned: always
      type: dict
      sample: null
      contains:
        primary_dns_server:
          description:
            - The primary IPv4 DNS server for the device
          returned: always
          type: str
          sample: null
        primary_ipv6dns_server:
          description:
            - The primary IPv6 DNS server for the device
          returned: always
          type: str
          sample: null
        secondary_dns_servers:
          description:
            - The secondary IPv4 DNS server for the device
          returned: always
          type: list
          sample: null
        secondary_ipv6dns_servers:
          description:
            - The secondary IPv6 DNS server for the device
          returned: always
          type: list
          sample: null
    network_adapters:
      description:
        - The network adapter list of device.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - The value.
          returned: always
          type: list
          sample: null
          contains:
            interface_id:
              description:
                - The ID of the network adapter.
              returned: always
              type: sealed-choice
              sample: null
            net_interface_status:
              description:
                - Value indicating status of network adapter.
              returned: always
              type: sealed-choice
              sample: null
            is_default:
              description:
                - Value indicating whether this instance is default.
              returned: always
              type: bool
              sample: null
            iscsi_and_cloud_status:
              description:
                - Value indicating cloud and ISCSI status of network adapter.
              returned: always
              type: sealed-choice
              sample: null
            speed:
              description:
                - The speed of the network adapter.
              returned: always
              type: integer
              sample: null
            mode:
              description:
                - 'The mode of network adapter, either IPv4, IPv6 or both.'
              returned: always
              type: sealed-choice
              sample: null
            nic_ipv4settings:
              description:
                - The IPv4 configuration of the network adapter.
              returned: always
              type: dict
              sample: null
              contains:
                ipv4address:
                  description:
                    - The IPv4 address of the network adapter.
                  returned: always
                  type: str
                  sample: null
                ipv4netmask:
                  description:
                    - The IPv4 netmask of the network adapter.
                  returned: always
                  type: str
                  sample: null
                ipv4gateway:
                  description:
                    - The IPv4 gateway of the network adapter.
                  returned: always
                  type: str
                  sample: null
                controller0ipv4address:
                  description:
                    - The IPv4 address of Controller0.
                  returned: always
                  type: str
                  sample: null
                controller1ipv4address:
                  description:
                    - The IPv4 address of Controller1.
                  returned: always
                  type: str
                  sample: null
            nic_ipv6settings:
              description:
                - The IPv6 configuration of the network adapter.
              returned: always
              type: dict
              sample: null
              contains:
                ipv6address:
                  description:
                    - The IPv6 address of the network adapter.
                  returned: always
                  type: str
                  sample: null
                ipv6prefix:
                  description:
                    - The IPv6 prefix of the network adapter.
                  returned: always
                  type: str
                  sample: null
                ipv6gateway:
                  description:
                    - The IPv6 gateway of the network adapter.
                  returned: always
                  type: str
                  sample: null
                controller0ipv6address:
                  description:
                    - The IPv6 address of Controller0.
                  returned: always
                  type: str
                  sample: null
                controller1ipv6address:
                  description:
                    - The IPv6 address of Controller1.
                  returned: always
                  type: str
                  sample: null
    webproxy_settings:
      description:
        - The webproxy settings of device.
      returned: always
      type: dict
      sample: null
      contains:
        connection_uri:
          description:
            - The connection URI.
          returned: always
          type: str
          sample: null
        authentication:
          description:
            - The authentication type.
          returned: always
          type: sealed-choice
          sample: null
        username:
          description:
            - The webproxy username.
          returned: always
          type: str
          sample: null
    remote_management_settings:
      description:
        - The settings for remote management of a device.
      returned: always
      type: dict
      sample: null
      contains:
        remote_management_mode:
          description:
            - The remote management mode.
          returned: always
          type: sealed-choice
          sample: null
        remote_management_certificate:
          description:
            - The remote management certificates.
          returned: always
          type: str
          sample: null
    chap_settings:
      description:
        - The Challenge-Handshake Authentication Protocol (CHAP) settings.
      returned: always
      type: dict
      sample: null
      contains:
        initiator_user:
          description:
            - The CHAP initiator user.
          returned: always
          type: str
          sample: null
        initiator_secret:
          description:
            - The CHAP initiator secret.
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
        target_user:
          description:
            - The CHAP target user.
          returned: always
          type: str
          sample: null
        target_secret:
          description:
            - The target secret.
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
    time_zone:
      description:
        - 'The timezone of device, like ''(UTC -06:00) Central America'''
      returned: always
      type: str
      sample: null
    primary_time_server:
      description:
        - >-
          The primary Network Time Protocol (NTP) server name, like
          'time.windows.com'.
      returned: always
      type: str
      sample: null
    secondary_time_server:
      description:
        - >-
          The secondary Network Time Protocol (NTP) server name, like
          'time.contoso.com'. It's optional.
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


class AzureRMDeviceSettingInfo(AzureRMModuleBase):
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
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None

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
        super(AzureRMDeviceSettingInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['device_settings'] = self.format_item(self.getalertsetting())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['device_settings'] = self.format_item(self.getnetworksetting())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['device_settings'] = self.format_item(self.getsecuritysetting())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['device_settings'] = self.format_item(self.gettimesetting())
        return self.results

    def getalertsetting(self):
        response = None

        try:
            response = self.mgmt_client.device_settings.get_alert_setting(device_name=self.device_name,
                                                                          resource_group_name=self.resource_group_name,
                                                                          manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getnetworksetting(self):
        response = None

        try:
            response = self.mgmt_client.device_settings.get_network_setting(device_name=self.device_name,
                                                                            resource_group_name=self.resource_group_name,
                                                                            manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getsecuritysetting(self):
        response = None

        try:
            response = self.mgmt_client.device_settings.get_security_setting(device_name=self.device_name,
                                                                             resource_group_name=self.resource_group_name,
                                                                             manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def gettimesetting(self):
        response = None

        try:
            response = self.mgmt_client.device_settings.get_time_setting(device_name=self.device_name,
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
    AzureRMDeviceSettingInfo()


if __name__ == '__main__':
    main()
