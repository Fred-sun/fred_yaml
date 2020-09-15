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
module: azure_rm_iothubresource
version_added: '2.9'
short_description: Manage Azure IotHubResource instance.
description:
  - 'Create, update and delete instance of Azure IotHubResource.'
options:
  resource_group_name:
    description:
      - The name of the resource group that contains the IoT hub.
      - Resource group identifier.
    required: true
    type: str
  resource_name:
    description:
      - The name of the IoT hub.
      - Name of iot hub to update.
    required: true
    type: str
  if_match:
    description:
      - >-
        ETag of the IoT Hub. Do not specify for creating a brand new IoT Hub.
        Required to update an existing IoT Hub.
    type: str
  location:
    description:
      - The resource location.
    type: str
  etag:
    description:
      - >-
        The Etag field is *not* required. If it is provided in the response
        body, it must also be provided as a header per the normal ETag
        convention.
    type: str
  sku:
    description:
      - IotHub SKU info
    type: dict
    suboptions:
      name:
        description:
          - The name of the SKU.
        required: true
        type: str
        choices:
          - F1
          - S1
          - S2
          - S3
          - B1
          - B2
          - B3
      tier:
        description:
          - The billing tier for the IoT hub.
        type: sealed-choice
      capacity:
        description:
          - >-
            The number of provisioned IoT Hub units. See:
            https://docs.microsoft.com/azure/azure-subscription-service-limits#iot-hub-limits.
        type: integer
  authorization_policies:
    description:
      - >-
        The shared access policies you can use to secure a connection to the IoT
        hub.
    type: list
    suboptions:
      key_name:
        description:
          - The name of the shared access policy.
        required: true
        type: str
      primary_key:
        description:
          - The primary key.
        type: str
      secondary_key:
        description:
          - The secondary key.
        type: str
      rights:
        description:
          - The permissions assigned to the shared access policy.
        required: true
        type: sealed-choice
  public_network_access:
    description:
      - Whether requests from Public Network are allowed
    type: str
    choices:
      - Enabled
      - Disabled
  ip_filter_rules:
    description:
      - The IP filter rules.
    type: list
    suboptions:
      filter_name:
        description:
          - The name of the IP filter rule.
        required: true
        type: str
      action:
        description:
          - The desired action for requests captured by this rule.
        required: true
        type: sealed-choice
      ip_mask:
        description:
          - >-
            A string that contains the IP address range in CIDR notation for the
            rule.
        required: true
        type: str
  min_tls_version:
    description:
      - >-
        Specifies the minimum TLS version to support for this hub. Can be set to
        "1.2" to have clients that use a TLS version below 1.2 to be rejected.
    type: str
  private_endpoint_connections:
    description:
      - Private endpoint connections created on this IotHub
    type: list
    suboptions:
      id:
        description:
          - The resource identifier.
        type: str
      name:
        description:
          - The resource name.
        type: str
      type:
        description:
          - The resource type.
        type: str
      private_endpoint:
        description:
          - The private endpoint property of a private endpoint connection
        type: dict
        suboptions:
          id:
            description:
              - The resource identifier.
            type: str
      private_link_service_connection_state:
        description:
          - The current state of a private endpoint connection
        required: true
        type: dict
        suboptions:
          status:
            description:
              - The status of a private endpoint connection
            required: true
            type: str
            choices:
              - Pending
              - Approved
              - Rejected
              - Disconnected
          description:
            description:
              - >-
                The description for the current state of a private endpoint
                connection
            required: true
            type: str
          actions_required:
            description:
              - Actions required for a private endpoint connection
            type: str
  event_hub_endpoints:
    description:
      - >-
        The Event Hub-compatible endpoint properties. The only possible keys to
        this dictionary is events. This key has to be present in the dictionary
        while making create or update calls for the IoT hub.
    type: dictionary
  routing:
    description:
      - >-
        The routing related properties of the IoT hub. See:
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging
    type: dict
    suboptions:
      endpoints:
        description:
          - >-
            The properties related to the custom endpoints to which your IoT hub
            routes messages based on the routing rules. A maximum of 10 custom
            endpoints are allowed across all endpoint types for paid hubs and
            only 1 custom endpoint is allowed across all endpoint types for free
            hubs.
        type: dict
        suboptions:
          service_bus_queues:
            description:
              - >-
                The list of Service Bus queue endpoints that IoT hub routes the
                messages to, based on the routing rules.
            type: list
            suboptions:
              id:
                description:
                  - Id of the service bus queue endpoint
                type: str
              connection_string:
                description:
                  - The connection string of the service bus queue endpoint.
                type: str
              endpoint_uri:
                description:
                  - >-
                    The url of the service bus queue endpoint. It must include
                    the protocol sb://
                type: str
              entity_path:
                description:
                  - Queue name on the service bus namespace
                type: str
              authentication_type:
                description:
                  - >-
                    Method used to authenticate against the service bus queue
                    endpoint
                type: str
                choices:
                  - keyBased
                  - identityBased
              name:
                description:
                  - >-
                    The name that identifies this endpoint. The name can only
                    include alphanumeric characters, periods, underscores,
                    hyphens and has a maximum length of 64 characters. The
                    following names are reserved:  events, fileNotifications,
                    $default. Endpoint names must be unique across endpoint
                    types. The name need not be the same as the actual queue
                    name.
                required: true
                type: str
              subscription_id:
                description:
                  - >-
                    The subscription identifier of the service bus queue
                    endpoint.
                type: str
              resource_group:
                description:
                  - >-
                    The name of the resource group of the service bus queue
                    endpoint.
                type: str
          service_bus_topics:
            description:
              - >-
                The list of Service Bus topic endpoints that the IoT hub routes
                the messages to, based on the routing rules.
            type: list
            suboptions:
              id:
                description:
                  - Id of the service bus topic endpoint
                type: str
              connection_string:
                description:
                  - The connection string of the service bus topic endpoint.
                type: str
              endpoint_uri:
                description:
                  - >-
                    The url of the service bus topic endpoint. It must include
                    the protocol sb://
                type: str
              entity_path:
                description:
                  - Queue name on the service bus topic
                type: str
              authentication_type:
                description:
                  - >-
                    Method used to authenticate against the service bus topic
                    endpoint
                type: str
                choices:
                  - keyBased
                  - identityBased
              name:
                description:
                  - >-
                    The name that identifies this endpoint. The name can only
                    include alphanumeric characters, periods, underscores,
                    hyphens and has a maximum length of 64 characters. The
                    following names are reserved:  events, fileNotifications,
                    $default. Endpoint names must be unique across endpoint
                    types.  The name need not be the same as the actual topic
                    name.
                required: true
                type: str
              subscription_id:
                description:
                  - >-
                    The subscription identifier of the service bus topic
                    endpoint.
                type: str
              resource_group:
                description:
                  - >-
                    The name of the resource group of the service bus topic
                    endpoint.
                type: str
          event_hubs:
            description:
              - >-
                The list of Event Hubs endpoints that IoT hub routes messages
                to, based on the routing rules. This list does not include the
                built-in Event Hubs endpoint.
            type: list
            suboptions:
              id:
                description:
                  - Id of the event hub endpoint
                type: str
              connection_string:
                description:
                  - 'The connection string of the event hub endpoint. '
                type: str
              endpoint_uri:
                description:
                  - >-
                    The url of the event hub endpoint. It must include the
                    protocol sb://
                type: str
              entity_path:
                description:
                  - Event hub name on the event hub namespace
                type: str
              authentication_type:
                description:
                  - Method used to authenticate against the event hub endpoint
                type: str
                choices:
                  - keyBased
                  - identityBased
              name:
                description:
                  - >-
                    The name that identifies this endpoint. The name can only
                    include alphanumeric characters, periods, underscores,
                    hyphens and has a maximum length of 64 characters. The
                    following names are reserved:  events, fileNotifications,
                    $default. Endpoint names must be unique across endpoint
                    types.
                required: true
                type: str
              subscription_id:
                description:
                  - The subscription identifier of the event hub endpoint.
                type: str
              resource_group:
                description:
                  - The name of the resource group of the event hub endpoint.
                type: str
          storage_containers:
            description:
              - >-
                The list of storage container endpoints that IoT hub routes
                messages to, based on the routing rules.
            type: list
            suboptions:
              id:
                description:
                  - Id of the storage container endpoint
                type: str
              connection_string:
                description:
                  - The connection string of the storage account.
                type: str
              endpoint_uri:
                description:
                  - >-
                    The url of the storage endpoint. It must include the
                    protocol https://
                type: str
              authentication_type:
                description:
                  - Method used to authenticate against the storage endpoint
                type: str
                choices:
                  - keyBased
                  - identityBased
              name:
                description:
                  - >-
                    The name that identifies this endpoint. The name can only
                    include alphanumeric characters, periods, underscores,
                    hyphens and has a maximum length of 64 characters. The
                    following names are reserved:  events, fileNotifications,
                    $default. Endpoint names must be unique across endpoint
                    types.
                required: true
                type: str
              subscription_id:
                description:
                  - The subscription identifier of the storage account.
                type: str
              resource_group:
                description:
                  - The name of the resource group of the storage account.
                type: str
              container_name:
                description:
                  - The name of storage container in the storage account.
                required: true
                type: str
              file_name_format:
                description:
                  - >-
                    File name format for the blob. Default format is
                    {iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}. All
                    parameters are mandatory but can be reordered.
                type: str
              batch_frequency_in_seconds:
                description:
                  - >-
                    Time interval at which blobs are written to storage. Value
                    should be between 60 and 720 seconds. Default value is 300
                    seconds.
                type: integer
              max_chunk_size_in_bytes:
                description:
                  - >-
                    Maximum number of bytes for each blob written to storage.
                    Value should be between 10485760(10MB) and 524288000(500MB).
                    Default value is 314572800(300MB).
                type: integer
              encoding:
                description:
                  - >-
                    Encoding that is used to serialize messages to blobs.
                    Supported values are 'avro', 'avrodeflate', and 'JSON'.
                    Default value is 'avro'.
                type: str
                choices:
                  - Avro
                  - AvroDeflate
                  - JSON
      routes:
        description:
          - >-
            The list of user-provided routing rules that the IoT hub uses to
            route messages to built-in and custom endpoints. A maximum of 100
            routing rules are allowed for paid hubs and a maximum of 5 routing
            rules are allowed for free hubs.
        type: list
        suboptions:
          name:
            description:
              - >-
                The name of the route. The name can only include alphanumeric
                characters, periods, underscores, hyphens, has a maximum length
                of 64 characters, and must be unique.
            required: true
            type: str
          source:
            description:
              - >-
                The source that the routing rule is to be applied to, such as
                DeviceMessages.
            required: true
            type: str
            choices:
              - Invalid
              - DeviceMessages
              - TwinChangeEvents
              - DeviceLifecycleEvents
              - DeviceJobLifecycleEvents
          condition:
            description:
              - >-
                The condition that is evaluated to apply the routing rule. If no
                condition is provided, it evaluates to true by default. For
                grammar, see:
                https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
            type: str
          endpoint_names:
            description:
              - >-
                The list of endpoints to which messages that satisfy the
                condition are routed. Currently only one endpoint is allowed.
            required: true
            type: list
          is_enabled:
            description:
              - Used to specify whether a route is enabled.
            required: true
            type: bool
      fallback_route:
        description:
          - >-
            The properties of the route that is used as a fall-back route when
            none of the conditions specified in the 'routes' section are met.
            This is an optional parameter. When this property is not set, the
            messages which do not meet any of the conditions specified in the
            'routes' section get routed to the built-in eventhub endpoint.
        type: dict
        suboptions:
          name:
            description:
              - >-
                The name of the route. The name can only include alphanumeric
                characters, periods, underscores, hyphens, has a maximum length
                of 64 characters, and must be unique.
            type: str
          source:
            description:
              - >-
                The source to which the routing rule is to be applied to. For
                example, DeviceMessages
            required: true
            type: str
            choices:
              - Invalid
              - DeviceMessages
              - TwinChangeEvents
              - DeviceLifecycleEvents
              - DeviceJobLifecycleEvents
          condition:
            description:
              - >-
                The condition which is evaluated in order to apply the fallback
                route. If the condition is not provided it will evaluate to true
                by default. For grammar, See:
                https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
            type: str
          endpoint_names:
            description:
              - >-
                The list of endpoints to which the messages that satisfy the
                condition are routed to. Currently only 1 endpoint is allowed.
            required: true
            type: list
          is_enabled:
            description:
              - Used to specify whether the fallback route is enabled.
            required: true
            type: bool
      enrichments:
        description:
          - >-
            The list of user-provided enrichments that the IoT hub applies to
            messages to be delivered to built-in and custom endpoints. See:
            https://aka.ms/telemetryoneventgrid
        type: list
        suboptions:
          key:
            description:
              - The key or name for the enrichment property.
            required: true
            type: str
          value:
            description:
              - The value for the enrichment property.
            required: true
            type: str
          endpoint_names:
            description:
              - >-
                The list of endpoints for which the enrichment is applied to the
                message.
            required: true
            type: list
  storage_endpoints:
    description:
      - >-
        The list of Azure Storage endpoints where you can upload files.
        Currently you can configure only one Azure Storage account and that MUST
        have its key as $default. Specifying more than one storage account
        causes an error to be thrown. Not specifying a value for this property
        when the enableFileUploadNotifications property is set to True, causes
        an error to be thrown.
    type: dictionary
  messaging_endpoints:
    description:
      - >-
        The messaging endpoint properties for the file upload notification
        queue.
    type: dictionary
  enable_file_upload_notifications:
    description:
      - 'If True, file upload notifications are enabled.'
    type: bool
  cloud_to_device:
    description:
      - The IoT hub cloud-to-device messaging properties.
    type: dict
    suboptions:
      max_delivery_count:
        description:
          - >-
            The max delivery count for cloud-to-device messages in the device
            queue. See:
            https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
        type: integer
      default_ttl_as_iso8601:
        description:
          - >-
            The default time to live for cloud-to-device messages in the device
            queue. See:
            https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
        type: duration
      feedback:
        description:
          - The properties of the feedback queue for cloud-to-device messages.
        type: dict
        suboptions:
          lock_duration_as_iso8601:
            description:
              - >-
                The lock duration for the feedback queue. See:
                https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
            type: duration
          ttl_as_iso8601:
            description:
              - >-
                The period of time for which a message is available to consume
                before it is expired by the IoT hub. See:
                https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
            type: duration
          max_delivery_count:
            description:
              - >-
                The number of times the IoT hub attempts to deliver a message on
                the feedback queue. See:
                https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
            type: integer
  comments:
    description:
      - IoT hub comments.
    type: str
  features:
    description:
      - The capabilities and features enabled for the IoT hub.
    type: str
    choices:
      - None
      - DeviceManagement
  state:
    description:
      - Assert the state of the IotHubResource.
      - >-
        Use C(present) to create or update an IotHubResource and C(absent) to
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
    - name: IotHubResource_CreateOrUpdate
      azure_rm_iothubresource: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_Update
      azure_rm_iothubresource: 
        resource_group_name: myResourceGroup
        resource_name: myHub
        

    - name: IotHubResource_Delete
      azure_rm_iothubresource: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

