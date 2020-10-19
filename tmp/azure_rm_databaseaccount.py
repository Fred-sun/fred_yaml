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
module: azure_rm_databaseaccount
version_added: '2.9'
short_description: Manage Azure DatabaseAccount instance.
description:
  - 'Create, update and delete instance of Azure DatabaseAccount.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    required: true
    type: str
  location:
    description:
      - The location of the resource group to which the resource belongs.
    type: str
  consistency_policy:
    description:
      - The consistency policy for the Cosmos DB account.
    type: dict
    suboptions:
      default_consistency_level:
        description:
          - >-
            The default consistency level and configuration settings of the
            Cosmos DB account.
        required: true
        type: sealed-choice
      max_staleness_prefix:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the number of stale requests tolerated. Accepted range
            for this value is 1 – 2,147,483,647. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
        type: integer
      max_interval_in_seconds:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the time amount of staleness (in seconds) tolerated.
            Accepted range for this value is 5 - 86400. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
        type: integer
  locations:
    description:
      - >-
        An array that contains the georeplication locations enabled for the
        Cosmos DB account.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region within the database account.
            Example: &lt;accountName&gt;-&lt;locationName&gt;.
        type: str
      location_name:
        description:
          - The name of the region.
        type: str
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
        type: str
      provisioning_state:
        description:
          - >-
            The status of the Cosmos DB account at the time the operation was
            called. The status can be one of following. 'Creating' – the Cosmos
            DB account is being created. When an account is in Creating state,
            only properties that are specified as input for the Create Cosmos DB
            account operation are returned. 'Succeeded' – the Cosmos DB account
            is active for use. 'Updating' – the Cosmos DB account is being
            updated. 'Deleting' – the Cosmos DB account is being deleted.
            'Failed' – the Cosmos DB account failed creation. 'DeletionFailed' –
            the Cosmos DB account deletion failed.
        type: str
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
        type: integer
      is_zone_redundant:
        description:
          - >-
            Flag to indicate whether or not this region is an AvailabilityZone
            region
        type: bool
  ip_rules:
    description:
      - List of IpRules.
    type: list
    suboptions:
      ip_address_or_range:
        description:
          - >-
            A single IPv4 address or a single IPv4 address range in CIDR format.
            Provided IPs must be well-formatted and cannot be contained in one
            of the following ranges: 10.0.0.0/8, 100.64.0.0/10, 172.16.0.0/12,
            192.168.0.0/16, since these are not enforceable by the IP address
            filter. Example of valid inputs: “23.40.210.245” or “23.40.210.0/8”.
        type: str
  is_virtual_network_filter_enabled:
    description:
      - Flag to indicate whether to enable/disable Virtual Network ACL rules.
    type: bool
  enable_automatic_failover:
    description:
      - >-
        Enables automatic failover of the write region in the rare event that
        the region is unavailable due to an outage. Automatic failover will
        result in a new write region for the account and is chosen based on the
        failover priorities configured for the account.
    type: bool
  capabilities:
    description:
      - List of Cosmos DB capabilities for the account
    type: list
    suboptions:
      name:
        description:
          - >-
            Name of the Cosmos DB capability. For example, "name":
            "EnableCassandra". Current values also include "EnableTable" and
            "EnableGremlin".
        type: str
  virtual_network_rules:
    description:
      - List of Virtual Network ACL rules configured for the Cosmos DB account.
    type: list
    suboptions:
      id:
        description:
          - >-
            Resource ID of a subnet, for example:
            /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
        type: str
      ignore_missing_vnet_service_endpoint:
        description:
          - >-
            Create firewall rule before the virtual network has vnet service
            endpoint enabled.
        type: bool
  enable_multiple_write_locations:
    description:
      - Enables the account to write in multiple locations
    type: bool
  enable_cassandra_connector:
    description:
      - Enables the cassandra connector on the Cosmos DB C* account
    type: bool
  connector_offer:
    description:
      - >-
        The cassandra connector offer type for the Cosmos DB database C*
        account.
    type: str
    choices:
      - Small
  disable_key_based_metadata_write_access:
    description:
      - >-
        Disable write operations on metadata resources (databases, containers,
        throughput) via account keys
    type: bool
  key_vault_key_uri:
    description:
      - The URI of the key vault
    type: str
  enable_free_tier:
    description:
      - Flag to indicate whether Free Tier is enabled.
    type: bool
  enable_analytical_storage:
    description:
      - Flag to indicate whether to enable storage analytics.
    type: bool
  cors:
    description:
      - The CORS policy for the Cosmos DB database account.
    type: list
    suboptions:
      allowed_origins:
        description:
          - >-
            The origin domains that are permitted to make a request against the
            service via CORS.
        required: true
        type: str
      allowed_methods:
        description:
          - >-
            The methods (HTTP request verbs) that the origin domain may use for
            a CORS request.
        type: str
      allowed_headers:
        description:
          - >-
            The request headers that the origin domain may specify on the CORS
            request.
        type: str
      exposed_headers:
        description:
          - >-
            The response headers that may be sent in the response to the CORS
            request and exposed by the browser to the request issuer.
        type: str
      max_age_in_seconds:
        description:
          - >-
            The maximum amount time that a browser should cache the preflight
            OPTIONS request.
        type: integer
  server_version:
    description:
      - Describes the ServerVersion of an a MongoDB account.
    type: str
    choices:
      - '3.2'
      - '3.6'
  kind:
    description:
      - >-
        Indicates the type of database account. This can only be set at database
        account creation.
    type: str
    choices:
      - GlobalDocumentDB
      - MongoDB
      - Parse
  databaseaccountoffertype:
    description:
      - The offer type for the database
    type: constant
  state:
    description:
      - Assert the state of the DatabaseAccount.
      - >-
        Use C(present) to create or update an DatabaseAccount and C(absent) to
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
    - name: CosmosDBDatabaseAccountPatch
      azure_rm_databaseaccount: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountCreateMax
      azure_rm_databaseaccount: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountCreateMin
      azure_rm_databaseaccount: 
        account_name: ddb1
        resource_group_name: rg1
        

    - name: CosmosDBDatabaseAccountDelete
      azure_rm_databaseaccount: 
        account_name: ddb1
        resource_group_name: rg1
        

