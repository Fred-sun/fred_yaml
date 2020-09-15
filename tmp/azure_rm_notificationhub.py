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
module: azure_rm_notificationhub
version_added: '2.9'
short_description: Manage Azure NotificationHub instance.
description:
  - 'Create, update and delete instance of Azure NotificationHub.'
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
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  sku:
    description:
      - The sku of the created namespace
    type: dict
    suboptions:
      name:
        description:
          - Name of the notification hub sku
        required: true
        type: str
        choices:
          - Free
          - Basic
          - Standard
      tier:
        description:
          - The tier of particular sku
        type: str
      size:
        description:
          - The Sku size
        type: str
      family:
        description:
          - The Sku Family
        type: str
      capacity:
        description:
          - The capacity of the resource
        type: integer
  name:
    description:
      - The NotificationHub name.
    type: str
  registration_ttl:
    description:
      - The RegistrationTtl of the created NotificationHub
    type: str
  authorization_rules:
    description:
      - The AuthorizationRules of the created NotificationHub
    type: list
    suboptions:
      rights:
        description:
          - The rights associated with the rule.
        type: list
      primary_key:
        description:
          - >-
            A base64-encoded 256-bit primary key for signing and validating the
            SAS token.
        type: str
      secondary_key:
        description:
          - >-
            A base64-encoded 256-bit primary key for signing and validating the
            SAS token.
        type: str
      key_name:
        description:
          - A string that describes the authorization rule.
        type: str
      claim_type:
        description:
          - A string that describes the claim type
        type: str
      claim_value:
        description:
          - A string that describes the claim value
        type: str
      modified_time:
        description:
          - The last modified time for this rule
        type: str
      created_time:
        description:
          - The created time for this rule
        type: str
      revision:
        description:
          - The revision number for the rule
        type: integer
  baidu_api_key:
    description:
      - Baidu Api Key.
    type: str
  baidu_end_point:
    description:
      - Baidu Endpoint.
    type: str
  baidu_secret_key:
    description:
      - Baidu Secret Key
    type: str
  client_id:
    description:
      - The client identifier.
    type: str
  client_secret:
    description:
      - The credential secret access key.
    type: str
  auth_token_url:
    description:
      - The URL of the authorization token.
    type: str
  mpns_certificate:
    description:
      - The MPNS certificate.
    type: str
  certificate_key:
    description:
      - The certificate key for this credential.
    type: str
  thumbprint:
    description:
      - The MPNS certificate Thumbprint
    type: str
  gcm_endpoint:
    description:
      - >-
        The FCM legacy endpoint. Default value is
        'https://fcm.googleapis.com/fcm/send'
    type: str
  google_api_key:
    description:
      - The Google API key.
    type: str
  package_sid:
    description:
      - The package ID for this credential.
    type: str
  secret_key:
    description:
      - The secret key.
    type: str
  windows_live_endpoint:
    description:
      - The Windows Live endpoint.
    type: str
  apns_certificate:
    description:
      - The APNS certificate. Specify if using Certificate Authentication Mode.
    type: str
  apns_credential_properties_certificate_key:
    description:
      - The APNS certificate password if it exists.
    type: str
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
    type: str
  apns_credential_properties_thumbprint:
    description:
      - >-
        The APNS certificate thumbprint. Specify if using Certificate
        Authentication Mode.
    type: str
  key_id:
    description:
      - >-
        A 10-character key identifier (kid) key, obtained from your developer
        account. Specify if using Token Authentication Mode.
    type: str
  app_name:
    description:
      - >-
        The name of the application or BundleId. Specify if using Token
        Authentication Mode.
    type: str
  app_id:
    description:
      - >-
        The issuer (iss) registered claim key. The value is a 10-character
        TeamId, obtained from your developer account. Specify if using Token
        Authentication Mode.
    type: str
  token:
    description:
      - >-
        Provider Authentication Token, obtained through your developer account.
        Specify if using Token Authentication Mode.
    type: str
  state:
    description:
      - Assert the state of the NotificationHub.
      - >-
        Use C(present) to create or update an NotificationHub and C(absent) to
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
    - name: NotificationHubCreate
      azure_rm_notificationhub: 
        namespace_name: nh-sdk-ns
        notification_hub_name: nh-sdk-hub
        resource_group_name: 5ktrial
        location: eastus
        properties: {}
        

    - name: NotificationHubDelete
      azure_rm_notificationhub: 
        namespace_name: nh-sdk-ns
        notification_hub_name: nh-sdk-hub
        resource_group_name: 5ktrial
        

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
    - The APNS certificate. Specify if using Certificate Authentication Mode.
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
      The APNS endpoint of this credential. If using Certificate Authentication
      Mode and Sandbox specify 'gateway.sandbox.push.apple.com'. If using
      Certificate Authentication Mode and Production specify
      'gateway.push.apple.com'. If using Token Authentication Mode and Sandbox
      specify 'https://api.development.push.apple.com:443/3/device'. If using
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
      The issuer (iss) registered claim key. The value is a 10-character TeamId,
      obtained from your developer account. Specify if using Token
      Authentication Mode.
  returned: always
  type: str
  sample: null
