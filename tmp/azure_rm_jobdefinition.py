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
module: azure_rm_jobdefinition
version_added: '2.9'
short_description: Manage Azure JobDefinition instance.
description:
  - 'Create, update and delete instance of Azure JobDefinition.'
options:
  data_service_name:
    description:
      - The data service name of the job definition
      - The data service type of the job definition.
    required: true
    type: str
  job_definition_name:
    description:
      - The job definition name that is being queried.
      - The job definition name to be created or updated.
      - The job definition name to be deleted.
    required: true
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
  data_source_id:
    description:
      - Data Source Id associated to the job definition.
    type: str
  data_sink_id:
    description:
      - Data Sink Id associated to the job definition.
    type: str
  schedules:
    description:
      - Schedule for running the job definition
    type: list
    suboptions:
      name:
        description:
          - Name of the schedule.
        type: str
      policy_list:
        description:
          - A list of repetition intervals in ISO 8601 format.
        type: list
  state:
    description:
      - Assert the state of the JobDefinition.
      - >-
        Use C(present) to create or update an JobDefinition and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
  last_modified_time:
    description:
      - Last modified time of the job definition.
    type: str
  run_location:
    description:
      - This is the preferred geo location for the job to run.
    type: sealed-choice
  user_confirmation:
    description:
      - >-
        Enum to detect if user confirmation is required. If not passed will
        default to NotRequired.
    type: sealed-choice
  data_service_input:
    description:
      - A generic json used differently by each data service type.
    type: any
  customer_secrets:
    description:
      - >-
        List of customer secrets containing a key identifier and key value. The
        key identifier is a way for the specific data source to understand the
        key. Value contains customer secret encrypted by the encryptionKeys.
    type: list
    suboptions:
      key_identifier:
        description:
          - >-
            The identifier to the data service input object which this secret
            corresponds to.
        required: true
        type: str
      key_value:
        description:
          - It contains the encrypted customer secret.
        required: true
        type: str
      algorithm:
        description:
          - The encryption algorithm used to encrypt data.
        required: true
        type: sealed-choice
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: JobDefinitions_CreateOrUpdatePUT83
      azure_rm_jobdefinition: 
        data_manager_name: TestAzureSDKOperations
        data_service_name: DataTransformation
        job_definition_name: jobdeffromtestcode1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: JobDefinitions_DeleteDELETE81
      azure_rm_jobdefinition: 
        data_manager_name: TestAzureSDKOperations
        data_service_name: DataTransformation
        job_definition_name: jobdeffromtestcode1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
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
      List of customer secrets containing a key identifier and key value. The
      key identifier is a way for the specific data source to understand the
      key. Value contains customer secret encrypted by the encryptionKeys.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMJobDefinition(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            data_service_name=dict(
                type='str',
                required=True
            ),
            job_definition_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            data_source_id=dict(
                type='str',
                disposition='/data_source_id'
            ),
            data_sink_id=dict(
                type='str',
                disposition='/data_sink_id'
            ),
            schedules=dict(
                type='list',
                disposition='/schedules',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    policy_list=dict(
                        type='list',
                        disposition='policy_list',
                        elements='str'
                    )
                )
            ),
            state=dict(
                type='sealed-choice',
                disposition='/state'
            ),
            last_modified_time=dict(
                type='str',
                disposition='/last_modified_time'
            ),
            run_location=dict(
                type='sealed-choice',
                disposition='/run_location'
            ),
            user_confirmation=dict(
                type='sealed-choice',
                disposition='/user_confirmation'
            ),
            data_service_input=dict(
                type='any',
                disposition='/data_service_input'
            ),
            customer_secrets=dict(
                type='list',
                disposition='/customer_secrets',
                elements='dict',
                options=dict(
                    key_identifier=dict(
                        type='str',
                        disposition='key_identifier',
                        required=True
                    ),
                    key_value=dict(
                        type='str',
                        disposition='key_value',
                        required=True
                    ),
                    algorithm=dict(
                        type='sealed-choice',
                        disposition='algorithm',
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.data_service_name = None
        self.job_definition_name = None
        self.resource_group_name = None
        self.data_manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobDefinition, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

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
            response = self.mgmt_client.job_definitions.create_or_update(data_service_name=self.data_service_name,
                                                                         job_definition_name=self.job_definition_name,
                                                                         resource_group_name=self.resource_group_name,
                                                                         data_manager_name=self.data_manager_name,
                                                                         job_definition=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobDefinition instance.')
            self.fail('Error creating the JobDefinition instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.job_definitions.delete(data_service_name=self.data_service_name,
                                                               job_definition_name=self.job_definition_name,
                                                               resource_group_name=self.resource_group_name,
                                                               data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the JobDefinition instance.')
            self.fail('Error deleting the JobDefinition instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.job_definitions.get(data_service_name=self.data_service_name,
                                                            job_definition_name=self.job_definition_name,
                                                            resource_group_name=self.resource_group_name,
                                                            data_manager_name=self.data_manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobDefinition()


if __name__ == '__main__':
    main()
