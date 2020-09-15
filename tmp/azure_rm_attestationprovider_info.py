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
module: azure_rm_attestationprovider_info
version_added: '2.9'
short_description: Get AttestationProvider info.
description:
  - Get info of AttestationProvider.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  provider_name:
    description:
      - Name of the attestation service instance
    type: str
  location:
    description:
      - The location of the default provider.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: AttestationProviders_Get
      azure_rm_attestationprovider_info: 
        provider_name: myattestationprovider
        resource_group_name: MyResourceGroup
        

    - name: AttestationProviders_List
      azure_rm_attestationprovider_info: 
        {}
        

    - name: AttestationProviders_ListByResourceGroup
      azure_rm_attestationprovider_info: 
        resource_group_name: testrg1
        

    - name: AttestationProviders_GetDefault
      azure_rm_attestationprovider_info: 
        {}
        

    - name: AttestationProviders_GetDefaultWithLocation
      azure_rm_attestationprovider_info: 
        location: Central US
        

'''

RETURN = '''
attestation_providers:
  description: >-
    A list of dict results where the key is the name of the AttestationProvider
    and the values are the facts for that AttestationProvider.
  returned: always
  type: complex
  contains:
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    trust_model:
      description:
        - Trust model for the attestation service instance.
      returned: always
      type: str
      sample: null
    status:
      description:
        - Status of attestation service.
      returned: always
      type: str
      sample: null
    attest_uri:
      description:
        - Gets the uri of attestation service
      returned: always
      type: str
      sample: null
    value:
      description:
        - Attestation Provider array.
      returned: always
      type: list
      sample: null
      contains:
        trust_model:
          description:
            - Trust model for the attestation service instance.
          returned: always
          type: str
          sample: null
        status:
          description:
            - Status of attestation service.
          returned: always
          type: str
          sample: null
        attest_uri:
          description:
            - Gets the uri of attestation service
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
    from azure.mgmt.attestation import AttestationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAttestationProviderInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            provider_name=dict(
                type='str'
            ),
            location=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.provider_name = None
        self.location = None

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
        super(AzureRMAttestationProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AttestationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.provider_name is not None):
            self.results['attestation_providers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['attestation_providers'] = self.format_item(self.listbyresourcegroup())
        elif (self.location is not None):
            self.results['attestation_providers'] = self.format_item(self.getdefaultbylocation())
        else:
            self.results['attestation_providers'] = self.format_item(self.list())
        else:
            self.results['attestation_providers'] = self.format_item(self.listdefault())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.attestation_providers.get(resource_group_name=self.resource_group_name,
                                                                  provider_name=self.provider_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.attestation_providers.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getdefaultbylocation(self):
        response = None

        try:
            response = self.mgmt_client.attestation_providers.get_default_by_location(location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.attestation_providers.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listdefault(self):
        response = None

        try:
            response = self.mgmt_client.attestation_providers.list_default()
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
    AzureRMAttestationProviderInfo()


if __name__ == '__main__':
    main()