'''

RETURN = '''
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - The resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: dictionary
  sample: null
etag:
  description:
    - >-
      The Etag field is *not* required. If it is provided in the response body,
      it must also be provided as a header per the normal ETag convention.
  returned: always
  type: str
  sample: null
sku:
  description:
    - IotHub SKU info
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - The name of the SKU.
      returned: always
      type: str
      sample: null
    tier:
      description:
        - The billing tier for the IoT hub.
      returned: always
      type: sealed-choice
      sample: null
    capacity:
      description:
        - >-
          The number of provisioned IoT Hub units. See:
          https://docs.microsoft.com/azure/azure-subscription-service-limits#iot-hub-limits.
      returned: always
      type: integer
      sample: null
authorization_policies:
  description:
    - >-
      The shared access policies you can use to secure a connection to the IoT
      hub.
  returned: always
  type: list
  sample: null
  contains:
    key_name:
      description:
        - The name of the shared access policy.
      returned: always
      type: str
      sample: null
    primary_key:
      description:
        - The primary key.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - The secondary key.
      returned: always
      type: str
      sample: null
    rights:
      description:
        - The permissions assigned to the shared access policy.
      returned: always
      type: sealed-choice
      sample: null
public_network_access:
  description:
    - Whether requests from Public Network are allowed
  returned: always
  type: str
  sample: null
