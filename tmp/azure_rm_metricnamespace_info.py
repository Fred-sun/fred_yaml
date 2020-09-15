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
module: azure_rm_metricnamespace_info
version_added: '2.9'
short_description: Get MetricNamespace info.
description:
  - Get info of MetricNamespace.
options:
  resource_uri:
    description:
      - The identifier of the resource.
    required: true
    type: str
  start_time:
    description:
      - >-
        The ISO 8601 conform Date start time from which to query for metric
        namespaces.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Metric Namespaces without filter
      azure_rm_metricnamespace_info: 
        resource_uri: >-
          subscriptions/a252e87d-ec06-45b1-8901-57e613be91b0/resourceGroups/larrytest/providers/Microsoft.DocumentDB/databaseAccounts/larrytestdocdb
        start_time: '2018-08-31T15:53:00Z'
        

'''

RETURN = '''
metric_namespaces:
  description: >-
    A list of dict results where the key is the name of the MetricNamespace and
    the values are the facts for that MetricNamespace.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The values for the metric namespaces.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The ID of the metricNamespace.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the namespace.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the namespace.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties which include the fully qualified namespace name.
          returned: always
          type: dict
          sample: null
          contains:
            metric_namespace_name:
              description:
                - The metric namespace name.
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


class AzureRMMetricNamespaceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            start_time=dict(
                type='str',
                required=True
            )
        )

        self.resource_uri = None
        self.start_time = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-12-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMetricNamespaceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-12-01-preview')

        if (self.resource_uri is not None):
            self.results['metric_namespaces'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.metric_namespaces.list(resource_uri=self.resource_uri,
                                                               start_time=self.start_time)
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
    AzureRMMetricNamespaceInfo()


if __name__ == '__main__':
    main()
