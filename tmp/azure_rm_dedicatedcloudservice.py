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
module: azure_rm_dedicatedcloudservice
version_added: '2.9'
short_description: Manage Azure DedicatedCloudService instance.
description:
  - 'Create, update and delete instance of Azure DedicatedCloudService.'
options:
  resource_group_name:
    description:
      - The name of the resource group
    required: true
    type: str
  dedicated_cloud_service_name:
    description:
      - dedicated cloud Service name
      - dedicated cloud service name
    required: true
    type: str
  location:
    description:
      - Azure region
    type: str
  gateway_subnet:
    description:
      - >-
        gateway Subnet for the account. It will collect the subnet address and
        always treat it as /28
    type: str
  state:
    description:
      - Assert the state of the DedicatedCloudService.
      - >-
        Use C(present) to create or update an DedicatedCloudService and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CreateDedicatedCloudService
      azure_rm_dedicatedcloudservice: 
        dedicated_cloud_service_name: myService
        resource_group_name: myResourceGroup
        

    - name: DeleteDedicatedCloudService
      azure_rm_dedicatedcloudservice: 
        dedicated_cloud_service_name: myService
        resource_group_name: myResourceGroup
        

    - name: PatchDedicatedService
      azure_rm_dedicatedcloudservice: 
        dedicated_cloud_service_name: myService
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
id:
  description:
    - >-
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
  returned: always
  type: str
  sample: null
location:
  description:
    - Azure region
  returned: always
  type: str
  sample: null
name:
  description:
    - '{dedicatedCloudServiceName}'
  returned: always
  type: str
  sample: null
tags:
  description:
    - The list of tags
  returned: always
  type: dictionary
  sample: null
type:
  description:
    - '{resourceProviderNamespace}/{resourceType}'
  returned: always
  type: str
  sample: null
gateway_subnet:
  description:
    - >-
      gateway Subnet for the account. It will collect the subnet address and
      always treat it as /28
  returned: always
  type: str
  sample: null
is_account_onboarded:
  description:
    - indicates whether account onboarded or not in a given region
  returned: always
  type: sealed-choice
  sample: null
nodes:
  description:
    - total nodes purchased
  returned: always
  type: integer
  sample: null
service_url:
  description:
    - link to a service management web portal
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmware import VMwareCloudSimple
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedCloudService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            dedicated_cloud_service_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            gateway_subnet=dict(
                type='str',
                disposition='/gateway_subnet'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.dedicated_cloud_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedCloudService, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                           supports_check_mode=True,
                                                           supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.dedicated_cloud_services.create_or_update(resource_group_name=self.resource_group_name,
                                                                                  dedicated_cloud_service_name=self.dedicated_cloud_service_name,
                                                                                  dedicated_cloud_service_request=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedCloudService instance.')
            self.fail('Error creating the DedicatedCloudService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_cloud_services.delete(resource_group_name=self.resource_group_name,
                                                                        dedicated_cloud_service_name=self.dedicated_cloud_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedCloudService instance.')
            self.fail('Error deleting the DedicatedCloudService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dedicated_cloud_services.get(resource_group_name=self.resource_group_name,
                                                                     dedicated_cloud_service_name=self.dedicated_cloud_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedCloudService()


if __name__ == '__main__':
    main()