ip_filter_rules:
  description:
    - The IP filter rules.
  returned: always
  type: list
  sample: null
  contains:
    filter_name:
      description:
        - The name of the IP filter rule.
      returned: always
      type: str
      sample: null
    action:
      description:
        - The desired action for requests captured by this rule.
      returned: always
      type: sealed-choice
      sample: null
    ip_mask:
      description:
        - >-
          A string that contains the IP address range in CIDR notation for the
          rule.
      returned: always
      type: str
      sample: null
min_tls_version:
  description:
    - >-
      Specifies the minimum TLS version to support for this hub. Can be set to
      "1.2" to have clients that use a TLS version below 1.2 to be rejected.
  returned: always
  type: str
  sample: null
private_endpoint_connections:
  description:
    - Private endpoint connections created on this IotHub
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - The resource identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The resource type.
      returned: always
      type: str
      sample: null
    private_endpoint:
      description:
        - The private endpoint property of a private endpoint connection
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The resource identifier.
          returned: always
          type: str
          sample: null
    private_link_service_connection_state:
      description:
        - The current state of a private endpoint connection
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - The status of a private endpoint connection
          returned: always
          type: str
          sample: null
        description:
          description:
            - >-
              The description for the current state of a private endpoint
              connection
          returned: always
          type: str
          sample: null
        actions_required:
          description:
            - Actions required for a private endpoint connection
          returned: always
          type: str
          sample: null
