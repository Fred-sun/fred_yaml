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
module: azure_rm_jobdefinition_info
version_added: '2.9'
short_description: Get JobDefinition info.
description:
  - Get info of JobDefinition.
options:
  data_service_name:
    description:
      - The data service type of interest.
      - The data service name of the job definition
    type: str
  resource_group_name:
    description:
      - The Resource Group Name
    required: true
    type: str
  data_manager_name:
    description:
      - >-
        The name of the DataManager Resource within the specified resource
        group. DataManager names must be between 3 and 24 characters in length
        and use any alphanumeric and underscore only
    required: true
    type: str
  filter:
    description:
      - OData Filter options
    type: str
  job_definition_name:
    description:
      - The job definition name that is being queried.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: JobDefinitions_ListByDataServiceGET71
      azure_rm_jobdefinition_info: 
        data_manager_name: TestAzureSDKOperations
        data_service_name: DataTransformation
        resource_group_name: ResourceGroupForSDKTest
        

    - name: JobDefinitions_GetGET81
      azure_rm_jobdefinition_info: 
        data_manager_name: TestAzureSDKOperations
        data_service_name: DataTransformation
        job_definition_name: jobdeffromtestcode1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: JobDefinitions_ListByDataManagerGET191
      azure_rm_jobdefinition_info: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
job_definitions:
  description: >-
    A list of dict results where the key is the name of the JobDefinition and
    the values are the facts for that JobDefinition.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of job definitions.
      returned: always
      type: list
      sample: null
      contains:
        data_source_id:
          description:
            - Data Source Id associated to the job definition.
          returned: always
          type: str
          sample: null
        data_sink_id:
          description:
            - Data Sink Id associated to the job definition.
          returned: always
          type: str
          sample: null
        schedules:
          description:
            - Schedule for running the job definition
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the schedule.
              returned: always
              type: str
              sample: null
            policy_list:
              description:
                - A list of repetition intervals in ISO 8601 format.
              returned: always
              type: list
              sample: null
        state:
          description:
            - State of the job definition.
          returned: always
          type: sealed-choice
          sample: null
        last_modified_time:
          description:
            - Last modified time of the job definition.
          returned: always
          type: str
          sample: null
        run_location:
          description:
            - This is the preferred geo location for the job to run.
          returned: always
          type: sealed-choice
          sample: null
        user_confirmation:
          description:
            - >-
              Enum to detect if user confirmation is required. If not passed
              will default to NotRequired.
          returned: always
          type: sealed-choice
          sample: null
        data_service_input:
          description:
            - A generic json used differently by each data service type.
          returned: always
          type: any
          sample: null
        customer_secrets:
          description:
            - >-
              List of customer secrets containing a key identifier and key
              value. The key identifier is a way for the specific data source to
              understand the key. Value contains customer secret encrypted by
              the encryptionKeys.
          returned: always
          type: list
          sample: null
          contains:
            key_identifier:
              description:
                - >-
                  The identifier to the data service input object which this
                  secret corresponds to.
              returned: always
              type: str
              sample: null
            key_value:
              description:
                - It contains the encrypted customer secret.
              returned: always
              type: str
              sample: null
            algorithm:
              description:
                - The encryption algorithm used to encrypt data.
              returned: always
              type: sealed-choice
              sample: null
    next_link:
      description:
        - Link for the next set of job definitions.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the object.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Id of the object.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the object.
      returned: always
      type: str
      sample: null
    data_source_id:
      description:
        - Data Source Id associated to the job definition.
      returned: always
      type: str
      sample: null
    data_sink_id:
      description:
        - Data Sink Id associated to the job definition.
      returned: always
      type: str
      sample: null
    schedules:
      description:
        - Schedule for running the job definition
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the schedule.
          returned: always
          type: str
          sample: null
        policy_list:
          description:
            - A list of repetition intervals in ISO 8601 format.
          returned: always
          type: list
          sample: null
    state:
      description:
        - State of the job definition.
      returned: always
      type: sealed-choice
      sample: null
    last_modified_time:
      description:
        - Last modified time of the job definition.
      returned: always
      type: str
      sample: null
    run_location:
      description:
        - This is the preferred geo location for the job to run.
      returned: always
      type: sealed-choice
      sample: null
    user_confirmation:
      description:
        - >-
          Enum to detect if user confirmation is required. If not passed will
          default to NotRequired.
      returned: always
      type: sealed-choice
      sample: null
    data_service_input:
      description:
        - A generic json used differently by each data service type.
      returned: always
      type: any
      sample: null
    customer_secrets:
      description:
        - >-
          List of customer secrets containing a key identifier and key value.
          The key identifier is a way for the specific data source to understand
          the key. Value contains customer secret encrypted by the
          encryptionKeys.
      returned: always
      type: list
      sample: null
      contains:
        key_identifier:
          description:
            - >-
              The identifier to the data service input object which this secret
              corresponds to.
          returned: always
          type: str
          sample: null
        key_value:
          description:
            - It contains the encrypted customer secret.
          returned: always
          type: str
          sample: null
        algorithm:
          description:
            - The encryption algorithm used to encrypt data.
          returned: always
          type: sealed-choice
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMJobDefinitionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            data_service_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            job_definition_name=dict(
                type='str'
            )
        )

        self.data_service_name = None
        self.resource_group_name = None
        self.data_manager_name = None
        self.filter = None
        self.job_definition_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMJobDefinitionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.data_service_name is not None and
            self.job_definition_name is not None and
            self.resource_group_name is not None and
            self.data_manager_name is not None):
            self.results['job_definitions'] = self.format_item(self.get())
        elif (self.data_service_name is not None and
              self.resource_group_name is not None and
              self.data_manager_name is not None):
            self.results['job_definitions'] = self.format_item(self.listbydataservice())
        elif (self.resource_group_name is not None and
              self.data_manager_name is not None):
            self.results['job_definitions'] = self.format_item(self.listbydatamanager())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_definitions.get(data_service_name=self.data_service_name,
                                                            job_definition_name=self.job_definition_name,
                                                            resource_group_name=self.resource_group_name,
                                                            data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydataservice(self):
        response = None

        try:
            response = self.mgmt_client.job_definitions.list_by_data_service(data_service_name=self.data_service_name,
                                                                             resource_group_name=self.resource_group_name,
                                                                             data_manager_name=self.data_manager_name,
                                                                             filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatamanager(self):
        response = None

        try:
            response = self.mgmt_client.job_definitions.list_by_data_manager(resource_group_name=self.resource_group_name,
                                                                             data_manager_name=self.data_manager_name,
                                                                             filter=self.filter)
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
    AzureRMJobDefinitionInfo()


if __name__ == '__main__':
    main()
