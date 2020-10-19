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
module: azure_rm_certificate_info
version_added: '2.9'
short_description: Get Certificate info.
description:
  - Get info of Certificate.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Certificates_ListByIotHub
      azure_rm_certificate_info: 
        resource_group_name: myResourceGroup
        resource_name: testhub
        

    - name: Certificates_Get
      azure_rm_certificate_info: 
        certificate_name: cert
        resource_group_name: myResourceGroup
        resource_name: testhub
        

'''

RETURN = '''
certificates:
  description: >-
    A list of dict results where the key is the name of the Certificate and the
    values are the facts for that Certificate.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The array of Certificate objects.
      returned: always
      type: list
      sample: null
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.iot import iotHubClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCertificateInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.certificate_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCertificateInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(iotHubClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

        if (self.resource_group_name is not None and
            self.resource_name is not None and
            self.certificate_name is not None):
            self.results['certificates'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['certificates'] = self.format_item(self.listbyiothub())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.certificates.get(resource_group_name=self.resource_group_name,
                                                         resource_name=self.resource_name,
                                                         certificate_name=self.certificate_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyiothub(self):
        response = None

        try:
            response = self.mgmt_client.certificates.list_by_iot_hub(resource_group_name=self.resource_group_name,
                                                                     resource_name=self.resource_name)
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
    AzureRMCertificateInfo()


if __name__ == '__main__':
    main()
