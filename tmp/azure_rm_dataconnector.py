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
module: azure_rm_dataconnector
version_added: '2.9'
short_description: Manage Azure DataConnector instance.
description:
  - 'Create, update and delete instance of Azure DataConnector.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  workspace_name:
    description:
      - The name of the workspace.
    required: true
    type: str
  data_connector_id:
    description:
      - Connector ID
    required: true
    type: str
  data_connector:
    description:
      - The data connector
    type: dict
    suboptions:
      kind:
        description:
          - The data connector kind
        required: true
        type: str
        choices:
          - AzureActiveDirectory
          - AzureSecurityCenter
          - MicrosoftCloudAppSecurity
          - ThreatIntelligence
          - Office365
          - AmazonWebServicesCloudTrail
          - AzureAdvancedThreatProtection
          - MicrosoftDefenderAdvancedThreatProtection
  state:
    description:
      - Assert the state of the DataConnector.
      - >-
        Use C(present) to create or update an DataConnector and C(absent) to
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
    - name: Creates or updates an Office365 data connector.
      azure_rm_dataconnector: 
        data_connector:
          etag: '"0300bf09-0000-0000-0000-5c37296e0000"'
          kind: Office365
          properties:
            data_types:
              exchange:
                state: Enabled
              share_point:
                state: Enabled
            tenant_id: 2070ecc9-b4d5-4ae4-adaa-936fa1954fa8
        data_connector_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Delete an Office365 data connector.
      azure_rm_dataconnector: 
        data_connector_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

'''

RETURN = '''
id:
  description:
    - Azure resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Azure resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Azure resource type
  returned: always
  type: str
  sample: null
etag:
  description:
    - Etag of the azure resource
  returned: always
  type: str
  sample: null
kind:
  description:
    - The data connector kind
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
    from azure.mgmt.security import Security Insights
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDataConnector(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            ),
            data_connector_id=dict(
                type='str',
                required=True
            ),
            data_connector=dict(
                type='dict',
                disposition='/data_connector',
                options=dict(
                    kind=dict(
                        type='str',
                        disposition='kind',
                        choices=['AzureActiveDirectory',
                                 'AzureSecurityCenter',
                                 'MicrosoftCloudAppSecurity',
                                 'ThreatIntelligence',
                                 'Office365',
                                 'AmazonWebServicesCloudTrail',
                                 'AzureAdvancedThreatProtection',
                                 'MicrosoftDefenderAdvancedThreatProtection'],
                        required=True
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
        self.workspace_name = None
        self.data_connector_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataConnector, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

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
            response = self.mgmt_client.data_connectors.create_or_update(resource_group_name=self.resource_group_name,
                                                                         workspace_name=self.workspace_name,
                                                                         data_connector_id=self.data_connector_id,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DataConnector instance.')
            self.fail('Error creating the DataConnector instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.data_connectors.delete(resource_group_name=self.resource_group_name,
                                                               workspace_name=self.workspace_name,
                                                               data_connector_id=self.data_connector_id)
        except CloudError as e:
            self.log('Error attempting to delete the DataConnector instance.')
            self.fail('Error deleting the DataConnector instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.data_connectors.get(resource_group_name=self.resource_group_name,
                                                            workspace_name=self.workspace_name,
                                                            data_connector_id=self.data_connector_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDataConnector()


if __name__ == '__main__':
    main()
