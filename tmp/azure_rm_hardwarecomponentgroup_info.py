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
module: azure_rm_hardwarecomponentgroup_info
version_added: '2.9'
short_description: Get HardwareComponentGroup info.
description:
  - Get info of HardwareComponentGroup.
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
    - name: HardwareComponentGroupsListByDevice
      azure_rm_hardwarecomponentgroup_info: 
        device_name: Device05ForSDKTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
hardware_component_groups:
  description: >-
    A list of dict results where the key is the name of the
    HardwareComponentGroup and the values are the facts for that
    HardwareComponentGroup.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        display_name:
          description:
            - The display name the hardware component group.
          returned: always
          type: str
          sample: null
        last_updated_time:
          description:
            - The last updated time.
          returned: always
          type: str
          sample: null
        components:
          description:
            - The list of hardware components.
          returned: always
          type: list
          sample: null
          contains:
            component_id:
              description:
                - The component ID.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The display name of the hardware component.
              returned: always
              type: str
              sample: null
            status:
              description:
                - The status of the hardware component.
              returned: always
              type: sealed-choice
              sample: null
            status_display_name:
              description:
                - The display name of the status of hardware component.
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


class AzureRMHardwareComponentGroupInfo(AzureRMModuleBase):
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
        super(AzureRMHardwareComponentGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.device_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['hardware_component_groups'] = self.format_item(self.listbydevice())
        return self.results

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.hardware_component_groups.list_by_device(device_name=self.device_name,
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
    AzureRMHardwareComponentGroupInfo()


if __name__ == '__main__':
    main()
