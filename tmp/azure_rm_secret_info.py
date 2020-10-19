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
module: azure_rm_secret_info
version_added: '2.9'
short_description: Get Secret info.
description:
  - Get info of Secret.
options:
  resource_group_name:
    description:
      - Azure resource group name
    type: str
  secret_resource_name:
    description:
      - The name of the secret resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetSecret
      azure_rm_secret_info: 
        resource_group_name: sbz_demo
        secret_resource_name: dbConnectionString
        

    - name: ListSecretsByResourceGroup
      azure_rm_secret_info: 
        resource_group_name: sbz_demo
        

    - name: ListSecretsBySubscriptionId
      azure_rm_secret_info: 
        {}
        

'''

RETURN = '''
secret:
  description: >-
    A list of dict results where the key is the name of the Secret and the
    values are the facts for that Secret.
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
    properties:
      description:
        - Describes the properties of a secret resource.
      returned: always
      type: dict
      sample: null
      contains:
        description:
          description:
            - User readable description of the secret.
          returned: always
          type: str
          sample: null
        status:
          description:
            - Status of the resource.
          returned: always
          type: str
          sample: null
        status_details:
          description:
            - >-
              Gives additional information about the current status of the
              secret.
          returned: always
          type: str
          sample: null
        content_type:
          description:
            - >-
              The type of the content stored in the secret value. The value of
              this property is opaque to Service Fabric. Once set, the value of
              this property cannot be changed.
          returned: always
          type: str
          sample: null
    value:
      description:
        - One page of the list.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - Describes the properties of a secret resource.
          returned: always
          type: dict
          sample: null
          contains:
            description:
              description:
                - User readable description of the secret.
              returned: always
              type: str
              sample: null
            status:
              description:
                - Status of the resource.
              returned: always
              type: str
              sample: null
            status_details:
              description:
                - >-
                  Gives additional information about the current status of the
                  secret.
              returned: always
              type: str
              sample: null
            content_type:
              description:
                - >-
                  The type of the content stored in the secret value. The value
                  of this property is opaque to Service Fabric. Once set, the
                  value of this property cannot be changed.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - URI to fetch the next page of the list.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSecretInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            secret_resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.secret_resource_name = None

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
        super(AzureRMSecretInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.secret_resource_name is not None):
            self.results['secret'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['secret'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['secret'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.secret.get(resource_group_name=self.resource_group_name,
                                                   secret_resource_name=self.secret_resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.secret.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.secret.list_by_subscription()
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
    AzureRMSecretInfo()


if __name__ == '__main__':
    main()
