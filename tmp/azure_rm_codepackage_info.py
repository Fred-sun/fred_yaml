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
module: azure_rm_codepackage_info
version_added: '2.9'
short_description: Get CodePackage info.
description:
  - Get info of CodePackage.
options:
  resource_group_name:
    description:
      - Azure resource group name
    required: true
    type: str
  application_resource_name:
    description:
      - The identity of the application.
    required: true
    type: str
  service_resource_name:
    description:
      - The identity of the service.
    required: true
    type: str
  replica_name:
    description:
      - Service Fabric replica name.
    required: true
    type: str
  code_package_name:
    description:
      - The name of code package of the service.
    required: true
    type: str
  tail:
    description:
      - Number of lines to show from the end of the logs. Default is 100.
    required: true
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetContainerLogs
      azure_rm_codepackage_info: 
        application_resource_name: sbzDocApp
        code_package_name: sbzDocCode
        replica_name: '0'
        resource_group_name: sbz_demo
        service_resource_name: sbzDocService
        

'''

RETURN = '''
code_package:
  description: >-
    A list of dict results where the key is the name of the CodePackage and the
    values are the facts for that CodePackage.
  returned: always
  type: complex
  contains:
    content:
      description:
        - Container logs.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCodePackageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            application_resource_name=dict(
                type='str',
                required=True
            ),
            service_resource_name=dict(
                type='str',
                required=True
            ),
            replica_name=dict(
                type='str',
                required=True
            ),
            code_package_name=dict(
                type='str',
                required=True
            ),
            tail=dict(
                type='integer',
                required=True
            )
        )

        self.resource_group_name = None
        self.application_resource_name = None
        self.service_resource_name = None
        self.replica_name = None
        self.code_package_name = None
        self.tail = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCodePackageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.application_resource_name is not None and
            self.service_resource_name is not None and
            self.replica_name is not None and
            self.code_package_name is not None):
            self.results['code_package'] = self.format_item(self.getcontainerlog())
        return self.results

    def getcontainerlog(self):
        response = None

        try:
            response = self.mgmt_client.code_package.get_container_log(resource_group_name=self.resource_group_name,
                                                                       application_resource_name=self.application_resource_name,
                                                                       service_resource_name=self.service_resource_name,
                                                                       replica_name=self.replica_name,
                                                                       code_package_name=self.code_package_name,
                                                                       tail=self.tail)
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
    AzureRMCodePackageInfo()


if __name__ == '__main__':
    main()
