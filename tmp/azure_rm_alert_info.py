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
module: azure_rm_alert_info
version_added: '2.9'
short_description: Get Alert info.
description:
  - Get info of Alert.
options:
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  filter:
    description:
      - OData Filter options
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: AlertsListByManager
      azure_rm_alert_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
alerts:
  description: >-
    A list of dict results where the key is the name of the Alert and the values
    are the facts for that Alert.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        title:
          description:
            - The title of the alert
          returned: always
          type: str
          sample: null
        scope:
          description:
            - The scope of the alert
          returned: always
          type: sealed-choice
          sample: null
        alert_type:
          description:
            - The type of the alert
          returned: always
          type: str
          sample: null
        appeared_at_time:
          description:
            - The UTC time at which the alert was raised
          returned: always
          type: str
          sample: null
        appeared_at_source_time:
          description:
            - The source time at which the alert was raised
          returned: always
          type: str
          sample: null
        cleared_at_time:
          description:
            - The UTC time at which the alert was cleared
          returned: always
          type: str
          sample: null
        cleared_at_source_time:
          description:
            - The source time at which the alert was cleared
          returned: always
          type: str
          sample: null
        source:
          description:
            - The source at which the alert was raised
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The name of the source
              returned: always
              type: str
              sample: null
            time_zone:
              description:
                - The time zone of the source
              returned: always
              type: str
              sample: null
            alert_source_type:
              description:
                - The source type of the alert
              returned: always
              type: sealed-choice
              sample: null
        recommendation:
          description:
            - The recommended action for the issue raised in the alert
          returned: always
          type: str
          sample: null
        resolution_reason:
          description:
            - The reason for resolving the alert
          returned: always
          type: str
          sample: null
        severity:
          description:
            - The severity of the alert
          returned: always
          type: sealed-choice
          sample: null
        status:
          description:
            - The current status of the alert
          returned: always
          type: sealed-choice
          sample: null
        error_details:
          description:
            - The details of the error for which the alert was raised
          returned: always
          type: dict
          sample: null
          contains:
            error_code:
              description:
                - The error code
              returned: always
              type: str
              sample: null
            error_message:
              description:
                - The error message
              returned: always
              type: str
              sample: null
            occurences:
              description:
                - The number of occurrences
              returned: always
              type: integer
              sample: null
        detailed_information:
          description:
            - More details about the alert
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - The URI of the next page of alerts.
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAlertInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.manager_name = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAlertInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group_name is not None and
            self.manager_name is not None):
            self.results['alerts'] = self.format_item(self.listbymanager())
        return self.results

    def listbymanager(self):
        response = None

        try:
            response = self.mgmt_client.alerts.list_by_manager(resource_group_name=self.resource_group_name,
                                                               manager_name=self.manager_name,
                                                               filter=self.filter)
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
    AzureRMAlertInfo()


if __name__ == '__main__':
    main()
