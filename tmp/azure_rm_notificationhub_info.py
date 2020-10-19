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
module: azure_rm_notificationhub_info
version_added: '2.9'
short_description: Get NotificationHub info.
description:
  - Get info of NotificationHub.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name.
    required: true
    type: str
  notification_hub_name:
    description:
      - The notification hub name.
    type: str
  authorization_rule_name:
    description:
      - authorization rule name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: NotificationHubGet
      azure_rm_notificationhub_info: 
        namespace_name: nh-sdk-ns
        notification_hub_name: nh-sdk-hub
        resource_group_name: 5ktrial
        

    - name: NotificationHubAuthorizationRuleGet
      azure_rm_notificationhub_info: 
        authorization_rule_name: DefaultListenSharedAccessSignature
        namespace_name: nh-sdk-ns
        notification_hub_name: nh-sdk-hub
        resource_group_name: 5ktrial
        

    - name: NotificationHubListByNameSpace
      azure_rm_notificationhub_info: 
        namespace_name: nh-sdk-ns
        resource_group_name: 5ktrial
        

    - name: NotificationHubAuthorizationRuleListAll
      azure_rm_notificationhub_info: 
        namespace_name: nh-sdk-ns
        notification_hub_name: nh-sdk-hub
        resource_group_name: 5ktrial
        

