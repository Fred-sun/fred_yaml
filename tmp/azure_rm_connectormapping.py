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
module: azure_rm_connectormapping
version_added: '2.9'
short_description: Manage Azure ConnectorMapping instance.
description:
  - 'Create, update and delete instance of Azure ConnectorMapping.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  hub_name:
    description:
      - The name of the hub.
    required: true
    type: str
  connector_name:
    description:
      - The name of the connector.
    required: true
    type: str
  mapping_name:
    description:
      - The name of the connector mapping.
    required: true
    type: str
  connector_type:
    description:
      - Type of connector.
    type: str
    choices:
      - None
      - CRM
      - AzureBlob
      - Salesforce
      - ExchangeOnline
      - Outbound
  entity_type:
    description:
      - Defines which entity type the file should map to.
    type: sealed-choice
  entity_type_name:
    description:
      - The mapping entity name.
    type: str
  display_name:
    description:
      - Display name for the connector mapping.
    type: str
  description:
    description:
      - The description of the connector mapping.
    type: str
  folder_path:
    description:
      - The folder path for the mapping.
    type: str
  file_filter:
    description:
      - The file filter for the mapping.
    type: str
  has_header:
    description:
      - If the file contains a header or not.
    type: bool
  error_management:
    description:
      - The error management setting for the mapping.
    type: dict
    suboptions:
      error_management_type:
        description:
          - The type of error management to use for the mapping.
        required: true
        type: sealed-choice
      error_limit:
        description:
          - The error limit allowed while importing data.
        type: integer
  format:
    description:
      - The format of mapping property.
    type: dict
    suboptions:
      format_type:
        description:
          - The type mapping format.
        required: true
        type: constant
      column_delimiter:
        description:
          - The character that signifies a break between columns.
        type: str
      accept_language:
        description:
          - The oData language.
        type: str
      quote_character:
        description:
          - 'Quote character, used to indicate enquoted fields.'
        type: str
      quote_escape_character:
        description:
          - 'Escape character for quotes, can be the same as the quoteCharacter.'
        type: str
      array_separator:
        description:
          - Character separating array elements.
        type: str
  availability:
    description:
      - The availability of mapping property.
    type: dict
    suboptions:
      frequency:
        description:
          - The frequency to update.
        type: sealed-choice
      interval:
        description:
          - The interval of the given frequency to use.
        required: true
        type: integer
  structure:
    description:
      - Ingestion mapping information at property level.
    type: list
    suboptions:
      property_name:
        description:
          - The property name of the mapping entity.
        required: true
        type: str
      column_name:
        description:
          - The column name of the import file.
        required: true
        type: str
      custom_format_specifier:
        description:
          - Custom format specifier for input parsing.
        type: str
      is_encrypted:
        description:
          - Indicates if the column is encrypted.
        type: bool
  complete_operation:
    description:
      - The operation after import is done.
    type: dict
    suboptions:
      completion_operation_type:
        description:
          - The type of completion operation.
        type: sealed-choice
      destination_folder:
        description:
          - >-
            The destination folder where files will be moved to once the import
            is done.
        type: str
  state:
    description:
      - Assert the state of the ConnectorMapping.
      - >-
        Use C(present) to create or update an ConnectorMapping and C(absent) to
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
    - name: ConnectorMappings_CreateOrUpdate
      azure_rm_connectormapping: 
        connector_name: testConnector8858
        hub_name: sdkTestHub
        mapping_name: testMapping12491
        resource_group_name: TestHubRG
        properties:
          description: Test mapping
          display_name: testMapping12491
          entity_type: Interaction
          entity_type_name: TestInteractionType2967
          mapping_properties:
            format:
              column_delimiter: '|'
              format_type: TextFormat
            availability:
              frequency: Hour
              interval: 5
            complete_operation:
              completion_operation_type: DeleteFile
              destination_folder: fakePath
            error_management:
              error_limit: 10
              error_management_type: StopImport
            file_filter: unknown
            folder_path: 'http://sample.dne/file'
            has_header: false
            structure:
              - column_name: unknown1
                is_encrypted: false
                property_name: unknwon1
              - column_name: unknown2
                is_encrypted: true
                property_name: unknwon2
        

    - name: ConnectorMappings_Delete
      azure_rm_connectormapping: 
        connector_name: testConnector8858
        hub_name: sdkTestHub
        mapping_name: testMapping12491
        resource_group_name: TestHubRG
        

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
connector_name:
  description:
    - The connector name.
  returned: always
  type: str
  sample: null
