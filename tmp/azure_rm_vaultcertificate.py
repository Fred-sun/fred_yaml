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
module: azure_rm_vaultcertificate
version_added: '2.9'
short_description: Manage Azure VaultCertificate instance.
description:
  - 'Create, update and delete instance of Azure VaultCertificate.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
    type: str
  vault_name:
    description:
      - The name of the recovery services vault.
    required: true
    type: str
  certificate_name:
    description:
      - Certificate friendly name.
    required: true
    type: str
  properties:
    description:
      - Raw certificate data.
    required: true
    type: dict
    suboptions:
      auth_type:
        description:
          - Specifies the authentication type.
        type: str
        choices:
          - Invalid
          - ACS
          - AAD
          - AccessControlService
          - AzureActiveDirectory
      certificate:
        description:
          - The base64 encoded certificate raw data string
        type: byte-array
  state:
    description:
      - Assert the state of the VaultCertificate.
      - >-
        Use C(present) to create or update an VaultCertificate and C(absent) to
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
    - name: Download vault credential file
      azure_rm_vaultcertificate: 
        certificate_name: BCDRIbzVault77777777-d41f-4550-9f70-7708a3a2283b-12-18-2017-vaultcredentials
        resource_group_name: BCDRIbzRG
        vault_name: BCDRIbzVault
        

'''

RETURN = '''
name:
  description:
    - Resource name associated with the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      Resource type represents the complete path of the form
      Namespace/ResourceType/ResourceType/...
  returned: always
  type: str
  sample: null
id:
  description:
    - Resource Id represents the complete path to the resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Certificate details representing the Vault credentials.
  returned: always
  type: dict
  sample: null
  contains:
    auth_type:
      description:
        - >-
          This property will be used as the discriminator for deciding the
          specific types in the polymorphic chain of types.
      returned: always
      type: str
      sample: null
    certificate:
      description:
        - The base64 encoded certificate raw data string.
      returned: always
      type: byte-array
      sample: null
    friendly_name:
      description:
        - Certificate friendly name.
      returned: always
      type: str
      sample: null
    issuer:
      description:
        - Certificate issuer.
      returned: always
      type: str
      sample: null
    resource_id:
      description:
        - Resource ID of the vault.
      returned: always
      type: integer
      sample: null
    subject:
      description:
        - Certificate Subject Name.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - Certificate thumbprint.
      returned: always
      type: str
      sample: null
    valid_from:
      description:
        - Certificate Validity start Date time.
      returned: always
      type: str
      sample: null
    valid_to:
      description:
        - Certificate Validity End Date time.
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
    from azure.mgmt.recovery import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVaultCertificate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vault_name=dict(
                type='str',
                required=True
            ),
            certificate_name=dict(
                type='str',
                required=True
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                required=True,
                options=dict(
                    auth_type=dict(
                        type='str',
                        disposition='auth_type',
                        choices=['Invalid',
                                 'ACS',
                                 'AAD',
                                 'AccessControlService',
                                 'AzureActiveDirectory']
                    ),
                    certificate=dict(
                        type='byte-array',
                        disposition='certificate'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vault_name = None
        self.certificate_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVaultCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-06-01')

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
                response = self.mgmt_client.vault_certificates.create(resource_group_name=self.resource_group_name,
                                                                      vault_name=self.vault_name,
                                                                      certificate_name=self.certificate_name,
                                                                      certificate_request=self.body)
            else:
                response = self.mgmt_client.vault_certificates.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VaultCertificate instance.')
            self.fail('Error creating the VaultCertificate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vault_certificates.delete()
        except CloudError as e:
            self.log('Error attempting to delete the VaultCertificate instance.')
            self.fail('Error deleting the VaultCertificate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vault_certificates.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVaultCertificate()


if __name__ == '__main__':
    main()
