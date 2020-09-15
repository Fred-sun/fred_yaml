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
module: azure_rm_liveevent
version_added: '2.9'
short_description: Manage Azure LiveEvent instance.
description:
  - 'Create, update and delete instance of Azure LiveEvent.'
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
  auto_start:
    description:
      - >-
        The flag indicates if the resource should be automatically started on
        creation.
    type: bool
  location:
    description:
      - The geo-location where the resource lives
    type: str
  description:
    description:
      - The Live Event description.
    type: str
  input:
    description:
      - The Live Event input.
    type: dict
    suboptions:
      streaming_protocol:
        description:
          - >-
            The streaming protocol for the Live Event.  This is specified at
            creation time and cannot be updated.
        required: true
        type: str
        choices:
          - FragmentedMP4
          - RTMP
      access_control:
        description:
          - The access control for LiveEvent Input.
        type: dict
        suboptions:
          ip:
            description:
              - The IP access control properties.
            type: dict
            suboptions:
              allow:
                description:
                  - The IP allow list.
                type: list
                suboptions:
                  name:
                    description:
                      - The friendly name for the IP address range.
                    type: str
                  address:
                    description:
                      - The IP address.
                    type: str
                  subnet_prefix_length:
                    description:
                      - The subnet mask prefix length (see CIDR notation).
                    type: integer
      key_frame_interval_duration:
        description:
          - ISO 8601 timespan duration of the key frame interval duration.
        type: str
      access_token:
        description:
          - >-
            A UUID in string form to uniquely identify the stream. This can be
            specified at creation time but cannot be updated.  If omitted, the
            service will generate a unique value.
        type: str
      endpoints:
        description:
          - The input endpoints for the Live Event.
        type: list
        suboptions:
          protocol:
            description:
              - The endpoint protocol.
            type: str
          url:
            description:
              - The endpoint URL.
            type: str
  preview:
    description:
      - The Live Event preview.
    type: dict
    suboptions:
      endpoints:
        description:
          - The endpoints for preview.
        type: list
        suboptions:
          protocol:
            description:
              - The endpoint protocol.
            type: str
          url:
            description:
              - The endpoint URL.
            type: str
      access_control:
        description:
          - The access control for LiveEvent preview.
        type: dict
        suboptions:
          ip:
            description:
              - The IP access control properties.
            type: dict
            suboptions:
              allow:
                description:
                  - The IP allow list.
                type: list
                suboptions:
                  name:
                    description:
                      - The friendly name for the IP address range.
                    type: str
                  address:
                    description:
                      - The IP address.
                    type: str
                  subnet_prefix_length:
                    description:
                      - The subnet mask prefix length (see CIDR notation).
                    type: integer
      preview_locator:
        description:
          - >-
            The identifier of the preview locator in Guid format.  Specifying
            this at creation time allows the caller to know the preview locator
            url before the event is created.  If omitted, the service will
            generate a random identifier.  This value cannot be updated once the
            live event is created.
        type: str
      streaming_policy_name:
        description:
          - >-
            The name of streaming policy used for the LiveEvent preview.  This
            value is specified at creation time and cannot be updated.
        type: str
      alternative_media_id:
        description:
          - >-
            An Alternative Media Identifier associated with the StreamingLocator
            created for the preview.  This value is specified at creation time
            and cannot be updated.  The identifier can be used in the
            CustomLicenseAcquisitionUrlTemplate or the
            CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in
            the StreamingPolicyName field.
        type: str
  encoding:
    description:
      - The Live Event encoding.
    type: dict
    suboptions:
      encoding_type:
        description:
          - >-
            The encoding type for Live Event. This value is specified at
            creation time and cannot be updated. When encodingType is set to
            None, the service simply passes through the incoming video and audio
            layer(s) to the output. When encodingType is set to Standard or
            Premium1080p, a live encoder transcodes the incoming stream into
            multiple bit rates or layers. See
            https://go.microsoft.com/fwlink/?linkid=2095101 for more
            information. The encodingType of Basic is obsolete – if specified,
            the service will treat this as a Standard Live Event.
        type: str
        choices:
          - None
          - Basic
          - Standard
          - Premium1080p
      preset_name:
        description:
          - >-
            The optional encoding preset name, used when encodingType is not
            None. This value is specified at creation time and cannot be
            updated. If the encodingType is set to Standard, then the default
            preset name is ‘Default720p’. Else if the encodingType is set to
            Premium1080p, the default preset is ‘Default1080p’.
        type: str
  cross_site_access_policies:
    description:
      - The Live Event access policies.
    type: dict
    suboptions:
      client_access_policy:
        description:
          - The content of clientaccesspolicy.xml used by Silverlight.
        type: str
      cross_domain_policy:
        description:
          - The content of crossdomain.xml used by Silverlight.
        type: str
  use_static_hostname:
    description:
      - >-
        Specifies whether to use a vanity url with the Live Event.  This value
        is specified at creation time and cannot be updated.
    type: bool
  stream_options:
    description:
      - >-
        The options to use for the LiveEvent.  This value is specified at
        creation time and cannot be updated. The valid values for the array
        entry values are 'Default' and 'LowLatency'.
    type: list
  state:
    description:
      - Assert the state of the LiveEvent.
      - >-
        Use C(present) to create or update an LiveEvent and C(absent) to delete
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
    - name: Create a LiveEvent
      azure_rm_liveevent: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        resource_group_name: mediaresources
        location: West US
        properties:
          description: test event 1
          input:
            key_frame_interval_duration: PT6S
            streaming_protocol: RTMP
          preview:
            access_control:
              ip:
                allow:
                  - name: AllowAll
                    address: 0.0.0.0
                    subnet_prefix_length: 0
        tags:
          tag1: value1
          tag2: value2
        

    - name: Update a LiveEvent
      azure_rm_liveevent: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        resource_group_name: mediaresources
        location: West US
        properties:
          description: test event updated
          input:
            key_frame_interval_duration: PT6S
            streaming_protocol: FragmentedMP4
          preview:
            access_control:
              ip:
                allow:
                  - name: AllowOne
                    address: 192.1.1.0
        tags:
          tag1: value1
          tag2: value2
          tag3: value3
        

    - name: Delete a LiveEvent
      azure_rm_liveevent: 
        account_name: slitestmedia10
        live_event_name: myLiveEvent1
        resource_group_name: mediaresources
        location: West US
        name: myLiveEvent1
        tags:
          dynamic_properties:
            tag1: value1
            tag2: value2
        type: >-
          /subscriptions/0a6ec948-5a62-437d-b9df-934dc7c1b722/resourcegroups/mediaresources/providers/Microsoft.Media/mediaservices/slitestmedia10/liveevents
        id: >-
          /subscriptions/0a6ec948-5a62-437d-b9df-934dc7c1b722/resourceGroups/mediaresources/providers/Microsoft.Media/mediaservices/slitestmedia10/liveevents/myLiveEvent1
        properties:
          created: '2018-03-02T18:25:07.5748853-08:00'
          cross_site_access_policies: {}
          description: test event updated
          encoding:
            encoding_type: None
            preset_name: {}
          input:
            access_token: {}
            endpoints: []
            key_frame_interval_duration: PT6S
            streaming_protocol: FragmentedMP4
          last_modified: '2018-03-02T18:25:07.5748853-08:00'
          preview:
            access_control:
              ip:
                allow:
                  - address: 192.1.1.0
                    name: AllowOne
                    subnet_prefix_length: {}
            endpoints: []
            preview_locator: {}
            streaming_policy_name: {}
          provisioning_state: {}
          resource_state: Stopped
          stream_options: []
          use_static_hostname: false
        

