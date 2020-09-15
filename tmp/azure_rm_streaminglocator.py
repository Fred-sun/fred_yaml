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
module: azure_rm_streaminglocator
version_added: '2.9'
short_description: Manage Azure StreamingLocator instance.
description:
  - 'Create, update and delete instance of Azure StreamingLocator.'
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
  streaming_locator_name:
    description:
      - The Streaming Locator name.
    required: true
    type: str
  asset_name:
    description:
      - Asset Name
    type: str
  start_time:
    description:
      - The start time of the Streaming Locator.
    type: str
  end_time:
    description:
      - The end time of the Streaming Locator.
    type: str
  streaming_locator_id:
    description:
      - The StreamingLocatorId of the Streaming Locator.
    type: uuid
  streaming_policy_name:
    description:
      - >-
        Name of the Streaming Policy used by this Streaming Locator. Either
        specify the name of Streaming Policy you created or use one of the
        predefined Streaming Policies. The predefined Streaming Policies
        available are: 'Predefined_DownloadOnly',
        'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming',
        'Predefined_ClearKey', 'Predefined_MultiDrmCencStreaming' and
        'Predefined_MultiDrmStreaming'
    type: str
  default_content_key_policy_name:
    description:
      - Name of the default ContentKeyPolicy used by this Streaming Locator.
    type: str
  content_keys:
    description:
      - The ContentKeys used by this Streaming Locator.
    type: list
    suboptions:
      id:
        description:
          - ID of Content Key
        required: true
        type: uuid
      type:
        description:
          - Encryption type of Content Key
        type: str
        choices:
          - CommonEncryptionCenc
          - CommonEncryptionCbcs
          - EnvelopeEncryption
      label_reference_in_streaming_policy:
        description:
          - Label of Content Key as specified in the Streaming Policy
        type: str
      value:
        description:
          - Value of Content Key
        type: str
      policy_name:
        description:
          - ContentKeyPolicy used by Content Key
        type: str
      tracks:
        description:
          - Tracks which use this Content Key
        type: list
        suboptions:
          track_selections:
            description:
              - >-
                TrackSelections is a track property condition list which can
                specify track(s)
            type: list
            suboptions:
              property:
                description:
                  - Track property type
                required: true
                type: str
                choices:
                  - Unknown
                  - FourCC
              operation:
                description:
                  - Track property condition operation
                required: true
                type: str
                choices:
                  - Unknown
                  - Equal
              value:
                description:
                  - Track property value
                type: str
  alternative_media_id:
    description:
      - Alternative Media ID of this Streaming Locator
    type: str
  filters:
    description:
      - A list of asset or account filters which apply to this streaming locator
    type: list
  state:
    description:
      - Assert the state of the StreamingLocator.
      - >-
        Use C(present) to create or update an StreamingLocator and C(absent) to
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
    - name: Creates a Streaming Locator with clear streaming
      azure_rm_streaminglocator: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_locator_name: UserCreatedClearStreamingLocator
        properties:
          asset_name: ClimbingMountRainier
          streaming_policy_name: clearStreamingPolicy
        

    - name: Creates a Streaming Locator with secure streaming
      azure_rm_streaminglocator: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_locator_name: UserCreatedSecureStreamingLocator
        properties:
          asset_name: ClimbingMountRainier
          end_time: '2028-12-31T23:59:59.9999999Z'
          start_time: '2018-03-01T00:00:00Z'
          streaming_policy_name: secureStreamingPolicy
        

    - name: Creates a Streaming Locator with user defined content keys
      azure_rm_streaminglocator: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_locator_name: UserCreatedSecureStreamingLocatorWithUserDefinedContentKeys
        properties:
          asset_name: ClimbingMountRainier
          content_keys:
            - id: 60000000-0000-0000-0000-000000000001
              label_reference_in_streaming_policy: aesDefaultKey
              value: 1UqLohAfWsEGkULYxHjYZg==
            - id: 60000000-0000-0000-0000-000000000004
              label_reference_in_streaming_policy: cencDefaultKey
              value: 4UqLohAfWsEGkULYxHjYZg==
            - id: 60000000-0000-0000-0000-000000000007
              label_reference_in_streaming_policy: cbcsDefaultKey
              value: 7UqLohAfWsEGkULYxHjYZg==
          streaming_locator_id: 90000000-0000-0000-0000-00000000000A
          streaming_policy_name: secureStreamingPolicy
        

    - name: Delete a Streaming Locator
      azure_rm_streaminglocator: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_locator_name: clearStreamingLocator
        

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
asset_name:
  description:
    - Asset Name
  returned: always
  type: str
  sample: null
created:
  description:
    - The creation time of the Streaming Locator.
  returned: always
  type: str
  sample: null
start_time:
  description:
    - The start time of the Streaming Locator.
  returned: always
  type: str
  sample: null
end_time:
  description:
    - The end time of the Streaming Locator.
  returned: always
  type: str
  sample: null
