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
module: azure_rm_signalr_info
version_added: '2.9'
short_description: Get SignalR info.
description:
  - Get info of SignalR.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    type: str
  resource_name:
    description:
      - The name of the SignalR resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SignalR_ListBySubscription
      azure_rm_signalr_info: 
        {}
        

    - name: SignalR_ListByResourceGroup
      azure_rm_signalr_info: 
        resource_group_name: myResourceGroup
        

    - name: SignalR_Get
      azure_rm_signalr_info: 
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        

'''

RETURN = '''
signal_r:
  description: >-
    A list of dict results where the key is the name of the SignalR and the
    values are the facts for that SignalR.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of SignalR services
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - 'The billing information of the resource.(e.g. Free, Standard)'
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - "The name of the SKU. Required.\r\n\r\nAllowed values: Standard_S1, Free_F1"
              returned: always
              type: str
              sample: null
            tier:
              description:
                - "Optional tier of this particular SKU. 'Standard' or 'Free'. \r\n\r\n`Basic` is deprecated, use `Standard` instead."
              returned: always
              type: str
              sample: null
            size:
              description:
                - Optional string. For future use.
              returned: always
              type: str
              sample: null
            family:
              description:
                - Optional string. For future use.
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - "Optional, integer. The unit count of SignalR resource. 1 by default.\r\n\r\nIf present, following values are allowed:\r\n    Free: 1\r\n    Standard: 1,2,5,10,20,50,100"
              returned: always
              type: integer
              sample: null
        kind:
          description:
            - >-
              The kind of the service - e.g. "SignalR", or "RawWebSockets" for
              "Microsoft.SignalRService/SignalR"
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - 'Represent the identity type: systemAssigned, userAssigned, None'
          returned: always
          type: str
          sample: null
        user_assigned_identities:
          description:
            - Get or set the user assigned identities
          returned: always
          type: dictionary
          sample: null
        principal_id:
          description:
            - "Get the principal id for the system assigned identity.\r\nOnly be used in response."
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - "Get the tenant id for the system assigned identity.\r\nOnly be used in response"
          returned: always
          type: str
          sample: null
        features:
          description:
            - "List of SignalR featureFlags. e.g. ServiceMode.\r\n\r\nFeatureFlags that are not included in the parameters for the update operation will not be modified.\r\nAnd the response will only include featureFlags that are explicitly set. \r\nWhen a featureFlag is not explicitly set, SignalR service will use its globally default value. \r\nBut keep in mind, the default value doesn't mean \"false\". It varies in terms of different FeatureFlags."
          returned: always
          type: list
          sample: null
          contains:
            flag:
              description:
                - "FeatureFlags is the supported features of Azure SignalR service.\r\n- ServiceMode: Flag for backend server for SignalR service. Values allowed: \"Default\": have your own backend server; \"Serverless\": your application doesn't have a backend server; \"Classic\": for backward compatibility. Support both Default and Serverless mode but not recommended; \"PredefinedOnly\": for future use.\r\n- EnableConnectivityLogs: \"true\"/\"false\", to enable/disable the connectivity log category respectively."
              returned: always
              type: str
              sample: null
            value:
              description:
                - >-
                  Value of the feature flag. See Azure SignalR service document
                  https://docs.microsoft.com/azure/azure-signalr/ for allowed
                  values.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Optional properties related to this feature.
              returned: always
              type: dictionary
              sample: null
        cors:
          description:
            - Cross-Origin Resource Sharing (CORS) settings.
          returned: always
          type: dict
          sample: null
          contains:
            allowed_origins:
              description:
                - >-
                  Gets or sets the list of origins that should be allowed to
                  make cross-origin calls (for example:
                  http://example.com:12345). Use "*" to allow all. If omitted,
                  allow all by default.
              returned: always
              type: list
              sample: null
        default_action:
          description:
            - Default action when no other rule matches
          returned: always
          type: str
          sample: null
        public_network:
          description:
            - ACL for requests from public network
          returned: always
          type: dict
          sample: null
          contains:
            allow:
              description:
                - >-
                  Allowed request types. The value can be one or more of:
                  ClientConnection, ServerConnection, RESTAPI.
              returned: always
              type: list
              sample: null
            deny:
              description:
                - >-
                  Denied request types. The value can be one or more of:
                  ClientConnection, ServerConnection, RESTAPI.
              returned: always
              type: list
              sample: null
        private_endpoints:
          description:
            - ACLs for requests from private endpoints
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the private endpoint connection
              returned: always
              type: str
              sample: null
        templates:
          description:
            - >-
              Gets or sets the list of Upstream URL templates. Order matters,
              and the first matching template takes effects.
          returned: always
          type: list
          sample: null
          contains:
            hub_pattern:
              description:
                - "Gets or sets the matching pattern for hub names. If not set, it matches any hub.\r\nThere are 3 kind of patterns supported:\r\n    1. \"*\", it to matches any hub name\r\n    2. Combine multiple hubs with \",\", for example \"hub1,hub2\", it matches \"hub1\" and \"hub2\"\r\n    3. The single hub name, for example, \"hub1\", it matches \"hub1\""
              returned: always
              type: str
              sample: null
            event_pattern:
              description:
                - "Gets or sets the matching pattern for event names. If not set, it matches any event.\r\nThere are 3 kind of patterns supported:\r\n    1. \"*\", it to matches any event name\r\n    2. Combine multiple events with \",\", for example \"connect,disconnect\", it matches event \"connect\" and \"disconnect\"\r\n    3. The single event name, for example, \"connect\", it matches \"connect\""
              returned: always
              type: str
              sample: null
            category_pattern:
              description:
                - "Gets or sets the matching pattern for category names. If not set, it matches any category.\r\nThere are 3 kind of patterns supported:\r\n    1. \"*\", it to matches any category name\r\n    2. Combine multiple categories with \",\", for example \"connections,messages\", it matches category \"connections\" and \"messages\"\r\n    3. The single category name, for example, \"connections\", it matches the category \"connections\""
              returned: always
              type: str
              sample: null
            url_template:
              description:
                - "Gets or sets the Upstream URL template. You can use 3 predefined parameters {hub}, {category} {event} inside the template, the value of the Upstream URL is dynamically calculated when the client request comes in.\r\nFor example, if the urlTemplate is `http://example.com/{hub}/api/{event}`, with a client request from hub `chat` connects, it will first POST to this URL: `http://example.com/chat/api/connect`."
              returned: always
              type: str
              sample: null
            auth:
              description:
                - >-
                  Gets or sets the auth settings for an upstream. If not set, no
                  auth is used for upstream messages.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - >-
                      Gets or sets the type of auth. None or ManagedIdentity is
                      supported now.
                  returned: always
                  type: str
                  sample: null
                managed_identity:
                  description:
                    - >-
                      Gets or sets the managed identity settings. It's required
                      if the auth type is set to ManagedIdentity.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    resource:
                      description:
                        - "The Resource indicating the App ID URI of the target resource.\r\nIt also appears in the aud (audience) claim of the issued token."
                      returned: always
                      type: str
                      sample: null
        provisioning_state:
          description:
            - Provisioning state of the resource.
          returned: always
          type: str
          sample: null
        external_ip:
          description:
            - The publicly accessible IP of the SignalR service.
          returned: always
          type: str
          sample: null
        host_name:
          description:
            - >-
              FQDN of the SignalR service instance. Format:
              xxx.service.signalr.net
          returned: always
          type: str
          sample: null
        public_port:
          description:
            - >-
              The publicly accessible port of the SignalR service which is
              designed for browser/client side usage.
          returned: always
          type: integer
          sample: null
        server_port:
          description:
            - >-
              The publicly accessible port of the SignalR service which is
              designed for customer server side usage.
          returned: always
          type: integer
          sample: null
        version:
          description:
            - >-
              Version of the SignalR resource. Probably you need the same or
              higher version of client SDKs.
          returned: always
          type: str
          sample: null
        private_endpoint_connections:
          description:
            - Private endpoint connections to the SignalR resource.
          returned: always
          type: list
          sample: null
          contains:
            provisioning_state:
              description:
                - Provisioning state of the private endpoint connection
              returned: always
              type: str
              sample: null
            private_link_service_connection_state:
              description:
                - Connection state
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - >-
                      Indicates whether the connection has been
                      Approved/Rejected/Removed by the owner of the service.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - The reason for approval/rejection of the connection.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - >-
                      A message indicating if changes on the service provider
                      require any updates on the consumer.
                  returned: always
                  type: str
                  sample: null
            id_properties_private_endpoint_id:
              description:
                - Full qualified Id of the private endpoint
              returned: always
              type: str
              sample: null
        client_cert_enabled:
          description:
            - Request client certificate during TLS handshake if enabled
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - "The URL the client should use to fetch the next page (per server side paging).\r\nIt's null for now, added for future use."
      returned: always
      type: str
      sample: null
    location:
      description:
        - >-
          The GEO location of the SignalR service. e.g. West US | East US |
          North Central US | South Central US.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - >-
          Tags of the service which is a list of key value pairs that describe
          the resource.
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - 'The billing information of the resource.(e.g. Free, Standard)'
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - "The name of the SKU. Required.\r\n\r\nAllowed values: Standard_S1, Free_F1"
          returned: always
          type: str
          sample: null
        tier:
          description:
            - "Optional tier of this particular SKU. 'Standard' or 'Free'. \r\n\r\n`Basic` is deprecated, use `Standard` instead."
          returned: always
          type: str
          sample: null
        size:
          description:
            - Optional string. For future use.
          returned: always
          type: str
          sample: null
        family:
          description:
            - Optional string. For future use.
          returned: always
          type: str
          sample: null
        capacity:
          description:
            - "Optional, integer. The unit count of SignalR resource. 1 by default.\r\n\r\nIf present, following values are allowed:\r\n    Free: 1\r\n    Standard: 1,2,5,10,20,50,100"
          returned: always
          type: integer
          sample: null
    kind:
      description:
        - >-
          The kind of the service - e.g. "SignalR", or "RawWebSockets" for
          "Microsoft.SignalRService/SignalR"
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - 'Represent the identity type: systemAssigned, userAssigned, None'
      returned: always
      type: str
      sample: null
    user_assigned_identities:
      description:
        - Get or set the user assigned identities
      returned: always
      type: dictionary
      sample: null
    principal_id:
      description:
        - "Get the principal id for the system assigned identity.\r\nOnly be used in response."
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - "Get the tenant id for the system assigned identity.\r\nOnly be used in response"
      returned: always
      type: str
      sample: null
    features:
      description:
        - "List of SignalR featureFlags. e.g. ServiceMode.\r\n\r\nFeatureFlags that are not included in the parameters for the update operation will not be modified.\r\nAnd the response will only include featureFlags that are explicitly set. \r\nWhen a featureFlag is not explicitly set, SignalR service will use its globally default value. \r\nBut keep in mind, the default value doesn't mean \"false\". It varies in terms of different FeatureFlags."
      returned: always
      type: list
      sample: null
      contains:
        flag:
          description:
            - "FeatureFlags is the supported features of Azure SignalR service.\r\n- ServiceMode: Flag for backend server for SignalR service. Values allowed: \"Default\": have your own backend server; \"Serverless\": your application doesn't have a backend server; \"Classic\": for backward compatibility. Support both Default and Serverless mode but not recommended; \"PredefinedOnly\": for future use.\r\n- EnableConnectivityLogs: \"true\"/\"false\", to enable/disable the connectivity log category respectively."
          returned: always
          type: str
          sample: null
        value:
          description:
            - >-
              Value of the feature flag. See Azure SignalR service document
              https://docs.microsoft.com/azure/azure-signalr/ for allowed
              values.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Optional properties related to this feature.
          returned: always
          type: dictionary
          sample: null
    cors:
      description:
        - Cross-Origin Resource Sharing (CORS) settings.
      returned: always
      type: dict
      sample: null
      contains:
        allowed_origins:
          description:
            - >-
              Gets or sets the list of origins that should be allowed to make
              cross-origin calls (for example: http://example.com:12345). Use
              "*" to allow all. If omitted, allow all by default.
          returned: always
          type: list
          sample: null
    default_action:
      description:
        - Default action when no other rule matches
      returned: always
      type: str
      sample: null
    public_network:
      description:
        - ACL for requests from public network
      returned: always
      type: dict
      sample: null
      contains:
        allow:
          description:
            - >-
              Allowed request types. The value can be one or more of:
              ClientConnection, ServerConnection, RESTAPI.
          returned: always
          type: list
          sample: null
        deny:
          description:
            - >-
              Denied request types. The value can be one or more of:
              ClientConnection, ServerConnection, RESTAPI.
          returned: always
          type: list
          sample: null
    private_endpoints:
      description:
        - ACLs for requests from private endpoints
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the private endpoint connection
          returned: always
          type: str
          sample: null
    templates:
      description:
        - >-
          Gets or sets the list of Upstream URL templates. Order matters, and
          the first matching template takes effects.
      returned: always
      type: list
      sample: null
      contains:
        hub_pattern:
          description:
            - "Gets or sets the matching pattern for hub names. If not set, it matches any hub.\r\nThere are 3 kind of patterns supported:\r\n    1. \"*\", it to matches any hub name\r\n    2. Combine multiple hubs with \",\", for example \"hub1,hub2\", it matches \"hub1\" and \"hub2\"\r\n    3. The single hub name, for example, \"hub1\", it matches \"hub1\""
          returned: always
          type: str
          sample: null
        event_pattern:
          description:
            - "Gets or sets the matching pattern for event names. If not set, it matches any event.\r\nThere are 3 kind of patterns supported:\r\n    1. \"*\", it to matches any event name\r\n    2. Combine multiple events with \",\", for example \"connect,disconnect\", it matches event \"connect\" and \"disconnect\"\r\n    3. The single event name, for example, \"connect\", it matches \"connect\""
          returned: always
          type: str
          sample: null
        category_pattern:
          description:
            - "Gets or sets the matching pattern for category names. If not set, it matches any category.\r\nThere are 3 kind of patterns supported:\r\n    1. \"*\", it to matches any category name\r\n    2. Combine multiple categories with \",\", for example \"connections,messages\", it matches category \"connections\" and \"messages\"\r\n    3. The single category name, for example, \"connections\", it matches the category \"connections\""
          returned: always
          type: str
          sample: null
        url_template:
          description:
            - "Gets or sets the Upstream URL template. You can use 3 predefined parameters {hub}, {category} {event} inside the template, the value of the Upstream URL is dynamically calculated when the client request comes in.\r\nFor example, if the urlTemplate is `http://example.com/{hub}/api/{event}`, with a client request from hub `chat` connects, it will first POST to this URL: `http://example.com/chat/api/connect`."
          returned: always
          type: str
          sample: null
        auth:
          description:
            - >-
              Gets or sets the auth settings for an upstream. If not set, no
              auth is used for upstream messages.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - >-
                  Gets or sets the type of auth. None or ManagedIdentity is
                  supported now.
              returned: always
              type: str
              sample: null
            managed_identity:
              description:
                - >-
                  Gets or sets the managed identity settings. It's required if
                  the auth type is set to ManagedIdentity.
              returned: always
              type: dict
              sample: null
              contains:
                resource:
                  description:
                    - "The Resource indicating the App ID URI of the target resource.\r\nIt also appears in the aud (audience) claim of the issued token."
                  returned: always
                  type: str
                  sample: null
    provisioning_state:
      description:
        - Provisioning state of the resource.
      returned: always
      type: str
      sample: null
    external_ip:
      description:
        - The publicly accessible IP of the SignalR service.
      returned: always
      type: str
      sample: null
    host_name:
      description:
        - 'FQDN of the SignalR service instance. Format: xxx.service.signalr.net'
      returned: always
      type: str
      sample: null
    public_port:
      description:
        - >-
          The publicly accessible port of the SignalR service which is designed
          for browser/client side usage.
      returned: always
      type: integer
      sample: null
    server_port:
      description:
        - >-
          The publicly accessible port of the SignalR service which is designed
          for customer server side usage.
      returned: always
      type: integer
      sample: null
    version:
      description:
        - >-
          Version of the SignalR resource. Probably you need the same or higher
          version of client SDKs.
      returned: always
      type: str
      sample: null
    private_endpoint_connections:
      description:
        - Private endpoint connections to the SignalR resource.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - Provisioning state of the private endpoint connection
          returned: always
          type: str
          sample: null
        private_link_service_connection_state:
          description:
            - Connection state
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  Indicates whether the connection has been
                  Approved/Rejected/Removed by the owner of the service.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The reason for approval/rejection of the connection.
              returned: always
              type: str
              sample: null
            actions_required:
              description:
                - >-
                  A message indicating if changes on the service provider
                  require any updates on the consumer.
              returned: always
              type: str
              sample: null
        id_properties_private_endpoint_id:
          description:
            - Full qualified Id of the private endpoint
          returned: always
          type: str
          sample: null
    client_cert_enabled:
      description:
        - Request client certificate during TLS handshake if enabled
      returned: always
      type: bool
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.signal import SignalRManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSignalRInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSignalRInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SignalRManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['signal_r'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['signal_r'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['signal_r'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.signal_r.get(resource_group_name=self.resource_group_name,
                                                     resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.signal_r.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.signal_r.list_by_subscription()
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
    AzureRMSignalRInfo()


if __name__ == '__main__':
    main()
