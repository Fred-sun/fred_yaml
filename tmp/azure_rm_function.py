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
module: azure_rm_function
version_added: '2.9'
short_description: Manage Azure Function instance.
description:
  - 'Create, update and delete instance of Azure Function.'
options:
  if_match:
    description:
      - >-
        The ETag of the function. Omit this value to always overwrite the
        current function. Specify the last-seen ETag value to prevent
        accidentally overwriting concurrent changes.
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
  function_name:
    description:
      - The name of the function.
    required: true
    type: str
  name:
    description:
      - Resource name
    type: str
  properties:
    description:
      - The properties that are associated with a function.
    type: dict
    suboptions:
      type:
        description:
          - Indicates the type of function.
        required: true
        type: str
      etag:
        description:
          - >-
            The current entity tag for the function. This is an opaque string.
            You can use it to detect whether the resource has changed between
            requests. You can also use it in the If-Match or If-None-Match
            headers for write operations for optimistic concurrency.
        type: str
      inputs:
        description:
          - undefined
        type: list
        suboptions:
          data_type:
            description:
              - >-
                The (Azure Stream Analytics supported) data type of the function
                input parameter. A list of valid Azure Stream Analytics data
                types are described at
                https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
            type: str
          is_configuration_parameter:
            description:
              - >-
                A flag indicating if the parameter is a configuration parameter.
                True if this input parameter is expected to be a constant.
                Default is false.
            type: bool
      output:
        description:
          - Describes the output of a function.
        type: dict
        suboptions:
          data_type:
            description:
              - >-
                The (Azure Stream Analytics supported) data type of the function
                output. A list of valid Azure Stream Analytics data types are
                described at
                https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
            type: str
      binding:
        description:
          - >-
            The physical binding of the function. For example, in the Azure
            Machine Learning web service’s case, this describes the endpoint.
        type: dict
        suboptions:
          type:
            description:
              - Indicates the function binding type.
            required: true
            type: str
  state:
    description:
      - Assert the state of the Function.
      - >-
        Use C(present) to create or update an Function and C(absent) to delete
        it.
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
    - name: Update a JavaScript function
      azure_rm_function: 
        function_name: function8197
        job_name: sj8653
        resource_group_name: sjrg
        properties:
          type: Scalar
          properties:
            binding:
              type: Microsoft.StreamAnalytics/JavascriptUdf
              properties:
                script: 'function (a, b) { return a * b; }'
        

    - name: Update an Azure ML function
      azure_rm_function: 
        function_name: function588
        job_name: sj9093
        resource_group_name: sjrg
        properties:
          type: Scalar
          properties:
            binding:
              type: Microsoft.MachineLearning/WebService
              properties:
                batch_size: 5000
        

    - name: Delete a function
      azure_rm_function: 
        function_name: function8197
        job_name: sj8653
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
    - The properties that are associated with a function.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - Indicates the type of function.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          The current entity tag for the function. This is an opaque string. You
          can use it to detect whether the resource has changed between
          requests. You can also use it in the If-Match or If-None-Match headers
          for write operations for optimistic concurrency.
      returned: always
      type: str
      sample: null
    inputs:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        data_type:
          description:
            - >-
              The (Azure Stream Analytics supported) data type of the function
              input parameter. A list of valid Azure Stream Analytics data types
              are described at
              https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
          returned: always
          type: str
          sample: null
        is_configuration_parameter:
          description:
            - >-
              A flag indicating if the parameter is a configuration parameter.
              True if this input parameter is expected to be a constant. Default
              is false.
          returned: always
          type: bool
          sample: null
    output:
      description:
        - Describes the output of a function.
      returned: always
      type: dict
      sample: null
      contains:
        data_type:
          description:
            - >-
              The (Azure Stream Analytics supported) data type of the function
              output. A list of valid Azure Stream Analytics data types are
              described at
              https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
          returned: always
          type: str
          sample: null
    binding:
      description:
        - >-
          The physical binding of the function. For example, in the Azure
          Machine Learning web service’s case, this describes the endpoint.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - Indicates the function binding type.
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


class AzureRMFunction(AzureRMModuleBaseExt):
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
            function_name=dict(
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
                    etag=dict(
                        type='str',
                        updatable=False,
                        disposition='etag'
                    ),
                    inputs=dict(
                        type='list',
                        disposition='inputs',
                        elements='dict',
                        options=dict(
                            data_type=dict(
                                type='str',
                                disposition='data_type'
                            ),
                            is_configuration_parameter=dict(
                                type='bool',
                                disposition='is_configuration_parameter'
                            )
                        )
                    ),
                    output=dict(
                        type='dict',
                        disposition='output',
                        options=dict(
                            data_type=dict(
                                type='str',
                                disposition='data_type'
                            )
                        )
                    ),
                    binding=dict(
                        type='dict',
                        disposition='binding',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                required=True
                            )
                        )
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
        self.function_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFunction, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.functions.create()
            else:
                response = self.mgmt_client.functions.update(if_match=self.if_match,
                                                             resource_group_name=self.resource_group_name,
                                                             job_name=self.job_name,
                                                             function_name=self.function_name,
                                                             function=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Function instance.')
            self.fail('Error creating the Function instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.functions.delete(resource_group_name=self.resource_group_name,
                                                         job_name=self.job_name,
                                                         function_name=self.function_name)
        except CloudError as e:
            self.log('Error attempting to delete the Function instance.')
            self.fail('Error deleting the Function instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.functions.get(resource_group_name=self.resource_group_name,
                                                      job_name=self.job_name,
                                                      function_name=self.function_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFunction()


if __name__ == '__main__':
    main()
