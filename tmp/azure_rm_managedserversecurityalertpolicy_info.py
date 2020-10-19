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
module: azure_rm_managedserversecurityalertpolicy_info
version_added: '2.9'
short_description: Get ManagedServerSecurityAlertPolicy info.
description:
  - Get info of ManagedServerSecurityAlertPolicy.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  security_alert_policy_name:
    description:
      - The name of the security alert policy.
    type: str
    choices:
      - Default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a managed server's threat detection policy
      azure_rm_managedserversecurityalertpolicy_info: 
        managed_instance_name: securityalert-6440
        resource_group_name: securityalert-4799
        security_alert_policy_name: Default
        

    - name: Get the managed server's threat detection policies
      azure_rm_managedserversecurityalertpolicy_info: 
        managed_instance_name: securityalert-6440
        resource_group_name: securityalert-4799
        

'''

RETURN = '''
managed_server_security_alert_policies:
  description: >-
    A list of dict results where the key is the name of the
    ManagedServerSecurityAlertPolicy and the values are the facts for that
    ManagedServerSecurityAlertPolicy.
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
    state:
      description:
        - >-
          Specifies the state of the policy, whether it is enabled or disabled
          or a policy has not been applied yet on the specific database.
      returned: always
      type: sealed-choice
      sample: null
    disabled_alerts:
      description:
        - >-
          Specifies an array of alerts that are disabled. Allowed values are:
          Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly,
          Data_Exfiltration, Unsafe_Action
      returned: always
      type: list
      sample: null
    email_addresses:
      description:
        - Specifies an array of e-mail addresses to which the alert is sent.
      returned: always
      type: list
      sample: null
    email_account_admins:
      description:
        - Specifies that the alert is sent to the account administrators.
      returned: always
      type: bool
      sample: null
    storage_endpoint:
      description:
        - >-
          Specifies the blob storage endpoint (e.g.
          https://MyAccount.blob.core.windows.net). This blob storage will hold
          all Threat Detection audit logs.
      returned: always
      type: str
      sample: null
    storage_account_access_key:
      description:
        - >-
          Specifies the identifier key of the Threat Detection audit storage
          account.
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
    creation_time:
      description:
        - Specifies the UTC creation time of the policy.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        state:
          description:
            - >-
              Specifies the state of the policy, whether it is enabled or
              disabled or a policy has not been applied yet on the specific
              database.
          returned: always
          type: sealed-choice
          sample: null
        disabled_alerts:
          description:
            - >-
              Specifies an array of alerts that are disabled. Allowed values
              are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly,
              Data_Exfiltration, Unsafe_Action
          returned: always
          type: list
          sample: null
        email_addresses:
          description:
            - Specifies an array of e-mail addresses to which the alert is sent.
          returned: always
          type: list
          sample: null
        email_account_admins:
          description:
            - Specifies that the alert is sent to the account administrators.
          returned: always
          type: bool
          sample: null
        storage_endpoint:
          description:
            - >-
              Specifies the blob storage endpoint (e.g.
              https://MyAccount.blob.core.windows.net). This blob storage will
              hold all Threat Detection audit logs.
          returned: always
          type: str
          sample: null
        storage_account_access_key:
          description:
            - >-
              Specifies the identifier key of the Threat Detection audit storage
              account.
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
        creation_time:
          description:
            - Specifies the UTC creation time of the policy.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagedServerSecurityAlertPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            security_alert_policy_name=dict(
                type='str',
                choices=['Default']
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.security_alert_policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedServerSecurityAlertPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.security_alert_policy_name is not None):
            self.results['managed_server_security_alert_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['managed_server_security_alert_policies'] = self.format_item(self.listbyinstance())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_server_security_alert_policies.get(resource_group_name=self.resource_group_name,
                                                                                   managed_instance_name=self.managed_instance_name,
                                                                                   security_alert_policy_name=self.security_alert_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstance(self):
        response = None

        try:
            response = self.mgmt_client.managed_server_security_alert_policies.list_by_instance(resource_group_name=self.resource_group_name,
                                                                                                managed_instance_name=self.managed_instance_name)
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
    AzureRMManagedServerSecurityAlertPolicyInfo()


if __name__ == '__main__':
    main()