provisioning_state:
  description:
    - The provisioning state.
  returned: always
  type: str
  sample: null
state:
  description:
    - The hub state.
  returned: always
  type: str
  sample: null
host_name:
  description:
    - The name of the host.
  returned: always
  type: str
  sample: null
event_hub_endpoints:
  description:
    - >-
      The Event Hub-compatible endpoint properties. The only possible keys to
      this dictionary is events. This key has to be present in the dictionary
      while making create or update calls for the IoT hub.
  returned: always
  type: dictionary
  sample: null
routing:
  description:
    - >-
      The routing related properties of the IoT hub. See:
      https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging
  returned: always
  type: dict
  sample: null
  contains:
    endpoints:
      description:
        - >-
          The properties related to the custom endpoints to which your IoT hub
          routes messages based on the routing rules. A maximum of 10 custom
          endpoints are allowed across all endpoint types for paid hubs and only
          1 custom endpoint is allowed across all endpoint types for free hubs.
      returned: always
      type: dict
      sample: null
      contains:
        service_bus_queues:
          description:
            - >-
              The list of Service Bus queue endpoints that IoT hub routes the
              messages to, based on the routing rules.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Id of the service bus queue endpoint
              returned: always
              type: str
              sample: null
            connection_string:
              description:
                - The connection string of the service bus queue endpoint.
              returned: always
              type: str
              sample: null
            endpoint_uri:
              description:
                - >-
                  The url of the service bus queue endpoint. It must include the
                  protocol sb://
              returned: always
              type: str
              sample: null
            entity_path:
              description:
                - Queue name on the service bus namespace
              returned: always
              type: str
              sample: null
            authentication_type:
              description:
                - >-
                  Method used to authenticate against the service bus queue
                  endpoint
              returned: always
              type: str
              sample: null
            name:
              description:
                - >-
                  The name that identifies this endpoint. The name can only
                  include alphanumeric characters, periods, underscores, hyphens
                  and has a maximum length of 64 characters. The following names
                  are reserved:  events, fileNotifications, $default. Endpoint
                  names must be unique across endpoint types. The name need not
                  be the same as the actual queue name.
              returned: always
              type: str
              sample: null
            subscription_id:
              description:
                - The subscription identifier of the service bus queue endpoint.
              returned: always
              type: str
              sample: null
            resource_group:
              description:
                - >-
                  The name of the resource group of the service bus queue
                  endpoint.
              returned: always
              type: str
              sample: null
        service_bus_topics:
          description:
            - >-
              The list of Service Bus topic endpoints that the IoT hub routes
              the messages to, based on the routing rules.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Id of the service bus topic endpoint
              returned: always
              type: str
              sample: null
            connection_string:
              description:
                - The connection string of the service bus topic endpoint.
              returned: always
              type: str
              sample: null
            endpoint_uri:
              description:
                - >-
                  The url of the service bus topic endpoint. It must include the
                  protocol sb://
              returned: always
              type: str
              sample: null
            entity_path:
              description:
                - Queue name on the service bus topic
              returned: always
              type: str
              sample: null
            authentication_type:
              description:
                - >-
                  Method used to authenticate against the service bus topic
                  endpoint
              returned: always
              type: str
              sample: null
            name:
              description:
                - >-
                  The name that identifies this endpoint. The name can only
                  include alphanumeric characters, periods, underscores, hyphens
                  and has a maximum length of 64 characters. The following names
                  are reserved:  events, fileNotifications, $default. Endpoint
                  names must be unique across endpoint types.  The name need not
                  be the same as the actual topic name.
              returned: always
              type: str
              sample: null
            subscription_id:
              description:
                - The subscription identifier of the service bus topic endpoint.
              returned: always
              type: str
              sample: null
            resource_group:
              description:
                - >-
                  The name of the resource group of the service bus topic
                  endpoint.
              returned: always
              type: str
              sample: null
        event_hubs:
          description:
            - >-
              The list of Event Hubs endpoints that IoT hub routes messages to,
              based on the routing rules. This list does not include the
              built-in Event Hubs endpoint.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Id of the event hub endpoint
              returned: always
              type: str
              sample: null
            connection_string:
              description:
                - 'The connection string of the event hub endpoint. '
              returned: always
              type: str
              sample: null
            endpoint_uri:
              description:
                - >-
                  The url of the event hub endpoint. It must include the
                  protocol sb://
              returned: always
              type: str
              sample: null
            entity_path:
              description:
                - Event hub name on the event hub namespace
              returned: always
              type: str
              sample: null
            authentication_type:
              description:
                - Method used to authenticate against the event hub endpoint
              returned: always
              type: str
              sample: null
            name:
              description:
                - >-
                  The name that identifies this endpoint. The name can only
                  include alphanumeric characters, periods, underscores, hyphens
                  and has a maximum length of 64 characters. The following names
                  are reserved:  events, fileNotifications, $default. Endpoint
                  names must be unique across endpoint types.
              returned: always
              type: str
              sample: null
            subscription_id:
              description:
                - The subscription identifier of the event hub endpoint.
              returned: always
              type: str
              sample: null
            resource_group:
              description:
                - The name of the resource group of the event hub endpoint.
              returned: always
              type: str
              sample: null
        storage_containers:
          description:
            - >-
              The list of storage container endpoints that IoT hub routes
              messages to, based on the routing rules.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Id of the storage container endpoint
              returned: always
              type: str
              sample: null
            connection_string:
              description:
                - The connection string of the storage account.
              returned: always
              type: str
              sample: null
            endpoint_uri:
              description:
                - >-
                  The url of the storage endpoint. It must include the protocol
                  https://
              returned: always
              type: str
              sample: null
            authentication_type:
              description:
                - Method used to authenticate against the storage endpoint
              returned: always
              type: str
              sample: null
            name:
              description:
                - >-
                  The name that identifies this endpoint. The name can only
                  include alphanumeric characters, periods, underscores, hyphens
                  and has a maximum length of 64 characters. The following names
                  are reserved:  events, fileNotifications, $default. Endpoint
                  names must be unique across endpoint types.
              returned: always
              type: str
              sample: null
            subscription_id:
              description:
                - The subscription identifier of the storage account.
              returned: always
              type: str
              sample: null
            resource_group:
              description:
                - The name of the resource group of the storage account.
              returned: always
              type: str
              sample: null
            container_name:
              description:
                - The name of storage container in the storage account.
              returned: always
              type: str
              sample: null
            file_name_format:
              description:
                - >-
                  File name format for the blob. Default format is
                  {iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}. All
                  parameters are mandatory but can be reordered.
              returned: always
              type: str
              sample: null
            batch_frequency_in_seconds:
              description:
                - >-
                  Time interval at which blobs are written to storage. Value
                  should be between 60 and 720 seconds. Default value is 300
                  seconds.
              returned: always
              type: integer
              sample: null
            max_chunk_size_in_bytes:
              description:
                - >-
                  Maximum number of bytes for each blob written to storage.
                  Value should be between 10485760(10MB) and 524288000(500MB).
                  Default value is 314572800(300MB).
              returned: always
              type: integer
              sample: null
            encoding:
              description:
                - >-
                  Encoding that is used to serialize messages to blobs.
                  Supported values are 'avro', 'avrodeflate', and 'JSON'.
                  Default value is 'avro'.
              returned: always
              type: str
              sample: null
    routes:
      description:
        - >-
          The list of user-provided routing rules that the IoT hub uses to route
          messages to built-in and custom endpoints. A maximum of 100 routing
          rules are allowed for paid hubs and a maximum of 5 routing rules are
          allowed for free hubs.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the route. The name can only include alphanumeric
              characters, periods, underscores, hyphens, has a maximum length of
              64 characters, and must be unique.
          returned: always
          type: str
          sample: null
        source:
          description:
            - >-
              The source that the routing rule is to be applied to, such as
              DeviceMessages.
          returned: always
          type: str
          sample: null
        condition:
          description:
            - >-
              The condition that is evaluated to apply the routing rule. If no
              condition is provided, it evaluates to true by default. For
              grammar, see:
              https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
          returned: always
          type: str
          sample: null
        endpoint_names:
          description:
            - >-
              The list of endpoints to which messages that satisfy the condition
              are routed. Currently only one endpoint is allowed.
          returned: always
          type: list
          sample: null
        is_enabled:
          description:
            - Used to specify whether a route is enabled.
          returned: always
          type: bool
          sample: null
    fallback_route:
      description:
        - >-
          The properties of the route that is used as a fall-back route when
          none of the conditions specified in the 'routes' section are met. This
          is an optional parameter. When this property is not set, the messages
          which do not meet any of the conditions specified in the 'routes'
          section get routed to the built-in eventhub endpoint.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the route. The name can only include alphanumeric
              characters, periods, underscores, hyphens, has a maximum length of
              64 characters, and must be unique.
          returned: always
          type: str
          sample: null
        source:
          description:
            - >-
              The source to which the routing rule is to be applied to. For
              example, DeviceMessages
          returned: always
          type: str
          sample: null
        condition:
          description:
            - >-
              The condition which is evaluated in order to apply the fallback
              route. If the condition is not provided it will evaluate to true
              by default. For grammar, See:
              https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
          returned: always
          type: str
          sample: null
        endpoint_names:
          description:
            - >-
              The list of endpoints to which the messages that satisfy the
              condition are routed to. Currently only 1 endpoint is allowed.
          returned: always
          type: list
          sample: null
        is_enabled:
          description:
            - Used to specify whether the fallback route is enabled.
          returned: always
          type: bool
          sample: null
    enrichments:
      description:
        - >-
          The list of user-provided enrichments that the IoT hub applies to
          messages to be delivered to built-in and custom endpoints. See:
          https://aka.ms/telemetryoneventgrid
      returned: always
      type: list
      sample: null
      contains:
        key:
          description:
            - The key or name for the enrichment property.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The value for the enrichment property.
          returned: always
          type: str
          sample: null
        endpoint_names:
          description:
            - >-
              The list of endpoints for which the enrichment is applied to the
              message.
          returned: always
          type: list
          sample: null
