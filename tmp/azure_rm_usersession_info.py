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
module: azure_rm_usersession_info
version_added: '2.9'
short_description: Get UserSession info.
description:
  - Get info of UserSession.
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
  filter:
    description:
      - >-
        OData filter expression. Valid properties for filtering are
        userprincipalname and sessionstate.
    type: str
  session_host_name:
    description:
      - The name of the session host within the specified host pool
    type: str
  user_session_id:
    description:
      - The name of the user session within the specified session host
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: UserSession_ListByHostPool
      azure_rm_usersession_info: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        

    - name: UserSession_Get
      azure_rm_usersession_info: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        session_host_name: sessionHost1.microsoft.com
        user_session_id: '1'
        

    - name: UserSession_List
      azure_rm_usersession_info: 
        host_pool_name: hostPool1
        resource_group_name: resourceGroup1
        session_host_name: sessionHost1.microsoft.com
        

'''

RETURN = '''
user_sessions:
  description: >-
    A list of dict results where the key is the name of the UserSession and the
    values are the facts for that UserSession.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of UserSession definitions.
      returned: always
      type: list
      sample: null
      contains:
        user_principal_name:
          description:
            - The user principal name.
          returned: always
          type: str
          sample: null
        application_type:
          description:
            - Application type of application.
          returned: always
          type: str
          sample: null
        session_state:
          description:
            - State of user session.
          returned: always
          type: str
          sample: null
        active_directory_user_name:
          description:
            - The active directory user name.
          returned: always
          type: str
          sample: null
        create_time:
          description:
            - The timestamp of the user session create.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to the next page of results.
      returned: always
      type: str
      sample: null
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
    user_principal_name:
      description:
        - The user principal name.
      returned: always
      type: str
      sample: null
    application_type:
      description:
        - Application type of application.
      returned: always
      type: str
      sample: null
    session_state:
      description:
        - State of user session.
      returned: always
      type: str
      sample: null
    active_directory_user_name:
      description:
        - The active directory user name.
      returned: always
      type: str
      sample: null
    create_time:
      description:
        - The timestamp of the user session create.
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


class AzureRMUserSessionInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            session_host_name=dict(
                type='str'
            ),
            user_session_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.host_pool_name = None
        self.filter = None
        self.session_host_name = None
        self.user_session_id = None

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
        super(AzureRMUserSessionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Desktop Virtualization API Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-10-preview')

        if (self.resource_group_name is not None and
            self.host_pool_name is not None and
            self.session_host_name is not None and
            self.user_session_id is not None):
            self.results['user_sessions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.host_pool_name is not None and
              self.session_host_name is not None):
            self.results['user_sessions'] = self.format_item(self.list())
        elif (self.resource_group_name is not None and
              self.host_pool_name is not None):
            self.results['user_sessions'] = self.format_item(self.listbyhostpool())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.user_sessions.get(resource_group_name=self.resource_group_name,
                                                          host_pool_name=self.host_pool_name,
                                                          session_host_name=self.session_host_name,
                                                          user_session_id=self.user_session_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.user_sessions.list(resource_group_name=self.resource_group_name,
                                                           host_pool_name=self.host_pool_name,
                                                           session_host_name=self.session_host_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhostpool(self):
        response = None

        try:
            response = self.mgmt_client.user_sessions.list_by_host_pool(resource_group_name=self.resource_group_name,
                                                                        host_pool_name=self.host_pool_name,
                                                                        filter=self.filter)
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
    AzureRMUserSessionInfo()


if __name__ == '__main__':
    main()
