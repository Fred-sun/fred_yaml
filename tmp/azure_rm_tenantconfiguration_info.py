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
module: azure_rm_tenantconfiguration_info
version_added: '2.9'
short_description: Get TenantConfiguration info.
description:
  - Get info of TenantConfiguration.
options:
  configuration_name:
    description:
      - The configuration name. Value must be 'default'
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get list of Tenant configurations
      azure_rm_tenantconfiguration_info: 
        {}
        

    - name: Get Tenant configuration
      azure_rm_tenantconfiguration_info: 
        configuration_name: default
        

'''

RETURN = '''
tenant_configurations:
  description: >-
    A list of dict results where the key is the name of the TenantConfiguration
    and the values are the facts for that TenantConfiguration.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The array of custom resource provider manifests.
      returned: always
      type: list
      sample: null
      contains:
        enforce_private_markdown_storage:
          description:
            - >-
              When flag is set to true Markdown tile will require external
              storage configuration (URI). The inline content configuration will
              be prohibited.
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    enforce_private_markdown_storage:
      description:
        - >-
          When flag is set to true Markdown tile will require external storage
          configuration (URI). The inline content configuration will be
          prohibited.
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
    from azure.mgmt.portal import portal
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTenantConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            configuration_name=dict(
                type='str',
                choices=['default']
            )
        )

        self.configuration_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTenantConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(portal,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

        if (self.configuration_name is not None):
            self.results['tenant_configurations'] = self.format_item(self.get())
        else:
            self.results['tenant_configurations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.tenant_configurations.get(configuration_name=self.configuration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.tenant_configurations.list()
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
    AzureRMTenantConfigurationInfo()


if __name__ == '__main__':
    main()