storage_endpoints:
  description:
    - >-
      The list of Azure Storage endpoints where you can upload files. Currently
      you can configure only one Azure Storage account and that MUST have its
      key as $default. Specifying more than one storage account causes an error
      to be thrown. Not specifying a value for this property when the
      enableFileUploadNotifications property is set to True, causes an error to
      be thrown.
  returned: always
  type: dictionary
  sample: null
messaging_endpoints:
  description:
    - The messaging endpoint properties for the file upload notification queue.
  returned: always
  type: dictionary
  sample: null
enable_file_upload_notifications:
  description:
    - 'If True, file upload notifications are enabled.'
  returned: always
  type: bool
  sample: null
cloud_to_device:
  description:
    - The IoT hub cloud-to-device messaging properties.
  returned: always
  type: dict
  sample: null
  contains:
    max_delivery_count:
      description:
        - >-
          The max delivery count for cloud-to-device messages in the device
          queue. See:
          https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
      returned: always
      type: integer
      sample: null
    default_ttl_as_iso8601:
      description:
        - >-
          The default time to live for cloud-to-device messages in the device
          queue. See:
          https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
      returned: always
      type: duration
      sample: null
    feedback:
      description:
        - The properties of the feedback queue for cloud-to-device messages.
      returned: always
      type: dict
      sample: null
      contains:
        lock_duration_as_iso8601:
          description:
            - >-
              The lock duration for the feedback queue. See:
              https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
          returned: always
          type: duration
          sample: null
        ttl_as_iso8601:
          description:
            - >-
              The period of time for which a message is available to consume
              before it is expired by the IoT hub. See:
              https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
          returned: always
          type: duration
          sample: null
        max_delivery_count:
          description:
            - >-
              The number of times the IoT hub attempts to deliver a message on
              the feedback queue. See:
              https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
          returned: always
          type: integer
          sample: null
