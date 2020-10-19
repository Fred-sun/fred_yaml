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
module: azure_rm_liveoutput_info
version_added: '2.9'
short_description: Get LiveOutput info.
description:
  - Get info of LiveOutput.
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
  live_event_name:
    description:
      - The name of the Live Event.
    required: true
    type: str
  live_output_name:
    description:
      - The name of the Live Output.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all LiveOutputs
      azure_rm_liveoutput_info: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        resource_group_name: mediaresources
        

    - name: Get a LiveOutput by name
      azure_rm_liveoutput_info: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        live_output_name: myLiveOutput1
        resource_group_name: mediaresources
        

'''

RETURN = '''
live_outputs:
  description: >-
    A list of dict results where the key is the name of the LiveOutput and the
    values are the facts for that LiveOutput.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The result of the List Live Output operation.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The description of the Live Output.
          returned: always
          type: str
          sample: null
        asset_name:
          description:
            - The asset name.
          returned: always
          type: str
          sample: null
        archive_window_length:
          description:
            - >-
              ISO 8601 timespan duration of the archive window length. This is
              duration that customer want to retain the recorded content.
          returned: always
          type: duration
          sample: null
        manifest_name:
          description:
            - >-
              The manifest file name.  If not provided, the service will
              generate one automatically.
          returned: always
          type: str
          sample: null
        output_snap_time:
          description:
            - The output snapshot time.
          returned: always
          type: integer
          sample: null
        created:
          description:
            - The exact time the Live Output was created.
          returned: always
          type: str
          sample: null
        last_modified:
          description:
            - The exact time the Live Output was last modified.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state of the Live Output.
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - The resource state of the Live Output.
          returned: always
          type: str
          sample: null
        fragments_per_ts_segment:
          description:
            - The amount of fragments per HTTP Live Streaming (HLS) segment.
          returned: always
          type: integer
          sample: null
    odata_count:
      description:
        - The number of result.
      returned: always
      type: integer
      sample: null
    odata_next_link:
      description:
        - >-
          Th link to the next set of results. Not empty if value contains
          incomplete list of Live Outputs.
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
    description:
      description:
        - The description of the Live Output.
      returned: always
      type: str
      sample: null
    asset_name:
      description:
        - The asset name.
      returned: always
      type: str
      sample: null
    archive_window_length:
      description:
        - >-
          ISO 8601 timespan duration of the archive window length. This is
          duration that customer want to retain the recorded content.
      returned: always
      type: duration
      sample: null
    manifest_name:
      description:
        - >-
          The manifest file name.  If not provided, the service will generate
          one automatically.
      returned: always
      type: str
      sample: null
    output_snap_time:
      description:
        - The output snapshot time.
      returned: always
      type: integer
      sample: null
    created:
      description:
        - The exact time the Live Output was created.
      returned: always
      type: str
      sample: null
    last_modified:
      description:
        - The exact time the Live Output was last modified.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the Live Output.
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - The resource state of the Live Output.
      returned: always
      type: str
      sample: null
    fragments_per_ts_segment:
      description:
        - The amount of fragments per HTTP Live Streaming (HLS) segment.
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


class AzureRMLiveOutputInfo(AzureRMModuleBase):
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
            live_event_name=dict(
                type='str',
                required=True
            ),
            live_output_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.live_event_name = None
        self.live_output_name = None

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
        super(AzureRMLiveOutputInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.live_event_name is not None and
            self.live_output_name is not None):
            self.results['live_outputs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.live_event_name is not None):
            self.results['live_outputs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.live_outputs.get(resource_group_name=self.resource_group_name,
                                                         account_name=self.account_name,
                                                         live_event_name=self.live_event_name,
                                                         live_output_name=self.live_output_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.live_outputs.list(resource_group_name=self.resource_group_name,
                                                          account_name=self.account_name,
                                                          live_event_name=self.live_event_name)
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
    AzureRMLiveOutputInfo()


if __name__ == '__main__':
    main()
