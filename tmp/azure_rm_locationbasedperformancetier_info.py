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
module: azure_rm_locationbasedperformancetier_info
version_added: '2.9'
short_description: Get LocationBasedPerformanceTier info.
description:
  - Get info of LocationBasedPerformanceTier.
options:
  location_name:
    description:
      - The name of the location.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: PerformanceTiersList
      azure_rm_locationbasedperformancetier_info: 
        location_name: WestUS
        

'''

RETURN = '''
location_based_performance_tier:
  description: >-
    A list of dict results where the key is the name of the
    LocationBasedPerformanceTier and the values are the facts for that
    LocationBasedPerformanceTier.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of performance tiers
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - ID of the performance tier.
          returned: always
          type: str
          sample: null
        service_level_objectives:
          description:
            - Service level objectives associated with the performance tier
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - ID for the service level objective.
              returned: always
              type: str
              sample: null
            edition:
              description:
                - Edition of the performance tier.
              returned: always
              type: str
              sample: null
            v_core:
              description:
                - vCore associated with the service level objective
              returned: always
              type: integer
              sample: null
            hardware_generation:
              description:
                - >-
                  Hardware generation associated with the service level
                  objective
              returned: always
              type: str
              sample: null
            max_backup_retention_days:
              description:
                - >-
                  Maximum Backup retention in days for the performance tier
                  edition
              returned: always
              type: integer
              sample: null
            min_backup_retention_days:
              description:
                - >-
                  Minimum Backup retention in days for the performance tier
                  edition
              returned: always
              type: integer
              sample: null
            max_storage_mb:
              description:
                - Max storage allowed for a server.
              returned: always
              type: integer
              sample: null
            min_storage_mb:
              description:
                - Max storage allowed for a server.
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
    from azure.mgmt.postgre import PostgreSQLManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLocationBasedPerformanceTierInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=True
            )
        )

        self.location_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLocationBasedPerformanceTierInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-12-01')

        if (self.location_name is not None):
            self.results['location_based_performance_tier'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.location_based_performance_tier.list(location_name=self.location_name)
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
    AzureRMLocationBasedPerformanceTierInfo()


if __name__ == '__main__':
    main()
