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
module: azure_rm_dpscertificate
version_added: '2.9'
short_description: Manage Azure DpsCertificate instance.
description:
  - 'Create, update and delete instance of Azure DpsCertificate.'
options:
  certificate_name:
    description:
      - Name of the certificate to retrieve.
      - The name of the certificate create or update.
      - >-
        This is a mandatory field, and is the logical name of the certificate
        that the provisioning service will access by.
    required: true
    type: str
  resource_group_name:
    description:
      - Resource group identifier.
    required: true
    type: str
  provisioning_service_name:
    description:
      - Name of the provisioning service the certificate is associated with.
      - The name of the provisioning service.
    required: true
    type: str
  if_match:
    description:
      - ETag of the certificate.
      - >-
        ETag of the certificate. This is required to update an existing
        certificate, and ignored while creating a brand new certificate.
    required: true
    type: str
  certificate:
    description:
      - >-
        Base-64 representation of the X509 leaf certificate .cer file or just
        .pem file content.
    type: str
  certificate_name1:
    description:
      - 'This is optional, and it is the Common Name of the certificate.'
    type: str
  certificate_raw_bytes:
    description:
      - Raw data within the certificate.
    type: byte-array
  certificate_is_verified:
    description:
      - Indicates if certificate has been verified by owner of the private key.
    type: bool
  certificate_purpose:
    description:
      - A description that mentions the purpose of the certificate.
    type: str
    choices:
      - clientAuthentication
      - serverAuthentication
  certificate_created:
    description:
      - Time the certificate is created.
    type: str
  certificate_last_updated:
    description:
      - Time the certificate is last updated.
    type: str
  certificate_has_private_key:
    description:
      - Indicates if the certificate contains a private key.
    type: bool
  certificate_nonce:
    description:
      - Random number generated to indicate Proof of Possession.
    type: str
  state:
    description:
      - Assert the state of the DpsCertificate.
      - >-
        Use C(present) to create or update an DpsCertificate and C(absent) to
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
    - name: DPSCreateOrUpdateCertificate
      azure_rm_dpscertificate: 
        certificate_name: cert
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: DPSDeleteCertificate
      azure_rm_dpscertificate: 
        certificate_name: cert
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
properties:
  description:
    - properties of a certificate
  returned: always
  type: dict
  sample: null
  contains:
    subject:
      description:
        - The certificate's subject name.
      returned: always
      type: str
      sample: null
    expiry:
      description:
        - The certificate's expiration date and time.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - The certificate's thumbprint.
      returned: always
      type: str
      sample: null
    is_verified:
      description:
        - Determines whether certificate has been verified.
      returned: always
      type: bool
      sample: null
    created:
      description:
        - The certificate's creation date and time.
      returned: always
      type: str
      sample: null
    updated:
      description:
        - The certificate's last update date and time.
      returned: always
      type: str
      sample: null
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the certificate.
  returned: always
  type: str
  sample: null
etag:
  description:
    - The entity tag.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
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
    from azure.mgmt.iot import iotDpsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDpsCertificate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            certificate_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            provisioning_service_name=dict(
                type='str',
                required=True
            ),
            if_match=dict(
                type='str',
                required=True
            ),
            certificate=dict(
                type='str',
                disposition='/certificate'
            ),
            certificate_name1=dict(
                type='str'
            ),
            certificate_raw_bytes=dict(
                type='byte-array'
            ),
            certificate_is_verified=dict(
                type='bool'
            ),
            certificate_purpose=dict(
                type='str',
                choices=['clientAuthentication',
                         'serverAuthentication']
            ),
            certificate_created=dict(
                type='str'
            ),
            certificate_last_updated=dict(
                type='str'
            ),
            certificate_has_private_key=dict(
                type='bool'
            ),
            certificate_nonce=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.certificate_name = None
        self.resource_group_name = None
        self.provisioning_service_name = None
        self.if_match = None
        self.certificate_name1 = None
        self.certificate_raw_bytes = None
        self.certificate_is_verified = None
        self.certificate_purpose = None
        self.certificate_created = None
        self.certificate_last_updated = None
        self.certificate_has_private_key = None
        self.certificate_nonce = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDpsCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(iotDpsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

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
            response = self.mgmt_client.dps_certificate.create_or_update(resource_group_name=self.resource_group_name,
                                                                         provisioning_service_name=self.provisioning_service_name,
                                                                         certificate_name=self.certificate_name,
                                                                         if_match=self.if_match,
                                                                         certificate_description=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DpsCertificate instance.')
            self.fail('Error creating the DpsCertificate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dps_certificate.delete(resource_group_name=self.resource_group_name,
                                                               if_match=self.if_match,
                                                               provisioning_service_name=self.provisioning_service_name,
                                                               certificate_name=self.certificate_name,
                                                               certificate_name1=self.certificate_name1,
                                                               certificate_raw_bytes=self.certificate_raw_bytes,
                                                               certificate_is_verified=self.certificate_is_verified,
                                                               certificate_purpose=self.certificate_purpose,
                                                               certificate_created=self.certificate_created,
                                                               certificate_last_updated=self.certificate_last_updated,
                                                               certificate_has_private_key=self.certificate_has_private_key,
                                                               certificate_nonce=self.certificate_nonce)
        except CloudError as e:
            self.log('Error attempting to delete the DpsCertificate instance.')
            self.fail('Error deleting the DpsCertificate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dps_certificate.get(certificate_name=self.certificate_name,
                                                            resource_group_name=self.resource_group_name,
                                                            provisioning_service_name=self.provisioning_service_name,
                                                            if_match=self.if_match)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDpsCertificate()


if __name__ == '__main__':
    main()
