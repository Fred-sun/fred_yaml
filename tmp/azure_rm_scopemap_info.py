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
module: azure_rm_scopemap_info
version_added: '2.9'
short_description: Get ScopeMap info.
description:
  - Get info of ScopeMap.
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  registry_name:
    description:
      - The name of the container registry.
    required: true
    type: str
  scope_map_name:
    description:
      - The name of the scope map.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ScopeMapGet
      azure_rm_scopemap_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        scope_map_name: myScopeMap
        

    - name: ScopeMapList
      azure_rm_scopemap_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
scope_maps:
  description: >-
    A list of dict results where the key is the name of the ScopeMap and the
    values are the facts for that ScopeMap.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The user friendly description of the scope map.
      returned: always
      type: str
      sample: null
    type_properties_type:
      description:
        - The type of the scope map. E.g. BuildIn scope map.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of scope map.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the resource.
      returned: always
      type: str
      sample: null
    actions:
      description:
        - "The list of scoped permissions for registry artifacts.\r\nE.g. repositories/repository-name/content/read,\r\nrepositories/repository-name/metadata/write"
      returned: always
      type: list
      sample: null
    value:
      description:
        - >-
          The list of scope maps. Since this list may be incomplete, the
          nextLink field should be used to request the next list of scope maps.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The user friendly description of the scope map.
          returned: always
          type: str
          sample: null
        type_properties_type:
          description:
            - The type of the scope map. E.g. BuildIn scope map.
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of scope map.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state of the resource.
          returned: always
          type: str
          sample: null
        actions:
          description:
            - "The list of scoped permissions for registry artifacts.\r\nE.g. repositories/repository-name/content/read,\r\nrepositories/repository-name/metadata/write"
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - The URI that can be used to request the next list of scope maps.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMScopeMapInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            scope_map_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.scope_map_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMScopeMapInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-05-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.scope_map_name is not None):
            self.results['scope_maps'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['scope_maps'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.scope_maps.get(resource_group_name=self.resource_group_name,
                                                       registry_name=self.registry_name,
                                                       scope_map_name=self.scope_map_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.scope_maps.list(resource_group_name=self.resource_group_name,
                                                        registry_name=self.registry_name)
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
    AzureRMScopeMapInfo()


if __name__ == '__main__':
    main()
