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
module: azure_rm_registration_info
version_added: '2.9'
short_description: Get Registration info.
description:
  - Get info of Registration.
options:
  resource_group:
    description:
      - Name of the resource group.
    required: true
    type: str
  registration_name:
    description:
      - Name of the Azure Stack registration.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Returns a list of all registrations.
      azure_rm_registration_info: 
        resource_group: azurestack
        

    - name: Returns the properties of an Azure Stack registration.
      azure_rm_registration_info: 
        registration_name: testregistration
        resource_group: azurestack
        

'''

RETURN = '''
registrations:
  description: >-
    A list of dict results where the key is the name of the Registration and the
    values are the facts for that Registration.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URI to the next page.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of Registrations
      returned: always
      type: list
      sample: null
      contains:
        object_id:
          description:
            - >-
              The object identifier associated with the Azure Stack connecting
              to Azure.
          returned: always
          type: str
          sample: null
        cloud_id:
          description:
            - The identifier of the registered Azure Stack.
          returned: always
          type: str
          sample: null
        billing_model:
          description:
            - Specifies the billing mode for the Azure Stack registration.
          returned: always
          type: str
          sample: null
    id:
      description:
        - ID of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of Resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Custom tags for the resource.
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - >-
          The entity tag used for optimistic concurrency when modifying the
          resource.
      returned: always
      type: str
      sample: null
    object_id:
      description:
        - >-
          The object identifier associated with the Azure Stack connecting to
          Azure.
      returned: always
      type: str
      sample: null
    cloud_id:
      description:
        - The identifier of the registered Azure Stack.
      returned: always
      type: str
      sample: null
    billing_model:
      description:
        - Specifies the billing mode for the Azure Stack registration.
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
    from azure.mgmt.azure import AzureStackManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRegistrationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            registration_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.registration_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRegistrationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureStackManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group is not None and
            self.registration_name is not None):
            self.results['registrations'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['registrations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.registrations.get(resource_group=self.resource_group,
                                                          registration_name=self.registration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.registrations.list(resource_group=self.resource_group)
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
    AzureRMRegistrationInfo()


if __name__ == '__main__':
    main()
