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
module: azure_rm_azureadmetric_info
version_added: '2.9'
short_description: Get azureADMetric info.
description:
  - Get info of azureADMetric.
options:
  resource_group_name:
    description:
      - Name of an Azure resource group.
    type: str
  azure_ad_metrics_name:
    description:
      - Name of the azureADMetrics instance.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: azureADMetricsGet
      azure_rm_azureadmetric_info: 
        resource_group_name: rg1
        

    - name: azureADMetricsListBySubscription
      azure_rm_azureadmetric_info: 
        {}
        

    - name: azureADMetricsGetList
      azure_rm_azureadmetric_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
azure_admetrics:
  description: >-
    A list of dict results where the key is the name of the azureADMetric and
    the values are the facts for that azureADMetric.
  returned: always
  type: complex
  contains:
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
    properties:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        provisioning_state:
          description:
            - The provisioning state of the resource.
          returned: always
          type: str
          sample: null
    value:
      description:
        - Array of AzureADMetrics resources.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            provisioning_state:
              description:
                - The provisioning state of the resource.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - The link used to get the next page of operations.
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
    from azure.mgmt.azureactivedirectory import azureactivedirectory
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMazureADMetricInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            azure_ad_metrics_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.azure_ad_metrics_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMazureADMetricInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(azureactivedirectory,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01-preview')

        if (self.resource_group_name is not None and
            self.azure_ad_metrics_name is not None):
            self.results['azure_admetrics'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['azure_admetrics'] = self.format_item(self.list())
        else:
            self.results['azure_admetrics'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.azure_admetrics.get(resource_group_name=self.resource_group_name,
                                                            azure_ad_metrics_name=self.azure_ad_metrics_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.azure_admetrics.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.azure_admetrics.list_by_subscription()
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
    AzureRMazureADMetricInfo()


if __name__ == '__main__':
    main()