connector_type:
  description:
    - Type of connector.
  returned: always
  type: str
  sample: null
created:
  description:
    - The created time.
  returned: always
  type: str
  sample: null
last_modified:
  description:
    - The last modified time.
  returned: always
  type: str
  sample: null
entity_type:
  description:
    - Defines which entity type the file should map to.
  returned: always
  type: sealed-choice
  sample: null
entity_type_name:
  description:
    - The mapping entity name.
  returned: always
  type: str
  sample: null
connector_mapping_name:
  description:
    - The connector mapping name
  returned: always
  type: str
  sample: null
display_name:
  description:
    - Display name for the connector mapping.
  returned: always
  type: str
  sample: null
description:
  description:
    - The description of the connector mapping.
  returned: always
  type: str
  sample: null
data_format_id:
  description:
    - The DataFormat ID.
  returned: always
  type: str
  sample: null
next_run_time:
  description:
    - The next run time based on customer's settings.
  returned: always
  type: str
  sample: null
run_id:
  description:
    - The RunId.
  returned: always
  type: str
  sample: null
state:
  description:
    - State of connector mapping.
  returned: always
  type: sealed-choice
  sample: null
tenant_id:
  description:
    - The hub name.
  returned: always
  type: str
  sample: null
folder_path:
  description:
    - The folder path for the mapping.
  returned: always
  type: str
  sample: null
file_filter:
  description:
    - The file filter for the mapping.
  returned: always
  type: str
  sample: null
has_header:
  description:
    - If the file contains a header or not.
  returned: always
  type: bool
  sample: null
error_management:
  description:
    - The error management setting for the mapping.
  returned: always
  type: dict
  sample: null
  contains:
    error_management_type:
      description:
        - The type of error management to use for the mapping.
      returned: always
      type: sealed-choice
      sample: null
    error_limit:
      description:
        - The error limit allowed while importing data.
      returned: always
      type: integer
      sample: null
format:
  description:
    - The format of mapping property.
  returned: always
  type: dict
  sample: null
  contains:
    format_type:
      description:
        - The type mapping format.
      returned: always
      type: constant
      sample: null
    column_delimiter:
      description:
        - The character that signifies a break between columns.
      returned: always
      type: str
      sample: null
    accept_language:
      description:
        - The oData language.
      returned: always
      type: str
      sample: null
    quote_character:
      description:
        - 'Quote character, used to indicate enquoted fields.'
      returned: always
      type: str
      sample: null
    quote_escape_character:
      description:
        - 'Escape character for quotes, can be the same as the quoteCharacter.'
      returned: always
      type: str
      sample: null
    array_separator:
      description:
        - Character separating array elements.
      returned: always
      type: str
      sample: null
availability:
  description:
    - The availability of mapping property.
  returned: always
  type: dict
  sample: null
  contains:
    frequency:
      description:
        - The frequency to update.
      returned: always
      type: sealed-choice
      sample: null
    interval:
      description:
        - The interval of the given frequency to use.
      returned: always
      type: integer
      sample: null
structure:
  description:
    - Ingestion mapping information at property level.
  returned: always
  type: list
  sample: null
  contains:
    property_name:
      description:
        - The property name of the mapping entity.
      returned: always
      type: str
      sample: null
    column_name:
      description:
        - The column name of the import file.
      returned: always
      type: str
      sample: null
    custom_format_specifier:
      description:
        - Custom format specifier for input parsing.
      returned: always
      type: str
      sample: null
    is_encrypted:
      description:
        - Indicates if the column is encrypted.
      returned: always
      type: bool
      sample: null