streaming_locator_id:
  description:
    - The StreamingLocatorId of the Streaming Locator.
  returned: always
  type: uuid
  sample: null
streaming_policy_name:
  description:
    - >-
      Name of the Streaming Policy used by this Streaming Locator. Either
      specify the name of Streaming Policy you created or use one of the
      predefined Streaming Policies. The predefined Streaming Policies available
      are: 'Predefined_DownloadOnly', 'Predefined_ClearStreamingOnly',
      'Predefined_DownloadAndClearStreaming', 'Predefined_ClearKey',
      'Predefined_MultiDrmCencStreaming' and 'Predefined_MultiDrmStreaming'
  returned: always
  type: str
  sample: null
default_content_key_policy_name:
  description:
    - Name of the default ContentKeyPolicy used by this Streaming Locator.
  returned: always
  type: str
  sample: null
content_keys:
  description:
    - The ContentKeys used by this Streaming Locator.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - ID of Content Key
      returned: always
      type: uuid
      sample: null
    type:
      description:
        - Encryption type of Content Key
      returned: always
      type: str
      sample: null
    label_reference_in_streaming_policy:
      description:
        - Label of Content Key as specified in the Streaming Policy
      returned: always
      type: str
      sample: null
    value:
      description:
        - Value of Content Key
      returned: always
      type: str
      sample: null
    policy_name:
      description:
        - ContentKeyPolicy used by Content Key
      returned: always
      type: str
      sample: null
    tracks:
      description:
        - Tracks which use this Content Key
      returned: always
      type: list
      sample: null
      contains:
        track_selections:
          description:
            - >-
              TrackSelections is a track property condition list which can
              specify track(s)
          returned: always
          type: list
          sample: null
          contains:
            property:
              description:
                - Track property type
              returned: always
              type: str
              sample: null
            operation:
              description:
                - Track property condition operation
              returned: always
              type: str
              sample: null
            value:
              description:
                - Track property value
              returned: always
              type: str
              sample: null
alternative_media_id:
  description:
    - Alternative Media ID of this Streaming Locator
  returned: always
  type: str
  sample: null
filters:
  description:
    - A list of asset or account filters which apply to this streaming locator
  returned: always
  type: list
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


class AzureRMStreamingLocator(AzureRMModuleBaseExt):
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
            streaming_locator_name=dict(
                type='str',
                required=True
            ),
            asset_name=dict(
                type='str',
                disposition='/asset_name'
            ),
            start_time=dict(
                type='str',
                disposition='/start_time'
            ),
            end_time=dict(
                type='str',
                disposition='/end_time'
            ),
            streaming_locator_id=dict(
                type='uuid',
                disposition='/streaming_locator_id'
            ),
            streaming_policy_name=dict(
                type='str',
                disposition='/streaming_policy_name'
            ),
            default_content_key_policy_name=dict(
                type='str',
                disposition='/default_content_key_policy_name'
            ),
            content_keys=dict(
                type='list',
                disposition='/content_keys',
                elements='dict',
                options=dict(
                    id=dict(
                        type='uuid',
                        disposition='id',
                        required=True
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type',
                        choices=['CommonEncryptionCenc',
                                 'CommonEncryptionCbcs',
                                 'EnvelopeEncryption']
                    ),
                    label_reference_in_streaming_policy=dict(
                        type='str',
                        disposition='label_reference_in_streaming_policy'
                    ),
                    value=dict(
                        type='str',
                        disposition='value'
                    ),
                    policy_name=dict(
                        type='str',
                        updatable=False,
                        disposition='policy_name'
                    ),
                    tracks=dict(
                        type='list',
                        updatable=False,
                        disposition='tracks',
                        elements='dict',
                        options=dict(
                            track_selections=dict(
                                type='list',
                                disposition='track_selections',
                                elements='dict',
                                options=dict(
                                    property=dict(
                                        type='str',
                                        disposition='property',
                                        choices=['Unknown',
                                                 'FourCC'],
                                        required=True
                                    ),
                                    operation=dict(
                                        type='str',
                                        disposition='operation',
                                        choices=['Unknown',
                                                 'Equal'],
                                        required=True
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            alternative_media_id=dict(
                type='str',
                disposition='/alternative_media_id'
            ),
            filters=dict(
                type='list',
                disposition='/filters',
                elements='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.streaming_locator_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStreamingLocator, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.streaming_locators.create(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      streaming_locator_name=self.streaming_locator_name,
                                                                      parameters=self.body)
            else:
                response = self.mgmt_client.streaming_locators.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StreamingLocator instance.')
            self.fail('Error creating the StreamingLocator instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.streaming_locators.delete(resource_group_name=self.resource_group_name,
                                                                  account_name=self.account_name,
                                                                  streaming_locator_name=self.streaming_locator_name)
        except CloudError as e:
            self.log('Error attempting to delete the StreamingLocator instance.')
            self.fail('Error deleting the StreamingLocator instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.streaming_locators.get(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               streaming_locator_name=self.streaming_locator_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStreamingLocator()


if __name__ == '__main__':
    main()