'''

RETURN = '''
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
          The identifier of the preview locator in Guid format.  Specifying this
          at creation time allows the caller to know the preview locator url
          before the event is created.  If omitted, the service will generate a
          random identifier.  This value cannot be updated once the live event
          is created.
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
          An Alternative Media Identifier associated with the StreamingLocator
          created for the preview.  This value is specified at creation time and
          cannot be updated.  The identifier can be used in the
          CustomLicenseAcquisitionUrlTemplate or the
          CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in
          the StreamingPolicyName field.
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
          The encoding type for Live Event. This value is specified at creation
          time and cannot be updated. When encodingType is set to None, the
          service simply passes through the incoming video and audio layer(s) to
          the output. When encodingType is set to Standard or Premium1080p, a
          live encoder transcodes the incoming stream into multiple bit rates or
          layers. See https://go.microsoft.com/fwlink/?linkid=2095101 for more
          information. The encodingType of Basic is obsolete – if specified, the
          service will treat this as a Standard Live Event.
      returned: always
      type: str
      sample: null
    preset_name:
      description:
        - >-
          The optional encoding preset name, used when encodingType is not None.
          This value is specified at creation time and cannot be updated. If the
          encodingType is set to Standard, then the default preset name is
          ‘Default720p’. Else if the encodingType is set to Premium1080p, the
          default preset is ‘Default1080p’.
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
      Specifies whether to use a vanity url with the Live Event.  This value is
      specified at creation time and cannot be updated.
  returned: always
  type: bool
  sample: null
