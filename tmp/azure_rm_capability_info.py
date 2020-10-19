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
module: azure_rm_capability_info
version_added: '2.9'
short_description: Get Capability info.
description:
  - Get info of Capability.
options:
  location_name:
    description:
      - The location name whose capabilities are retrieved.
    required: true
    type: str
  include:
    description:
      - 'If specified, restricts the response to only include the selected item.'
    required: true
    type: str
    choices:
      - supportedEditions
      - supportedElasticPoolEditions
      - supportedManagedInstanceVersions
      - supportedInstancePoolEditions
      - supportedManagedInstanceEditions
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List subscription capabilities in the given location.
      azure_rm_capability_info: 
        location_name: eastus2euap
        

'''

RETURN = '''
capabilities:
  description: >-
    A list of dict results where the key is the name of the Capability and the
    values are the facts for that Capability.
  returned: always
  type: complex
  contains:
    name:
      description:
        - The location name.
      returned: always
      type: str
      sample: null
    supported_server_versions:
      description:
        - The list of supported server versions.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The server version name.
          returned: always
          type: str
          sample: null
        supported_editions:
          description:
            - The list of supported database editions.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The database edition name.
              returned: always
              type: str
              sample: null
            supported_service_level_objectives:
              description:
                - The list of supported service objectives for the edition.
              returned: always
              type: list
              sample: null
              contains:
                id:
                  description:
                    - The unique ID of the service objective.
                  returned: always
                  type: uuid
                  sample: null
                name:
                  description:
                    - The service objective name.
                  returned: always
                  type: str
                  sample: null
                supported_max_sizes:
                  description:
                    - The list of supported maximum database sizes.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    min_value:
                      description:
                        - Minimum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    max_value:
                      description:
                        - Maximum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    scale_size:
                      description:
                        - >-
                          Scale/step size for discrete values between the
                          minimum value and the maximum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    log_size:
                      description:
                        - Size of transaction log.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The log size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                performance_level:
                  description:
                    - The performance level.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    value:
                      description:
                        - Performance level value.
                      returned: always
                      type: number
                      sample: null
                    unit:
                      description:
                        - Unit type used to measure performance level.
                      returned: always
                      type: str
                      sample: null
                sku:
                  description:
                    - The sku.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    name:
                      description:
                        - >-
                          The name of the SKU, typically, a letter + Number
                          code, e.g. P3.
                      returned: always
                      type: str
                      sample: null
                    tier:
                      description:
                        - >-
                          The tier or edition of the particular SKU, e.g. Basic,
                          Premium.
                      returned: always
                      type: str
                      sample: null
                    size:
                      description:
                        - Size of the particular SKU
                      returned: always
                      type: str
                      sample: null
                    family:
                      description:
                        - >-
                          If the service has different generations of hardware,
                          for the same SKU, then that can be captured here.
                      returned: always
                      type: str
                      sample: null
                    capacity:
                      description:
                        - Capacity of the particular SKU.
                      returned: always
                      type: integer
                      sample: null
                supported_license_types:
                  description:
                    - List of supported license types.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - License type identifier.
                      returned: always
                      type: str
                      sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                included_max_size:
                  description:
                    - The included (free) max size.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    limit:
                      description:
                        - The maximum size limit (see 'unit' for the units).
                      returned: always
                      type: integer
                      sample: null
                    unit:
                      description:
                        - The units that the limit is expressed in.
                      returned: always
                      type: str
                      sample: null
                zone_redundant:
                  description:
                    - >-
                      Whether or not zone redundancy is supported for the
                      service objective.
                  returned: always
                  type: bool
                  sample: null
                supported_auto_pause_delay:
                  description:
                    - Supported time range for auto pause delay
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    min_value:
                      description:
                        - Minimum value
                      returned: always
                      type: integer
                      sample: null
                    max_value:
                      description:
                        - Maximum value
                      returned: always
                      type: integer
                      sample: null
                    step_size:
                      description:
                        - >-
                          Step value for discrete values between the minimum
                          value and the maximum value.
                      returned: always
                      type: integer
                      sample: null
                    default:
                      description:
                        - Default value is no value is provided
                      returned: always
                      type: integer
                      sample: null
                    unit:
                      description:
                        - Unit of time that delay is expressed in
                      returned: always
                      type: str
                      sample: null
                    do_not_pause_value:
                      description:
                        - >-
                          Value that is used to not pause (infinite delay before
                          pause)
                      returned: always
                      type: integer
                      sample: null
                supported_min_capacities:
                  description:
                    - List of supported min capacities
                  returned: always
                  type: list
                  sample: null
                  contains:
                    value:
                      description:
                        - Min capacity value
                      returned: always
                      type: number
                      sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                compute_model:
                  description:
                    - The compute model
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - The status of the capability.
                  returned: always
                  type: sealed-choice
                  sample: null
                reason:
                  description:
                    - The reason for the capability not being available.
                  returned: always
                  type: str
                  sample: null
            zone_redundant:
              description:
                - Whether or not zone redundancy is supported for the edition.
              returned: always
              type: bool
              sample: null
            read_scale:
              description:
                - The read scale capability for the edition.
              returned: always
              type: dict
              sample: null
              contains:
                max_number_of_replicas:
                  description:
                    - The maximum number of read scale replicas.
                  returned: always
                  type: integer
                  sample: null
                status:
                  description:
                    - The status of the capability.
                  returned: always
                  type: sealed-choice
                  sample: null
                reason:
                  description:
                    - The reason for the capability not being available.
                  returned: always
                  type: str
                  sample: null
            supported_storage_capabilities:
              description:
                - The list of supported storage capabilities for this edition
              returned: always
              type: list
              sample: null
              contains:
                storage_account_type:
                  description:
                    - The storage account type for the database's backups.
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - The status of the capability.
                  returned: always
                  type: sealed-choice
                  sample: null
                reason:
                  description:
                    - The reason for the capability not being available.
                  returned: always
                  type: str
                  sample: null
            status:
              description:
                - The status of the capability.
              returned: always
              type: sealed-choice
              sample: null
            reason:
              description:
                - The reason for the capability not being available.
              returned: always
              type: str
              sample: null
        supported_elastic_pool_editions:
          description:
            - The list of supported elastic pool editions.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The elastic pool edition name.
              returned: always
              type: str
              sample: null
            supported_elastic_pool_performance_levels:
              description:
                - The list of supported elastic pool DTU levels for the edition.
              returned: always
              type: list
              sample: null
              contains:
                performance_level:
                  description:
                    - The performance level for the pool.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    value:
                      description:
                        - Performance level value.
                      returned: always
                      type: number
                      sample: null
                    unit:
                      description:
                        - Unit type used to measure performance level.
                      returned: always
                      type: str
                      sample: null
                sku:
                  description:
                    - The sku.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    name:
                      description:
                        - >-
                          The name of the SKU, typically, a letter + Number
                          code, e.g. P3.
                      returned: always
                      type: str
                      sample: null
                    tier:
                      description:
                        - >-
                          The tier or edition of the particular SKU, e.g. Basic,
                          Premium.
                      returned: always
                      type: str
                      sample: null
                    size:
                      description:
                        - Size of the particular SKU
                      returned: always
                      type: str
                      sample: null
                    family:
                      description:
                        - >-
                          If the service has different generations of hardware,
                          for the same SKU, then that can be captured here.
                      returned: always
                      type: str
                      sample: null
                    capacity:
                      description:
                        - Capacity of the particular SKU.
                      returned: always
                      type: integer
                      sample: null
                supported_license_types:
                  description:
                    - List of supported license types.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - License type identifier.
                      returned: always
                      type: str
                      sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                max_database_count:
                  description:
                    - The maximum number of databases supported.
                  returned: always
                  type: integer
                  sample: null
                included_max_size:
                  description:
                    - The included (free) max size for this performance level.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    limit:
                      description:
                        - The maximum size limit (see 'unit' for the units).
                      returned: always
                      type: integer
                      sample: null
                    unit:
                      description:
                        - The units that the limit is expressed in.
                      returned: always
                      type: str
                      sample: null
                supported_max_sizes:
                  description:
                    - The list of supported max sizes.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    min_value:
                      description:
                        - Minimum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    max_value:
                      description:
                        - Maximum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    scale_size:
                      description:
                        - >-
                          Scale/step size for discrete values between the
                          minimum value and the maximum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    log_size:
                      description:
                        - Size of transaction log.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The log size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                supported_per_database_max_sizes:
                  description:
                    - The list of supported per database max sizes.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    min_value:
                      description:
                        - Minimum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    max_value:
                      description:
                        - Maximum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    scale_size:
                      description:
                        - >-
                          Scale/step size for discrete values between the
                          minimum value and the maximum value.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    log_size:
                      description:
                        - Size of transaction log.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The log size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                supported_per_database_max_performance_levels:
                  description:
                    - The list of supported per database max performance levels.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    limit:
                      description:
                        - The maximum performance level per database.
                      returned: always
                      type: number
                      sample: null
                    unit:
                      description:
                        - Unit type used to measure performance level.
                      returned: always
                      type: str
                      sample: null
                    supported_per_database_min_performance_levels:
                      description:
                        - The list of supported min database performance levels.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        limit:
                          description:
                            - The minimum performance level per database.
                          returned: always
                          type: number
                          sample: null
                        unit:
                          description:
                            - Unit type used to measure performance level.
                          returned: always
                          type: str
                          sample: null
                        status:
                          description:
                            - The status of the capability.
                          returned: always
                          type: sealed-choice
                          sample: null
                        reason:
                          description:
                            - The reason for the capability not being available.
                          returned: always
                          type: str
                          sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                zone_redundant:
                  description:
                    - >-
                      Whether or not zone redundancy is supported for the
                      performance level.
                  returned: always
                  type: bool
                  sample: null
                status:
                  description:
                    - The status of the capability.
                  returned: always
                  type: sealed-choice
                  sample: null
                reason:
                  description:
                    - The reason for the capability not being available.
                  returned: always
                  type: str
                  sample: null
            zone_redundant:
              description:
                - Whether or not zone redundancy is supported for the edition.
              returned: always
              type: bool
              sample: null
            status:
              description:
                - The status of the capability.
              returned: always
              type: sealed-choice
              sample: null
            reason:
              description:
                - The reason for the capability not being available.
              returned: always
              type: str
              sample: null
        status:
          description:
            - The status of the capability.
          returned: always
          type: sealed-choice
          sample: null
        reason:
          description:
            - The reason for the capability not being available.
          returned: always
          type: str
          sample: null
    supported_managed_instance_versions:
      description:
        - The list of supported managed instance versions.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The server version name.
          returned: always
          type: str
          sample: null
        supported_editions:
          description:
            - The list of supported managed instance editions.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The managed server version name.
              returned: always
              type: str
              sample: null
            supported_families:
              description:
                - The supported families.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Family name.
                  returned: always
                  type: str
                  sample: null
                sku:
                  description:
                    - SKU name.
                  returned: always
                  type: str
                  sample: null
                supported_license_types:
                  description:
                    - List of supported license types.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - License type identifier.
                      returned: always
                      type: str
                      sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                supported_vcores_values:
                  description:
                    - List of supported virtual cores values.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - The virtual cores identifier.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - The virtual cores value.
                      returned: always
                      type: integer
                      sample: null
                    included_max_size:
                      description:
                        - Included size.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    supported_storage_sizes:
                      description:
                        - Storage size ranges.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        min_value:
                          description:
                            - Minimum value.
                          returned: always
                          type: dict
                          sample: null
                          contains:
                            limit:
                              description:
                                - >-
                                  The maximum size limit (see 'unit' for the
                                  units).
                              returned: always
                              type: integer
                              sample: null
                            unit:
                              description:
                                - The units that the limit is expressed in.
                              returned: always
                              type: str
                              sample: null
                        max_value:
                          description:
                            - Maximum value.
                          returned: always
                          type: dict
                          sample: null
                          contains:
                            limit:
                              description:
                                - >-
                                  The maximum size limit (see 'unit' for the
                                  units).
                              returned: always
                              type: integer
                              sample: null
                            unit:
                              description:
                                - The units that the limit is expressed in.
                              returned: always
                              type: str
                              sample: null
                        scale_size:
                          description:
                            - >-
                              Scale/step size for discrete values between the
                              minimum value and the maximum value.
                          returned: always
                          type: dict
                          sample: null
                          contains:
                            limit:
                              description:
                                - >-
                                  The maximum size limit (see 'unit' for the
                                  units).
                              returned: always
                              type: integer
                              sample: null
                            unit:
                              description:
                                - The units that the limit is expressed in.
                              returned: always
                              type: str
                              sample: null
                        log_size:
                          description:
                            - Size of transaction log.
                          returned: always
                          type: dict
                          sample: null
                          contains:
                            limit:
                              description:
                                - The log size limit (see 'unit' for the units).
                              returned: always
                              type: integer
                              sample: null
                            unit:
                              description:
                                - The units that the limit is expressed in.
                              returned: always
                              type: str
                              sample: null
                        status:
                          description:
                            - The status of the capability.
                          returned: always
                          type: sealed-choice
                          sample: null
                        reason:
                          description:
                            - The reason for the capability not being available.
                          returned: always
                          type: str
                          sample: null
                    instance_pool_supported:
                      description:
                        - >-
                          True if this service objective is supported for
                          managed instances in an instance pool.
                      returned: always
                      type: bool
                      sample: null
                    standalone_supported:
                      description:
                        - >-
                          True if this service objective is supported for
                          standalone managed instances.
                      returned: always
                      type: bool
                      sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                status:
                  description:
                    - The status of the capability.
                  returned: always
                  type: sealed-choice
                  sample: null
                reason:
                  description:
                    - The reason for the capability not being available.
                  returned: always
                  type: str
                  sample: null
            status:
              description:
                - The status of the capability.
              returned: always
              type: sealed-choice
              sample: null
            reason:
              description:
                - The reason for the capability not being available.
              returned: always
              type: str
              sample: null
        supported_instance_pool_editions:
          description:
            - The list of supported instance pool editions.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The instance pool version name.
              returned: always
              type: str
              sample: null
            supported_families:
              description:
                - The supported families.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Family name.
                  returned: always
                  type: str
                  sample: null
                supported_license_types:
                  description:
                    - List of supported license types.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - License type identifier.
                      returned: always
                      type: str
                      sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                supported_vcores_values:
                  description:
                    - List of supported virtual cores values.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - The virtual cores identifier.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - The virtual cores value.
                      returned: always
                      type: integer
                      sample: null
                    storage_limit:
                      description:
                        - Storage limit.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        limit:
                          description:
                            - The maximum size limit (see 'unit' for the units).
                          returned: always
                          type: integer
                          sample: null
                        unit:
                          description:
                            - The units that the limit is expressed in.
                          returned: always
                          type: str
                          sample: null
                    status:
                      description:
                        - The status of the capability.
                      returned: always
                      type: sealed-choice
                      sample: null
                    reason:
                      description:
                        - The reason for the capability not being available.
                      returned: always
                      type: str
                      sample: null
                status:
                  description:
                    - The status of the capability.
                  returned: always
                  type: sealed-choice
                  sample: null
                reason:
                  description:
                    - The reason for the capability not being available.
                  returned: always
                  type: str
                  sample: null
            status:
              description:
                - The status of the capability.
              returned: always
              type: sealed-choice
              sample: null
            reason:
              description:
                - The reason for the capability not being available.
              returned: always
              type: str
              sample: null
        status:
          description:
            - The status of the capability.
          returned: always
          type: sealed-choice
          sample: null
        reason:
          description:
            - The reason for the capability not being available.
          returned: always
          type: str
          sample: null
    status:
      description:
        - The status of the capability.
      returned: always
      type: sealed-choice
      sample: null
    reason:
      description:
        - The reason for the capability not being available.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCapabilityInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            ),
            include=dict(
                type='str',
                choices=['supportedEditions',
                         'supportedElasticPoolEditions',
                         'supportedManagedInstanceVersions',
                         'supportedInstancePoolEditions',
                         'supportedManagedInstanceEditions'],
                required=True
            )
        )

        self.location_name = None
        self.include = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCapabilityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.location_name is not None):
            self.results['capabilities'] = self.format_item(self.listbylocation())
        return self.results

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.capabilities.list_by_location(location_name=self.location_name,
                                                                      include=self.include)
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
    AzureRMCapabilityInfo()


if __name__ == '__main__':
    main()
