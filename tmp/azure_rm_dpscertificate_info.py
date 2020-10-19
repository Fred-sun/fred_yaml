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
module: azure_rm_dpscertificate_info
version_added: '2.9'
short_description: Get DpsCertificate info.
description:
  - Get info of DpsCertificate.
options:
  certificate_name:
    description:
      - Name of the certificate to retrieve.
    type: str
  resource_group_name:
    description:
      - Resource group identifier.
      - Name of resource group.
    required: true
    type: str
  provisioning_service_name:
    description:
      - Name of the provisioning service the certificate is associated with.
      - Name of provisioning service to retrieve certificates for.
    required: true
    type: str
  if_match:
    description:
      - ETag of the certificate.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DPSGetCertificate
      azure_rm_dpscertificate_info: 
        certificate_name: cert
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: DPSGetCertificates
      azure_rm_dpscertificate_info: 
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
dps_certificate:
  description: >-
    A list of dict results where the key is the name of the DpsCertificate and
    the values are the facts for that DpsCertificate.
  returned: always
  type: complex
  contains:
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
    value:
      description:
        - The array of Certificate objects.
      returned: always
      type: list
      sample: null
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.iot import iotDpsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDpsCertificateInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            certificate_name=dict(
                type='str'
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
                type='str'
            )
        )

        self.certificate_name = None
        self.resource_group_name = None
        self.provisioning_service_name = None
        self.if_match = None

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
        super(AzureRMDpsCertificateInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(iotDpsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

        if (self.certificate_name is not None and
            self.resource_group_name is not None and
            self.provisioning_service_name is not None):
            self.results['dps_certificate'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.provisioning_service_name is not None):
            self.results['dps_certificate'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dps_certificate.get(certificate_name=self.certificate_name,
                                                            resource_group_name=self.resource_group_name,
                                                            provisioning_service_name=self.provisioning_service_name,
                                                            if_match=self.if_match)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.dps_certificate.list(resource_group_name=self.resource_group_name,
                                                             provisioning_service_name=self.provisioning_service_name)
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
    AzureRMDpsCertificateInfo()


if __name__ == '__main__':
    main()
