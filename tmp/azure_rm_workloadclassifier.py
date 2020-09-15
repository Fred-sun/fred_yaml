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
module: azure_rm_workloadclassifier
version_added: '2.9'
short_description: Manage Azure WorkloadClassifier instance.
description:
  - 'Create, update and delete instance of Azure WorkloadClassifier.'
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
    required: true
    type: str
  workload_classifier_name:
    description:
      - The name of the workload classifier.
      - The name of the workload classifier to create/update.
      - The name of the workload classifier to delete.
    required: true
    type: str
  member_name:
    description:
      - The workload classifier member name.
    type: str
  label:
    description:
      - The workload classifier label.
    type: str
  context:
    description:
      - The workload classifier context.
    type: str
  start_time:
    description:
      - The workload classifier start time for classification.
    type: str
  end_time:
    description:
      - The workload classifier end time for classification.
    type: str
  importance:
    description:
      - The workload classifier importance.
    type: str
  state:
    description:
      - Assert the state of the WorkloadClassifier.
      - >-
        Use C(present) to create or update an WorkloadClassifier and C(absent)
        to delete it.
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
    - name: Create a workload group with all properties specified.
      azure_rm_workloadclassifier: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_classifier_name: wlm_workloadclassifier
        workload_group_name: wlm_workloadgroup
        properties:
          context: test_context
          end_time: '14:00'
          importance: high
          label: test_label
          member_name: dbo
          start_time: '12:00'
        

    - name: Create a workload group with the required properties specified.
      azure_rm_workloadclassifier: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_classifier_name: wlm_workloadclassifier
        workload_group_name: wlm_workloadgroup
        properties:
          member_name: dbo
        

    - name: Delete a workload classifier
      azure_rm_workloadclassifier: 
        database_name: testdb
        resource_group_name: Default-SQL-SouthEastAsia
        server_name: testsvr
        workload_classifier_name: wlm_workloadclassifier
        workload_group_name: wlm_workloadgroup
        

'''

RETURN = '''
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMWorkloadClassifier(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            member_name=dict(
                type='str',
                disposition='/member_name'
            ),
            label=dict(
                type='str',
                disposition='/label'
            ),
            context=dict(
                type='str',
                disposition='/context'
            ),
            start_time=dict(
                type='str',
                disposition='/start_time'
            ),
            end_time=dict(
                type='str',
                disposition='/end_time'
            ),
            importance=dict(
                type='str',
                disposition='/importance'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.workload_group_name = None
        self.workload_classifier_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMWorkloadClassifier, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01-preview')

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
            response = self.mgmt_client.workload_classifiers.create_or_update(resource_group_name=self.resource_group_name,
                                                                              server_name=self.server_name,
                                                                              database_name=self.database_name,
                                                                              workload_group_name=self.workload_group_name,
                                                                              workload_classifier_name=self.workload_classifier_name,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the WorkloadClassifier instance.')
            self.fail('Error creating the WorkloadClassifier instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.workload_classifiers.delete(resource_group_name=self.resource_group_name,
                                                                    server_name=self.server_name,
                                                                    database_name=self.database_name,
                                                                    workload_group_name=self.workload_group_name,
                                                                    workload_classifier_name=self.workload_classifier_name)
        except CloudError as e:
            self.log('Error attempting to delete the WorkloadClassifier instance.')
            self.fail('Error deleting the WorkloadClassifier instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.workload_classifiers.get(resource_group_name=self.resource_group_name,
                                                                 server_name=self.server_name,
                                                                 database_name=self.database_name,
                                                                 workload_group_name=self.workload_group_name,
                                                                 workload_classifier_name=self.workload_classifier_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMWorkloadClassifier()


if __name__ == '__main__':
    main()
