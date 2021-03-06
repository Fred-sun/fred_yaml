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
module: azure_rm_replicationusage_info
version_added: '2.9'
short_description: Get ReplicationUsage info.
description:
  - Get info of ReplicationUsage.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
    type: str
  vault_name:
    description:
      - The name of the recovery services vault.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets Replication usages of vault
      azure_rm_replicationusage_info: 
        resource_group_name: avrai7517RG1
        vault_name: avrai7517Vault1
        

'''

RETURN = '''
replication_usages:
  description: >-
    A list of dict results where the key is the name of the ReplicationUsage and
    the values are the facts for that ReplicationUsage.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of replication usages for the given vault.
      returned: always
      type: list
      sample: null
      contains:
        monitoring_summary:
          description:
            - Summary of the replication monitoring data for this vault.
          returned: always
          type: dict
          sample: null
          contains:
            un_healthy_vm_count:
              description:
                - Count of unhealthy VMs.
              returned: always
              type: integer
              sample: null
            un_healthy_provider_count:
              description:
                - Count of unhealthy replication providers.
              returned: always
              type: integer
              sample: null
            events_count:
              description:
                - Count of all critical warnings.
              returned: always
              type: integer
              sample: null
            deprecated_provider_count:
              description:
                - Count of all deprecated recovery service providers.
              returned: always
              type: integer
              sample: null
            supported_provider_count:
              description:
                - Count of all the supported recovery service providers.
              returned: always
              type: integer
              sample: null
            unsupported_provider_count:
              description:
                - Count of all the unsupported recovery service providers.
              returned: always
              type: integer
              sample: null
        jobs_summary:
          description:
            - Summary of the replication jobs data for this vault.
          returned: always
          type: dict
          sample: null
          contains:
            failed_jobs:
              description:
                - Count of failed jobs.
              returned: always
              type: integer
              sample: null
            suspended_jobs:
              description:
                - Count of suspended jobs.
              returned: always
              type: integer
              sample: null
            in_progress_jobs:
              description:
                - Count of in-progress jobs.
              returned: always
              type: integer
              sample: null
        protected_item_count:
          description:
            - Number of replication protected items for this vault.
          returned: always
          type: integer
          sample: null
        recovery_plan_count:
          description:
            - Number of replication recovery plans for this vault.
          returned: always
          type: integer
          sample: null
        registered_servers_count:
          description:
            - Number of servers registered to this vault.
          returned: always
          type: integer
          sample: null
        recovery_services_provider_auth_type:
          description:
            - >-
              The authentication type of recovery service providers in the
              vault.
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
    from azure.mgmt.recovery import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReplicationUsageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vault_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.vault_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReplicationUsageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-06-01')

        if (self.resource_group_name is not None and
            self.vault_name is not None):
            self.results['replication_usages'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.replication_usages.list(resource_group_name=self.resource_group_name,
                                                                vault_name=self.vault_name)
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
    AzureRMReplicationUsageInfo()


if __name__ == '__main__':
    main()
