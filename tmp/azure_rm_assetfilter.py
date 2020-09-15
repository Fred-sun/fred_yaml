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
module: azure_rm_assetfilter
version_added: '2.9'
short_description: Manage Azure AssetFilter instance.
description:
  - 'Create, update and delete instance of Azure AssetFilter.'
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
  asset_name:
    description:
      - The Asset name.
    required: true
    type: str
  filter_name:
    description:
      - The Asset Filter name
    required: true
    type: str
  presentation_time_range:
    description:
      - The presentation time range.
    type: dict
    suboptions:
      start_timestamp:
        description:
          - The absolute start time boundary.
        type: integer
      end_timestamp:
        description:
          - The absolute end time boundary.
        type: integer
      presentation_window_duration:
        description:
          - The relative to end sliding window.
        type: integer
      live_backoff_duration:
        description:
          - The relative to end right edge.
        type: integer
      timescale:
        description:
          - The time scale of time stamps.
        type: integer
      force_end_timestamp:
        description:
          - The indicator of forcing existing of end time stamp.
        type: bool
  tracks:
    description:
      - The tracks selection conditions.
    type: list
    suboptions:
      track_selections:
        description:
          - The track selections.
        required: true
        type: list
        suboptions:
          property:
            description:
              - The track property type.
            required: true
            type: str
            choices:
              - Unknown
              - Type
              - Name
              - Language
              - FourCC
              - Bitrate
          value:
            description:
              - The track property value.
            required: true
            type: str
          operation:
            description:
              - The track property condition operation.
            required: true
            type: str
            choices:
              - Equal
              - NotEqual
  bitrate:
    description:
      - The first quality bitrate.
    type: integer
  state:
    description:
      - Assert the state of the AssetFilter.
      - >-
        Use C(present) to create or update an AssetFilter and C(absent) to
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
    - name: Create an Asset Filter
      azure_rm_assetfilter: 
        account_name: contosomedia
        asset_name: ClimbingMountRainer
        filter_name: newAssetFilter
        resource_group_name: contoso
        properties:
          first_quality:
            bitrate: 128000
          presentation_time_range:
            end_timestamp: 170000000
            force_end_timestamp: false
            live_backoff_duration: 0
            presentation_window_duration: 9223372036854776000
            start_timestamp: 0
            timescale: 10000000
          tracks:
            - track_selections:
                - operation: Equal
                  property: Type
                  value: Audio
                - operation: NotEqual
                  property: Language
                  value: en
                - operation: NotEqual
                  property: FourCC
                  value: EC-3
            - track_selections:
                - operation: Equal
                  property: Type
                  value: Video
                - operation: Equal
                  property: Bitrate
                  value: 3000000-5000000
        

    - name: Delete an Asset Filter
      azure_rm_assetfilter: 
        account_name: contosomedia
        asset_name: ClimbingMountRainer
        filter_name: assetFilterWithTimeWindowAndTrack
        resource_group_name: contoso
        

    - name: Update an Asset Filter
      azure_rm_assetfilter: 
        account_name: contosomedia
        asset_name: ClimbingMountRainer
        filter_name: assetFilterWithTimeWindowAndTrack
        resource_group_name: contoso
        properties:
          first_quality:
            bitrate: 128000
          presentation_time_range:
            end_timestamp: 170000000
            force_end_timestamp: false
            live_backoff_duration: 0
            presentation_window_duration: 9223372036854776000
            start_timestamp: 10
            timescale: 10000000
        

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
presentation_time_range:
  description:
    - The presentation time range.
  returned: always
  type: dict
  sample: null
  contains:
    start_timestamp:
      description:
        - The absolute start time boundary.
      returned: always
      type: integer
      sample: null
    end_timestamp:
      description:
        - The absolute end time boundary.
      returned: always
      type: integer
      sample: null
    presentation_window_duration:
      description:
        - The relative to end sliding window.
      returned: always
      type: integer
      sample: null
    live_backoff_duration:
      description:
        - The relative to end right edge.
      returned: always
      type: integer
      sample: null
    timescale:
      description:
        - The time scale of time stamps.
      returned: always
      type: integer
      sample: null
    force_end_timestamp:
      description:
        - The indicator of forcing existing of end time stamp.
      returned: always
      type: bool
      sample: null
tracks:
  description:
    - The tracks selection conditions.
  returned: always
  type: list
  sample: null
  contains:
    track_selections:
      description:
        - The track selections.
      returned: always
      type: list
      sample: null
      contains:
        property:
          description:
            - The track property type.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The track property value.
          returned: always
          type: str
          sample: null
        operation:
          description:
            - The track property condition operation.
          returned: always
          type: str
          sample: null
bitrate:
  description:
    - The first quality bitrate.
  returned: always
  type: integer
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


class AzureRMAssetFilter(AzureRMModuleBaseExt):
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
            asset_name=dict(
                type='str',
                required=True
            ),
            filter_name=dict(
                type='str',
                required=True
            ),
            presentation_time_range=dict(
                type='dict',
                disposition='/presentation_time_range',
                options=dict(
                    start_timestamp=dict(
                        type='integer',
                        disposition='start_timestamp'
                    ),
                    end_timestamp=dict(
                        type='integer',
                        disposition='end_timestamp'
                    ),
                    presentation_window_duration=dict(
                        type='integer',
                        disposition='presentation_window_duration'
                    ),
                    live_backoff_duration=dict(
                        type='integer',
                        disposition='live_backoff_duration'
                    ),
                    timescale=dict(
                        type='integer',
                        disposition='timescale'
                    ),
                    force_end_timestamp=dict(
                        type='bool',
                        disposition='force_end_timestamp'
                    )
                )
            ),
            tracks=dict(
                type='list',
                disposition='/tracks',
                elements='dict',
                options=dict(
                    track_selections=dict(
                        type='list',
                        disposition='track_selections',
                        required=True,
                        elements='dict',
                        options=dict(
                            property=dict(
                                type='str',
                                disposition='property',
                                choices=['Unknown',
                                         'Type',
                                         'Name',
                                         'Language',
                                         'FourCC',
                                         'Bitrate'],
                                required=True
                            ),
                            value=dict(
                                type='str',
                                disposition='value',
                                required=True
                            ),
                            operation=dict(
                                type='str',
                                disposition='operation',
                                choices=['Equal',
                                         'NotEqual'],
                                required=True
                            )
                        )
                    )
                )
            ),
            bitrate=dict(
                type='integer',
                disposition='/bitrate'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.asset_name = None
        self.filter_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAssetFilter, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.asset_filters.create_or_update(resource_group_name=self.resource_group_name,
                                                                       account_name=self.account_name,
                                                                       asset_name=self.asset_name,
                                                                       filter_name=self.filter_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AssetFilter instance.')
            self.fail('Error creating the AssetFilter instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.asset_filters.delete(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name,
                                                             asset_name=self.asset_name,
                                                             filter_name=self.filter_name)
        except CloudError as e:
            self.log('Error attempting to delete the AssetFilter instance.')
            self.fail('Error deleting the AssetFilter instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.asset_filters.get(resource_group_name=self.resource_group_name,
                                                          account_name=self.account_name,
                                                          asset_name=self.asset_name,
                                                          filter_name=self.filter_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAssetFilter()


if __name__ == '__main__':
    main()
