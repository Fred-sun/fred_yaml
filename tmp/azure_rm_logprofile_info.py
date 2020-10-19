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
module: azure_rm_logprofile_info
version_added: '2.9'
short_description: Get LogProfile info.
description:
  - Get info of LogProfile.
options:
  log_profile_name:
    description:
      - The name of the log profile.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get log profile
      azure_rm_logprofile_info: 
        log_profile_name: default
        

    - name: List log profiles
      azure_rm_logprofile_info: 
        {}
        

'''

RETURN = '''
log_profiles:
  description: >-
    A list of dict results where the key is the name of the LogProfile and the
    values are the facts for that LogProfile.
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
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    storage_account_id:
      description:
        - >-
          the resource id of the storage account to which you would like to send
          the Activity Log.
      returned: always
      type: str
      sample: null
    service_bus_rule_id:
      description:
        - >-
          The service bus rule ID of the service bus namespace in which you
          would like to have Event Hubs created for streaming the Activity Log.
          The rule ID is of the format: '{service bus resource
          ID}/authorizationrules/{key name}'.
      returned: always
      type: str
      sample: null
    locations:
      description:
        - >-
          List of regions for which Activity Log events should be stored or
          streamed. It is a comma separated list of valid ARM locations
          including the 'global' location.
      returned: always
      type: list
      sample: null
    categories:
      description:
        - >-
          the categories of the logs. These categories are created as is
          convenient to the user. Some values are: 'Write', 'Delete', and/or
          'Action.'
      returned: always
      type: list
      sample: null
    retention_policy:
      description:
        - the retention policy for the events in the log.
      returned: always
      type: dict
      sample: null
      contains:
        enabled:
          description:
            - a value indicating whether the retention policy is enabled.
          returned: always
          type: bool
          sample: null
        days:
          description:
            - >-
              the number of days for the retention in days. A value of 0 will
              retain the events indefinitely.
          returned: always
          type: integer
          sample: null
    value:
      description:
        - the values of the log profiles.
      returned: always
      type: list
      sample: null
      contains:
        storage_account_id:
          description:
            - >-
              the resource id of the storage account to which you would like to
              send the Activity Log.
          returned: always
          type: str
          sample: null
        service_bus_rule_id:
          description:
            - >-
              The service bus rule ID of the service bus namespace in which you
              would like to have Event Hubs created for streaming the Activity
              Log. The rule ID is of the format: '{service bus resource
              ID}/authorizationrules/{key name}'.
          returned: always
          type: str
          sample: null
        locations:
          description:
            - >-
              List of regions for which Activity Log events should be stored or
              streamed. It is a comma separated list of valid ARM locations
              including the 'global' location.
          returned: always
          type: list
          sample: null
        categories:
          description:
            - >-
              the categories of the logs. These categories are created as is
              convenient to the user. Some values are: 'Write', 'Delete', and/or
              'Action.'
          returned: always
          type: list
          sample: null
        retention_policy:
          description:
            - the retention policy for the events in the log.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - a value indicating whether the retention policy is enabled.
              returned: always
              type: bool
              sample: null
            days:
              description:
                - >-
                  the number of days for the retention in days. A value of 0
                  will retain the events indefinitely.
              returned: always
              type: integer
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


class AzureRMLogProfileInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            log_profile_name=dict(
                type='str'
            )
        )

        self.log_profile_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLogProfileInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-01')

        if (self.log_profile_name is not None):
            self.results['log_profiles'] = self.format_item(self.get())
        else:
            self.results['log_profiles'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.log_profiles.get(log_profile_name=self.log_profile_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.log_profiles.list()
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
    AzureRMLogProfileInfo()


if __name__ == '__main__':
    main()
