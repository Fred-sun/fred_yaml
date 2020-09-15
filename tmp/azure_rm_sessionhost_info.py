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
module: azure_rm_sessionhost_info
version_added: '2.9'
short_description: Get SessionHost info.
description:
  - Get info of SessionHost.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  host_pool_name:
    description:
      - The name of the host pool within the specified resource group
    required: true
    type: str
  session_host_name:
    description:
      - The name of the session host within the specified host pool
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SessionHost_Get
      azure_rm_sessionhost_info: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        session_host_name: sessionHost1.microsoft.com
        

    - name: SessionHost_List
      azure_rm_sessionhost_info: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
session_hosts:
  description: >-
    A list of dict results where the key is the name of the SessionHost and the
    values are the facts for that SessionHost.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    last_heart_beat:
      description:
        - Last heart beat from SessionHost.
      returned: always
      type: str
      sample: null
    sessions:
      description:
        - Number of sessions on SessionHost.
      returned: always
      type: integer
      sample: null
    agent_version:
      description:
        - Version of agent on SessionHost.
      returned: always
      type: str
      sample: null
    allow_new_session:
      description:
        - Allow a new session.
      returned: always
      type: bool
      sample: null
    virtual_machine_id:
      description:
        - Virtual Machine Id of SessionHost's underlying virtual machine.
      returned: always
      type: str
      sample: null
    resource_id:
      description:
        - Resource Id of SessionHost's underlying virtual machine.
      returned: always
      type: str
      sample: null
    assigned_user:
      description:
        - User assigned to SessionHost.
      returned: always
      type: str
      sample: null
    status:
      description:
        - Status for a SessionHost.
      returned: always
      type: str
      sample: null
    status_timestamp:
      description:
        - The timestamp of the status.
      returned: always
      type: str
      sample: null
    os_version:
      description:
        - The version of the OS on the session host.
      returned: always
      type: str
      sample: null
    sx_sstack_version:
      description:
        - The version of the side by side stack on the session host.
      returned: always
      type: str
      sample: null
    update_state:
      description:
        - Update state of a SessionHost.
      returned: always
      type: str
      sample: null
    last_update_time:
      description:
        - The timestamp of the last update.
      returned: always
      type: str
      sample: null
    update_error_message:
      description:
        - The error message.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of SessionHost definitions.
      returned: always
      type: list
      sample: null
      contains:
        last_heart_beat:
          description:
            - Last heart beat from SessionHost.
          returned: always
          type: str
          sample: null
        sessions:
          description:
            - Number of sessions on SessionHost.
          returned: always
          type: integer
          sample: null
        agent_version:
          description:
            - Version of agent on SessionHost.
          returned: always
          type: str
          sample: null
        allow_new_session:
          description:
            - Allow a new session.
          returned: always
          type: bool
          sample: null
        virtual_machine_id:
          description:
            - Virtual Machine Id of SessionHost's underlying virtual machine.
          returned: always
          type: str
          sample: null
        resource_id:
          description:
            - Resource Id of SessionHost's underlying virtual machine.
          returned: always
          type: str
          sample: null
        assigned_user:
          description:
            - User assigned to SessionHost.
          returned: always
          type: str
          sample: null
        status:
          description:
            - Status for a SessionHost.
          returned: always
          type: str
          sample: null
        status_timestamp:
          description:
            - The timestamp of the status.
          returned: always
          type: str
          sample: null
        os_version:
          description:
            - The version of the OS on the session host.
          returned: always
          type: str
          sample: null
        sx_sstack_version:
          description:
            - The version of the side by side stack on the session host.
          returned: always
          type: str
          sample: null
        update_state:
          description:
            - Update state of a SessionHost.
          returned: always
          type: str
          sample: null
        last_update_time:
          description:
            - The timestamp of the last update.
          returned: always
          type: str
          sample: null
        update_error_message:
          description:
            - The error message.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to the next page of results.
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
    from azure.mgmt.desktop import Desktop Virtualization API Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSessionHostInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            host_pool_name=dict(
                type='str',
                required=True
            ),
            session_host_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.host_pool_name = None
        self.session_host_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-10-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSessionHostInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

        if (self.resource_group_name is not None and
            self.host_pool_name is not None and
            self.session_host_name is not None):
            self.results['session_hosts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.host_pool_name is not None):
            self.results['session_hosts'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.session_hosts.get(resource_group_name=self.resource_group_name,
                                                          host_pool_name=self.host_pool_name,
                                                          session_host_name=self.session_host_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.session_hosts.list(resource_group_name=self.resource_group_name,
                                                           host_pool_name=self.host_pool_name)
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
    AzureRMSessionHostInfo()


if __name__ == '__main__':
    main()
