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
module: azure_rm_function_info
version_added: '2.9'
short_description: Get Function info.
description:
  - Get info of Function.
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
  function_name:
    description:
      - The name of the function.
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
    - name: Get a JavaScript function
      azure_rm_function_info: 
        function_name: function8197
        job_name: sj8653
        resource_group_name: sjrg
        

    - name: Get an Azure ML function
      azure_rm_function_info: 
        function_name: function588
        job_name: sj9093
        resource_group_name: sjrg
        

    - name: List all functions in a streaming job
      azure_rm_function_info: 
        job_name: sj8653
        resource_group_name: sjrg
        

'''

RETURN = '''
functions:
  description: >-
    A list of dict results where the key is the name of the Function and the
    values are the facts for that Function.
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
              The current entity tag for the function. This is an opaque string.
              You can use it to detect whether the resource has changed between
              requests. You can also use it in the If-Match or If-None-Match
              headers for write operations for optimistic concurrency.
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
                  The (Azure Stream Analytics supported) data type of the
                  function input parameter. A list of valid Azure Stream
                  Analytics data types are described at
                  https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
              returned: always
              type: str
              sample: null
            is_configuration_parameter:
              description:
                - >-
                  A flag indicating if the parameter is a configuration
                  parameter. True if this input parameter is expected to be a
                  constant. Default is false.
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
                  The (Azure Stream Analytics supported) data type of the
                  function output. A list of valid Azure Stream Analytics data
                  types are described at
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
    value:
      description:
        - >-
          A list of functions under a streaming job. Populated by a 'List'
          operation.
      returned: always
      type: list
      sample: null
      contains:
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
                  The current entity tag for the function. This is an opaque
                  string. You can use it to detect whether the resource has
                  changed between requests. You can also use it in the If-Match
                  or If-None-Match headers for write operations for optimistic
                  concurrency.
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
                      The (Azure Stream Analytics supported) data type of the
                      function input parameter. A list of valid Azure Stream
                      Analytics data types are described at
                      https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                  returned: always
                  type: str
                  sample: null
                is_configuration_parameter:
                  description:
                    - >-
                      A flag indicating if the parameter is a configuration
                      parameter. True if this input parameter is expected to be
                      a constant. Default is false.
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
                      The (Azure Stream Analytics supported) data type of the
                      function output. A list of valid Azure Stream Analytics
                      data types are described at
                      https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                  returned: always
                  type: str
                  sample: null
            binding:
              description:
                - >-
                  The physical binding of the function. For example, in the
                  Azure Machine Learning web service’s case, this describes the
                  endpoint.
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


class AzureRMFunctionInfo(AzureRMModuleBase):
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
            function_name=dict(
                type='str'
            ),
            select=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.job_name = None
        self.function_name = None
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
        super(AzureRMFunctionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Stream Analytics Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01-preview')

        if (self.resource_group_name is not None and
            self.job_name is not None and
            self.function_name is not None):
            self.results['functions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.job_name is not None):
            self.results['functions'] = self.format_item(self.listbystreamingjob())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.functions.get(resource_group_name=self.resource_group_name,
                                                      job_name=self.job_name,
                                                      function_name=self.function_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbystreamingjob(self):
        response = None

        try:
            response = self.mgmt_client.functions.list_by_streaming_job(select=self.select,
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
    AzureRMFunctionInfo()


if __name__ == '__main__':
    main()
