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
module: azure_rm_managementconfiguration_info
version_added: '2.9'
short_description: Get ManagementConfiguration info.
description:
  - Get info of ManagementConfiguration.
options:
  resource_group_name:
    description:
      - The name of the resource group to get. The name is case insensitive.
    type: str
  management_configuration_name:
    description:
      - User Management Configuration Name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SolutionList
      azure_rm_managementconfiguration_info: 
        {}
        

    - name: SolutionGet
      azure_rm_managementconfiguration_info: 
        management_configuration_name: managementConfigurationName
        resource_group_name: rg1
        

'''

RETURN = '''
management_configurations:
  description: >-
    A list of dict results where the key is the name of the
    ManagementConfiguration and the values are the facts for that
    ManagementConfiguration.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Management Configuration properties within the subscription.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        application_id:
          description:
            - The applicationId of the appliance for this Management.
          returned: always
          type: str
          sample: null
        parent_resource_type:
          description:
            - The type of the parent resource.
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - Parameters to run the ARM template
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - name of the parameter.
              returned: always
              type: str
              sample: null
            value:
              description:
                - 'value for the parameter. In Jtoken '
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - The provisioning state for the ManagementConfiguration.
          returned: always
          type: str
          sample: null
        template:
          description:
            - The Json object containing the ARM template to deploy
          returned: always
          type: any
          sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    application_id:
      description:
        - The applicationId of the appliance for this Management.
      returned: always
      type: str
      sample: null
    parent_resource_type:
      description:
        - The type of the parent resource.
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - Parameters to run the ARM template
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - name of the parameter.
          returned: always
          type: str
          sample: null
        value:
          description:
            - 'value for the parameter. In Jtoken '
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state for the ManagementConfiguration.
      returned: always
      type: str
      sample: null
    template:
      description:
        - The Json object containing the ARM template to deploy
      returned: always
      type: any
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.operations import OperationsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagementConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            management_configuration_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.management_configuration_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-11-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagementConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(OperationsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-11-01-preview')

        if (self.resource_group_name is not None and
            self.management_configuration_name is not None):
            self.results['management_configurations'] = self.format_item(self.get())
        else:
            self.results['management_configurations'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.management_configurations.get(resource_group_name=self.resource_group_name,
                                                                      management_configuration_name=self.management_configuration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.management_configurations.list_by_subscription()
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
    AzureRMManagementConfigurationInfo()


if __name__ == '__main__':
    main()
