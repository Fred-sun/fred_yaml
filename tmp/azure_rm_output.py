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
module: azure_rm_output
version_added: '2.9'
short_description: Manage Azure Output instance.
description:
  - 'Create, update and delete instance of Azure Output.'
options:
  if_match:
    description:
      - >-
        The ETag of the output. Omit this value to always overwrite the current
        output. Specify the last-seen ETag value to prevent accidentally
        overwriting concurrent changes.
    type: str
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  job_name:
    description:
      - The name of the streaming job.
    required: true
    type: str
  output_name:
    description:
      - The name of the output.
    required: true
    type: str
  name:
    description:
      - Resource name
    type: str
  datasource:
    description:
      - >-
        Describes the data source that output will be written to. Required on
        PUT (CreateOrReplace) requests.
    type: dict
    suboptions:
      type:
        description:
          - >-
            Indicates the type of data source output will be written to.
            Required on PUT (CreateOrReplace) requests.
        required: true
        type: str
  time_window:
    description:
      - undefined
    type: str
  size_window:
    description:
      - undefined
    type: number
  serialization:
    description:
      - >-
        Describes how data from an input is serialized or how data is serialized
        when written to an output. Required on PUT (CreateOrReplace) requests.
    type: dict
    suboptions:
      type:
        description:
          - >-
            Indicates the type of serialization that the input or output uses.
            Required on PUT (CreateOrReplace) requests.
        required: true
        type: str
        choices:
          - Csv
          - Avro
          - Json
          - CustomClr
          - Parquet
  state:
    description:
      - Assert the state of the Output.
      - Use C(present) to create or update an Output and C(absent) to delete it.
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
    - name: Update a DocumentDB output
      azure_rm_output: 
        job_name: sj2331
        output_name: output3022
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.Storage/DocumentDB
            properties:
              partition_key: differentPartitionKey
        

    - name: Update a Power BI output
      azure_rm_output: 
        job_name: sj2331
        output_name: output3022
        resource_group_name: sjrg
        properties:
          datasource:
            type: PowerBI
            properties:
              dataset: differentDataset
        

    - name: Update a Service Bus Queue output with Avro serialization
      azure_rm_output: 
        job_name: sj5095
        output_name: output3456
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.ServiceBus/Queue
            properties:
              queue_name: differentQueueName
          serialization:
            type: Json
            properties:
              format: LineSeparated
              encoding: UTF8
        

    - name: Update a Service Bus Topic output with CSV serialization
      azure_rm_output: 
        job_name: sj7094
        output_name: output7886
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.ServiceBus/Topic
            properties:
              topic_name: differentTopicName
          serialization:
            type: Csv
            properties:
              encoding: UTF8
              field_delimiter: '|'
        

    - name: Update a blob output with CSV serialization
      azure_rm_output: 
        job_name: sj900
        output_name: output1623
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.Storage/Blob
            properties:
              container: differentContainer
          serialization:
            type: Csv
            properties:
              encoding: UTF8
              field_delimiter: '|'
        

    - name: Update an Azure Data Lake Store output with JSON serialization
      azure_rm_output: 
        job_name: sj3310
        output_name: output5195
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.DataLake/Accounts
            properties:
              account_name: differentaccount
          serialization:
            type: Json
            properties:
              format: LineSeparated
              encoding: UTF8
        

    - name: Update an Azure SQL database output
      azure_rm_output: 
        job_name: sj6458
        output_name: output1755
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.Sql/Server/Database
            properties:
              table: differentTable
        

    - name: Update an Azure Table output
      azure_rm_output: 
        job_name: sj2790
        output_name: output958
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.Storage/Table
            properties:
              partition_key: differentPartitionKey
        

    - name: Update an Event Hub output with JSON serialization
      azure_rm_output: 
        job_name: sj3310
        output_name: output5195
        resource_group_name: sjrg
        properties:
          datasource:
            type: Microsoft.ServiceBus/EventHub
            properties:
              partition_key: differentPartitionKey
          serialization:
            type: Json
            properties:
              format: LineSeparated
              encoding: UTF8
        

    - name: Delete an output
      azure_rm_output: 
        job_name: sj6458
        output_name: output1755
        resource_group_name: sjrg
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
datasource:
  description:
    - >-
      Describes the data source that output will be written to. Required on PUT
      (CreateOrReplace) requests.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - >-
          Indicates the type of data source output will be written to. Required
          on PUT (CreateOrReplace) requests.
      returned: always
      type: str
      sample: null
time_window:
  description:
    - ''
  returned: always
  type: str
  sample: null
size_window:
  description:
    - ''
  returned: always
  type: number
  sample: null
serialization:
  description:
    - >-
      Describes how data from an input is serialized or how data is serialized
      when written to an output. Required on PUT (CreateOrReplace) requests.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - >-
          Indicates the type of serialization that the input or output uses.
          Required on PUT (CreateOrReplace) requests.
      returned: always
      type: str
      sample: null
diagnostics:
  description:
    - >-
      Describes conditions applicable to the Input, Output, or the job overall,
      that warrant customer attention.
  returned: always
  type: dict
  sample: null
  contains:
    conditions:
      description:
        - >-
          A collection of zero or more conditions applicable to the resource, or
          to the job overall, that warrant customer attention.
      returned: always
      type: list
      sample: null
      contains:
        since:
          description:
            - >-
              The UTC timestamp of when the condition started. Customers should
              be able to find a corresponding event in the ops log around this
              time.
          returned: always
          type: str
          sample: null
        code:
          description:
            - The opaque diagnostic code.
          returned: always
          type: str
          sample: null
        message:
          description:
            - >-
              The human-readable message describing the condition in detail.
              Localized in the Accept-Language of the client request.
          returned: always
          type: str
          sample: null
etag:
  description:
    - >-
      The current entity tag for the output. This is an opaque string. You can
      use it to detect whether the resource has changed between requests. You
      can also use it in the If-Match or If-None-Match headers for write
      operations for optimistic concurrency.
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
    from azure.mgmt.stream import Stream Analytics Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOutput(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            if_match=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            job_name=dict(
                type='str',
                required=True
            ),
            output_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            datasource=dict(
                type='dict',
                disposition='/datasource',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        required=True
                    )
                )
            ),
            time_window=dict(
                type='str',
                disposition='/time_window'
            ),
            size_window=dict(
                type='number',
                disposition='/size_window'
            ),
            serialization=dict(
                type='dict',
                disposition='/serialization',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['Csv',
                                 'Avro',
                                 'Json',
                                 'CustomClr',
                                 'Parquet'],
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

        self.if_match = None
        self.resource_group_name = None
        self.job_name = None
        self.output_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOutput, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Stream Analytics Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.outputs.create()
            else:
                response = self.mgmt_client.outputs.update(if_match=self.if_match,
                                                           resource_group_name=self.resource_group_name,
                                                           job_name=self.job_name,
                                                           output_name=self.output_name,
                                                           output=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Output instance.')
            self.fail('Error creating the Output instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.outputs.delete(resource_group_name=self.resource_group_name,
                                                       job_name=self.job_name,
                                                       output_name=self.output_name)
        except CloudError as e:
            self.log('Error attempting to delete the Output instance.')
            self.fail('Error deleting the Output instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.outputs.get(resource_group_name=self.resource_group_name,
                                                    job_name=self.job_name,
                                                    output_name=self.output_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOutput()


if __name__ == '__main__':
    main()
