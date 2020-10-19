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
module: azure_rm_domainservice
version_added: '2.9'
short_description: Manage Azure DomainService instance.
description:
  - 'Create, update and delete instance of Azure DomainService.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  domain_service_name:
    description:
      - The name of the domain service.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  etag:
    description:
      - Resource etag
    type: str
  domain_name:
    description:
      - >-
        The name of the Azure domain that the user would like to deploy Domain
        Services to.
    type: str
  subnet_id:
    description:
      - >-
        The name of the virtual network that Domain Services will be deployed
        on. The id of the subnet that Domain Services will be deployed on.
        /virtualNetwork/vnetName/subnets/subnetName.
    type: str
  ldaps_settings:
    description:
      - Secure LDAP Settings
    type: dict
    suboptions:
      ldaps:
        description:
          - >-
            A flag to determine whether or not Secure LDAP is enabled or
            disabled.
        type: str
        choices:
          - Enabled
          - Disabled
      pfx_certificate:
        description:
          - >-
            The certificate required to configure Secure LDAP. The parameter
            passed here should be a base64encoded representation of the
            certificate pfx file.
        type: str
      pfx_certificate_password:
        description:
          - >-
            The password to decrypt the provided Secure LDAP certificate pfx
            file.
        type: str
      public_certificate:
        description:
          - Public certificate used to configure secure ldap.
        type: str
      certificate_thumbprint:
        description:
          - Thumbprint of configure ldaps certificate.
        type: str
      certificate_not_after:
        description:
          - NotAfter DateTime of configure ldaps certificate.
        type: str
      external_access:
        description:
          - >-
            A flag to determine whether or not Secure LDAP access over the
            internet is enabled or disabled.
        type: str
        choices:
          - Enabled
          - Disabled
      external_access_ip_address:
        description:
          - External access ip address.
        type: str
  notification_settings:
    description:
      - Notification Settings
    type: dict
    suboptions:
      notify_global_admins:
        description:
          - Should global admins be notified
        type: str
        choices:
          - Enabled
          - Disabled
      notify_dc_admins:
        description:
          - Should domain controller admins be notified
        type: str
        choices:
          - Enabled
          - Disabled
      additional_recipients:
        description:
          - The list of additional recipients
        type: list
  domain_security_settings:
    description:
      - DomainSecurity Settings
    type: dict
    suboptions:
      ntlm_v1:
        description:
          - A flag to determine whether or not NtlmV1 is enabled or disabled.
        type: str
        choices:
          - Enabled
          - Disabled
      tls_v1:
        description:
          - A flag to determine whether or not TlsV1 is enabled or disabled.
        type: str
        choices:
          - Enabled
          - Disabled
      sync_ntlm_passwords:
        description:
          - >-
            A flag to determine whether or not SyncNtlmPasswords is enabled or
            disabled.
        type: str
        choices:
          - Enabled
          - Disabled
  filtered_sync:
    description:
      - Enabled or Disabled flag to turn on Group-based filtered sync
    type: str
    choices:
      - Enabled
      - Disabled
  state:
    description:
      - Assert the state of the DomainService.
      - >-
        Use C(present) to create or update an DomainService and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create Domain Service
      azure_rm_domainservice: 
        domain_service_name: zdomain.zforest.com
        resource_group_name: sva-tt-WUS
        

    - name: Delete Domain Service
      azure_rm_domainservice: 
        domain_service_name: zdomain.zforest.com
        resource_group_name: sva-tt-WUS
        

    - name: Update Domain Service
      azure_rm_domainservice: 
        domain_service_name: zdomain.zforest.com
        resource_group_name: sva-tt-WUS
        

'''

RETURN = '''
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
      The name of the virtual network that Domain Services will be deployed on.
      The id of the subnet that Domain Services will be deployed on.
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
        - A flag to determine whether or not Secure LDAP is enabled or disabled.
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
        - The password to decrypt the provided Secure LDAP certificate pfx file.
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
      the current deployment or provisioning state, which only appears in the
      response.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.domain import Domain Services Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDomainService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            domain_service_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            domain_name=dict(
                type='str',
                disposition='/domain_name'
            ),
            subnet_id=dict(
                type='str',
                disposition='/subnet_id'
            ),
            ldaps_settings=dict(
                type='dict',
                disposition='/ldaps_settings',
                options=dict(
                    ldaps=dict(
                        type='str',
                        disposition='ldaps',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    pfx_certificate=dict(
                        type='str',
                        disposition='pfx_certificate'
                    ),
                    pfx_certificate_password=dict(
                        type='str',
                        disposition='pfx_certificate_password'
                    ),
                    public_certificate=dict(
                        type='str',
                        updatable=False,
                        disposition='public_certificate'
                    ),
                    certificate_thumbprint=dict(
                        type='str',
                        updatable=False,
                        disposition='certificate_thumbprint'
                    ),
                    certificate_not_after=dict(
                        type='str',
                        updatable=False,
                        disposition='certificate_not_after'
                    ),
                    external_access=dict(
                        type='str',
                        disposition='external_access',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    external_access_ip_address=dict(
                        type='str',
                        updatable=False,
                        disposition='external_access_ip_address'
                    )
                )
            ),
            notification_settings=dict(
                type='dict',
                disposition='/notification_settings',
                options=dict(
                    notify_global_admins=dict(
                        type='str',
                        disposition='notify_global_admins',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    notify_dc_admins=dict(
                        type='str',
                        disposition='notify_dc_admins',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    additional_recipients=dict(
                        type='list',
                        disposition='additional_recipients',
                        elements='str'
                    )
                )
            ),
            domain_security_settings=dict(
                type='dict',
                disposition='/domain_security_settings',
                options=dict(
                    ntlm_v1=dict(
                        type='str',
                        disposition='ntlm_v1',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    tls_v1=dict(
                        type='str',
                        disposition='tls_v1',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    sync_ntlm_passwords=dict(
                        type='str',
                        disposition='sync_ntlm_passwords',
                        choices=['Enabled',
                                 'Disabled']
                    )
                )
            ),
            filtered_sync=dict(
                type='str',
                disposition='/filtered_sync',
                choices=['Enabled',
                         'Disabled']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.domain_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDomainService, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Domain Services Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

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
            response = self.mgmt_client.domain_services.create_or_update(resource_group_name=self.resource_group_name,
                                                                         domain_service_name=self.domain_service_name,
                                                                         domain_service=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DomainService instance.')
            self.fail('Error creating the DomainService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.domain_services.delete(resource_group_name=self.resource_group_name,
                                                               domain_service_name=self.domain_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the DomainService instance.')
            self.fail('Error deleting the DomainService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.domain_services.get(resource_group_name=self.resource_group_name,
                                                            domain_service_name=self.domain_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDomainService()


if __name__ == '__main__':
    main()
