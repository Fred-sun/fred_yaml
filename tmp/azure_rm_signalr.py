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
module: azure_rm_signalr
version_added: '2.9'
short_description: Manage Azure SignalR instance.
description:
  - 'Create, update and delete instance of Azure SignalR.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  resource_name:
    description:
      - The name of the SignalR resource.
    required: true
    type: str
  location:
    description:
      - >-
        The GEO location of the SignalR service. e.g. West US | East US | North
        Central US | South Central US.
    type: str
  sku:
    description:
      - 'The billing information of the resource.(e.g. Free, Standard)'
    type: dict
    suboptions:
      name:
        description:
          - "The name of the SKU. Required.\r"
          - "\r"
          - 'Allowed values: Standard_S1, Free_F1'
        required: true
        type: str
      tier:
        description:
          - "Optional tier of this particular SKU. 'Standard' or 'Free'. \r"
          - "\r"
          - '`Basic` is deprecated, use `Standard` instead.'
        type: str
        choices:
          - Free
          - Basic
          - Standard
          - Premium
      size:
        description:
          - Optional string. For future use.
        type: str
      family:
        description:
          - Optional string. For future use.
        type: str
      capacity:
        description:
          - "Optional, integer. The unit count of SignalR resource. 1 by default.\r"
          - "\r"
          - "If present, following values are allowed:\r"
          - "    Free: 1\r"
          - '    Standard: 1,2,5,10,20,50,100'
        type: integer
  kind:
    description:
      - >-
        The kind of the service - e.g. "SignalR", or "RawWebSockets" for
        "Microsoft.SignalRService/SignalR"
    type: str
    choices:
      - SignalR
      - RawWebSockets
  type:
    description:
      - 'Represent the identity type: systemAssigned, userAssigned, None'
    type: str
    choices:
      - None
      - SystemAssigned
      - UserAssigned
  user_assigned_identities:
    description:
      - Get or set the user assigned identities
    type: dictionary
  features:
    description:
      - "List of SignalR featureFlags. e.g. ServiceMode.\r"
      - "\r"
      - "FeatureFlags that are not included in the parameters for the update operation will not be modified.\r"
      - "And the response will only include featureFlags that are explicitly set. \r"
      - "When a featureFlag is not explicitly set, SignalR service will use its globally default value. \r"
      - >-
        But keep in mind, the default value doesn't mean "false". It varies in
        terms of different FeatureFlags.
    type: list
    suboptions:
      flag:
        description:
          - "FeatureFlags is the supported features of Azure SignalR service.\r"
          - "- ServiceMode: Flag for backend server for SignalR service. Values allowed: \"Default\": have your own backend server; \"Serverless\": your application doesn't have a backend server; \"Classic\": for backward compatibility. Support both Default and Serverless mode but not recommended; \"PredefinedOnly\": for future use.\r"
          - >-
            - EnableConnectivityLogs: "true"/"false", to enable/disable the
            connectivity log category respectively.
        required: true
        type: str
        choices:
          - ServiceMode
          - EnableConnectivityLogs
          - EnableMessagingLogs
      value:
        description:
          - >-
            Value of the feature flag. See Azure SignalR service document
            https://docs.microsoft.com/azure/azure-signalr/ for allowed values.
        required: true
        type: str
      properties:
        description:
          - Optional properties related to this feature.
        type: dictionary
  cors:
    description:
      - Cross-Origin Resource Sharing (CORS) settings.
    type: dict
    suboptions:
      allowed_origins:
        description:
          - >-
            Gets or sets the list of origins that should be allowed to make
            cross-origin calls (for example: http://example.com:12345). Use "*"
            to allow all. If omitted, allow all by default.
        type: list
  default_action:
    description:
      - Default action when no other rule matches
    type: str
    choices:
      - Allow
      - Deny
  public_network:
    description:
      - ACL for requests from public network
    type: dict
    suboptions:
      allow:
        description:
          - >-
            Allowed request types. The value can be one or more of:
            ClientConnection, ServerConnection, RESTAPI.
        type: list
      deny:
        description:
          - >-
            Denied request types. The value can be one or more of:
            ClientConnection, ServerConnection, RESTAPI.
        type: list
  private_endpoints:
    description:
      - ACLs for requests from private endpoints
    type: list
    suboptions:
      name:
        description:
          - Name of the private endpoint connection
        required: true
        type: str
  templates:
    description:
      - >-
        Gets or sets the list of Upstream URL templates. Order matters, and the
        first matching template takes effects.
    type: list
    suboptions:
      hub_pattern:
        description:
          - "Gets or sets the matching pattern for hub names. If not set, it matches any hub.\r"
          - "There are 3 kind of patterns supported:\r"
          - "    1. \"*\", it to matches any hub name\r"
          - "    2. Combine multiple hubs with \",\", for example \"hub1,hub2\", it matches \"hub1\" and \"hub2\"\r"
          - '    3. The single hub name, for example, "hub1", it matches "hub1"'
        type: str
      event_pattern:
        description:
          - "Gets or sets the matching pattern for event names. If not set, it matches any event.\r"
          - "There are 3 kind of patterns supported:\r"
          - "    1. \"*\", it to matches any event name\r"
          - "    2. Combine multiple events with \",\", for example \"connect,disconnect\", it matches event \"connect\" and \"disconnect\"\r"
          - '    3. The single event name, for example, "connect", it matches "connect"'
        type: str
      category_pattern:
        description:
          - "Gets or sets the matching pattern for category names. If not set, it matches any category.\r"
          - "There are 3 kind of patterns supported:\r"
          - "    1. \"*\", it to matches any category name\r"
          - "    2. Combine multiple categories with \",\", for example \"connections,messages\", it matches category \"connections\" and \"messages\"\r"
          - '    3. The single category name, for example, "connections", it matches the category "connections"'
        type: str
      url_template:
        description:
          - "Gets or sets the Upstream URL template. You can use 3 predefined parameters {hub}, {category} {event} inside the template, the value of the Upstream URL is dynamically calculated when the client request comes in.\r"
          - >-
            For example, if the urlTemplate is
            `http://example.com/{hub}/api/{event}`, with a client request from
            hub `chat` connects, it will first POST to this URL:
            `http://example.com/chat/api/connect`.
        required: true
        type: str
      auth:
        description:
          - >-
            Gets or sets the auth settings for an upstream. If not set, no auth
            is used for upstream messages.
        type: dict
        suboptions:
          type:
            description:
              - >-
                Gets or sets the type of auth. None or ManagedIdentity is
                supported now.
            type: str
            choices:
              - None
              - ManagedIdentity
          managed_identity:
            description:
              - >-
                Gets or sets the managed identity settings. It's required if the
                auth type is set to ManagedIdentity.
            type: dict
            suboptions:
              resource:
                description:
                  - "The Resource indicating the App ID URI of the target resource.\r"
                  - >-
                    It also appears in the aud (audience) claim of the issued
                    token.
                type: str
  client_cert_enabled:
    description:
      - Request client certificate during TLS handshake if enabled
    type: bool
  state:
    description:
      - Assert the state of the SignalR.
      - >-
        Use C(present) to create or update an SignalR and C(absent) to delete
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
    - name: SignalR_CreateOrUpdate
      azure_rm_signalr: 
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        identity:
          type: SystemAssigned
        kind: SignalR
        location: eastus
        properties:
          cors:
            allowed_origins:
              - 'https://foo.com'
              - 'https://bar.com'
          features:
            - flag: ServiceMode
              properties: {}
              value: Serverless
            - flag: EnableConnectivityLogs
              properties: {}
              value: 'True'
            - flag: EnableMessagingLogs
              properties: {}
              value: 'False'
          network_acls:
            default_action: Deny
            private_endpoints:
              - name: mySignalRService.1fa229cd-bf3f-47f0-8c49-afb36723997e
                allow:
                  - ServerConnection
                deny: {}
            public_network:
              allow:
                - ClientConnection
              deny: {}
          tls:
            client_cert_enabled: false
          upstream:
            templates:
              - auth:
                  type: ManagedIdentity
                  managed_identity:
                    resource: 'api://example'
                category_pattern: '*'
                event_pattern: 'connect,disconnect'
                hub_pattern: '*'
                url_template: 'https://example.com/chat/api/connect'
        sku:
          name: Standard_S1
          capacity: 1
          tier: Standard
        tags:
          key1: value1
        

    - name: SignalR_Delete
      azure_rm_signalr: 
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        

    - name: SignalR_Update
      azure_rm_signalr: 
        resource_group_name: myResourceGroup
        resource_name: mySignalRService
        identity:
          type: SystemAssigned
        kind: SignalR
        location: eastus
        properties:
          cors:
            allowed_origins:
              - 'https://foo.com'
              - 'https://bar.com'
          features:
            - flag: ServiceMode
              properties: {}
              value: Serverless
            - flag: EnableConnectivityLogs
              properties: {}
              value: 'True'
            - flag: EnableMessagingLogs
              properties: {}
              value: 'False'
          network_acls:
            default_action: Deny
            private_endpoints:
              - name: mySignalRService.1fa229cd-bf3f-47f0-8c49-afb36723997e
                allow:
                  - ServerConnection
                deny: {}
            public_network:
              allow:
                - ClientConnection
              deny: {}
          tls:
            client_cert_enabled: false
          upstream:
            templates:
              - auth:
                  type: ManagedIdentity
                  managed_identity:
                    resource: 'api://example'
                category_pattern: '*'
                event_pattern: 'connect,disconnect'
                hub_pattern: '*'
                url_template: 'https://example.com/chat/api/connect'
        sku:
          name: Standard_S1
          capacity: 1
          tier: Standard
        tags:
          key1: value1
        

'''

RETURN = '''
location:
  description:
    - >-
      The GEO location of the SignalR service. e.g. West US | East US | North
      Central US | South Central US.
  returned: always
  type: str
  sample: null
tags:
  description:
    - >-
      Tags of the service which is a list of key value pairs that describe the
      resource.
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
          https://docs.microsoft.com/azure/azure-signalr/ for allowed values.
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
          cross-origin calls (for example: http://example.com:12345). Use "*" to
          allow all. If omitted, allow all by default.
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
      Gets or sets the list of Upstream URL templates. Order matters, and the
      first matching template takes effects.
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
          Gets or sets the auth settings for an upstream. If not set, no auth is
          used for upstream messages.
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
              Gets or sets the managed identity settings. It's required if the
              auth type is set to ManagedIdentity.
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
      The publicly accessible port of the SignalR service which is designed for
      browser/client side usage.
  returned: always
  type: integer
  sample: null
server_port:
  description:
    - >-
      The publicly accessible port of the SignalR service which is designed for
      customer server side usage.
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
              A message indicating if changes on the service provider require
              any updates on the consumer.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.signal import SignalRManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSignalR(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier',
                        choices=['Free',
                                 'Basic',
                                 'Standard',
                                 'Premium']
                    ),
                    size=dict(
                        type='str',
                        disposition='size'
                    ),
                    family=dict(
                        type='str',
                        disposition='family'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            kind=dict(
                type='str',
                disposition='/kind',
                choices=['SignalR',
                         'RawWebSockets']
            ),
            type=dict(
                type='str',
                disposition='/type',
                choices=['None',
                         'SystemAssigned',
                         'UserAssigned']
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            features=dict(
                type='list',
                disposition='/features',
                elements='dict',
                options=dict(
                    flag=dict(
                        type='str',
                        disposition='flag',
                        choices=['ServiceMode',
                                 'EnableConnectivityLogs',
                                 'EnableMessagingLogs'],
                        required=True
                    ),
                    value=dict(
                        type='str',
                        disposition='value',
                        required=True
                    ),
                    properties=dict(
                        type='dictionary',
                        disposition='properties'
                    )
                )
            ),
            cors=dict(
                type='dict',
                disposition='/cors',
                options=dict(
                    allowed_origins=dict(
                        type='list',
                        disposition='allowed_origins',
                        elements='str'
                    )
                )
            ),
            default_action=dict(
                type='str',
                disposition='/default_action',
                choices=['Allow',
                         'Deny']
            ),
            public_network=dict(
                type='dict',
                disposition='/public_network',
                options=dict(
                    allow=dict(
                        type='list',
                        disposition='allow',
                        elements='str'
                    ),
                    deny=dict(
                        type='list',
                        disposition='deny',
                        elements='str'
                    )
                )
            ),
            private_endpoints=dict(
                type='list',
                disposition='/private_endpoints',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    )
                )
            ),
            templates=dict(
                type='list',
                disposition='/templates',
                elements='dict',
                options=dict(
                    hub_pattern=dict(
                        type='str',
                        disposition='hub_pattern'
                    ),
                    event_pattern=dict(
                        type='str',
                        disposition='event_pattern'
                    ),
                    category_pattern=dict(
                        type='str',
                        disposition='category_pattern'
                    ),
                    url_template=dict(
                        type='str',
                        disposition='url_template',
                        required=True
                    ),
                    auth=dict(
                        type='dict',
                        disposition='auth',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                choices=['None',
                                         'ManagedIdentity']
                            ),
                            managed_identity=dict(
                                type='dict',
                                disposition='managed_identity',
                                options=dict(
                                    resource=dict(
                                        type='str',
                                        disposition='resource'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            client_cert_enabled=dict(
                type='bool',
                disposition='/client_cert_enabled'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSignalR, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SignalRManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

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
            response = self.mgmt_client.signal_r.create_or_update(resource_group_name=self.resource_group_name,
                                                                  resource_name=self.resource_name,
                                                                  parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SignalR instance.')
            self.fail('Error creating the SignalR instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.signal_r.delete(resource_group_name=self.resource_group_name,
                                                        resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the SignalR instance.')
            self.fail('Error deleting the SignalR instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.signal_r.get(resource_group_name=self.resource_group_name,
                                                     resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSignalR()


if __name__ == '__main__':
    main()
