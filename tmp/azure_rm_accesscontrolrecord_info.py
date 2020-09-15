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
module: azure_rm_accesscontrolrecord_info
version_added: '2.9'
short_description: Get AccessControlRecord info.
description:
  - Get info of AccessControlRecord.
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
  access_control_record_name:
    description:
      - Name of access control record to be fetched.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: AccessControlRecordsListByManager
      azure_rm_accesscontrolrecord_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: AccessControlRecordsGet
      azure_rm_accesscontrolrecord_info: 
        access_control_record_name: ACRForTest
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
access_control_records:
  description: >-
    A list of dict results where the key is the name of the AccessControlRecord
    and the values are the facts for that AccessControlRecord.
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
        initiator_name:
          description:
            - The iSCSI initiator name (IQN).
          returned: always
          type: str
          sample: null
        volume_count:
          description:
            - The number of volumes using the access control record.
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
    initiator_name:
      description:
        - The iSCSI initiator name (IQN).
      returned: always
      type: str
      sample: null
    volume_count:
      description:
        - The number of volumes using the access control record.
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


class AzureRMAccessControlRecordInfo(AzureRMModuleBase):
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
            access_control_record_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.manager_name = None
        self.access_control_record_name = None

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
        super(AzureRMAccessControlRecordInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.access_control_record_name is not None and
            self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['access_control_records'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['access_control_records'] = self.format_item(self.listbymanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.access_control_records.get(access_control_record_name=self.access_control_record_name,
                                                                   resource_group_name=self.resource_group_name,
                                                                   manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbymanager(self):
        response = None

        try:
            response = self.mgmt_client.access_control_records.list_by_manager(resource_group_name=self.resource_group_name,
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
    AzureRMAccessControlRecordInfo()


if __name__ == '__main__':
    main()
