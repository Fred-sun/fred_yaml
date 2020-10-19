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
module: azure_rm_contentkeypolicy
version_added: '2.9'
short_description: Manage Azure ContentKeyPolicy instance.
description:
  - 'Create, update and delete instance of Azure ContentKeyPolicy.'
options:
  resource_group_name:
    description:
      - The name of the resource group within the Azure subscription.
    required: true
    type: str
  account_name:
    description:
      - The Media Services account name.
    required: true
    type: str
  content_key_policy_name:
    description:
      - The Content Key Policy name.
    required: true
    type: str
  description:
    description:
      - A description for the Policy.
    type: str
  options:
    description:
      - The Key Policy options.
    type: list
    suboptions:
      policy_option_id:
        description:
          - The legacy Policy Option ID.
        type: uuid
      name:
        description:
          - The Policy Option description.
        type: str
      configuration:
        description:
          - The key delivery configuration.
        required: true
        type: dict
        suboptions:
          odata_type:
            description:
              - The discriminator for derived types.
            required: true
            type: str
      restriction:
        description:
          - >-
            The requirements that must be met to deliver keys with this
            configuration
        required: true
        type: dict
        suboptions:
          odata_type:
            description:
              - The discriminator for derived types.
            required: true
            type: str
  state:
    description:
      - Assert the state of the ContentKeyPolicy.
      - >-
        Use C(present) to create or update an ContentKeyPolicy and C(absent) to
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
    - name: Creates a Content Key Policy with ClearKey option and Token Restriction
      azure_rm_contentkeypolicy: 
        account_name: contosomedia
        content_key_policy_name: PolicyWithClearKeyOptionAndSwtTokenRestriction
        resource_group_name: contoso
        properties:
          description: ArmPolicyDescription
          options:
            - name: ClearKeyOption
              configuration:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyClearKeyConfiguration'
              restriction:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyTokenRestriction'
                audience: 'urn:audience'
                issuer: 'urn:issuer'
                primary_verification_key:
                  '@odata.type': '#Microsoft.Media.ContentKeyPolicySymmetricTokenKey'
                  key_value: AAAAAAAAAAAAAAAAAAAAAA==
                restriction_token_type: Swt
        

    - name: Creates a Content Key Policy with PlayReady option and Open Restriction
      azure_rm_contentkeypolicy: 
        account_name: contosomedia
        content_key_policy_name: PolicyWithPlayReadyOptionAndOpenRestriction
        resource_group_name: contoso
        properties:
          description: ArmPolicyDescription
          options:
            - name: ArmPolicyOptionName
              configuration:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyPlayReadyConfiguration'
                licenses:
                  - allow_test_devices: true
                    begin_date: '2017-10-16T18:22:53.46Z'
                    content_key_location:
                      '@odata.type': >-
                        #Microsoft.Media.ContentKeyPolicyPlayReadyContentEncryptionKeyFromHeader
                    content_type: UltraVioletDownload
                    license_type: Persistent
                    play_right:
                      allow_passing_video_content_to_unknown_output: NotAllowed
                      digital_video_only_content_restriction: false
                      image_constraint_for_analog_component_video_restriction: true
                      image_constraint_for_analog_computer_monitor_restriction: false
                      scms_restriction: 2
              restriction:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyOpenRestriction'
        

    - name: Creates a Content Key Policy with Widevine option and Token Restriction
      azure_rm_contentkeypolicy: 
        account_name: contosomedia
        content_key_policy_name: PolicyWithWidevineOptionAndJwtTokenRestriction
        resource_group_name: contoso
        properties:
          description: ArmPolicyDescription
          options:
            - name: widevineoption
              configuration:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyWidevineConfiguration'
                widevine_template: >-
                  {"allowed_track_types":"SD_HD","content_key_specs":[{"track_type":"SD","security_level":1,"required_output_protection":{"hdcp":"HDCP_V2"}}],"policy_overrides":{"can_play":true,"can_persist":true,"can_renew":false}}
              restriction:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyTokenRestriction'
                alternate_verification_keys:
                  - '@odata.type': '#Microsoft.Media.ContentKeyPolicySymmetricTokenKey'
                    key_value: AAAAAAAAAAAAAAAAAAAAAA==
                audience: 'urn:audience'
                issuer: 'urn:issuer'
                primary_verification_key:
                  '@odata.type': '#Microsoft.Media.ContentKeyPolicyRsaTokenKey'
                  exponent: AQAB
                  modulus: AQAD
                restriction_token_type: Jwt
        

    - name: Creates a Content Key Policy with multiple options
      azure_rm_contentkeypolicy: 
        account_name: contosomedia
        content_key_policy_name: PolicyCreatedWithMultipleOptions
        resource_group_name: contoso
        properties:
          description: ArmPolicyDescription
          options:
            - name: ClearKeyOption
              configuration:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyClearKeyConfiguration'
              restriction:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyTokenRestriction'
                audience: 'urn:audience'
                issuer: 'urn:issuer'
                primary_verification_key:
                  '@odata.type': '#Microsoft.Media.ContentKeyPolicySymmetricTokenKey'
                  key_value: AAAAAAAAAAAAAAAAAAAAAA==
                restriction_token_type: Swt
            - name: widevineoption
              configuration:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyWidevineConfiguration'
                widevine_template: >-
                  {"allowed_track_types":"SD_HD","content_key_specs":[{"track_type":"SD","security_level":1,"required_output_protection":{"hdcp":"HDCP_V2"}}],"policy_overrides":{"can_play":true,"can_persist":true,"can_renew":false}}
              restriction:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyOpenRestriction'
        

    - name: Delete a Key Policy
      azure_rm_contentkeypolicy: 
        account_name: contosomedia
        content_key_policy_name: PolicyWithPlayReadyOptionAndOpenRestriction
        resource_group_name: contoso
        

    - name: Update a Content Key Policy
      azure_rm_contentkeypolicy: 
        account_name: contosomedia
        content_key_policy_name: PolicyWithClearKeyOptionAndTokenRestriction
        resource_group_name: contoso
        properties:
          description: Updated Policy
          options:
            - name: ClearKeyOption
              configuration:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyClearKeyConfiguration'
              restriction:
                '@odata.type': '#Microsoft.Media.ContentKeyPolicyOpenRestriction'
        