'''

RETURN = '''
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
      Tags are a list of key-value pairs that describe the resource. These tags
      can be used in viewing and grouping this resource (across resource
      groups). A maximum of 15 tags can be provided for a resource. Each tag
      must have a key no greater than 128 characters and value no greater than
      256 characters. For example, the default experience for a template type is
      set with "defaultExperience": "Cassandra". Current "defaultExperience"
      values also include "Table", "Graph", "DocumentDB", and "MongoDB".
  returned: always
  type: dictionary
  sample: null
kind:
  description:
    - >-
      Indicates the type of database account. This can only be set at database
      account creation.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - >-
      The status of the Cosmos DB account at the time the operation was called.
      The status can be one of following. 'Creating' – the Cosmos DB account is
      being created. When an account is in Creating state, only properties that
      are specified as input for the Create Cosmos DB account operation are
      returned. 'Succeeded' – the Cosmos DB account is active for use.
      'Updating' – the Cosmos DB account is being updated. 'Deleting' – the
      Cosmos DB account is being deleted. 'Failed' – the Cosmos DB account
      failed creation. 'DeletionFailed' – the Cosmos DB account deletion failed.
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
          A single IPv4 address or a single IPv4 address range in CIDR format.
          Provided IPs must be well-formatted and cannot be contained in one of
          the following ranges: 10.0.0.0/8, 100.64.0.0/10, 172.16.0.0/12,
          192.168.0.0/16, since these are not enforceable by the IP address
          filter. Example of valid inputs: “23.40.210.245” or “23.40.210.0/8”.
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
      Enables automatic failover of the write region in the rare event that the
      region is unavailable due to an outage. Automatic failover will result in
      a new write region for the account and is chosen based on the failover
      priorities configured for the account.
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
          The default consistency level and configuration settings of the Cosmos
          DB account.
      returned: always
      type: sealed-choice
      sample: null
    max_staleness_prefix:
      description:
        - >-
          When used with the Bounded Staleness consistency level, this value
          represents the number of stale requests tolerated. Accepted range for
          this value is 1 – 2,147,483,647. Required when
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
    failover_priority:
      description:
        - >-
          The failover priority of the region. A failover priority of 0
          indicates a write region. The maximum value for a failover priority =
          (total number of regions - 1). Failover priority values must be unique
          for each of the regions in which the database account exists.
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
    failover_priority:
      description:
        - >-
          The failover priority of the region. A failover priority of 0
          indicates a write region. The maximum value for a failover priority =
          (total number of regions - 1). Failover priority values must be unique
          for each of the regions in which the database account exists.
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
    failover_priority:
      description:
        - >-
          The failover priority of the region. A failover priority of 0
          indicates a write region. The maximum value for a failover priority =
          (total number of regions - 1). Failover priority values must be unique
          for each of the regions in which the database account exists.
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
    - An array that contains the regions ordered by their failover priorities.
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
          indicates a write region. The maximum value for a failover priority =
          (total number of regions - 1). Failover priority values must be unique
          for each of the regions in which the database account exists.
      returned: always
      type: integer
      sample: null