complete_operation:
  description:
    - The operation after import is done.
  returned: always
  type: dict
  sample: null
  contains:
    completion_operation_type:
      description:
        - The type of completion operation.
      returned: always
      type: sealed-choice
      sample: null
    destination_folder:
      description:
        - >-
          The destination folder where files will be moved to once the import is
          done.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConnectorMapping(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            hub_name=dict(
                type='str',
                required=True
            ),
            connector_name=dict(
                type='str',
                required=True
            ),
            mapping_name=dict(
                type='str',
                required=True
            ),
            connector_type=dict(
                type='str',
                disposition='/connector_type',
                choices=['None',
                         'CRM',
                         'AzureBlob',
                         'Salesforce',
                         'ExchangeOnline',
                         'Outbound']
            ),
            entity_type=dict(
                type='sealed-choice',
                disposition='/entity_type'
            ),
            entity_type_name=dict(
                type='str',
                disposition='/entity_type_name'
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            folder_path=dict(
                type='str',
                disposition='/folder_path'
            ),
            file_filter=dict(
                type='str',
                disposition='/file_filter'
            ),
            has_header=dict(
                type='bool',
                disposition='/has_header'
            ),
            error_management=dict(
                type='dict',
                disposition='/error_management',
                options=dict(
                    error_management_type=dict(
                        type='sealed-choice',
                        disposition='error_management_type',
                        required=True
                    ),
                    error_limit=dict(
                        type='integer',
                        disposition='error_limit'
                    )
                )
            ),
            format=dict(
                type='dict',
                disposition='/format',
                options=dict(
                    format_type=dict(
                        type='constant',
                        disposition='format_type',
                        required=True
                    ),
                    column_delimiter=dict(
                        type='str',
                        disposition='column_delimiter'
                    ),
                    accept_language=dict(
                        type='str',
                        disposition='accept_language'
                    ),
                    quote_character=dict(
                        type='str',
                        disposition='quote_character'
                    ),
                    quote_escape_character=dict(
                        type='str',
                        disposition='quote_escape_character'
                    ),
                    array_separator=dict(
                        type='str',
                        disposition='array_separator'
                    )
                )
            ),
            availability=dict(
                type='dict',
                disposition='/availability',
                options=dict(
                    frequency=dict(
                        type='sealed-choice',
                        disposition='frequency'
                    ),
                    interval=dict(
                        type='integer',
                        disposition='interval',
                        required=True
                    )
                )
            ),
            structure=dict(
                type='list',
                disposition='/structure',
                elements='dict',
                options=dict(
                    property_name=dict(
                        type='str',
                        disposition='property_name',
                        required=True
                    ),
                    column_name=dict(
                        type='str',
                        disposition='column_name',
                        required=True
                    ),
                    custom_format_specifier=dict(
                        type='str',
                        disposition='custom_format_specifier'
                    ),
                    is_encrypted=dict(
                        type='bool',
                        disposition='is_encrypted'
                    )
                )
            ),
            complete_operation=dict(
                type='dict',
                disposition='/complete_operation',
                options=dict(
                    completion_operation_type=dict(
                        type='sealed-choice',
                        disposition='completion_operation_type'
                    ),
                    destination_folder=dict(
                        type='str',
                        disposition='destination_folder'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.connector_name = None
        self.mapping_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConnectorMapping, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

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
            response = self.mgmt_client.connector_mappings.create_or_update(resource_group_name=self.resource_group_name,
                                                                            hub_name=self.hub_name,
                                                                            connector_name=self.connector_name,
                                                                            mapping_name=self.mapping_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ConnectorMapping instance.')
            self.fail('Error creating the ConnectorMapping instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.connector_mappings.delete(resource_group_name=self.resource_group_name,
                                                                  hub_name=self.hub_name,
                                                                  connector_name=self.connector_name,
                                                                  mapping_name=self.mapping_name)
        except CloudError as e:
            self.log('Error attempting to delete the ConnectorMapping instance.')
            self.fail('Error deleting the ConnectorMapping instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.connector_mappings.get(resource_group_name=self.resource_group_name,
                                                               hub_name=self.hub_name,
                                                               connector_name=self.connector_name,
                                                               mapping_name=self.mapping_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMConnectorMapping()


if __name__ == '__main__':
    main()