'''

RETURN = '''
id:
  description:
    - >-
      Fully qualified resource Id for the resource. Ex -
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource. Ex- Microsoft.Compute/virtualMachines or
      Microsoft.Storage/storageAccounts.
  returned: always
  type: str
  sample: null
policy_id:
  description:
    - The legacy Policy ID.
  returned: always
  type: uuid
  sample: null
created:
  description:
    - The creation date of the Policy
  returned: always
  type: str
  sample: null
last_modified:
  description:
    - The last modified date of the Policy
  returned: always
  type: str
  sample: null
description:
  description:
    - A description for the Policy.
  returned: always
  type: str
  sample: null
options:
  description:
    - The Key Policy options.
  returned: always
  type: list
  sample: null
  contains:
    policy_option_id:
      description:
        - The legacy Policy Option ID.
      returned: always
      type: uuid
      sample: null
    name:
      description:
        - The Policy Option description.
      returned: always
      type: str
      sample: null
    configuration:
      description:
        - The key delivery configuration.
      returned: always
      type: dict
      sample: null
      contains:
        odata_type:
          description:
            - The discriminator for derived types.
          returned: always
          type: str
          sample: null
    restriction:
      description:
        - >-
          The requirements that must be met to deliver keys with this
          configuration
      returned: always
      type: dict
      sample: null
      contains:
        odata_type:
          description:
            - The discriminator for derived types.
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
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMContentKeyPolicy(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            content_key_policy_name=dict(
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            options=dict(
                type='list',
                disposition='/options',
                elements='dict',
                options=dict(
                    policy_option_id=dict(
                        type='uuid',
                        updatable=False,
                        disposition='policy_option_id'
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    configuration=dict(
                        type='dict',
                        disposition='configuration',
                        required=True,
                        options=dict(
                            odata_type=dict(
                                type='str',
                                disposition='odata_type',
                                required=True
                            )
                        )
                    ),
                    restriction=dict(
                        type='dict',
                        disposition='restriction',
                        required=True,
                        options=dict(
                            odata_type=dict(
                                type='str',
                                disposition='odata_type',
                                required=True
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.content_key_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContentKeyPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
            response = self.mgmt_client.content_key_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                              account_name=self.account_name,
                                                                              content_key_policy_name=self.content_key_policy_name,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ContentKeyPolicy instance.')
            self.fail('Error creating the ContentKeyPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.content_key_policies.delete(resource_group_name=self.resource_group_name,
                                                                    account_name=self.account_name,
                                                                    content_key_policy_name=self.content_key_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the ContentKeyPolicy instance.')
            self.fail('Error deleting the ContentKeyPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.content_key_policies.get(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name,
                                                                 content_key_policy_name=self.content_key_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContentKeyPolicy()


if __name__ == '__main__':
    main()
