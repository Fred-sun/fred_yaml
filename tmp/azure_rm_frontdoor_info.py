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
module: azure_rm_frontdoor_info
version_added: '2.9'
short_description: Get FrontDoor info.
description:
  - Get info of FrontDoor.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all Front Doors
      azure_rm_frontdoor_info: 
        {}
        

    - name: List Front Doors in a Resource Group
      azure_rm_frontdoor_info: 
        resource_group_name: rg1
        

    - name: Get Front Door
      azure_rm_frontdoor_info: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        

'''

RETURN = '''
front_doors:
  description: >-
    A list of dict results where the key is the name of the FrontDoor and the
    values are the facts for that FrontDoor.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Front Doors within a resource group.
      returned: always
      type: list
      sample: null
      contains:
        friendly_name:
          description:
            - A friendly name for the frontDoor
          returned: always
          type: str
          sample: null
        routing_rules:
          description:
            - Routing rules associated with this Front Door.
          returned: always
          type: list
          sample: null
          contains:
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
            frontend_endpoints:
              description:
                - Frontend endpoints associated with this rule
              returned: always
              type: list
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            accepted_protocols:
              description:
                - Protocol schemes to match for this rule
              returned: always
              type: list
              sample: null
            patterns_to_match:
              description:
                - The route patterns of the rule.
              returned: always
              type: list
              sample: null
            enabled_state:
              description:
                - >-
                  Whether to enable use of this rule. Permitted values are
                  'Enabled' or 'Disabled'
              returned: always
              type: str
              sample: null
            route_configuration:
              description:
                - A reference to the routing configuration.
              returned: always
              type: dict
              sample: null
              contains:
                odata_type:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
            rules_engine:
              description:
                - >-
                  A reference to a specific Rules Engine Configuration to apply
                  to this route.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            web_application_firewall_policy_link:
              description:
                - >-
                  Defines the Web Application Firewall policy for each routing
                  rule (if applicable)
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        load_balancing_settings:
          description:
            - Load balancing settings associated with this Front Door instance.
          returned: always
          type: list
          sample: null
          contains:
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
            sample_size:
              description:
                - The number of samples to consider for load balancing decisions
              returned: always
              type: integer
              sample: null
            successful_samples_required:
              description:
                - >-
                  The number of samples within the sample period that must
                  succeed
              returned: always
              type: integer
              sample: null
            additional_latency_milliseconds:
              description:
                - >-
                  The additional latency in milliseconds for probes to fall into
                  the lowest latency bucket
              returned: always
              type: integer
              sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        health_probe_settings:
          description:
            - Health probe settings associated with this Front Door instance.
          returned: always
          type: list
          sample: null
          contains:
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
            path:
              description:
                - The path to use for the health probe. Default is /
              returned: always
              type: str
              sample: null
            protocol:
              description:
                - Protocol scheme to use for this probe
              returned: always
              type: str
              sample: null
            interval_in_seconds:
              description:
                - The number of seconds between health probes.
              returned: always
              type: integer
              sample: null
            health_probe_method:
              description:
                - >-
                  Configures which HTTP method to use to probe the backends
                  defined under backendPools.
              returned: always
              type: str
              sample: null
            enabled_state:
              description:
                - >-
                  Whether to enable health probes to be made against backends
                  defined under backendPools. Health probes can only be disabled
                  if there is a single enabled backend in single enabled backend
                  pool.
              returned: always
              type: str
              sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        backend_pools:
          description:
            - Backend pools available to routing rules.
          returned: always
          type: list
          sample: null
          contains:
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
            backends:
              description:
                - The set of backends for this pool
              returned: always
              type: list
              sample: null
              contains:
                address:
                  description:
                    - Location of the backend (IP address or FQDN)
                  returned: always
                  type: str
                  sample: null
                private_link_alias:
                  description:
                    - >-
                      The Alias of the Private Link resource. Populating this
                      optional field indicates that this backend is 'Private'
                  returned: always
                  type: str
                  sample: null
                private_link_resource_id:
                  description:
                    - >-
                      The Resource Id of the Private Link resource. Populating
                      this optional field indicates that this backend is
                      'Private'
                  returned: always
                  type: str
                  sample: null
                private_link_location:
                  description:
                    - >-
                      The location of the Private Link resource. Required only
                      if 'privateLinkResourceId' is populated
                  returned: always
                  type: str
                  sample: null
                private_endpoint_status:
                  description:
                    - The Approval status for the connection to the Private Link
                  returned: always
                  type: str
                  sample: null
                private_link_approval_message:
                  description:
                    - >-
                      A custom message to be included in the approval request to
                      connect to the Private Link
                  returned: always
                  type: str
                  sample: null
                http_port:
                  description:
                    - The HTTP TCP port number. Must be between 1 and 65535.
                  returned: always
                  type: integer
                  sample: null
                https_port:
                  description:
                    - The HTTPS TCP port number. Must be between 1 and 65535.
                  returned: always
                  type: integer
                  sample: null
                enabled_state:
                  description:
                    - >-
                      Whether to enable use of this backend. Permitted values
                      are 'Enabled' or 'Disabled'
                  returned: always
                  type: str
                  sample: null
                priority:
                  description:
                    - >-
                      Priority to use for load balancing. Higher priorities will
                      not be used for load balancing if any lower priority
                      backend is healthy.
                  returned: always
                  type: integer
                  sample: null
                weight:
                  description:
                    - Weight of this endpoint for load balancing purposes.
                  returned: always
                  type: integer
                  sample: null
                backend_host_header:
                  description:
                    - >-
                      The value to use as the host header sent to the backend.
                      If blank or unspecified, this defaults to the incoming
                      host.
                  returned: always
                  type: str
                  sample: null
            load_balancing_settings:
              description:
                - Load balancing settings for a backend pool
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            health_probe_settings:
              description:
                - L7 health probe settings for a backend pool
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        frontend_endpoints:
          description:
            - Frontend endpoints available to routing rules.
          returned: always
          type: list
          sample: null
          contains:
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
            host_name:
              description:
                - The host name of the frontendEndpoint. Must be a domain name.
              returned: always
              type: str
              sample: null
            session_affinity_enabled_state:
              description:
                - >-
                  Whether to allow session affinity on this host. Valid options
                  are 'Enabled' or 'Disabled'
              returned: always
              type: str
              sample: null
            session_affinity_ttl_seconds:
              description:
                - >-
                  UNUSED. This field will be ignored. The TTL to use in seconds
                  for session affinity, if applicable.
              returned: always
              type: integer
              sample: null
            id_properties_web_application_firewall_policy_link_id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
            custom_https_provisioning_state:
              description:
                - Provisioning status of Custom Https of the frontendEndpoint.
              returned: always
              type: str
              sample: null
            custom_https_provisioning_substate:
              description:
                - >-
                  Provisioning substate shows the progress of custom HTTPS
                  enabling/disabling process step by step.
              returned: always
              type: str
              sample: null
            custom_https_configuration:
              description:
                - The configuration specifying how to enable HTTPS
              returned: always
              type: dict
              sample: null
              contains:
                certificate_source:
                  description:
                    - Defines the source of the SSL certificate
                  returned: always
                  type: str
                  sample: null
                protocol_type:
                  description:
                    - >-
                      Defines the TLS extension protocol that is used for secure
                      delivery
                  returned: always
                  type: str
                  sample: null
                minimum_tls_version:
                  description:
                    - >-
                      The minimum TLS version required from the clients to
                      establish an SSL handshake with Front Door.
                  returned: always
                  type: str
                  sample: null
                certificate_type:
                  description:
                    - >-
                      Defines the type of the certificate used for secure
                      connections to a frontendEndpoint
                  returned: always
                  type: str
                  sample: null
                vault:
                  description:
                    - The Key Vault containing the SSL certificate
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    id:
                      description:
                        - Resource ID.
                      returned: always
                      type: str
                      sample: null
                secret_name:
                  description:
                    - >-
                      The name of the Key Vault secret representing the full
                      certificate PFX
                  returned: always
                  type: str
                  sample: null
                secret_version:
                  description:
                    - >-
                      The version of the Key Vault secret representing the full
                      certificate PFX
                  returned: always
                  type: str
                  sample: null
        backend_pools_settings:
          description:
            - Settings for all backendPools
          returned: always
          type: dict
          sample: null
          contains:
            enforce_certificate_name_check:
              description:
                - >-
                  Whether to enforce certificate name check on HTTPS requests to
                  all backend pools. No effect on non-HTTPS requests.
              returned: always
              type: str
              sample: null
            send_recv_timeout_seconds:
              description:
                - >-
                  Send and receive timeout on forwarding request to the backend.
                  When timeout is reached, the request fails and returns.
              returned: always
              type: integer
              sample: null
        enabled_state:
          description:
            - >-
              Operational status of the Front Door load balancer. Permitted
              values are 'Enabled' or 'Disabled'
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - Resource status of the Front Door.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Provisioning state of the Front Door.
          returned: always
          type: str
          sample: null
        cname:
          description:
            - The host that each frontendEndpoint must CNAME to.
          returned: always
          type: str
          sample: null
        frontdoor_id:
          description:
            - The Id of the frontdoor.
          returned: always
          type: str
          sample: null
        rules_engines:
          description:
            - Rules Engine Configurations available to routing rules.
          returned: always
          type: list
          sample: null
          contains:
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
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
            rules:
              description:
                - >-
                  A list of rules that define a particular Rules Engine
                  Configuration.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - A name to refer to this specific rule.
                  returned: always
                  type: str
                  sample: null
                priority:
                  description:
                    - 'A priority assigned to this rule. '
                  returned: always
                  type: integer
                  sample: null
                action:
                  description:
                    - >-
                      Actions to perform on the request and response if all of
                      the match conditions are met.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    request_header_actions:
                      description:
                        - >-
                          A list of header actions to apply from the request
                          from AFD to the origin.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        header_action_type:
                          description:
                            - Which type of manipulation to apply to the header.
                          returned: always
                          type: str
                          sample: null
                        header_name:
                          description:
                            - The name of the header this action will apply to.
                          returned: always
                          type: str
                          sample: null
                        value:
                          description:
                            - >-
                              The value to update the given header name with.
                              This value is not used if the actionType is
                              Delete.
                          returned: always
                          type: str
                          sample: null
                    response_header_actions:
                      description:
                        - >-
                          A list of header actions to apply from the response
                          from AFD to the client.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        header_action_type:
                          description:
                            - Which type of manipulation to apply to the header.
                          returned: always
                          type: str
                          sample: null
                        header_name:
                          description:
                            - The name of the header this action will apply to.
                          returned: always
                          type: str
                          sample: null
                        value:
                          description:
                            - >-
                              The value to update the given header name with.
                              This value is not used if the actionType is
                              Delete.
                          returned: always
                          type: str
                          sample: null
                    route_configuration_override:
                      description:
                        - Override the route configuration.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        odata_type:
                          description:
                            - ''
                          returned: always
                          type: str
                          sample: null
                match_conditions:
                  description:
                    - >-
                      A list of match conditions that must meet in order for the
                      actions of this rule to run. Having no match conditions
                      means the actions will always run.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    rules_engine_match_variable:
                      description:
                        - Match Variable
                      returned: always
                      type: str
                      sample: null
                    selector:
                      description:
                        - >-
                          Name of selector in RequestHeader or RequestBody to be
                          matched
                      returned: always
                      type: str
                      sample: null
                    rules_engine_operator:
                      description:
                        - Describes operator to apply to the match condition.
                      returned: always
                      type: str
                      sample: null
                    negate_condition:
                      description:
                        - Describes if this is negate condition or not
                      returned: always
                      type: bool
                      sample: null
                    rules_engine_match_value:
                      description:
                        - >-
                          Match values to match against. The operator will apply
                          to each value in here with OR semantics. If any of
                          them match the variable with the given operator this
                          match condition is considered a match.
                      returned: always
                      type: list
                      sample: null
                    transforms:
                      description:
                        - List of transforms
                      returned: always
                      type: list
                      sample: null
                match_processing_behavior:
                  description:
                    - >-
                      If this rule is a match should the rules engine continue
                      running the remaining rules or stop. If not present,
                      defaults to Continue.
                  returned: always
                  type: str
                  sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - URL to get the next set of Front Door objects if there are any.
      returned: always
      type: str
      sample: null
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
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    friendly_name:
      description:
        - A friendly name for the frontDoor
      returned: always
      type: str
      sample: null
    routing_rules:
      description:
        - Routing rules associated with this Front Door.
      returned: always
      type: list
      sample: null
      contains:
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
        frontend_endpoints:
          description:
            - Frontend endpoints associated with this rule
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        accepted_protocols:
          description:
            - Protocol schemes to match for this rule
          returned: always
          type: list
          sample: null
        patterns_to_match:
          description:
            - The route patterns of the rule.
          returned: always
          type: list
          sample: null
        enabled_state:
          description:
            - >-
              Whether to enable use of this rule. Permitted values are 'Enabled'
              or 'Disabled'
          returned: always
          type: str
          sample: null
        route_configuration:
          description:
            - A reference to the routing configuration.
          returned: always
          type: dict
          sample: null
          contains:
            odata_type:
              description:
                - ''
              returned: always
              type: str
              sample: null
        rules_engine:
          description:
            - >-
              A reference to a specific Rules Engine Configuration to apply to
              this route.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        web_application_firewall_policy_link:
          description:
            - >-
              Defines the Web Application Firewall policy for each routing rule
              (if applicable)
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
    load_balancing_settings:
      description:
        - Load balancing settings associated with this Front Door instance.
      returned: always
      type: list
      sample: null
      contains:
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
        sample_size:
          description:
            - The number of samples to consider for load balancing decisions
          returned: always
          type: integer
          sample: null
        successful_samples_required:
          description:
            - The number of samples within the sample period that must succeed
          returned: always
          type: integer
          sample: null
        additional_latency_milliseconds:
          description:
            - >-
              The additional latency in milliseconds for probes to fall into the
              lowest latency bucket
          returned: always
          type: integer
          sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
    health_probe_settings:
      description:
        - Health probe settings associated with this Front Door instance.
      returned: always
      type: list
      sample: null
      contains:
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
        path:
          description:
            - The path to use for the health probe. Default is /
          returned: always
          type: str
          sample: null
        protocol:
          description:
            - Protocol scheme to use for this probe
          returned: always
          type: str
          sample: null
        interval_in_seconds:
          description:
            - The number of seconds between health probes.
          returned: always
          type: integer
          sample: null
        health_probe_method:
          description:
            - >-
              Configures which HTTP method to use to probe the backends defined
              under backendPools.
          returned: always
          type: str
          sample: null
        enabled_state:
          description:
            - >-
              Whether to enable health probes to be made against backends
              defined under backendPools. Health probes can only be disabled if
              there is a single enabled backend in single enabled backend pool.
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
    backend_pools:
      description:
        - Backend pools available to routing rules.
      returned: always
      type: list
      sample: null
      contains:
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
        backends:
          description:
            - The set of backends for this pool
          returned: always
          type: list
          sample: null
          contains:
            address:
              description:
                - Location of the backend (IP address or FQDN)
              returned: always
              type: str
              sample: null
            private_link_alias:
              description:
                - >-
                  The Alias of the Private Link resource. Populating this
                  optional field indicates that this backend is 'Private'
              returned: always
              type: str
              sample: null
            private_link_resource_id:
              description:
                - >-
                  The Resource Id of the Private Link resource. Populating this
                  optional field indicates that this backend is 'Private'
              returned: always
              type: str
              sample: null
            private_link_location:
              description:
                - >-
                  The location of the Private Link resource. Required only if
                  'privateLinkResourceId' is populated
              returned: always
              type: str
              sample: null
            private_endpoint_status:
              description:
                - The Approval status for the connection to the Private Link
              returned: always
              type: str
              sample: null
            private_link_approval_message:
              description:
                - >-
                  A custom message to be included in the approval request to
                  connect to the Private Link
              returned: always
              type: str
              sample: null
            http_port:
              description:
                - The HTTP TCP port number. Must be between 1 and 65535.
              returned: always
              type: integer
              sample: null
            https_port:
              description:
                - The HTTPS TCP port number. Must be between 1 and 65535.
              returned: always
              type: integer
              sample: null
            enabled_state:
              description:
                - >-
                  Whether to enable use of this backend. Permitted values are
                  'Enabled' or 'Disabled'
              returned: always
              type: str
              sample: null
            priority:
              description:
                - >-
                  Priority to use for load balancing. Higher priorities will not
                  be used for load balancing if any lower priority backend is
                  healthy.
              returned: always
              type: integer
              sample: null
            weight:
              description:
                - Weight of this endpoint for load balancing purposes.
              returned: always
              type: integer
              sample: null
            backend_host_header:
              description:
                - >-
                  The value to use as the host header sent to the backend. If
                  blank or unspecified, this defaults to the incoming host.
              returned: always
              type: str
              sample: null
        load_balancing_settings:
          description:
            - Load balancing settings for a backend pool
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        health_probe_settings:
          description:
            - L7 health probe settings for a backend pool
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
    frontend_endpoints:
      description:
        - Frontend endpoints available to routing rules.
      returned: always
      type: list
      sample: null
      contains:
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
        host_name:
          description:
            - The host name of the frontendEndpoint. Must be a domain name.
          returned: always
          type: str
          sample: null
        session_affinity_enabled_state:
          description:
            - >-
              Whether to allow session affinity on this host. Valid options are
              'Enabled' or 'Disabled'
          returned: always
          type: str
          sample: null
        session_affinity_ttl_seconds:
          description:
            - >-
              UNUSED. This field will be ignored. The TTL to use in seconds for
              session affinity, if applicable.
          returned: always
          type: integer
          sample: null
        id_properties_web_application_firewall_policy_link_id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
        custom_https_provisioning_state:
          description:
            - Provisioning status of Custom Https of the frontendEndpoint.
          returned: always
          type: str
          sample: null
        custom_https_provisioning_substate:
          description:
            - >-
              Provisioning substate shows the progress of custom HTTPS
              enabling/disabling process step by step.
          returned: always
          type: str
          sample: null
        custom_https_configuration:
          description:
            - The configuration specifying how to enable HTTPS
          returned: always
          type: dict
          sample: null
          contains:
            certificate_source:
              description:
                - Defines the source of the SSL certificate
              returned: always
              type: str
              sample: null
            protocol_type:
              description:
                - >-
                  Defines the TLS extension protocol that is used for secure
                  delivery
              returned: always
              type: str
              sample: null
            minimum_tls_version:
              description:
                - >-
                  The minimum TLS version required from the clients to establish
                  an SSL handshake with Front Door.
              returned: always
              type: str
              sample: null
            certificate_type:
              description:
                - >-
                  Defines the type of the certificate used for secure
                  connections to a frontendEndpoint
              returned: always
              type: str
              sample: null
            vault:
              description:
                - The Key Vault containing the SSL certificate
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            secret_name:
              description:
                - >-
                  The name of the Key Vault secret representing the full
                  certificate PFX
              returned: always
              type: str
              sample: null
            secret_version:
              description:
                - >-
                  The version of the Key Vault secret representing the full
                  certificate PFX
              returned: always
              type: str
              sample: null
    backend_pools_settings:
      description:
        - Settings for all backendPools
      returned: always
      type: dict
      sample: null
      contains:
        enforce_certificate_name_check:
          description:
            - >-
              Whether to enforce certificate name check on HTTPS requests to all
              backend pools. No effect on non-HTTPS requests.
          returned: always
          type: str
          sample: null
        send_recv_timeout_seconds:
          description:
            - >-
              Send and receive timeout on forwarding request to the backend.
              When timeout is reached, the request fails and returns.
          returned: always
          type: integer
          sample: null
    enabled_state:
      description:
        - >-
          Operational status of the Front Door load balancer. Permitted values
          are 'Enabled' or 'Disabled'
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status of the Front Door.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the Front Door.
      returned: always
      type: str
      sample: null
    cname:
      description:
        - The host that each frontendEndpoint must CNAME to.
      returned: always
      type: str
      sample: null
    frontdoor_id:
      description:
        - The Id of the frontdoor.
      returned: always
      type: str
      sample: null
    rules_engines:
      description:
        - Rules Engine Configurations available to routing rules.
      returned: always
      type: list
      sample: null
      contains:
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
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        rules:
          description:
            - >-
              A list of rules that define a particular Rules Engine
              Configuration.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - A name to refer to this specific rule.
              returned: always
              type: str
              sample: null
            priority:
              description:
                - 'A priority assigned to this rule. '
              returned: always
              type: integer
              sample: null
            action:
              description:
                - >-
                  Actions to perform on the request and response if all of the
                  match conditions are met.
              returned: always
              type: dict
              sample: null
              contains:
                request_header_actions:
                  description:
                    - >-
                      A list of header actions to apply from the request from
                      AFD to the origin.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    header_action_type:
                      description:
                        - Which type of manipulation to apply to the header.
                      returned: always
                      type: str
                      sample: null
                    header_name:
                      description:
                        - The name of the header this action will apply to.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - >-
                          The value to update the given header name with. This
                          value is not used if the actionType is Delete.
                      returned: always
                      type: str
                      sample: null
                response_header_actions:
                  description:
                    - >-
                      A list of header actions to apply from the response from
                      AFD to the client.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    header_action_type:
                      description:
                        - Which type of manipulation to apply to the header.
                      returned: always
                      type: str
                      sample: null
                    header_name:
                      description:
                        - The name of the header this action will apply to.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - >-
                          The value to update the given header name with. This
                          value is not used if the actionType is Delete.
                      returned: always
                      type: str
                      sample: null
                route_configuration_override:
                  description:
                    - Override the route configuration.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    odata_type:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
            match_conditions:
              description:
                - >-
                  A list of match conditions that must meet in order for the
                  actions of this rule to run. Having no match conditions means
                  the actions will always run.
              returned: always
              type: list
              sample: null
              contains:
                rules_engine_match_variable:
                  description:
                    - Match Variable
                  returned: always
                  type: str
                  sample: null
                selector:
                  description:
                    - >-
                      Name of selector in RequestHeader or RequestBody to be
                      matched
                  returned: always
                  type: str
                  sample: null
                rules_engine_operator:
                  description:
                    - Describes operator to apply to the match condition.
                  returned: always
                  type: str
                  sample: null
                negate_condition:
                  description:
                    - Describes if this is negate condition or not
                  returned: always
                  type: bool
                  sample: null
                rules_engine_match_value:
                  description:
                    - >-
                      Match values to match against. The operator will apply to
                      each value in here with OR semantics. If any of them match
                      the variable with the given operator this match condition
                      is considered a match.
                  returned: always
                  type: list
                  sample: null
                transforms:
                  description:
                    - List of transforms
                  returned: always
                  type: list
                  sample: null
            match_processing_behavior:
              description:
                - >-
                  If this rule is a match should the rules engine continue
                  running the remaining rules or stop. If not present, defaults
                  to Continue.
              returned: always
              type: str
              sample: null
        resource_state:
          description:
            - Resource status.
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMFrontDoorInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            front_door_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.front_door_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMFrontDoorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.front_door_name is not None):
            self.results['front_doors'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['front_doors'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['front_doors'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.front_doors.get(resource_group_name=self.resource_group_name,
                                                        front_door_name=self.front_door_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.front_doors.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.front_doors.list()
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
    AzureRMFrontDoorInfo()


if __name__ == '__main__':
    main()
