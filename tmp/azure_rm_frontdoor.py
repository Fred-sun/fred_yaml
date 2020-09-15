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
module: azure_rm_frontdoor
version_added: '2.9'
short_description: Manage Azure FrontDoor instance.
description:
  - 'Create, update and delete instance of Azure FrontDoor.'
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  friendly_name:
    description:
      - A friendly name for the frontDoor
    type: str
  routing_rules:
    description:
      - Routing rules associated with this Front Door.
    type: list
    suboptions:
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
      frontend_endpoints:
        description:
          - Frontend endpoints associated with this rule
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      accepted_protocols:
        description:
          - Protocol schemes to match for this rule
        type: list
      patterns_to_match:
        description:
          - The route patterns of the rule.
        type: list
      enabled_state:
        description:
          - >-
            Whether to enable use of this rule. Permitted values are 'Enabled'
            or 'Disabled'
        type: str
        choices:
          - Enabled
          - Disabled
      route_configuration:
        description:
          - A reference to the routing configuration.
        type: dict
        suboptions:
          odata_type:
            description:
              - undefined
            required: true
            type: str
      rules_engine:
        description:
          - >-
            A reference to a specific Rules Engine Configuration to apply to
            this route.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      web_application_firewall_policy_link:
        description:
          - >-
            Defines the Web Application Firewall policy for each routing rule
            (if applicable)
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      resource_state:
        description:
          - Resource status.
        type: str
        choices:
          - Creating
          - Enabling
          - Enabled
          - Disabling
          - Disabled
          - Deleting
  load_balancing_settings:
    description:
      - Load balancing settings associated with this Front Door instance.
    type: list
    suboptions:
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
      sample_size:
        description:
          - The number of samples to consider for load balancing decisions
        type: integer
      successful_samples_required:
        description:
          - The number of samples within the sample period that must succeed
        type: integer
      additional_latency_milliseconds:
        description:
          - >-
            The additional latency in milliseconds for probes to fall into the
            lowest latency bucket
        type: integer
      resource_state:
        description:
          - Resource status.
        type: str
        choices:
          - Creating
          - Enabling
          - Enabled
          - Disabling
          - Disabled
          - Deleting
  health_probe_settings:
    description:
      - Health probe settings associated with this Front Door instance.
    type: list
    suboptions:
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
      path:
        description:
          - The path to use for the health probe. Default is /
        type: str
      protocol:
        description:
          - Protocol scheme to use for this probe
        type: str
        choices:
          - Http
          - Https
      interval_in_seconds:
        description:
          - The number of seconds between health probes.
        type: integer
      health_probe_method:
        description:
          - >-
            Configures which HTTP method to use to probe the backends defined
            under backendPools.
        type: str
        choices:
          - GET
          - HEAD
      enabled_state:
        description:
          - >-
            Whether to enable health probes to be made against backends defined
            under backendPools. Health probes can only be disabled if there is a
            single enabled backend in single enabled backend pool.
        type: str
        choices:
          - Enabled
          - Disabled
      resource_state:
        description:
          - Resource status.
        type: str
        choices:
          - Creating
          - Enabling
          - Enabled
          - Disabling
          - Disabled
          - Deleting
  backend_pools:
    description:
      - Backend pools available to routing rules.
    type: list
    suboptions:
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
      backends:
        description:
          - The set of backends for this pool
        type: list
        suboptions:
          address:
            description:
              - Location of the backend (IP address or FQDN)
            type: str
          private_link_alias:
            description:
              - >-
                The Alias of the Private Link resource. Populating this optional
                field indicates that this backend is 'Private'
            type: str
          private_link_resource_id:
            description:
              - >-
                The Resource Id of the Private Link resource. Populating this
                optional field indicates that this backend is 'Private'
            type: str
          private_link_location:
            description:
              - >-
                The location of the Private Link resource. Required only if
                'privateLinkResourceId' is populated
            type: str
          private_endpoint_status:
            description:
              - The Approval status for the connection to the Private Link
            type: str
            choices:
              - Pending
              - Approved
              - Rejected
              - Disconnected
              - Timeout
          private_link_approval_message:
            description:
              - >-
                A custom message to be included in the approval request to
                connect to the Private Link
            type: str
          http_port:
            description:
              - The HTTP TCP port number. Must be between 1 and 65535.
            type: integer
          https_port:
            description:
              - The HTTPS TCP port number. Must be between 1 and 65535.
            type: integer
          enabled_state:
            description:
              - >-
                Whether to enable use of this backend. Permitted values are
                'Enabled' or 'Disabled'
            type: str
            choices:
              - Enabled
              - Disabled
          priority:
            description:
              - >-
                Priority to use for load balancing. Higher priorities will not
                be used for load balancing if any lower priority backend is
                healthy.
            type: integer
          weight:
            description:
              - Weight of this endpoint for load balancing purposes.
            type: integer
          backend_host_header:
            description:
              - >-
                The value to use as the host header sent to the backend. If
                blank or unspecified, this defaults to the incoming host.
            type: str
      load_balancing_settings:
        description:
          - Load balancing settings for a backend pool
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      health_probe_settings:
        description:
          - L7 health probe settings for a backend pool
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      resource_state:
        description:
          - Resource status.
        type: str
        choices:
          - Creating
          - Enabling
          - Enabled
          - Disabling
          - Disabled
          - Deleting
  frontend_endpoints:
    description:
      - Frontend endpoints available to routing rules.
    type: list
    suboptions:
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
      host_name:
        description:
          - The host name of the frontendEndpoint. Must be a domain name.
        type: str
      session_affinity_enabled_state:
        description:
          - >-
            Whether to allow session affinity on this host. Valid options are
            'Enabled' or 'Disabled'
        type: str
        choices:
          - Enabled
          - Disabled
      session_affinity_ttl_seconds:
        description:
          - >-
            UNUSED. This field will be ignored. The TTL to use in seconds for
            session affinity, if applicable.
        type: integer
      id_properties_web_application_firewall_policy_link_id:
        description:
          - Resource ID.
        type: str
      resource_state:
        description:
          - Resource status.
        type: str
        choices:
          - Creating
          - Enabling
          - Enabled
          - Disabling
          - Disabled
          - Deleting
      custom_https_provisioning_state:
        description:
          - Provisioning status of Custom Https of the frontendEndpoint.
        type: str
        choices:
          - Enabling
          - Enabled
          - Disabling
          - Disabled
          - Failed
      custom_https_provisioning_substate:
        description:
          - >-
            Provisioning substate shows the progress of custom HTTPS
            enabling/disabling process step by step.
        type: str
        choices:
          - SubmittingDomainControlValidationRequest
          - PendingDomainControlValidationREquestApproval
          - DomainControlValidationRequestApproved
          - DomainControlValidationRequestRejected
          - DomainControlValidationRequestTimedOut
          - IssuingCertificate
          - DeployingCertificate
          - CertificateDeployed
          - DeletingCertificate
          - CertificateDeleted
      custom_https_configuration:
        description:
          - The configuration specifying how to enable HTTPS
        type: dict
        suboptions:
          certificate_source:
            description:
              - Defines the source of the SSL certificate
            required: true
            type: str
            choices:
              - AzureKeyVault
              - FrontDoor
          protocol_type:
            description:
              - >-
                Defines the TLS extension protocol that is used for secure
                delivery
            required: true
            type: str
            choices:
              - ServerNameIndication
          minimum_tls_version:
            description:
              - >-
                The minimum TLS version required from the clients to establish
                an SSL handshake with Front Door.
            required: true
            type: str
            choices:
              - '1.0'
              - '1.2'
          certificate_type:
            description:
              - >-
                Defines the type of the certificate used for secure connections
                to a frontendEndpoint
            type: str
            choices:
              - Dedicated
          vault:
            description:
              - The Key Vault containing the SSL certificate
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          secret_name:
            description:
              - >-
                The name of the Key Vault secret representing the full
                certificate PFX
            type: str
          secret_version:
            description:
              - >-
                The version of the Key Vault secret representing the full
                certificate PFX
            type: str
  backend_pools_settings:
    description:
      - Settings for all backendPools
    type: dict
    suboptions:
      enforce_certificate_name_check:
        description:
          - >-
            Whether to enforce certificate name check on HTTPS requests to all
            backend pools. No effect on non-HTTPS requests.
        type: str
        choices:
          - Enabled
          - Disabled
      send_recv_timeout_seconds:
        description:
          - >-
            Send and receive timeout on forwarding request to the backend. When
            timeout is reached, the request fails and returns.
        type: integer
  enabled_state:
    description:
      - >-
        Operational status of the Front Door load balancer. Permitted values are
        'Enabled' or 'Disabled'
    type: str
    choices:
      - Enabled
      - Disabled
  state:
    description:
      - Assert the state of the FrontDoor.
      - >-
        Use C(present) to create or update an FrontDoor and C(absent) to delete
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
    - name: Create or update specific Front Door
      azure_rm_frontdoor: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        

    - name: Delete Front Door
      azure_rm_frontdoor: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        

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
          Whether to enable use of this rule. Permitted values are 'Enabled' or
          'Disabled'
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
          A reference to a specific Rules Engine Configuration to apply to this
          route.
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
          Defines the Web Application Firewall policy for each routing rule (if
          applicable)
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
          Whether to enable health probes to be made against backends defined
          under backendPools. Health probes can only be disabled if there is a
          single enabled backend in single enabled backend pool.
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
              The Alias of the Private Link resource. Populating this optional
              field indicates that this backend is 'Private'
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
              A custom message to be included in the approval request to connect
              to the Private Link
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
              Priority to use for load balancing. Higher priorities will not be
              used for load balancing if any lower priority backend is healthy.
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
              The value to use as the host header sent to the backend. If blank
              or unspecified, this defaults to the incoming host.
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
              The minimum TLS version required from the clients to establish an
              SSL handshake with Front Door.
          returned: always
          type: str
          sample: null
        certificate_type:
          description:
            - >-
              Defines the type of the certificate used for secure connections to
              a frontendEndpoint
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
              The name of the Key Vault secret representing the full certificate
              PFX
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
          Send and receive timeout on forwarding request to the backend. When
          timeout is reached, the request fails and returns.
      returned: always
      type: integer
      sample: null
