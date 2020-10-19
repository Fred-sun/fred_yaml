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
module: azure_rm_datastoretype_info
version_added: '2.9'
short_description: Get DataStoreType info.
description:
  - Get info of DataStoreType.
options:
  resource_group_name:
    description:
      - The Resource Group Name
    required: true
    type: str
  data_manager_name:
    description:
      - >-
        The name of the DataManager Resource within the specified resource
        group. DataManager names must be between 3 and 24 characters in length
        and use any alphanumeric and underscore only
    required: true
    type: str
  data_store_type_name:
    description:
      - The data store/repository type name for which details are needed.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DataStoreTypes_ListByDataManagerGET171
      azure_rm_datastoretype_info: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataStoreTypes_GetGET182
      azure_rm_datastoretype_info: 
        data_manager_name: TestAzureSDKOperations
        data_store_type_name: StorSimple8000Series
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataStoreTypes_GetGET183
      azure_rm_datastoretype_info: 
        data_manager_name: TestAzureSDKOperations
        data_store_type_name: AzureStorageAccount
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
data_store_types:
  description: >-
    A list of dict results where the key is the name of the DataStoreType and
    the values are the facts for that DataStoreType.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of DataStoreType.
      returned: always
      type: list
      sample: null
      contains:
        repository_type:
          description:
            - >-
              Arm type for the manager resource to which the data source type is
              associated. This is optional.
          returned: always
          type: str
          sample: null
        state:
          description:
            - State of the data store type.
          returned: always
          type: sealed-choice
          sample: null
        supported_data_services_as_sink:
          description:
            - Supported data services where it can be used as a sink.
          returned: always
          type: list
          sample: null
        supported_data_services_as_source:
          description:
            - Supported data services where it can be used as a source.
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - Link for the next set of data store types.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the object.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Id of the object.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the object.
      returned: always
      type: str
      sample: null
    repository_type:
      description:
        - >-
          Arm type for the manager resource to which the data source type is
          associated. This is optional.
      returned: always
      type: str
      sample: null
    state:
      description:
        - State of the data store type.
      returned: always
      type: sealed-choice
      sample: null
    supported_data_services_as_sink:
      description:
        - Supported data services where it can be used as a sink.
      returned: always
      type: list
      sample: null
    supported_data_services_as_source:
      description:
        - Supported data services where it can be used as a source.
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
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataStoreTypeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            data_store_type_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.data_manager_name = None
        self.data_store_type_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDataStoreTypeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.data_store_type_name is not None and
            self.resource_group_name is not None and
            self.data_manager_name is not None):
            self.results['data_store_types'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.data_manager_name is not None):
            self.results['data_store_types'] = self.format_item(self.listbydatamanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_store_types.get(data_store_type_name=self.data_store_type_name,
                                                             resource_group_name=self.resource_group_name,
                                                             data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatamanager(self):
        response = None

        try:
            response = self.mgmt_client.data_store_types.list_by_data_manager(resource_group_name=self.resource_group_name,
                                                                              data_manager_name=self.data_manager_name)
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
    AzureRMDataStoreTypeInfo()


if __name__ == '__main__':
    main()
