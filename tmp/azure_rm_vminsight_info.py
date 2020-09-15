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
module: azure_rm_vminsight_info
version_added: '2.9'
short_description: Get VMInsight info.
description:
  - Get info of VMInsight.
options:
  resource_uri:
    description:
      - >-
        The fully qualified Azure Resource manager identifier of the resource,
        or scope, whose status to retrieve.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get status for a VM scale set that is actively reporting data
      azure_rm_vminsight_info: 
        resource_uri: >-
          subscriptions/3d51de47-8d1c-4d24-b42f-bcae075dfa87/resourceGroups/my-service-cluster/providers/Microsoft.Compute/virtualMachineScaleSets/scale-set-01
        

    - name: Get status for a VM that has not yet reported data
      azure_rm_vminsight_info: 
        resource_uri: >-
          subscriptions/3d51de47-8d1c-4d24-b42f-bcae075dfa87/resourceGroups/vm-resource-group/providers/Microsoft.Compute/virtualMachines/ubuntu-vm
        

    - name: Get status for a VM that is actively reporting data
      azure_rm_vminsight_info: 
        resource_uri: >-
          subscriptions/3d51de47-8d1c-4d24-b42f-bcae075dfa87/resourceGroups/vm-resource-group/providers/Microsoft.Compute/virtualMachines/ubuntu-vm
        

    - name: Get status for a resource group that has at least one VM that is actively reporting data
      azure_rm_vminsight_info: 
        resource_uri: >-
          subscriptions/3d51de47-8d1c-4d24-b42f-bcae075dfa87/resourceGroups/resource-group-with-vms
        

    - name: Get status for a subscription that has at least one VM that is actively reporting data
      azure_rm_vminsight_info: 
        resource_uri: subscriptions/3d51de47-8d1c-4d24-b42f-bcae075dfa87
        

'''

RETURN = '''
vminsights:
  description: >-
    A list of dict results where the key is the name of the VMInsight and the
    values are the facts for that VMInsight.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Azure resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Azure resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Azure resource type
      returned: always
      type: str
      sample: null
    resource_id:
      description:
        - >-
          Azure Resource Manager identifier of the resource whose onboarding
          status is being represented.
      returned: always
      type: str
      sample: null
    onboarding_status:
      description:
        - >-
          The onboarding status for the resource. Note that, a higher level
          scope, e.g., resource group or subscription, is considered onboarded
          if at least one resource under it is onboarded.
      returned: always
      type: str
      sample: null
    data_status:
      description:
        - >-
          The status of VM Insights data from the resource. When reported as
          `present` the data array will contain information about the data
          containers to which data for the specified resource is being routed.
      returned: always
      type: str
      sample: null
    data:
      description:
        - >-
          Containers that currently store VM Insights data for the specified
          resource.
      returned: always
      type: list
      sample: null
      contains:
        workspace:
          description:
            - Log Analytics workspace information.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - >-
                  Azure Resource Manager identifier of the Log Analytics
                  Workspace.
              returned: always
              type: str
              sample: null
            location:
              description:
                - Location of the Log Analytics workspace.
              returned: always
              type: str
              sample: null
            customer_id:
              description:
                - Log Analytics workspace identifier.
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
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVMInsightInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            )
        )

        self.resource_uri = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-11-27-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVMInsightInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-27-preview')

        if (self.resource_uri is not None):
            self.results['vminsights'] = self.format_item(self.getonboardingstatus())
        return self.results

    def getonboardingstatus(self):
        response = None

        try:
            response = self.mgmt_client.vminsights.get_onboarding_status(resource_uri=self.resource_uri)
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
    AzureRMVMInsightInfo()


if __name__ == '__main__':
    main()