comments:
  description:
    - IoT hub comments.
  returned: always
  type: str
  sample: null
features:
  description:
    - The capabilities and features enabled for the IoT hub.
  returned: always
  type: str
  sample: null
locations:
  description:
    - Primary and secondary location for iot hub
  returned: always
  type: list
  sample: null
  contains:
    location:
      description:
        - The name of the Azure region
      returned: always
      type: str
      sample: null
    role:
      description:
        - >-
          The role of the region, can be either primary or secondary. The
          primary region is where the IoT hub is currently provisioned. The
          secondary region is the Azure disaster recovery (DR) paired region and
          also the region where the IoT hub can failover to.
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
    from azure.mgmt.iot import iotHubClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMIotHubResource(AzureRMModuleBaseExt):
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
            if_match=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['F1',
                                 'S1',
                                 'S2',
                                 'S3',
                                 'B1',
                                 'B2',
                                 'B3'],
                        required=True
                    ),
                    tier=dict(
                        type='sealed-choice',
                        updatable=False,
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            authorization_policies=dict(
                type='list',
                disposition='/authorization_policies',
                elements='dict',
                options=dict(
                    key_name=dict(
                        type='str',
                        disposition='key_name',
                        required=True
                    ),
                    primary_key=dict(
                        type='str',
                        disposition='primary_key'
                    ),
                    secondary_key=dict(
                        type='str',
                        disposition='secondary_key'
                    ),
                    rights=dict(
                        type='sealed-choice',
                        disposition='rights',
                        required=True
                    )
                )
            ),
            public_network_access=dict(
                type='str',
                disposition='/public_network_access',
                choices=['Enabled',
                         'Disabled']
            ),
            ip_filter_rules=dict(
                type='list',
                disposition='/ip_filter_rules',
                elements='dict',
                options=dict(
                    filter_name=dict(
                        type='str',
                        disposition='filter_name',
                        required=True
                    ),
                    action=dict(
                        type='sealed-choice',
                        disposition='action',
                        required=True
                    ),
                    ip_mask=dict(
                        type='str',
                        disposition='ip_mask',
                        required=True
                    )
                )
            ),
            min_tls_version=dict(
                type='str',
                disposition='/min_tls_version'
            ),
            private_endpoint_connections=dict(
                type='list',
                disposition='/private_endpoint_connections',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        updatable=False,
                        disposition='id'
                    ),
                    name=dict(
                        type='str',
                        updatable=False,
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    private_endpoint=dict(
                        type='dict',
                        disposition='private_endpoint',
                        options=dict(
                            id=dict(
                                type='str',
                                updatable=False,
                                disposition='id'
                            )
                        )
                    ),
                    private_link_service_connection_state=dict(
                        type='dict',
                        disposition='private_link_service_connection_state',
                        required=True,
                        options=dict(
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Pending',
                                         'Approved',
                                         'Rejected',
                                         'Disconnected'],
                                required=True
                            ),
                            description=dict(
                                type='str',
                                disposition='description',
                                required=True
                            ),
                            actions_required=dict(
                                type='str',
                                disposition='actions_required'
                            )
                        )
                    )
                )
            ),
            event_hub_endpoints=dict(
                type='dictionary',
                disposition='/event_hub_endpoints'
            ),
            routing=dict(
                type='dict',
                disposition='/routing',
                options=dict(
                    endpoints=dict(
                        type='dict',
                        disposition='endpoints',
                        options=dict(
                            service_bus_queues=dict(
                                type='list',
                                disposition='service_bus_queues',
                                elements='dict',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    ),
                                    connection_string=dict(
                                        type='str',
                                        disposition='connection_string'
                                    ),
                                    endpoint_uri=dict(
                                        type='str',
                                        disposition='endpoint_uri'
                                    ),
                                    entity_path=dict(
                                        type='str',
                                        disposition='entity_path'
                                    ),
                                    authentication_type=dict(
                                        type='str',
                                        disposition='authentication_type',
                                        choices=['keyBased',
                                                 'identityBased']
                                    ),
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    subscription_id=dict(
                                        type='str',
                                        disposition='subscription_id'
                                    ),
                                    resource_group=dict(
                                        type='str',
                                        disposition='resource_group'
                                    )
                                )
                            ),
                            service_bus_topics=dict(
                                type='list',
                                disposition='service_bus_topics',
                                elements='dict',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    ),
                                    connection_string=dict(
                                        type='str',
                                        disposition='connection_string'
                                    ),
                                    endpoint_uri=dict(
                                        type='str',
                                        disposition='endpoint_uri'
                                    ),
                                    entity_path=dict(
                                        type='str',
                                        disposition='entity_path'
                                    ),
                                    authentication_type=dict(
                                        type='str',
                                        disposition='authentication_type',
                                        choices=['keyBased',
                                                 'identityBased']
                                    ),
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    subscription_id=dict(
                                        type='str',
                                        disposition='subscription_id'
                                    ),
                                    resource_group=dict(
                                        type='str',
                                        disposition='resource_group'
                                    )
                                )
                            ),
                            event_hubs=dict(
                                type='list',
                                disposition='event_hubs',
                                elements='dict',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    ),
                                    connection_string=dict(
                                        type='str',
                                        disposition='connection_string'
                                    ),
                                    endpoint_uri=dict(
                                        type='str',
                                        disposition='endpoint_uri'
                                    ),
                                    entity_path=dict(
                                        type='str',
                                        disposition='entity_path'
                                    ),
                                    authentication_type=dict(
                                        type='str',
                                        disposition='authentication_type',
                                        choices=['keyBased',
                                                 'identityBased']
                                    ),
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    subscription_id=dict(
                                        type='str',
                                        disposition='subscription_id'
                                    ),
                                    resource_group=dict(
                                        type='str',
                                        disposition='resource_group'
                                    )
                                )
                            ),
                            storage_containers=dict(
                                type='list',
                                disposition='storage_containers',
                                elements='dict',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    ),
                                    connection_string=dict(
                                        type='str',
                                        disposition='connection_string'
                                    ),
                                    endpoint_uri=dict(
                                        type='str',
                                        disposition='endpoint_uri'
                                    ),
                                    authentication_type=dict(
                                        type='str',
                                        disposition='authentication_type',
                                        choices=['keyBased',
                                                 'identityBased']
                                    ),
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    subscription_id=dict(
                                        type='str',
                                        disposition='subscription_id'
                                    ),
                                    resource_group=dict(
                                        type='str',
                                        disposition='resource_group'
                                    ),
                                    container_name=dict(
                                        type='str',
                                        disposition='container_name',
                                        required=True
                                    ),
                                    file_name_format=dict(
                                        type='str',
                                        disposition='file_name_format'
                                    ),
                                    batch_frequency_in_seconds=dict(
                                        type='integer',
                                        disposition='batch_frequency_in_seconds'
                                    ),
                                    max_chunk_size_in_bytes=dict(
                                        type='integer',
                                        disposition='max_chunk_size_in_bytes'
                                    ),
                                    encoding=dict(
                                        type='str',
                                        disposition='encoding',
                                        choices=['Avro',
                                                 'AvroDeflate',
                                                 'JSON']
                                    )
                                )
                            )
                        )
                    ),
                    routes=dict(
                        type='list',
                        disposition='routes',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            source=dict(
                                type='str',
                                disposition='source',
                                choices=['Invalid',
                                         'DeviceMessages',
                                         'TwinChangeEvents',
                                         'DeviceLifecycleEvents',
                                         'DeviceJobLifecycleEvents'],
                                required=True
                            ),
                            condition=dict(
                                type='str',
                                disposition='condition'
                            ),
                            endpoint_names=dict(
                                type='list',
                                disposition='endpoint_names',
                                required=True,
                                elements='str'
                            ),
                            is_enabled=dict(
                                type='bool',
                                disposition='is_enabled',
                                required=True
                            )
                        )
                    ),
                    fallback_route=dict(
                        type='dict',
                        disposition='fallback_route',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            source=dict(
                                type='str',
                                disposition='source',
                                choices=['Invalid',
                                         'DeviceMessages',
                                         'TwinChangeEvents',
                                         'DeviceLifecycleEvents',
                                         'DeviceJobLifecycleEvents'],
                                required=True
                            ),
                            condition=dict(
                                type='str',
                                disposition='condition'
                            ),
                            endpoint_names=dict(
                                type='list',
                                disposition='endpoint_names',
                                required=True,
                                elements='str'
                            ),
                            is_enabled=dict(
                                type='bool',
                                disposition='is_enabled',
                                required=True
                            )
                        )
                    ),
                    enrichments=dict(
                        type='list',
                        disposition='enrichments',
                        elements='dict',
                        options=dict(
                            key=dict(
                                type='str',
                                disposition='key',
                                required=True
                            ),
                            value=dict(
                                type='str',
                                disposition='value',
                                required=True
                            ),
                            endpoint_names=dict(
                                type='list',
                                disposition='endpoint_names',
                                required=True,
                                elements='str'
                            )
                        )
                    )
                )
            ),
            storage_endpoints=dict(
                type='dictionary',
                disposition='/storage_endpoints'
            ),
            messaging_endpoints=dict(
                type='dictionary',
                disposition='/messaging_endpoints'
            ),
            enable_file_upload_notifications=dict(
                type='bool',
                disposition='/enable_file_upload_notifications'
            ),
            cloud_to_device=dict(
                type='dict',
                disposition='/cloud_to_device',
                options=dict(
                    max_delivery_count=dict(
                        type='integer',
                        disposition='max_delivery_count'
                    ),
                    default_ttl_as_iso8601=dict(
                        type='duration',
                        disposition='default_ttl_as_iso8601'
                    ),
                    feedback=dict(
                        type='dict',
                        disposition='feedback',
                        options=dict(
                            lock_duration_as_iso8601=dict(
                                type='duration',
                                disposition='lock_duration_as_iso8601'
                            ),
                            ttl_as_iso8601=dict(
                                type='duration',
                                disposition='ttl_as_iso8601'
                            ),
                            max_delivery_count=dict(
                                type='integer',
                                disposition='max_delivery_count'
                            )
                        )
                    )
                )
            ),
            comments=dict(
                type='str',
                disposition='/comments'
            ),
            features=dict(
                type='str',
                disposition='/features',
                choices=['None',
                         'DeviceManagement']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.if_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIotHubResource, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(iotHubClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

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
            response = self.mgmt_client.iot_hub_resource.create_or_update(resource_group_name=self.resource_group_name,
                                                                          resource_name=self.resource_name,
                                                                          if_match=self.if_match,
                                                                          iot_hub_description=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IotHubResource instance.')
            self.fail('Error creating the IotHubResource instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.iot_hub_resource.delete(resource_group_name=self.resource_group_name,
                                                                resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the IotHubResource instance.')
            self.fail('Error deleting the IotHubResource instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.iot_hub_resource.get(resource_group_name=self.resource_group_name,
                                                             resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIotHubResource()


if __name__ == '__main__':
    main()
