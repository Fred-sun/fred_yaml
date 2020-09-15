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
module: azure_rm_dataconnection
version_added: '2.9'
short_description: Manage Azure DataConnection instance.
description:
  - 'Create, update and delete instance of Azure DataConnection.'
options:
  resource_group_name:
    description:
      - The name of the resource group containing the Kusto cluster.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the Kusto cluster.
    required: true
    type: str
  database_name:
    description:
      - The name of the database in the Kusto cluster.
    required: true
    type: str
  data_connection_name:
    description:
      - The name of the data connection.
    required: true
    type: str
  parameters:
    description:
      - The data connection parameters supplied to the CreateOrUpdate operation.
      - The data connection parameters supplied to the Update operation.
    type: dict
    suboptions:
      location:
        description:
          - Resource location.
        type: str
      kind:
        description:
          - Kind of the endpoint for the data connection
        required: true
        type: str
        choices:
          - ReadWrite
          - ReadOnlyFollowing
          - EventHub
          - EventGrid
          - IotHub
  state:
    description:
      - Assert the state of the DataConnection.
      - >-
        Use C(present) to create or update an DataConnection and C(absent) to
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
    - name: KustoDataConnectionsCreateOrUpdate
      azure_rm_dataconnection: 
        cluster_name: kustoclusterrptest4
        data_connection_name: DataConnections8
        database_name: KustoDatabase8
        parameters:
          kind: EventHub
          location: westus
          properties:
            consumer_group: testConsumerGroup1
            event_hub_resource_id: >-
              /subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1
        resource_group_name: kustorptest
        kind: EventHub
        location: westus
        properties:
          consumer_group: testConsumerGroup1
          event_hub_resource_id: >-
            /subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1
        

    - name: KustoDataConnectionsUpdate
      azure_rm_dataconnection: 
        cluster_name: kustoclusterrptest4
        data_connection_name: DataConnections8
        database_name: KustoDatabase8
        parameters:
          kind: EventHub
          location: westus
          properties:
            consumer_group: testConsumerGroup1
            event_hub_resource_id: >-
              /subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1
        resource_group_name: kustorptest
        kind: EventHub
        location: westus
        properties:
          consumer_group: testConsumerGroup1
          event_hub_resource_id: >-
            /subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1
        

    - name: KustoDataConnectionsDelete
      azure_rm_dataconnection: 
        cluster_name: kustoclusterrptest4
        data_connection_name: kustoeventhubconnection1
        database_name: KustoDatabase8
        resource_group_name: kustorptest
        

'''

RETURN = '''
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
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
kind:
  description:
    - Kind of the endpoint for the data connection
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
    from azure.mgmt.kusto import KustoManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDataConnection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            data_connection_name=dict(
                type='str',
                required=True
            ),
            parameters=dict(
                type='dict',
                disposition='/parameters',
                options=dict(
                    location=dict(
                        type='str',
                        disposition='location'
                    ),
                    kind=dict(
                        type='str',
                        disposition='kind',
                        choices=['ReadWrite',
                                 'ReadOnlyFollowing',
                                 'EventHub',
                                 'EventGrid',
                                 'IotHub'],
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
        self.cluster_name = None
        self.database_name = None
        self.data_connection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(KustoManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-14')

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
            response = self.mgmt_client.data_connections.create_or_update(resource_group_name=self.resource_group_name,
                                                                          cluster_name=self.cluster_name,
                                                                          database_name=self.database_name,
                                                                          data_connection_name=self.data_connection_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DataConnection instance.')
            self.fail('Error creating the DataConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.data_connections.delete(resource_group_name=self.resource_group_name,
                                                                cluster_name=self.cluster_name,
                                                                database_name=self.database_name,
                                                                data_connection_name=self.data_connection_name)
        except CloudError as e:
            self.log('Error attempting to delete the DataConnection instance.')
            self.fail('Error deleting the DataConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.data_connections.get(resource_group_name=self.resource_group_name,
                                                             cluster_name=self.cluster_name,
                                                             database_name=self.database_name,
                                                             data_connection_name=self.data_connection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDataConnection()


if __name__ == '__main__':
    main()
