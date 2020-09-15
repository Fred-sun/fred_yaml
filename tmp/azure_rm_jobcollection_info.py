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
module: azure_rm_jobcollection_info
version_added: '2.9'
short_description: Get JobCollection info.
description:
  - Get info of JobCollection.
options:
  resource_group_name:
    description:
      - The resource group name.
    type: str
  job_collection_name:
    description:
      - The job collection name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
job_collections:
  description: >-
    A list of dict results where the key is the name of the JobCollection and
    the values are the facts for that JobCollection.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Gets the job collections.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Gets the job collection resource identifier.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Gets the job collection resource type.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Gets or sets the job collection resource name.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Gets or sets the storage account location.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Gets or sets the tags.
          returned: always
          type: dictionary
          sample: null
        state:
          description:
            - Gets or sets the state.
          returned: always
          type: sealed-choice
          sample: null
        max_job_count:
          description:
            - Gets or set the maximum job count.
          returned: always
          type: integer
          sample: null
        max_job_occurrence:
          description:
            - Gets or sets the maximum job occurrence.
          returned: always
          type: integer
          sample: null
        max_recurrence:
          description:
            - Gets or set the maximum recurrence.
          returned: always
          type: dict
          sample: null
          contains:
            frequency:
              description:
                - >-
                  Gets or sets the frequency of recurrence (second, minute,
                  hour, day, week, month).
              returned: always
              type: sealed-choice
              sample: null
            interval:
              description:
                - Gets or sets the interval between retries.
              returned: always
              type: integer
              sample: null
        name_properties_sku_name:
          description:
            - Gets or set the SKU.
          returned: always
          type: sealed-choice
          sample: null
    next_link:
      description:
        - Gets or sets the URL to get the next set of job collections.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Gets the job collection resource identifier.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Gets the job collection resource type.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Gets or sets the job collection resource name.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Gets or sets the storage account location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Gets or sets the tags.
      returned: always
      type: dictionary
      sample: null
    state:
      description:
        - Gets or sets the state.
      returned: always
      type: sealed-choice
      sample: null
    max_job_count:
      description:
        - Gets or set the maximum job count.
      returned: always
      type: integer
      sample: null
    max_job_occurrence:
      description:
        - Gets or sets the maximum job occurrence.
      returned: always
      type: integer
      sample: null
    max_recurrence:
      description:
        - Gets or set the maximum recurrence.
      returned: always
      type: dict
      sample: null
      contains:
        frequency:
          description:
            - >-
              Gets or sets the frequency of recurrence (second, minute, hour,
              day, week, month).
          returned: always
          type: sealed-choice
          sample: null
        interval:
          description:
            - Gets or sets the interval between retries.
          returned: always
          type: integer
          sample: null
    name_properties_sku_name:
      description:
        - Gets or set the SKU.
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.scheduler import SchedulerManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMJobCollectionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            job_collection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.job_collection_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMJobCollectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SchedulerManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-01')

        if (self.resource_group_name is not None and
            self.job_collection_name is not None):
            self.results['job_collections'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['job_collections'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['job_collections'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_collections.get(resource_group_name=self.resource_group_name,
                                                            job_collection_name=self.job_collection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.job_collections.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.job_collections.list_by_subscription()
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
    AzureRMJobCollectionInfo()


if __name__ == '__main__':
    main()
