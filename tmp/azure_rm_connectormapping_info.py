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
module: azure_rm_connectormapping_info
version_added: '2.9'
short_description: Get ConnectorMapping info.
description:
  - Get info of ConnectorMapping.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ConnectorMappings_Get
      azure_rm_connectormapping_info: 
        connector_name: testConnector8858
        hub_name: sdkTestHub
        mapping_name: testMapping12491
        resource_group_name: TestHubRG
        

    - name: ConnectorMappings_ListByConnector
      azure_rm_connectormapping_info: 
        connector_name: testConnector8858
        hub_name: sdkTestHub
        resource_group_name: TestHubRG
        

'''

RETURN = '''
connector_mappings:
  description: >-
    A list of dict results where the key is the name of the ConnectorMapping and
    the values are the facts for that ConnectorMapping.
  returned: always
  type: complex
  contains:
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
            - >-
              Escape character for quotes, can be the same as the
              quoteCharacter.
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
              The destination folder where files will be moved to once the
              import is done.
          returned: always
          type: str
          sample: null
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
                - >-
                  Escape character for quotes, can be the same as the
                  quoteCharacter.
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
                  The destination folder where files will be moved to once the
                  import is done.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Link to the next set of results.
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
    from azure.mgmt.customer import CustomerInsightsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMConnectorMappingInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.hub_name = None
        self.connector_name = None
        self.mapping_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-26'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMConnectorMappingInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CustomerInsightsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-26')

        if (self.resource_group_name is not None and
            self.hub_name is not None and
            self.connector_name is not None and
            self.mapping_name is not None):
            self.results['connector_mappings'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.hub_name is not None and
              self.connector_name is not None):
            self.results['connector_mappings'] = self.format_item(self.listbyconnector())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.connector_mappings.get(resource_group_name=self.resource_group_name,
                                                               hub_name=self.hub_name,
                                                               connector_name=self.connector_name,
                                                               mapping_name=self.mapping_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyconnector(self):
        response = None

        try:
            response = self.mgmt_client.connector_mappings.list_by_connector(resource_group_name=self.resource_group_name,
                                                                             hub_name=self.hub_name,
                                                                             connector_name=self.connector_name)
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
    AzureRMConnectorMappingInfo()


if __name__ == '__main__':
    main()
