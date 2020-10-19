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
module: azure_rm_datamanager_info
version_added: '2.9'
short_description: Get DataManager info.
description:
  - Get info of DataManager.
options:
  resource_group_name:
    description:
      - The Resource Group Name
    type: str
  data_manager_name:
    description:
      - >-
        The name of the DataManager Resource within the specified resource
        group. DataManager names must be between 3 and 24 characters in length
        and use any alphanumeric and underscore only
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DataManagers_ListGET21
      azure_rm_datamanager_info: 
        {}
        

    - name: DataManagers_ListByResourceGroupGET31
      azure_rm_datamanager_info: 
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataManagers_GetGET41
      azure_rm_datamanager_info: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
data_managers:
  description: >-
    A list of dict results where the key is the name of the DataManager and the
    values are the facts for that DataManager.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of data manager resources.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - Etag of the Resource.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link for the next set of data stores.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The Resource Id.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The Resource Name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - "The location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East\r\nUS, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo\r\nregion is specified on update the request will succeed."
      returned: always
      type: str
      sample: null
    tags:
      description:
        - "The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource\r\n(across resource groups)."
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - The sku type.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              The sku name. Required for data manager creation, optional for
              update.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The sku tier. This is based on the SKU name.
          returned: always
          type: str
          sample: null
    etag:
      description:
        - Etag of the Resource.
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
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataManagerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            data_manager_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.data_manager_name = None

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
        super(AzureRMDataManagerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.data_manager_name is not None):
            self.results['data_managers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['data_managers'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['data_managers'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_managers.get(resource_group_name=self.resource_group_name,
                                                          data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.data_managers.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.data_managers.list()
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
    AzureRMDataManagerInfo()


if __name__ == '__main__':
    main()
