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
module: azure_rm_liveevent_info
version_added: '2.9'
short_description: Get LiveEvent info.
description:
  - Get info of LiveEvent.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all LiveEvents
      azure_rm_liveevent_info: 
        account_name: slitestmedia10
        resource_group_name: mediaresources
        

    - name: Get a LiveEvent by name
      azure_rm_liveevent_info: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        resource_group_name: mediaresources
        

'''

RETURN = '''
live_events:
  description: >-
    A list of dict results where the key is the name of the LiveEvent and the
    values are the facts for that LiveEvent.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The result of the List Live Event operation.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The Live Event description.
          returned: always
          type: str
          sample: null
        input:
          description:
            - The Live Event input.
          returned: always
          type: dict
          sample: null
          contains:
            streaming_protocol:
              description:
                - >-
                  The streaming protocol for the Live Event.  This is specified
                  at creation time and cannot be updated.
              returned: always
              type: str
              sample: null
            access_control:
              description:
                - The access control for LiveEvent Input.
              returned: always
              type: dict
              sample: null
              contains:
                ip:
                  description:
                    - The IP access control properties.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    allow:
                      description:
                        - The IP allow list.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        name:
                          description:
                            - The friendly name for the IP address range.
                          returned: always
                          type: str
                          sample: null
                        address:
                          description:
                            - The IP address.
                          returned: always
                          type: str
                          sample: null
                        subnet_prefix_length:
                          description:
                            - The subnet mask prefix length (see CIDR notation).
                          returned: always
                          type: integer
                          sample: null
            key_frame_interval_duration:
              description:
                - ISO 8601 timespan duration of the key frame interval duration.
              returned: always
              type: str
              sample: null
            access_token:
              description:
                - >-
                  A UUID in string form to uniquely identify the stream. This
                  can be specified at creation time but cannot be updated.  If
                  omitted, the service will generate a unique value.
              returned: always
              type: str
              sample: null
            endpoints:
              description:
                - The input endpoints for the Live Event.
              returned: always
              type: list
              sample: null
              contains:
                protocol:
                  description:
                    - The endpoint protocol.
                  returned: always
                  type: str
                  sample: null
                url:
                  description:
                    - The endpoint URL.
                  returned: always
                  type: str
                  sample: null
        preview:
          description:
            - The Live Event preview.
          returned: always
          type: dict
          sample: null
          contains:
            endpoints:
              description:
                - The endpoints for preview.
              returned: always
              type: list
              sample: null
              contains:
                protocol:
                  description:
                    - The endpoint protocol.
                  returned: always
                  type: str
                  sample: null
                url:
                  description:
                    - The endpoint URL.
                  returned: always
                  type: str
                  sample: null
            access_control:
              description:
                - The access control for LiveEvent preview.
              returned: always
              type: dict
              sample: null
              contains:
                ip:
                  description:
                    - The IP access control properties.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    allow:
                      description:
                        - The IP allow list.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        name:
                          description:
                            - The friendly name for the IP address range.
                          returned: always
                          type: str
                          sample: null
                        address:
                          description:
                            - The IP address.
                          returned: always
                          type: str
                          sample: null
                        subnet_prefix_length:
                          description:
                            - The subnet mask prefix length (see CIDR notation).
                          returned: always
                          type: integer
                          sample: null
            preview_locator:
              description:
                - >-
                  The identifier of the preview locator in Guid format. 
                  Specifying this at creation time allows the caller to know the
                  preview locator url before the event is created.  If omitted,
                  the service will generate a random identifier.  This value
                  cannot be updated once the live event is created.
              returned: always
              type: str
              sample: null
            streaming_policy_name:
              description:
                - >-
                  The name of streaming policy used for the LiveEvent preview. 
                  This value is specified at creation time and cannot be
                  updated.
              returned: always
              type: str
              sample: null
            alternative_media_id:
              description:
                - >-
                  An Alternative Media Identifier associated with the
                  StreamingLocator created for the preview.  This value is
                  specified at creation time and cannot be updated.  The
                  identifier can be used in the
                  CustomLicenseAcquisitionUrlTemplate or the
                  CustomKeyAcquisitionUrlTemplate of the StreamingPolicy
                  specified in the StreamingPolicyName field.
              returned: always
              type: str
              sample: null
        encoding:
          description:
            - The Live Event encoding.
          returned: always
          type: dict
          sample: null
          contains:
            encoding_type:
              description:
                - >-
                  The encoding type for Live Event. This value is specified at
                  creation time and cannot be updated. When encodingType is set
                  to None, the service simply passes through the incoming video
                  and audio layer(s) to the output. When encodingType is set to
                  Standard or Premium1080p, a live encoder transcodes the
                  incoming stream into multiple bit rates or layers. See
                  https://go.microsoft.com/fwlink/?linkid=2095101 for more
                  information. The encodingType of Basic is obsolete – if
                  specified, the service will treat this as a Standard Live
                  Event.
              returned: always
              type: str
              sample: null
            preset_name:
              description:
                - >-
                  The optional encoding preset name, used when encodingType is
                  not None. This value is specified at creation time and cannot
                  be updated. If the encodingType is set to Standard, then the
                  default preset name is ‘Default720p’. Else if the encodingType
                  is set to Premium1080p, the default preset is ‘Default1080p’.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - The provisioning state of the Live Event.
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - The resource state of the Live Event.
          returned: always
          type: str
          sample: null
        cross_site_access_policies:
          description:
            - The Live Event access policies.
          returned: always
          type: dict
          sample: null
          contains:
            client_access_policy:
              description:
                - The content of clientaccesspolicy.xml used by Silverlight.
              returned: always
              type: str
              sample: null
            cross_domain_policy:
              description:
                - The content of crossdomain.xml used by Silverlight.
              returned: always
              type: str
              sample: null
        use_static_hostname:
          description:
            - >-
              Specifies whether to use a vanity url with the Live Event.  This
              value is specified at creation time and cannot be updated.
          returned: always
          type: bool
          sample: null
        stream_options:
          description:
            - >-
              The options to use for the LiveEvent.  This value is specified at
              creation time and cannot be updated. The valid values for the
              array entry values are 'Default' and 'LowLatency'.
          returned: always
          type: list
          sample: null
        created:
          description:
            - The exact time the Live Event was created.
          returned: always
          type: str
          sample: null
        last_modified:
          description:
            - The exact time the Live Event was last modified.
          returned: always
          type: str
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
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    description:
      description:
        - The Live Event description.
      returned: always
      type: str
      sample: null
    input:
      description:
        - The Live Event input.
      returned: always
      type: dict
      sample: null
      contains:
        streaming_protocol:
          description:
            - >-
              The streaming protocol for the Live Event.  This is specified at
              creation time and cannot be updated.
          returned: always
          type: str
          sample: null
        access_control:
          description:
            - The access control for LiveEvent Input.
          returned: always
          type: dict
          sample: null
          contains:
            ip:
              description:
                - The IP access control properties.
              returned: always
              type: dict
              sample: null
              contains:
                allow:
                  description:
                    - The IP allow list.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - The friendly name for the IP address range.
                      returned: always
                      type: str
                      sample: null
                    address:
                      description:
                        - The IP address.
                      returned: always
                      type: str
                      sample: null
                    subnet_prefix_length:
                      description:
                        - The subnet mask prefix length (see CIDR notation).
                      returned: always
                      type: integer
                      sample: null
        key_frame_interval_duration:
          description:
            - ISO 8601 timespan duration of the key frame interval duration.
          returned: always
          type: str
          sample: null
        access_token:
          description:
            - >-
              A UUID in string form to uniquely identify the stream. This can be
              specified at creation time but cannot be updated.  If omitted, the
              service will generate a unique value.
          returned: always
          type: str
          sample: null
        endpoints:
          description:
            - The input endpoints for the Live Event.
          returned: always
          type: list
          sample: null
          contains:
            protocol:
              description:
                - The endpoint protocol.
              returned: always
              type: str
              sample: null
            url:
              description:
                - The endpoint URL.
              returned: always
              type: str
              sample: null
    preview:
      description:
        - The Live Event preview.
      returned: always
      type: dict
      sample: null
      contains:
        endpoints:
          description:
            - The endpoints for preview.
          returned: always
          type: list
          sample: null
          contains:
            protocol:
              description:
                - The endpoint protocol.
              returned: always
              type: str
              sample: null
            url:
              description:
                - The endpoint URL.
              returned: always
              type: str
              sample: null
        access_control:
          description:
            - The access control for LiveEvent preview.
          returned: always
          type: dict
          sample: null
          contains:
            ip:
              description:
                - The IP access control properties.
              returned: always
              type: dict
              sample: null
              contains:
                allow:
                  description:
                    - The IP allow list.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - The friendly name for the IP address range.
                      returned: always
                      type: str
                      sample: null
                    address:
                      description:
                        - The IP address.
                      returned: always
                      type: str
                      sample: null
                    subnet_prefix_length:
                      description:
                        - The subnet mask prefix length (see CIDR notation).
                      returned: always
                      type: integer
                      sample: null
        preview_locator:
          description:
            - >-
              The identifier of the preview locator in Guid format.  Specifying
              this at creation time allows the caller to know the preview
              locator url before the event is created.  If omitted, the service
              will generate a random identifier.  This value cannot be updated
              once the live event is created.
          returned: always
          type: str
          sample: null
        streaming_policy_name:
          description:
            - >-
              The name of streaming policy used for the LiveEvent preview.  This
              value is specified at creation time and cannot be updated.
          returned: always
          type: str
          sample: null
        alternative_media_id:
          description:
            - >-
              An Alternative Media Identifier associated with the
              StreamingLocator created for the preview.  This value is specified
              at creation time and cannot be updated.  The identifier can be
              used in the CustomLicenseAcquisitionUrlTemplate or the
              CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified
              in the StreamingPolicyName field.
          returned: always
          type: str
          sample: null
    encoding:
      description:
        - The Live Event encoding.
      returned: always
      type: dict
      sample: null
      contains:
        encoding_type:
          description:
            - >-
              The encoding type for Live Event. This value is specified at
              creation time and cannot be updated. When encodingType is set to
              None, the service simply passes through the incoming video and
              audio layer(s) to the output. When encodingType is set to Standard
              or Premium1080p, a live encoder transcodes the incoming stream
              into multiple bit rates or layers. See
              https://go.microsoft.com/fwlink/?linkid=2095101 for more
              information. The encodingType of Basic is obsolete – if specified,
              the service will treat this as a Standard Live Event.
          returned: always
          type: str
          sample: null
        preset_name:
          description:
            - >-
              The optional encoding preset name, used when encodingType is not
              None. This value is specified at creation time and cannot be
              updated. If the encodingType is set to Standard, then the default
              preset name is ‘Default720p’. Else if the encodingType is set to
              Premium1080p, the default preset is ‘Default1080p’.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the Live Event.
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - The resource state of the Live Event.
      returned: always
      type: str
      sample: null
    cross_site_access_policies:
      description:
        - The Live Event access policies.
      returned: always
      type: dict
      sample: null
      contains:
        client_access_policy:
          description:
            - The content of clientaccesspolicy.xml used by Silverlight.
          returned: always
          type: str
          sample: null
        cross_domain_policy:
          description:
            - The content of crossdomain.xml used by Silverlight.
          returned: always
          type: str
          sample: null
    use_static_hostname:
      description:
        - >-
          Specifies whether to use a vanity url with the Live Event.  This value
          is specified at creation time and cannot be updated.
      returned: always
      type: bool
      sample: null
    stream_options:
      description:
        - >-
          The options to use for the LiveEvent.  This value is specified at
          creation time and cannot be updated. The valid values for the array
          entry values are 'Default' and 'LowLatency'.
      returned: always
      type: list
      sample: null
    created:
      description:
        - The exact time the Live Event was created.
      returned: always
      type: str
      sample: null
    last_modified:
      description:
        - The exact time the Live Event was last modified.
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
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLiveEventInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.live_event_name = None

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
        super(AzureRMLiveEventInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.live_event_name is not None):
            self.results['live_events'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['live_events'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.live_events.get(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        live_event_name=self.live_event_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.live_events.list(resource_group_name=self.resource_group_name,
                                                         account_name=self.account_name)
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
    AzureRMLiveEventInfo()


if __name__ == '__main__':
    main()
