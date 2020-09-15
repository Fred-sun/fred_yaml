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
module: azure_rm_connector
version_added: '2.9'
short_description: Manage Azure Connector instance.
description:
  - 'Create, update and delete instance of Azure Connector.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  hub_name:
    description:
      - The name of the hub.
    required: true
    type: str
  connector_name:
    description:
      - The name of the connector.
    required: true
    type: str
  connector_name1:
    description:
      - Name of the connector.
    type: str
  connector_type:
    description:
      - Type of connector.
    type: str
    choices:
      - None
      - CRM
      - AzureBlob
      - Salesforce
      - ExchangeOnline
      - Outbound
  display_name:
    description:
      - Display name of the connector.
    type: str
  description:
    description:
      - Description of the connector.
    type: str
  connector_properties:
    description:
      - The connector properties.
    type: dictionary
  is_internal:
    description:
      - If this is an internal connector.
    type: bool
  state:
    description:
      - Assert the state of the Connector.
      - >-
        Use C(present) to create or update an Connector and C(absent) to delete
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
    - name: Connectors_CreateOrUpdate
      azure_rm_connector: 
        connector_name: testConnector
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        properties:
          description: Test connector
          connector_properties:
            connection_key_vault_url:
              organization_id: XXX
              organization_url: 'https://XXX.crmlivetie.com/'
          connector_type: AzureBlob
          display_name: testConnector
        

    - name: Connectors_Delete
      azure_rm_connector: 
        connector_name: testConnector
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

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
connector_id:
  description:
    - ID of the connector.
  returned: always
  type: integer
  sample: null
connector_name:
  description:
    - Name of the connector.
  returned: always
  type: str
  sample: null
connector_type:
  description:
    - Type of connector.
  returned: always
  type: str
  sample: null
display_name:
  description:
    - Display name of the connector.
  returned: always
  type: str
  sample: null
description:
  description:
    - Description of the connector.
  returned: always
  type: str
  sample: null
connector_properties:
  description:
    - The connector properties.
  returned: always
  type: dictionary
  sample: null
created:
  description:
    - The created time.
  returned: always
  type: str
  sample: null
last_modified:
  description:
    - The last modified time.
  returned: always
  type: str
  sample: null
state:
  description:
    - State of connector.
  returned: always
  type: sealed-choice
  sample: null
tenant_id:
  description:
    - The hub name.
  returned: always
  type: str
  sample: null
is_internal:
  description:
    - If this is an internal connector.
  returned: always
  type: bool
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConnector(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            hub_name=dict(
                type='str',
                required=True
            ),
            connector_name=dict(
                type='str',
                required=True
            ),
            connector_name1=dict(
                type='str',
                disposition='/connector_name1'
            ),
            connector_type=dict(
                type='str',
                disposition='/connector_type',
                choices=['None',
                         'CRM',
                         'AzureBlob',
                         'Salesforce',
                         'ExchangeOnline',
                         'Outbound']
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            connector_properties=dict(
                type='dictionary',
                disposition='/connector_properties'
            ),
            is_internal=dict(
                type='bool',
                disposition='/is_internal'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.connector_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConnector, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

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
            response = self.mgmt_client.connectors.create_or_update(resource_group_name=self.resource_group_name,
                                                                    hub_name=self.hub_name,
                                                                    connector_name=self.connector_name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Connector instance.')
            self.fail('Error creating the Connector instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.connectors.delete(resource_group_name=self.resource_group_name,
                                                          hub_name=self.hub_name,
                                                          connector_name=self.connector_name)
        except CloudError as e:
            self.log('Error attempting to delete the Connector instance.')
            self.fail('Error deleting the Connector instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.connectors.get(resource_group_name=self.resource_group_name,
                                                       hub_name=self.hub_name,
                                                       connector_name=self.connector_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMConnector()


if __name__ == '__main__':
    main()
