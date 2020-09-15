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
module: azure_rm_token
version_added: '2.9'
short_description: Manage Azure Token instance.
description:
  - 'Create, update and delete instance of Azure Token.'
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
    required: true
    type: str
  scope_map_id:
    description:
      - >-
        The resource ID of the scope map to which the token will be associated
        with.
    type: str
  status:
    description:
      - The status of the token example enabled or disabled.
    type: str
    choices:
      - enabled
      - disabled
  active_directory_object:
    description:
      - >-
        The Active Directory Object that will be used for authenticating the
        token of a container registry.
    type: dict
    suboptions:
      object_id:
        description:
          - >-
            The user/group/application object ID for Active Directory Object
            that will be used for authenticating the token of a container
            registry.
        type: str
      tenant_id:
        description:
          - >-
            The tenant ID of user/group/application object Active Directory
            Object that will be used for authenticating the token of a container
            registry.
        type: str
  certificates:
    description:
      - undefined
    type: list
    suboptions:
      name:
        description:
          - undefined
        type: str
        choices:
          - certificate1
          - certificate2
      expiry:
        description:
          - The expiry datetime of the certificate.
        type: str
      thumbprint:
        description:
          - The thumbprint of the certificate.
        type: str
      encoded_pem_certificate:
        description:
          - >-
            Base 64 encoded string of the public certificate1 in PEM format that
            will be used for authenticating the token.
        type: str
  passwords:
    description:
      - undefined
    type: list
    suboptions:
      creation_time:
        description:
          - The creation datetime of the password.
        type: str
      expiry:
        description:
          - The expiry datetime of the password.
        type: str
      name:
        description:
          - The password name "password1" or "password2"
        type: str
        choices:
          - password1
          - password2
      value:
        description:
          - The password value.
        type: str
  state:
    description:
      - Assert the state of the Token.
      - Use C(present) to create or update an Token and C(absent) to delete it.
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
    - name: TokenCreate
      azure_rm_token: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        token_name: myToken
        

    - name: TokenDelete
      azure_rm_token: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        token_name: myToken
        

    - name: TokenUpdate
      azure_rm_token: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        token_name: myToken
        

'''

RETURN = '''
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
      The Active Directory Object that will be used for authenticating the token
      of a container registry.
  returned: always
  type: dict
  sample: null
  contains:
    object_id:
      description:
        - >-
          The user/group/application object ID for Active Directory Object that
          will be used for authenticating the token of a container registry.
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - >-
          The tenant ID of user/group/application object Active Directory Object
          that will be used for authenticating the token of a container
          registry.
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
          Base 64 encoded string of the public certificate1 in PEM format that
          will be used for authenticating the token.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMToken(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            scope_map_id=dict(
                type='str',
                disposition='/scope_map_id'
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['enabled',
                         'disabled']
            ),
            active_directory_object=dict(
                type='dict',
                disposition='/active_directory_object',
                options=dict(
                    object_id=dict(
                        type='str',
                        disposition='object_id'
                    ),
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id'
                    )
                )
            ),
            certificates=dict(
                type='list',
                disposition='/certificates',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['certificate1',
                                 'certificate2']
                    ),
                    expiry=dict(
                        type='str',
                        disposition='expiry'
                    ),
                    thumbprint=dict(
                        type='str',
                        disposition='thumbprint'
                    ),
                    encoded_pem_certificate=dict(
                        type='str',
                        disposition='encoded_pem_certificate'
                    )
                )
            ),
            passwords=dict(
                type='list',
                disposition='/passwords',
                elements='dict',
                options=dict(
                    creation_time=dict(
                        type='str',
                        disposition='creation_time'
                    ),
                    expiry=dict(
                        type='str',
                        disposition='expiry'
                    ),
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['password1',
                                 'password2']
                    ),
                    value=dict(
                        type='str',
                        updatable=False,
                        disposition='value'
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
        self.registry_name = None
        self.token_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMToken, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-05-01-preview')

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
                response = self.mgmt_client.tokens.create(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name,
                                                          token_name=self.token_name,
                                                          token_create_parameters=self.body)
            else:
                response = self.mgmt_client.tokens.update(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name,
                                                          token_name=self.token_name,
                                                          token_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Token instance.')
            self.fail('Error creating the Token instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.tokens.delete(resource_group_name=self.resource_group_name,
                                                      registry_name=self.registry_name,
                                                      token_name=self.token_name)
        except CloudError as e:
            self.log('Error attempting to delete the Token instance.')
            self.fail('Error deleting the Token instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.tokens.get(resource_group_name=self.resource_group_name,
                                                   registry_name=self.registry_name,
                                                   token_name=self.token_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMToken()


if __name__ == '__main__':
    main()
