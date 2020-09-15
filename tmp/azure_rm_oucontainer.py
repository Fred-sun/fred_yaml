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
module: azure_rm_oucontainer
version_added: '2.9'
short_description: Manage Azure OuContainer instance.
description:
  - 'Create, update and delete instance of Azure OuContainer.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  domain_service_name:
    description:
      - The name of the domain service.
    required: true
    type: str
  ou_container_name:
    description:
      - The name of the OuContainer.
    required: true
    type: str
  account_name:
    description:
      - The account name
    type: str
  spn:
    description:
      - The account spn
    type: str
  password:
    description:
      - The account password
    type: str
  state:
    description:
      - Assert the state of the OuContainer.
      - >-
        Use C(present) to create or update an OuContainer and C(absent) to
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
    - name: Create Domain Service
      azure_rm_oucontainer: 
        domain_service_name: OuContainer.com
        ou_container_name: OuContainer1
        resource_group_name: OuContainerResourceGroup
        

    - name: Delete OuContainer
      azure_rm_oucontainer: 
        domain_service_name: OuContainer.com
        ou_container_name: OuContainer1
        resource_group_name: OuContainerResourceGroup
        

    - name: Update Domain Service
      azure_rm_oucontainer: 
        domain_service_name: OuContainer.com
        ou_container_name: OuContainer1
        resource_group_name: OuContainerResourceGroup
        

'''

RETURN = '''
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
etag:
  description:
    - Resource etag
  returned: always
  type: str
  sample: null
tenant_id:
  description:
    - Azure Active Directory tenant id
  returned: always
  type: str
  sample: null
domain_name:
  description:
    - The domain name of Domain Services.
  returned: always
  type: str
  sample: null
deployment_id:
  description:
    - The Deployment id
  returned: always
  type: str
  sample: null
container_id:
  description:
    - The OuContainer name
  returned: always
  type: str
  sample: null
accounts:
  description:
    - The list of container accounts
  returned: always
  type: list
  sample: null
  contains:
    account_name:
      description:
        - The account name
      returned: always
      type: str
      sample: null
    spn:
      description:
        - The account spn
      returned: always
      type: str
      sample: null
    password:
      description:
        - The account password
      returned: always
      type: str
      sample: null
service_status:
  description:
    - Status of OuContainer instance
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - >-
      The current deployment or provisioning state, which only appears in the
      response.
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
    from azure.mgmt.domain import Domain Services Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOuContainer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            domain_service_name=dict(
                type='str',
                required=True
            ),
            ou_container_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                disposition='/account_name'
            ),
            spn=dict(
                type='str',
                disposition='/spn'
            ),
            password=dict(
                type='str',
                disposition='/password'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.domain_service_name = None
        self.ou_container_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOuContainer, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Domain Services Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
                response = self.mgmt_client.ou_container.create(resource_group_name=self.resource_group_name,
                                                                domain_service_name=self.domain_service_name,
                                                                ou_container_name=self.ou_container_name,
                                                                container_account=self.body)
            else:
                response = self.mgmt_client.ou_container.update(resource_group_name=self.resource_group_name,
                                                                domain_service_name=self.domain_service_name,
                                                                ou_container_name=self.ou_container_name,
                                                                container_account=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the OuContainer instance.')
            self.fail('Error creating the OuContainer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.ou_container.delete(resource_group_name=self.resource_group_name,
                                                            domain_service_name=self.domain_service_name,
                                                            ou_container_name=self.ou_container_name)
        except CloudError as e:
            self.log('Error attempting to delete the OuContainer instance.')
            self.fail('Error deleting the OuContainer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.ou_container.get(resource_group_name=self.resource_group_name,
                                                         domain_service_name=self.domain_service_name,
                                                         ou_container_name=self.ou_container_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOuContainer()


if __name__ == '__main__':
    main()
