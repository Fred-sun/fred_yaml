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
module: azure_rm_artifact_info
version_added: '2.9'
short_description: Get Artifact info.
description:
  - Get info of Artifact.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  artifact_source_name:
    description:
      - The name of the artifact source.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=title)'''
    required: true
    type: str
  filter:
    description:
      - >-
        The filter to apply to the operation. Example:
        '$filter=contains(name,'myName')
    type: str
  top:
    description:
      - >-
        The maximum number of resources to return from the operation. Example:
        '$top=10'
    type: integer
  orderby:
    description:
      - >-
        The ordering expression for the results, using OData notation. Example:
        '$orderby=name desc'
    type: str
  name:
    description:
      - The name of the artifact.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
artifacts:
  description: >-
    A list of dict results where the key is the name of the Artifact and the
    values are the facts for that Artifact.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        title:
          description:
            - The artifact's title.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The artifact's description.
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - The artifact's publisher.
          returned: always
          type: str
          sample: null
        file_path:
          description:
            - The file path to the artifact.
          returned: always
          type: str
          sample: null
        icon:
          description:
            - The URI to the artifact icon.
          returned: always
          type: str
          sample: null
        target_os_type:
          description:
            - The artifact's target OS.
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - The artifact's parameters.
          returned: always
          type: any
          sample: null
        created_date:
          description:
            - The artifact's creation date.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link for next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The identifier of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    title:
      description:
        - The artifact's title.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The artifact's description.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - The artifact's publisher.
      returned: always
      type: str
      sample: null
    file_path:
      description:
        - The file path to the artifact.
      returned: always
      type: str
      sample: null
    icon:
      description:
        - The URI to the artifact icon.
      returned: always
      type: str
      sample: null
    target_os_type:
      description:
        - The artifact's target OS.
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - The artifact's parameters.
      returned: always
      type: any
      sample: null
    created_date:
      description:
        - The artifact's creation date.
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMArtifactInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            artifact_source_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.artifact_source_name = None
        self.expand = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMArtifactInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

        if (self.resource_group_name is not None and
            self.lab_name is not None and
            self.artifact_source_name is not None and
            self.name is not None):
            self.results['artifacts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_name is not None and
              self.artifact_source_name is not None):
            self.results['artifacts'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.artifacts.get(resource_group_name=self.resource_group_name,
                                                      lab_name=self.lab_name,
                                                      artifact_source_name=self.artifact_source_name,
                                                      name=self.name,
                                                      expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.artifacts.list(resource_group_name=self.resource_group_name,
                                                       lab_name=self.lab_name,
                                                       artifact_source_name=self.artifact_source_name,
                                                       expand=self.expand,
                                                       filter=self.filter,
                                                       top=self.top,
                                                       orderby=self.orderby)
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
    AzureRMArtifactInfo()


if __name__ == '__main__':
    main()
