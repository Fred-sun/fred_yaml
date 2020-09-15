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
module: azure_rm_registeredserver
version_added: '2.9'
short_description: Manage Azure RegisteredServer instance.
description:
  - 'Create, update and delete instance of Azure RegisteredServer.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  storage_sync_service_name:
    description:
      - Name of Storage Sync Service resource.
    required: true
    type: str
  server_id:
    description:
      - GUID identifying the on-premises server.
    required: true
    type: str
  server_certificate:
    description:
      - Registered Server Certificate
    type: str
  agent_version:
    description:
      - Registered Server Agent Version
    type: str
  server_os_version:
    description:
      - Registered Server OS Version
    type: str
  last_heart_beat:
    description:
      - Registered Server last heart beat
    type: str
  server_role:
    description:
      - Registered Server serverRole
    type: str
  cluster_id:
    description:
      - Registered Server clusterId
    type: str
  cluster_name:
    description:
      - Registered Server clusterName
    type: str
  registered_server_create_parameters_properties_server_id:
    description:
      - Registered Server serverId
    type: str
  friendly_name:
    description:
      - Friendly Name
    type: str
  state:
    description:
      - Assert the state of the RegisteredServer.
      - >-
        Use C(present) to create or update an RegisteredServer and C(absent) to
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
    - name: RegisteredServers_Create
      azure_rm_registeredserver: 
        resource_group_name: SampleResourceGroup_1
        server_id: '"080d4133-bdb5-40a0-96a0-71a6057bfe9a"'
        storage_sync_service_name: SampleStorageSyncService_1
        properties:
          agent_version: 1.0.277.0
          last_heart_beat: '"2017-08-08T18:29:06.470652Z"'
          server_certificate: >-
            "MIIDFjCCAf6gAwIBAgIQQS+DS8uhc4VNzUkTw7wbRjANBgkqhkiG9w0BAQ0FADAzMTEwLwYDVQQDEyhhbmt1c2hiLXByb2QzLnJlZG1vbmQuY29ycC5taWNyb3NvZnQuY29tMB4XDTE3MDgwMzE3MDQyNFoXDTE4MDgwNDE3MDQyNFowMzExMC8GA1UEAxMoYW5rdXNoYi1wcm9kMy5yZWRtb25kLmNvcnAubWljcm9zb2Z0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALDRvV4gmsIy6jGDPiHsXmvgVP749NNP7DopdlbHaNhjFmYINHl0uWylyaZmgJrROt2mnxN/zEyJtGnqYHlzUr4xvGq/qV5pqgdB9tag/sw9i22gfe9PRZ0FmSOZnXMbLYgLiDFqLtut5gHcOuWMj03YnkfoBEKlFBxWbagvW2yxz/Sxi9OVSJOKCaXra0RpcIHrO/KFl6ho2eE1/7Ykmfa8hZvSdoPd5gHdLiQcMB/pxq+mWp1fI6c8vFZoDu7Atn+NXTzYPKUxKzaisF12TsaKpohUsJpbB3Wocb0F5frn614D2pg14ERB5otjAMWw1m65csQWPI6dP8KIYe0+QPkCAwEAAaMmMCQwIgYDVR0lAQH/BBgwFgYIKwYBBQUHAwIGCisGAQQBgjcKAwwwDQYJKoZIhvcNAQENBQADggEBAA4RhVIBkw34M1RwakJgHvtjsOFxF1tVQA941NtLokx1l2Z8+GFQkcG4xpZSt+UN6wLerdCbnNhtkCErWUDeaT0jxk4g71Ofex7iM04crT4iHJr8mi96/XnhnkTUs+GDk12VgdeeNEczMZz+8Mxw9dJ5NCnYgTwO0SzGlclRsDvjzkLo8rh2ZG6n/jKrEyNXXo+hOqhupij0QbRP2Tvexdfw201kgN1jdZify8XzJ8Oi0bTS0KpJf2pNPOlooK2bjMUei9ANtEdXwwfVZGWvVh6tJjdv6k14wWWJ1L7zhA1IIVb1J+sQUzJji5iX0DrezjTz1Fg+gAzITaA/WsuujlM="
          server_osversion: 10.0.14393.0
          server_role: Standalone
        

    - name: RegisteredServers_Delete
      azure_rm_registeredserver: 
        resource_group_name: SampleResourceGroup_1
        server_id: 41166691-ab03-43e9-ab3e-0330eda162ac
        storage_sync_service_name: SampleStorageSyncService_1
        

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
server_certificate:
  description:
    - Registered Server Certificate
  returned: always
  type: str
  sample: null
