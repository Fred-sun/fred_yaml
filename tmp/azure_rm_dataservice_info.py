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
module: azure_rm_dataservice_info
version_added: '2.9'
short_description: Get DataService info.
description:
  - Get info of DataService.
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
  data_service_name:
    description:
      - The name of the data service that is being queried.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DataServices_ListByDataManagerGET51
      azure_rm_dataservice_info: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataServices_GetGET62
      azure_rm_dataservice_info: 
        data_manager_name: TestAzureSDKOperations
        data_service_name: DataTransformation
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
data_services:
  description: >-
    A list of dict results where the key is the name of the DataService and the
    values are the facts for that DataService.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of data services.
      returned: always
      type: list
      sample: null
      contains:
        state:
          description:
            - State of the data service.
          returned: always
          type: sealed-choice
          sample: null
        supported_data_sink_types:
          description:
            - Supported data store types which can be used as a sink.
          returned: always
          type: list
          sample: null
        supported_data_source_types:
          description:
            - Supported data store types which can be used as a source.
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - Link for the next set of data services.
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
    state:
      description:
        - State of the data service.
      returned: always
      type: sealed-choice
      sample: null
    supported_data_sink_types:
      description:
        - Supported data store types which can be used as a sink.
      returned: always
      type: list
      sample: null
    supported_data_source_types:
      description:
        - Supported data store types which can be used as a source.
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


class AzureRMDataServiceInfo(AzureRMModuleBase):
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
            data_service_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.data_manager_name = None
        self.data_service_name = None

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
        super(AzureRMDataServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.data_service_name is not None and
            self.resource_group_name is not None and
            self.data_manager_name is not None):
            self.results['data_services'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.data_manager_name is not None):
            self.results['data_services'] = self.format_item(self.listbydatamanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_services.get(data_service_name=self.data_service_name,
                                                          resource_group_name=self.resource_group_name,
                                                          data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatamanager(self):
        response = None

        try:
            response = self.mgmt_client.data_services.list_by_data_manager(resource_group_name=self.resource_group_name,
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
    AzureRMDataServiceInfo()


if __name__ == '__main__':
    main()
