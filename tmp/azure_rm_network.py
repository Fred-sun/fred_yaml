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
module: azure_rm_network
version_added: '2.9'
short_description: Manage Azure Network instance.
description:
  - 'Create, update and delete instance of Azure Network.'
options:
  resource_group_name:
    description:
      - Azure resource group name
    required: true
    type: str
  network_resource_name:
    description:
      - The identity of the network.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  properties:
    description:
      - Describes properties of a network resource.
    type: dict
    suboptions:
      description:
        description:
          - User readable description of the network.
        type: str
      status:
        description:
          - Status of the network.
        type: str
        choices:
          - Unknown
          - Ready
          - Upgrading
          - Creating
          - Deleting
          - Failed
      status_details:
        description:
          - >-
            Gives additional information about the current status of the
            network.
        type: str
  state:
    description:
      - Assert the state of the Network.
      - >-
        Use C(present) to create or update an Network and C(absent) to delete
        it.
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
    - name: CreateOrUpdateNetwork
      azure_rm_network: 
        network_resource_name: sampleNetwork
        resource_group_name: sbz_demo
        

    - name: DeleteNetwork
      azure_rm_network: 
        network_resource_name: sampleNetwork
        resource_group_name: sbz_demo
        

'''

RETURN = '''
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
    - Describes properties of a network resource.
  returned: always
  type: dict
  sample: null
  contains:
    description:
      description:
        - User readable description of the network.
      returned: always
      type: str
      sample: null
    status:
      description:
        - Status of the network.
      returned: always
      type: str
      sample: null
    status_details:
      description:
        - Gives additional information about the current status of the network.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNetwork(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            network_resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    description=dict(
                        type='str',
                        disposition='description'
                    ),
                    status=dict(
                        type='str',
                        updatable=False,
                        disposition='status',
                        choices=['Unknown',
                                 'Ready',
                                 'Upgrading',
                                 'Creating',
                                 'Deleting',
                                 'Failed']
                    ),
                    status_details=dict(
                        type='str',
                        updatable=False,
                        disposition='status_details'
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
        self.network_resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNetwork, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

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
                response = self.mgmt_client.network.create(resource_group_name=self.resource_group_name,
                                                           network_resource_name=self.network_resource_name,
                                                           network_resource_description=self.body)
            else:
                response = self.mgmt_client.network.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Network instance.')
            self.fail('Error creating the Network instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.network.delete(resource_group_name=self.resource_group_name,
                                                       network_resource_name=self.network_resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Network instance.')
            self.fail('Error deleting the Network instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.network.get(resource_group_name=self.resource_group_name,
                                                    network_resource_name=self.network_resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNetwork()


if __name__ == '__main__':
    main()