agent_version:
  description:
    - Registered Server Agent Version
  returned: always
  type: str
  sample: null
server_os_version:
  description:
    - Registered Server OS Version
  returned: always
  type: str
  sample: null
server_management_error_code:
  description:
    - Registered Server Management Error Code
  returned: always
  type: integer
  sample: null
last_heart_beat:
  description:
    - Registered Server last heart beat
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Registered Server Provisioning State
  returned: always
  type: str
  sample: null
server_role:
  description:
    - Registered Server serverRole
  returned: always
  type: str
  sample: null
cluster_id:
  description:
    - Registered Server clusterId
  returned: always
  type: str
  sample: null
cluster_name:
  description:
    - Registered Server clusterName
  returned: always
  type: str
  sample: null
server_id:
  description:
    - Registered Server serverId
  returned: always
  type: str
  sample: null
storage_sync_service_uid:
  description:
    - Registered Server storageSyncServiceUid
  returned: always
  type: str
  sample: null
last_workflow_id:
  description:
    - Registered Server lastWorkflowId
  returned: always
  type: str
  sample: null
last_operation_name:
  description:
    - Resource Last Operation Name
  returned: always
  type: str
  sample: null
discovery_endpoint_uri:
  description:
    - Resource discoveryEndpointUri
  returned: always
  type: str
  sample: null
resource_location:
  description:
    - Resource Location
  returned: always
  type: str
  sample: null
service_location:
  description:
    - Service Location
  returned: always
  type: str
  sample: null
friendly_name:
  description:
    - Friendly Name
  returned: always
  type: str
  sample: null
management_endpoint_uri:
  description:
    - Management Endpoint Uri
  returned: always
  type: str
  sample: null
monitoring_endpoint_uri:
  description:
    - Telemetry Endpoint Uri
  returned: always
  type: str
  sample: null
monitoring_configuration:
  description:
    - Monitoring Configuration
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
    from azure.mgmt.microsoft import Microsoft Storage Sync
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRegisteredServer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            storage_sync_service_name=dict(
                type='str',
                required=True
            ),
            server_id=dict(
                type='str',
                required=True
            ),
            server_certificate=dict(
                type='str',
                disposition='/server_certificate'
            ),
            agent_version=dict(
                type='str',
                disposition='/agent_version'
            ),
            server_os_version=dict(
                type='str',
                disposition='/server_os_version'
            ),
            last_heart_beat=dict(
                type='str',
                disposition='/last_heart_beat'
            ),
            server_role=dict(
                type='str',
                disposition='/server_role'
            ),
            cluster_id=dict(
                type='str',
                disposition='/cluster_id'
            ),
            cluster_name=dict(
                type='str',
                disposition='/cluster_name'
            ),
            registered_server_create_parameters_properties_server_id=dict(
                type='str',
                disposition='/registered_server_create_parameters_properties_server_id'
            ),
            friendly_name=dict(
                type='str',
                disposition='/friendly_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.server_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRegisteredServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

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
                response = self.mgmt_client.registered_servers.create(resource_group_name=self.resource_group_name,
                                                                      storage_sync_service_name=self.storage_sync_service_name,
                                                                      server_id=self.server_id,
                                                                      parameters=self.body)
            else:
                response = self.mgmt_client.registered_servers.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RegisteredServer instance.')
            self.fail('Error creating the RegisteredServer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.registered_servers.delete(resource_group_name=self.resource_group_name,
                                                                  storage_sync_service_name=self.storage_sync_service_name,
                                                                  server_id=self.server_id)
        except CloudError as e:
            self.log('Error attempting to delete the RegisteredServer instance.')
            self.fail('Error deleting the RegisteredServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.registered_servers.get(resource_group_name=self.resource_group_name,
                                                               storage_sync_service_name=self.storage_sync_service_name,
                                                               server_id=self.server_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRegisteredServer()


if __name__ == '__main__':
    main()
