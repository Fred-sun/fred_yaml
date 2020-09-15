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
module: azure_rm_certificate
version_added: '2.9'
short_description: Manage Azure Certificate instance.
description:
  - 'Create, update and delete instance of Azure Certificate.'
options:
  resource_group_name:
    description:
      - The name of the resource group that contains the IoT hub.
    required: true
    type: str
  resource_name:
    description:
      - The name of the IoT hub.
    required: true
    type: str
  certificate_name:
    description:
      - The name of the certificate
    required: true
    type: str
  if_match:
    description:
      - >-
        ETag of the Certificate. Do not specify for creating a brand new
        certificate. Required to update an existing certificate.
    type: str
  certificate:
    description:
      - The certificate content
    type: str
  state:
    description:
      - Assert the state of the Certificate.
      - >-
        Use C(present) to create or update an Certificate and C(absent) to
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
    - name: Certificates_CreateOrUpdate
      azure_rm_certificate: 
        certificate_name: cert
        resource_group_name: myResourceGroup
        resource_name: iothub
        

    - name: Certificates_Delete
      azure_rm_certificate: 
        certificate_name: cert
        resource_group_name: myResourceGroup
        resource_name: myhub
        

'''

RETURN = '''
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
    - The certificate's create date and time.
  returned: always
  type: str
  sample: null
updated:
  description:
    - The certificate's last update date and time.
  returned: always
  type: str
  sample: null
certificate:
  description:
    - The certificate content
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
    from azure.mgmt.iot import iotHubClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCertificate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            certificate_name=dict(
                type='str',
                required=True
            ),
            if_match=dict(
                type='str'
            ),
            certificate=dict(
                type='str',
                disposition='/certificate'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.certificate_name = None
        self.if_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(iotHubClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

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
            response = self.mgmt_client.certificates.create_or_update(resource_group_name=self.resource_group_name,
                                                                      resource_name=self.resource_name,
                                                                      certificate_name=self.certificate_name,
                                                                      if_match=self.if_match,
                                                                      certificate_description=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Certificate instance.')
            self.fail('Error creating the Certificate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.certificates.delete(resource_group_name=self.resource_group_name,
                                                            resource_name=self.resource_name,
                                                            certificate_name=self.certificate_name,
                                                            if_match=self.if_match)
        except CloudError as e:
            self.log('Error attempting to delete the Certificate instance.')
            self.fail('Error deleting the Certificate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.certificates.get(resource_group_name=self.resource_group_name,
                                                         resource_name=self.resource_name,
                                                         certificate_name=self.certificate_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCertificate()


if __name__ == '__main__':
    main()
