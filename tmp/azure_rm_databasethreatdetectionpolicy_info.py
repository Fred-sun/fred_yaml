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
module: azure_rm_databasethreatdetectionpolicy_info
version_added: '2.9'
short_description: Get DatabaseThreatDetectionPolicy info.
description:
  - Get info of DatabaseThreatDetectionPolicy.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - >-
        The name of the database for which database Threat Detection policy is
        defined.
    required: true
    type: str
  security_alert_policy_name:
    description:
      - The name of the security alert policy.
    required: true
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get database security alert policy
      azure_rm_databasethreatdetectionpolicy_info: 
        database_name: testdb
        resource_group_name: securityalert-6852
        security_alert_policy_name: default
        server_name: securityalert-2080
        

'''

RETURN = '''
database_threat_detection_policies:
  description: >-
    A list of dict results where the key is the name of the
    DatabaseThreatDetectionPolicy and the values are the facts for that
    DatabaseThreatDetectionPolicy.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    kind:
      description:
        - Resource kind.
      returned: always
      type: str
      sample: null
    state:
      description:
        - >-
          Specifies the state of the policy. If state is Enabled,
          storageEndpoint and storageAccountAccessKey are required.
      returned: always
      type: sealed-choice
      sample: null
    disabled_alerts:
      description:
        - >-
          Specifies the semicolon-separated list of alerts that are disabled, or
          empty string to disable no alerts. Possible values: Sql_Injection;
          Sql_Injection_Vulnerability; Access_Anomaly; Data_Exfiltration;
          Unsafe_Action.
      returned: always
      type: str
      sample: null
    email_addresses:
      description:
        - >-
          Specifies the semicolon-separated list of e-mail addresses to which
          the alert is sent.
      returned: always
      type: str
      sample: null
    email_account_admins:
      description:
        - Specifies that the alert is sent to the account administrators.
      returned: always
      type: sealed-choice
      sample: null
    storage_endpoint:
      description:
        - >-
          Specifies the blob storage endpoint (e.g.
          https://MyAccount.blob.core.windows.net). This blob storage will hold
          all Threat Detection audit logs. If state is Enabled, storageEndpoint
          is required.
      returned: always
      type: str
      sample: null
    storage_account_access_key:
      description:
        - >-
          Specifies the identifier key of the Threat Detection audit storage
          account. If state is Enabled, storageAccountAccessKey is required.
      returned: always
      type: str
      sample: null
    retention_days:
      description:
        - >-
          Specifies the number of days to keep in the Threat Detection audit
          logs.
      returned: always
      type: integer
      sample: null
    use_server_default:
      description:
        - Specifies whether to use the default server policy.
      returned: always
      type: sealed-choice
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDatabaseThreatDetectionPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            security_alert_policy_name=dict(
                type='str',
                choices=['default'],
                required=True
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.security_alert_policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDatabaseThreatDetectionPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.security_alert_policy_name is not None):
            self.results['database_threat_detection_policies'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.database_threat_detection_policies.get(resource_group_name=self.resource_group_name,
                                                                               server_name=self.server_name,
                                                                               database_name=self.database_name,
                                                                               security_alert_policy_name=self.security_alert_policy_name)
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
    AzureRMDatabaseThreatDetectionPolicyInfo()


if __name__ == '__main__':
    main()
