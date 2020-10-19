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
module: azure_rm_databasethreatdetectionpolicy
version_added: '2.9'
short_description: Manage Azure DatabaseThreatDetectionPolicy instance.
description:
  - 'Create, update and delete instance of Azure DatabaseThreatDetectionPolicy.'
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
  location:
    description:
      - The geo-location where the resource lives
    type: str
  state:
    description:
      - Assert the state of the DatabaseThreatDetectionPolicy.
      - >-
        Use C(present) to create or update an DatabaseThreatDetectionPolicy and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
  disabled_alerts:
    description:
      - >-
        Specifies the semicolon-separated list of alerts that are disabled, or
        empty string to disable no alerts. Possible values: Sql_Injection;
        Sql_Injection_Vulnerability; Access_Anomaly; Data_Exfiltration;
        Unsafe_Action.
    type: str
  email_addresses:
    description:
      - >-
        Specifies the semicolon-separated list of e-mail addresses to which the
        alert is sent.
    type: str
  email_account_admins:
    description:
      - Specifies that the alert is sent to the account administrators.
    type: sealed-choice
  storage_endpoint:
    description:
      - >-
        Specifies the blob storage endpoint (e.g.
        https://MyAccount.blob.core.windows.net). This blob storage will hold
        all Threat Detection audit logs. If state is Enabled, storageEndpoint is
        required.
    type: str
  storage_account_access_key:
    description:
      - >-
        Specifies the identifier key of the Threat Detection audit storage
        account. If state is Enabled, storageAccountAccessKey is required.
    type: str
  retention_days:
    description:
      - Specifies the number of days to keep in the Threat Detection audit logs.
    type: integer
  use_server_default:
    description:
      - Specifies whether to use the default server policy.
    type: sealed-choice
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create database security alert policy max
      azure_rm_databasethreatdetectionpolicy: 
        database_name: testdb
        resource_group_name: securityalert-4799
        security_alert_policy_name: default
        server_name: securityalert-6440
        properties:
          disabled_alerts: Sql_Injection;Usage_Anomaly;
          email_account_admins: Enabled
          email_addresses: test@microsoft.com;user@microsoft.com
          retention_days: 6
          state: Enabled
          storage_account_access_key: >-
            sdlfkjabc+sdlfkjsdlkfsjdfLDKFTERLKFDFKLjsdfksjdflsdkfD2342309432849328476458/3RSD==
          storage_endpoint: 'https://mystorage.blob.core.windows.net'
          use_server_default: Enabled
        

    - name: Create database security alert policy min
      azure_rm_databasethreatdetectionpolicy: 
        database_name: testdb
        resource_group_name: securityalert-4799
        security_alert_policy_name: default
        server_name: securityalert-6440
        properties:
          state: Enabled
          storage_account_access_key: >-
            sdlfkjabc+sdlfkjsdlkfsjdfLDKFTERLKFDFKLjsdfksjdflsdkfD2342309432849328476458/3RSD==
          storage_endpoint: 'https://mystorage.blob.core.windows.net'
        

'''

RETURN = '''
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
      Specifies the state of the policy. If state is Enabled, storageEndpoint
      and storageAccountAccessKey are required.
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
      Specifies the semicolon-separated list of e-mail addresses to which the
      alert is sent.
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
      https://MyAccount.blob.core.windows.net). This blob storage will hold all
      Threat Detection audit logs. If state is Enabled, storageEndpoint is
      required.
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
    - Specifies the number of days to keep in the Threat Detection audit logs.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDatabaseThreatDetectionPolicy(AzureRMModuleBaseExt):
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
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            state=dict(
                type='sealed-choice',
                disposition='/state'
            ),
            disabled_alerts=dict(
                type='str',
                disposition='/disabled_alerts'
            ),
            email_addresses=dict(
                type='str',
                disposition='/email_addresses'
            ),
            email_account_admins=dict(
                type='sealed-choice',
                disposition='/email_account_admins'
            ),
            storage_endpoint=dict(
                type='str',
                disposition='/storage_endpoint'
            ),
            storage_account_access_key=dict(
                type='str',
                disposition='/storage_account_access_key'
            ),
            retention_days=dict(
                type='integer',
                disposition='/retention_days'
            ),
            use_server_default=dict(
                type='sealed-choice',
                disposition='/use_server_default'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.security_alert_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDatabaseThreatDetectionPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                   supports_check_mode=True,
                                                                   supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.database_threat_detection_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                                            server_name=self.server_name,
                                                                                            database_name=self.database_name,
                                                                                            security_alert_policy_name=self.security_alert_policy_name,
                                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DatabaseThreatDetectionPolicy instance.')
            self.fail('Error creating the DatabaseThreatDetectionPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.database_threat_detection_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DatabaseThreatDetectionPolicy instance.')
            self.fail('Error deleting the DatabaseThreatDetectionPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.database_threat_detection_policies.get(resource_group_name=self.resource_group_name,
                                                                               server_name=self.server_name,
                                                                               database_name=self.database_name,
                                                                               security_alert_policy_name=self.security_alert_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDatabaseThreatDetectionPolicy()


if __name__ == '__main__':
    main()
