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
module: azure_rm_iothubresource_info
version_added: '2.9'
short_description: Get IotHubResource info.
description:
  - Get info of IotHubResource.
options:
  resource_group_name:
    description:
      - The name of the resource group that contains the IoT hub.
    type: str
  resource_name:
    description:
      - The name of the IoT hub.
    type: str
  event_hub_endpoint_name:
    description:
      - The name of the Event Hub-compatible endpoint.
      - The name of the Event Hub-compatible endpoint in the IoT hub.
    type: str
  name:
    description:
      - The name of the consumer group to retrieve.
    type: str
  job_id:
    description:
      - The job identifier.
    type: str
  iot_hub_name:
    description:
      - undefined
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: IotHubResource_Get
      azure_rm_iothubresource_info: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_ListBySubscription
      azure_rm_iothubresource_info: 
        {}
        

    - name: IotHubResource_ListByResourceGroup
      azure_rm_iothubresource_info: 
        resource_group_name: myResourceGroup
        

    - name: IotHubResource_GetStats
      azure_rm_iothubresource_info: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_GetValidSkus
      azure_rm_iothubresource_info: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_ListEventHubConsumerGroups
      azure_rm_iothubresource_info: 
        event_hub_endpoint_name: events
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_ListJobs
      azure_rm_iothubresource_info: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_GetJob
      azure_rm_iothubresource_info: 
        job_id: test
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_GetQuotaMetrics
      azure_rm_iothubresource_info: 
        resource_group_name: myResourceGroup
        resource_name: testHub
        

    - name: IotHubResource_GetEndpointHealth
      azure_rm_iothubresource_info: 
        iot_hub_name: testHub
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
iot_hub_resource:
  description: >-
    A list of dict results where the key is the name of the IotHubResource and
    the values are the facts for that IotHubResource.
  returned: always
  type: complex
  contains:
    id:
      description:
        - |-
          The resource identifier.
          The Event Hub-compatible consumer group identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - |-
          The resource name.
          The Event Hub-compatible consumer group name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - |-
          The resource type.
          the resource type.
          The type of the job.
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
          The Etag field is *not* required. If it is provided in the response
          body, it must also be provided as a header per the normal ETag
          convention.

          The etag.
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
          The shared access policies you can use to secure a connection to the
          IoT hub.
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
              A string that contains the IP address range in CIDR notation for
              the rule.
          returned: always
          type: str
          sample: null
    min_tls_version:
      description:
        - >-
          Specifies the minimum TLS version to support for this hub. Can be set
          to "1.2" to have clients that use a TLS version below 1.2 to be
          rejected.
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
          The Event Hub-compatible endpoint properties. The only possible keys
          to this dictionary is events. This key has to be present in the
          dictionary while making create or update calls for the IoT hub.
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
              The properties related to the custom endpoints to which your IoT
              hub routes messages based on the routing rules. A maximum of 10
              custom endpoints are allowed across all endpoint types for paid
              hubs and only 1 custom endpoint is allowed across all endpoint
              types for free hubs.
          returned: always
          type: dict
          sample: null
          contains:
            service_bus_queues:
              description:
                - >-
                  The list of Service Bus queue endpoints that IoT hub routes
                  the messages to, based on the routing rules.
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
                      The url of the service bus queue endpoint. It must include
                      the protocol sb://
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
                      include alphanumeric characters, periods, underscores,
                      hyphens and has a maximum length of 64 characters. The
                      following names are reserved:  events, fileNotifications,
                      $default. Endpoint names must be unique across endpoint
                      types. The name need not be the same as the actual queue
                      name.
                  returned: always
                  type: str
                  sample: null
                subscription_id:
                  description:
                    - >-
                      The subscription identifier of the service bus queue
                      endpoint.
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
                  The list of Service Bus topic endpoints that the IoT hub
                  routes the messages to, based on the routing rules.
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
                      The url of the service bus topic endpoint. It must include
                      the protocol sb://
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
                      include alphanumeric characters, periods, underscores,
                      hyphens and has a maximum length of 64 characters. The
                      following names are reserved:  events, fileNotifications,
                      $default. Endpoint names must be unique across endpoint
                      types.  The name need not be the same as the actual topic
                      name.
                  returned: always
                  type: str
                  sample: null
                subscription_id:
                  description:
                    - >-
                      The subscription identifier of the service bus topic
                      endpoint.
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
                  The list of Event Hubs endpoints that IoT hub routes messages
                  to, based on the routing rules. This list does not include the
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
                      include alphanumeric characters, periods, underscores,
                      hyphens and has a maximum length of 64 characters. The
                      following names are reserved:  events, fileNotifications,
                      $default. Endpoint names must be unique across endpoint
                      types.
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
                      The url of the storage endpoint. It must include the
                      protocol https://
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
                      include alphanumeric characters, periods, underscores,
                      hyphens and has a maximum length of 64 characters. The
                      following names are reserved:  events, fileNotifications,
                      $default. Endpoint names must be unique across endpoint
                      types.
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
                      Value should be between 10485760(10MB) and
                      524288000(500MB). Default value is 314572800(300MB).
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
              The list of user-provided routing rules that the IoT hub uses to
              route messages to built-in and custom endpoints. A maximum of 100
              routing rules are allowed for paid hubs and a maximum of 5 routing
              rules are allowed for free hubs.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the route. The name can only include alphanumeric
                  characters, periods, underscores, hyphens, has a maximum
                  length of 64 characters, and must be unique.
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
                  The condition that is evaluated to apply the routing rule. If
                  no condition is provided, it evaluates to true by default. For
                  grammar, see:
                  https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
              returned: always
              type: str
              sample: null
            endpoint_names:
              description:
                - >-
                  The list of endpoints to which messages that satisfy the
                  condition are routed. Currently only one endpoint is allowed.
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
              none of the conditions specified in the 'routes' section are met.
              This is an optional parameter. When this property is not set, the
              messages which do not meet any of the conditions specified in the
              'routes' section get routed to the built-in eventhub endpoint.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the route. The name can only include alphanumeric
                  characters, periods, underscores, hyphens, has a maximum
                  length of 64 characters, and must be unique.
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
                  The condition which is evaluated in order to apply the
                  fallback route. If the condition is not provided it will
                  evaluate to true by default. For grammar, See:
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
                  The list of endpoints for which the enrichment is applied to
                  the message.
              returned: always
              type: list
              sample: null
    storage_endpoints:
      description:
        - >-
          The list of Azure Storage endpoints where you can upload files.
          Currently you can configure only one Azure Storage account and that
          MUST have its key as $default. Specifying more than one storage
          account causes an error to be thrown. Not specifying a value for this
          property when the enableFileUploadNotifications property is set to
          True, causes an error to be thrown.
      returned: always
      type: dictionary
      sample: null
    messaging_endpoints:
      description:
        - >-
          The messaging endpoint properties for the file upload notification
          queue.
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
              The default time to live for cloud-to-device messages in the
              device queue. See:
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
                  The number of times the IoT hub attempts to deliver a message
                  on the feedback queue. See:
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
              secondary region is the Azure disaster recovery (DR) paired region
              and also the region where the IoT hub can failover to.
          returned: always
          type: str
          sample: null
    value:
      description:
        - |-
          The array of IotHubDescription objects.
          The array of IotHubSkuDescription.
          List of consumer groups objects
          The array of JobResponse objects.
          The array of quota metrics objects.
          JSON-serialized array of Endpoint health data
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - >-
              The Etag field is *not* required. If it is provided in the
              response body, it must also be provided as a header per the normal
              ETag convention.
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
              The shared access policies you can use to secure a connection to
              the IoT hub.
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
                  A string that contains the IP address range in CIDR notation
                  for the rule.
              returned: always
              type: str
              sample: null
        min_tls_version:
          description:
            - >-
              Specifies the minimum TLS version to support for this hub. Can be
              set to "1.2" to have clients that use a TLS version below 1.2 to
              be rejected.
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
                      The description for the current state of a private
                      endpoint connection
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
              The Event Hub-compatible endpoint properties. The only possible
              keys to this dictionary is events. This key has to be present in
              the dictionary while making create or update calls for the IoT
              hub.
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
                  The properties related to the custom endpoints to which your
                  IoT hub routes messages based on the routing rules. A maximum
                  of 10 custom endpoints are allowed across all endpoint types
                  for paid hubs and only 1 custom endpoint is allowed across all
                  endpoint types for free hubs.
              returned: always
              type: dict
              sample: null
              contains:
                service_bus_queues:
                  description:
                    - >-
                      The list of Service Bus queue endpoints that IoT hub
                      routes the messages to, based on the routing rules.
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
                        - >-
                          The connection string of the service bus queue
                          endpoint.
                      returned: always
                      type: str
                      sample: null
                    endpoint_uri:
                      description:
                        - >-
                          The url of the service bus queue endpoint. It must
                          include the protocol sb://
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
                          Method used to authenticate against the service bus
                          queue endpoint
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - >-
                          The name that identifies this endpoint. The name can
                          only include alphanumeric characters, periods,
                          underscores, hyphens and has a maximum length of 64
                          characters. The following names are reserved:  events,
                          fileNotifications, $default. Endpoint names must be
                          unique across endpoint types. The name need not be the
                          same as the actual queue name.
                      returned: always
                      type: str
                      sample: null
                    subscription_id:
                      description:
                        - >-
                          The subscription identifier of the service bus queue
                          endpoint.
                      returned: always
                      type: str
                      sample: null
                    resource_group:
                      description:
                        - >-
                          The name of the resource group of the service bus
                          queue endpoint.
                      returned: always
                      type: str
                      sample: null
                service_bus_topics:
                  description:
                    - >-
                      The list of Service Bus topic endpoints that the IoT hub
                      routes the messages to, based on the routing rules.
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
                        - >-
                          The connection string of the service bus topic
                          endpoint.
                      returned: always
                      type: str
                      sample: null
                    endpoint_uri:
                      description:
                        - >-
                          The url of the service bus topic endpoint. It must
                          include the protocol sb://
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
                          Method used to authenticate against the service bus
                          topic endpoint
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - >-
                          The name that identifies this endpoint. The name can
                          only include alphanumeric characters, periods,
                          underscores, hyphens and has a maximum length of 64
                          characters. The following names are reserved:  events,
                          fileNotifications, $default. Endpoint names must be
                          unique across endpoint types.  The name need not be
                          the same as the actual topic name.
                      returned: always
                      type: str
                      sample: null
                    subscription_id:
                      description:
                        - >-
                          The subscription identifier of the service bus topic
                          endpoint.
                      returned: always
                      type: str
                      sample: null
                    resource_group:
                      description:
                        - >-
                          The name of the resource group of the service bus
                          topic endpoint.
                      returned: always
                      type: str
                      sample: null
                event_hubs:
                  description:
                    - >-
                      The list of Event Hubs endpoints that IoT hub routes
                      messages to, based on the routing rules. This list does
                      not include the built-in Event Hubs endpoint.
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
                        - >-
                          Method used to authenticate against the event hub
                          endpoint
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - >-
                          The name that identifies this endpoint. The name can
                          only include alphanumeric characters, periods,
                          underscores, hyphens and has a maximum length of 64
                          characters. The following names are reserved:  events,
                          fileNotifications, $default. Endpoint names must be
                          unique across endpoint types.
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
                        - >-
                          The name of the resource group of the event hub
                          endpoint.
                      returned: always
                      type: str
                      sample: null
                storage_containers:
                  description:
                    - >-
                      The list of storage container endpoints that IoT hub
                      routes messages to, based on the routing rules.
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
                          The url of the storage endpoint. It must include the
                          protocol https://
                      returned: always
                      type: str
                      sample: null
                    authentication_type:
                      description:
                        - >-
                          Method used to authenticate against the storage
                          endpoint
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - >-
                          The name that identifies this endpoint. The name can
                          only include alphanumeric characters, periods,
                          underscores, hyphens and has a maximum length of 64
                          characters. The following names are reserved:  events,
                          fileNotifications, $default. Endpoint names must be
                          unique across endpoint types.
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
                          Time interval at which blobs are written to storage.
                          Value should be between 60 and 720 seconds. Default
                          value is 300 seconds.
                      returned: always
                      type: integer
                      sample: null
                    max_chunk_size_in_bytes:
                      description:
                        - >-
                          Maximum number of bytes for each blob written to
                          storage. Value should be between 10485760(10MB) and
                          524288000(500MB). Default value is 314572800(300MB).
                      returned: always
                      type: integer
                      sample: null
                    encoding:
                      description:
                        - >-
                          Encoding that is used to serialize messages to blobs.
                          Supported values are 'avro', 'avrodeflate', and
                          'JSON'. Default value is 'avro'.
                      returned: always
                      type: str
                      sample: null
            routes:
              description:
                - >-
                  The list of user-provided routing rules that the IoT hub uses
                  to route messages to built-in and custom endpoints. A maximum
                  of 100 routing rules are allowed for paid hubs and a maximum
                  of 5 routing rules are allowed for free hubs.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - >-
                      The name of the route. The name can only include
                      alphanumeric characters, periods, underscores, hyphens,
                      has a maximum length of 64 characters, and must be unique.
                  returned: always
                  type: str
                  sample: null
                source:
                  description:
                    - >-
                      The source that the routing rule is to be applied to, such
                      as DeviceMessages.
                  returned: always
                  type: str
                  sample: null
                condition:
                  description:
                    - >-
                      The condition that is evaluated to apply the routing rule.
                      If no condition is provided, it evaluates to true by
                      default. For grammar, see:
                      https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
                  returned: always
                  type: str
                  sample: null
                endpoint_names:
                  description:
                    - >-
                      The list of endpoints to which messages that satisfy the
                      condition are routed. Currently only one endpoint is
                      allowed.
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
                  The properties of the route that is used as a fall-back route
                  when none of the conditions specified in the 'routes' section
                  are met. This is an optional parameter. When this property is
                  not set, the messages which do not meet any of the conditions
                  specified in the 'routes' section get routed to the built-in
                  eventhub endpoint.
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - >-
                      The name of the route. The name can only include
                      alphanumeric characters, periods, underscores, hyphens,
                      has a maximum length of 64 characters, and must be unique.
                  returned: always
                  type: str
                  sample: null
                source:
                  description:
                    - >-
                      The source to which the routing rule is to be applied to.
                      For example, DeviceMessages
                  returned: always
                  type: str
                  sample: null
                condition:
                  description:
                    - >-
                      The condition which is evaluated in order to apply the
                      fallback route. If the condition is not provided it will
                      evaluate to true by default. For grammar, See:
                      https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
                  returned: always
                  type: str
                  sample: null
                endpoint_names:
                  description:
                    - >-
                      The list of endpoints to which the messages that satisfy
                      the condition are routed to. Currently only 1 endpoint is
                      allowed.
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
                  The list of user-provided enrichments that the IoT hub applies
                  to messages to be delivered to built-in and custom endpoints.
                  See: https://aka.ms/telemetryoneventgrid
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
                      The list of endpoints for which the enrichment is applied
                      to the message.
                  returned: always
                  type: list
                  sample: null
        storage_endpoints:
          description:
            - >-
              The list of Azure Storage endpoints where you can upload files.
              Currently you can configure only one Azure Storage account and
              that MUST have its key as $default. Specifying more than one
              storage account causes an error to be thrown. Not specifying a
              value for this property when the enableFileUploadNotifications
              property is set to True, causes an error to be thrown.
          returned: always
          type: dictionary
          sample: null
        messaging_endpoints:
          description:
            - >-
              The messaging endpoint properties for the file upload notification
              queue.
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
                  The max delivery count for cloud-to-device messages in the
                  device queue. See:
                  https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
              returned: always
              type: integer
              sample: null
            default_ttl_as_iso8601:
              description:
                - >-
                  The default time to live for cloud-to-device messages in the
                  device queue. See:
                  https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
              returned: always
              type: duration
              sample: null
            feedback:
              description:
                - >-
                  The properties of the feedback queue for cloud-to-device
                  messages.
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
                      The period of time for which a message is available to
                      consume before it is expired by the IoT hub. See:
                      https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages.
                  returned: always
                  type: duration
                  sample: null
                max_delivery_count:
                  description:
                    - >-
                      The number of times the IoT hub attempts to deliver a
                      message on the feedback queue. See:
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
                  The role of the region, can be either primary or secondary.
                  The primary region is where the IoT hub is currently
                  provisioned. The secondary region is the Azure disaster
                  recovery (DR) paired region and also the region where the IoT
                  hub can failover to.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - |-
          The next link.
          Link to more results
      returned: always
      type: str
      sample: null
    total_device_count:
      description:
        - The total count of devices in the identity registry.
      returned: always
      type: integer
      sample: null
    enabled_device_count:
      description:
        - The count of enabled devices in the identity registry.
      returned: always
      type: integer
      sample: null
    disabled_device_count:
      description:
        - The count of disabled devices in the identity registry.
      returned: always
      type: integer
      sample: null
    properties:
      description:
        - The tags.
      returned: always
      type: dictionary
      sample: null
    job_id:
      description:
        - The job identifier.
      returned: always
      type: str
      sample: null
    start_time_utc:
      description:
        - The start time of the job.
      returned: always
      type: str
      sample: null
    end_time_utc:
      description:
        - The time the job stopped processing.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the job.
      returned: always
      type: sealed-choice
      sample: null
    failure_reason:
      description:
        - >-
          If status == failed, this string containing the reason for the
          failure.
      returned: always
      type: str
      sample: null
    status_message:
      description:
        - The status message for the job.
      returned: always
      type: str
      sample: null
    parent_job_id:
      description:
        - 'The job identifier of the parent job, if any.'
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
    from azure.mgmt.iot import iotHubClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMIotHubResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            ),
            event_hub_endpoint_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            job_id=dict(
                type='str'
            ),
            iot_hub_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.event_hub_endpoint_name = None
        self.name = None
        self.job_id = None
        self.iot_hub_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMIotHubResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(iotHubClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

        if (self.resource_group_name is not None and
            self.resource_name is not None and
            self.event_hub_endpoint_name is not None and
            self.name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.geteventhubconsumergroup())
        elif (self.resource_group_name is not None and
              self.resource_name is not None and
              self.event_hub_endpoint_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.listeventhubconsumergroup())
        elif (self.resource_group_name is not None and
              self.resource_name is not None and
              self.job_id is not None):
            self.results['iot_hub_resource'] = self.format_item(self.getjob())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.getstat())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.getvalidsku())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.listjob())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.getquotametric())
        elif (self.resource_group_name is not None and
              self.iot_hub_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.getendpointhealth())
        elif (self.resource_group_name is not None):
            self.results['iot_hub_resource'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['iot_hub_resource'] = self.format_item(self.listbysubscription())
        return self.results

    def geteventhubconsumergroup(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get_event_hub_consumer_group(resource_group_name=self.resource_group_name,
                                                                                      resource_name=self.resource_name,
                                                                                      event_hub_endpoint_name=self.event_hub_endpoint_name,
                                                                                      name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listeventhubconsumergroup(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.list_event_hub_consumer_group(resource_group_name=self.resource_group_name,
                                                                                       resource_name=self.resource_name,
                                                                                       event_hub_endpoint_name=self.event_hub_endpoint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getjob(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get_job(resource_group_name=self.resource_group_name,
                                                                 resource_name=self.resource_name,
                                                                 job_id=self.job_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get(resource_group_name=self.resource_group_name,
                                                             resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getstat(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get_stat(resource_group_name=self.resource_group_name,
                                                                  resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getvalidsku(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get_valid_sku(resource_group_name=self.resource_group_name,
                                                                       resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listjob(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.list_job(resource_group_name=self.resource_group_name,
                                                                  resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getquotametric(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get_quota_metric(resource_group_name=self.resource_group_name,
                                                                          resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getendpointhealth(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.get_endpoint_health(resource_group_name=self.resource_group_name,
                                                                             iot_hub_name=self.iot_hub_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.iot_hub_resource.list_by_subscription()
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
    AzureRMIotHubResourceInfo()


if __name__ == '__main__':
    main()