token:
  description:
    - >-
      Provider Authentication Token, obtained through your developer account.
      Specify if using Token Authentication Mode.
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
    from azure.mgmt.notification import NotificationHubsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNotificationHub(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['Free',
                                 'Basic',
                                 'Standard'],
                        required=True
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    size=dict(
                        type='str',
                        disposition='size'
                    ),
                    family=dict(
                        type='str',
                        disposition='family'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            registration_ttl=dict(
                type='str',
                disposition='/registration_ttl'
            ),
            authorization_rules=dict(
                type='list',
                disposition='/authorization_rules',
                elements='dict',
                options=dict(
                    rights=dict(
                        type='list',
                        disposition='rights',
                        elements='sealed-choice'
                    ),
                    primary_key=dict(
                        type='str',
                        updatable=False,
                        disposition='primary_key'
                    ),
                    secondary_key=dict(
                        type='str',
                        updatable=False,
                        disposition='secondary_key'
                    ),
                    key_name=dict(
                        type='str',
                        updatable=False,
                        disposition='key_name'
                    ),
                    claim_type=dict(
                        type='str',
                        updatable=False,
                        disposition='claim_type'
                    ),
                    claim_value=dict(
                        type='str',
                        updatable=False,
                        disposition='claim_value'
                    ),
                    modified_time=dict(
                        type='str',
                        updatable=False,
                        disposition='modified_time'
                    ),
                    created_time=dict(
                        type='str',
                        updatable=False,
                        disposition='created_time'
                    ),
                    revision=dict(
                        type='integer',
                        updatable=False,
                        disposition='revision'
                    )
                )
            ),
            baidu_api_key=dict(
                type='str',
                disposition='/baidu_api_key'
            ),
            baidu_end_point=dict(
                type='str',
                disposition='/baidu_end_point'
            ),
            baidu_secret_key=dict(
                type='str',
                disposition='/baidu_secret_key'
            ),
            client_id=dict(
                type='str',
                disposition='/client_id'
            ),
            client_secret=dict(
                type='str',
                disposition='/client_secret'
            ),
            auth_token_url=dict(
                type='str',
                disposition='/auth_token_url'
            ),
            mpns_certificate=dict(
                type='str',
                disposition='/mpns_certificate'
            ),
            certificate_key=dict(
                type='str',
                disposition='/certificate_key'
            ),
            thumbprint=dict(
                type='str',
                disposition='/thumbprint'
            ),
            gcm_endpoint=dict(
                type='str',
                disposition='/gcm_endpoint'
            ),
            google_api_key=dict(
                type='str',
                disposition='/google_api_key'
            ),
            package_sid=dict(
                type='str',
                disposition='/package_sid'
            ),
            secret_key=dict(
                type='str',
                disposition='/secret_key'
            ),
            windows_live_endpoint=dict(
                type='str',
                disposition='/windows_live_endpoint'
            ),
            apns_certificate=dict(
                type='str',
                disposition='/apns_certificate'
            ),
            apns_credential_properties_certificate_key=dict(
                type='str',
                disposition='/apns_credential_properties_certificate_key'
            ),
            endpoint=dict(
                type='str',
                disposition='/endpoint'
            ),
            apns_credential_properties_thumbprint=dict(
                type='str',
                disposition='/apns_credential_properties_thumbprint'
            ),
            key_id=dict(
                type='str',
                disposition='/key_id'
            ),
            app_name=dict(
                type='str',
                disposition='/app_name'
            ),
            app_id=dict(
                type='str',
                disposition='/app_id'
            ),
            token=dict(
                type='str',
                disposition='/token'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.notification_hub_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNotificationHub, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(NotificationHubsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

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
            response = self.mgmt_client.notification_hubs.create_or_update(resource_group_name=self.resource_group_name,
                                                                           namespace_name=self.namespace_name,
                                                                           notification_hub_name=self.notification_hub_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the NotificationHub instance.')
            self.fail('Error creating the NotificationHub instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.notification_hubs.delete(resource_group_name=self.resource_group_name,
                                                                 namespace_name=self.namespace_name,
                                                                 notification_hub_name=self.notification_hub_name)
        except CloudError as e:
            self.log('Error attempting to delete the NotificationHub instance.')
            self.fail('Error deleting the NotificationHub instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.notification_hubs.get(resource_group_name=self.resource_group_name,
                                                              namespace_name=self.namespace_name,
                                                              notification_hub_name=self.notification_hub_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNotificationHub()


if __name__ == '__main__':
    main()
