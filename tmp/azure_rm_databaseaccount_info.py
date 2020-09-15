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
module: azure_rm_databaseaccount_info
version_added: '2.9'
short_description: Get DatabaseAccount info.
description:
  - Get info of DatabaseAccount.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    type: str
  filter:
    description:
      - >-
        An OData filter expression that describes a subset of metrics to return.
        The parameters that can be filtered are name.value (name of the metric,
        can have an or of multiple names), startTime, endTime, and timeGrain.
        The supported operator is eq.
      - >-
        An OData filter expression that describes a subset of usages to return.
        The supported parameter is name.value (name of the metric, can have an
        or of multiple names).
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: CosmosDBDatabaseAccountGet
      azure_rm_databaseaccount_info: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountList
      azure_rm_databaseaccount_info: 
        {}
        

    - name: CosmosDBDatabaseAccountListByResourceGroup
      azure_rm_databaseaccount_info: 
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountListReadOnlyKeys
      azure_rm_databaseaccount_info: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountGetMetrics
      azure_rm_databaseaccount_info: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountGetUsages
      azure_rm_databaseaccount_info: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountGetMetricDefinitions
      azure_rm_databaseaccount_info: 
        account_name: ddb1
        resource_group_name: rg1
        

'''

RETURN = '''
database_accounts:
  description: >-
    A list of dict results where the key is the name of the DatabaseAccount and
    the values are the facts for that DatabaseAccount.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The unique resource identifier of the ARM resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the ARM resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of Azure resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The location of the resource group to which the resource belongs.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - >-
          Tags are a list of key-value pairs that describe the resource. These
          tags can be used in viewing and grouping this resource (across
          resource groups). A maximum of 15 tags can be provided for a resource.
          Each tag must have a key no greater than 128 characters and value no
          greater than 256 characters. For example, the default experience for a
          template type is set with "defaultExperience": "Cassandra". Current
          "defaultExperience" values also include "Table", "Graph",
          "DocumentDB", and "MongoDB".
      returned: always
      type: dictionary
      sample: null
    kind:
      description:
        - >-
          Indicates the type of database account. This can only be set at
          database account creation.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The status of the Cosmos DB account at the time the operation was
          called. The status can be one of following. 'Creating' – the Cosmos DB
          account is being created. When an account is in Creating state, only
          properties that are specified as input for the Create Cosmos DB
          account operation are returned. 'Succeeded' – the Cosmos DB account is
          active for use. 'Updating' – the Cosmos DB account is being updated.
          'Deleting' – the Cosmos DB account is being deleted. 'Failed' – the
          Cosmos DB account failed creation. 'DeletionFailed' – the Cosmos DB
          account deletion failed.
      returned: always
      type: str
      sample: null
    document_endpoint:
      description:
        - The connection endpoint for the Cosmos DB database account.
      returned: always
      type: str
      sample: null
    database_account_offer_type:
      description:
        - >-
          The offer type for the Cosmos DB database account. Default value:
          Standard.
      returned: always
      type: constant
      sample: null
    ip_rules:
      description:
        - List of IpRules.
      returned: always
      type: list
      sample: null
      contains:
        ip_address_or_range:
          description:
            - >-
              A single IPv4 address or a single IPv4 address range in CIDR
              format. Provided IPs must be well-formatted and cannot be
              contained in one of the following ranges: 10.0.0.0/8,
              100.64.0.0/10, 172.16.0.0/12, 192.168.0.0/16, since these are not
              enforceable by the IP address filter. Example of valid inputs:
              “23.40.210.245” or “23.40.210.0/8”.
          returned: always
          type: str
          sample: null
    is_virtual_network_filter_enabled:
      description:
        - Flag to indicate whether to enable/disable Virtual Network ACL rules.
      returned: always
      type: bool
      sample: null
    enable_automatic_failover:
      description:
        - >-
          Enables automatic failover of the write region in the rare event that
          the region is unavailable due to an outage. Automatic failover will
          result in a new write region for the account and is chosen based on
          the failover priorities configured for the account.
      returned: always
      type: bool
      sample: null
    consistency_policy:
      description:
        - The consistency policy for the Cosmos DB database account.
      returned: always
      type: dict
      sample: null
      contains:
        default_consistency_level:
          description:
            - >-
              The default consistency level and configuration settings of the
              Cosmos DB account.
          returned: always
          type: sealed-choice
          sample: null
        max_staleness_prefix:
          description:
            - >-
              When used with the Bounded Staleness consistency level, this value
              represents the number of stale requests tolerated. Accepted range
              for this value is 1 – 2,147,483,647. Required when
              defaultConsistencyPolicy is set to 'BoundedStaleness'.
          returned: always
          type: integer
          sample: null
        max_interval_in_seconds:
          description:
            - >-
              When used with the Bounded Staleness consistency level, this value
              represents the time amount of staleness (in seconds) tolerated.
              Accepted range for this value is 5 - 86400. Required when
              defaultConsistencyPolicy is set to 'BoundedStaleness'.
          returned: always
          type: integer
          sample: null
    capabilities:
      description:
        - List of Cosmos DB capabilities for the account
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              Name of the Cosmos DB capability. For example, "name":
              "EnableCassandra". Current values also include "EnableTable" and
              "EnableGremlin".
          returned: always
          type: str
          sample: null
    write_locations:
      description:
        - An array that contains the write location for the Cosmos DB account.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region within the database account.
              Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region.
          returned: always
          type: str
          sample: null
        document_endpoint:
          description:
            - >-
              The connection endpoint for the specific region. Example:
              https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The status of the Cosmos DB account at the time the operation was
              called. The status can be one of following. 'Creating' – the
              Cosmos DB account is being created. When an account is in Creating
              state, only properties that are specified as input for the Create
              Cosmos DB account operation are returned. 'Succeeded' – the Cosmos
              DB account is active for use. 'Updating' – the Cosmos DB account
              is being updated. 'Deleting' – the Cosmos DB account is being
              deleted. 'Failed' – the Cosmos DB account failed creation.
              'DeletionFailed' – the Cosmos DB account deletion failed.
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: integer
          sample: null
        is_zone_redundant:
          description:
            - >-
              Flag to indicate whether or not this region is an AvailabilityZone
              region
          returned: always
          type: bool
          sample: null
    read_locations:
      description:
        - >-
          An array that contains of the read locations enabled for the Cosmos DB
          account.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region within the database account.
              Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region.
          returned: always
          type: str
          sample: null
        document_endpoint:
          description:
            - >-
              The connection endpoint for the specific region. Example:
              https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The status of the Cosmos DB account at the time the operation was
              called. The status can be one of following. 'Creating' – the
              Cosmos DB account is being created. When an account is in Creating
              state, only properties that are specified as input for the Create
              Cosmos DB account operation are returned. 'Succeeded' – the Cosmos
              DB account is active for use. 'Updating' – the Cosmos DB account
              is being updated. 'Deleting' – the Cosmos DB account is being
              deleted. 'Failed' – the Cosmos DB account failed creation.
              'DeletionFailed' – the Cosmos DB account deletion failed.
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: integer
          sample: null
        is_zone_redundant:
          description:
            - >-
              Flag to indicate whether or not this region is an AvailabilityZone
              region
          returned: always
          type: bool
          sample: null
    locations:
      description:
        - >-
          An array that contains all of the locations enabled for the Cosmos DB
          account.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region within the database account.
              Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region.
          returned: always
          type: str
          sample: null
        document_endpoint:
          description:
            - >-
              The connection endpoint for the specific region. Example:
              https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The status of the Cosmos DB account at the time the operation was
              called. The status can be one of following. 'Creating' – the
              Cosmos DB account is being created. When an account is in Creating
              state, only properties that are specified as input for the Create
              Cosmos DB account operation are returned. 'Succeeded' – the Cosmos
              DB account is active for use. 'Updating' – the Cosmos DB account
              is being updated. 'Deleting' – the Cosmos DB account is being
              deleted. 'Failed' – the Cosmos DB account failed creation.
              'DeletionFailed' – the Cosmos DB account deletion failed.
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: integer
          sample: null
        is_zone_redundant:
          description:
            - >-
              Flag to indicate whether or not this region is an AvailabilityZone
              region
          returned: always
          type: bool
          sample: null
    failover_policies:
      description:
        - >-
          An array that contains the regions ordered by their failover
          priorities.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region in which the database account
              replicates to. Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region in which the database account exists.
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: integer
          sample: null
    virtual_network_rules:
      description:
        - >-
          List of Virtual Network ACL rules configured for the Cosmos DB
          account.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              Resource ID of a subnet, for example:
              /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
          returned: always
          type: str
          sample: null
        ignore_missing_vnet_service_endpoint:
          description:
            - >-
              Create firewall rule before the virtual network has vnet service
              endpoint enabled.
          returned: always
          type: bool
          sample: null
    private_endpoint_connections:
      description:
        - >-
          List of Private Endpoint Connections configured for the Cosmos DB
          account.
      returned: always
      type: list
      sample: null
      contains:
        private_endpoint:
          description:
            - Private endpoint which the connection belongs to.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource id of the private endpoint.
              returned: always
              type: str
              sample: null
        private_link_service_connection_state:
          description:
            - Connection State of the Private Endpoint Connection.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - The private link service connection status.
              returned: always
              type: str
              sample: null
            actions_required:
              description:
                - >-
                  Any action that is required beyond basic workflow (approve/
                  reject/ disconnect)
              returned: always
              type: str
              sample: null
    enable_multiple_write_locations:
      description:
        - Enables the account to write in multiple locations
      returned: always
      type: bool
      sample: null
    enable_cassandra_connector:
      description:
        - Enables the cassandra connector on the Cosmos DB C* account
      returned: always
      type: bool
      sample: null
    connector_offer:
      description:
        - >-
          The cassandra connector offer type for the Cosmos DB database C*
          account.
      returned: always
      type: str
      sample: null
    disable_key_based_metadata_write_access:
      description:
        - >-
          Disable write operations on metadata resources (databases, containers,
          throughput) via account keys
      returned: always
      type: bool
      sample: null
    key_vault_key_uri:
      description:
        - The URI of the key vault
      returned: always
      type: str
      sample: null
    public_network_access:
      description:
        - Whether requests from Public Network are allowed
      returned: always
      type: str
      sample: null
    enable_free_tier:
      description:
        - Flag to indicate whether Free Tier is enabled.
      returned: always
      type: bool
      sample: null
    api_properties:
      description:
        - API specific properties.
      returned: always
      type: dict
      sample: null
      contains:
        server_version:
          description:
            - Describes the ServerVersion of an a MongoDB account.
          returned: always
          type: str
          sample: null
    enable_analytical_storage:
      description:
        - Flag to indicate whether to enable storage analytics.
      returned: always
      type: bool
      sample: null
    cors:
      description:
        - The CORS policy for the Cosmos DB database account.
      returned: always
      type: list
      sample: null
      contains:
        allowed_origins:
          description:
            - >-
              The origin domains that are permitted to make a request against
              the service via CORS.
          returned: always
          type: str
          sample: null
        allowed_methods:
          description:
            - >-
              The methods (HTTP request verbs) that the origin domain may use
              for a CORS request.
          returned: always
          type: str
          sample: null
        allowed_headers:
          description:
            - >-
              The request headers that the origin domain may specify on the CORS
              request.
          returned: always
          type: str
          sample: null
        exposed_headers:
          description:
            - >-
              The response headers that may be sent in the response to the CORS
              request and exposed by the browser to the request issuer.
          returned: always
          type: str
          sample: null
        max_age_in_seconds:
          description:
            - >-
              The maximum amount time that a browser should cache the preflight
              OPTIONS request.
          returned: always
          type: integer
          sample: null
    value:
      description:
        - |-
          List of database account and their properties.
          The list of metrics for the account.
          The list of usages for the database. A usage is a point in time metric
          The list of metric definitions for the account.
      returned: always
      type: list
      sample: null
      contains:
        kind:
          description:
            - >-
              Indicates the type of database account. This can only be set at
              database account creation.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The status of the Cosmos DB account at the time the operation was
              called. The status can be one of following. 'Creating' – the
              Cosmos DB account is being created. When an account is in Creating
              state, only properties that are specified as input for the Create
              Cosmos DB account operation are returned. 'Succeeded' – the Cosmos
              DB account is active for use. 'Updating' – the Cosmos DB account
              is being updated. 'Deleting' – the Cosmos DB account is being
              deleted. 'Failed' – the Cosmos DB account failed creation.
              'DeletionFailed' – the Cosmos DB account deletion failed.
          returned: always
          type: str
          sample: null
        document_endpoint:
          description:
            - The connection endpoint for the Cosmos DB database account.
          returned: always
          type: str
          sample: null
        database_account_offer_type:
          description:
            - >-
              The offer type for the Cosmos DB database account. Default value:
              Standard.
          returned: always
          type: constant
          sample: null
        ip_rules:
          description:
            - List of IpRules.
          returned: always
          type: list
          sample: null
          contains:
            ip_address_or_range:
              description:
                - >-
                  A single IPv4 address or a single IPv4 address range in CIDR
                  format. Provided IPs must be well-formatted and cannot be
                  contained in one of the following ranges: 10.0.0.0/8,
                  100.64.0.0/10, 172.16.0.0/12, 192.168.0.0/16, since these are
                  not enforceable by the IP address filter. Example of valid
                  inputs: “23.40.210.245” or “23.40.210.0/8”.
              returned: always
              type: str
              sample: null
        is_virtual_network_filter_enabled:
          description:
            - >-
              Flag to indicate whether to enable/disable Virtual Network ACL
              rules.
          returned: always
          type: bool
          sample: null
        enable_automatic_failover:
          description:
            - >-
              Enables automatic failover of the write region in the rare event
              that the region is unavailable due to an outage. Automatic
              failover will result in a new write region for the account and is
              chosen based on the failover priorities configured for the
              account.
          returned: always
          type: bool
          sample: null
        consistency_policy:
          description:
            - The consistency policy for the Cosmos DB database account.
          returned: always
          type: dict
          sample: null
          contains:
            default_consistency_level:
              description:
                - >-
                  The default consistency level and configuration settings of
                  the Cosmos DB account.
              returned: always
              type: sealed-choice
              sample: null
            max_staleness_prefix:
              description:
                - >-
                  When used with the Bounded Staleness consistency level, this
                  value represents the number of stale requests tolerated.
                  Accepted range for this value is 1 – 2,147,483,647. Required
                  when defaultConsistencyPolicy is set to 'BoundedStaleness'.
              returned: always
              type: integer
              sample: null
            max_interval_in_seconds:
              description:
                - >-
                  When used with the Bounded Staleness consistency level, this
                  value represents the time amount of staleness (in seconds)
                  tolerated. Accepted range for this value is 5 - 86400.
                  Required when defaultConsistencyPolicy is set to
                  'BoundedStaleness'.
              returned: always
              type: integer
              sample: null
        capabilities:
          description:
            - List of Cosmos DB capabilities for the account
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  Name of the Cosmos DB capability. For example, "name":
                  "EnableCassandra". Current values also include "EnableTable"
                  and "EnableGremlin".
              returned: always
              type: str
              sample: null
        write_locations:
          description:
            - >-
              An array that contains the write location for the Cosmos DB
              account.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  The unique identifier of the region within the database
                  account. Example: &lt;accountName&gt;-&lt;locationName&gt;.
              returned: always
              type: str
              sample: null
            location_name:
              description:
                - The name of the region.
              returned: always
              type: str
              sample: null
            document_endpoint:
              description:
                - >-
                  The connection endpoint for the specific region. Example:
                  https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
              returned: always
              type: str
              sample: null
            provisioning_state:
              description:
                - >-
                  The status of the Cosmos DB account at the time the operation
                  was called. The status can be one of following. 'Creating' –
                  the Cosmos DB account is being created. When an account is in
                  Creating state, only properties that are specified as input
                  for the Create Cosmos DB account operation are returned.
                  'Succeeded' – the Cosmos DB account is active for use.
                  'Updating' – the Cosmos DB account is being updated.
                  'Deleting' – the Cosmos DB account is being deleted. 'Failed'
                  – the Cosmos DB account failed creation. 'DeletionFailed' –
                  the Cosmos DB account deletion failed.
              returned: always
              type: str
              sample: null
            failover_priority:
              description:
                - >-
                  The failover priority of the region. A failover priority of 0
                  indicates a write region. The maximum value for a failover
                  priority = (total number of regions - 1). Failover priority
                  values must be unique for each of the regions in which the
                  database account exists.
              returned: always
              type: integer
              sample: null
            is_zone_redundant:
              description:
                - >-
                  Flag to indicate whether or not this region is an
                  AvailabilityZone region
              returned: always
              type: bool
              sample: null
        read_locations:
          description:
            - >-
              An array that contains of the read locations enabled for the
              Cosmos DB account.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  The unique identifier of the region within the database
                  account. Example: &lt;accountName&gt;-&lt;locationName&gt;.
              returned: always
              type: str
              sample: null
            location_name:
              description:
                - The name of the region.
              returned: always
              type: str
              sample: null
            document_endpoint:
              description:
                - >-
                  The connection endpoint for the specific region. Example:
                  https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
              returned: always
              type: str
              sample: null
            provisioning_state:
              description:
                - >-
                  The status of the Cosmos DB account at the time the operation
                  was called. The status can be one of following. 'Creating' –
                  the Cosmos DB account is being created. When an account is in
                  Creating state, only properties that are specified as input
                  for the Create Cosmos DB account operation are returned.
                  'Succeeded' – the Cosmos DB account is active for use.
                  'Updating' – the Cosmos DB account is being updated.
                  'Deleting' – the Cosmos DB account is being deleted. 'Failed'
                  – the Cosmos DB account failed creation. 'DeletionFailed' –
                  the Cosmos DB account deletion failed.
              returned: always
              type: str
              sample: null
            failover_priority:
              description:
                - >-
                  The failover priority of the region. A failover priority of 0
                  indicates a write region. The maximum value for a failover
                  priority = (total number of regions - 1). Failover priority
                  values must be unique for each of the regions in which the
                  database account exists.
              returned: always
              type: integer
              sample: null
            is_zone_redundant:
              description:
                - >-
                  Flag to indicate whether or not this region is an
                  AvailabilityZone region
              returned: always
              type: bool
              sample: null
        locations:
          description:
            - >-
              An array that contains all of the locations enabled for the Cosmos
              DB account.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  The unique identifier of the region within the database
                  account. Example: &lt;accountName&gt;-&lt;locationName&gt;.
              returned: always
              type: str
              sample: null
            location_name:
              description:
                - The name of the region.
              returned: always
              type: str
              sample: null
            document_endpoint:
              description:
                - >-
                  The connection endpoint for the specific region. Example:
                  https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
              returned: always
              type: str
              sample: null
            provisioning_state:
              description:
                - >-
                  The status of the Cosmos DB account at the time the operation
                  was called. The status can be one of following. 'Creating' –
                  the Cosmos DB account is being created. When an account is in
                  Creating state, only properties that are specified as input
                  for the Create Cosmos DB account operation are returned.
                  'Succeeded' – the Cosmos DB account is active for use.
                  'Updating' – the Cosmos DB account is being updated.
                  'Deleting' – the Cosmos DB account is being deleted. 'Failed'
                  – the Cosmos DB account failed creation. 'DeletionFailed' –
                  the Cosmos DB account deletion failed.
              returned: always
              type: str
              sample: null
            failover_priority:
              description:
                - >-
                  The failover priority of the region. A failover priority of 0
                  indicates a write region. The maximum value for a failover
                  priority = (total number of regions - 1). Failover priority
                  values must be unique for each of the regions in which the
                  database account exists.
              returned: always
              type: integer
              sample: null
            is_zone_redundant:
              description:
                - >-
                  Flag to indicate whether or not this region is an
                  AvailabilityZone region
              returned: always
              type: bool
              sample: null
        failover_policies:
          description:
            - >-
              An array that contains the regions ordered by their failover
              priorities.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  The unique identifier of the region in which the database
                  account replicates to. Example:
                  &lt;accountName&gt;-&lt;locationName&gt;.
              returned: always
              type: str
              sample: null
            location_name:
              description:
                - The name of the region in which the database account exists.
              returned: always
              type: str
              sample: null
            failover_priority:
              description:
                - >-
                  The failover priority of the region. A failover priority of 0
                  indicates a write region. The maximum value for a failover
                  priority = (total number of regions - 1). Failover priority
                  values must be unique for each of the regions in which the
                  database account exists.
              returned: always
              type: integer
              sample: null
        virtual_network_rules:
          description:
            - >-
              List of Virtual Network ACL rules configured for the Cosmos DB
              account.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  Resource ID of a subnet, for example:
                  /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
              returned: always
              type: str
              sample: null
            ignore_missing_vnet_service_endpoint:
              description:
                - >-
                  Create firewall rule before the virtual network has vnet
                  service endpoint enabled.
              returned: always
              type: bool
              sample: null
        private_endpoint_connections:
          description:
            - >-
              List of Private Endpoint Connections configured for the Cosmos DB
              account.
          returned: always
          type: list
          sample: null
          contains:
            private_endpoint:
              description:
                - Private endpoint which the connection belongs to.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource id of the private endpoint.
                  returned: always
                  type: str
                  sample: null
            private_link_service_connection_state:
              description:
                - Connection State of the Private Endpoint Connection.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - The private link service connection status.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - >-
                      Any action that is required beyond basic workflow
                      (approve/ reject/ disconnect)
                  returned: always
                  type: str
                  sample: null
        enable_multiple_write_locations:
          description:
            - Enables the account to write in multiple locations
          returned: always
          type: bool
          sample: null
        enable_cassandra_connector:
          description:
            - Enables the cassandra connector on the Cosmos DB C* account
          returned: always
          type: bool
          sample: null
        connector_offer:
          description:
            - >-
              The cassandra connector offer type for the Cosmos DB database C*
              account.
          returned: always
          type: str
          sample: null
        disable_key_based_metadata_write_access:
          description:
            - >-
              Disable write operations on metadata resources (databases,
              containers, throughput) via account keys
          returned: always
          type: bool
          sample: null
        key_vault_key_uri:
          description:
            - The URI of the key vault
          returned: always
          type: str
          sample: null
        public_network_access:
          description:
            - Whether requests from Public Network are allowed
          returned: always
          type: str
          sample: null
        enable_free_tier:
          description:
            - Flag to indicate whether Free Tier is enabled.
          returned: always
          type: bool
          sample: null
        api_properties:
          description:
            - API specific properties.
          returned: always
          type: dict
          sample: null
          contains:
            server_version:
              description:
                - Describes the ServerVersion of an a MongoDB account.
              returned: always
              type: str
              sample: null
        enable_analytical_storage:
          description:
            - Flag to indicate whether to enable storage analytics.
          returned: always
          type: bool
          sample: null
        cors:
          description:
            - The CORS policy for the Cosmos DB database account.
          returned: always
          type: list
          sample: null
          contains:
            allowed_origins:
              description:
                - >-
                  The origin domains that are permitted to make a request
                  against the service via CORS.
              returned: always
              type: str
              sample: null
            allowed_methods:
              description:
                - >-
                  The methods (HTTP request verbs) that the origin domain may
                  use for a CORS request.
              returned: always
              type: str
              sample: null
            allowed_headers:
              description:
                - >-
                  The request headers that the origin domain may specify on the
                  CORS request.
              returned: always
              type: str
              sample: null
            exposed_headers:
              description:
                - >-
                  The response headers that may be sent in the response to the
                  CORS request and exposed by the browser to the request issuer.
              returned: always
              type: str
              sample: null
            max_age_in_seconds:
              description:
                - >-
                  The maximum amount time that a browser should cache the
                  preflight OPTIONS request.
              returned: always
              type: integer
              sample: null
    primary_readonly_master_key:
      description:
        - Base 64 encoded value of the primary read-only key.
      returned: always
      type: str
      sample: null
    secondary_readonly_master_key:
      description:
        - Base 64 encoded value of the secondary read-only key.
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
    from azure.mgmt.cosmos import CosmosDBManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDatabaseAccountInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            account_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDatabaseAccountInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.filter is not None):
            self.results['database_accounts'] = self.format_item(self.listmetric())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listusage())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.getreadonlykey())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listmetricdefinition())
        elif (self.resource_group_name is not None):
            self.results['database_accounts'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['database_accounts'] = self.format_item(self.list())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_metric(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listusage(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_usage(resource_group_name=self.resource_group_name,
                                                                     account_name=self.account_name,
                                                                     filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get(resource_group_name=self.resource_group_name,
                                                              account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getreadonlykey(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_read_only_key(resource_group_name=self.resource_group_name,
                                                                            account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_metric_definition(resource_group_name=self.resource_group_name,
                                                                                 account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list()
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
    AzureRMDatabaseAccountInfo()


if __name__ == '__main__':
    main()
