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
module: azure_rm_domainservice_info
version_added: '2.9'
short_description: Get DomainService info.
description:
  - Get info of DomainService.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    type: str
  domain_service_name:
    description:
      - The name of the domain service.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Domain Service
      azure_rm_domainservice_info: 
        {}
        

    - name: Get Domain Service
      azure_rm_domainservice_info: 
        domain_service_name: zdomain.zforest.com
        resource_group_name: sva-tt-WUS
        

'''

RETURN = '''
domain_services:
  description: >-
    A list of dict results where the key is the name of the DomainService and
    the values are the facts for that DomainService.
  returned: always
  type: complex
  contains:
    value:
      description:
        - the list of domain services.
      returned: always
      type: list
      sample: null
      contains:
        tenant_id:
          description:
            - Azure Active Directory tenant id
          returned: always
          type: str
          sample: null
        domain_name:
          description:
            - >-
              The name of the Azure domain that the user would like to deploy
              Domain Services to.
          returned: always
          type: str
          sample: null
        vnet_site_id:
          description:
            - Virtual network site id
          returned: always
          type: str
          sample: null
        subnet_id:
          description:
            - >-
              The name of the virtual network that Domain Services will be
              deployed on. The id of the subnet that Domain Services will be
              deployed on. /virtualNetwork/vnetName/subnets/subnetName.
          returned: always
          type: str
          sample: null
        ldaps_settings:
          description:
            - Secure LDAP Settings
          returned: always
          type: dict
          sample: null
          contains:
            ldaps:
              description:
                - >-
                  A flag to determine whether or not Secure LDAP is enabled or
                  disabled.
              returned: always
              type: str
              sample: null
            pfx_certificate:
              description:
                - >-
                  The certificate required to configure Secure LDAP. The
                  parameter passed here should be a base64encoded representation
                  of the certificate pfx file.
              returned: always
              type: str
              sample: null
            pfx_certificate_password:
              description:
                - >-
                  The password to decrypt the provided Secure LDAP certificate
                  pfx file.
              returned: always
              type: str
              sample: null
            public_certificate:
              description:
                - Public certificate used to configure secure ldap.
              returned: always
              type: str
              sample: null
            certificate_thumbprint:
              description:
                - Thumbprint of configure ldaps certificate.
              returned: always
              type: str
              sample: null
            certificate_not_after:
              description:
                - NotAfter DateTime of configure ldaps certificate.
              returned: always
              type: str
              sample: null
            external_access:
              description:
                - >-
                  A flag to determine whether or not Secure LDAP access over the
                  internet is enabled or disabled.
              returned: always
              type: str
              sample: null
            external_access_ip_address:
              description:
                - External access ip address.
              returned: always
              type: str
              sample: null
        health_last_evaluated:
          description:
            - Last domain evaluation run DateTime
          returned: always
          type: str
          sample: null
        health_monitors:
          description:
            - List of Domain Health Monitors
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Health Monitor Id
              returned: always
              type: str
              sample: null
            name:
              description:
                - Health Monitor Name
              returned: always
              type: str
              sample: null
            details:
              description:
                - Health Monitor Details
              returned: always
              type: str
              sample: null
        health_alerts:
          description:
            - List of Domain Health Alerts
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Health Alert Id
              returned: always
              type: str
              sample: null
            name:
              description:
                - Health Alert Name
              returned: always
              type: str
              sample: null
            issue:
              description:
                - Health Alert Issue
              returned: always
              type: str
              sample: null
            severity:
              description:
                - Health Alert Severity
              returned: always
              type: str
              sample: null
            raised:
              description:
                - Health Alert Raised DateTime
              returned: always
              type: str
              sample: null
            last_detected:
              description:
                - Health Alert Last Detected DateTime
              returned: always
              type: str
              sample: null
            resolution_uri:
              description:
                - Health Alert TSG Link
              returned: always
              type: str
              sample: null
        notification_settings:
          description:
            - Notification Settings
          returned: always
          type: dict
          sample: null
          contains:
            notify_global_admins:
              description:
                - Should global admins be notified
              returned: always
              type: str
              sample: null
            notify_dc_admins:
              description:
                - Should domain controller admins be notified
              returned: always
              type: str
              sample: null
            additional_recipients:
              description:
                - The list of additional recipients
              returned: always
              type: list
              sample: null
        domain_security_settings:
          description:
            - DomainSecurity Settings
          returned: always
          type: dict
          sample: null
          contains:
            ntlm_v1:
              description:
                - >-
                  A flag to determine whether or not NtlmV1 is enabled or
                  disabled.
              returned: always
              type: str
              sample: null
            tls_v1:
              description:
                - >-
                  A flag to determine whether or not TlsV1 is enabled or
                  disabled.
              returned: always
              type: str
              sample: null
            sync_ntlm_passwords:
              description:
                - >-
                  A flag to determine whether or not SyncNtlmPasswords is
                  enabled or disabled.
              returned: always
              type: str
              sample: null
        filtered_sync:
          description:
            - Enabled or Disabled flag to turn on Group-based filtered sync
          returned: always
          type: str
          sample: null
        domain_controller_ip_address:
          description:
            - List of Domain Controller IP Address
          returned: always
          type: list
          sample: null
        service_status:
          description:
            - Status of Domain Service instance
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              the current deployment or provisioning state, which only appears
              in the response.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The continuation token for the next page of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
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
    etag:
      description:
        - Resource etag
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - Azure Active Directory tenant id
      returned: always
      type: str
      sample: null
    domain_name:
      description:
        - >-
          The name of the Azure domain that the user would like to deploy Domain
          Services to.
      returned: always
      type: str
      sample: null
    vnet_site_id:
      description:
        - Virtual network site id
      returned: always
      type: str
      sample: null
    subnet_id:
      description:
        - >-
          The name of the virtual network that Domain Services will be deployed
          on. The id of the subnet that Domain Services will be deployed on.
          /virtualNetwork/vnetName/subnets/subnetName.
      returned: always
      type: str
      sample: null
    ldaps_settings:
      description:
        - Secure LDAP Settings
      returned: always
      type: dict
      sample: null
      contains:
        ldaps:
          description:
            - >-
              A flag to determine whether or not Secure LDAP is enabled or
              disabled.
          returned: always
          type: str
          sample: null
        pfx_certificate:
          description:
            - >-
              The certificate required to configure Secure LDAP. The parameter
              passed here should be a base64encoded representation of the
              certificate pfx file.
          returned: always
          type: str
          sample: null
        pfx_certificate_password:
          description:
            - >-
              The password to decrypt the provided Secure LDAP certificate pfx
              file.
          returned: always
          type: str
          sample: null
        public_certificate:
          description:
            - Public certificate used to configure secure ldap.
          returned: always
          type: str
          sample: null
        certificate_thumbprint:
          description:
            - Thumbprint of configure ldaps certificate.
          returned: always
          type: str
          sample: null
        certificate_not_after:
          description:
            - NotAfter DateTime of configure ldaps certificate.
          returned: always
          type: str
          sample: null
        external_access:
          description:
            - >-
              A flag to determine whether or not Secure LDAP access over the
              internet is enabled or disabled.
          returned: always
          type: str
          sample: null
        external_access_ip_address:
          description:
            - External access ip address.
          returned: always
          type: str
          sample: null
    health_last_evaluated:
      description:
        - Last domain evaluation run DateTime
      returned: always
      type: str
      sample: null
    health_monitors:
      description:
        - List of Domain Health Monitors
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Health Monitor Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Health Monitor Name
          returned: always
          type: str
          sample: null
        details:
          description:
            - Health Monitor Details
          returned: always
          type: str
          sample: null
    health_alerts:
      description:
        - List of Domain Health Alerts
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Health Alert Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Health Alert Name
          returned: always
          type: str
          sample: null
        issue:
          description:
            - Health Alert Issue
          returned: always
          type: str
          sample: null
        severity:
          description:
            - Health Alert Severity
          returned: always
          type: str
          sample: null
        raised:
          description:
            - Health Alert Raised DateTime
          returned: always
          type: str
          sample: null
        last_detected:
          description:
            - Health Alert Last Detected DateTime
          returned: always
          type: str
          sample: null
        resolution_uri:
          description:
            - Health Alert TSG Link
          returned: always
          type: str
          sample: null
    notification_settings:
      description:
        - Notification Settings
      returned: always
      type: dict
      sample: null
      contains:
        notify_global_admins:
          description:
            - Should global admins be notified
          returned: always
          type: str
          sample: null
        notify_dc_admins:
          description:
            - Should domain controller admins be notified
          returned: always
          type: str
          sample: null
        additional_recipients:
          description:
            - The list of additional recipients
          returned: always
          type: list
          sample: null
    domain_security_settings:
      description:
        - DomainSecurity Settings
      returned: always
      type: dict
      sample: null
      contains:
        ntlm_v1:
          description:
            - A flag to determine whether or not NtlmV1 is enabled or disabled.
          returned: always
          type: str
          sample: null
        tls_v1:
          description:
            - A flag to determine whether or not TlsV1 is enabled or disabled.
          returned: always
          type: str
          sample: null
        sync_ntlm_passwords:
          description:
            - >-
              A flag to determine whether or not SyncNtlmPasswords is enabled or
              disabled.
          returned: always
          type: str
          sample: null
    filtered_sync:
      description:
        - Enabled or Disabled flag to turn on Group-based filtered sync
      returned: always
      type: str
      sample: null
    domain_controller_ip_address:
      description:
        - List of Domain Controller IP Address
      returned: always
      type: list
      sample: null
    service_status:
      description:
        - Status of Domain Service instance
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          the current deployment or provisioning state, which only appears in
          the response.
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
    from azure.mgmt.domain import Domain Services Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDomainServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            domain_service_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.domain_service_name = None

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
        super(AzureRMDomainServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Domain Services Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group_name is not None and
            self.domain_service_name is not None):
            self.results['domain_services'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['domain_services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['domain_services'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.domain_services.get(resource_group_name=self.resource_group_name,
                                                            domain_service_name=self.domain_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.domain_services.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.domain_services.list()
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
    AzureRMDomainServiceInfo()


if __name__ == '__main__':
    main()
