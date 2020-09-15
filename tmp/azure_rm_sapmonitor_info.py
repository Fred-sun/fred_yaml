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
module: azure_rm_sapmonitor_info
version_added: '2.9'
short_description: Get SapMonitor info.
description:
  - Get info of SapMonitor.
options:
  resource_group_name:
    description:
      - Name of the resource group.
    type: str
  sap_monitor_name:
    description:
      - Name of the SAP monitor resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all SAP Monitors in a subscription
      azure_rm_sapmonitor_info: 
        {}
        

    - name: Get properties of a SAP monitor
      azure_rm_sapmonitor_info: 
        resource_group_name: myResourceGroup
        sap_monitor_name: mySapMonitor
        

'''

RETURN = '''
sap_monitors:
  description: >-
    A list of dict results where the key is the name of the SapMonitor and the
    values are the facts for that SapMonitor.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of SAP monitors.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - State of provisioning of the HanaInstance
          returned: always
          type: str
          sample: null
        managed_resource_group_name:
          description:
            - >-
              The name of the resource group the SAP Monitor resources get
              deployed into.
          returned: always
          type: str
          sample: null
        log_analytics_workspace_arm_id:
          description:
            - >-
              The ARM ID of the Log Analytics Workspace that is used for
              monitoring
          returned: always
          type: str
          sample: null
        enable_customer_analytics:
          description:
            - The value indicating whether to send analytics to Microsoft
          returned: always
          type: bool
          sample: null
        log_analytics_workspace_id:
          description:
            - >-
              The workspace ID of the log analytics workspace to be used for
              monitoring
          returned: always
          type: str
          sample: null
        log_analytics_workspace_shared_key:
          description:
            - >-
              The shared key of the log analytics workspace that is used for
              monitoring
          returned: always
          type: str
          sample: null
        sap_monitor_collector_version:
          description:
            - The version of the payload running in the Collector VM
          returned: always
          type: str
          sample: null
        monitor_subnet:
          description:
            - The subnet which the SAP monitor will be deployed in
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of SAP monitors.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - State of provisioning of the HanaInstance
      returned: always
      type: str
      sample: null
    managed_resource_group_name:
      description:
        - >-
          The name of the resource group the SAP Monitor resources get deployed
          into.
      returned: always
      type: str
      sample: null
    log_analytics_workspace_arm_id:
      description:
        - The ARM ID of the Log Analytics Workspace that is used for monitoring
      returned: always
      type: str
      sample: null
    enable_customer_analytics:
      description:
        - The value indicating whether to send analytics to Microsoft
      returned: always
      type: bool
      sample: null
    log_analytics_workspace_id:
      description:
        - >-
          The workspace ID of the log analytics workspace to be used for
          monitoring
      returned: always
      type: str
      sample: null
    log_analytics_workspace_shared_key:
      description:
        - >-
          The shared key of the log analytics workspace that is used for
          monitoring
      returned: always
      type: str
      sample: null
    sap_monitor_collector_version:
      description:
        - The version of the payload running in the Collector VM
      returned: always
      type: str
      sample: null
    monitor_subnet:
      description:
        - The subnet which the SAP monitor will be deployed in
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
    from azure.mgmt.hana import HanaManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSapMonitorInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            sap_monitor_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.sap_monitor_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-07-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSapMonitorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HanaManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-07-preview')

        if (self.resource_group_name is not None and
            self.sap_monitor_name is not None):
            self.results['sap_monitors'] = self.format_item(self.get())
        else:
            self.results['sap_monitors'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sap_monitors.get(resource_group_name=self.resource_group_name,
                                                         sap_monitor_name=self.sap_monitor_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.sap_monitors.list()
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
    AzureRMSapMonitorInfo()


if __name__ == '__main__':
    main()
