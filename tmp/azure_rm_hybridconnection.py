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
module: azure_rm_hybridconnection
version_added: '2.9'
short_description: Manage Azure HybridConnection instance.
description:
  - 'Create, update and delete instance of Azure HybridConnection.'
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
  hybrid_connection_name:
    description:
      - The hybrid connection name.
    required: true
    type: str
  requires_client_authorization:
    description:
      - >-
        Returns true if client authorization is needed for this hybrid
        connection; otherwise, false.
    type: bool
  user_metadata:
    description:
      - >-
        The usermetadata is a placeholder to store user-defined string data for
        the hybrid connection endpoint. For example, it can be used to store
        descriptive data, such as a list of teams and their contact information.
        Also, user-defined configuration settings can be stored.
    type: str
  state:
    description:
      - Assert the state of the HybridConnection.
      - >-
        Use C(present) to create or update an HybridConnection and C(absent) to
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
    - name: RelayHybridConnectionCreate
      azure_rm_hybridconnection: 
        hybrid_connection_name: sdk-Relay-Hybrid-01
        namespace_name: sdk-RelayNamespace-01
        resource_group_name: RG-eg
        properties:
          requires_client_authorization: true
        

    - name: RelayHybridconnectionDelete
      azure_rm_hybridconnection: 
        hybrid_connection_name: sdk-Relay-Hybrid-01
        namespace_name: sdk-RelayNamespace-01
        resource_group_name: RG-eg
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
created_at:
  description:
    - The time the hybrid connection was created.
  returned: always
  type: str
  sample: null
updated_at:
  description:
    - The time the namespace was updated.
  returned: always
  type: str
  sample: null
listener_count:
  description:
    - >-
      The number of listeners for this hybrid connection. Note that min : 1 and
      max:25 are supported.
  returned: always
  type: integer
  sample: null
requires_client_authorization:
  description:
    - >-
      Returns true if client authorization is needed for this hybrid connection;
      otherwise, false.
  returned: always
  type: bool
  sample: null
user_metadata:
  description:
    - >-
      The usermetadata is a placeholder to store user-defined string data for
      the hybrid connection endpoint. For example, it can be used to store
      descriptive data, such as a list of teams and their contact information.
      Also, user-defined configuration settings can be stored.
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
    from azure.mgmt.relay import Relay API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMHybridConnection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            ),
            hybrid_connection_name=dict(
                type='str',
                required=True
            ),
            requires_client_authorization=dict(
                type='bool',
                disposition='/requires_client_authorization'
            ),
            user_metadata=dict(
                type='str',
                disposition='/user_metadata'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.hybrid_connection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMHybridConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Relay API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

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
            response = self.mgmt_client.hybrid_connections.create_or_update(resource_group_name=self.resource_group_name,
                                                                            namespace_name=self.namespace_name,
                                                                            hybrid_connection_name=self.hybrid_connection_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the HybridConnection instance.')
            self.fail('Error creating the HybridConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.hybrid_connections.delete(resource_group_name=self.resource_group_name,
                                                                  namespace_name=self.namespace_name,
                                                                  hybrid_connection_name=self.hybrid_connection_name)
        except CloudError as e:
            self.log('Error attempting to delete the HybridConnection instance.')
            self.fail('Error deleting the HybridConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.hybrid_connections.get(resource_group_name=self.resource_group_name,
                                                               namespace_name=self.namespace_name,
                                                               hybrid_connection_name=self.hybrid_connection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMHybridConnection()


if __name__ == '__main__':
    main()
