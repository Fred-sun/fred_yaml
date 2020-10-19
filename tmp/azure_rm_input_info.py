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
module: azure_rm_input_info
version_added: '2.9'
short_description: Get Input info.
description:
  - Get info of Input.
options:
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
    type: str
  select:
    description:
      - >-
        The $select OData query parameter. This is a comma-separated list of
        structural properties to include in the response, or "*" to include all
        properties. By default, all properties are returned except diagnostics.
        Currently only accepts '*' as a valid value.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a reference blob input with CSV serialization
      azure_rm_input_info: 
        input_name: input7225
        job_name: sj9597
        resource_group_name: sjrg
        

    - name: Get a stream Event Hub input with JSON serialization
      azure_rm_input_info: 
        input_name: input7425
        job_name: sj197
        resource_group_name: sjrg
        

    - name: Get a stream IoT Hub input with Avro serialization
      azure_rm_input_info: 
        input_name: input7970
        job_name: sj9742
        resource_group_name: sjrg
        

    - name: Get a stream blob input with CSV serialization
      azure_rm_input_info: 
        input_name: input8899
        job_name: sj6695
        resource_group_name: sjrg
        

    - name: List all inputs in a streaming job
      azure_rm_input_info: 
        job_name: sj9597
        resource_group_name: sjrg
        

    - name: List all inputs in a streaming job and include diagnostic information using the $select OData query parameter
      azure_rm_input_info: 
        job_name: sj7804
        resource_group_name: sjrg
        

'''

RETURN = '''
inputs:
  description: >-
    A list of dict results where the key is the name of the Input and the values
    are the facts for that Input.
  returned: always
  type: complex
  contains:
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
              Indicates whether the input is a source of reference data or
              stream data. Required on PUT (CreateOrReplace) requests.
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
                  Indicates the type of serialization that the input or output
                  uses. Required on PUT (CreateOrReplace) requests.
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
                  resource, or to the job overall, that warrant customer
                  attention.
              returned: always
              type: list
              sample: null
              contains:
                since:
                  description:
                    - >-
                      The UTC timestamp of when the condition started. Customers
                      should be able to find a corresponding event in the ops
                      log around this time.
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
                      The human-readable message describing the condition in
                      detail. Localized in the Accept-Language of the client
                      request.
                  returned: always
                  type: str
                  sample: null
        etag:
          description:
            - >-
              The current entity tag for the input. This is an opaque string.
              You can use it to detect whether the resource has changed between
              requests. You can also use it in the If-Match or If-None-Match
              headers for write operations for optimistic concurrency.
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
    value:
      description:
        - >-
          A list of inputs under a streaming job. Populated by a 'List'
          operation.
      returned: always
      type: list
      sample: null
      contains:
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
                  Indicates whether the input is a source of reference data or
                  stream data. Required on PUT (CreateOrReplace) requests.
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
                      Indicates the type of serialization that the input or
                      output uses. Required on PUT (CreateOrReplace) requests.
                  returned: always
                  type: str
                  sample: null
            diagnostics:
              description:
                - >-
                  Describes conditions applicable to the Input, Output, or the
                  job overall, that warrant customer attention.
              returned: always
              type: dict
              sample: null
              contains:
                conditions:
                  description:
                    - >-
                      A collection of zero or more conditions applicable to the
                      resource, or to the job overall, that warrant customer
                      attention.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    since:
                      description:
                        - >-
                          The UTC timestamp of when the condition started.
                          Customers should be able to find a corresponding event
                          in the ops log around this time.
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
                          The human-readable message describing the condition in
                          detail. Localized in the Accept-Language of the client
                          request.
                      returned: always
                      type: str
                      sample: null
            etag:
              description:
                - >-
                  The current entity tag for the input. This is an opaque
                  string. You can use it to detect whether the resource has
                  changed between requests. You can also use it in the If-Match
                  or If-None-Match headers for write operations for optimistic
                  concurrency.
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
                  partitionKey Describes a key in the input data which is used
                  for partitioning the input data
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - The link (url) to the next page of results.
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
    from azure.mgmt.stream import Stream Analytics Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMInputInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            job_name=dict(
                type='str',
                required=True
            ),
            input_name=dict(
                type='str'
            ),
            select=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.job_name = None
        self.input_name = None
        self.select = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMInputInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Stream Analytics Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01-preview')

        if (self.resource_group_name is not None and
            self.job_name is not None and
            self.input_name is not None):
            self.results['inputs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.job_name is not None):
            self.results['inputs'] = self.format_item(self.listbystreamingjob())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.inputs.get(resource_group_name=self.resource_group_name,
                                                   job_name=self.job_name,
                                                   input_name=self.input_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbystreamingjob(self):
        response = None

        try:
            response = self.mgmt_client.inputs.list_by_streaming_job(select=self.select,
                                                                     resource_group_name=self.resource_group_name,
                                                                     job_name=self.job_name)
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
    AzureRMInputInfo()


if __name__ == '__main__':
    main()
