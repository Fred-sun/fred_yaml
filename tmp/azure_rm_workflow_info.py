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
module: azure_rm_workflow_info
version_added: '2.9'
short_description: Get Workflow info.
description:
  - Get info of Workflow.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  storage_sync_service_name:
    description:
      - Name of Storage Sync Service resource.
    required: true
    type: str
  workflow_id:
    description:
      - workflow Id
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Workflows_ListByStorageSyncService
      azure_rm_workflow_info: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        

    - name: Workflows_Get
      azure_rm_workflow_info: 
        resource_group_name: SampleResourceGroup_1
        storage_sync_service_name: SampleStorageSyncService_1
        workflow_id: 828219ea-083e-48b5-89ea-8fd9991b2e75
        

'''

RETURN = '''
workflows:
  description: >-
    A list of dict results where the key is the name of the Workflow and the
    values are the facts for that Workflow.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Collection of workflow items.
      returned: always
      type: list
      sample: null
      contains:
        last_step_name:
          description:
            - last step name
          returned: always
          type: str
          sample: null
        status:
          description:
            - workflow status.
          returned: always
          type: str
          sample: null
        operation:
          description:
            - operation direction.
          returned: always
          type: str
          sample: null
        steps:
          description:
            - workflow steps
          returned: always
          type: str
          sample: null
        last_operation_id:
          description:
            - workflow last operation identifier.
          returned: always
          type: str
          sample: null
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    last_step_name:
      description:
        - last step name
      returned: always
      type: str
      sample: null
    status:
      description:
        - workflow status.
      returned: always
      type: str
      sample: null
    operation:
      description:
        - operation direction.
      returned: always
      type: str
      sample: null
    steps:
      description:
        - workflow steps
      returned: always
      type: str
      sample: null
    last_operation_id:
      description:
        - workflow last operation identifier.
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
    from azure.mgmt.microsoft import Microsoft Storage Sync
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWorkflowInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            storage_sync_service_name=dict(
                type='str',
                required=True
            ),
            workflow_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.storage_sync_service_name = None
        self.workflow_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWorkflowInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft Storage Sync,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.storage_sync_service_name is not None and
            self.workflow_id is not None):
            self.results['workflows'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.storage_sync_service_name is not None):
            self.results['workflows'] = self.format_item(self.listbystoragesyncservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.workflows.get(resource_group_name=self.resource_group_name,
                                                      storage_sync_service_name=self.storage_sync_service_name,
                                                      workflow_id=self.workflow_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbystoragesyncservice(self):
        response = None

        try:
            response = self.mgmt_client.workflows.list_by_storage_sync_service(resource_group_name=self.resource_group_name,
                                                                               storage_sync_service_name=self.storage_sync_service_name)
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
    AzureRMWorkflowInfo()


if __name__ == '__main__':
    main()
