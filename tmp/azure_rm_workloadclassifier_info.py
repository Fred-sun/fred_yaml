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
module: azure_rm_workloadclassifier_info
version_added: '2.9'
short_description: Get WorkloadClassifier info.
description:
  - Get info of WorkloadClassifier.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - The name of the database.
    required: true
    type: str
  workload_group_name:
    description:
      - >-
        The name of the workload group from which to receive the classifier
        from.
      - >-
        The name of the workload group from which to receive the classifiers
        from.
    required: true
    type: str
  workload_classifier_name:
    description:
      - The name of the workload classifier.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a workload classifier for a data warehouse
      azure_rm_workloadclassifier_info: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_classifier_name: wlm_classifier
        workload_group_name: wlm_workloadgroup
        

    - name: Get the list of workload classifiers for a workload group
      azure_rm_workloadclassifier_info: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_group_name: wlm_workloadgroup
        

'''

RETURN = '''
workload_classifiers:
  description: >-
    A list of dict results where the key is the name of the WorkloadClassifier
    and the values are the facts for that WorkloadClassifier.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    member_name:
      description:
        - The workload classifier member name.
      returned: always
      type: str
      sample: null
    label:
      description:
        - The workload classifier label.
      returned: always
      type: str
      sample: null
    context:
      description:
        - The workload classifier context.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - The workload classifier start time for classification.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - The workload classifier end time for classification.
      returned: always
      type: str
      sample: null
    importance:
      description:
        - The workload classifier importance.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        member_name:
          description:
            - The workload classifier member name.
          returned: always
          type: str
          sample: null
        label:
          description:
            - The workload classifier label.
          returned: always
          type: str
          sample: null
        context:
          description:
            - The workload classifier context.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - The workload classifier start time for classification.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The workload classifier end time for classification.
          returned: always
          type: str
          sample: null
        importance:
          description:
            - The workload classifier importance.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWorkloadClassifierInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            workload_group_name=dict(
                type='str',
                required=True
            ),
            workload_classifier_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.workload_group_name = None
        self.workload_classifier_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWorkloadClassifierInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.workload_group_name is not None and
            self.workload_classifier_name is not None):
            self.results['workload_classifiers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.workload_group_name is not None):
            self.results['workload_classifiers'] = self.format_item(self.listbyworkloadgroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.workload_classifiers.get(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 database_name=self.database_name,
                                                                 workload_group_name=self.workload_group_name,
                                                                 workload_classifier_name=self.workload_classifier_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyworkloadgroup(self):
        response = None

        try:
            response = self.mgmt_client.workload_classifiers.list_by_workload_group(resource_group_name=self.resource_group_name,
                                                                                    server_name=self.server_name,
                                                                                    database_name=self.database_name,
                                                                                    workload_group_name=self.workload_group_name)
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
    AzureRMWorkloadClassifierInfo()


if __name__ == '__main__':
    main()