'''

RETURN = '''
notification_hubs:
  description: >-
    A list of dict results where the key is the name of the NotificationHub and
    the values are the facts for that NotificationHub.
  returned: always
  type: complex
  contains:
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
    sku:
      description:
        - The sku of the created namespace
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of the notification hub sku
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The tier of particular sku
          returned: always
          type: str
          sample: null
        size:
          description:
            - The Sku size
          returned: always
          type: str
          sample: null
        family:
          description:
            - The Sku Family
          returned: always
          type: str
          sample: null
        capacity:
          description:
            - The capacity of the resource
          returned: always
          type: integer
          sample: null
    name_properties_name:
      description:
        - The NotificationHub name.
      returned: always
      type: str
      sample: null
    registration_ttl:
      description:
        - The RegistrationTtl of the created NotificationHub
      returned: always
      type: str
      sample: null
    authorization_rules:
      description:
        - The AuthorizationRules of the created NotificationHub
      returned: always
      type: list
      sample: null
      contains:
        rights:
          description:
            - The rights associated with the rule.
          returned: always
          type: list
          sample: null
        primary_key:
          description:
            - >-
              A base64-encoded 256-bit primary key for signing and validating
              the SAS token.
          returned: always
          type: str
          sample: null
        secondary_key:
          description:
            - >-
              A base64-encoded 256-bit primary key for signing and validating
              the SAS token.
          returned: always
          type: str
          sample: null
        key_name:
          description:
            - A string that describes the authorization rule.
          returned: always
          type: str
          sample: null
        claim_type:
          description:
            - A string that describes the claim type
          returned: always
          type: str
          sample: null
        claim_value:
          description:
            - A string that describes the claim value
          returned: always
          type: str
          sample: null
        modified_time:
          description:
            - The last modified time for this rule
          returned: always
          type: str
          sample: null
        created_time:
          description:
            - The created time for this rule
          returned: always
          type: str
          sample: null
        revision:
          description:
            - The revision number for the rule
          returned: always
          type: integer
          sample: null
    baidu_api_key:
      description:
        - Baidu Api Key.
      returned: always
      type: str
      sample: null
    baidu_end_point:
      description:
        - Baidu Endpoint.
      returned: always
      type: str
      sample: null
    baidu_secret_key:
      description:
        - Baidu Secret Key
      returned: always
      type: str
      sample: null
    client_id:
      description:
        - The client identifier.
      returned: always
      type: str
      sample: null
    client_secret:
      description:
        - The credential secret access key.
      returned: always
      type: str
      sample: null
    auth_token_url:
      description:
        - The URL of the authorization token.
      returned: always
      type: str
      sample: null
    mpns_certificate:
      description:
        - The MPNS certificate.
      returned: always
      type: str
      sample: null
    certificate_key_properties_mpns_credential_properties_certificate_key:
      description:
        - The certificate key for this credential.
      returned: always
      type: str
      sample: null
    thumbprint_properties_mpns_credential_properties_thumbprint:
      description:
        - The MPNS certificate Thumbprint
      returned: always
      type: str
      sample: null
    gcm_endpoint:
      description:
        - >-
          The FCM legacy endpoint. Default value is
          'https://fcm.googleapis.com/fcm/send'
      returned: always
      type: str
      sample: null
    google_api_key:
      description:
        - The Google API key.
      returned: always
      type: str
      sample: null
    package_sid:
      description:
        - The package ID for this credential.
      returned: always
      type: str
      sample: null
    secret_key:
      description:
        - The secret key.
      returned: always
      type: str
      sample: null
    windows_live_endpoint:
      description:
        - The Windows Live endpoint.
      returned: always
      type: str
      sample: null
    apns_certificate:
      description:
        - >-
          The APNS certificate. Specify if using Certificate Authentication
          Mode.
      returned: always
      type: str
      sample: null
    certificate_key_properties_apns_credential_properties_certificate_key:
      description:
        - The APNS certificate password if it exists.
      returned: always
      type: str
      sample: null
    endpoint:
      description:
        - >-
          The APNS endpoint of this credential. If using Certificate
          Authentication Mode and Sandbox specify
          'gateway.sandbox.push.apple.com'. If using Certificate Authentication
          Mode and Production specify 'gateway.push.apple.com'. If using Token
          Authentication Mode and Sandbox specify
          'https://api.development.push.apple.com:443/3/device'. If using Token
          Authentication Mode and Production specify
          'https://api.push.apple.com:443/3/device'.
      returned: always
      type: str
      sample: null
    thumbprint_properties_apns_credential_properties_thumbprint:
      description:
        - >-
          The APNS certificate thumbprint. Specify if using Certificate
          Authentication Mode.
      returned: always
      type: str
      sample: null
    key_id:
      description:
        - >-
          A 10-character key identifier (kid) key, obtained from your developer
          account. Specify if using Token Authentication Mode.
      returned: always
      type: str
      sample: null
    app_name:
      description:
        - >-
          The name of the application or BundleId. Specify if using Token
          Authentication Mode.
      returned: always
      type: str
      sample: null
    app_id:
      description:
        - >-
          The issuer (iss) registered claim key. The value is a 10-character
          TeamId, obtained from your developer account. Specify if using Token
          Authentication Mode.
      returned: always
      type: str
      sample: null
    token:
      description:
        - >-
          Provider Authentication Token, obtained through your developer
          account. Specify if using Token Authentication Mode.
      returned: always
      type: str
      sample: null
    rights:
      description:
        - The rights associated with the rule.
      returned: always
      type: list
      sample: null
    primary_key:
      description:
        - >-
          A base64-encoded 256-bit primary key for signing and validating the
          SAS token.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - >-
          A base64-encoded 256-bit primary key for signing and validating the
          SAS token.
      returned: always
      type: str
      sample: null
    key_name:
      description:
        - A string that describes the authorization rule.
      returned: always
      type: str
      sample: null
    claim_type:
      description:
        - A string that describes the claim type
      returned: always
      type: str
      sample: null
    claim_value:
      description:
        - A string that describes the claim value
      returned: always
      type: str
      sample: null
    modified_time:
      description:
        - The last modified time for this rule
      returned: always
      type: str
      sample: null
    created_time:
      description:
        - The created time for this rule
      returned: always
      type: str
      sample: null
    revision:
      description:
        - The revision number for the rule
      returned: always
      type: integer
      sample: null
    value:
      description:
        - |-
          Result of the List NotificationHub operation.
          Result of the List AuthorizationRules operation.
      returned: always
      type: list
      sample: null
      contains:
        name_properties_name:
          description:
            - The NotificationHub name.
          returned: always
          type: str
          sample: null
        registration_ttl:
          description:
            - The RegistrationTtl of the created NotificationHub
          returned: always
          type: str
          sample: null
        authorization_rules:
          description:
            - The AuthorizationRules of the created NotificationHub
          returned: always
          type: list
          sample: null
          contains:
            rights:
              description:
                - The rights associated with the rule.
              returned: always
              type: list
              sample: null
            primary_key:
              description:
                - >-
                  A base64-encoded 256-bit primary key for signing and
                  validating the SAS token.
              returned: always
              type: str
              sample: null
            secondary_key:
              description:
                - >-
                  A base64-encoded 256-bit primary key for signing and
                  validating the SAS token.
              returned: always
              type: str
              sample: null
            key_name:
              description:
                - A string that describes the authorization rule.
              returned: always
              type: str
              sample: null
            claim_type:
              description:
                - A string that describes the claim type
              returned: always
              type: str
              sample: null
            claim_value:
              description:
                - A string that describes the claim value
              returned: always
              type: str
              sample: null
            modified_time:
              description:
                - The last modified time for this rule
              returned: always
              type: str
              sample: null
            created_time:
              description:
                - The created time for this rule
              returned: always
              type: str
              sample: null
            revision:
              description:
                - The revision number for the rule
              returned: always
              type: integer
              sample: null
        baidu_api_key:
          description:
            - Baidu Api Key.
          returned: always
          type: str
          sample: null
        baidu_end_point:
          description:
            - Baidu Endpoint.
          returned: always
          type: str
          sample: null
        baidu_secret_key:
          description:
            - Baidu Secret Key
          returned: always
          type: str
          sample: null
        client_id:
          description:
            - The client identifier.
          returned: always
          type: str
          sample: null
        client_secret:
          description:
            - The credential secret access key.
          returned: always
          type: str
          sample: null
        auth_token_url:
          description:
            - The URL of the authorization token.
          returned: always
          type: str
          sample: null
        mpns_certificate:
          description:
            - The MPNS certificate.
          returned: always
          type: str
          sample: null
        certificate_key_properties_mpns_credential_properties_certificate_key:
          description:
            - The certificate key for this credential.
          returned: always
          type: str
          sample: null
        thumbprint_properties_mpns_credential_properties_thumbprint:
          description:
            - The MPNS certificate Thumbprint
          returned: always
          type: str
          sample: null
        gcm_endpoint:
          description:
            - >-
              The FCM legacy endpoint. Default value is
              'https://fcm.googleapis.com/fcm/send'
          returned: always
          type: str
          sample: null
        google_api_key:
          description:
            - The Google API key.
          returned: always
          type: str
          sample: null
        package_sid:
          description:
            - The package ID for this credential.
          returned: always
          type: str
          sample: null
        secret_key:
          description:
            - The secret key.
          returned: always
          type: str
          sample: null
        windows_live_endpoint:
          description:
            - The Windows Live endpoint.
          returned: always
          type: str
          sample: null
        apns_certificate:
          description:
            - >-
              The APNS certificate. Specify if using Certificate Authentication
              Mode.
          returned: always
          type: str
          sample: null
        certificate_key_properties_apns_credential_properties_certificate_key:
          description:
            - The APNS certificate password if it exists.
          returned: always
          type: str
          sample: null
        endpoint:
          description:
            - >-
              The APNS endpoint of this credential. If using Certificate
              Authentication Mode and Sandbox specify
              'gateway.sandbox.push.apple.com'. If using Certificate
              Authentication Mode and Production specify
              'gateway.push.apple.com'. If using Token Authentication Mode and
              Sandbox specify
              'https://api.development.push.apple.com:443/3/device'. If using
              Token Authentication Mode and Production specify
              'https://api.push.apple.com:443/3/device'.
          returned: always
          type: str
          sample: null
        thumbprint_properties_apns_credential_properties_thumbprint:
          description:
            - >-
              The APNS certificate thumbprint. Specify if using Certificate
              Authentication Mode.
          returned: always
          type: str
          sample: null
        key_id:
          description:
            - >-
              A 10-character key identifier (kid) key, obtained from your
              developer account. Specify if using Token Authentication Mode.
          returned: always
          type: str
          sample: null
        app_name:
          description:
            - >-
              The name of the application or BundleId. Specify if using Token
              Authentication Mode.
          returned: always
          type: str
          sample: null
        app_id:
          description:
            - >-
              The issuer (iss) registered claim key. The value is a 10-character
              TeamId, obtained from your developer account. Specify if using
              Token Authentication Mode.
          returned: always
          type: str
          sample: null
        token:
          description:
            - >-
              Provider Authentication Token, obtained through your developer
              account. Specify if using Token Authentication Mode.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of NotificationHub

          Link to the next set of results. Not empty if Value contains
          incomplete list of AuthorizationRules
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
    from azure.mgmt.notification import NotificationHubsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNotificationHubInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            ),
            notification_hub_name=dict(
                type='str'
            ),
            authorization_rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.notification_hub_name = None
        self.authorization_rule_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMNotificationHubInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NotificationHubsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.notification_hub_name is not None and
            self.authorization_rule_name is not None):
            self.results['notification_hubs'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.notification_hub_name is not None):
            self.results['notification_hubs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.notification_hub_name is not None):
            self.results['notification_hubs'] = self.format_item(self.listauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['notification_hubs'] = self.format_item(self.list())
        return self.results

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.notification_hubs.get_authorization_rule(resource_group_name=self.resource_group_name,
                                                                                 namespace_name=self.namespace_name,
                                                                                 notification_hub_name=self.notification_hub_name,
                                                                                 authorization_rule_name=self.authorization_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.notification_hubs.get(resource_group_name=self.resource_group_name,
                                                              namespace_name=self.namespace_name,
                                                              notification_hub_name=self.notification_hub_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.notification_hubs.list_authorization_rule(resource_group_name=self.resource_group_name,
                                                                                  namespace_name=self.namespace_name,
                                                                                  notification_hub_name=self.notification_hub_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.notification_hubs.list(resource_group_name=self.resource_group_name,
                                                               namespace_name=self.namespace_name)
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
    AzureRMNotificationHubInfo()


if __name__ == '__main__':
    main()
