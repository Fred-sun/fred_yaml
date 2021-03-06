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
module: azure_rm_emergingissue_info
version_added: '2.9'
short_description: Get EmergingIssue info.
description:
  - Get info of EmergingIssue.
options:
  issuename:
    description:
      - The name of the emerging issue.
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetEmergingIssues
      azure_rm_emergingissue_info: 
        {}
        

'''

RETURN = '''
emerging_issues:
  description: >-
    A list of dict results where the key is the name of the EmergingIssue and
    the values are the facts for that EmergingIssue.
  returned: always
  type: complex
  contains:
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
    refresh_timestamp:
      description:
        - Timestamp for when last time refreshed for ongoing emerging issue.
      returned: always
      type: str
      sample: null
    status_banners:
      description:
        - The list of emerging issues of banner type.
      returned: always
      type: list
      sample: null
      contains:
        title:
          description:
            - The banner title.
          returned: always
          type: str
          sample: null
        message:
          description:
            - The details of banner.
          returned: always
          type: str
          sample: null
        cloud:
          description:
            - The cloud type of this banner.
          returned: always
          type: str
          sample: null
        last_modified_time:
          description:
            - The last time modified on this banner.
          returned: always
          type: str
          sample: null
    status_active_events:
      description:
        - The list of emerging issues of active event type.
      returned: always
      type: list
      sample: null
      contains:
        title:
          description:
            - The active event title.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The details of active event.
          returned: always
          type: str
          sample: null
        tracking_id:
          description:
            - The tracking id of this active event.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - The impact start time on this active event.
          returned: always
          type: str
          sample: null
        cloud:
          description:
            - The cloud type of this active event.
          returned: always
          type: str
          sample: null
        severity:
          description:
            - The severity level of this active event.
          returned: always
          type: str
          sample: null
        stage:
          description:
            - The stage of this active event.
          returned: always
          type: str
          sample: null
        published:
          description:
            - The boolean value of this active event if published or not.
          returned: always
          type: bool
          sample: null
        last_modified_time:
          description:
            - The last time modified on this banner.
          returned: always
          type: str
          sample: null
        impacts:
          description:
            - The list of emerging issues impacts.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - The impacted service id.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The impacted service name.
              returned: always
              type: str
              sample: null
            regions:
              description:
                - >-
                  The list of impacted regions for corresponding emerging
                  issues.
              returned: always
              type: list
              sample: null
              contains:
                id:
                  description:
                    - The impacted region id.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The impacted region name.
                  returned: always
                  type: str
                  sample: null
    value:
      description:
        - The list of emerging issues.
      returned: always
      type: list
      sample: null
      contains:
        refresh_timestamp:
          description:
            - Timestamp for when last time refreshed for ongoing emerging issue.
          returned: always
          type: str
          sample: null
        status_banners:
          description:
            - The list of emerging issues of banner type.
          returned: always
          type: list
          sample: null
          contains:
            title:
              description:
                - The banner title.
              returned: always
              type: str
              sample: null
            message:
              description:
                - The details of banner.
              returned: always
              type: str
              sample: null
            cloud:
              description:
                - The cloud type of this banner.
              returned: always
              type: str
              sample: null
            last_modified_time:
              description:
                - The last time modified on this banner.
              returned: always
              type: str
              sample: null
        status_active_events:
          description:
            - The list of emerging issues of active event type.
          returned: always
          type: list
          sample: null
          contains:
            title:
              description:
                - The active event title.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The details of active event.
              returned: always
              type: str
              sample: null
            tracking_id:
              description:
                - The tracking id of this active event.
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - The impact start time on this active event.
              returned: always
              type: str
              sample: null
            cloud:
              description:
                - The cloud type of this active event.
              returned: always
              type: str
              sample: null
            severity:
              description:
                - The severity level of this active event.
              returned: always
              type: str
              sample: null
            stage:
              description:
                - The stage of this active event.
              returned: always
              type: str
              sample: null
            published:
              description:
                - The boolean value of this active event if published or not.
              returned: always
              type: bool
              sample: null
            last_modified_time:
              description:
                - The last time modified on this banner.
              returned: always
              type: str
              sample: null
            impacts:
              description:
                - The list of emerging issues impacts.
              returned: always
              type: list
              sample: null
              contains:
                id:
                  description:
                    - The impacted service id.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The impacted service name.
                  returned: always
                  type: str
                  sample: null
                regions:
                  description:
                    - >-
                      The list of impacted regions for corresponding emerging
                      issues.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    id:
                      description:
                        - The impacted region id.
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - The impacted region name.
                      returned: always
                      type: str
                      sample: null
    next_link:
      description:
        - The link used to get the next page of emerging issues.
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
    from azure.mgmt.microsoft.resource import Microsoft.ResourceHealth
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEmergingIssueInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            issuename=dict(
                type='constant'
            )
        )

        self.issuename = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEmergingIssueInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.ResourceHealth,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-07-01')

        if (self.issuename is not None):
            self.results['emerging_issues'] = self.format_item(self.get())
        else:
            self.results['emerging_issues'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.emerging_issues.get(issuename=self.issuename)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.emerging_issues.list()
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
    AzureRMEmergingIssueInfo()


if __name__ == '__main__':
    main()
