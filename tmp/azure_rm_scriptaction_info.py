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
module: azure_rm_scriptaction_info
version_added: '2.9'
short_description: Get ScriptAction info.
description:
  - Get info of ScriptAction.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the cluster.
    required: true
    type: str
  script_execution_id:
    description:
      - The script execution Id
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all persisted script actions for the given cluster
      azure_rm_scriptaction_info: 
        cluster_name: cluster1
        resource_group_name: rg1
        

    - name: Get script execution history by script id
      azure_rm_scriptaction_info: 
        cluster_name: cluster1
        resource_group_name: rg1
        script_execution_id: '391145124054712'
        

'''

RETURN = '''
script_actions:
  description: >-
    A list of dict results where the key is the name of the ScriptAction and the
    values are the facts for that ScriptAction.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of persisted script action details for the cluster.
      returned: always
      type: list
      sample: null
      contains:
        script_execution_id:
          description:
            - The execution id of the script action.
          returned: always
          type: integer
          sample: null
        start_time:
          description:
            - The start time of script action execution.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - The end time of script action execution.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The current execution status of the script action.
          returned: always
          type: str
          sample: null
        operation:
          description:
            - The reason why the script action was executed.
          returned: always
          type: str
          sample: null
        execution_summary:
          description:
            - The summary of script action execution result.
          returned: always
          type: list
          sample: null
          contains:
            status:
              description:
                - The status of script action execution.
              returned: always
              type: str
              sample: null
            instance_count:
              description:
                - The instance count for a given script action execution status.
              returned: always
              type: integer
              sample: null
        debug_information:
          description:
            - The script action execution debug information.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The link (url) to the next page of results.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the script action.
      returned: always
      type: str
      sample: null
    uri:
      description:
        - The URI to the script.
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - The parameters for the script
      returned: always
      type: str
      sample: null
    roles:
      description:
        - The list of roles where script will be executed.
      returned: always
      type: list
      sample: null
    application_name:
      description:
        - 'The application name of the script action, if any.'
      returned: always
      type: str
      sample: null
    script_execution_id:
      description:
        - The execution id of the script action.
      returned: always
      type: integer
      sample: null
    start_time:
      description:
        - The start time of script action execution.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - The end time of script action execution.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The current execution status of the script action.
      returned: always
      type: str
      sample: null
    operation:
      description:
        - The reason why the script action was executed.
      returned: always
      type: str
      sample: null
    execution_summary:
      description:
        - The summary of script action execution result.
      returned: always
      type: list
      sample: null
      contains:
        status:
          description:
            - The status of script action execution.
          returned: always
          type: str
          sample: null
        instance_count:
          description:
            - The instance count for a given script action execution status.
          returned: always
          type: integer
          sample: null
    debug_information:
      description:
        - The script action execution debug information.
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
    from azure.mgmt.hdinsight import HDInsightManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMScriptActionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            script_execution_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.script_execution_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-06-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMScriptActionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HDInsightManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-06-01-preview')

        if (self.resource_group_name is not None and
            self.cluster_name is not None and
            self.script_execution_id is not None):
            self.results['script_actions'] = self.format_item(self.getexecutiondetail())
        elif (self.resource_group_name is not None and
              self.cluster_name is not None):
            self.results['script_actions'] = self.format_item(self.listbycluster())
        return self.results

    def getexecutiondetail(self):
        response = None

        try:
            response = self.mgmt_client.script_actions.get_execution_detail(resource_group_name=self.resource_group_name,
                                                                            cluster_name=self.cluster_name,
                                                                            script_execution_id=self.script_execution_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbycluster(self):
        response = None

        try:
            response = self.mgmt_client.script_actions.list_by_cluster(resource_group_name=self.resource_group_name,
                                                                       cluster_name=self.cluster_name)
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
    AzureRMScriptActionInfo()


if __name__ == '__main__':
    main()
