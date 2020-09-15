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
module: azure_rm_recommendationmetadata_info
version_added: '2.9'
short_description: Get RecommendationMetadata info.
description:
  - Get info of RecommendationMetadata.
options:
  name:
    description:
      - Name of metadata entity.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetMetadata
      azure_rm_recommendationmetadata_info: 
        name: types
        

'''

RETURN = '''
recommendation_metadata:
  description: >-
    A list of dict results where the key is the name of the
    RecommendationMetadata and the values are the facts for that
    RecommendationMetadata.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The resource Id of the metadata entity.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the metadata entity.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the metadata entity.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - The display name.
      returned: always
      type: str
      sample: null
    depends_on:
      description:
        - The list of keys on which this entity depends on.
      returned: always
      type: list
      sample: null
    applicable_scenarios:
      description:
        - The list of scenarios applicable to this metadata entity.
      returned: always
      type: list
      sample: null
    supported_values:
      description:
        - The list of supported values.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The id.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The display name.
          returned: always
          type: str
          sample: null
    value:
      description:
        - The list of metadata entities.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The resource Id of the metadata entity.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the metadata entity.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the metadata entity.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The display name.
          returned: always
          type: str
          sample: null
        depends_on:
          description:
            - The list of keys on which this entity depends on.
          returned: always
          type: list
          sample: null
        applicable_scenarios:
          description:
            - The list of scenarios applicable to this metadata entity.
          returned: always
          type: list
          sample: null
        supported_values:
          description:
            - The list of supported values.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - The id.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The display name.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - The link used to get the next page of metadata.
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
    from azure.mgmt.advisor import AdvisorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRecommendationMetadataInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str'
            )
        )

        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRecommendationMetadataInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AdvisorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.name is not None):
            self.results['recommendation_metadata'] = self.format_item(self.get())
        else:
            self.results['recommendation_metadata'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.recommendation_metadata.get(name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.recommendation_metadata.list()
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
    AzureRMRecommendationMetadataInfo()


if __name__ == '__main__':
    main()