stream_options:
  description:
    - >-
      The options to use for the LiveEvent.  This value is specified at creation
      time and cannot be updated. The valid values for the array entry values
      are 'Default' and 'LowLatency'.
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


class AzureRMLiveEvent(AzureRMModuleBaseExt):
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
            auto_start=dict(
                type='bool'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            input=dict(
                type='dict',
                disposition='/input',
                options=dict(
                    streaming_protocol=dict(
                        type='str',
                        disposition='streaming_protocol',
                        choices=['FragmentedMP4',
                                 'RTMP'],
                        required=True
                    ),
                    access_control=dict(
                        type='dict',
                        disposition='access_control',
                        options=dict(
                            ip=dict(
                                type='dict',
                                disposition='ip',
                                options=dict(
                                    allow=dict(
                                        type='list',
                                        disposition='allow',
                                        elements='dict',
                                        options=dict(
                                            name=dict(
                                                type='str',
                                                disposition='name'
                                            ),
                                            address=dict(
                                                type='str',
                                                disposition='address'
                                            ),
                                            subnet_prefix_length=dict(
                                                type='integer',
                                                disposition='subnet_prefix_length'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    key_frame_interval_duration=dict(
                        type='str',
                        disposition='key_frame_interval_duration'
                    ),
                    access_token=dict(
                        type='str',
                        disposition='access_token'
                    ),
                    endpoints=dict(
                        type='list',
                        disposition='endpoints',
                        elements='dict',
                        options=dict(
                            protocol=dict(
                                type='str',
                                disposition='protocol'
                            ),
                            url=dict(
                                type='str',
                                disposition='url'
                            )
                        )
                    )
                )
            ),
            preview=dict(
                type='dict',
                disposition='/preview',
                options=dict(
                    endpoints=dict(
                        type='list',
                        disposition='endpoints',
                        elements='dict',
                        options=dict(
                            protocol=dict(
                                type='str',
                                disposition='protocol'
                            ),
                            url=dict(
                                type='str',
                                disposition='url'
                            )
                        )
                    ),
                    access_control=dict(
                        type='dict',
                        disposition='access_control',
                        options=dict(
                            ip=dict(
                                type='dict',
                                disposition='ip',
                                options=dict(
                                    allow=dict(
                                        type='list',
                                        disposition='allow',
                                        elements='dict',
                                        options=dict(
                                            name=dict(
                                                type='str',
                                                disposition='name'
                                            ),
                                            address=dict(
                                                type='str',
                                                disposition='address'
                                            ),
                                            subnet_prefix_length=dict(
                                                type='integer',
                                                disposition='subnet_prefix_length'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    preview_locator=dict(
                        type='str',
                        disposition='preview_locator'
                    ),
                    streaming_policy_name=dict(
                        type='str',
                        disposition='streaming_policy_name'
                    ),
                    alternative_media_id=dict(
                        type='str',
                        disposition='alternative_media_id'
                    )
                )
            ),
            encoding=dict(
                type='dict',
                disposition='/encoding',
                options=dict(
                    encoding_type=dict(
                        type='str',
                        disposition='encoding_type',
                        choices=['None',
                                 'Basic',
                                 'Standard',
                                 'Premium1080p']
                    ),
                    preset_name=dict(
                        type='str',
                        disposition='preset_name'
                    )
                )
            ),
            cross_site_access_policies=dict(
                type='dict',
                disposition='/cross_site_access_policies',
                options=dict(
                    client_access_policy=dict(
                        type='str',
                        disposition='client_access_policy'
                    ),
                    cross_domain_policy=dict(
                        type='str',
                        disposition='cross_domain_policy'
                    )
                )
            ),
            use_static_hostname=dict(
                type='bool',
                disposition='/use_static_hostname'
            ),
            stream_options=dict(
                type='list',
                disposition='/stream_options',
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
        self.live_event_name = None
        self.auto_start = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLiveEvent, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.live_events.create(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               live_event_name=self.live_event_name,
                                                               auto_start=self.auto_start,
                                                               parameters=self.body)
            else:
                response = self.mgmt_client.live_events.update(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               live_event_name=self.live_event_name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LiveEvent instance.')
            self.fail('Error creating the LiveEvent instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.live_events.delete(resource_group_name=self.resource_group_name,
                                                           account_name=self.account_name,
                                                           live_event_name=self.live_event_name)
        except CloudError as e:
            self.log('Error attempting to delete the LiveEvent instance.')
            self.fail('Error deleting the LiveEvent instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.live_events.get(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        live_event_name=self.live_event_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLiveEvent()


if __name__ == '__main__':
    main()
