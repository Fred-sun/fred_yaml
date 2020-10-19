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
module: azure_rm_token_info
version_added: '2.9'
short_description: Get Token info.
description:
  - Get info of Token.
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  registry_name:
    description:
      - The name of the container registry.
    required: true
    type: str
  token_name:
    description:
      - The name of the token.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: TokenGet
      azure_rm_token_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        token_name: myToken
        

    - name: TokenList
      azure_rm_token_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
tokens:
  description: >-
    A list of dict results where the key is the name of the Token and the values
    are the facts for that Token.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of scope map.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the resource.
      returned: always
      type: str
      sample: null
    scope_map_id:
      description:
        - >-
          The resource ID of the scope map to which the token will be associated
          with.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the token example enabled or disabled.
      returned: always
      type: str
      sample: null
    active_directory_object:
      description:
        - >-
          The Active Directory Object that will be used for authenticating the
          token of a container registry.
      returned: always
      type: dict
      sample: null
      contains:
        object_id:
          description:
            - >-
              The user/group/application object ID for Active Directory Object
              that will be used for authenticating the token of a container
              registry.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              The tenant ID of user/group/application object Active Directory
              Object that will be used for authenticating the token of a
              container registry.
          returned: always
          type: str
          sample: null
    certificates:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - ''
          returned: always
          type: str
          sample: null
        expiry:
          description:
            - The expiry datetime of the certificate.
          returned: always
          type: str
          sample: null
        thumbprint:
          description:
            - The thumbprint of the certificate.
          returned: always
          type: str
          sample: null
        encoded_pem_certificate:
          description:
            - >-
              Base 64 encoded string of the public certificate1 in PEM format
              that will be used for authenticating the token.
          returned: always
          type: str
          sample: null
    passwords:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        creation_time:
          description:
            - The creation datetime of the password.
          returned: always
          type: str
          sample: null
        expiry:
          description:
            - The expiry datetime of the password.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The password name "password1" or "password2"
          returned: always
          type: str
          sample: null
        value:
          description:
            - The password value.
          returned: always
          type: str
          sample: null
    value:
      description:
        - >-
          The list of tokens. Since this list may be incomplete, the nextLink
          field should be used to request the next list of tokens.
      returned: always
      type: list
      sample: null
      contains:
        creation_date:
          description:
            - The creation date of scope map.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state of the resource.
          returned: always
          type: str
          sample: null
        scope_map_id:
          description:
            - >-
              The resource ID of the scope map to which the token will be
              associated with.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The status of the token example enabled or disabled.
          returned: always
          type: str
          sample: null
        active_directory_object:
          description:
            - >-
              The Active Directory Object that will be used for authenticating
              the token of a container registry.
          returned: always
          type: dict
          sample: null
          contains:
            object_id:
              description:
                - >-
                  The user/group/application object ID for Active Directory
                  Object that will be used for authenticating the token of a
                  container registry.
              returned: always
              type: str
              sample: null
            tenant_id:
              description:
                - >-
                  The tenant ID of user/group/application object Active
                  Directory Object that will be used for authenticating the
                  token of a container registry.
              returned: always
              type: str
              sample: null
        certificates:
          description:
            - ''
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - ''
              returned: always
              type: str
              sample: null
            expiry:
              description:
                - The expiry datetime of the certificate.
              returned: always
              type: str
              sample: null
            thumbprint:
              description:
                - The thumbprint of the certificate.
              returned: always
              type: str
              sample: null
            encoded_pem_certificate:
              description:
                - >-
                  Base 64 encoded string of the public certificate1 in PEM
                  format that will be used for authenticating the token.
              returned: always
              type: str
              sample: null
        passwords:
          description:
            - ''
          returned: always
          type: list
          sample: null
          contains:
            creation_time:
              description:
                - The creation datetime of the password.
              returned: always
              type: str
              sample: null
            expiry:
              description:
                - The expiry datetime of the password.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The password name "password1" or "password2"
              returned: always
              type: str
              sample: null
            value:
              description:
                - The password value.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - The URI that can be used to request the next list of tokens.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTokenInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            token_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.token_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-05-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTokenInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-05-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.token_name is not None):
            self.results['tokens'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['tokens'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.tokens.get(resource_group_name=self.resource_group_name,
                                                   registry_name=self.registry_name,
                                                   token_name=self.token_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.tokens.list(resource_group_name=self.resource_group_name,
                                                    registry_name=self.registry_name)
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
    AzureRMTokenInfo()


if __name__ == '__main__':
    main()
