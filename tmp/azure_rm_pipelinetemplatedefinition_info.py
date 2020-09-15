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
module: azure_rm_pipelinetemplatedefinition_info
version_added: '2.9'
short_description: Get PipelineTemplateDefinition info.
description:
  - Get info of PipelineTemplateDefinition.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get the list of pipeline template definitions
      azure_rm_pipelinetemplatedefinition_info: 
        {}
        

'''

RETURN = '''
pipeline_template_definitions:
  description: >-
    A list of dict results where the key is the name of the
    PipelineTemplateDefinition and the values are the facts for that
    PipelineTemplateDefinition.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of pipeline template definitions.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Unique identifier of the pipeline template.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Description of the pipeline enabled by the template.
          returned: always
          type: str
          sample: null
        inputs:
          description:
            - >-
              List of input parameters required by the template to create a
              pipeline.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Identifier of the input parameter.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Description of the input parameter.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Data type of the value of the input parameter.
              returned: always
              type: str
              sample: null
            possible_values:
              description:
                - List of possible values for the input parameter.
              returned: always
              type: list
              sample: null
              contains:
                value:
                  description:
                    - Value of an input parameter.
                  returned: always
                  type: str
                  sample: null
                display_value:
                  description:
                    - Description of the input parameter value.
                  returned: always
                  type: str
                  sample: null
    next_link:
      description:
        - >-
          The URL to get the next set of pipeline template definitions, if there
          are any.
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
    from azure.mgmt.azure import Azure DevOps
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPipelineTemplateDefinitionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPipelineTemplateDefinitionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure DevOps,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-01-preview')

        else:
            self.results['pipeline_template_definitions'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.pipeline_template_definitions.list()
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
    AzureRMPipelineTemplateDefinitionInfo()


if __name__ == '__main__':
    main()
