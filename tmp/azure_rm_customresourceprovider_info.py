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
module: azure_rm_customresourceprovider_info
version_added: '2.9'
short_description: Get CustomResourceProvider info.
description:
  - Get info of CustomResourceProvider.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  resource_provider_name:
    description:
      - The name of the resource provider.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a custom resource provider
      azure_rm_customresourceprovider_info: 
        resource_group_name: testRG
        resource_provider_name: newrp
        

    - name: List all custom resource providers on the resourceGroup
      azure_rm_customresourceprovider_info: 
        resource_group_name: testRG
        

    - name: List all custom resource providers on the subscription
      azure_rm_customresourceprovider_info: 
        {}
        

'''

RETURN = '''
custom_resource_provider:
  description: >-
    A list of dict results where the key is the name of the
    CustomResourceProvider and the values are the facts for that
    CustomResourceProvider.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    actions:
      description:
        - A list of actions that the custom resource provider implements.
      returned: always
      type: list
      sample: null
      contains:
        routing_type:
          description:
            - The routing types that are supported for action requests.
          returned: always
          type: str
          sample: null
    resource_types:
      description:
        - A list of resource types that the custom resource provider implements.
      returned: always
      type: list
      sample: null
      contains:
        routing_type:
          description:
            - The routing types that are supported for resource requests.
          returned: always
          type: str
          sample: null
    validations:
      description:
        - >-
          A list of validations to run on the custom resource provider's
          requests.
      returned: always
      type: list
      sample: null
      contains:
        validation_type:
          description:
            - The type of validation to run against a matching request.
          returned: always
          type: str
          sample: null
        specification:
          description:
            - >-
              A link to the validation specification. The specification must be
              hosted on raw.githubusercontent.com.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource provider.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The array of custom resource provider manifests.
      returned: always
      type: list
      sample: null
      contains:
        actions:
          description:
            - A list of actions that the custom resource provider implements.
          returned: always
          type: list
          sample: null
          contains:
            routing_type:
              description:
                - The routing types that are supported for action requests.
              returned: always
              type: str
              sample: null
        resource_types:
          description:
            - >-
              A list of resource types that the custom resource provider
              implements.
          returned: always
          type: list
          sample: null
          contains:
            routing_type:
              description:
                - The routing types that are supported for resource requests.
              returned: always
              type: str
              sample: null
        validations:
          description:
            - >-
              A list of validations to run on the custom resource provider's
              requests.
          returned: always
          type: list
          sample: null
          contains:
            validation_type:
              description:
                - The type of validation to run against a matching request.
              returned: always
              type: str
              sample: null
            specification:
              description:
                - >-
                  A link to the validation specification. The specification must
                  be hosted on raw.githubusercontent.com.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - The provisioning state of the resource provider.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
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
    from azure.mgmt.customproviders import customproviders
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCustomResourceProviderInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_provider_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_provider_name = None

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
        super(AzureRMCustomResourceProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(customproviders,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.resource_provider_name is not None):
            self.results['custom_resource_provider'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['custom_resource_provider'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['custom_resource_provider'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.custom_resource_provider.get(resource_group_name=self.resource_group_name,
                                                                     resource_provider_name=self.resource_provider_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.custom_resource_provider.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.custom_resource_provider.list_by_subscription()
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
    AzureRMCustomResourceProviderInfo()


if __name__ == '__main__':
    main()
