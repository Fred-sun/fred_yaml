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
module: azure_rm_providerinstance
version_added: '2.9'
short_description: Manage Azure ProviderInstance instance.
description:
  - 'Create, update and delete instance of Azure ProviderInstance.'
options:
  resource_group_name:
    description:
      - Name of the resource group.
    required: true
    type: str
  sap_monitor_name:
    description:
      - Name of the SAP monitor resource.
    required: true
    type: str
  provider_instance_name:
    description:
      - Name of the provider instance.
    required: true
    type: str
  type:
    description:
      - The type of provider instance.
    type: str
  properties:
    description:
      - A JSON string containing the properties of the provider instance.
    type: str
  metadata:
    description:
      - A JSON string containing metadata of the provider instance.
    type: str
  state:
    description:
      - Assert the state of the ProviderInstance.
      - >-
        Use C(present) to create or update an ProviderInstance and C(absent) to
        delete it.
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
    - name: Create a SAP Monitor
      azure_rm_providerinstance: 
        provider_instance_name: myProviderInstance
        resource_group_name: myResourceGroup
        sap_monitor_name: mySapMonitor
        

    - name: Deletes a SAP monitor
      azure_rm_providerinstance: 
        provider_instance_name: myProviderInstance
        resource_group_name: myResourceGroup
        sap_monitor_name: mySapMonitor
        

'''

RETURN = '''
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
type_properties_type:
  description:
    - The type of provider instance.
  returned: always
  type: str
  sample: null
properties:
  description:
    - A JSON string containing the properties of the provider instance.
  returned: always
  type: str
  sample: null
metadata:
  description:
    - A JSON string containing metadata of the provider instance.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - State of provisioning of the provider instance
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
    from azure.mgmt.hana import HanaManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMProviderInstance(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sap_monitor_name=dict(
                type='str',
                required=True
            ),
            provider_instance_name=dict(
                type='str',
                required=True
            ),
            type=dict(
                type='str',
                disposition='/type'
            ),
            properties=dict(
                type='str',
                disposition='/properties'
            ),
            metadata=dict(
                type='str',
                disposition='/metadata'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.sap_monitor_name = None
        self.provider_instance_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMProviderInstance, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HanaManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-07-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.provider_instances.create(resource_group_name=self.resource_group_name,
                                                                      sap_monitor_name=self.sap_monitor_name,
                                                                      provider_instance_name=self.provider_instance_name,
                                                                      provider_instance_parameter=self.body)
            else:
                response = self.mgmt_client.provider_instances.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ProviderInstance instance.')
            self.fail('Error creating the ProviderInstance instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.provider_instances.delete(resource_group_name=self.resource_group_name,
                                                                  sap_monitor_name=self.sap_monitor_name,
                                                                  provider_instance_name=self.provider_instance_name)
        except CloudError as e:
            self.log('Error attempting to delete the ProviderInstance instance.')
            self.fail('Error deleting the ProviderInstance instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.provider_instances.get(resource_group_name=self.resource_group_name,
                                                               sap_monitor_name=self.sap_monitor_name,
                                                               provider_instance_name=self.provider_instance_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMProviderInstance()


if __name__ == '__main__':
    main()