virtual_network_rules:
  description:
    - List of Virtual Network ACL rules configured for the Cosmos DB account.
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
    - List of Private Endpoint Connections configured for the Cosmos DB account.
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
    - The cassandra connector offer type for the Cosmos DB database C* account.
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
          The origin domains that are permitted to make a request against the
          service via CORS.
      returned: always
      type: str
      sample: null
    allowed_methods:
      description:
        - >-
          The methods (HTTP request verbs) that the origin domain may use for a
          CORS request.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.cosmos import CosmosDBManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDatabaseAccount(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            consistency_policy=dict(
                type='dict',
                disposition='/consistency_policy',
                options=dict(
                    default_consistency_level=dict(
                        type='sealed-choice',
                        disposition='default_consistency_level',
                        required=True
                    ),
                    max_staleness_prefix=dict(
                        type='integer',
                        disposition='max_staleness_prefix'
                    ),
                    max_interval_in_seconds=dict(
                        type='integer',
                        disposition='max_interval_in_seconds'
                    )
                )
            ),
            locations=dict(
                type='list',
                disposition='/locations',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        updatable=False,
                        disposition='id'
                    ),
                    location_name=dict(
                        type='str',
                        disposition='location_name'
                    ),
                    document_endpoint=dict(
                        type='str',
                        updatable=False,
                        disposition='document_endpoint'
                    ),
                    provisioning_state=dict(
                        type='str',
                        updatable=False,
                        disposition='provisioning_state'
                    ),
                    failover_priority=dict(
                        type='integer',
                        disposition='failover_priority'
                    ),
                    is_zone_redundant=dict(
                        type='bool',
                        disposition='is_zone_redundant'
                    )
                )
            ),
            ip_rules=dict(
                type='list',
                disposition='/ip_rules',
                elements='dict',
                options=dict(
                    ip_address_or_range=dict(
                        type='str',
                        disposition='ip_address_or_range'
                    )
                )
            ),
            is_virtual_network_filter_enabled=dict(
                type='bool',
                disposition='/is_virtual_network_filter_enabled'
            ),
            enable_automatic_failover=dict(
                type='bool',
                disposition='/enable_automatic_failover'
            ),
            capabilities=dict(
                type='list',
                disposition='/capabilities',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    )
                )
            ),
            virtual_network_rules=dict(
                type='list',
                disposition='/virtual_network_rules',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    ),
                    ignore_missing_vnet_service_endpoint=dict(
                        type='bool',
                        disposition='ignore_missing_vnet_service_endpoint'
                    )
                )
            ),
            enable_multiple_write_locations=dict(
                type='bool',
                disposition='/enable_multiple_write_locations'
            ),
            enable_cassandra_connector=dict(
                type='bool',
                disposition='/enable_cassandra_connector'
            ),
            connector_offer=dict(
                type='str',
                disposition='/connector_offer',
                choices=['Small']
            ),
            disable_key_based_metadata_write_access=dict(
                type='bool',
                disposition='/disable_key_based_metadata_write_access'
            ),
            key_vault_key_uri=dict(
                type='str',
                disposition='/key_vault_key_uri'
            ),
            enable_free_tier=dict(
                type='bool',
                disposition='/enable_free_tier'
            ),
            enable_analytical_storage=dict(
                type='bool',
                disposition='/enable_analytical_storage'
            ),
            cors=dict(
                type='list',
                disposition='/cors',
                elements='dict',
                options=dict(
                    allowed_origins=dict(
                        type='str',
                        disposition='allowed_origins',
                        required=True
                    ),
                    allowed_methods=dict(
                        type='str',
                        disposition='allowed_methods'
                    ),
                    allowed_headers=dict(
                        type='str',
                        disposition='allowed_headers'
                    ),
                    exposed_headers=dict(
                        type='str',
                        disposition='exposed_headers'
                    ),
                    max_age_in_seconds=dict(
                        type='integer',
                        disposition='max_age_in_seconds'
                    )
                )
            ),
            server_version=dict(
                type='str',
                disposition='/server_version',
                choices=['3.2',
                         '3.6']
            ),
            kind=dict(
                type='str',
                disposition='/kind',
                choices=['GlobalDocumentDB',
                         'MongoDB',
                         'Parse']
            ),
            databaseaccountoffertype=dict(
                type='constant',
                disposition='/databaseaccountoffertype'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDatabaseAccount, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

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
            response = self.mgmt_client.database_accounts.create_or_update(resource_group_name=self.resource_group_name,
                                                                           account_name=self.account_name,
                                                                           create_update_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DatabaseAccount instance.')
            self.fail('Error creating the DatabaseAccount instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.database_accounts.delete(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name)
        except CloudError as e:
            self.log('Error attempting to delete the DatabaseAccount instance.')
            self.fail('Error deleting the DatabaseAccount instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.database_accounts.get(resource_group_name=self.resource_group_name,
                                                              account_name=self.account_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDatabaseAccount()


if __name__ == '__main__':
    main()
