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
module: azure_rm_problemclassification_info
version_added: '2.9'
short_description: Get ProblemClassification info.
description:
  - Get info of ProblemClassification.
options:
  service_name:
    description:
      - >-
        Name of the Azure service for which the problem classifications need to
        be retrieved.
      - Name of the Azure service available for support.
    required: true
    type: str
  problem_classification_name:
    description:
      - Name of problem classification.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets list of problemClassifications for a service for which a support ticket can be created
      azure_rm_problemclassification_info: 
        service_name: service_guid
        

    - name: Gets details of problemClassification for Azure service
      azure_rm_problemclassification_info: 
        problem_classification_name: problemClassification_guid
        service_name: service_guid
        

'''

RETURN = '''
problem_classifications:
  description: >-
    A list of dict results where the key is the name of the
    ProblemClassification and the values are the facts for that
    ProblemClassification.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of ProblemClassification resources.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Id of the resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Name of the resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Type of the resource 'Microsoft.Support/problemClassification'.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - Localized name of problem classification.
          returned: always
          type: str
          sample: null
    id:
      description:
        - Id of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the resource 'Microsoft.Support/problemClassification'.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Localized name of problem classification.
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
    from azure.mgmt.microsoft.support import Microsoft.Support
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProblemClassificationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            service_name=dict(
                type='str',
                required=True
            ),
            problem_classification_name=dict(
                type='str'
            )
        )

        self.service_name = None
        self.problem_classification_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProblemClassificationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.Support,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.service_name is not None and
            self.problem_classification_name is not None):
            self.results['problem_classifications'] = self.format_item(self.get())
        elif (self.service_name is not None):
            self.results['problem_classifications'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.problem_classifications.get(service_name=self.service_name,
                                                                    problem_classification_name=self.problem_classification_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.problem_classifications.list(service_name=self.service_name)
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
    AzureRMProblemClassificationInfo()


if __name__ == '__main__':
    main()