enabled_state:
  description:
    - >-
      Operational status of the Front Door load balancer. Permitted values are
      'Enabled' or 'Disabled'
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
        - A list of rules that define a particular Rules Engine Configuration.
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
              Actions to perform on the request and response if all of the match
              conditions are met.
          returned: always
          type: dict
          sample: null
          contains:
            request_header_actions:
              description:
                - >-
                  A list of header actions to apply from the request from AFD to
                  the origin.
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
                      The value to update the given header name with. This value
                      is not used if the actionType is Delete.
                  returned: always
                  type: str
                  sample: null
            response_header_actions:
              description:
                - >-
                  A list of header actions to apply from the response from AFD
                  to the client.
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
                      The value to update the given header name with. This value
                      is not used if the actionType is Delete.
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
              A list of match conditions that must meet in order for the actions
              of this rule to run. Having no match conditions means the actions
              will always run.
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
                - Name of selector in RequestHeader or RequestBody to be matched
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
                  Match values to match against. The operator will apply to each
                  value in here with OR semantics. If any of them match the
                  variable with the given operator this match condition is
                  considered a match.
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
              If this rule is a match should the rules engine continue running
              the remaining rules or stop. If not present, defaults to Continue.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFrontDoor(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            front_door_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            friendly_name=dict(
                type='str',
                disposition='/friendly_name'
            ),
            routing_rules=dict(
                type='list',
                disposition='/routing_rules',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    frontend_endpoints=dict(
                        type='list',
                        disposition='frontend_endpoints',
                        elements='dict',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    accepted_protocols=dict(
                        type='list',
                        disposition='accepted_protocols',
                        elements='str'
                    ),
                    patterns_to_match=dict(
                        type='list',
                        disposition='patterns_to_match',
                        elements='str'
                    ),
                    enabled_state=dict(
                        type='str',
                        disposition='enabled_state',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    route_configuration=dict(
                        type='dict',
                        disposition='route_configuration',
                        options=dict(
                            odata_type=dict(
                                type='str',
                                disposition='odata_type',
                                required=True
                            )
                        )
                    ),
                    rules_engine=dict(
                        type='dict',
                        disposition='rules_engine',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    web_application_firewall_policy_link=dict(
                        type='dict',
                        disposition='web_application_firewall_policy_link',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    resource_state=dict(
                        type='str',
                        updatable=False,
                        disposition='resource_state',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    )
                )
            ),
            load_balancing_settings=dict(
                type='list',
                disposition='/load_balancing_settings',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    sample_size=dict(
                        type='integer',
                        disposition='sample_size'
                    ),
                    successful_samples_required=dict(
                        type='integer',
                        disposition='successful_samples_required'
                    ),
                    additional_latency_milliseconds=dict(
                        type='integer',
                        disposition='additional_latency_milliseconds'
                    ),
                    resource_state=dict(
                        type='str',
                        updatable=False,
                        disposition='resource_state',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    )
                )
            ),
            health_probe_settings=dict(
                type='list',
                disposition='/health_probe_settings',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    path=dict(
                        type='str',
                        disposition='path'
                    ),
                    protocol=dict(
                        type='str',
                        disposition='protocol',
                        choices=['Http',
                                 'Https']
                    ),
                    interval_in_seconds=dict(
                        type='integer',
                        disposition='interval_in_seconds'
                    ),
                    health_probe_method=dict(
                        type='str',
                        disposition='health_probe_method',
                        choices=['GET',
                                 'HEAD']
                    ),
                    enabled_state=dict(
                        type='str',
                        disposition='enabled_state',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    resource_state=dict(
                        type='str',
                        updatable=False,
                        disposition='resource_state',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    )
                )
            ),
            backend_pools=dict(
                type='list',
                disposition='/backend_pools',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    backends=dict(
                        type='list',
                        disposition='backends',
                        elements='dict',
                        options=dict(
                            address=dict(
                                type='str',
                                disposition='address'
                            ),
                            private_link_alias=dict(
                                type='str',
                                disposition='private_link_alias'
                            ),
                            private_link_resource_id=dict(
                                type='str',
                                disposition='private_link_resource_id'
                            ),
                            private_link_location=dict(
                                type='str',
                                disposition='private_link_location'
                            ),
                            private_endpoint_status=dict(
                                type='str',
                                updatable=False,
                                disposition='private_endpoint_status',
                                choices=['Pending',
                                         'Approved',
                                         'Rejected',
                                         'Disconnected',
                                         'Timeout']
                            ),
                            private_link_approval_message=dict(
                                type='str',
                                disposition='private_link_approval_message'
                            ),
                            http_port=dict(
                                type='integer',
                                disposition='http_port'
                            ),
                            https_port=dict(
                                type='integer',
                                disposition='https_port'
                            ),
                            enabled_state=dict(
                                type='str',
                                disposition='enabled_state',
                                choices=['Enabled',
                                         'Disabled']
                            ),
                            priority=dict(
                                type='integer',
                                disposition='priority'
                            ),
                            weight=dict(
                                type='integer',
                                disposition='weight'
                            ),
                            backend_host_header=dict(
                                type='str',
                                disposition='backend_host_header'
                            )
                        )
                    ),
                    load_balancing_settings=dict(
                        type='dict',
                        disposition='load_balancing_settings',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    health_probe_settings=dict(
                        type='dict',
                        disposition='health_probe_settings',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    resource_state=dict(
                        type='str',
                        updatable=False,
                        disposition='resource_state',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    )
                )
            ),
            frontend_endpoints=dict(
                type='list',
                disposition='/frontend_endpoints',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    host_name=dict(
                        type='str',
                        disposition='host_name'
                    ),
                    session_affinity_enabled_state=dict(
                        type='str',
                        disposition='session_affinity_enabled_state',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    session_affinity_ttl_seconds=dict(
                        type='integer',
                        disposition='session_affinity_ttl_seconds'
                    ),
                    id_properties_web_application_firewall_policy_link_id=dict(
                        type='str',
                        disposition='id_properties_web_application_firewall_policy_link_id'
                    ),
                    resource_state=dict(
                        type='str',
                        updatable=False,
                        disposition='resource_state',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    ),
                    custom_https_provisioning_state=dict(
                        type='str',
                        updatable=False,
                        disposition='custom_https_provisioning_state',
                        choices=['Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Failed']
                    ),
                    custom_https_provisioning_substate=dict(
                        type='str',
                        updatable=False,
                        disposition='custom_https_provisioning_substate',
                        choices=['SubmittingDomainControlValidationRequest',
                                 'PendingDomainControlValidationREquestApproval',
                                 'DomainControlValidationRequestApproved',
                                 'DomainControlValidationRequestRejected',
                                 'DomainControlValidationRequestTimedOut',
                                 'IssuingCertificate',
                                 'DeployingCertificate',
                                 'CertificateDeployed',
                                 'DeletingCertificate',
                                 'CertificateDeleted']
                    ),
                    custom_https_configuration=dict(
                        type='dict',
                        updatable=False,
                        disposition='custom_https_configuration',
                        options=dict(
                            certificate_source=dict(
                                type='str',
                                disposition='certificate_source',
                                choices=['AzureKeyVault',
                                         'FrontDoor'],
                                required=True
                            ),
                            protocol_type=dict(
                                type='str',
                                disposition='protocol_type',
                                choices=['ServerNameIndication'],
                                required=True
                            ),
                            minimum_tls_version=dict(
                                type='str',
                                disposition='minimum_tls_version',
                                choices=['1.0',
                                         '1.2'],
                                required=True
                            ),
                            certificate_type=dict(
                                type='str',
                                disposition='certificate_type',
                                choices=['Dedicated']
                            ),
                            vault=dict(
                                type='dict',
                                disposition='vault',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            secret_name=dict(
                                type='str',
                                disposition='secret_name'
                            ),
                            secret_version=dict(
                                type='str',
                                disposition='secret_version'
                            )
                        )
                    )
                )
            ),
            backend_pools_settings=dict(
                type='dict',
                disposition='/backend_pools_settings',
                options=dict(
                    enforce_certificate_name_check=dict(
                        type='str',
                        disposition='enforce_certificate_name_check',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    send_recv_timeout_seconds=dict(
                        type='integer',
                        disposition='send_recv_timeout_seconds'
                    )
                )
            ),
            enabled_state=dict(
                type='str',
                disposition='/enabled_state',
                choices=['Enabled',
                         'Disabled']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.front_door_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFrontDoor, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
            response = self.mgmt_client.front_doors.create_or_update(resource_group_name=self.resource_group_name,
                                                                     front_door_name=self.front_door_name,
                                                                     front_door_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FrontDoor instance.')
            self.fail('Error creating the FrontDoor instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.front_doors.delete(resource_group_name=self.resource_group_name,
                                                           front_door_name=self.front_door_name)
        except CloudError as e:
            self.log('Error attempting to delete the FrontDoor instance.')
            self.fail('Error deleting the FrontDoor instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.front_doors.get(resource_group_name=self.resource_group_name,
                                                        front_door_name=self.front_door_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFrontDoor()


if __name__ == '__main__':
    main()
