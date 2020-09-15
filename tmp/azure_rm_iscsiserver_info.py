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
module: azure_rm_iscsiserver_info
version_added: '2.9'
short_description: Get IscsiServer info.
description:
  - Get info of IscsiServer.
options:
  device_name:
    description:
      - The device name.
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
    - name: IscsiServersListByDevice
      azure_rm_iscsiserver_info: 
        device_name: HSDK-UGU4PITWNI
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiServersGet
      azure_rm_iscsiserver_info: 
        device_name: HSDK-WSJQERQW3F
        iscsi_server_name: HSDK-WSJQERQW3F
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiServersListMetrics
      azure_rm_iscsiserver_info: 
        device_name: HSDK-UGU4PITWNI
        iscsi_server_name: HSDK-UGU4PITWNI
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiServersListMetricDefinition
      azure_rm_iscsiserver_info: 
        device_name: HSDK-UGU4PITWNI
        iscsi_server_name: HSDK-UGU4PITWNI
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiServersListByManager
      azure_rm_iscsiserver_info: 
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
iscsi_servers:
  description: >-
    A list of dict results where the key is the name of the IscsiServer and the
    values are the facts for that IscsiServer.
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
        storage_domain_id:
          description:
            - The storage domain id.
          returned: always
          type: str
          sample: null
        backup_schedule_group_id:
          description:
            - The backup policy id.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The description.
          returned: always
          type: str
          sample: null
        chap_id:
          description:
            - The chap id.
          returned: always
          type: str
          sample: null
        reverse_chap_id:
          description:
            - The reverse chap id.
          returned: always
          type: str
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
    storage_domain_id:
      description:
        - The storage domain id.
      returned: always
      type: str
      sample: null
    backup_schedule_group_id:
      description:
        - The backup policy id.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description.
      returned: always
      type: str
      sample: null
    chap_id:
      description:
        - The chap id.
      returned: always
      type: str
      sample: null
    reverse_chap_id:
      description:
        - The reverse chap id.
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
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMIscsiServerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
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
            iscsi_server_name=dict(
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
        super(AzureRMIscsiServerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

        if (self.device_name is not None and
            self.iscsi_server_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['iscsi_servers'] = self.format_item(self.listmetric())
        elif (self.device_name is not None and
              self.iscsi_server_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_servers'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.iscsi_server_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_servers'] = self.format_item(self.listmetricdefinition())
        elif (self.device_name is not None and
              self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_servers'] = self.format_item(self.listbydevice())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['iscsi_servers'] = self.format_item(self.listbymanager())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_servers.list_metric(device_name=self.device_name,
                                                                  iscsi_server_name=self.iscsi_server_name,
                                                                  resource_group_name=self.resource_group_name,
                                                                  manager_name=self.manager_name,
                                                                  filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_servers.get(device_name=self.device_name,
                                                          iscsi_server_name=self.iscsi_server_name,
                                                          resource_group_name=self.resource_group_name,
                                                          manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_servers.list_metric_definition(device_name=self.device_name,
                                                                             iscsi_server_name=self.iscsi_server_name,
                                                                             resource_group_name=self.resource_group_name,
                                                                             manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydevice(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_servers.list_by_device(device_name=self.device_name,
                                                                     resource_group_name=self.resource_group_name,
                                                                     manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanager(self):
        response = None

        try:
            response = self.mgmt_client.iscsi_servers.list_by_manager(resource_group_name=self.resource_group_name,
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
    AzureRMIscsiServerInfo()


if __name__ == '__main__':
    main()
