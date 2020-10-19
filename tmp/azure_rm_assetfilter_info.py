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
module: azure_rm_assetfilter_info
version_added: '2.9'
short_description: Get AssetFilter info.
description:
  - Get info of AssetFilter.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all Asset Filters
      azure_rm_assetfilter_info: 
        account_name: contosomedia
        asset_name: ClimbingMountRainer
        resource_group_name: contoso
        

    - name: Get an Asset Filter by name
      azure_rm_assetfilter_info: 
        account_name: contosomedia
        asset_name: ClimbingMountRainer
        filter_name: assetFilterWithTimeWindowAndTrack
        resource_group_name: contoso
        

'''

RETURN = '''
asset_filters:
  description: >-
    A list of dict results where the key is the name of the AssetFilter and the
    values are the facts for that AssetFilter.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A collection of AssetFilter items.
      returned: always
      type: list
      sample: null
      contains:
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


class AzureRMAssetFilterInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.asset_name = None
        self.filter_name = None

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
        super(AzureRMAssetFilterInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.asset_name is not None and
            self.filter_name is not None):
            self.results['asset_filters'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.asset_name is not None):
            self.results['asset_filters'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.asset_filters.get(resource_group_name=self.resource_group_name,
                                                          account_name=self.account_name,
                                                          asset_name=self.asset_name,
                                                          filter_name=self.filter_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.asset_filters.list(resource_group_name=self.resource_group_name,
                                                           account_name=self.account_name,
                                                           asset_name=self.asset_name)
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
    AzureRMAssetFilterInfo()


if __name__ == '__main__':
    main()
