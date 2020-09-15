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
module: azure_rm_chapsetting_info
version_added: '2.9'
short_description: Get ChapSetting info.
description:
  - Get info of ChapSetting.
options:
  device_name:
    description:
      - The name of the device.
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
  chap_user_name:
    description:
      - The user name of chap to be fetched.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ChapSettingsListByDevice
      azure_rm_chapsetting_info: 
        device_name: HSDK-0NZI14MDTF
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ChapSettingsGet
      azure_rm_chapsetting_info: 
        chap_user_name: ChapSettingForSDK
        device_name: HSDK-WSJQERQW3F
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
chap_settings:
  description: >-
    A list of dict results where the key is the name of the ChapSetting and the
    values are the facts for that ChapSetting.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The chap settings entity collection
      returned: always
      type: list
      sample: null
      contains:
        password:
          description:
            - The chap password.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - >-
                  The value of the secret itself. If the secret is in plaintext
                  then EncryptionAlgorithm will be none and
                  EncryptionCertThumbprint will be null.
              returned: always
              type: str
              sample: null
            encryption_certificate_thumbprint:
              description:
                - Thumbprint certificate that was used to encrypt "Value"
              returned: always
              type: str
              sample: null
            encryption_algorithm:
              description:
                - Algorithm used to encrypt "Value"
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
    password:
      description:
        - The chap password.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - >-
              The value of the secret itself. If the secret is in plaintext then
              EncryptionAlgorithm will be none and EncryptionCertThumbprint will
              be null.
          returned: always
          type: str
          sample: null
        encryption_certificate_thumbprint:
          description:
            - Thumbprint certificate that was used to encrypt "Value"
          returned: always
          type: str
          sample: null
        encryption_algorithm:
          description:
            - Algorithm used to encrypt "Value"
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


class AzureRMChapSettingInfo(AzureRMModuleBase):
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
            chap_user_name=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.chap_user_name = None

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
        super(AzureRMChapSettingInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

        if (self.device_name is not None and
            self.chap_user_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['chap_settings'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['chap_settings'] = self.format_item(self.listbydevice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.chap_settings.get(device_name=self.device_name,
                                                          chap_user_name=self.chap_user_name,
                                                          resource_group_name=self.resource_group_name,
                                                          manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.chap_settings.list_by_device(device_name=self.device_name,
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
    AzureRMChapSettingInfo()


if __name__ == '__main__':
    main()
