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
module: azure_rm_streaminglocator_info
version_added: '2.9'
short_description: Get StreamingLocator info.
description:
  - Get info of StreamingLocator.
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
  filter:
    description:
      - Restricts the set of items returned.
    type: str
  top:
    description:
      - >-
        Specifies a non-negative integer n that limits the number of items
        returned from a collection. The service returns the number of available
        items up to but not greater than the specified value n.
    type: integer
  orderby:
    description:
      - Specifies the key by which the result collection should be ordered.
    type: str
  streaming_locator_name:
    description:
      - The Streaming Locator name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists Streaming Locators
      azure_rm_streaminglocator_info: 
        account_name: contosomedia
        resource_group_name: contoso
        

    - name: Get a Streaming Locator by name
      azure_rm_streaminglocator_info: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_locator_name: clearStreamingLocator
        

'''

RETURN = '''
streaming_locators:
  description: >-
    A list of dict results where the key is the name of the StreamingLocator and
    the values are the facts for that StreamingLocator.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A collection of StreamingLocator items.
      returned: always
      type: list
      sample: null
      contains:
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
              Name of the Streaming Policy used by this Streaming Locator.
              Either specify the name of Streaming Policy you created or use one
              of the predefined Streaming Policies. The predefined Streaming
              Policies available are: 'Predefined_DownloadOnly',
              'Predefined_ClearStreamingOnly',
              'Predefined_DownloadAndClearStreaming', 'Predefined_ClearKey',
              'Predefined_MultiDrmCencStreaming' and
              'Predefined_MultiDrmStreaming'
          returned: always
          type: str
          sample: null
        default_content_key_policy_name:
          description:
            - >-
              Name of the default ContentKeyPolicy used by this Streaming
              Locator.
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
                      TrackSelections is a track property condition list which
                      can specify track(s)
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
            - >-
              A list of asset or account filters which apply to this streaming
              locator
          returned: always
          type: list
          sample: null
    odata_next_link:
      description:
        - >-
          A link to the next page of the collection (when the collection
          contains too many results to return in one response).
      returned: always
      type: str
      sample: null
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
          predefined Streaming Policies. The predefined Streaming Policies
          available are: 'Predefined_DownloadOnly',
          'Predefined_ClearStreamingOnly',
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
        - >-
          A list of asset or account filters which apply to this streaming
          locator
      returned: always
      type: list
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMStreamingLocatorInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            ),
            streaming_locator_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.streaming_locator_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMStreamingLocatorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.streaming_locator_name is not None):
            self.results['streaming_locators'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['streaming_locators'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.streaming_locators.get(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               streaming_locator_name=self.streaming_locator_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.streaming_locators.list(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                filter=self.filter,
                                                                top=self.top,
                                                                orderby=self.orderby)
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
    AzureRMStreamingLocatorInfo()


if __name__ == '__main__':
    main()
