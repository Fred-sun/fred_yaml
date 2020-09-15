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
module: azure_rm_liveoutput
version_added: '2.9'
short_description: Manage Azure LiveOutput instance.
description:
  - 'Create, update and delete instance of Azure LiveOutput.'
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
    required: true
    type: str
  description:
    description:
      - The description of the Live Output.
    type: str
  asset_name:
    description:
      - The asset name.
    type: str
  archive_window_length:
    description:
      - >-
        ISO 8601 timespan duration of the archive window length. This is
        duration that customer want to retain the recorded content.
    type: duration
  manifest_name:
    description:
      - >-
        The manifest file name.  If not provided, the service will generate one
        automatically.
    type: str
  output_snap_time:
    description:
      - The output snapshot time.
    type: integer
  fragments_per_ts_segment:
    description:
      - The amount of fragments per HTTP Live Streaming (HLS) segment.
    type: integer
  state:
    description:
      - Assert the state of the LiveOutput.
      - >-
        Use C(present) to create or update an LiveOutput and C(absent) to delete
        it.
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
    - name: Create a LiveOutput
      azure_rm_liveoutput: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        live_output_name: myLiveOutput1
        resource_group_name: mediaresources
        properties:
          description: test live output 1
          archive_window_length: PT5M
          asset_name: 6f3264f5-a189-48b4-a29a-a40f22575212
          hls:
            fragments_per_ts_segment: 5
          manifest_name: testmanifest
        

    - name: Delete a LiveOutput
      azure_rm_liveoutput: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        live_output_name: myLiveOutput1
        resource_group_name: mediaresources
        

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
      ISO 8601 timespan duration of the archive window length. This is duration
      that customer want to retain the recorded content.
  returned: always
  type: duration
  sample: null
manifest_name:
  description:
    - >-
      The manifest file name.  If not provided, the service will generate one
      automatically.
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


class AzureRMLiveOutput(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            asset_name=dict(
                type='str',
                disposition='/asset_name'
            ),
            archive_window_length=dict(
                type='duration',
                disposition='/archive_window_length'
            ),
            manifest_name=dict(
                type='str',
                disposition='/manifest_name'
            ),
            output_snap_time=dict(
                type='integer',
                disposition='/output_snap_time'
            ),
            fragments_per_ts_segment=dict(
                type='integer',
                disposition='/fragments_per_ts_segment'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.live_event_name = None
        self.live_output_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLiveOutput, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.live_outputs.create(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                live_event_name=self.live_event_name,
                                                                live_output_name=self.live_output_name,
                                                                parameters=self.body)
            else:
                response = self.mgmt_client.live_outputs.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LiveOutput instance.')
            self.fail('Error creating the LiveOutput instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.live_outputs.delete(resource_group_name=self.resource_group_name,
                                                            account_name=self.account_name,
                                                            live_event_name=self.live_event_name,
                                                            live_output_name=self.live_output_name)
        except CloudError as e:
            self.log('Error attempting to delete the LiveOutput instance.')
            self.fail('Error deleting the LiveOutput instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.live_outputs.get(resource_group_name=self.resource_group_name,
                                                         account_name=self.account_name,
                                                         live_event_name=self.live_event_name,
                                                         live_output_name=self.live_output_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLiveOutput()


if __name__ == '__main__':
    main()
