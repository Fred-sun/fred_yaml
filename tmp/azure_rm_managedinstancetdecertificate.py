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
module: azure_rm_managedinstancetdecertificate
version_added: '2.9'
short_description: Manage Azure ManagedInstanceTdeCertificate instance.
description:
  - 'Create, update and delete instance of Azure ManagedInstanceTdeCertificate.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  private_blob:
    description:
      - The base64 encoded certificate private blob.
    required: true
    type: str
  cert_password:
    description:
      - The certificate password.
    required: true
    type: str
  state:
    description:
      - Assert the state of the ManagedInstanceTdeCertificate.
      - >-
        Use C(present) to create or update an ManagedInstanceTdeCertificate and
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
    - name: Upload a TDE certificate
      azure_rm_managedinstancetdecertificate: 
        managed_instance_name: testtdecert
        resource_group_name: testtdecert
        properties:
          cert_password: password
          private_blob: >-
            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
        

'''

RETURN = '''
{}

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagedInstanceTdeCertificate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            private_blob=dict(
                type='str',
                disposition='/private_blob',
                required=True
            ),
            cert_password=dict(
                type='str',
                disposition='/cert_password',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagedInstanceTdeCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01-preview')

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
                response = self.mgmt_client.managed_instance_tde_certificates.create(resource_group_name=self.resource_group_name,
                                                                                     managed_instance_name=self.managed_instance_name,
                                                                                     parameters=self.body)
            else:
                response = self.mgmt_client.managed_instance_tde_certificates.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagedInstanceTdeCertificate instance.')
            self.fail('Error creating the ManagedInstanceTdeCertificate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.managed_instance_tde_certificates.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ManagedInstanceTdeCertificate instance.')
            self.fail('Error deleting the ManagedInstanceTdeCertificate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.managed_instance_tde_certificates.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagedInstanceTdeCertificate()


if __name__ == '__main__':
    main()
