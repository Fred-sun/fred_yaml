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
module: azure_rm_input
version_added: '2.9'
short_description: Manage Azure Input instance.
description:
  - 'Create, update and delete instance of Azure Input.'
options:
  if_match:
    description:
      - >-
        The ETag of the input. Omit this value to always overwrite the current
        input. Specify the last-seen ETag value to prevent accidentally
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
  input_name:
    description:
      - The name of the input.
    required: true
    type: str
  name:
    description:
      - Resource name
    type: str
  properties:
    description:
      - >-
        The properties that are associated with an input. Required on PUT
        (CreateOrReplace) requests.
    type: dict
    suboptions:
      type:
        description:
          - >-
            Indicates whether the input is a source of reference data or stream
            data. Required on PUT (CreateOrReplace) requests.
        required: true
        type: str
      serialization:
        description:
          - >-
            Describes how data from an input is serialized or how data is
            serialized when written to an output. Required on PUT
            (CreateOrReplace) requests.
        type: dict
        suboptions:
          type:
            description:
              - >-
                Indicates the type of serialization that the input or output
                uses. Required on PUT (CreateOrReplace) requests.
            required: true
            type: str
            choices:
              - Csv
              - Avro
              - Json
              - CustomClr
              - Parquet
      diagnostics:
        description:
          - >-
            Describes conditions applicable to the Input, Output, or the job
            overall, that warrant customer attention.
        type: dict
        suboptions:
          conditions:
            description:
              - >-
                A collection of zero or more conditions applicable to the
                resource, or to the job overall, that warrant customer
                attention.
            type: list
            suboptions:
              since:
                description:
                  - >-
                    The UTC timestamp of when the condition started. Customers
                    should be able to find a corresponding event in the ops log
                    around this time.
                type: str
              code:
                description:
                  - The opaque diagnostic code.
                type: str
              message:
                description:
                  - >-
                    The human-readable message describing the condition in
                    detail. Localized in the Accept-Language of the client
                    request.
                type: str
      etag:
        description:
          - >-
            The current entity tag for the input. This is an opaque string. You
            can use it to detect whether the resource has changed between
            requests. You can also use it in the If-Match or If-None-Match
            headers for write operations for optimistic concurrency.
        type: str
      compression:
        description:
          - Describes how input data is compressed
        type: dict
        suboptions:
          type:
            description:
              - undefined
            required: true
            type: str
      partition_key:
        description:
          - >-
            partitionKey Describes a key in the input data which is used for
            partitioning the input data
        type: str
  state:
    description:
      - Assert the state of the Input.
      - Use C(present) to create or update an Input and C(absent) to delete it.
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
    - name: Update a reference blob input
      azure_rm_input: 
        input_name: input7225
        job_name: sj9597
        resource_group_name: sjrg
        properties:
          type: Reference
          datasource:
            type: Microsoft.Storage/Blob
            properties:
              container: differentContainer
          serialization:
            type: Csv
            properties:
              encoding: UTF8
              field_delimiter: '|'
        

    - name: Update a stream Event Hub input
      azure_rm_input: 
        input_name: input7425
        job_name: sj197
        resource_group_name: sjrg
        properties:
          type: Stream
          datasource:
            type: Microsoft.ServiceBus/EventHub
            properties:
              consumer_group_name: differentConsumerGroupName
          serialization:
            type: Avro
        

    - name: Update a stream IoT Hub input
      azure_rm_input: 
        input_name: input7970
        job_name: sj9742
        resource_group_name: sjrg
        properties:
          type: Stream
          datasource:
            type: Microsoft.Devices/IotHubs
            properties:
              endpoint: messages/operationsMonitoringEvents
          serialization:
            type: Csv
            properties:
              encoding: UTF8
              field_delimiter: '|'
        

    - name: Update a stream blob input
      azure_rm_input: 
        input_name: input8899
        job_name: sj6695
        resource_group_name: sjrg
        properties:
          type: Stream
          datasource:
            type: Microsoft.Storage/Blob
            properties:
              source_partition_count: 32
          serialization:
            type: Csv
            properties:
              encoding: UTF8
              field_delimiter: '|'
        

    - name: Delete an input
      azure_rm_input: 
        input_name: input7225
        job_name: sj9597
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
properties:
  description:
    - >-
      The properties that are associated with an input. Required on PUT
      (CreateOrReplace) requests.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - >-
          Indicates whether the input is a source of reference data or stream
          data. Required on PUT (CreateOrReplace) requests.
      returned: always
      type: str
      sample: null
    serialization:
      description:
        - >-
          Describes how data from an input is serialized or how data is
          serialized when written to an output. Required on PUT
          (CreateOrReplace) requests.
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
          Describes conditions applicable to the Input, Output, or the job
          overall, that warrant customer attention.
      returned: always
      type: dict
      sample: null
      contains:
        conditions:
          description:
            - >-
              A collection of zero or more conditions applicable to the
              resource, or to the job overall, that warrant customer attention.
          returned: always
          type: list
          sample: null
          contains:
            since:
              description:
                - >-
                  The UTC timestamp of when the condition started. Customers
                  should be able to find a corresponding event in the ops log
                  around this time.
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
          The current entity tag for the input. This is an opaque string. You
          can use it to detect whether the resource has changed between
          requests. You can also use it in the If-Match or If-None-Match headers
          for write operations for optimistic concurrency.
      returned: always
      type: str
      sample: null
    compression:
      description:
        - Describes how input data is compressed
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - ''
          returned: always
          type: str
          sample: null
    partition_key:
      description:
        - >-
          partitionKey Describes a key in the input data which is used for
          partitioning the input data
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


class AzureRMInput(AzureRMModuleBaseExt):
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
            input_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        required=True
                    ),
                    serialization=dict(
                        type='dict',
                        disposition='serialization',
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
                    diagnostics=dict(
                        type='dict',
                        updatable=False,
                        disposition='diagnostics',
                        options=dict(
                            conditions=dict(
                                type='list',
                                updatable=False,
                                disposition='conditions',
                                elements='dict',
                                options=dict(
                                    since=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='since'
                                    ),
                                    code=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='code'
                                    ),
                                    message=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='message'
                                    )
                                )
                            )
                        )
                    ),
                    etag=dict(
                        type='str',
                        updatable=False,
                        disposition='etag'
                    ),
                    compression=dict(
                        type='dict',
                        disposition='compression',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                required=True
                            )
                        )
                    ),
                    partition_key=dict(
                        type='str',
                        disposition='partition_key'
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
        self.input_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMInput, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.inputs.create()
            else:
                response = self.mgmt_client.inputs.update(if_match=self.if_match,
                                                          resource_group_name=self.resource_group_name,
                                                          job_name=self.job_name,
                                                          input_name=self.input_name,
                                                          input=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Input instance.')
            self.fail('Error creating the Input instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.inputs.delete(resource_group_name=self.resource_group_name,
                                                      job_name=self.job_name,
                                                      input_name=self.input_name)
        except CloudError as e:
            self.log('Error attempting to delete the Input instance.')
            self.fail('Error deleting the Input instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.inputs.get(resource_group_name=self.resource_group_name,
                                                   job_name=self.job_name,
                                                   input_name=self.input_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMInput()


if __name__ == '__main__':
    main()
