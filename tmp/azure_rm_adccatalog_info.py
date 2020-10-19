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
module: azure_rm_adccatalog_info
version_added: '2.9'
short_description: Get ADCCatalog info.
description:
  - Get info of ADCCatalog.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  catalogname:
    description:
      - >-
        The name of the data catalog in the specified subscription and resource
        group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Azure Data Catalog Service
      azure_rm_adccatalog_info: 
        resource_group_name: exampleResourceGroup
        

    - name: Get Azure Data Catalog Service
      azure_rm_adccatalog_info: 
        resource_group_name: exampleResourceGroup
        

'''

RETURN = '''
adccatalogs:
  description: >-
    A list of dict results where the key is the name of the ADCCatalog and the
    values are the facts for that ADCCatalog.
  returned: always
  type: complex
  contains:
    value:
      description:
        - the list of Azure Data Catalogs.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - Azure data catalog SKU.
          returned: always
          type: str
          sample: null
        units:
          description:
            - Azure data catalog units.
          returned: always
          type: integer
          sample: null
        admins:
          description:
            - Azure data catalog admin list.
          returned: always
          type: list
          sample: null
          contains:
            upn:
              description:
                - UPN of the user.
              returned: always
              type: str
              sample: null
            object_id:
              description:
                - Object Id for the user
              returned: always
              type: str
              sample: null
        users:
          description:
            - Azure data catalog user list.
          returned: always
          type: list
          sample: null
          contains:
            upn:
              description:
                - UPN of the user.
              returned: always
              type: str
              sample: null
            object_id:
              description:
                - Object Id for the user
              returned: always
              type: str
              sample: null
        successfully_provisioned:
          description:
            - Azure data catalog provision status.
          returned: always
          type: bool
          sample: null
        enable_automatic_unit_adjustment:
          description:
            - Automatic unit adjustment enabled or not.
          returned: always
          type: bool
          sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - Resource etag
      returned: always
      type: str
      sample: null
    sku:
      description:
        - Azure data catalog SKU.
      returned: always
      type: str
      sample: null
    units:
      description:
        - Azure data catalog units.
      returned: always
      type: integer
      sample: null
    admins:
      description:
        - Azure data catalog admin list.
      returned: always
      type: list
      sample: null
      contains:
        upn:
          description:
            - UPN of the user.
          returned: always
          type: str
          sample: null
        object_id:
          description:
            - Object Id for the user
          returned: always
          type: str
          sample: null
    users:
      description:
        - Azure data catalog user list.
      returned: always
      type: list
      sample: null
      contains:
        upn:
          description:
            - UPN of the user.
          returned: always
          type: str
          sample: null
        object_id:
          description:
            - Object Id for the user
          returned: always
          type: str
          sample: null
    successfully_provisioned:
      description:
        - Azure data catalog provision status.
      returned: always
      type: bool
      sample: null
    enable_automatic_unit_adjustment:
      description:
        - Automatic unit adjustment enabled or not.
      returned: always
      type: bool
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataCatalogRestClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMADCCatalogInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            catalogname=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.catalogname = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-03-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMADCCatalogInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataCatalogRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-30')

        if (self.resource_group_name is not None and
            self.catalogname is not None):
            self.results['adccatalogs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['adccatalogs'] = self.format_item(self.listtbyresourcegroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.adccatalogs.get(resource_group_name=self.resource_group_name,
                                                        catalogname=self.catalogname)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listtbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.adccatalogs.listt_by_resource_group(resource_group_name=self.resource_group_name)
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
    AzureRMADCCatalogInfo()


if __name__ == '__main__':
    main()
